from contextlib import redirect_stdout
from io import StringIO
import json
import tomllib
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import sync
from sync import patch_config, plugin_drift


class PluginDriftTests(unittest.TestCase):
    def test_bootstrap_dependencies_do_not_hide_source_or_unexpected_file_drift(self):
        with TemporaryDirectory() as directory:
            home = Path(directory)
            source = home / 'source.ts'
            source.write_text('export const value = 1;')
            name = 'skills/poteto-mode/scripts/bootstrap.ts'
            files = {'local-plugins/pstack/' + name: source}
            installed = home / 'plugins/cache/personal/pstack/test'
            target = installed / name
            target.parent.mkdir(parents=True)
            target.write_bytes(source.read_bytes())
            generated = target.parent / 'node_modules/commander/package.json'
            generated.parent.mkdir(parents=True)
            generated.write_text('{"version": "14.0.0"}')

            self.assertEqual(plugin_drift(home, 'test', files), (installed, []))

            target.write_text('export const value = 2;')
            unexpected = installed / 'skills/other/node_modules/unknown.txt'
            unexpected.parent.mkdir(parents=True)
            unexpected.write_text('unexpected')
            (target.parent / 'unexpected.txt').write_text('unexpected')

            _, drift = plugin_drift(home, 'test', files)
            self.assertCountEqual(drift, [
                'installed/' + name,
                'installed/extra/skills/other/node_modules/unknown.txt',
                'installed/extra/skills/poteto-mode/scripts/unexpected.txt',
            ])


class PatchConfigInsertionTests(unittest.TestCase):
    def assert_config(self, raw, desired, expected):
        updated, changes = patch_config(raw, desired)
        self.assertEqual(tomllib.loads(updated.decode('utf-8-sig')), expected)
        self.assertCountEqual(changes, ['.'.join(path) for path in desired])
        return updated

    def test_empty_config_keeps_root_and_new_table_scopes(self):
        desired = {('agents', 'enabled'): True, ('model',): 'example'}

        updated = self.assert_config(
            b'', desired, {'agents': {'enabled': True}, 'model': 'example'})

        again, changes = patch_config(updated, desired)
        self.assertEqual(again, updated)
        self.assertEqual(changes, [])

    def test_comment_only_config_accepts_reversed_desired_order(self):
        raw = b'\xef\xbb\xbf# existing config\r\n'
        desired = {('agents', 'enabled'): True, ('model',): 'example'}

        updated = self.assert_config(
            raw, desired, {'agents': {'enabled': True}, 'model': 'example'})

        self.assertTrue(updated.startswith(b'\xef\xbb\xbf'))
        self.assertIn(b'\r\n', updated)
        self.assertNotIn(b'\n', updated.replace(b'\r\n', b''))

    def test_root_last_section_and_new_tables_preserve_unmanaged_values(self):
        raw = (
            b'unmanaged = "keep"\n'
            b'[agents]\n'
            b'max_threads = 2\n')
        desired = {
            ('features', 'multi_agent'): True,
            ('agents', 'worker', 'description'): 'worker description',
            ('agents', 'enabled'): True,
            ('model',): 'example',
        }

        self.assert_config(
            raw,
            desired,
            {
                'unmanaged': 'keep',
                'model': 'example',
                'agents': {
                    'max_threads': 2,
                    'enabled': True,
                    'worker': {'description': 'worker description'},
                },
                'features': {'multi_agent': True},
            },
        )

    def test_managed_multiline_value_remains_unsupported(self):
        raw = b'model = """existing\nmultiline value"""\n'

        with self.assertRaisesRegex(
                ValueError, 'Unsupported managed multiline or complex value: model'):
            patch_config(raw, {('model',): 'example'})


class SyncCommandTests(unittest.TestCase):
    workflow = '''model = "gpt-6-astra"
model_reasoning_effort = "high"
review_model = "gpt-6-astra"
developer_instructions = "source developer instructions"

[agents]
enabled = true
max_threads = 4
max_depth = 2
default_subagent_model = "gpt-6-luna"
default_subagent_reasoning_effort = "max"

[features]
multi_agent = true
multi_agent_v2 = true

[agents.worker]
description = "worker"
config_file = "agents/worker.toml"

[agents.poteto-agent]
description = "poteto agent"
config_file = "agents/poteto-agent.toml"

[agents.astra-advisor]
description = "astra advisor"
config_file = "agents/astra-advisor.toml"
'''

    def write(self, path, content):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode('utf-8') if isinstance(content, str) else content)

    def create_fixture(self, base, include_globals=True):
        source = base / 'source'
        home = base / 'home'
        self.write(source / 'pstack/.codex-plugin/plugin.json', '{"version":"test-version"}')
        self.write(source / 'pstack/README.md', 'updated plugin content')
        if include_globals:
            self.write(source / 'AGENTS.md', 'source global instructions')
            self.write(source / 'prompts/codex-event-driven-base.md', 'source prompt')
            for role in ('worker', 'poteto-agent', 'astra-advisor'):
                self.write(source / ('agents/' + role + '.toml'), 'model = "gpt-6-luna"\n')
            self.write(source / 'config/workflow.toml', self.workflow)
        return source, home

    def invoke(self, source, home, *arguments):
        output = StringIO()
        argv = ['sync.py', *arguments, '--codex-home', str(home), '--skip-plugin-install']
        with patch.object(sync, 'ROOT', source), patch.object(sys, 'argv', argv), redirect_stdout(output):
            status = sync.main()
        return status, json.loads(output.getvalue())

    def test_plugin_only_preserves_config_and_global_instructions(self):
        with TemporaryDirectory() as directory:
            source, home = self.create_fixture(Path(directory))
            original_config = b'model = "gpt-6.1-sol"\nmodel_reasoning_effort = "high"\n'
            self.write(home / 'config.toml', original_config)
            global_sentinels = {
                'AGENTS.md': b'user global instructions',
                'prompts/codex-event-driven-base.md': b'user prompt',
                'agents/worker.toml': b'user agent configuration',
            }
            for name, content in global_sentinels.items():
                self.write(home / name, content)

            status, full_check = self.invoke(source, home, 'check')
            self.assertEqual(status, 1)
            self.assertIn('model', full_check['config_drift'])
            self.assertFalse(full_check['plugin_only'])

            for name in ('AGENTS.md', 'prompts/codex-event-driven-base.md',
                         'agents/worker.toml', 'agents/poteto-agent.toml',
                         'agents/astra-advisor.toml'):
                (source / name).unlink()
            (source / 'config/workflow.toml').write_text('not valid TOML = [', encoding='utf-8')

            deploy_status, receipt = self.invoke(source, home, 'deploy', '--plugin-only')
            self.assertEqual(deploy_status, 0)
            self.assertTrue(receipt['plugin_only'])
            self.assertEqual(receipt['config_drift'], [])
            self.assertEqual((home / 'config.toml').read_bytes(), original_config)
            self.assertEqual((home / 'local-plugins/pstack/README.md').read_text(encoding='utf-8'),
                             'updated plugin content')
            for name, content in global_sentinels.items():
                self.assertEqual((home / name).read_bytes(), content)

            check_status, plugin_check = self.invoke(source, home, 'check', '--plugin-only')
            self.assertEqual(check_status, 0)
            self.assertEqual(plugin_check['status'], 'ok')
            self.assertTrue(plugin_check['plugin_only'])
            self.assertEqual(plugin_check['config_drift'], [])

    def test_plugin_only_deploy_does_not_create_missing_config(self):
        with TemporaryDirectory() as directory:
            source, home = self.create_fixture(Path(directory), include_globals=False)

            status, receipt = self.invoke(source, home, 'deploy', '--plugin-only')

            self.assertEqual(status, 0)
            self.assertTrue(receipt['plugin_only'])
            self.assertEqual(receipt['config_drift'], [])
            self.assertFalse((home / 'config.toml').exists())
            self.assertTrue((home / 'local-plugins/pstack/README.md').is_file())

    def test_default_deploy_still_synchronizes_managed_configuration(self):
        with TemporaryDirectory() as directory:
            source, home = self.create_fixture(Path(directory))
            self.write(home / 'config.toml', 'model = "gpt-6.1-sol"\nmodel_reasoning_effort = "high"\n')

            status, receipt = self.invoke(source, home, 'deploy')

            self.assertEqual(status, 0)
            self.assertFalse(receipt['plugin_only'])
            self.assertIn('model', receipt['config_drift'])
            self.assertEqual(tomllib.loads((home / 'config.toml').read_text(encoding='utf-8'))['model'],
                             'gpt-6-astra')


if __name__ == '__main__':
    unittest.main()
