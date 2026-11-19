"""Offline tests: python3 -m unittest discover -s benchmark -v."""
import argparse
import contextlib
import csv
import hashlib
import io
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

import bench


class BenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)

    def remove(self, text, titles):
        skill = self.root / 'skill'
        skill.mkdir(exist_ok=True)
        (skill / 'SKILL.md').write_bytes(text.encode())
        args = argparse.Namespace(skill_folder=str(skill), out=str(self.root / 'run'),
                                  file='SKILL.md', heading=titles, node=['review'], source_url=None)
        with contextlib.redirect_stdout(io.StringIO()):
            bench.remove(args)
        return self.root / 'run'

    def test_remove_nested_and_fenced_headings(self):
        text = '# Skill\r\n## Keep\r\n```md\r\n## Review\r\n```\r\n## Review\r\nCheck.\r\n### Detail\r\nMore.\r\n## Send\r\nSend.\r\n'
        work = self.remove(text, ['Review'])
        key = json.loads((work / 'key.json').read_text())['items'][0]
        removed = (work / 'removed/R1.md').read_bytes()
        self.assertEqual(key['removed_line_range'], [6, 9])
        self.assertEqual(key['line_count'], 4)
        self.assertEqual(key['sha256'], hashlib.sha256(removed).hexdigest())
        self.assertIn(b'## Send\r\n', (work / 'altered/SKILL.md').read_bytes())

    def test_remove_missing_empty_ambiguous_overlap(self):
        for text, titles in [('', ['Review']), ('## Other\n', ['Review']),
                             ('## Review\n## Review\n', ['Review']),
                             ('## Review\n### Child\n', ['Review', 'Child'])]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.remove(text, titles)
        self.assertFalse((self.root / 'run').exists())

    def test_multiple_and_setext(self):
        work = self.remove('Skill\n=====\nReview\n------\nCheck.\n## Send\nSend.\n', ['Review', 'Send'])
        self.assertEqual((work / 'altered/SKILL.md').read_text(), 'Skill\n=====\n')

    def test_remove_excludes_vcs_metadata(self):
        skill = self.root / 'skill'
        skill.mkdir()
        for name in ('.git', '.hg', '.svn'):
            metadata = skill / 'nested' / name
            metadata.mkdir(parents=True)
            (metadata / 'original').write_text('## Review\nCheck.\n')
        work = self.remove('# Skill\n## Review\nCheck.\n', ['Review'])
        for name in ('.git', '.hg', '.svn'):
            self.assertFalse(list((work / 'altered').rglob(name)))

    def test_remove_rejects_symlinks(self):
        skill = self.root / 'skill'
        skill.mkdir()
        for name, target in [('backup.md', 'SKILL.md'), ('alias', '.'), ('broken', 'missing')]:
            with self.subTest(name=name):
                link = skill / name
                link.symlink_to(target)
                with self.assertRaisesRegex(ValueError, name):
                    self.remove('# Skill\n## Review\nCheck.\n', ['Review'])
                self.assertFalse((self.root / 'run').exists())
                link.unlink()

    def test_remove_rejects_backup_copies_and_cleans_work_directory(self):
        skill = self.root / 'skill'
        skill.mkdir()
        text = '# Skill\n## Review\nCheck.\n## Send\nSend.\n'
        (skill / 'SKILL.md.bak').write_text(text)
        (skill / 'copy.bin').write_bytes(b'prefix\x00## Send\nSend.\n')
        with self.assertRaises(ValueError) as error:
            self.remove(text, ['Review', 'Send'])
        self.assertIn('SKILL.md.bak', str(error.exception))
        self.assertIn('copy.bin', str(error.exception))
        self.assertFalse((self.root / 'run').exists())
        self.assertEqual((skill / 'SKILL.md.bak').read_text(), text)

    def test_findings_and_empty(self):
        report = self.root / 'report.md'
        out = self.root / 'marks.csv'
        report.write_text('## Findings\n### Needed\n1. **Review** [map]\n   Map node: review.check — source: example\n## Trace\n2. **Ignore** [map]\n')
        args = argparse.Namespace(report=str(report), out=str(out))
        with contextlib.redirect_stdout(io.StringIO()):
            bench.findings(args)
        with out.open() as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['nodes'], 'review.check')
        self.assertEqual(rows[0]['verdict'], '')
        report.write_text('## Findings\nNone.\n')
        with contextlib.redirect_stdout(io.StringIO()):
            bench.findings(args)
        self.assertEqual(out.read_text().strip(), ','.join(bench.FIELDS))
        report.write_text('No section')
        with self.assertRaises(ValueError):
            bench.findings(args)

    def test_findings_ignore_fenced_bands_items_and_node_details(self):
        report = self.root / 'report.md'
        report.write_text(
            '## Findings\n### Needed\n1. **Real finding**\n'
            '   ~~~~markdown\n   Map node: fake.override\n'
            '   ~~~\n### Minor\n2. **Shorter fence is not a close**\n'
            '   ~~~~text\n3. **Fence with info is not a close**\n   ~~~~\n'
            '   Map node: review.check\n'
            '```md\n## Fake section end\n### Minor\n4. **Example**\n```\n'
            '5. **Still Needed**\n'
            '## Trace\n### Minor\n6. **Not a finding**\n',
            encoding='utf-8')
        with contextlib.redirect_stdout(io.StringIO()) as output:
            bench.findings(argparse.Namespace(report=report, out=None))
        self.assertEqual([(row['rank'], row['band'], row['nodes']) for row in csv.DictReader(
            io.StringIO(output.getvalue()))], [('1', 'Needed', 'review.check'), ('5', 'Needed', '')])

    def test_score_normal_empty_and_errors(self):
        key, marks, out = [self.root / name for name in ('key.json', 'marks.csv', 'result.json')]
        args = argparse.Namespace(key=str(key), marks=str(marks), out=str(out), top=1)
        bench.write_json(key, {'items': [{'id': 'R1'}, {'id': 'R2'}]})
        def run(rows):
            with marks.open('w', newline='') as handle:
                writer = csv.writer(handle)
                writer.writerow(bench.FIELDS)
                writer.writerows(rows)
            with contextlib.redirect_stdout(io.StringIO()):
                bench.score(args)
            return json.loads(out.read_text())
        result = run([[1, 'Needed', 'a', '', 'R1', 'real'], [2, 'Minor', 'b', '', 'R1', 'real'],
                      [3, 'Minor', 'c', '', '', 'false']])
        self.assertEqual((result['recovered'], result['recovered_top_n'], result['false_positives']), (1, 1, 1))
        self.assertEqual(result['unmatched'], ['R2'])
        for match, verdict in [('R9', 'real'), ('R1', 'false'), ('', ''), ('', 'maybe')]:
            with self.subTest(match=match, verdict=verdict), self.assertRaises(ValueError):
                run([[1, 'Needed', 'a', '', match, verdict]])
        bench.write_json(key, {'items': []})
        self.assertIsNone(run([])['recovery_rate'])

    def test_score_cli_rejects_short_and_long_csv_rows_with_line_number(self):
        key, marks, out = [self.root / name for name in ('key.json', 'marks.csv', 'result.json')]
        bench.write_json(key, {'items': [{'id': 'R1'}]})
        for row in ('2,Needed,Incomplete', '2,Needed,Extra,,R1,real,extra'):
            with self.subTest(row=row):
                marks.write_text(','.join(bench.FIELDS) + '\n1,Needed,"Multi\nline",,R1,real\n' + row + '\n',
                                 encoding='utf-8')
                result = subprocess.run([sys.executable, bench.__file__, 'score', str(key), str(marks),
                                         '--out', str(out)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 2)
                self.assertIn('CSV line 4: expected 6 columns', result.stderr)
                self.assertNotIn('Traceback', result.stderr)
                self.assertFalse(out.exists())

    def test_summary(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            bench.summary(argparse.Namespace(results=[]))
        self.assertIn('Historical pilot (not independently rescorable): Test 1', output.getvalue())
        self.assertIn('Combined skill (one run) | 11/12', output.getvalue())

    def test_recorded_pilot_counts_distinguish_items_from_repeated_chances(self):
        pilot = json.loads((bench.HERE / 'data' / 'validation-2026-11.json').read_text(encoding='utf-8'))
        video, mdr, combined = pilot['tests']
        items = sum(len(test['removed_items']) for test in (video, mdr))
        self.assertEqual(items, 12)
        self.assertEqual(video['chances'] + mdr['chances'], items * 2)
        self.assertEqual(combined['chances'], items)
        self.assertEqual([a['recovered'] + b['recovered'] for a, b in zip(video['methods'], mdr['methods'])],
                         [20, 18])


if __name__ == '__main__':
    unittest.main()
