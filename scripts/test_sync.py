import tomllib
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

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


if __name__ == '__main__':
    unittest.main()
