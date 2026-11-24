#!/usr/bin/env python3
"""Helper for the blindspot skill. Python 3.8+, standard library only.

It does the mechanical parts of an audit with code, so the model spends its
tokens on judgement:

  prepare  read the skill folder and build a worksheet: files read, files the
           skill mentions that are missing, its headings, and for every map
           node the lines of the skill that look related
  grep     search every file under one or more folders, code included, for
           the words of a finding before it is rated Needed
  sources  print the sources of some map nodes, for the report
  checklist  before a skill is written: the map's nodes as a design checklist,
           one source each, minus the groups outside the planned skill
  lint     check a finished report against the map: unknown node ids, nodes
           missing from the table, absent or shallow nodes that no finding
           mentions, counts that do not add up; with --skill, verify evidence
           quotes in covered and shallow rows against the audited files
  diff     compare two audit reports by map node id, with before/after evidence

Usage:
  python3 blindspot.py prepare <skill-folder> --map <id> --out worksheet.md
           (writes worksheet.md and worksheet-nodes.md; open the nodes file in step 3)
  python3 blindspot.py grep <folder> [<folder> ...] -e <term> [-e <term> ...]
  python3 blindspot.py sources --map <id> <node-id> [<node-id> ...]
  python3 blindspot.py lint <report.md> --map <id> [--skill <skill-folder> [--skill <delegated-path>] ...] [--profile <.blindspot.yaml>]
  python3 blindspot.py diff <old-report.md> <new-report.md> [--map <id>]
  python3 blindspot.py checklist --map <id> [--skip <group> ...] [--out checklist.md]
  python3 blindspot.py checklist --map <id> --groups    (list group ids to skip)
  python3 blindspot.py maps

A keyword hit is a hint, not a verdict. A node with no hit can still be
covered in other words, and a hit can be a different thing with the same word.
"""
import argparse
import json
import pathlib
import re
import string
import sys
from urllib.parse import unquote, urlsplit

HERE = pathlib.Path(__file__).resolve().parent
MAPS_JSON = HERE.parent / "maps" / "maps.json"

PROSE_EXT = {".md", ".markdown", ".txt", ".rst"}
DATA_EXT = {".yaml", ".yml", ".json", ".toml", ".csv", ".tsv", ".html", ".xml"}
CODE_EXT = {".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".sh", ".bash", ".ps1", ".rb", ".go", ".rs", ".java", ".kt", ".swift", ".php", ".lua"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".next"}
MAX_FILE_BYTES = 400_000
MAX_TOTAL_BYTES = 3_000_000
STATES = {"covered", "shallow", "absent", "not-applicable", "excluded", "undetermined"}

STOP = set("""
a an and are as at be been before being by can do does each for from has have how in into is it its
may more most must not of on or other over own so such than that the their them then there these
they this those to under up use used uses using was were what when where which while who will with
within without would your you any all also only one two three first after same new make made makes
making keep kept give gives given get gets set sets need needs needed every very per via e.g i.e
""".split())


def load_maps():
    try:
        return json.loads(MAPS_JSON.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeError) as error:
        raise ValueError(f"{MAPS_JSON}: {error}") from None


def resolve(maps, map_id):
    """Combined node list for a map, following extends and dropping excluded base nodes."""
    if map_id not in maps:
        sys.exit(f"unknown map {map_id!r}; known: {', '.join(sorted(maps))}")
    chain, seen = [], set()
    current = map_id
    while current:
        if current in seen:
            raise ValueError(f"extends cycle while resolving {map_id!r}: {current!r} repeats")
        if current not in maps:
            raise ValueError(f"unknown map {current!r} in extends chain of {map_id!r}")
        seen.add(current)
        chain.append(maps[current])
        current = maps[current]["map"].get("extends")
    chain.reverse()
    excluded = {e["node"] for d in chain for e in d.get("exclude") or []}
    sources, groups = {}, []
    for d in chain:
        for s in d.get("sources") or []:
            sources[s["id"]] = s
        for g in d.get("groups") or []:
            nodes = [n for n in g.get("nodes") or [] if n["id"] not in excluded]
            if nodes:
                groups.append({"id": g["id"], "title": g.get("title", g["id"]), "nodes": nodes})
    label = " extends ".join(f"{d['map']['id']} {d['map']['version']}" for d in reversed(chain))
    return {"label": label, "scope": chain[-1]["map"].get("scope", ""), "sources": sources,
            "groups": groups, "excluded": excluded}


# ---------- reading the skill ----------

def read_skill(folder):
    folder = pathlib.Path(folder).resolve()
    if not (folder / "SKILL.md").exists():
        sys.exit(f"no SKILL.md in {folder}")
    texts, code, data, skipped, total = {}, [], [], [], 0
    skill_text = (folder / "SKILL.md").read_text(encoding="utf-8", errors="replace")
    order = [folder / "SKILL.md"] + sorted(p for p in folder.rglob("*") if p.is_file() and p != folder / "SKILL.md")
    for p in order:
        rel = p.relative_to(folder).as_posix()
        if any(part in SKIP_DIRS for part in p.relative_to(folder).parts):
            continue
        ext = p.suffix.lower()
        if ext in CODE_EXT:
            code.append(rel)
            continue
        if p.name.upper().startswith(("LICENSE", "LICENCE", "COPYING", "NOTICE")):
            continue
        # prose is read; data files only when SKILL.md names them
        if ext in DATA_EXT and texts and (p.name not in skill_text):
            data.append(rel)
            continue
        if ext not in PROSE_EXT and ext not in DATA_EXT:
            continue
        size = p.stat().st_size
        if size > MAX_FILE_BYTES or total + size > MAX_TOTAL_BYTES:
            skipped.append(f"{rel} ({size} bytes)")
            continue
        try:
            texts[rel] = p.read_text(encoding="utf-8", errors="replace").splitlines()
            total += size
        except OSError:
            skipped.append(rel)
    return folder, texts, code, data, skipped


LINK_TARGET = r"""\]\(([^\s)]+)(?:\s+(?:"[^"\n]*"|'[^'\n]*'|\([^)\n]*\)))?\s*\)"""
LINK_RE = re.compile(LINK_TARGET)
LINK_TEXT_RE = re.compile(r"(?:\[[^\]\n]*)?" + LINK_TARGET)
PROSE_RE = re.compile(r"(?<![\w/.$-])((?:\.{1,2}/)?[\w.-]+(?:/[\w.-]+)*\.(?:md|txt))\b")


def missing_references(folder, texts):
    """Missing local references, relative to the prose file containing them."""
    out, seen = [], set()
    for rel, lines in texts.items():
        for i, line in enumerate(lines, 1):
            refs = [(ref, False) for ref in LINK_RE.findall(line)]
            if not any(char in line for char in "├└│"):
                refs += [(ref, True) for ref in PROSE_RE.findall(LINK_TEXT_RE.sub("", line))]
            for ref, prose in refs:
                try:
                    parsed = urlsplit(ref)
                except ValueError:
                    continue
                path = unquote(parsed.path)
                key = (rel, path, prose)
                if parsed.scheme or parsed.netloc or not path or path.startswith(("/", "~", "$")) or key in seen:
                    continue
                seen.add(key)
                if not (folder / rel).parent.joinpath(path).exists() and not (prose and (folder / path).exists()):
                    out.append((rel, i, ref))
    return out


def headings(lines):
    out, fence = [], False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            fence = not fence
        elif not fence and re.match(r"#{1,4} ", line):
            out.append((i, line.strip()))
    return out


# ---------- matching ----------

WORD_RE = re.compile(r"[a-z][a-z0-9-]{2,}")
CJK_RE = re.compile(r"[㐀-鿿]")


def stem(word):
    word = word.strip("-")
    for suf in ("ations", "ation", "ings", "ing", "ies", "ed", "es", "s"):
        if len(word) > len(suf) + 3 and word.endswith(suf):
            word = word[: -len(suf)]
            break
    return word[:7]


def stems_of(text):
    return {stem(w) for w in WORD_RE.findall(text.lower()) if w not in STOP}


def node_terms(groups):
    """Key stems per node, (title, description), minus stems common across the map."""
    raw = {}
    for g in groups:
        for n in g["nodes"]:
            raw[n["id"]] = (stems_of(n["title"]), stems_of(n.get("description", "")))
    count = {}
    for t, d in raw.values():
        for x in t | d:
            count[x] = count.get(x, 0) + 1
    limit = max(4, int(len(raw) * 0.08))
    keep = lambda st: {x for x in st if count[x] <= limit and len(x) >= 4}
    return {nid: (keep(t), keep(d) - keep(t)) for nid, (t, d) in raw.items()}


def match(groups, texts, per_node=2):
    terms = node_terms(groups)
    lines = []
    for rel, ls in texts.items():
        fence = False
        for i, line in enumerate(ls, 1):
            if line.lstrip().startswith("```"):
                fence = not fence
            text = line.strip()
            if len(text) < 4:
                continue
            lines.append((rel, i, text, stems_of(text), text.lower()))
    result = {}
    for g in groups:
        for n in g["nodes"]:
            title_t, desc_t = terms[n["id"]]
            kws = [k.lower() for k in n.get("keywords") or []]
            scored = []
            for rel, i, text, st, low in lines:
                score = 2 * len(title_t & st) + len(desc_t & st)
                kw = [k for k in kws if k in low]
                if kw:
                    score += 2 * len(kw)
                if score >= (2 if rel == "SKILL.md" else 3):
                    scored.append((score, rel == "SKILL.md", rel, i, text))
            scored.sort(key=lambda x: (-(x[0] + (1 if x[1] else 0)), x[2] != "SKILL.md", x[2], x[3]))
            result[n["id"]] = (scored[:per_node], len(scored))
    return result


def read_profile(path):
    """Minimal reader for .blindspot.yaml: '- node: id' and '- finding: text' entries."""
    nodes, findings = set(), []
    if not path or not pathlib.Path(path).exists():
        return nodes, findings
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*-\s*(node|finding):\s*(.+?)\s*(#.*)?$", line)
        if m:
            val = m.group(2).strip().strip("\"'")
            (nodes.add(val) if m.group(1) == "node" else findings.append(val))
    return nodes, findings


def clip(text, n=150):
    text = re.sub(r"\s+", " ", text)
    return text if len(text) <= n else text[: n - 1] + "…"


# ---------- commands ----------

def cmd_prepare(args):
    maps = load_maps()
    m = resolve(maps, args.map)
    folder, texts, code, data, skipped = read_skill(args.skill)
    profile = args.profile or (folder / ".blindspot.yaml")
    excl_nodes, excl_findings = read_profile(profile)
    hits = match(m["groups"], texts)
    hit_all = match(m["groups"], texts, per_node=10_000)
    hit_all = {k: v[0] for k, v in hit_all.items()}
    total_nodes = sum(len(g["nodes"]) for g in m["groups"])
    has_cjk = any(CJK_RE.search(" ".join(ls[:200])) for ls in texts.values())

    out = [f"# Worksheet: {folder.name}", "",
           f"Map: {m['label']} ({total_nodes} nodes). Map scope: {m['scope']}", ""]
    out.append("## Files")
    out.append(f"- read ({len(texts)}): " + ", ".join(f"{rel} ({len(ls)})" for rel, ls in texts.items()))
    if code:
        out.append(f"- code, not read ({len(code)}): " + ", ".join(code[:40]) + (" …" if len(code) > 40 else ""))
    if data:
        out.append(f"- data files SKILL.md does not name, not read ({len(data)}): " + ", ".join(data[:20]) + (" …" if len(data) > 20 else ""))
    for s in skipped:
        out.append(f"- skipped, too large: {s}")
    miss = missing_references(folder, texts)
    for rel, i, ref in miss:
        out.append(f"- MISSING: {rel}:{i} mentions `{ref}`, not found")
    if has_cjk:
        out.append("- note: the skill has CJK text; keyword hits use the map's English wording and node keywords only, so expect more nodes without hits. Check those by reading.")
    out.append("")
    out.append("## SKILL.md headings")
    for i, h in headings(texts.get("SKILL.md", [])):
        out.append(f"- {i}: {h}")
    out.append("")
    if excl_nodes or excl_findings:
        out.append("## Profile")
        out += [f"- excluded node: {n}" for n in sorted(excl_nodes)]
        out += [f"- excluded finding: {f}" for f in excl_findings]
        out.append("")
    head_len = len(out)
    out.append("## Nodes")
    out.append("Each node with the skill lines that share its key words. `no hit` means no shared key words, not that it is absent.")
    no_hit = 0
    for g in m["groups"]:
        n_hit = sum(1 for n in g["nodes"] if hits[n["id"]][1])
        out.append("")
        out.append(f"### {g['id']}: {g['title']} ({n_hit}/{len(g['nodes'])} nodes with hits)")
        for n in g["nodes"]:
            top, count = hits[n["id"]]
            tag = " [excluded by profile]" if n["id"] in excl_nodes else ""
            out.append(f"- **{n['id']}**{tag}: {n['title']}. {clip(n.get('description', ''), 200)}")
            if not top:
                no_hit += 1
                out.append("  - no hit")
                continue
            in_skill = [f"{i}" for _, _, rel, i, _ in hit_all[n["id"]] if rel == "SKILL.md"][:4]
            if in_skill:
                out.append("  - SKILL.md lines " + ", ".join(in_skill))
            other = [(rel, i, text) for _, _, rel, i, text in top if rel != "SKILL.md"][:1]
            for rel, i, text in other:
                out.append(f"  - {rel}:{i}: {clip(text, 110)}")
    out.append("")
    out.append(f"Summary: {total_nodes} nodes, {total_nodes - no_hit} with hits, {no_hit} without.")
    if args.out:
        main_path = pathlib.Path(args.out)
        main_path.parent.mkdir(parents=True, exist_ok=True)
        nodes_path = main_path.with_name(main_path.stem + "-nodes" + main_path.suffix)
        main_path.write_text("\n".join(out[:head_len] + [f"Map nodes are in {nodes_path.name}. Open it in step 3, after the step 2 list is written."]) + "\n", encoding="utf-8")
        nodes_path.write_text("\n".join([out[0], ""] + out[head_len:]) + "\n", encoding="utf-8")
        print(f"wrote {main_path} and {nodes_path}: {total_nodes} nodes, {total_nodes - no_hit} with hits, {no_hit} without, {len(miss)} missing files")
    else:
        sys.stdout.write("\n".join(out) + "\n")


def cmd_grep(args):
    terms = [t.lower() for t in args.e]
    roots = [pathlib.Path(folder).resolve() for folder in args.folders]
    for root in roots:
        if not root.is_dir():
            sys.exit(f"grep root does not exist or is not a directory: {root}")
    shown = 0
    for root in roots:
        for p in sorted(root.rglob("*")):
            if not p.is_file() or any(part in SKIP_DIRS for part in p.relative_to(root).parts):
                continue
            if p.suffix.lower() not in PROSE_EXT | DATA_EXT | CODE_EXT and p.suffix:
                continue
            if p.stat().st_size > MAX_FILE_BYTES:
                continue
            try:
                lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
            except OSError:
                continue
            for i, line in enumerate(lines, 1):
                low = line.lower()
                hit = [t for t in terms if t in low]
                if hit:
                    shown += 1
                    if shown <= args.max:
                        print(f"{p.relative_to(root.parent)}:{i}: {clip(line.strip(), 160)}")
    if shown > args.max:
        print(f"... {shown - args.max} more lines; narrow the terms")
    if not shown:
        print("no match in " + ", ".join(args.folders))


def cmd_sources(args):
    m = resolve(load_maps(), args.map)
    nodes = {n["id"]: n for g in m["groups"] for n in g["nodes"]}
    status = 0
    for nid in args.nodes:
        n = nodes.get(nid)
        if not n:
            print(f"{nid}: unknown node in {args.map}", file=sys.stderr)
            status = 1
            continue
        print(f"{nid}: {n['title']}")
        for s in n.get("sources") or []:
            src = m["sources"].get(s["ref"], {})
            print(f"  - {src.get('title', s['ref'])}, \"{s.get('locator', '')}\" <{src.get('url', '')}>")
    return status


MARKDOWN_ESCAPE_RE = re.compile(r"\\([" + re.escape(string.punctuation) + r"])")
EVIDENCE_TOKEN_RE = re.compile(MARKDOWN_ESCAPE_RE.pattern + r'|["“”]')


def evidence_excerpts(evidence):
    tokens = list(EVIDENCE_TOKEN_RE.finditer(evidence))
    curly_pairs = {}
    open_curly = []
    for index, match in enumerate(tokens):
        if match[0] == '“':
            open_curly.append(index)
        elif match[0] == '”' and open_curly:
            curly_pairs[open_curly.pop()] = index

    straight_opening = None
    curly_end = -1
    for index, match in enumerate(tokens):
        if index <= curly_end:
            continue
        token = match[0]
        if straight_opening is not None:
            if token == '"':
                yield evidence[straight_opening.end():match.start()]
                straight_opening = None
        elif token == '"':
            straight_opening = match
        elif token == '“':
            if index in curly_pairs:
                curly_end = curly_pairs[index]
                yield evidence[match.end():tokens[curly_end].start()]
            else:
                yield None


def evidence_files(roots):
    for root in roots:
        if root.is_file():
            yield root
        else:
            for path in root.rglob("*"):
                if ".git" not in path.relative_to(root).parts and not path.is_symlink() and path.is_file():
                    yield path


def missing_evidence_quotes(roots, report, quotes):
    missing = set(quotes)
    for path in evidence_files(roots):
        if path == report:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "\x00" in text:
            continue
        normalized = " ".join(text.split())
        missing = {quote for quote in missing if quote not in normalized}
        if not missing:
            break
    return missing


def report_sections(text):
    sections = re.split(r"^## ", text, flags=re.M)
    return sections[0], {s.split("\n", 1)[0].strip().lower(): s for s in sections[1:]}


def find_report_section(sections, title):
    return next((v for k, v in sections.items() if k.startswith(title)), None)


def map_table_rows(table):
    for line in table.splitlines():
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if len(cells) < 2 or cells[0] in ("Node", "") or set(cells[0]) <= set("-: "):
            continue
        yield cells[0].strip("`* "), cells[1].strip("`* ").lower(), cells[1], cells[2:]


def map_groups(map_id):
    m = resolve(load_maps(), map_id)
    return {g["id"]: [n["id"] for n in g["nodes"]] for g in m["groups"]}


def group_targets(groups, key):
    return groups.get(key) or groups.get(key.rstrip(".*"))


def normalize_evidence_quote(excerpt):
    return " ".join(MARKDOWN_ESCAPE_RE.sub(r"\1", excerpt).split())


def cmd_lint(args):
    groups = map_groups(args.map)
    all_nodes = {nid for ids in groups.values() for nid in ids}
    report = pathlib.Path(args.report).resolve()
    text = report.read_text(encoding="utf-8")
    problems = []
    roots = [pathlib.Path(path).resolve() for path in args.skill]
    if roots and not (roots[0] / "SKILL.md").is_file():
        raise ValueError(f"no SKILL.md in {roots[0]}")
    for root in roots[1:]:
        if not root.is_file() and not root.is_dir():
            raise ValueError(f"evidence path is not a file or directory: {root}")

    header, sections = report_sections(text)
    table = find_report_section(sections, "map table")
    findings = find_report_section(sections, "findings") or ""
    if table is None:
        print("no '## Map table' section; nothing to check")
        return 1

    states = {}
    evidence_quotes = []
    for key, state, state_cell, rest in map_table_rows(table):
        if state not in STATES:
            problems.append(f"table: {key}: unknown state {state_cell!r}")
            continue
        targets = group_targets(groups, key) or ([key] if key in all_nodes else None)
        if targets is None:
            problems.append(f"table: {key!r} is not a node or group of {args.map}")
            continue
        if state == "undetermined" and (not rest or not rest[0]):
            problems.append(f"table: {key}: undetermined needs evidence")
        if roots and state in ("covered", "shallow") and rest:
            malformed_curly = False
            for excerpt in evidence_excerpts(rest[0]):
                if excerpt is None:
                    malformed_curly = True
                    continue
                quote = normalize_evidence_quote(excerpt)
                if quote:
                    evidence_quotes.append((key, quote))
            if malformed_curly:
                problems.append(f"table: {key}: malformed curly quote; use straight quotes for a literal unmatched curly mark")
        for nid in targets:
            if nid in states and states[nid] != state:
                problems.append(f"table: {nid} listed twice with different states")
            states[nid] = state

    if evidence_quotes:
        missing = missing_evidence_quotes(roots, report, (quote for _, quote in evidence_quotes))
        for key, quote in evidence_quotes:
            if quote in missing:
                problems.append(f"table: {key}: evidence quote not found in the Skill: {quote!r}")

    for nid in sorted(all_nodes - set(states)):
        problems.append(f"table: {nid} is missing")

    profile = args.profile
    if not profile:
        match_ = re.search(r"Profile:[ \t]*(.*?)(?=[ \t]{2,}(?:Date|Map):|$)", header, re.M)
        if match_:
            value = match_.group(1).strip().strip("`\"'")
            if value and value.lower() != "none":
                profile = report.parent / value
    if profile and not pathlib.Path(profile).is_file():
        problems.append(f"profile: file not found: {profile}")
    excl_nodes, _ = read_profile(profile)
    for nid, state in sorted(states.items()):
        if state == "excluded" and nid not in excl_nodes:
            problems.append(f"profile: {nid} is marked excluded but not listed in the active profile")
    for nid in sorted(excl_nodes & all_nodes):
        if states.get(nid) not in (None, "excluded"):
            problems.append(f"profile: {nid} is excluded but marked {states[nid]}")

    mentioned = set(re.findall(r"[a-z][a-z0-9-]*\.[a-z0-9.-]*[a-z0-9]", findings))
    for nid, st in sorted(states.items()):
        if st in ("absent", "shallow") and nid not in mentioned:
            problems.append(f"findings: {nid} is {st} in the table but no finding names it")
    for nid in sorted(mentioned):
        if nid not in all_nodes and pathlib.PurePosixPath(nid).suffix in PROSE_EXT | DATA_EXT | CODE_EXT:
            continue
        if "." in nid and nid.split(".")[0] in {k.split(".")[0] for k in all_nodes} and nid not in all_nodes and nid not in groups:
            problems.append(f"findings: {nid} is not a node of {args.map}")

    counts = {k: sum(1 for v in states.values() if v == k) for k in sorted(STATES)}
    cm = re.search(r"covered (\d+), shallow (\d+), absent (\d+), not-applicable (\d+)"
                   r"(?:, undetermined (\d+))?", table)
    if cm:
        want = dict(zip(("covered", "shallow", "absent", "not-applicable", "undetermined"),
                        (int(n or 0) for n in cm.groups())))
        got = {k: counts[k] for k in want}
        if want != got:
            problems.append(f"counts line says {want}, table has {got}")

    print(f"{len(states)}/{len(all_nodes)} nodes in table; " + ", ".join(f"{k} {v}" for k, v in counts.items()))
    for p in problems:
        print(f"- {p}")
    print("ok" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


def report_nodes(report, map_id):
    header, sections = report_sections(pathlib.Path(report).read_text(encoding="utf-8"))
    table = find_report_section(sections, "map table")
    if table is None:
        raise ValueError(f"{report}: no '## Map table' section")
    if not map_id:
        match_ = re.search(r"^Map:[ \t]*`?([a-z][a-z0-9-]*)", header, re.M)
        map_id = match_.group(1) if match_ else None

    groups = None
    nodes = {}
    for key, state, state_cell, rest in map_table_rows(table):
        if state not in STATES:
            raise ValueError(f"{report}: {key}: unknown state {state_cell!r}")
        if re.fullmatch(r"[a-z][a-z0-9-]*(?:\.[a-z0-9-]+)+", key):
            targets = [key]
        else:
            if groups is None:
                groups = map_groups(map_id) if map_id and map_id != "none" else {}
            targets = group_targets(groups, key)
            if not targets:
                raise ValueError(f"{report}: cannot expand group {key!r}; use explicit node IDs or --map")
        evidence = rest[0] if rest else ""
        for nid in targets:
            if nid in nodes and nodes[nid][0] != state:
                raise ValueError(f"{report}: {nid} listed twice with different states")
            nodes[nid] = state, evidence
    if not nodes:
        raise ValueError(f"{report}: no node rows in '## Map table'")
    return nodes


def quoted_evidence(evidence):
    return {normalize_evidence_quote(excerpt) for excerpt in evidence_excerpts(evidence)
            if excerpt is not None} - {""}


def coverage_change(before, after, old_evidence, new_evidence):
    coverage = {"absent": 0, "shallow": 1, "covered": 2}
    if before == "—":
        return "unchanged", "new report only"
    if after == "—":
        return "unchanged", "old report only"
    if before == after:
        return "unchanged", ""
    if {before, after} & {"excluded", "not-applicable"}:
        return "unchanged", "scope or profile change"
    if "undetermined" in (before, after):
        return "unchanged", "insufficient evidence to compare"
    if coverage[after] < coverage[before]:
        return "regressed", ""
    if after == "shallow":
        return "partially resolved", ""
    if not quoted_evidence(new_evidence) - quoted_evidence(old_evidence):
        return "partially resolved", "no new quoted evidence"
    return "resolved", ""


def cmd_diff(args):
    old = report_nodes(args.old_report, args.map)
    new = report_nodes(args.new_report, args.map)
    counts = {"resolved": 0, "partially resolved": 0, "unchanged": 0, "regressed": 0}
    rows = []
    for nid in sorted(old.keys() | new.keys()):
        before, old_evidence = old.get(nid, ("—", ""))
        after, new_evidence = new.get(nid, ("—", ""))
        change, note = coverage_change(before, after, old_evidence, new_evidence)
        counts[change] += 1
        rows.append((nid, before, after, change, note, old_evidence, new_evidence))

    print(f"{len(rows)} nodes; " + ", ".join(f"{change} {count}" for change, count in counts.items()))
    print("Unchanged includes non-comparable rows (see Note). Labels compare report evidence, not Skill behavior.\n")
    print("| Node | Before | After | Change | Note | Old evidence | New evidence |")
    print("|---|---|---|---|---|---|---|")
    for row in rows:
        print("| " + " | ".join(row) + " |")


def cmd_checklist(args):
    m = resolve(load_maps(), args.map)
    if args.groups:
        for g in m["groups"]:
            print(f"{g['id']}: {g['title']} ({len(g['nodes'])} nodes)")
        return 0
    skip = set(args.skip or [])
    unknown = skip - {g["id"] for g in m["groups"]}
    if unknown:
        sys.exit(f"unknown group(s): {', '.join(sorted(unknown))}; run with --groups to list them")
    kept = [g for g in m["groups"] if g["id"] not in skip]
    total = sum(len(g["nodes"]) for g in kept)
    out = [f"# Design checklist: {m['label']}", "",
           f"Map scope: {m['scope']}", "",
           f"{total} items in {len(kept)} groups."
           + (f" Left out as outside the planned skill: {', '.join(sorted(skip))}." if skip else ""), "",
           "Use it before writing the skill. For each item decide: the skill does it (say in which step),",
           "or it is left out on purpose (say why; later this goes in the profile). Every item cites where",
           "it comes from, so an answer can be checked instead of guessed. After the skill is written,",
           "run the audit with the same map to see what made it in.", ""]
    for g in kept:
        out += [f"## {g['title']} (`{g['id']}`)", ""]
        for n in g["nodes"]:
            line = f"- [ ] **{n['title']}** `{n['id']}`"
            if n.get("description"):
                line += f": {n['description'].strip()}"
            out.append(line)
            srcs = n.get("sources") or []
            for s_ in srcs[:args.max_sources]:
                src = m["sources"].get(s_["ref"], {})
                url = f" <{src['url']}>" if src.get("url") else ""
                out.append(f"  - {src.get('title', s_['ref'])}: \"{clip(s_.get('locator', ''), 120)}\"{url}")
            if len(srcs) > args.max_sources:
                out.append(f"  - {len(srcs) - args.max_sources} more: `sources --map {args.map} {n['id']}`")
        out.append("")
    text = "\n".join(out)
    if args.out:
        path = pathlib.Path(args.out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path} ({total} items, {len(text.encode('utf-8')) // 1024} KB)")
    else:
        print(text)
    return 0


def cmd_maps(_):
    maps = load_maps()
    for mid in sorted(maps):
        r = resolve(maps, mid)
        print(f"{mid}: {r['label']}, {sum(len(g['nodes']) for g in r['groups'])} nodes. {clip(r['scope'], 120)}")


def positive_int(value):
    try:
        count = int(value)
        if count > 0:
            return count
    except ValueError:
        pass
    raise argparse.ArgumentTypeError("must be a positive integer")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare"); p.add_argument("skill"); p.add_argument("--map", required=True)
    p.add_argument("--profile"); p.add_argument("--out")
    p = sub.add_parser("grep"); p.add_argument("folders", nargs="+"); p.add_argument("-e", action="append", required=True)
    p.add_argument("--max", type=int, default=40)
    p = sub.add_parser("sources"); p.add_argument("--map", required=True); p.add_argument("nodes", nargs="+")
    p = sub.add_parser("lint"); p.add_argument("report"); p.add_argument("--map", required=True); p.add_argument("--profile")
    p.add_argument("--skill", metavar="PATH", action="append", default=[],
                   help="audited Skill folder; repeat for delegated files or folders")
    p = sub.add_parser("diff", help="compare two reports of the same Skill")
    p.add_argument("old_report")
    p.add_argument("new_report")
    p.add_argument("--map", help="override both report headers when expanding group rows")
    p = sub.add_parser("checklist"); p.add_argument("--map", required=True); p.add_argument("--skip", nargs="+")
    p.add_argument("--groups", action="store_true"); p.add_argument("--out")
    p.add_argument("--max-sources", type=positive_int, default=1)
    sub.add_parser("maps")
    args = ap.parse_args()
    commands = {"prepare": cmd_prepare, "grep": cmd_grep, "sources": cmd_sources,
                "lint": cmd_lint, "diff": cmd_diff, "checklist": cmd_checklist, "maps": cmd_maps}
    try:
        return commands[args.cmd](args) or 0
    except (OSError, ValueError) as error:
        ap.exit(1, f"{args.cmd}: {error}\n")


if __name__ == "__main__":
    sys.exit(main())
