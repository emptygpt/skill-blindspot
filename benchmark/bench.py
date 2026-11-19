#!/usr/bin/env python3
"""Remove stages and score human-marked recovery. Python 3.8+, stdlib only.

Usage:
  python3 benchmark/bench.py remove skill --heading Review --out benchmark/work/run
  python3 benchmark/bench.py findings report.md --out marks.csv
  python3 benchmark/bench.py score key.json marks.csv --top 10 --out result.json
  python3 benchmark/bench.py summary [result.json ...]

No model is called. Matches and false positives are judged by a person.
"""
import argparse
import csv
import hashlib
import io
import json
import os
import pathlib
import re
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIELDS = ['rank', 'band', 'title', 'nodes', 'match', 'verdict']


def headings(lines):
    fence = None
    for i, line in enumerate(lines):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        match = re.match(r'^ {0,3}(#{1,6})[ \t]+(.+?)\s*$', line)
        if match:
            yield i, len(match.group(1)), re.sub(r'[ \t]+#+[ \t]*$', '', match.group(2))
        elif i + 1 < len(lines) and line.strip():
            underline = re.fullmatch(r' {0,3}(=+|-+)[ \t]*\r?\n?', lines[i + 1])
            if underline:
                yield i, 1 if underline.group(1)[0] == '=' else 2, line.strip()


def write_json(path, value):
    pathlib.Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def remove(args):
    if pathlib.Path(args.skill_folder).is_symlink():
        raise ValueError('symlinks are not allowed in the source skill: ' + str(args.skill_folder))
    source = pathlib.Path(args.skill_folder).resolve()
    target = pathlib.Path(args.out).resolve()
    relative = pathlib.Path(args.file)
    if not source.is_dir():
        raise ValueError('skill folder does not exist')
    if target == source or source in target.parents:
        raise ValueError('work directory must be outside the source skill')
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('--file must stay inside the skill folder')
    path = source / relative
    for directory, dirs, files in os.walk(str(source)):
        for name in dirs + files:
            entry = pathlib.Path(directory) / name
            if entry.is_symlink():
                raise ValueError('symlinks are not allowed in the source skill: ' +
                                 entry.relative_to(source).as_posix())
    if source not in path.resolve().parents:
        raise ValueError('--file must stay inside the skill folder')
    lines = path.read_bytes().decode('utf-8').splitlines(keepends=True)
    entries = list(headings(lines))
    selected = []
    for title in args.heading:
        matches = [entry for entry in entries if entry[2] == title]
        if not matches:
            raise ValueError('heading not found: ' + title)
        if len(matches) != 1:
            raise ValueError('heading is ambiguous: ' + title)
        start, level, _ = matches[0]
        end = next((i for i, depth, _ in entries if i > start and depth <= level), len(lines))
        if any(start < b and a < end for a, b, _ in selected):
            raise ValueError('requested sections overlap: ' + title)
        selected.append((start, end, title))
    if target.exists():
        raise ValueError('work directory already exists; choose a new --out')
    target.mkdir(parents=True)
    try:
        shutil.copytree(str(source), str(target / 'altered'),
                        ignore=shutil.ignore_patterns('.git', '.hg', '.svn'))
        (target / 'removed').mkdir()
        items, removed_texts = [], []
        for n, (start, end, title) in enumerate(selected, 1):
            text = ''.join(lines[start:end]).encode('utf-8')
            removed_texts.append(text)
            item_id = 'R' + str(n)
            (target / 'removed' / (item_id + '.md')).write_bytes(text)
            item = dict(id=item_id, file=relative.as_posix(), heading=title,
                        removed_line_range=[start + 1, end], line_count=end - start,
                        sha256=hashlib.sha256(text).hexdigest())
            if args.node:
                item['nodes'] = args.node
            items.append(item)
        retained = [line for i, line in enumerate(lines) if not any(a <= i < b for a, b, _ in selected)]
        altered = target / 'altered'
        (altered / relative).write_bytes(''.join(retained).encode('utf-8'))
        leaks = []
        for entry in sorted(altered.rglob('*')):
            if entry.is_file():
                content = entry.read_bytes()
                if any(text in content for text in removed_texts):
                    leaks.append(entry.relative_to(altered).as_posix())
        if leaks:
            raise ValueError('removed section text remains in altered files: ' + ', '.join(leaks))
        write_json(target / 'key.json', dict(source_skill=str(source), source_url=args.source_url, items=items))
    except Exception:
        shutil.rmtree(str(target))
        raise
    print('Removed {} section(s); key: {}'.format(len(items), target / 'key.json'))


def findings(args):
    lines = pathlib.Path(args.report).read_text(encoding='utf-8').splitlines(keepends=True)
    entries = list(headings(lines))
    start = next((i for i, depth, title in entries if depth == 2 and title == 'Findings'), None)
    if start is None:
        raise ValueError('report has no ## Findings section')
    end = next((i for i, depth, _ in entries if i > start and depth <= 2), len(lines))
    band = None
    rows = []
    current = None
    for line in lines[start + 1:end]:
        heading = re.match(r'^###\s+(.+?)\s*$', line)
        if heading:
            band = heading.group(1)
            current = None
        item = re.match(r'^\s*(\d+)\.\s+\*\*(.+?)\*\*\s*(?:\[[^\]]*\])?\s*$', line)
        if item and band in {'Needed', 'Worth considering', 'Minor'}:
            current = dict(zip(FIELDS, [item.group(1), band, item.group(2), '', '', '']))
            rows.append(current)
        node = re.match(r'^\s*Map nodes?:\s*(.*)', line)
        if node and current is not None:
            nodes = node.group(1).split(' — ')[0].split(' - source:')[0]
            current['nodes'] = nodes.strip().strip('`')
    output = io.StringIO(newline='')
    writer = csv.DictWriter(output, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(rows)
    if args.out:
        pathlib.Path(args.out).write_text(output.getvalue(), encoding='utf-8')
        print('Wrote {} findings: {}'.format(len(rows), args.out))
    else:
        print(output.getvalue(), end='')


def score(args):
    if args.top < 1:
        raise ValueError('--top must be positive')
    key = json.loads(pathlib.Path(args.key).read_text(encoding='utf-8'))
    ids = [item['id'] for item in key['items']]
    if len(set(ids)) != len(ids):
        raise ValueError('duplicate key ids')
    recovered, within, ranks = set(), set(), set()
    false = 0
    with pathlib.Path(args.marks).open(encoding='utf-8', newline='') as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            raise ValueError('CSV columns must be: ' + ','.join(FIELDS))
        for row in reader:
            rank = int(row['rank'])
            if rank < 1 or rank in ranks:
                raise ValueError('ranks must be positive and unique')
            ranks.add(rank)
            verdict, match = row['verdict'].strip(), row['match'].strip()
            if verdict not in {'real', 'false'}:
                raise ValueError('each verdict must be real or false (finish marking first)')
            if match and match not in ids:
                raise ValueError('unknown key id: ' + match)
            if match and verdict == 'false':
                raise ValueError('a false positive cannot recover a key item')
            false += verdict == 'false'
            if match:
                recovered.add(match)
                if rank <= args.top:
                    within.add(match)
    result = dict(kind='scored', name=pathlib.Path(args.marks).stem, key=str(args.key),
                  total=len(ids), recovered=len(recovered), top=args.top,
                  recovered_top_n=len(within), recovery_rate=len(recovered) / len(ids) if ids else None,
                  false_positives=false, unmatched=[item for item in ids if item not in recovered])
    if args.out:
        write_json(args.out, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def summary(args):
    paths = [pathlib.Path(p) for p in args.results] if args.results else sorted((HERE / 'data').glob('*.json'))
    print('| Test / method | Recovered | Top N | Shared across runs | False positives |')
    print('|---|---|---|---|---|')
    for path in paths:
        data = json.loads(path.read_text(encoding='utf-8'))
        if data.get('kind') == 'recorded':
            for test in data['tests']:
                for method in test['methods']:
                    shared = method.get('shared')
                    print('| {} / {} | {}/{} | {} | {} | not recorded |'.format(
                        test['name'], method['name'], method['recovered'], test['chances'],
                        method.get('top', 'not recorded'),
                        'about {}/30'.format(shared) if shared is not None else 'not recorded'))
        else:
            print('| {} | {}/{} | {}/{} within {} | — | {} |'.format(
                str(data['name']).replace('|', '\\|'), data['recovered'], data['total'],
                data['recovered_top_n'], data['total'], data['top'], data['false_positives']))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest='command', required=True)
    command = commands.add_parser('remove')
    command.add_argument('skill_folder')
    command.add_argument('--heading', action='append', required=True)
    command.add_argument('--file', default='SKILL.md')
    command.add_argument('--node', action='append')
    command.add_argument('--source-url')
    command.add_argument('--out', required=True)
    command = commands.add_parser('findings')
    command.add_argument('report')
    command.add_argument('--out')
    command = commands.add_parser('score')
    command.add_argument('key')
    command.add_argument('marks')
    command.add_argument('--top', type=int, default=10)
    command.add_argument('--out')
    command = commands.add_parser('summary')
    command.add_argument('results', nargs='*')
    args = parser.parse_args()
    try:
        globals()[args.command](args)
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(2, 'error: {}\n'.format(error))


if __name__ == '__main__':
    main()
