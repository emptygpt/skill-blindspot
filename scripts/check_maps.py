#!/usr/bin/env python3
"""Check every map in skills/blindspot/maps/: structure, unique ids, and that every node cites a defined source.
Also checks that maps/maps.json (the resolved copy read by skills/blindspot/scripts/blindspot.py) is up to date.

Usage: python3 scripts/check_maps.py            check
       python3 scripts/check_maps.py --write    check, then rewrite maps.json
Needs PyYAML. Exits 1 if any map fails or maps.json is stale.
"""
import json
import pathlib
import sys

import yaml

MAPS = pathlib.Path(__file__).resolve().parent.parent / "skills" / "blindspot" / "maps"


def load(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def nodes_of(doc):
    return [(g["id"], n) for g in doc.get("groups") or [] for n in g.get("nodes") or []]


def main():
    docs = {p.stem: load(p) for p in sorted(MAPS.glob("*.yaml"))}
    failed = False
    for name, doc in docs.items():
        errors = []
        meta = doc.get("map") or {}
        if meta.get("id") != name:
            errors.append(f"map.id {meta.get('id')!r} does not match file name")
        for key in ("title", "version", "updated", "scope"):
            if not meta.get(key):
                errors.append(f"map.{key} is missing")
        sources = {s["id"] for s in doc.get("sources") or []}
        base_nodes = set()
        base = meta.get("extends")
        if base:
            if base not in docs:
                errors.append(f"extends unknown map {base!r}")
            else:
                sources |= {s["id"] for s in docs[base].get("sources") or []}
                base_nodes = {n["id"] for _, n in nodes_of(docs[base])}
        for entry in doc.get("exclude") or []:
            if entry.get("node") not in base_nodes:
                errors.append(f"exclude names unknown base node {entry.get('node')!r}")
        seen = set()
        for _, node in nodes_of(doc):
            nid = node.get("id")
            if not nid or nid in seen or nid in base_nodes:
                errors.append(f"node id missing or duplicated: {nid!r}")
            seen.add(nid)
            kw = node.get("keywords")
            if kw is not None and not (isinstance(kw, list) and all(isinstance(k, str) and k for k in kw)):
                errors.append(f"{nid}: keywords must be a list of strings")
            if not node.get("title") or not node.get("description"):
                errors.append(f"{nid}: title or description missing")
            refs = node.get("sources") or []
            if not refs:
                errors.append(f"{nid}: no source")
            for ref in refs:
                if ref.get("ref") not in sources:
                    errors.append(f"{nid}: source {ref.get('ref')!r} is not defined")
                if not ref.get("locator"):
                    errors.append(f"{nid}: source {ref.get('ref')!r} has no locator")
        status = "FAIL" if errors else "ok"
        extra = f", extends {base}, excludes {len(doc.get('exclude') or [])}" if base else ""
        print(f"{status:4} {name}: {len(seen)} nodes{extra}")
        for err in errors:
            print(f"     - {err}")
        failed = failed or bool(errors)
    if failed:
        return 1
    compiled = json.dumps(compile_maps(docs), ensure_ascii=False, separators=(",", ":")) + "\n"
    target = MAPS / "maps.json"
    if "--write" in sys.argv:
        target.write_text(compiled, encoding="utf-8")
        print(f"wrote {target.relative_to(MAPS.parent.parent.parent)}")
    elif not target.exists() or target.read_text(encoding="utf-8") != compiled:
        print("FAIL maps.json is missing or stale: run python3 scripts/check_maps.py --write")
        return 1
    else:
        print("ok   maps.json is up to date")
    return 0


def compile_maps(docs):
    """The same maps as JSON, so the runtime script needs no YAML parser. Dates become strings."""
    return json.loads(json.dumps(docs, default=str))


if __name__ == "__main__":
    sys.exit(main())
