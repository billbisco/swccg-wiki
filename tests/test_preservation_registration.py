import copy
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "tools"), str(ROOT / "ops")]
from preservation_contracts import (object_id, registration_job_id, registration_object_id,
                                    source_backup_subject, validate_backup_receipt,
                                    validate_registration_identity, validate_source_representation)
from preservation_enqueue import deliver
from preservation_registry import SERVER_OWNER, export_records, main, promote_ready, register


def fixture(title="File:one.png", timestamp="2026-11-14T00:00:00Z", ready=True):
    payload = b"exact original image bytes"
    sha = hashlib.sha256(payload).hexdigest()
    subject = dict(kind="wiki_file_version", title=title, upload_timestamp=timestamp,
                   original_version_url="https://wiki.swccg.com/images/one.png",
                   content_sha256=sha, bytes=len(payload))
    receipt = dict(schema_version=1, subject=copy.deepcopy(subject),
                   storage=dict(kind="git", repository="https://github.com/billbisco/swccg-wiki-files",
                                commit="a" * 40, path="preservation/objects/" + sha + ".bin"),
                   verification=dict(status="verified", independent=True,
                                     restored_sha256=sha, restored_bytes=len(payload),
                                     verified_at="2026-11-14T01:00:00Z"))
    return dict(schema_version=1, subject=subject,
                source=dict(url=subject["original_version_url"], sha256=sha, bytes=len(payload),
                            checked_evidence=dict(path="evidence/410/source.json", sha256="b" * 64)),
                readiness=dict(ready=ready, reason="checked public source" if ready else "private stage not published",
                               stage_bytes=len(payload), private_locator="/private/operator-only"),
                backup_receipt=receipt, owner="MemoryCoreChatGPT",
                continuation="Existing server owner checks the public payload before queue promotion",
                approval_scope=dict(ticket=410, publication_ticket=386))


class BackupContractTests(unittest.TestCase):
    def test_exact_independent_receipt(self):
        request = fixture()
        self.assertEqual([], validate_backup_receipt(request["backup_receipt"], request["subject"]))

    def test_queued_local_or_mismatched_receipts_are_not_recoverable(self):
        for field, value in (("status", "queued"), ("independent", False),
                             ("restored_sha256", "c" * 64), ("restored_bytes", True)):
            with self.subTest(field=field):
                request = fixture()
                request["backup_receipt"]["verification"][field] = value
                self.assertTrue(validate_backup_receipt(request["backup_receipt"], request["subject"]))

    def test_other_filename_or_upload_version_cannot_borrow_receipt(self):
        request = fixture()
        for field, value in (("title", "File:other.png"), ("upload_timestamp", "2026-11-13T00:00:00Z")):
            subject = dict(request["subject"], **{field: value})
            self.assertTrue(validate_backup_receipt(request["backup_receipt"], subject))

    def test_invalid_subjects_return_errors_instead_of_crashing(self):
        self.assertTrue(validate_backup_receipt({}, None))

    def test_thumbnail_or_credential_url_is_not_a_full_original_version(self):
        request = fixture()
        for url in ("https://wiki.swccg.com/images/thumb/one.png", "https://user:secret@wiki.swccg.com/images/one.png"):
            subject = dict(request["subject"], original_version_url=url)
            receipt = copy.deepcopy(request["backup_receipt"])
            receipt["subject"] = subject
            self.assertTrue(validate_backup_receipt(receipt, subject))

    def snapshot_source(self):
        source = fixture()["source"]
        source["primary_url"] = "https://www.starwarsccg.org/event-deck/"
        source["url"] = "https://swccg.com/snapshots/pc/event-deck.html"
        source["representation"] = "checked_self_contained_snapshot"
        source["provenance_equivalence"] = dict(
            primary_url=source["primary_url"], snapshot_url=source["url"],
            primary_html_sha256="c" * 64, snapshot_html_sha256=source["sha256"],
            primary_article_text_sha256="d" * 64, snapshot_article_text_sha256="d" * 64,
            evidence_path="evidence/409/proof.json", evidence_sha256="e" * 64)
        return source

    def test_checked_snapshot_keeps_distinct_primary_and_capture_payload_identities(self):
        self.assertEqual([], validate_source_representation(self.snapshot_source()))

    def test_different_article_text_or_unbound_capture_target_fails(self):
        for field, value in (("snapshot_article_text_sha256", "f" * 64),
                             ("snapshot_html_sha256", "f" * 64),
                             ("primary_url", "https://example.org/another")):
            source = self.snapshot_source()
            source["provenance_equivalence"][field] = value
            self.assertTrue(validate_source_representation(source))

    def test_snapshot_alias_without_explicit_equivalence_is_not_an_original(self):
        source = self.snapshot_source()
        source.pop("representation")
        self.assertTrue(validate_source_representation(source))

    def test_container_receipt_binds_both_compressed_artifact_and_raw_member(self):
        request = fixture()
        receipt = request["backup_receipt"]
        receipt["storage"].update(container="tar.xz", member="sources/one.png",
                                  artifact_sha256="c" * 64, artifact_bytes=123,
                                  uncompressed_bytes=456)
        receipt["verification"].update(restored_container_sha256="c" * 64,
                                       restored_container_bytes=123)
        self.assertEqual([], validate_backup_receipt(receipt, request["subject"]))
        receipt["verification"].pop("restored_container_sha256")
        self.assertTrue(validate_backup_receipt(receipt, request["subject"]))


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_scoped_export_matches_full_rows_with_latest_generation_and_promotion(self):
        first = register(self.root, fixture())
        second = register(self.root, fixture("File:two.png"))
        revised = fixture(ready=False)
        revised["generation"] = 1
        register(self.root, revised)
        promote_ready(self.root, queued_urls=set(), stage_budget_bytes=1000,
                      limit=1, owner=SERVER_OWNER, check_public=lambda _: True,
                      check_approval=lambda _: True,
                      enqueue=lambda url, job: dict(queued=True, url=url, job_id=job))
        full = export_records(self.root)
        self.assertEqual(full, export_records(self.root, object_ids=[first["object_id"], second["object_id"]]))
        for key in (first["object_id"], second["object_id"]):
            scoped = export_records(self.root, object_ids=(item for item in [key, key]))
            self.assertEqual(dict(full, objects=[row for row in full["objects"] if row["object_id"] == key]), scoped)
        self.assertEqual({"awaiting_stage", "queued"}, {row["state"] for row in full["objects"]})
        self.assertEqual([1], [row["generation"] for row in full["objects"] if row["object_id"] == first["object_id"]])

    def test_scoped_export_never_opens_unrelated_malformed_records_or_receipts(self):
        selected = register(self.root, fixture())
        expected = export_records(self.root)
        unrelated = register(self.root, fixture("File:unrelated.png"))
        # A different payload also gives the unrelated object its own receipt paths.
        broken = self.root / "requests" / ("c" * 64) / ("d" * 64) / "broken.json"
        broken.parent.mkdir(parents=True)
        broken.write_text("not JSON", encoding="utf-8")
        other = self.root / unrelated["record"]
        other.write_text("not JSON", encoding="utf-8")
        owner = self.root / "owner-jobs" / (("c" * 64) + ".json")
        owner.parent.mkdir(parents=True)
        owner.write_text("not JSON", encoding="utf-8")
        promotion = self.root / "promotions" / (("c" * 64) + ".json")
        promotion.parent.mkdir(parents=True)
        promotion.write_text("not JSON", encoding="utf-8")
        real_open = Path.open
        opened = []

        def track_open(path, *args, **kwargs):
            opened.append(path)
            self.assertNotIn(path, (broken, other, owner, promotion))
            return real_open(path, *args, **kwargs)

        with patch.object(Path, "open", track_open):
            self.assertEqual(expected, export_records(self.root, object_ids=[selected["object_id"]]))
            self.assertEqual(dict(expected, objects=[]), export_records(self.root, object_ids=[]))
        self.assertIn(self.root / selected["record"], opened)
        with self.assertRaises(ValueError):
            export_records(self.root)

    def test_scoped_export_preserves_actual_owner_receipt_application(self):
        from preservation_owner_receipts import store_event
        request = fixture()
        selected = register(self.root, request)
        register(self.root, fixture("File:two.png"))
        event = dict(source_sha256=request["source"]["sha256"],
                     source_bytes=request["source"]["bytes"], job_id=selected["job_id"],
                     approved_object_ids=[selected["object_id"]], state="submitted",
                     reason="synthetic owner submission", accepted_job_id="fixture-job")
        store_event(self.root, event)
        full = export_records(self.root)
        expected = next(row for row in full["objects"] if row["object_id"] == selected["object_id"])
        self.assertTrue(expected["submitted"])
        self.assertEqual(event, expected["owner_job_receipt"])
        self.assertEqual(dict(full, objects=[expected]), export_records(self.root, object_ids=[selected["object_id"]]))

    def test_export_scope_validation_happens_before_any_record_read(self):
        for ids in ("a" * 64, ["a" * 63], ["A" * 64], ["g" * 64],
                    ["../" + "a" * 64], [None], [True], ["a" * 64 + "\n"]):
            with self.subTest(ids=ids), patch.object(Path, "open", side_effect=AssertionError("unexpected read")):
                with self.assertRaises(ValueError):
                    export_records(self.root, object_ids=ids)
        self.assertEqual([], export_records(self.root, object_ids=[])["objects"])
        found = register(self.root, fixture())
        for ids in (["f" * 64], [found["object_id"], "f" * 64]):
            with self.subTest(ids=ids), self.assertRaisesRegex(ValueError, "requested object IDs not found: " + "f" * 64):
                export_records(self.root, object_ids=ids)

    def test_cli_scoped_export_and_missing_scope_fail_without_partial_output(self):
        key = register(self.root, fixture())["object_id"]
        argv = ["preservation_registry.py", "export", "--registry", str(self.root)]
        for scope in ([], ["--object-id", key, "--object-id", key]):
            with patch.object(sys, "argv", argv + scope), patch.object(sys, "stdout", io.StringIO()) as output:
                self.assertEqual(0, main())
                self.assertEqual(export_records(self.root), json.loads(output.getvalue()))
        for scope in (["--object-id", "f" * 64], ["--object-id", key, "--object-id", "invalid"]):
            with patch.object(sys, "argv", argv + scope), patch.object(sys, "stdout", io.StringIO()) as output:
                with self.assertRaises(ValueError):
                    main()
                self.assertEqual("", output.getvalue())
        with patch.object(sys, "argv", [argv[0], "register", *argv[2:], "--object-id", key]), patch.object(sys, "stderr", io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                main()
            self.assertEqual(2, error.exception.code)

    def test_private_work_receipt_registers_without_submitting(self):
        request = fixture()
        request["backup_receipt"]["storage"]["repository"] = "https://github.com/swccg-guild/work"
        result = register(self.root, request)
        self.assertTrue(result["created"])
        self.assertFalse(result["submitted"])
        row = export_records(self.root)["objects"][0]
        self.assertEqual(request["backup_receipt"], row["backup_receipt"])
        self.assertEqual("ready", row["state"])

    def test_repeat_reconciliation_deduplicates_without_submitting(self):
        request = fixture()
        first = register(self.root, request)
        second = register(self.root, request)
        self.assertTrue(first["created"])
        self.assertFalse(second["created"])
        self.assertFalse(first["submitted"])
        self.assertEqual(first["job_id"], second["job_id"])
        self.assertEqual(1, len(export_records(self.root)["objects"]))

    def test_identical_payload_keeps_distinct_filename_and_history_mappings(self):
        first = register(self.root, fixture())
        second = register(self.root, fixture("File:two.png"))
        third = register(self.root, fixture(timestamp="2026-11-13T00:00:00Z"))
        self.assertEqual(first["job_id"], second["job_id"])
        self.assertEqual(first["job_id"], third["job_id"])
        self.assertEqual(3, len({first["object_id"], second["object_id"], third["object_id"]}))
        self.assertEqual(3, len(export_records(self.root)["objects"]))

    def test_one_page_retains_separate_citation_payloads_and_requires_both_backups(self):
        first = fixture()
        first["subject"] = dict(kind="wiki_draft", title="Event article",
                                content_sha256="c" * 64, bytes=123)
        first["backup_receipt"]["subject"] = copy.deepcopy(first["subject"])
        first["backup_receipt"]["verification"].update(restored_sha256="c" * 64, restored_bytes=123)
        self.assertEqual("awaiting_backup", register(self.root, first)["state"])
        first["generation"] = 1
        first["source_backup_receipt"] = copy.deepcopy(fixture()["backup_receipt"])
        first["source_backup_receipt"]["subject"] = source_backup_subject(first["source"])
        register(self.root, first)
        second = copy.deepcopy(first)
        second["generation"] = 0
        second["source"]["url"] = "https://example.org/another-source"
        second["source"]["sha256"] = "d" * 64
        second["source_backup_receipt"]["subject"] = source_backup_subject(second["source"])
        second["source_backup_receipt"]["verification"]["restored_sha256"] = "d" * 64
        register(self.root, second)
        rows = export_records(self.root)["objects"]
        self.assertEqual(2, len(rows))
        self.assertEqual(1, len({x["subject_id"] for x in rows}))
        self.assertEqual(2, len({x["object_id"] for x in rows}))
        self.assertEqual(2, len({x["job_id"] for x in rows}))
        self.assertTrue(all(validate_registration_identity(x) == [] for x in rows))

    def test_private_early_registration_cannot_promote_missing_public_url(self):
        register(self.root, fixture(ready=False))
        checked = []
        result = promote_ready(self.root, queued_urls=set(), stage_budget_bytes=100, limit=10,
                               owner=SERVER_OWNER, check_public=lambda r: checked.append(r),
                               check_approval=lambda r: True,
                               enqueue=lambda *args: self.fail("unready URL reached queue"))
        self.assertEqual([], result)
        self.assertEqual([], checked)
        row = export_records(self.root)["objects"][0]
        self.assertEqual("awaiting_stage", row["state"])
        self.assertNotIn("private_locator", row["readiness"])

    def test_missing_backup_remains_registered_and_never_queued(self):
        request = fixture()
        request.pop("backup_receipt")
        self.assertEqual("awaiting_backup", register(self.root, request)["state"])
        self.assertEqual([], self.promote())

    def promote(self, queue=None, budget=100, check=lambda r: True):
        queue = [] if queue is None else queue
        def enqueue(url, job):
            if url not in queue:
                queue.append(url)
            return {"queued": True, "url": url, "job_id": job}
        return promote_ready(self.root, queued_urls=set(queue), stage_budget_bytes=budget,
                             limit=10, owner=SERVER_OWNER, check_public=check, enqueue=enqueue,
                             check_approval=lambda r: True)

    def test_distinct_versions_share_one_promotion_and_preserve_queue_order(self):
        register(self.root, fixture())
        register(self.root, fixture("File:two.png"))
        queue = ["https://example.org/older"]
        self.assertEqual(1, len(self.promote(queue)))
        self.assertEqual("https://example.org/older", queue[0])
        self.assertEqual(2, len(queue))

    def test_existing_queue_entry_recovers_after_interrupted_promotion(self):
        request = fixture()
        register(self.root, request)
        queue = []
        def append_then_crash(url, job):
            queue.append(url)
            raise OSError("interrupted after durable queue append")
        with self.assertRaises(OSError):
            promote_ready(self.root, queued_urls=set(), stage_budget_bytes=100, limit=1,
                          owner=SERVER_OWNER, check_public=lambda r: True, enqueue=append_then_crash,
                          check_approval=lambda r: True)
        self.promote(queue)
        self.assertEqual([request["source"]["url"]], queue)

    def test_budget_and_exact_public_check_gate_promotion(self):
        register(self.root, fixture())
        self.assertEqual([], self.promote(budget=1))
        self.assertEqual([], self.promote(check=lambda r: False))
        self.assertEqual(1, len(self.promote()))
        self.assertEqual("queued", export_records(self.root)["objects"][0]["state"])

    def test_client_readiness_cannot_replace_server_approval_scope_check(self):
        register(self.root, fixture())
        result = promote_ready(self.root, queued_urls=set(), stage_budget_bytes=100, limit=1,
                               owner=SERVER_OWNER, check_public=lambda r: True,
                               check_approval=lambda r: False,
                               enqueue=lambda *args: self.fail("unapproved request reached queue"))
        self.assertEqual([], result)

    def test_revised_readiness_needs_explicit_generation_and_supersedes_old(self):
        request = fixture()
        register(self.root, request)
        withdrawn = copy.deepcopy(request)
        withdrawn["readiness"]["ready"] = False
        with self.assertRaisesRegex(ValueError, "generation"):
            register(self.root, withdrawn)
        withdrawn["generation"] = 1
        register(self.root, withdrawn)
        self.assertEqual([], self.promote())
        self.assertEqual("superseded", register(self.root, request)["state"])

    def test_metadata_write_interruption_does_not_publish_partial_request(self):
        with patch("preservation_registry.os.link", side_effect=OSError("interrupted")):
            with self.assertRaises(OSError):
                register(self.root, fixture())
        self.assertEqual([], export_records(self.root)["objects"])
        self.assertEqual([], list(self.root.rglob(".register-*")))

    def test_corrupt_or_misplaced_immutable_record_is_not_exported_or_promoted(self):
        receipt = register(self.root, fixture())
        path = self.root / receipt["record"]
        data = json.loads(path.read_text(encoding="utf-8"))
        data["owner"] = "unrecorded change"
        path.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "immutable identity"):
            export_records(self.root)
        with self.assertRaisesRegex(ValueError, "immutable identity"):
            self.promote()

    def test_large_source_payload_cannot_be_embedded_in_metadata_inbox(self):
        request = fixture()
        request["accidental_payload"] = "x" * (1024 * 1024)
        with self.assertRaisesRegex(ValueError, "metadata cap"):
            register(self.root, request)
        self.assertEqual([], list(self.root.rglob("*.json")))

    def test_a_pc_owner_cannot_claim_server_promotion(self):
        register(self.root, fixture())
        with self.assertRaisesRegex(ValueError, "server submission owner"):
            promote_ready(self.root, queued_urls=set(), stage_budget_bytes=100, limit=1,
                          owner="pc-local-lock", check_public=lambda r: True, enqueue=lambda *r: {},
                          check_approval=lambda r: True)


class EnqueueClientTests(unittest.TestCase):
    def test_client_uses_fixed_server_registration_and_no_archive_request(self):
        request = fixture()
        response = dict(object_id=registration_object_id(request["subject"], request["source"]),
                        subject_id=object_id(request["subject"]),
                        job_id=registration_job_id(request["source"]), submitted=False)
        calls = []
        def run(command, **kwargs):
            calls.append((command, kwargs))
            return SimpleNamespace(returncode=0, stdout=json.dumps(response).encode())
        self.assertEqual(response, deliver(request, "/var/lib/swccg-ops/preservation", run=run))
        self.assertEqual("gemp", calls[0][0][-2])
        self.assertIn("preservation_registry.py register", calls[0][0][-1])
        self.assertNotIn("web.archive.org", " ".join(calls[0][0]))


if __name__ == "__main__":
    unittest.main()
