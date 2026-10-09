"""Check or deploy this repository's managed Codex files and configuration."""

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tomllib


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HOME = Path('J:/Users/yangda01/.codex')
ALLOWED = {
    (): {'model', 'model_reasoning_effort', 'review_model', 'developer_instructions'},
    ('agents',): {'enabled', 'max_threads', 'max_depth', 'default_subagent_model', 'default_subagent_reasoning_effort'},
    ('features',): {'multi_agent', 'multi_agent_v2'},
    ('plugins', 'pstack@personal'): {'enabled'},
    **{('agents', role): {'description', 'config_file'} for role in ('worker', 'poteto-agent', 'astra-advisor')},
}


def read_toml(path):
    return tomllib.loads(path.read_text(encoding='utf-8-sig'))


def leaves(value, prefix=()):
    for key, item in value.items():
        if isinstance(item, dict):
            yield from leaves(item, prefix + (key,))
        else:
            yield prefix + (key,), item


def value_at(data, path):
    for key in path:
        if not isinstance(data, dict) or key not in data:
            return None
        data = data[key]
    return data


def scalar(value):
    if type(value) not in (str, bool, int):
        raise ValueError('Managed configuration must contain only string, boolean, or integer values')
    return json.dumps(value, ensure_ascii=False)


def without_managed(data, managed):
    result = copy.deepcopy(data)
    for path in managed:
        node = result
        parents = []
        for key in path[:-1]:
            if key not in node or not isinstance(node[key], dict):
                break
            parents.append((node, key))
            node = node[key]
        else:
            node.pop(path[-1], None)
            for parent, key in reversed(parents):
                if parent[key]:
                    break
                del parent[key]
    return result


def end_string_state(line, state):
    i = 0
    while i < len(line):
        if state:
            if state == '"""' and line[i] == '\\':
                i += 2
            elif line.startswith(state, i):
                i += len(state)
                state = None
            else:
                i += 1
        elif line[i] == '#':
            break
        elif line.startswith('"""', i) or line.startswith("'''", i):
            state = line[i:i + 3]
            i += 3
        elif line[i] in ('"', "'"):
            quote = line[i]
            i += 1
            while i < len(line):
                if line[i] == '\\' and quote == '"':
                    i += 2
                elif line[i] == quote:
                    i += 1
                    break
                else:
                    i += 1
        else:
            i += 1
    return state


def table_path(line):
    parsed = tomllib.loads(line + '\n__pigeonstack_marker__ = true\n')
    path = []
    while isinstance(parsed, dict) and '__pigeonstack_marker__' not in parsed:
        key, parsed = next(iter(parsed.items()))
        path.append(key)
    return tuple(path) if isinstance(parsed, dict) else None


def patch_config(raw, desired):
    text = raw.decode('utf-8-sig')
    before = tomllib.loads(text)
    changes = {path: value for path, value in desired.items() if value_at(before, path) != value}
    if not changes:
        return raw, []
    lines = text.splitlines(keepends=True)
    newline = '\r\n' if '\r\n' in text else '\n'
    sections = {(): [0, len(lines)]}
    assignments = {}
    section = ()
    state = None
    for index, line in enumerate(lines):
        if state is None:
            stripped = line.strip()
            if stripped.startswith('['):
                if section in sections:
                    sections[section][1] = index
                section = table_path(stripped)
                if section is not None:
                    sections[section] = [index + 1, len(lines)]
            elif section is not None:
                match = re.match(r'\s*([A-Za-z0-9_-]+|"[^"\\]+"|\'[^\']+\')\s*=', line)
                if match:
                    key = match.group(1).strip('"\'')
                    path = section + (key,)
                    if path in desired:
                        try:
                            parsed = tomllib.loads(line)
                            scalar(parsed[key])
                        except (ValueError, KeyError):
                            raise ValueError('Unsupported managed multiline or complex value: ' + '.'.join(path)) from None
                        assignments[path] = index
        state = end_string_state(line, state)
    insertions = {}
    for path, value in changes.items():
        line = path[-1] + ' = ' + scalar(value) + newline
        if path in assignments:
            lines[assignments[path]] = line
        else:
            insertions.setdefault(path[:-1], []).append(line)
    edits = {}
    for section, additions in insertions.items():
        index = sections[section][1] if section in sections else len(lines)
        edit = edits.setdefault(index, {'existing': [], 'tables': []})
        if section in sections:
            edit['existing'].append(''.join(additions))
        else:
            header = '[' + '.'.join(json.dumps(key) for key in section) + ']' + newline
            edit['tables'].append(newline + header + ''.join(additions))
    for index in sorted(edits, reverse=True):
        addition = ''.join(edits[index]['existing'] + edits[index]['tables'])
        if index and not lines[index - 1].endswith(('\n', '\r')):
            lines[index - 1] += newline
        lines.insert(index, addition)
    updated = ''.join(lines)
    after = tomllib.loads(updated)
    if any(value_at(after, path) != value for path, value in desired.items()):
        raise ValueError('Managed configuration could not be patched safely')
    if without_managed(before, desired) != without_managed(after, desired):
        raise ValueError('Configuration patch would change unmanaged values')
    return (b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b'') + updated.encode('utf-8'), ['.'.join(path) for path in changes]


def contained(root, path):
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('Path escapes its managed root: ' + str(path))
    return path


def source_files(plugin_only=False):
    files = {}
    if not plugin_only:
        files = {'AGENTS.md': ROOT / 'AGENTS.md',
                 'prompts/codex-event-driven-base.md': ROOT / 'prompts/codex-event-driven-base.md'}
        for role in ('worker', 'poteto-agent', 'astra-advisor'):
            relative = 'agents/' + role + '.toml'
            files[relative] = ROOT / relative
    plugin = ROOT / 'pstack'
    for path in sorted(plugin.rglob('*')):
        if path.is_file():
            files['local-plugins/pstack/' + path.relative_to(plugin).as_posix()] = path
    for path in files.values():
        contained(ROOT, path)
        if not path.is_file():
            raise ValueError('Required source is missing: ' + str(path))
        if path.suffix == '.toml':
            read_toml(path)
        elif path.suffix == '.json':
            json.loads(path.read_text(encoding='utf-8-sig'))
    manifest = json.loads((plugin / '.codex-plugin/plugin.json').read_text(encoding='utf-8-sig'))
    version = manifest['version']
    if not isinstance(version, str) or not re.fullmatch(r'[A-Za-z0-9.+_-]+', version):
        raise ValueError('Invalid plugin version')
    return files, version


def plugin_drift(home, version, files):
    installed = contained(home, home / 'plugins/cache/personal/pstack' / version)
    expected = {name.removeprefix('local-plugins/pstack/'): source for name, source in files.items() if name.startswith('local-plugins/pstack/')}
    drift = []
    for name, source in expected.items():
        target = contained(installed, installed / name)
        if not target.is_file() or target.read_bytes() != source.read_bytes():
            drift.append('installed/' + name)
    if installed.exists():
        for path in installed.rglob('*'):
            name = path.relative_to(installed).as_posix()
            if name.startswith('skills/poteto-mode/scripts/node_modules/'):
                continue
            if path.is_file() and name not in expected:
                drift.append('installed/extra/' + name)
    return installed, drift


def install_plugin(expected, version):
    command = shutil.which('codex.cmd') or shutil.which('codex')
    if not command:
        raise ValueError('codex command is unavailable; runtime deployment completed but plugin installation is unverified')
    result = subprocess.run([command, 'plugin', 'add', 'pstack@personal', '--json'], capture_output=True, text=True, encoding='utf-8', timeout=180)
    if result.returncode:
        raise ValueError('Local plugin installation failed (exit ' + str(result.returncode) + '); no retry attempted')
    try:
        response = json.loads(result.stdout)
    except ValueError:
        raise ValueError('Plugin installation did not return valid JSON') from None
    strings = []
    def collect(item):
        if isinstance(item, dict):
            for value in item.values():
                collect(value)
        elif isinstance(item, list):
            for value in item:
                collect(value)
        elif isinstance(item, str):
            strings.append(item)
    collect(response)
    if not any(Path(item).is_absolute() and Path(item).resolve() == expected.resolve() for item in strings):
        raise ValueError('Plugin installation returned an unexpected installed path')
    if version not in strings and not any(version in item and Path(item).is_absolute() for item in strings):
        raise ValueError('Plugin installation did not confirm the expected version')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('check', 'deploy'))
    parser.add_argument('--codex-home', type=Path, default=DEFAULT_HOME)
    parser.add_argument('--skip-plugin-install', action='store_true', help='Skip installed-cache checks and installation for fixtures')
    parser.add_argument('--plugin-only', action='store_true', help='Manage only the pstack plugin, skipping global files and configuration')
    args = parser.parse_args()
    home = args.codex_home.resolve()
    if home.is_relative_to(ROOT) or ROOT.is_relative_to(home):
        raise ValueError('Source and runtime paths must not overlap')
    if home != DEFAULT_HOME.resolve() and not args.skip_plugin_install:
        raise ValueError('A nondefault target requires --skip-plugin-install')
    files, version = source_files(args.plugin_only)
    config = None
    config_before = None
    config_after = None
    config_drift = []
    if not args.plugin_only:
        workflow = read_toml(contained(ROOT, ROOT / 'config/workflow.toml'))
        desired = dict(leaves(workflow))
        for path, value in desired.items():
            if path[-1] not in ALLOWED.get(path[:-1], set()):
                raise ValueError('Unmanaged key in workflow.toml: ' + '.'.join(path))
            scalar(value)
        required = {(section + (key,)) for section, keys in ALLOWED.items() if section != ('plugins', 'pstack@personal') for key in keys}
        if not required.issubset(desired):
            raise ValueError('workflow.toml is missing required managed keys')
        desired[('model_instructions_file',)] = str(home / 'prompts/codex-event-driven-base.md')
        config = contained(home, home / 'config.toml')
        config_before = config.read_bytes() if config.exists() else b''
        config_after, config_drift = patch_config(config_before, desired)
    plan = []
    for name, source in files.items():
        target = contained(home, home / name)
        content = source.read_bytes()
        previous = target.read_bytes() if target.exists() else None
        if previous != content:
            plan.append((target, previous, content))
    if config is not None and config_before != config_after:
        plan.append((config, config_before if config.exists() else None, config_after))
    installed, cache_drift = plugin_drift(home, version, files) if not args.skip_plugin_install else (None, [])
    drift = [str(path.relative_to(home)) for path, _, _ in plan]
    if args.command == 'check':
        print(json.dumps({'status': 'drift' if drift or cache_drift else 'ok', 'managed_files': len(files), 'runtime_drift': drift, 'config_drift': config_drift, 'plugin_version': version, 'installed_drift': cache_drift, 'plugin_skipped': args.skip_plugin_install, 'plugin_only': args.plugin_only}, indent=2))
        return 1 if drift or cache_drift else 0
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    backup = contained(home, home / 'backups/pigeonstack' / stamp)
    for target, previous, _ in plan:
        if (target.read_bytes() if target.exists() else None) != previous:
            raise ValueError('Runtime changed during preflight: ' + str(target.relative_to(home)))
        if previous is not None:
            contained(backup, backup / target.relative_to(home))
    backups = 0
    for target, previous, content in plan:
        if previous is not None:
            saved = backup / target.relative_to(home)
            saved.parent.mkdir(parents=True, exist_ok=True)
            saved.write_bytes(previous)
            backups += 1
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    if not args.skip_plugin_install and (plan or cache_drift):
        install_plugin(installed, version)
    if any((home / name).read_bytes() != source.read_bytes() for name, source in files.items()):
        raise ValueError('Runtime file readback failed')
    if config is not None and config.read_bytes() != config_after:
        raise ValueError('Runtime configuration readback failed')
    if not args.skip_plugin_install:
        installed, cache_drift = plugin_drift(home, version, files)
        if cache_drift:
            raise ValueError('Installed plugin hash verification failed: ' + ', '.join(cache_drift))
    print(json.dumps({'status': 'ok', 'managed_files': len(files), 'files_written': len(plan), 'backups': backups, 'backup_path': str(backup) if backups else None, 'plugin_version': version, 'installed_path': str(installed) if installed else None, 'plugin_skipped': args.skip_plugin_install, 'config_drift': config_drift, 'plugin_only': args.plugin_only}, indent=2))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        sys.exit(2)
