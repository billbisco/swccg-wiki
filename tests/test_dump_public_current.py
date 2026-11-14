"""Offline all-public export fixtures; no network or credentials are used."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import dump_public_current as dump


def page(page_id, namespace, title, text):
    raw = text.encode("utf-8")
    return {"pageid": page_id, "ns": namespace, "title": title, "revisions": [{
        "revid": page_id * 10, "parentid": page_id * 10 - 1,
        "timestamp": "2026-01-01T00:00:00Z", "sha1": hashlib.sha1(raw).hexdigest(),
        "size": len(raw), "slots": {"main": {"contentmodel": "wikitext", "content": text}},
    }]}


class Fixture:
    def __init__(self, pages, namespaces=None, closing_extra=None):
        self.pages = pages
        self.namespaces = namespaces or sorted({p["ns"] for p in pages} | {-2, -1, 0})
        self.closing_extra = closing_extra or []
        self.calls = []

    def __call__(self, params):
        self.calls.append(dict(params))
        if params.get("meta") == "siteinfo":
            return {"query": {"namespaces": {str(ns): {"id": ns} for ns in self.namespaces}}}
        if params.get("generator") == "allpages":
            selected = [p for p in self.pages if p["ns"] == int(params["gapnamespace"])]
            start, limit = int(params.get("gapcontinue", 0)), int(params["gaplimit"])
            result = {"query": {"pages": selected[start:start + limit]}}
            if start + limit < len(selected):
                result["continue"] = {"gapcontinue": str(start + limit), "continue": "gapcontinue||"}
            return result
        if params.get("list") == "allpages":
            selected = [p for p in self.pages + self.closing_extra if p["ns"] == int(params["apnamespace"])]
            return {"query": {"allpages": [{k: p[k] for k in ("pageid", "ns", "title")} for p in selected]}}
        if "pageids" in params:
            wanted = set(map(int, params["pageids"].split("|")))
            return {"query": {"pages": [p for p in self.pages + self.closing_extra if p["pageid"] in wanted]}}
        raise AssertionError(params)


class PublicDumpTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / ".git").mkdir()

    def run_dump(self, fixture, batch_size=50):
        return dump.Exporter(self.root, fixture, batch_size=batch_size).run()

    def metadata(self, namespace):
        path = self.root / f"pages/public-current/ns-{namespace}.jsonl"
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

    def test_all_nonnegative_namespaces_and_exact_empty_newline_unicode_bytes(self):
        samples = [page(1, 0, "Article", "no final newline\r\n雪"),
                   page(2, 1, "Talk:Article", "talk\n"), page(3, 2, "User:Example", "user"),
                   page(4, 6, "File:Example.png", "")]
        fixture = Fixture(samples)
        manifest = self.run_dump(fixture)
        self.assertEqual(manifest["public_namespaces"], [0, 1, 2, 6])
        self.assertEqual(manifest["captured_pages"], 4)
        self.assertEqual(manifest["closing_inventory_pages"], 4)
        for source in samples:
            raw = source["revisions"][0]["slots"]["main"]["content"].encode("utf-8")
            self.assertEqual((self.root / f"pages/by-id/{source['pageid']}.wiki").read_bytes(), raw)
            record = self.metadata(source["ns"])[0]
            self.assertEqual(record["sha256"], hashlib.sha256(raw).hexdigest())
            self.assertEqual(record["mediawiki_sha1"], hashlib.sha1(raw).hexdigest())
            self.assertEqual(record["bytes"], len(raw))
        self.assertTrue(all(int(call.get("gapnamespace", 0)) >= 0 for call in fixture.calls))
        self.assertIn("not an atomic database snapshot", manifest["membership_semantics"])

    def test_existing_canonical_paths_preserved_and_new_titles_use_numeric_paths(self):
        (self.root / "pages").mkdir()
        (self.root / "pages/INDEX.tsv").write_text("Existing\tpages/custom/Existing.wiki\n")
        manifest = self.run_dump(Fixture([page(1, 0, "Existing", "exact"), page(2, 1, "Talk:New/?*", "new")]))
        index = (self.root / "pages/INDEX.tsv").read_text()
        self.assertIn("Existing\tpages/custom/Existing.wiki\n", index)
        self.assertIn("Talk:New/?*\tpages/by-id/2.wiki\n", index)
        self.assertEqual((self.root / "pages/custom/Existing.wiki").read_bytes(), b"exact")
        self.assertEqual(manifest["captured_pages"], 2)

    def test_old_filename_collision_retains_both_numeric_payloads(self):
        (self.root / "pages").mkdir()
        (self.root / "pages/INDEX.tsv").write_text("A/B\tpages/A_B.wiki\nA:B\tpages/A_B.wiki\n")
        (self.root / "pages/A_B.wiki").write_text("old alias")
        manifest = self.run_dump(Fixture([page(1, 0, "A/B", "first"), page(2, 0, "A:B", "second")]))
        self.assertEqual((self.root / "pages/by-id/1.wiki").read_bytes(), b"first")
        self.assertEqual((self.root / "pages/by-id/2.wiki").read_bytes(), b"second")
        self.assertEqual((self.root / "pages/A_B.wiki").read_text(), "old alias")
        self.assertEqual(manifest["canonical_alias_collisions"], {"pages/A_B.wiki": ["A/B", "A:B"]})

    def test_recreated_title_cannot_overwrite_another_numeric_payload(self):
        (self.root / "pages").mkdir()
        (self.root / "pages/INDEX.tsv").write_text("Recreated\tpages/by-id/1.wiki\n")
        manifest = self.run_dump(Fixture([page(1, 0, "Other", "one"), page(2, 0, "Recreated", "two")]))
        self.assertEqual((self.root / "pages/by-id/1.wiki").read_bytes(), b"one")
        self.assertEqual((self.root / "pages/by-id/2.wiki").read_bytes(), b"two")
        self.assertEqual(manifest["numeric_alias_replacements"], {"Recreated": "pages/by-id/1.wiki"})

    def test_hidden_revision_content_is_excluded_without_payload_or_secret(self):
        hidden = page(1, 0, "Public title", "suppressed secret")
        hidden["revisions"][0]["texthidden"] = True
        manifest = self.run_dump(Fixture([hidden]))
        self.assertEqual(manifest["captured_pages"], 0)
        self.assertEqual(manifest["excluded_pages"][0]["excluded"], "revision_content_not_public")
        self.assertFalse((self.root / "pages/by-id/1.wiki").exists())
        self.assertNotIn("suppressed secret", json.dumps(manifest))

    def test_no_revision_at_cutoff_is_explicitly_excluded(self):
        later = {"pageid": 1, "ns": 0, "title": "Created after cutoff", "revisions": []}
        manifest = self.run_dump(Fixture([later]))
        self.assertEqual(manifest["captured_pages"], 0)
        self.assertEqual(manifest["closing_inventory_pages"], 1)
        self.assertEqual(manifest["excluded_pages"][0]["excluded"], "no_public_revision_at_cutoff")

    def test_sha1_size_mismatch_and_missing_content_fail_before_completed_manifest(self):
        for mutation in (lambda p: p["revisions"][0].update(size=999),
                         lambda p: p["revisions"][0]["slots"]["main"].pop("content")):
            sample = page(1, 0, "Article", "text")
            mutation(sample)
            with self.assertRaises(dump.ExportError):
                self.run_dump(Fixture([sample]))
            self.assertFalse((self.root / "pages/public-current/manifest.json").exists())

    def test_interrupted_continuation_resumes_at_checkpoint_and_preserves_cutoff(self):
        fixture = Fixture([page(1, 0, "A", "one"), page(2, 0, "B", "two")])

        def interrupted(params):
            if params.get("generator") and params.get("gapcontinue") == "1":
                raise dump.ExportError("fixture interruption")
            return fixture(params)

        with self.assertRaisesRegex(dump.ExportError, "fixture interruption"):
            self.run_dump(interrupted, batch_size=1)
        state_path = self.root / ".git/wiki-public-export/state.json"
        state = json.loads(state_path.read_text())
        self.assertEqual(state["batches"], 1)
        self.assertFalse((self.root / "pages/by-id/1.wiki").exists())
        fixture.calls.clear()
        manifest = self.run_dump(fixture, batch_size=1)
        first_scan = next(c for c in fixture.calls if c.get("generator"))
        self.assertEqual(first_scan["gapcontinue"], "1")
        self.assertEqual(manifest["revision_cutoff"], state["cutoff"])
        self.assertEqual(manifest["captured_pages"], 2)

    def test_closing_inventory_reconciles_page_missed_by_first_scan(self):
        fixture = Fixture([page(1, 0, "A", "one")], closing_extra=[page(2, 0, "B", "two")])
        manifest = self.run_dump(fixture)
        self.assertEqual(manifest["captured_pages"], 2)
        self.assertTrue(any(c.get("pageids") == "2" for c in fixture.calls))

    def test_corrupted_resume_payload_cannot_be_published(self):
        fixture = Fixture([page(1, 0, "A", "one")])
        self.run_dump(fixture)
        (self.root / ".git/wiki-public-export/payloads/1").write_bytes(b"modified")
        with self.assertRaisesRegex(dump.ExportError, "SHA256 readback"):
            self.run_dump(fixture)

    def test_api_error_never_becomes_silent_empty_namespace_success(self):
        fixture = Fixture([page(1, 0, "A", "one")])

        def broken(params):
            return {"error": {"code": "maxlag"}} if params.get("generator") else fixture(params)

        with self.assertRaisesRegex(dump.ExportError, "API returned an error"):
            self.run_dump(broken)
        self.assertFalse((self.root / "pages/public-current/manifest.json").exists())


if __name__ == "__main__":
    unittest.main()
