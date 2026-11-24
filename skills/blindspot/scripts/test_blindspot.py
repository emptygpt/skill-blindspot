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
            status = blindspot.cmd_lint(argparse.Namespace(report=str(report), map='software', profile=profile, skill=[]))
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

    def test_prepare_keeps_deferred_decisions_separate_from_exclusions(self):
        self.write('skill/SKILL.md', '# Example')
        self.write('skill/.blindspot.yaml',
                   'exclude:\n  - node: requirements.understand-request\n'
                   'deferred:\n  - node: testing.test-the-change\n'
                   '    reason: Later\n  - finding: "detailed release notes"\n')
        worksheet = self.root / 'worksheet.md'
        result = self.cli('prepare', self.root / 'skill', '--map', 'software', '--out', worksheet)
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = worksheet.read_text()
        nodes = worksheet.with_name('worksheet-nodes.md').read_text()
        self.assertIn('- excluded node: requirements.understand-request', summary)
        self.assertIn('- deferred node: testing.test-the-change', summary)
        self.assertIn('- deferred finding: detailed release notes', summary)
        self.assertIn('**testing.test-the-change** [deferred by profile]', nodes)
        self.assertNotIn('excluded node: testing.test-the-change', summary)

    def test_lint_deferred_state_is_visible_and_counted_separately(self):
        self.write('reports/profile.yaml', 'deferred:\n  - node: requirements.understand-request\n')
        report = self.report('profile.yaml')
        text = report.read_text().replace(' | excluded | ', ' | deferred | ')
        size = sum(len(g['nodes']) for g in blindspot.resolve(blindspot.load_maps(), 'software')['groups'])
        counts = f'covered {size - 1}, shallow 0, absent 0, not-applicable 0, deferred 1'
        report.write_text(text + '\n\n' + counts)
        status, output = self.lint(report)
        self.assertEqual(status, 0, output)
        self.assertIn('deferred 1, excluded 0', output)
        report.write_text(text + '\n\n' + counts.replace('deferred 1', 'deferred 0'))
        status, output = self.lint(report)
        self.assertEqual(status, 1, output)
        self.assertIn('counts line says', output)

    def test_lint_deferred_requires_membership_in_active_profile(self):
        self.write('reports/excluded.yaml', 'exclude:\n  - node: requirements.understand-request\n')
        for profile in (None, 'excluded.yaml'):
            with self.subTest(profile=profile):
                report = self.report(profile)
                report.write_text(report.read_text().replace(' | excluded | ', ' | deferred | '))
                status, output = self.lint(report)
                self.assertEqual(status, 1, output)
                self.assertIn('marked deferred but not listed', output)

    def test_lint_finding_deferral_can_cover_multiple_map_nodes(self):
        self.write('reports/profile.yaml', 'deferred:\n  - finding: Verify the requested change\n')
        report = self.report('profile.yaml')
        text = report.read_text().replace(' | excluded | ', ' | deferred | ').replace(
            '| testing.test-the-change | covered |', '| testing.test-the-change | deferred |')
        deferred = ('\n\n## Deferred by profile\n| Node or finding | Reason | Map nodes |\n'
                    '| Verify the requested change | Later | '
                    '`requirements.understand-request`, `testing.test-the-change` |\n')
        report.write_text(text + deferred)
        status, output = self.lint(report)
        self.assertEqual(status, 0, output)
        report.write_text(text + deferred.replace('Verify the requested change', 'Unapproved deferral'))
        status, output = self.lint(report)
        self.assertEqual(status, 1, output)
        self.assertIn('marked deferred but not listed', output)
        report.write_text((text + deferred).replace(
            '| testing.test-the-change | deferred |', '| testing.test-the-change | shallow |'))
        status, output = self.lint(report)
        self.assertEqual(status, 1, output)
        self.assertIn('testing.test-the-change is deferred but marked shallow', output)

    def test_lint_rejects_reraised_deferred_node(self):
        self.write('reports/profile.yaml', 'deferred:\n  - node: requirements.understand-request\n')
        report = self.report('profile.yaml')
        text = report.read_text()
        report.write_text(text.replace(' | excluded | ', ' | absent | '))
        status, output = self.lint(report)
        self.assertEqual(status, 1, output)
        self.assertIn('is deferred but marked absent', output)
        for section in ('## Findings\n', '## Unsourced findings\n'):
            with self.subTest(section=section):
                report.write_text(text.replace(' | excluded | ', ' | deferred | ').replace(
                    '## Findings\n', section + 'Map node: requirements.understand-request\n'))
                status, output = self.lint(report)
                self.assertEqual(status, 1, output)
                self.assertIn('is deferred but named as a finding', output)

    def test_lint_allows_contextual_references_to_a_deferred_node(self):
        self.write('reports/profile.yaml', 'deferred:\n  - node: requirements.understand-request\n')
        report = self.report('profile.yaml')
        text = report.read_text().replace(' | excluded | ', ' | deferred | ')
        text = text.replace('## Findings\n', '## Findings\n'
                            '  Nodes: testing.test-the-change\n'
                            '  Why: requirements.understand-request does not cover this gap.\n'
                            '\n## Unsourced findings\n'
                            '- Back up material not covered by requirements.understand-request.\n')
        report.write_text(text)
        status, output = self.lint(report)
        self.assertEqual(status, 0, output)
        report.write_text(text.replace('Nodes: testing.test-the-change',
                                       'Nodes: testing.test-the-change, requirements.understand-request'))
        status, output = self.lint(report)
        self.assertEqual(status, 1, output)
        self.assertIn('is deferred but named as a finding', output)

    def test_prepare_rejects_conflicting_excluded_and_deferred_decisions(self):
        self.write('skill/SKILL.md', '# Example')
        self.write('skill/.blindspot.yaml',
                   'exclude:\n  - node: requirements.understand-request\n'
                   'deferred:\n  - node: requirements.understand-request\n')
        result = self.cli('prepare', self.root / 'skill', '--map', 'software')
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn('both excluded and deferred', result.stderr)

    def test_prepare_preserves_hashes_inside_profile_values(self):
        self.write('skill/SKILL.md', '# Example')
        self.write('skill/.blindspot.yaml',
                   'exclude:\n  - finding: "Release #alpha"  # comment\n'
                   "deferred:\n  - finding: 'Release #beta'  # comment\n"
                   '  - finding: Fix C# examples  # comment\n')
        result = self.cli('prepare', self.root / 'skill', '--map', 'software')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('- excluded finding: Release #alpha\n', result.stdout)
        self.assertIn('- deferred finding: Release #beta\n', result.stdout)
        self.assertIn('- deferred finding: Fix C# examples\n', result.stdout)

    def test_lint_missing_report_is_a_clean_cli_error(self):
        report = self.root / 'missing.md'
        result = self.cli('lint', report, '--map', 'software')
        self.assertEqual(result.returncode, 1)
        self.assertIn("lint: ", result.stderr)
        self.assertIn(str(report), result.stderr)
        self.assertNotIn('Traceback', result.stderr)

    def evidence_report(self, state, evidence, filename='reports/report.md'):
        report = self.report(excluded=False)
        text = report.read_text(encoding='utf-8').replace(
            '| requirements.understand-request | covered | Synthetic evidence |',
            f'| requirements.understand-request | {state} | {evidence} |')
        return self.write(filename, text.replace('## Findings\n',
                                                 '## Findings\nrequirements.understand-request\n'))

    def test_lint_checks_every_evidence_quote_for_covered_and_shallow(self):
        skill = self.write('skill/SKILL.md', 'Read the brief.').parent
        for state in ('covered', 'shallow'):
            with self.subTest(state=state):
                report = self.evidence_report(state, '"Read the brief." and “Fabricated instruction.”')
                result = self.cli('lint', report, '--map', 'software', '--skill', skill)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn('requirements.understand-request', result.stdout)
                self.assertIn('Fabricated instruction.', result.stdout)
                self.assertNotIn('Read the brief.', result.stdout)

    def test_lint_matches_evidence_across_whitespace_in_skill_and_nested_files(self):
        skill = self.write('skill/SKILL.md', 'Read\n  the\tbrief.').parent
        self.write('skill/scripts/review.py', 'Review    the risks and check x | y.')
        report = self.evidence_report('shallow', '"Read the brief." and “Review the risks and check x \\| y.”')
        result = self.cli('lint', report, '--map', 'software', '--skill', skill)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_lint_checks_the_whole_nested_curly_quote(self):
        skill = self.write('skill/SKILL.md', 'Check “risks” before delivery.').parent
        for tail, expected in (('before delivery.', 0), ('after release.', 1)):
            with self.subTest(tail=tail):
                report = self.evidence_report('covered', f'“Check “risks” {tail}”')
                result = self.cli('lint', report, '--map', 'software', '--skill', skill)
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                if expected:
                    self.assertIn(f'Check “risks” {tail}', result.stdout)

    def test_lint_unescapes_only_markdown_punctuation_in_evidence(self):
        skill = self.write('skill/SKILL.md', r'Use C:\temp and *literal* with x | y. Keep \q.').parent
        report = self.evidence_report(
            'covered', r'"Use C:\\temp and \*literal\* with x \| y." and “Keep \q.”')
        result = self.cli('lint', report, '--map', 'software', '--skill', skill)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_lint_reports_unbalanced_curly_quotes_and_checks_later_excerpts(self):
        skill = self.write('skill/SKILL.md', 'A literal “ mark.').parent
        report = self.evidence_report('covered', '“A literal “ mark.” and "Unsupported later excerpt."')
        result = self.cli('lint', report, '--map', 'software', '--skill', skill)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('requirements.understand-request: malformed curly quote', result.stdout)
        self.assertIn('evidence quote not found in the Skill: \'Unsupported later excerpt.\'', result.stdout)

    def test_lint_ignores_evidence_quotes_for_other_states(self):
        skill = self.write('skill/SKILL.md', '# Skill').parent
        for state in ('absent', 'not-applicable', 'undetermined'):
            with self.subTest(state=state):
                report = self.evidence_report(state, '"Discussed in the report, not present in the Skill."')
                result = self.cli('lint', report, '--map', 'software', '--skill', skill)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_lint_checks_explicit_delegated_files_and_folders(self):
        skill = self.write('skill/SKILL.md', 'Read the brief.').parent
        script = self.write('tools/check.py', 'Check the risks.')
        called_skill = self.write('shared/review/references/guide.md', 'Record the decision.').parent.parent
        report = self.evidence_report('covered', '"Check the risks." and "Record the decision."')
        result = self.cli('lint', report, '--map', 'software', '--skill', skill,
                          '--skill', script, '--skill', called_skill)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_lint_does_not_use_the_report_or_files_outside_the_skill_as_evidence(self):
        skill = self.write('skill/SKILL.md', 'Read the brief.').parent
        outside = self.write('outside.txt', 'Fabricated instruction.')
        (skill / 'outside.txt').symlink_to(outside)
        report = self.evidence_report('covered', '"Fabricated instruction."', 'skill/report.md')
        result = self.cli('lint', report, '--map', 'software', '--skill', skill)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('Fabricated instruction.', result.stdout)

    def test_lint_findings_skip_filenames_but_reject_unknown_nodes(self):
        report = self.report(excluded=False)
        original = report.read_text(encoding='utf-8')
        for extension in sorted(blindspot.PROSE_EXT | blindspot.DATA_EXT | blindspot.CODE_EXT):
            with self.subTest(extension=extension):
                report.write_text(original.replace('## Findings\n',
                                  '## Findings\nrequirements' + extension + ' requirements.config' + extension + '\n'),
                                  encoding='utf-8')
                status, output = self.lint(report)
                self.assertEqual(status, 0, output)
        report.write_text(original.replace('## Findings\n', '## Findings\nrequirements.unknown-node\n'),
                          encoding='utf-8')
        status, output = self.lint(report)
        self.assertEqual(status, 1)
        self.assertIn('findings: requirements.unknown-node is not a node of software', output)

    def test_lint_known_node_with_file_extension_still_requires_finding(self):
        resolved = {'groups': [{'id': 'requirements', 'nodes': [{'id': 'requirements.md'}]}]}
        for finding, expected in (('', 1), ('requirements.md', 0)):
            with self.subTest(finding=finding):
                report = self.write('report.md', '## Findings\n' + finding +
                                    '\n## Map table\n| requirements.md | absent |\n')
                with patch.object(blindspot, 'resolve', return_value=resolved):
                    status, output = self.lint(report)
                self.assertEqual(status, expected, output)
                if expected:
                    self.assertIn('requirements.md is absent in the table but no finding names it', output)

    def test_lint_undetermined_requires_evidence_but_not_a_finding(self):
        resolved = {'groups': [{'id': 'quality', 'nodes': [{'id': 'quality.check'}]}]}
        for evidence, expected in (('Cannot read references/review.md', 0), ('', 1)):
            with self.subTest(evidence=evidence):
                report = self.write('report.md', '## Findings\n\n## Map table\n'
                                    f'| quality.check | undetermined | {evidence} |\n')
                with patch.object(blindspot, 'resolve', return_value=resolved):
                    status, output = self.lint(report)
                self.assertEqual(status, expected, output)
                self.assertIn('undetermined 1', output)
                self.assertNotIn('no finding names it', output)
                if expected:
                    self.assertIn('needs evidence', output)

    def test_lint_undetermined_counts_and_legacy_counts(self):
        resolved = {'groups': [{'id': 'quality', 'nodes': [{'id': 'quality.check'}]}]}
        for state, counts, expected in (
            ('covered', 'covered 1, shallow 0, absent 0, not-applicable 0', 0),
            ('undetermined', 'covered 0, shallow 0, absent 0, not-applicable 0, undetermined 1', 0),
            ('undetermined', 'covered 0, shallow 0, absent 0, not-applicable 0, undetermined 2', 1),
            ('undetermined', 'covered 0, shallow 0, absent 0, not-applicable 0', 1),
        ):
            with self.subTest(state=state, counts=counts):
                report = self.write('report.md', '## Findings\n\n## Map table\n'
                                    f'| quality.check | {state} | Review instructions |\n\n{counts}\n')
                with patch.object(blindspot, 'resolve', return_value=resolved):
                    status, output = self.lint(report)
                self.assertEqual(status, expected, output)
                if expected:
                    self.assertIn('counts line says', output)

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
