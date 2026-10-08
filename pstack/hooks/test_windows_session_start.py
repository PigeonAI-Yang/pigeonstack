import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import textwrap
import unittest


HOOKS = Path(__file__).resolve().parent
WRAPPER = HOOKS / 'windows_session_start.ps1'
POWERSHELL = shutil.which('powershell.exe') or r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'


@unittest.skipUnless(os.name == 'nt', 'the wrapper requires Windows PowerShell')
class WindowsSessionStartTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='pstack-hook-test-')
        self.root = Path(self.temp.name)
        self.hooks = self.root / 'hooks'
        self.hooks.mkdir()
        shutil.copyfile(WRAPPER, self.hooks / WRAPPER.name)

    def tearDown(self):
        self.temp.cleanup()

    def environment(self):
        env = os.environ.copy()
        env['PLUGIN_ROOT'] = str(self.root)
        env['CLAUDE_PLUGIN_ROOT'] = str(self.root)
        env['PSTACK_WINDOWS_TEST_SENTINEL'] = 'unchanged-value'
        env['PYTHONDONTWRITEBYTECODE'] = '0'
        env['PYTHONIOENCODING'] = 'latin-1'
        return env

    def add_reader(self, source):
        (self.hooks / 'session_start.py').write_text(textwrap.dedent(source), encoding='utf-8')

    def run_wrapper(self, payload=b'{}', env=None, wrapper=None):
        completed = subprocess.run(
            [POWERSHELL, '-NoLogo', '-NoProfile', '-NonInteractive', '-File', str(wrapper or self.hooks / WRAPPER.name)],
            input=payload,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=str(self.root),
            env=env or self.environment(),
            timeout=15,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr.decode('utf-8', errors='replace'))
        self.assertEqual(completed.stderr, b'')
        self.assertLessEqual(len(completed.stdout), 32768)
        return completed.stdout

    def read_diagnostic(self, output):
        result = json.loads(output)
        self.assertEqual(set(result), {'systemMessage'})
        message = result['systemMessage']
        marker = ' Untrusted observation data: '
        self.assertIn(marker, message)
        return result, json.loads(message.split(marker, 1)[1])

    def test_forwards_valid_reader_json_byte_for_byte_and_preserves_environment(self):
        payload = b'{"permission_mode":"plan","event":"synthetic-only","value":"\xc3\xa9"}'
        source = '''
            import hashlib
            import json
            import os
            import sys

            raw = sys.stdin.buffer.read()
            result = {
                'digest': hashlib.sha256(raw).hexdigest(),
                'length': len(raw),
                'plugin_root': os.environ.get('PLUGIN_ROOT'),
                'claude_plugin_root': os.environ.get('CLAUDE_PLUGIN_ROOT'),
                'sentinel': os.environ.get('PSTACK_WINDOWS_TEST_SENTINEL'),
                'dontwritebytecode': os.environ.get('PYTHONDONTWRITEBYTECODE'),
                'ioencoding': os.environ.get('PYTHONIOENCODING'),
            }
            sys.stdout.buffer.write((json.dumps(result, separators=(',', ':')) + '\\n').encode('utf-8'))
        '''
        self.add_reader(source)
        result = self.run_wrapper(payload=payload)
        expected = {
            'digest': hashlib.sha256(payload).hexdigest(),
            'length': len(payload),
            'plugin_root': str(self.root),
            'claude_plugin_root': str(self.root),
            'sentinel': 'unchanged-value',
            'dontwritebytecode': '1',
            'ioencoding': 'utf-8',
        }
        self.assertEqual(result, (json.dumps(expected, separators=(',', ':')) + '\n').encode('utf-8'))

    def test_runs_the_real_reader_and_forwards_its_no_context_json(self):
        workspace = self.root / 'empty-workspace'
        workspace.mkdir()
        env = self.environment()
        env['PLUGIN_ROOT'] = str(HOOKS.parent)
        env['CLAUDE_PLUGIN_ROOT'] = str(HOOKS.parent)
        event = {
            'session_id': 'synthetic-session',
            'cwd': str(workspace),
            'hook_event_name': 'SessionStart',
            'source': 'startup',
            'transcript_path': None,
            'model': 'synthetic-model',
            'permission_mode': 'plan',
        }
        result = self.run_wrapper(payload=json.dumps(event).encode('utf-8'), env=env, wrapper=WRAPPER)
        self.assertEqual(
            result,
            b'{"systemMessage": "Pstack context not loaded: FileNotFoundError. Session continues."}\n',
        )

    def test_reports_reader_exit_and_bounded_stderr(self):
        self.add_reader('''
            import sys
            sys.stdin.buffer.read()
            sys.stderr.buffer.write(b'fixture stderr sentinel\\n' + (b'x' * 3000))
            sys.exit(1)
        ''')
        output = self.run_wrapper(payload=b'{"synthetic":true}')
        result, diagnostic = self.read_diagnostic(output)
        self.assertIn('original exit 1', result['systemMessage'])
        self.assertIn('untrusted observation data', result['systemMessage'].lower())
        self.assertEqual(diagnostic['error_type'], 'ReaderExitNonZero')
        self.assertEqual(diagnostic['original_exit'], 1)
        self.assertTrue(diagnostic['stderr'].startswith('fixture stderr sentinel'))
        self.assertLessEqual(len(diagnostic['stderr']), 2048)
        self.assertTrue(diagnostic['stderr_truncated'])

    def test_reports_malformed_stdout(self):
        self.add_reader('''
            import sys
            sys.stdin.buffer.read()
            sys.stdout.buffer.write(b'not json')
        ''')
        result, diagnostic = self.read_diagnostic(self.run_wrapper(payload=b'{"synthetic":true}'))
        self.assertIn('original exit 0', result['systemMessage'])
        self.assertEqual(diagnostic['error_type'], 'MalformedStdout')
        self.assertTrue(diagnostic['script_exists'])

    def test_reports_oversized_stdout_without_forwarding_it(self):
        self.add_reader('''
            import sys
            sys.stdin.buffer.read()
            sys.stdout.buffer.write(b'{' + (b' ' * 40000) + b'}')
        ''')
        output = self.run_wrapper(payload=b'{"synthetic":true}')
        result, diagnostic = self.read_diagnostic(output)
        self.assertEqual(diagnostic['error_type'], 'StdoutTooLarge')

    def test_reports_missing_reader_script(self):
        result, diagnostic = self.read_diagnostic(self.run_wrapper(payload=b'{"synthetic":true}'))
        self.assertEqual(diagnostic['error_type'], 'ReaderScriptMissing')
        self.assertFalse(diagnostic['script_exists'])
        self.assertIn('original exit unavailable', result['systemMessage'])

    def test_reports_missing_python_launcher(self):
        self.add_reader('import sys\nsys.stdout.write("{}")\n')
        env = self.environment()
        empty_path = self.root / 'empty-path'
        empty_path.mkdir()
        env['PATH'] = str(empty_path)
        result, diagnostic = self.read_diagnostic(self.run_wrapper(payload=b'{"synthetic":true}', env=env))
        self.assertEqual(diagnostic['error_type'], 'PythonLauncherNotFound')
        self.assertIsNone(diagnostic['py_path'])
        self.assertTrue(diagnostic['plugin_root']['present'])
        self.assertTrue(diagnostic['plugin_root']['matches'])
        self.assertTrue(diagnostic['claude_plugin_root']['present'])
        self.assertTrue(diagnostic['claude_plugin_root']['matches'])


if __name__ == '__main__':
    unittest.main()
