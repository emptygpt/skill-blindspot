import contextlib
import io
import pathlib
import tempfile
import unittest
from unittest.mock import patch

import yaml

import check_maps


def map_doc(name, base=None, ref=None):
    meta = dict(id=name, title=name, version="1.0", updated="2026-01-01", scope="Example")
    if base:
        meta["extends"] = base
    sources = [] if ref else [dict(id=name, title="Guide", publisher="Example", url="https://example.org",
                                  retrieved="2026-01-01", licence="not verified")]
    node = dict(id=f"{name}.node", title="Node", description="Review the example.",
                sources=[dict(ref=ref or name, locator="Review")])
    return dict(map=meta, sources=sources, groups=[dict(id=name, title="Group", nodes=[node])])


class MapValidationTests(unittest.TestCase):
    def test_valid_grandparent_source_and_exclusion(self):
        base = map_doc("base")
        middle = map_doc("middle", "base", ref="base")
        leaf = map_doc("leaf", "middle", ref="base")
        leaf["exclude"] = [{"node": "base.node"}]
        sources, groups, nodes, excluded = check_maps.validate_map(
            "leaf", {"base": base, "middle": middle, "leaf": leaf}, {})
        self.assertEqual(sources, {"base"})
        self.assertEqual(groups, {"base", "middle", "leaf"})
        self.assertEqual(nodes - excluded, {"middle.node", "leaf.node"})

    def test_source_fields_are_required(self):
        for field in ("id", "title", "publisher", "url", "retrieved", "licence"):
            with self.subTest(field=field):
                doc = map_doc("base")
                del doc["sources"][0][field]
                with self.assertRaisesRegex(ValueError, rf"\.{field}\b"):
                    check_maps.validate_map("base", {"base": doc}, {})

    def test_source_url_and_date_must_have_valid_forms(self):
        for field, value in (("url", "https://"), ("url", "../guide"), ("retrieved", "2026-02-30")):
            with self.subTest(field=field, value=value):
                doc = map_doc("base")
                doc["sources"][0][field] = value
                with self.assertRaisesRegex(ValueError, rf"\.{field}\b"):
                    check_maps.validate_map("base", {"base": doc}, {})

    def test_source_and_group_ids_cannot_be_duplicated(self):
        for key, label in (("sources", "source"), ("groups", "group")):
            with self.subTest(key=key):
                base, child = map_doc("base"), map_doc("child", "base")
                child[key].append(base[key][0])
                with self.assertRaisesRegex(ValueError, f"duplicate {label} id 'base'"):
                    check_maps.validate_map("child", {"base": base, "child": child}, {})
                base[key].append(base[key][0])
                with self.assertRaisesRegex(ValueError, f"duplicate {label} id 'base'"):
                    check_maps.validate_map("base", {"base": base}, {})

    def test_group_schema(self):
        for key, value, error in (("id", None, "group.id"), ("id", "bad.id", "invalid group id"),
                                  ("title", "", "group base.title"), ("nodes", {}, "nodes must be")):
            with self.subTest(key=key, value=value):
                doc = map_doc("base")
                doc["groups"][0][key] = value
                with self.assertRaisesRegex(ValueError, error):
                    check_maps.validate_map("base", {"base": doc}, {})

    def test_invalid_extends_chains(self):
        for base, error in (("ghost", "extends unknown map 'ghost'"), ("child", "child -> child"),
                            ("parent", "child -> parent -> child")):
            with self.subTest(base=base):
                docs = {"child": map_doc("child", base), "parent": map_doc("parent", "child")}
                with self.assertRaisesRegex(ValueError, error):
                    check_maps.validate_map("child", docs, {})

    def test_write_does_not_replace_cache_after_validation_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            doc = map_doc("base")
            del doc["sources"][0]["url"]
            (root / "base.yaml").write_text(yaml.safe_dump(doc), encoding="utf-8")
            cache = root / "maps.json"
            cache.write_text("previous cache", encoding="utf-8")
            with patch.object(check_maps, "MAPS", root), patch("sys.argv", ["check_maps.py", "--write"]):
                with contextlib.redirect_stdout(io.StringIO()) as out:
                    self.assertEqual(check_maps.main(), 1)
            self.assertIn("source base.url", out.getvalue())
            self.assertEqual(cache.read_text(encoding="utf-8"), "previous cache")
