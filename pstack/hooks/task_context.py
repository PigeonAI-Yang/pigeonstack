import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import errno
import hashlib
import json
import os
from pathlib import Path, PureWindowsPath
import re
import secrets
import stat
import sys
import tempfile


sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import session_start


MAX_RECORD_BYTES = session_start.MAX_SCAN_BYTES
MAX_CURRENT_BYTES = session_start.MAX_SECTION_BYTES
MAX_BODY_BYTES = session_start.MAX_SECTION_BYTES
SOFT_TARGET_BYTES = 8192
LOCK_SUFFIX = '.pstack.lock'
ARCHIVE_BODY_HEADER = b'## Archived current body\n\n'
SHA256_PATTERN = re.compile(r'[0-9a-fA-F]{64}')


class TaskContextError(Exception):
    pass


class LockUnavailable(Exception):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest()


def workspace_root(value):
    session_start.normalized_workspace(value)
    root = Path(value)
    if not root.is_dir():
        raise TaskContextError('workspace must be an existing absolute local directory')
    return root.resolve(strict=True)


def validate_anchor(anchor):
    if not isinstance(anchor, str) or not re.fullmatch(r'[a-z][a-z0-9-]{0,63}', anchor):
        raise TaskContextError('anchor must match [a-z][a-z0-9-]{0,63}')
    return anchor


def confined_directory(root, selection):
    if not isinstance(selection, str) or not selection or '\x00' in selection:
        raise TaskContextError('archive directory must be a nonempty relative path')
    if len(selection) > 1024:
        raise TaskContextError('archive directory exceeds 1024 characters')
    windows = PureWindowsPath(selection)
    relative = Path(selection.replace('\\', '/'))
    parts = selection.replace('\\', '/').split('/')
    if (windows.drive or windows.root or relative.is_absolute()
            or any(part in {'', '..', '.'} or ':' in part for part in parts)):
        raise TaskContextError('archive directory must be confined within the workspace')
    path = root / relative
    resolved = path.resolve(strict=True)
    if not resolved.is_relative_to(root):
        raise TaskContextError('archive directory resolves outside workspace')
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        info = cursor.lstat()
        if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
            raise TaskContextError('archive directory contains a symlink or reparse point')
    if not resolved.is_dir():
        raise TaskContextError('archive directory must be an existing directory')
    return resolved


def regular_file(path, label):
    info = path.lstat()
    if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
        raise TaskContextError(label + ' must not be a symlink or reparse point')
    if not stat.S_ISREG(info.st_mode):
        raise TaskContextError(label + ' must be a regular file')
    return info


def read_body_file(selection):
    path = Path(selection)
    info = regular_file(path, 'body file')
    resolved = path.resolve(strict=True)
    with path.open('rb') as stream:
        before = os.fstat(stream.fileno())
        if not stat.S_ISREG(before.st_mode):
            raise TaskContextError('body file must be a regular file')
        content = stream.read(MAX_BODY_BYTES + 1)
        after = os.fstat(stream.fileno())
    current = resolved.stat()
    if (session_start.identity(before) != session_start.identity(after)
            or session_start.identity(after) != session_start.identity(current)
            or session_start.identity(info) != session_start.identity(current)):
        raise TaskContextError('body file changed during read')
    if len(content) > MAX_BODY_BYTES:
        raise TaskContextError('body file exceeds 16384 bytes')
    try:
        text = content.decode('utf-8')
    except UnicodeDecodeError:
        raise TaskContextError('body file must be valid UTF-8') from None
    if not content or not text.strip():
        raise TaskContextError('body file must be nonempty')
    if not content.endswith(b'\n'):
        raise TaskContextError('body file must end with LF')
    return resolved, content


def lock_path_for(record_path):
    return record_path.with_name(record_path.name + LOCK_SUFFIX)


def same_file(left, right):
    try:
        return os.path.samefile(left, right)
    except OSError:
        return False


def reject_body_alias(body_path, record_path, archive_dir, lock_path):
    if (same_file(body_path, record_path) or same_file(body_path, lock_path)
            or body_path == record_path or body_path == lock_path):
        raise TaskContextError('body file must not alias the record or record lock')
    if body_path.is_relative_to(archive_dir):
        raise TaskContextError('body file must not be inside the archive directory')


def lock_is_busy(error):
    return (error.errno in {errno.EACCES, errno.EAGAIN, errno.EDEADLK, errno.EWOULDBLOCK}
            or getattr(error, 'winerror', None) in {33, 36})


@contextmanager
def record_lock(lock_path):
    try:
        regular_file(lock_path, 'record lock')
    except FileNotFoundError:
        pass
    flags = os.O_CREAT | os.O_RDWR
    if hasattr(os, 'O_BINARY'):
        flags |= os.O_BINARY
    if hasattr(os, 'O_NOFOLLOW'):
        flags |= os.O_NOFOLLOW
    descriptor = os.open(lock_path, flags, 0o600)
    acquired = False
    try:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode):
            raise TaskContextError('record lock must be a regular file')
        if info.st_size == 0:
            os.lseek(descriptor, 0, os.SEEK_SET)
            os.write(descriptor, b'\0')
            os.fsync(descriptor)
        elif info.st_size != 1:
            raise TaskContextError('record lock must contain exactly one byte')
        os.lseek(descriptor, 0, os.SEEK_SET)
        if os.name == 'nt':
            import msvcrt

            try:
                msvcrt.locking(descriptor, msvcrt.LK_NBLCK, 1)
            except OSError as error:
                if lock_is_busy(error):
                    raise LockUnavailable from None
                raise
        else:
            import fcntl

            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError as error:
                if lock_is_busy(error):
                    raise LockUnavailable from None
                raise
        acquired = True
        yield lock_path
    finally:
        if acquired:
            try:
                os.lseek(descriptor, 0, os.SEEK_SET)
                if os.name == 'nt':
                    import msvcrt

                    msvcrt.locking(descriptor, msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl

                    fcntl.flock(descriptor, fcntl.LOCK_UN)
            finally:
                os.close(descriptor)
        else:
            os.close(descriptor)


def snapshot_record(root, record):
    return session_start.read_snapshot(root, record, MAX_RECORD_BYTES, complete=True)


def readback_record(root, record):
    return snapshot_record(root, record)


def current_bytes(content, anchor):
    start, end = session_start.current_span(content, anchor)
    return content[start:end]


def read_task(workspace, record, anchor):
    root = workspace_root(workspace)
    validate_anchor(anchor)
    content, _ = snapshot_record(root, record)
    body = current_bytes(content, anchor)
    result = {
        'status': 'ok',
        'record_path': record.replace('\\', '/'),
        'anchor': anchor,
        'record_bytes': len(content),
        'current_bytes': len(body),
        'record_sha256': digest(content),
    }
    if len(body) > MAX_CURRENT_BYTES:
        result['status'] = 'current_oversized'
        return result
    result['current_text'] = session_start.current_section(content, anchor)
    if len(body) > SOFT_TARGET_BYTES:
        result['warning'] = 'current section exceeds the 8192-byte soft maintenance target'
    return result


def archive_payload(record, anchor, preimage_sha256, old_body):
    metadata = {
        'source_record': record.replace('\\', '/'),
        'anchor': anchor,
        'preimage_sha256': preimage_sha256,
        'old_body_bytes': len(old_body),
        'old_body_sha256': digest(old_body),
    }
    encoded = json.dumps(metadata, ensure_ascii=False, indent=2).encode('utf-8')
    return (b'# Historical checkpoint\n\n' + b'\x60\x60\x60json\n' + encoded
            + b'\n\x60\x60\x60\n\n' + ARCHIVE_BODY_HEADER + old_body)


def publish_archive(archive_dir, record, anchor, preimage_sha256, old_body):
    temporary = None
    try:
        descriptor, name = tempfile.mkstemp(prefix='.pstack-checkpoint-', suffix='.tmp',
                                            dir=archive_dir)
        temporary = Path(name)
        with os.fdopen(descriptor, 'wb') as stream:
            stream.write(archive_payload(record, anchor, preimage_sha256, old_body))
            stream.flush()
            os.fsync(stream.fileno())
        published = None
        for _ in range(8):
            timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
            candidate = archive_dir / ('checkpoint-' + timestamp + '-'
                                       + secrets.token_hex(8) + '.md')
            try:
                os.link(temporary, candidate)
                published = candidate
                break
            except FileExistsError:
                continue
        if published is None:
            raise TaskContextError('could not allocate a unique archive name')
        temporary.unlink()
        temporary = None
        return published
    finally:
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass


def write_candidate_temp(record_path, candidate):
    descriptor, name = tempfile.mkstemp(prefix='.' + record_path.name + '.pstack-',
                                        suffix='.tmp', dir=record_path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, 'wb') as stream:
            stream.write(candidate)
            stream.flush()
            os.fsync(stream.fileno())
    except Exception:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise
    return temporary


def remove_owned_temp(path):
    if path is None:
        return
    try:
        path.unlink()
    except FileNotFoundError:
        pass
    except OSError:
        pass


def archive_result_path(root, archive_path):
    return archive_path.relative_to(root).as_posix()


def update_task(workspace, record, anchor, expected_sha256, body_file, archive_directory):
    root = workspace_root(workspace)
    validate_anchor(anchor)
    if not isinstance(expected_sha256, str) or not SHA256_PATTERN.fullmatch(expected_sha256):
        raise TaskContextError('expected SHA-256 must contain 64 hexadecimal characters')
    expected_sha256 = expected_sha256.lower()
    record_path = session_start.selected_record(root, record)
    archive_dir = confined_directory(root, archive_directory)
    body_path, new_body = read_body_file(body_file)
    lock_path = lock_path_for(record_path)
    reject_body_alias(body_path, record_path, archive_dir, lock_path)
    try:
        with record_lock(lock_path):
            return update_locked(root, record, record_path, archive_dir, anchor,
                                 expected_sha256, new_body)
    except LockUnavailable:
        return {'status': 'locked', 'record_path': record.replace('\\', '/'),
                'anchor': anchor}


def update_locked(root, record, record_path, archive_dir, anchor,
                  expected_sha256, new_body):
    content, _ = snapshot_record(root, record)
    preimage_sha256 = digest(content)
    if preimage_sha256 != expected_sha256:
        return {'status': 'stale_revision', 'record_path': record.replace('\\', '/'),
                'anchor': anchor, 'expected_sha256': expected_sha256,
                'actual_sha256': preimage_sha256}
    start, end = session_start.current_span(content, anchor)
    old_body = content[start:end]
    try:
        old_text = old_body.decode('utf-8')
    except UnicodeDecodeError:
        raise TaskContextError('current section is not valid UTF-8') from None
    if not old_text.strip():
        raise TaskContextError('current section is empty')
    if old_body == new_body:
        return {'status': 'unchanged', 'record_path': record.replace('\\', '/'),
                'anchor': anchor, 'record_sha256': preimage_sha256,
                'current_bytes': len(old_body)}
    candidate = content[:start] + new_body + content[end:]
    if len(candidate) > MAX_RECORD_BYTES:
        raise TaskContextError('candidate record exceeds 2097152-byte scan limit')
    current_text = session_start.current_section(candidate, anchor)
    candidate_start, candidate_end = session_start.current_span(candidate, anchor)
    if candidate[candidate_start:candidate_end] != new_body:
        raise TaskContextError('candidate current section did not match the supplied body')
    candidate_sha256 = digest(candidate)
    try:
        archive_path = publish_archive(archive_dir, record, anchor, preimage_sha256, old_body)
    except Exception as error:
        return {'status': 'archive_failed', 'record_path': record.replace('\\', '/'),
                'anchor': anchor, 'record_sha256': preimage_sha256,
                'error': type(error).__name__}
    archived = archive_result_path(root, archive_path)
    temporary = None
    try:
        try:
            temporary = write_candidate_temp(record_path, candidate)
        except Exception as error:
            return {'status': 'update_failed', 'record_path': record.replace('\\', '/'),
                    'anchor': anchor, 'archive': archived, 'record_sha256': preimage_sha256,
                    'error': type(error).__name__}
        try:
            latest, _ = snapshot_record(root, record)
        except Exception as error:
            return {'status': 'pre_replace_check_failed',
                    'record_path': record.replace('\\', '/'), 'anchor': anchor,
                    'archive': archived, 'error': type(error).__name__}
        actual_sha256 = digest(latest)
        if actual_sha256 != preimage_sha256:
            return {'status': 'stale_revision', 'record_path': record.replace('\\', '/'),
                    'anchor': anchor, 'archive': archived,
                    'expected_sha256': preimage_sha256, 'actual_sha256': actual_sha256}
        try:
            os.replace(temporary, record_path)
            temporary = None
        except Exception as error:
            return {'status': 'replace_failed',
                    'record_path': record.replace('\\', '/'), 'anchor': anchor,
                    'archive': archived, 'expected_sha256': candidate_sha256,
                    'error': type(error).__name__}
        try:
            readback, _ = readback_record(root, record)
            readback_start, readback_end = session_start.current_span(readback, anchor)
            if (readback != candidate
                    or readback[readback_start:readback_end] != new_body
                    or session_start.current_section(readback, anchor) != current_text):
                raise TaskContextError('record readback did not match the candidate')
        except Exception as error:
            result = {'status': 'verification_failed', 'committed_uncertain': True,
                      'record_path': record.replace('\\', '/'), 'anchor': anchor,
                      'archive': archived, 'expected_sha256': candidate_sha256,
                      'error': type(error).__name__}
            if isinstance(error, TaskContextError):
                result['detail'] = str(error)
            return result
        return {'status': 'updated', 'record_path': record.replace('\\', '/'),
                'anchor': anchor, 'archive': archived,
                'previous_sha256': preimage_sha256, 'current_sha256': candidate_sha256,
                'archived_body_bytes': len(old_body),
                'archived_body_sha256': digest(old_body)}
    finally:
        remove_owned_temp(temporary)


def build_parser():
    parser = argparse.ArgumentParser(prog='task_context.py')
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('read', 'update'):
        command = commands.add_parser(name)
        command.add_argument('--workspace', required=True)
        command.add_argument('--record', required=True)
        command.add_argument('--anchor', required=True)
    update = commands.choices['update']
    update.add_argument('--expected-sha256', required=True)
    update.add_argument('--body-file', required=True)
    update.add_argument('--archive-dir', required=True)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        if args.command == 'read':
            result = read_task(args.workspace, args.record, args.anchor)
        else:
            result = update_task(args.workspace, args.record, args.anchor,
                                 args.expected_sha256, args.body_file, args.archive_dir)
    except (TaskContextError, session_start.ContextError) as error:
        result = {'status': 'error', 'error': str(error)}
    except (OSError, ValueError, TypeError, RuntimeError) as error:
        result = {'status': 'error', 'error': type(error).__name__}
    sys.stdout.buffer.write(json.dumps(result, ensure_ascii=False,
                                       separators=(',', ':')).encode('utf-8') + b'\n')
    return 0 if result['status'] in {'ok', 'current_oversized', 'updated', 'unchanged'} else 1


if __name__ == '__main__':
    sys.exit(main())
