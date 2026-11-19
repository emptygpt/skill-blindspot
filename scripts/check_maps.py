#!/usr/bin/env python3
"""Check every map in skills/blindspot/maps/: structure, unique ids, and that every node cites a defined source.
Also checks that maps/maps.json (the resolved copy read by skills/blindspot/scripts/blindspot.py) is up to date.

Usage: python3 scripts/check_maps.py            check
       python3 scripts/check_maps.py --write    check, then rewrite maps.json
Needs PyYAML. Exits 1 if any map fails or maps.json is stale.
"""
import datetime
import json
import pathlib
import re
import sys
from urllib.parse import urlsplit

import yaml

MAPS = pathlib.Path(__file__).resolve().parent.parent / "skills" / "blindspot" / "maps"


def load(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def records(parent, key, *, required=False):
    values = parent.get(key, [])
    if (not isinstance(values, list) or not all(isinstance(v, dict) for v in values)
            or (required and not values)):
        raise ValueError(f"{key} must be a {'non-empty ' if required else ''}list of records")
    return values


def require_text(record, key, label):
    value = record.get(key)
    if not nonblank(value):
        raise ValueError(f"{label}.{key} must be non-empty text")
    return value


def valid_url(value):
    if re.search(r"\s", value):
        return False
    try:
        url = urlsplit(value)
        return url.scheme in ("http", "https") and bool(url.hostname)
    except ValueError:
        return False


def valid_date(value):
    if type(value) is datetime.date:
        return True
    if not isinstance(value, str):
        return False
    try:
        return datetime.date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def add_id(seen, value, label):
    if value in seen:
        raise ValueError(f"duplicate {label} id {value!r} (including inherited ids)")
    seen.add(value)


def validate_map(name, docs, validated, ancestors=()):
    if name in validated:
        return validated[name]
    if name in ancestors:
        raise ValueError("extends cycle: " + " -> ".join((*ancestors, name)))

    doc = docs[name]
    meta = doc.get("map") if isinstance(doc, dict) else None
    if not isinstance(meta, dict):
        raise ValueError(f"{name}: map must be a record")
    if meta.get("id") != name:
        raise ValueError(f"{name}: map.id {meta.get('id')!r} does not match file name")
    for key in ("title", "version", "updated", "scope"):
        if not meta.get(key):
            raise ValueError(f"{name}: map.{key} is missing")

    sources, groups, nodes, excluded = set(), set(), set(), set()
    base = meta.get("extends")
    if "extends" in meta:
        if not nonblank(base) or base not in docs:
            raise ValueError(f"{name}: extends unknown map {base!r}")
        sources, groups, nodes, excluded = (
            ids.copy() for ids in validate_map(base, docs, validated, (*ancestors, name))
        )

    for source in records(doc, "sources"):
        sid = require_text(source, "id", "source")
        add_id(sources, sid, "source")
        label = f"source {sid}"
        for key in ("title", "publisher", "licence"):
            require_text(source, key, label)
        if not valid_url(require_text(source, "url", label)):
            raise ValueError(f"{label}.url must be an HTTP(S) URL")
        if not valid_date(source.get("retrieved")):
            raise ValueError(f"{label}.retrieved must be a YYYY-MM-DD date")

    for entry in records(doc, "exclude"):
        nid = require_text(entry, "node", "exclude")
        if nid not in nodes or nid in excluded:
            raise ValueError(f"exclude names unknown or already excluded base node {nid!r}")
        excluded.add(nid)

    for group in records(doc, "groups", required=True):
        gid = require_text(group, "id", "group")
        if not re.fullmatch(r"[a-z][a-z0-9-]*", gid):
            raise ValueError(f"invalid group id {gid!r}")
        add_id(groups, gid, "group")
        require_text(group, "title", f"group {gid}")
        for node in records(group, "nodes", required=True):
            nid = require_text(node, "id", "node")
            add_id(nodes, nid, "node")
            for key in ("title", "description"):
                require_text(node, key, nid)
            kw = node.get("keywords")
            if kw is not None and not (isinstance(kw, list) and all(map(nonblank, kw))):
                raise ValueError(f"{nid}: keywords must be a list of strings")
            for ref in records(node, "sources", required=True):
                sid = require_text(ref, "ref", nid)
                if sid not in sources:
                    raise ValueError(f"{nid}: source {sid!r} is not defined")
                require_text(ref, "locator", f"{nid}: source {sid!r}")
    validated[name] = (sources, groups, nodes, excluded)
    return validated[name]


def main():
    docs = {}
    try:
        for path in sorted(MAPS.glob("*.yaml")):
            docs[path.stem] = load(path)
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"FAIL {path.name}: {error}")
        return 1
    validated = {}
    failed = False
    for name, doc in docs.items():
        try:
            validate_map(name, docs, validated)
        except ValueError as error:
            print(f"FAIL {name}: {error}")
            failed = True
            continue
        base = doc["map"].get("extends")
        extra = f", extends {base}, excludes {len(doc.get('exclude', []))}" if base else ""
        count = sum(len(group["nodes"]) for group in doc["groups"])
        print(f"ok   {name}: {count} nodes{extra}")
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
