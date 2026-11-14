import copy
import hashlib
import json
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "ops"), str(ROOT / "tools")]
from source_inventory import SourceInventory, NoRedirect, candidates, safe_open
from preservation_contracts import object_id, source_backup_subject
from preservation_registry import register


def receipt(subject, storage):
    return {"schema_version": 1, "subject": subject, "storage": storage,
            "verification": {"status": "verified", "independent": True,
                             "restored_sha256": subject["content_sha256"], "restored_bytes": subject["bytes"],
                             "verified_at": "2026-11-14T00:00:00Z"}}


class SourceInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.directory, self.registry = self.root / "inventory", self.root / "registry"
        self.text = "See [https://example.org/source#part source]."
        self.storage = {"kind": "git", "repository": "https://github.com/billbisco/swccg-wiki",
                        "commit": "a" * 40, "path": "preservation/objects/test.bin"}
        self.make_marker()

    def make_marker(self):
        self.subject = {"kind": "wiki_revision", "title": "Test", "revision_id": 42,
                        "content_sha256": hashlib.sha256(self.text.encode()).hexdigest(), "bytes": len(self.text.encode())}
        self.marker = {"schema_version": 1, "subject": self.subject, "backup_storage": self.storage,
                       "state": "source_inventory_required", "owner": "Earlier owner", "capture_submitted": False,
                       "continuation": "Earlier continuation"}
        self.directory.mkdir(exist_ok=True)
        self.path = self.directory / (object_id(self.subject) + ".json")
        self.path.write_text(json.dumps(self.marker))

    def readback(self, subject, storage, *, restore_to, fetch):
        restore_to.write_bytes(self.text.encode())
        return receipt(subject, storage)

    def consumer(self, **kwargs):
        return SourceInventory(self.directory, self.registry, readback=self.readback,
                               parse=kwargs.pop("parse", lambda revid, deadline: {"revid": revid, "externallinks": ["https://example.org/source"], "templates": []}), **kwargs)

    def report(self):
        marker = json.loads(self.path.read_text())
        report = self.directory / marker["source_inventory_report"]["path"]
        raw = report.read_bytes()
        self.assertEqual(marker["source_inventory_report"]["sha256"], hashlib.sha256(raw).hexdigest())
        return marker, json.loads(raw)

    def test_exact_restored_revision_creates_owned_source_obligation_without_network(self):
        result = self.consumer().run()
        self.assertEqual(1, result["source_inventory_processed_this_run"])
        marker, report = self.report()
        self.assertEqual("source_inventory_recorded", marker["state"])
        self.assertEqual("Earlier owner", marker["owner"])
        self.assertEqual("Earlier continuation", marker["continuation"])
        self.assertEqual(["literal_wikitext", "rendered_externallinks"], report["sources"][0]["origins"])
        self.assertEqual("source_check_required", report["sources"][0]["state"])
        self.assertFalse(report["source_accuracy_verified"])
        self.assertFalse(report["external_preservation_verified"])
        self.assertEqual(0, report["archive_requests"])
        self.assertEqual(0, self.consumer().run()["source_inventory_processed_this_run"])

    def test_rendered_template_links_are_inventoried_but_ambiguity_stays_unresolved(self):
        result = self.consumer(parse=lambda revid, deadline: {"revid": revid, "externallinks": ["https://example.org/from-template"], "templates": [{"title": "Template:Cite"}]}).run()
        marker, report = self.report()
        self.assertEqual("source_inventory_review_required", marker["state"])
        self.assertEqual(2, len(report["sources"]))
        self.assertIn("template_or_parser_expansion_needs_exact-source_review", report["unresolved_constructs"])

    def test_archive_candidate_is_durable_held_without_any_fetch(self):
        result = self.consumer(parse=lambda revid, deadline: {"revid": revid, "externallinks": ["https://web.archive.org/web/20200101000000/https://example.org/"], "templates": []}).run()
        marker, report = self.report()
        held = [row for row in report["sources"] if "archive.org" in row["url"]][0]
        self.assertEqual("provider_hold", held["state"])
        self.assertFalse(held["capture_submitted"])

    def test_peer_marker_advance_during_readback_is_preserved(self):
        consumer = self.consumer()
        original = consumer.readback
        peer = dict(self.marker, state="peer_reviewed", owner="Peer", continuation="Peer follow-up")
        def concurrent(*args, **kwargs):
            self.path.write_text(json.dumps(peer))
            return original(*args, **kwargs)
        consumer.readback = concurrent
        self.assertEqual(0, consumer.run()["source_inventory_processed_this_run"])
        self.assertEqual(peer, json.loads(self.path.read_text()))

    def test_hash_mismatch_leaves_original_marker_and_reports_failure(self):
        consumer = self.consumer()
        def corrupted(subject, storage, *, restore_to, fetch):
            restore_to.write_bytes(b"corrupt")
            return receipt(subject, storage)
        consumer.readback = corrupted
        self.assertEqual(1, len(consumer.run()["source_inventory_failures"]))
        self.assertEqual(self.marker, json.loads(self.path.read_text()))
        self.assertEqual([], consumer.run()["source_inventory_failures"])
        self.assertEqual("source_inventory_retry", json.loads((self.directory / "consumer-issues" / self.path.name).read_text())["state"])

    def test_wrong_parse_revision_cannot_drain_marker(self):
        consumer = self.consumer(parse=lambda revid, deadline: {"revid": 41, "externallinks": [], "templates": []})
        self.assertEqual(1, len(consumer.run()["source_inventory_failures"]))
        self.assertEqual(self.marker, json.loads(self.path.read_text()))

    def test_corrupt_marker_subject_cannot_fetch_anything(self):
        marker = dict(self.marker, subject=dict(self.subject, revision_id=43))
        self.path.write_text(json.dumps(marker))
        consumer = self.consumer()
        consumer.readback = lambda *args, **kwargs: self.fail("invalid identity fetched")
        self.assertEqual(1, len(consumer.run()["source_inventory_failures"]))

    def test_limits_expired_deadline_and_existing_owner_progress_are_noops(self):
        consumer = self.consumer()
        consumer.readback = lambda *args, **kwargs: self.fail("no work permitted")
        self.assertEqual(0, consumer.run(limit=0)["source_inventory_processed_this_run"])
        self.assertEqual(0, consumer.run(deadline=time.monotonic()-1)["source_inventory_processed_this_run"])
        self.path.write_text(json.dumps(dict(self.marker, state="inventory_reviewed")))
        self.assertEqual(0, consumer.run()["source_inventory_processed_this_run"])

    def test_exact_valid_registry_source_reused_without_mutation(self):
        source = {"url": "https://example.org/source", "sha256": "c" * 64, "bytes": 123,
                  "checked_evidence": {"path": "evidence/source.json", "sha256": "d" * 64}}
        source_subject = source_backup_subject(source)
        request = {"schema_version": 1, "subject": self.subject, "source": source,
                   "readiness": {"ready": True, "reason": "checked source", "stage_bytes": 0},
                   "backup_receipt": receipt(self.subject, self.storage),
                   "source_backup_receipt": receipt(source_subject, self.storage),
                   "owner": "Peer source checker", "continuation": "Keep provider hold",
                   "approval_scope": {"ticket": 410}}
        register(self.registry, request)
        before = {p.relative_to(self.registry).as_posix(): p.read_bytes() for p in self.registry.rglob("*.json")}
        self.consumer().run()
        _, report = self.report()
        self.assertEqual("registered_source_backup", report["sources"][0]["state"])
        after = {p.relative_to(self.registry).as_posix(): p.read_bytes() for p in self.registry.rglob("*.json")}
        self.assertEqual(before, after)

    def test_other_revision_cannot_lend_source_receipt(self):
        source = {"url": "https://example.org/source", "sha256": "c" * 64, "bytes": 123,
                  "checked_evidence": {"path": "evidence/source.json", "sha256": "d" * 64}}
        other = dict(self.subject, revision_id=43)
        request = {"schema_version": 1, "subject": other, "source": source,
                   "readiness": {"ready": True, "reason": "checked source", "stage_bytes": 0},
                   "backup_receipt": receipt(other, self.storage),
                   "source_backup_receipt": receipt(source_backup_subject(source), self.storage),
                   "owner": "Peer", "continuation": "Keep provider hold", "approval_scope": {"ticket": 410}}
        register(self.registry, request)
        self.consumer().run()
        self.assertEqual("source_check_required", self.report()[1]["sources"][0]["state"])

    def test_private_or_credential_url_is_redacted_and_review_required(self):
        rows, unresolved = candidates("https://user:secret@example.org/a http://127.0.0.1/x", {"externallinks": [], "templates": []})
        self.assertEqual([], rows)
        self.assertEqual(2, len(unresolved))
        self.assertNotIn("secret", json.dumps(unresolved))

    def test_archive_and_other_source_hosts_are_denied_before_network(self):
        with patch("urllib.request.build_opener", side_effect=AssertionError("network forbidden")):
            for url in ("https://archive.org/x", "https://web.archive.org/x", "https://x.archive.org/x", "https://example.org/x", "https://wiki.swccg.com/images/x", "http://raw.githubusercontent.com/x", "https://user:secret@raw.githubusercontent.com/x"):
                with self.subTest(url=url), self.assertRaises(ValueError):
                    safe_open(url, time.monotonic()+10)

    def test_redirect_is_refused_without_following_archive_target(self):
        with self.assertRaises(ValueError):
            NoRedirect().redirect_request(None, None, 302, "Moved", {}, "https://web.archive.org/x")

    def test_candidate_cap_does_not_silently_record_partial_inventory(self):
        with patch("source_inventory.MAX_CANDIDATES", 1):
            result = self.consumer(parse=lambda revid, deadline: {"revid": revid, "externallinks": ["https://example.org/other"], "templates": []}).run()
        self.assertEqual(1, len(result["source_inventory_failures"]))
        self.assertEqual(self.marker, json.loads(self.path.read_text()))

    def test_marker_byte_cap_is_checked_before_decode_or_fetch(self):
        self.path.write_bytes(b"x" * 21)
        with patch("source_inventory.MAX_METADATA_BYTES", 20):
            result = self.consumer().run()
        self.assertEqual(1, len(result["source_inventory_failures"]))
        self.assertEqual(b"x" * 21, self.path.read_bytes())

    def test_registry_scan_partial_remains_review_work(self):
        other = dict(self.subject, revision_id=43)
        entries = [{"request": {"subject": other}}, {"request": {"subject": other}}]
        with patch("source_inventory.MAX_REGISTRY_RECORDS", 1):
            self.consumer(registry_records=lambda unused: iter(entries)).run()
        marker, report = self.report()
        self.assertEqual("source_inventory_review_required", marker["state"])
        self.assertIn("registry_scan_partial_no_unmatched_source_assumed_absent", report["unresolved_constructs"])


if __name__ == "__main__":
    unittest.main()
