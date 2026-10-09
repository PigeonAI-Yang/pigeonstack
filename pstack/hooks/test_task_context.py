import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest


ROOT = Path(__file__).resolve().parents[2]
HELPER = ROOT / 'pstack/hooks/task_context.py'
ANCHOR = 'main-checkpoint'
START = ('<!-- pstack-current:' + ANCHOR + ':start -->').encode('ascii')
END = ('<!-- pstack-current:' + ANCHOR + ':end -->').encode('ascii')
ARCHIVE_BODY_HEADER = b'## Archived current body\n\n'
MAX_BODY_BYTES = 16384


def digest(content):
    return hashlib.sha256(content).hexdigest()


def record_content(body, prefix=b'# Task record\n', suffix=b'# History\nOlder evidence.\n',
                   line_ending=b'\n'):
    return (prefix + START + line_ending + body + END + line_ending + suffix)


class TaskContextTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='pstack-task-context-')
        self.workspace = Path(self.temporary.name)
        self.record = self.workspace / 'TASKS.md'
        self.archive = self.workspace / 'archive'
        self.archive.mkdir()
        self.original_body = b'# Current checkpoint\nAccepted: keep the source.\n'
        self.prefix = b'# Task record\n'
        self.suffix = b'# History\nOlder evidence.\n'
        self.write_record(self.original_body)

    def tearDown(self):
        self.temporary.cleanup()

    def write_record(self, body, prefix=None, suffix=None, line_ending=b'\n'):
        content = record_content(
            body,
            self.prefix if prefix is None else prefix,
            self.suffix if suffix is None else suffix,
            line_ending,
        )
        self.record.write_bytes(content)
        return content

    def run_cli(self, *arguments, runner=None, timeout=10):
        command = [sys.executable, str(runner or HELPER), *map(str, arguments)]
        result = subprocess.run(command, capture_output=True, timeout=timeout)
        self.assertTrue(result.stdout, result.stderr.decode(errors='replace'))
        return result, json.loads(result.stdout.decode('utf-8'))

    def read(self):
        return self.run_cli(
            'read', '--workspace', str(self.workspace), '--record', 'TASKS.md',
            '--anchor', ANCHOR,
        )

    def body_file(self, content, name='new-current.md'):
        path = self.workspace / name
        path.write_bytes(content)
        return path

    def update(self, expected, body_path, *extra, runner=None):
        return self.run_cli(
            'update', '--workspace', str(self.workspace), '--record', 'TASKS.md',
            '--anchor', ANCHOR, '--expected-sha256', expected,
            '--body-file', str(body_path), '--archive-dir', 'archive',
            *extra, runner=runner,
        )

    def marker_span(self, content):
        start = content.index(START) + len(START)
        if content[start:start + 2] == b'\r\n':
            start += 2
        elif content[start:start + 1] == b'\n':
            start += 1
        else:
            raise AssertionError('start marker is not a standalone line')
        end = content.index(END)
        return start, end

    def archive_body(self, path):
        content = path.read_bytes()
        start = content.index(ARCHIVE_BODY_HEADER) + len(ARCHIVE_BODY_HEADER)
        return content, content[start:]

    def fault_runner(self, mode):
        runner = self.workspace / ('fault-' + mode + '.py')
        runner.write_text(
            'import importlib.util, sys\n'
            'sys.dont_write_bytecode = True\n'
            'spec = importlib.util.spec_from_file_location("task_context", '
            + repr(str(HELPER)) + ')\n'
            'module = importlib.util.module_from_spec(spec)\n'
            'sys.modules[spec.name] = module\n'
            'spec.loader.exec_module(module)\n'
            'mode = ' + repr(mode) + '\n'
            'args = sys.argv[1:]\n'
            'parsed = module.build_parser().parse_args(args)\n'
            'def fail(*unused, **unused_keywords):\n'
            '    raise OSError("injected test failure")\n'
            'if mode == "archive":\n'
            '    module.publish_archive = fail\n'
            'elif mode == "after-archive":\n'
            '    module.write_candidate_temp = fail\n'
            'elif mode == "readback":\n'
            '    module.readback_record = fail\n'
            'elif mode == "drift":\n'
            '    original = module.snapshot_record\n'
            '    calls = [0]\n'
            '    def changed(root, record):\n'
            '        calls[0] += 1\n'
            '        if calls[0] == 2:\n'
            '            target = module.session_start.selected_record(root, record)\n'
            '            target.write_bytes(target.read_bytes() + b"\\nexternal change\\n")\n'
            '        return original(root, record)\n'
            '    module.snapshot_record = changed\n'
            'sys.argv = [str(' + repr(str(HELPER)) + '), *args]\n'
            'sys.exit(module.main())\n',
            encoding='utf-8',
        )
        return runner

    def test_read_reports_text_hash_sizes_and_soft_warning(self):
        body = b'x' * 8193 + b'\n'
        content = self.write_record(body)
        result, output = self.read()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output['status'], 'ok')
        self.assertEqual(output['current_text'], body.decode('utf-8'))
        self.assertEqual(output['record_sha256'], digest(content))
        self.assertEqual(output['record_bytes'], len(content))
        self.assertEqual(output['current_bytes'], len(body))
        self.assertEqual(output['anchor'], ANCHOR)
        self.assertIn('soft maintenance target', output['warning'])
        self.assertEqual(self.record.read_bytes(), content)

    def test_read_oversized_current_omits_text_and_update_archives_all_bytes(self):
        old_body = b'x' * (22424 - 1) + b'\n'
        original = self.write_record(old_body)
        result, output = self.read()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(output['status'], 'current_oversized')
        self.assertNotIn('current_text', output)
        self.assertEqual(output['current_bytes'], len(old_body))
        self.assertEqual(output['record_sha256'], digest(original))
        new_body = '# Revised checkpoint\n证据仍在原记录中。\n'.encode('utf-8')
        result, output = self.update(digest(original), self.body_file(new_body))
        self.assertEqual(output['status'], 'updated', output)
        archive_path = self.workspace / output['archive']
        archive, archived_body = self.archive_body(archive_path)
        metadata_start = archive.index(b'\n{\n') + 1
        metadata_end = archive.index(b'\n}\n\x60\x60\x60\n\n')
        metadata = json.loads(archive[metadata_start:metadata_end + 2].decode('utf-8'))
        self.assertEqual(archived_body, old_body)
        self.assertEqual(metadata['source_record'], 'TASKS.md')
        self.assertEqual(metadata['anchor'], ANCHOR)
        self.assertEqual(metadata['preimage_sha256'], digest(original))
        self.assertEqual(metadata['old_body_bytes'], len(old_body))
        self.assertEqual(metadata['old_body_sha256'], digest(old_body))
        self.assertEqual(output['archived_body_sha256'], digest(old_body))
        self.assertEqual(output['previous_sha256'], digest(original))
        self.assertEqual(output['current_sha256'], digest(self.record.read_bytes()))
        updated = self.record.read_bytes()
        start, end = self.marker_span(updated)
        self.assertEqual(updated[start:end], new_body)

    def test_update_preserves_bom_crlf_chinese_and_bytes_outside_current(self):
        prefix = b'\xef\xbb\xbf' + '# 中文标题\r\n保留此前缀。\r\n'.encode('utf-8')
        suffix = '\r\n# Historical evidence\r\n原样保留。\r\n'.encode('utf-8')
        old_body = '# Current\r\nAccepted: 原文。\r\n'.encode('utf-8')
        original = self.write_record(old_body, prefix, suffix, b'\r\n')
        new_body = '# 更新检查点\r\nPending: 保留未验收状态。\r\n'.encode('utf-8')
        result, output = self.update(digest(original), self.body_file(new_body))
        self.assertEqual(output['status'], 'updated', output)
        updated = self.record.read_bytes()
        start, end = self.marker_span(updated)
        old_start, old_end = self.marker_span(original)
        self.assertEqual(updated[:start], original[:old_start])
        self.assertEqual(updated[end:], original[old_end:])
        self.assertEqual(updated[start:end], new_body)
        archive, archived_body = self.archive_body(self.workspace / output['archive'])
        self.assertEqual(archived_body, old_body)
        self.assertNotIn(b'pstack-current:', archive)

    def test_update_stale_suffix_creates_no_archive(self):
        original = self.record.read_bytes()
        expected = digest(original)
        changed = original + b'\nConcurrent suffix change.\n'
        self.record.write_bytes(changed)
        result, output = self.update(expected, self.body_file(b'# New current\n'))
        self.assertEqual(output['status'], 'stale_revision', output)
        self.assertEqual(self.record.read_bytes(), changed)
        self.assertEqual(list(self.archive.iterdir()), [])

    def test_new_body_boundary_and_invalid_inputs(self):
        accepted = b'a' * (MAX_BODY_BYTES - 1) + b'\n'
        original = self.record.read_bytes()
        result, output = self.update(digest(original), self.body_file(accepted))
        self.assertEqual(output['status'], 'updated', output)
        self.assertEqual(len(self.record.read_bytes()), len(original) - len(self.original_body) + len(accepted))
        result, output = self.read()
        self.assertEqual(output['status'], 'ok', output)
        self.assertEqual(output['current_bytes'], MAX_BODY_BYTES)
        self.assertEqual(len(output['current_text'].encode('utf-8')), MAX_BODY_BYTES)
        for path in self.archive.iterdir():
            path.unlink()
        for invalid in (
            b'a' * MAX_BODY_BYTES + b'\n',
            b'',
            b'\xff\n',
            b'body without newline',
        ):
            with self.subTest(size=len(invalid), content=invalid[:12]):
                self.write_record(self.original_body)
                original = self.record.read_bytes()
                result, output = self.update(digest(original), self.body_file(invalid))
                self.assertEqual(output['status'], 'error', output)
                self.assertEqual(self.record.read_bytes(), original)
                self.assertEqual(list(self.archive.iterdir()), [])

    def test_no_op_does_not_create_archive(self):
        original = self.record.read_bytes()
        result, output = self.update(digest(original), self.body_file(self.original_body))
        self.assertEqual(output['status'], 'unchanged', output)
        self.assertEqual(self.record.read_bytes(), original)
        self.assertEqual(list(self.archive.iterdir()), [])

    def test_marker_errors_and_record_scan_limit_are_rejected(self):
        valid = self.record.read_bytes()
        cases = {
            'missing': valid.replace(START, b'<!-- missing -->'),
            'duplicate': valid.replace(START + b'\n', START + b'\n' + START + b'\n'),
            'reordered': self.prefix + END + b'\n' + self.original_body + START + b'\n',
            'inline': self.prefix + b'inline ' + START + b'\nbody\n' + END + b'\n',
        }
        for name, content in cases.items():
            with self.subTest(name=name):
                self.record.write_bytes(content)
                result, output = self.read()
                self.assertEqual(output['status'], 'error', output)
        self.record.write_bytes(valid + b'x' * (2097152 + 1 - len(valid)))
        result, output = self.read()
        self.assertEqual(output['status'], 'error', output)
        self.assertIn('2097152-byte scan limit', output['error'])

    def test_archive_failure_leaves_record_and_archive_directory_unchanged(self):
        original = self.record.read_bytes()
        runner = self.fault_runner('archive')
        result, output = self.update(
            digest(original), self.body_file(b'# New current\n'), runner=runner,
        )
        self.assertEqual(output['status'], 'archive_failed', output)
        self.assertEqual(self.record.read_bytes(), original)
        self.assertEqual(list(self.archive.iterdir()), [])

    def test_after_archive_interruption_leaves_recoverable_archive(self):
        original = self.record.read_bytes()
        runner = self.fault_runner('after-archive')
        result, output = self.update(
            digest(original), self.body_file(b'# New current\n'), runner=runner,
        )
        self.assertEqual(output['status'], 'update_failed', output)
        self.assertEqual(self.record.read_bytes(), original)
        self.assertEqual(len(list(self.archive.glob('*.md'))), 1)
        archive, old_body = self.archive_body(self.workspace / output['archive'])
        self.assertEqual(old_body, self.original_body)

    def test_pre_replace_drift_keeps_archive_and_does_not_replace(self):
        original = self.record.read_bytes()
        runner = self.fault_runner('drift')
        result, output = self.update(
            digest(original), self.body_file(b'# New current\n'), runner=runner,
        )
        self.assertEqual(output['status'], 'stale_revision', output)
        self.assertIn('archive', output)
        self.assertEqual(len(list(self.archive.glob('*.md'))), 1)
        self.assertNotIn(b'# New current\n', self.record.read_bytes())
        archive, old_body = self.archive_body(self.workspace / output['archive'])
        self.assertEqual(old_body, self.original_body)

    def test_post_replace_missing_receipt_reports_uncertain_commit(self):
        original = self.record.read_bytes()
        new_body = b'# New current\n'
        runner = self.fault_runner('readback')
        result, output = self.update(digest(original), self.body_file(new_body), runner=runner)
        self.assertEqual(output['status'], 'verification_failed', output)
        self.assertTrue(output['committed_uncertain'])
        updated = self.record.read_bytes()
        start, end = self.marker_span(updated)
        self.assertEqual(updated[start:end], new_body)
        self.assertEqual(len(list(self.archive.glob('*.md'))), 1)

    def test_terminated_lock_holder_releases_record_lock(self):
        original = self.record.read_bytes()
        marker = self.workspace / 'lock-held'
        holder_script = self.workspace / 'lock-holder.py'
        holder_script.write_text(
            'import importlib.util, sys\n'
            'sys.dont_write_bytecode = True\n'
            'spec = importlib.util.spec_from_file_location("task_context", '
            + repr(str(HELPER)) + ')\n'
            'module = importlib.util.module_from_spec(spec)\n'
            'sys.modules[spec.name] = module\n'
            'spec.loader.exec_module(module)\n'
            'with module.record_lock(__import__("pathlib").Path(sys.argv[1])):\n'
            '    __import__("pathlib").Path(sys.argv[2]).write_text("ready", encoding="utf-8")\n'
            '    sys.stdin.read()\n',
            encoding='utf-8',
        )
        lock_path = self.workspace / ('TASKS.md' + '.pstack.lock')
        holder = subprocess.Popen(
            [sys.executable, str(holder_script), str(lock_path), str(marker)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        try:
            deadline = time.monotonic() + 8
            while time.monotonic() < deadline and not marker.exists():
                if holder.poll() is not None:
                    break
                time.sleep(0.01)
            self.assertTrue(marker.exists(), 'lock holder did not acquire the lock')
            result, output = self.update(digest(original), self.body_file(b'# New current\n'))
            self.assertEqual(output['status'], 'locked', output)
            self.assertEqual(self.record.read_bytes(), original)
            self.assertEqual(list(self.archive.iterdir()), [])
        finally:
            holder.terminate()
            holder.wait(timeout=5)
            if holder.stdin:
                holder.stdin.close()
            if holder.stdout:
                holder.stdout.close()
            if holder.stderr:
                holder.stderr.close()
        result, output = self.update(digest(original), self.body_file(b'# New current\n'))
        self.assertEqual(output['status'], 'updated', output)
        self.assertEqual(lock_path.stat().st_size, 1)


if __name__ == '__main__':
    unittest.main()
