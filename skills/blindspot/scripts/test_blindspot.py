"""Regression tests for the audit helper; fixtures are synthetic."""
import argparse
import contextlib
import io
import pathlib
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import blindspot


class HelperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def cli(self, *args):
        return subprocess.run([sys.executable, '-B', str(pathlib.Path(blindspot.__file__)), *map(str, args)],
                              capture_output=True, text=True)

    def test_resolve_rejects_invalid_extends(self):
        maps = {'first': {'map': {'extends': 'second'}}, 'second': {'map': {'extends': 'first'}}}
        with self.assertRaisesRegex(ValueError, 'extends cycle'):
            blindspot.resolve(maps, 'first')
        del maps['second']
        with self.assertRaisesRegex(ValueError, 'unknown map'):
            blindspot.resolve(maps, 'first')

    def test_prepare_reads_nested_skill_once(self):
        self.write('skill/SKILL.md', '# Parent\n')
        self.write('skill/nested/SKILL.md', '# Child\nReview the output.\n')
        worksheet = self.root / 'worksheet.md'
        result = self.cli('prepare', self.root / 'skill', '--map', 'software', '--out', worksheet)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('nested/SKILL.md (2)', worksheet.read_text())
        _, texts, _, _, _ = blindspot.read_skill(self.root / 'skill')
        self.assertEqual(set(texts), {'SKILL.md', 'nested/SKILL.md'})
        self.assertIn('Review the output.', texts['nested/SKILL.md'])

    def test_prepare_empty_skill_with_automatic_profile(self):
        self.write('skill/SKILL.md', '')
        self.write('skill/.blindspot.yaml', 'exclude:\n  - node: requirements.understand-request\n')
        result = self.cli('prepare', self.root / 'skill', '--map', 'software')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('## Profile\n- excluded node: requirements.understand-request', result.stdout)
        self.assertIn('**requirements.understand-request** [excluded by profile]', result.stdout)
        self.assertRegex(result.stdout, r'Summary: \d+ nodes, 0 with hits, \d+ without\.')

    def test_references_use_containing_file_not_basename(self):
        self.write('skill/SKILL.md', '[guide](missing/guide.md)\n')
        self.write('skill/other/guide.md', '# Guide\n')
        self.write('skill/nested/notes.md', '[parent](../SKILL.md)\n[local](guide.md)\n')
        _, texts, _, _, _ = blindspot.read_skill(self.root / 'skill')
        self.assertEqual(blindspot.missing_references(self.root / 'skill', texts),
                         [('SKILL.md', 1, 'missing/guide.md'), ('nested/notes.md', 2, 'guide.md')])
        output = self.cli('prepare', self.root / 'skill', '--map', 'software')
        self.assertIn('MISSING: nested/notes.md:2', output.stdout)

    def test_references_fragments_urls_and_encoded_paths(self):
        self.write('skill/SKILL.md', '[part](docs/my%20guide.md#part)\n[section](#section)\n'
                   '[web](https://example.org/doc.md)\n[mail](mailto:reader@example.org)\n')
        self.write('skill/docs/my guide.md', '# Part\n[home](../SKILL.md#top)\n')
        _, texts, _, _, _ = blindspot.read_skill(self.root / 'skill')
        self.assertEqual(blindspot.missing_references(self.root / 'skill', texts), [])
        self.assertEqual(blindspot.missing_references(self.root, {}), [])

    def test_prose_references_allow_skill_root_but_links_do_not(self):
        self.write('skill/SKILL.md', '# Parent\n')
        self.write('skill/references/style.md', '# Style\n')
        self.write('skill/nested/local.md', '# Local\n')
        self.write('skill/other/missing.md', '# Unrelated\n')
        self.write('skill/nested/notes.md', 'Read references/style.md and local.md.\n'
                   '[style](references/style.md)\nRead missing.md.\n')
        _, texts, _, _, _ = blindspot.read_skill(self.root / 'skill')
        self.assertEqual(blindspot.missing_references(self.root / 'skill', texts),
                         [('nested/notes.md', 2, 'references/style.md'),
                          ('nested/notes.md', 3, 'missing.md')])

    def test_prepare_skips_unparseable_reference(self):
        self.write('skill/SKILL.md', '[API](https://[YOUR_HOST]/docs)\n[local](missing.md)\n')
        _, texts, _, _, _ = blindspot.read_skill(self.root / 'skill')
        self.assertEqual(blindspot.missing_references(self.root / 'skill', texts),
                         [('SKILL.md', 2, 'missing.md')])
        result = self.cli('prepare', self.root / 'skill', '--map', 'software')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('YOUR_HOST', result.stdout)
        self.assertIn('MISSING: SKILL.md:2', result.stdout)

    def test_link_labels_are_not_prose_references(self):
        self.write('skill/SKILL.md', '[guide.md](resources/guide.md)\n'
                   '[absent.md](resources/missing.md "Guide") and read missing.txt.\n')
        self.write('skill/resources/guide.md', '# Guide\n')
        _, texts, _, _, _ = blindspot.read_skill(self.root / 'skill')
        self.assertEqual(blindspot.missing_references(self.root / 'skill', texts),
                         [('SKILL.md', 2, 'resources/missing.md'),
                          ('SKILL.md', 2, 'missing.txt')])
        result = self.cli('prepare', self.root / 'skill', '--map', 'software')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('mentions `guide.md`', result.stdout)
        self.assertNotIn('mentions `absent.md`', result.stdout)
        self.assertIn('mentions `resources/missing.md`', result.stdout)

    def test_link_with_bracketed_label_is_checked(self):
        self.write('skill/SKILL.md', 'Run [items[0]](scripts/check.py).\n')
        _, texts, _, _, _ = blindspot.read_skill(self.root / 'skill')
        self.assertEqual(blindspot.missing_references(self.root / 'skill', texts),
                         [('SKILL.md', 1, 'scripts/check.py')])

    def test_titled_links_are_checked_without_title_text(self):
        self.write('skill/SKILL.md',
                   "[a](gone.md 'Guide') [b](lost.md \"see (old.md)\") [c](away.md (x.md))\n")
        _, texts, _, _, _ = blindspot.read_skill(self.root / 'skill')
        self.assertEqual(blindspot.missing_references(self.root / 'skill', texts),
                         [('SKILL.md', 1, 'gone.md'), ('SKILL.md', 1, 'lost.md'),
                          ('SKILL.md', 1, 'away.md')])

    def test_tree_drawing_lines_are_not_prose_references(self):
        self.write('skill/SKILL.md', '```\nresources/\n'
                   '├── guide.md\n│   notes.md\n└── missing.md\n```\n'
                   'Read missing.md.\n└── [link](missing-link.md)\n')
        self.write('skill/resources/guide.md', '# Guide\n')
        _, texts, _, _, _ = blindspot.read_skill(self.root / 'skill')
        self.assertEqual(blindspot.missing_references(self.root / 'skill', texts),
                         [('SKILL.md', 7, 'missing.md'),
                          ('SKILL.md', 8, 'missing-link.md')])
        result = self.cli('prepare', self.root / 'skill', '--map', 'software')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('MISSING: SKILL.md:3', result.stdout)
        self.assertNotIn('MISSING: SKILL.md:4', result.stdout)
        self.assertNotIn('MISSING: SKILL.md:5', result.stdout)
        self.assertIn('MISSING: SKILL.md:7', result.stdout)

    def test_grep_rejects_missing_or_file_roots_before_searching(self):
        file_ = self.write('valid/note.md', 'review\n')
        for bad in (self.root / 'missing', file_):
            with self.subTest(root=bad):
                result = self.cli('grep', self.root / 'valid', bad, '-e', 'review')
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(str(bad), result.stderr)
                self.assertIn('not a directory', result.stderr)
                self.assertEqual(result.stdout, '')

    def test_grep_normal_and_empty(self):
        self.write('valid/note.md', 'review\n')
        result = self.cli('grep', self.root / 'valid', '-e', 'review')
        self.assertEqual(result.returncode, 0)
        self.assertIn('note.md:1: review', result.stdout)
        (self.root / 'empty').mkdir()
        result = self.cli('grep', self.root / 'empty', '-e', 'review')
        self.assertEqual(result.returncode, 0)
        self.assertIn('no match', result.stdout)

    def report(self, profile=None, excluded=True):
        header = 'Map: software 0.1.0'
        if profile is not None:
            header += '    Profile: ' + profile + '    Date: 2026-01-01'
        resolved = blindspot.resolve(blindspot.load_maps(), 'software')
        rows = []
        for group in resolved['groups']:
            for node in group['nodes']:
                state = 'excluded' if excluded and node['id'] == 'requirements.understand-request' else 'covered'
                rows.append('| {} | {} | Synthetic evidence |'.format(node['id'], state))
        return self.write('reports/report.md', header + '\n\n## Findings\n\n## Map table\n' + '\n'.join(rows))

    def lint(self, report, profile=None):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            status = blindspot.cmd_lint(argparse.Namespace(report=str(report), map='software', profile=profile))
        return status, output.getvalue()

    def test_lint_relative_header_profile(self):
        self.write('reports/profiles/exclude.yaml', 'exclude:\n  - node: requirements.understand-request\n')
        status, output = self.lint(self.report('profiles/exclude.yaml'))
        self.assertEqual(status, 0, output)

    def test_lint_absolute_header_profile(self):
        profile = self.write('absolute profile.yaml', 'exclude:\n  - node: requirements.understand-request\n')
        status, output = self.lint(self.report('`' + str(profile) + '`'))
        self.assertEqual(status, 0, output)

    def test_lint_override_takes_precedence(self):
        profile = self.write('override.yaml', 'exclude:\n  - node: requirements.understand-request\n')
        status, output = self.lint(self.report('missing.yaml'), str(profile))
        self.assertEqual(status, 0, output)

    def test_lint_excluded_requires_membership_in_active_profile(self):
        for profile in (None, 'none', 'empty.yaml'):
            with self.subTest(profile=profile):
                self.write('reports/empty.yaml', 'exclude: []\n')
                status, output = self.lint(self.report(profile))
                self.assertEqual(status, 1)
                self.assertIn('marked excluded but not listed', output)

    def test_lint_missing_profile_and_excluded_node_marked_covered(self):
        status, output = self.lint(self.report('missing.yaml', excluded=False))
        self.assertEqual(status, 1)
        self.assertIn('profile: file not found:', output)
        self.write('reports/profile.yaml', 'exclude:\n  - node: requirements.understand-request\n')
        status, output = self.lint(self.report('profile.yaml', excluded=False))
        self.assertEqual(status, 1)
        self.assertIn('is excluded but marked covered', output)

    def test_lint_without_exclusions_needs_no_profile(self):
        for profile in (None, 'none'):
            status, output = self.lint(self.report(profile, excluded=False))
            self.assertEqual(status, 0, output)

    def test_lint_missing_report_is_a_clean_cli_error(self):
        report = self.root / 'missing.md'
        result = self.cli('lint', report, '--map', 'software')
        self.assertEqual(result.returncode, 1)
        self.assertIn("lint: ", result.stderr)
        self.assertIn(str(report), result.stderr)
        self.assertNotIn('Traceback', result.stderr)

    def test_invalid_map_json_diagnostic_identifies_the_file(self):
        maps = self.write('maps.json', '{broken json')
        with patch.object(blindspot, 'MAPS_JSON', maps), patch.object(sys, 'argv', ['blindspot.py', 'maps']):
            with contextlib.redirect_stderr(io.StringIO()) as out, self.assertRaises(SystemExit) as error:
                blindspot.main()
        self.assertEqual(error.exception.code, 1)
        self.assertIn(f"maps: {maps}:", out.getvalue())
        self.assertIn('line 1 column', out.getvalue())

    def test_sources_mixed_lookup_returns_failure_and_prints_valid_sources(self):
        result = self.cli('sources', '--map', 'video', 'not.a-node', 'comp.ai-disclosure')
        self.assertEqual(result.returncode, 1)
        self.assertIn('not.a-node: unknown node in video', result.stderr)
        self.assertIn('comp.ai-disclosure:', result.stdout)
        self.assertIn('<https://', result.stdout)

    def test_checklist_requires_positive_source_limit(self):
        out = self.root / 'checklist.md'
        for count in (0, -1, 'many'):
            with self.subTest(count=count):
                result = self.cli('checklist', '--map', 'software', '--max-sources', count, '--out', out)
                self.assertEqual(result.returncode, 2)
                self.assertIn('--max-sources: must be a positive integer', result.stderr)
                self.assertFalse(out.exists())
        result = self.cli('checklist', '--map', 'software', '--max-sources', 1)
        self.assertEqual(result.returncode, 0, result.stderr)
        items = result.stdout.split('- [ ] **')[1:]
        self.assertTrue(items)
        for item in items:
            self.assertEqual(item.count('<https://') + item.count('<http://'), 1, item)


if __name__ == '__main__':
    unittest.main()
