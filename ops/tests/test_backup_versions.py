import hashlib
import contextlib
import io
import json
import sys
import tempfile
import tracemalloc
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]), str(Path(__file__).resolve().parents[2] / "tools")]
from backup_spool import Spool, BackupDeferred, candidate_id, CHUNK_BYTES, NoOriginalRedirect
from backup_versions import Inbox, Producer, discover_changes, reconcile_inventory, backup_owner
from preservation_backups import revision_artifact
from preservation_contracts import object_id
from preservation_registry import export_records
from backup_projection import Projection


def file_info(raw, timestamp="2026-11-14T00:00:00Z", archive=False):
    return {"url": "https://wiki.swccg.com/images/" + ("archive/a/a1/20261114!Test.bin" if archive else "a/a1/Test.bin"),
            "timestamp": timestamp, "sha1": hashlib.sha1(raw).hexdigest(), "size": len(raw), "mime": "application/octet-stream"}


def revision(revid=42, text="Japanese title 日本語\n"):
    return {"revid": revid, "timestamp": "2026-11-14T00:00:00Z", "sha1": hashlib.sha1(text.encode()).hexdigest(),
            "slots": {"main": {"content": text, "contentmodel": "wikitext"}}}


def receipt(subject, storage):
    return {"schema_version": 1, "subject": subject, "storage": storage,
            "verification": {"status": "verified", "independent": True, "restored_sha256": subject["content_sha256"],
                             "restored_bytes": subject["bytes"], "verified_at": "2026-11-14T00:00:00Z"}}


class ChunkOnly(io.BytesIO):
    def read(self, size=-1):
        if not 0 < size <= CHUNK_BYTES:
            raise AssertionError("unbounded original read")
        return super().read(size)


class SpoolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def test_binary_is_streamed_to_disk_and_cached_by_exact_version(self):
        raw = b"abc" * (CHUNK_BYTES * 3)
        calls = []
        spool = Spool(self.root, fetch=lambda url: (calls.append(url) or ChunkOnly(raw)), disk_reserve=0)
        artifact = spool.file("File:Test.bin", file_info(raw))
        self.assertIsInstance(artifact.payload, Path)
        self.assertEqual(raw, artifact.payload.read_bytes())
        self.assertEqual(artifact, spool.file("File:Test.bin", file_info(raw)))
        self.assertEqual(1, len(calls))
        self.assertEqual(len(raw), spool.used_bytes())

    def test_bad_original_hash_or_size_never_produces_saved_version(self):
        spool = Spool(self.root, fetch=lambda url: ChunkOnly(b"wrong"), disk_reserve=0)
        for info in (file_info(b"right"), file_info(b"longer")):
            with self.assertRaises(ValueError):
                spool.file("File:Test.bin", info)
        self.assertEqual([], list((self.root / "versions").iterdir()))
        self.assertEqual(0, spool.used_bytes())

    def test_budget_and_hidden_original_fail_before_network(self):
        def forbidden(url):
            self.fail("network should not be used")
        spool = Spool(self.root, fetch=forbidden, max_file_bytes=2, disk_reserve=0)
        with self.assertRaises(BackupDeferred):
            spool.file("File:Test.bin", file_info(b"123"))
        info = {**file_info(b"1"), "filehidden": ""}
        with self.assertRaises(BackupDeferred):
            spool.file("File:Test.bin", info)

    def test_owned_crash_partial_does_not_deadlock_budget(self):
        raw = b"1234"
        spool = Spool(self.root, fetch=lambda url: ChunkOnly(raw), max_spool_bytes=4, disk_reserve=0)
        (self.root / "inflight" / (candidate_id("File:Test.bin", file_info(raw)) + ".part")).write_bytes(raw)
        self.assertEqual(raw, spool.file("File:Test.bin", file_info(raw)).payload.read_bytes())

    def test_release_requires_independent_receipt_and_resume_avoids_redownload(self):
        raw = b"1234"
        calls = []
        spool = Spool(self.root, fetch=lambda url: (calls.append(url) or ChunkOnly(raw)), disk_reserve=0)
        artifact = spool.file("File:Test.bin", file_info(raw))
        with self.assertRaises(ValueError):
            spool.release(artifact)
        proof = receipt(artifact.subject, {"kind": "git", "repository": "https://github.com/billbisco/swccg-wiki-files", "commit": "a" * 40, "path": "objects/file.bin"})
        spool.record_receipt(proof)
        spool.release(artifact)
        self.assertEqual(0, spool.used_bytes())
        self.assertEqual(artifact.subject, spool.file("File:Test.bin", file_info(raw)).subject)
        self.assertEqual(1, len(calls))

    def test_large_original_peak_memory_is_independent_of_binary_size(self):
        block = b"z" * CHUNK_BYTES
        size = CHUNK_BYTES * 64
        sha1 = hashlib.sha1()
        for _ in range(64):
            sha1.update(block)
        class Generated:
            def __init__(self):
                self.remaining = size
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
            def read(self, count):
                if not 0 < count <= CHUNK_BYTES:
                    raise AssertionError("unbounded read")
                length = min(count, self.remaining)
                self.remaining -= length
                return block[:length]
        spool = Spool(self.root, fetch=lambda url: Generated(), disk_reserve=0)
        info = {**file_info(b""), "size": size, "sha1": sha1.hexdigest()}
        tracemalloc.start()
        try:
            artifact = spool.file("File:Test.bin", info)
            _, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()
        self.assertEqual(size, artifact.payload.stat().st_size)
        self.assertLess(peak, 2 * 1024 * 1024)

    def test_cached_receipt_cannot_bypass_new_suppression(self):
        raw = b"test"
        spool = Spool(self.root, fetch=lambda url: ChunkOnly(raw), disk_reserve=0)
        artifact = spool.file("File:Test.bin", file_info(raw))
        spool.record_receipt(receipt(artifact.subject, {"kind": "git", "repository": "https://github.com/billbisco/swccg-wiki-files", "commit": "a" * 40, "path": "file.bin"}))
        with self.assertRaises(BackupDeferred):
            spool.file("File:Test.bin", {**file_info(raw), "filehidden": ""})

    def test_tampered_cache_subject_and_path_cannot_return_another_version(self):
        raw = b"test"
        spool = Spool(self.root, fetch=lambda url: ChunkOnly(raw), disk_reserve=0)
        spool.file("File:Test.bin", file_info(raw))
        path = self.root / "versions" / (candidate_id("File:Test.bin", file_info(raw)) + ".json")
        good = json.loads(path.read_text())
        for change in ({"payload": "../../outside.bin"},
                       {"subject": {**good["subject"], "title": "File:Other.bin"}},
                       {"subject": {**good["subject"], "upload_timestamp": "2026-11-15T00:00:00Z"}}):
            path.write_text(json.dumps({**good, **change}), encoding="utf-8")
            with self.assertRaises(ValueError):
                spool.file("File:Test.bin", file_info(raw))

    def test_original_redirects_are_refused_before_fetching_another_origin(self):
        handler = NoOriginalRedirect()
        for destination in ("http://127.0.0.1/private", "https://another.example/image", "https://wiki.swccg.com/another"):
            with self.assertRaisesRegex(BackupDeferred, "redirected"):
                handler.redirect_request(None, None, 302, "Found", {}, destination)

    def test_slow_reader_absolute_deadline_leaves_no_saved_version(self):
        clock = [0]
        class SlowReader:
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
            def read(self, size):
                raise AssertionError("buffer-filling read must not hide trickle deadline")
            def read1(self, size):
                clock[0] = 6
                return b"test"
        spool = Spool(self.root, fetch=lambda url: SlowReader(), disk_reserve=0)
        with patch("backup_spool.time.monotonic", side_effect=lambda: clock[0]):
            with self.assertRaisesRegex(BackupDeferred, "deadline"):
                spool.file("File:Test.bin", file_info(b"test"), deadline=5)
        self.assertEqual([], list((self.root / "versions").iterdir()))
        self.assertEqual(0, spool.used_bytes())


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.inbox = Inbox(self.root)
        self.addCleanup(self.temp.cleanup)

    def test_exact_manual_talk_file_revision_ids_persist_before_cursor(self):
        rows = [{"title": "Talk:Card", "revid": 7}, {"title": "File:Card.gif", "revid": 8},
                {"title": "File:Card.gif", "logtype": "upload", "logid": 1, "timestamp": "a"},
                {"title": "File:Card.gif", "logtype": "upload", "logid": 2, "timestamp": "b"}]
        def api(query):
            return {"query": {"recentchanges": rows}, "continue": {"rccontinue": "next"}}
        state = discover_changes(api, self.inbox, since="2026-11-13T00:00:00Z", max_pages=1)
        tasks = [task for _, task in self.inbox.pending()]
        self.assertEqual(4, len(tasks))
        self.assertEqual({7, 8}, {task["revision_id"] for task in tasks if task["kind"] == "revision"})
        self.assertEqual("next", state["scan"]["continue"]["rccontinue"])
        self.assertNotIn("discovered_through", state)

    def test_failed_discovery_does_not_advance_cursor(self):
        with self.assertRaises(RuntimeError):
            discover_changes(lambda query: (_ for _ in ()).throw(RuntimeError("offline")), self.inbox)
        self.assertFalse((self.root / "recentchanges.json").exists())

    def test_inventory_includes_talk_and_file_and_cycles_generation(self):
        def api(query):
            if query.get("meta"):
                return {"query": {"namespaces": {"1": {"id": 1}, "6": {"id": 6}, "-1": {"id": -1}}}}
            return {"query": {"allpages": [{"title": "Talk:Card" if query["apnamespace"] == 1 else "File:Card.gif"}]}}
        state = reconcile_inventory(api, self.inbox, pages=2)
        self.assertEqual(2, state["generation"])
        tasks = [task for _, task in self.inbox.pending()]
        self.assertEqual(3, len(tasks))
        self.assertEqual({"page_history", "file_history"}, {task["kind"] for task in tasks})

    def test_single_owner_does_not_allow_a_second_producer(self):
        with backup_owner(self.root):
            with self.assertRaises(BackupDeferred):
                with backup_owner(self.root):
                    self.fail("second owner entered")


class ProducerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pages, self.files = self.root / "pages", self.root / "files"
        self.pages.mkdir()
        self.files.mkdir()
        self.addCleanup(self.temp.cleanup)

    def producer(self, api, **kwargs):
        self.commits = []
        def commit(repo, paths, message, redo):
            self.assertEqual([], paths)
            if not self.commits:
                self.assertFalse(list(repo.glob("preservation/objects/*/*")), "tracked write preceded shared Git transaction")
            written = redo()
            self.commits.append(written)
        spool = Spool(self.root / "spool", disk_reserve=0, fetch=lambda url: ChunkOnly(b"image"))
        factory = kwargs.pop("projection_factory", None)
        return Producer(api, self.pages, self.files, self.root / "work", self.root / "registry",
                        spool=spool, commit=commit, readback=receipt, remote_head=lambda repo: "a" * 40,
                        projection_factory=factory, **kwargs)

    def test_exact_revision_writes_only_in_callback_and_completes_after_remote_readback(self):
        producer = self.producer(lambda query: {"query": {"pages": [{"title": "Talk:Test", "pageid": 1, "revisions": [revision()]}]}})
        task = {"kind": "revision", "title": "Talk:Test", "revision_id": 42}
        key = producer.inbox.add(task)
        proof = producer.task(key, task)
        self.assertEqual("independently_backed_up", proof["state"])
        self.assertEqual(0, producer.spool.used_bytes())
        self.assertEqual([], list(producer.inbox.pending()))
        self.assertEqual(1, len(self.commits))
        self.assertEqual(1, producer.pending_source_inventory()["source_inventory_required"])
        marker = json.loads(next(producer.source_inventory.glob("*.json")).read_text())
        self.assertEqual(42, marker["subject"]["revision_id"])
        self.assertFalse(marker["capture_submitted"])
        self.assertEqual("source_inventory_required", marker["state"])

    def test_failed_readback_keeps_item_pending_and_spooled(self):
        producer = self.producer(lambda query: {"query": {"pages": [{"title": "Test", "revisions": [revision()]}]}})
        producer.readback = lambda subject, storage: (_ for _ in ()).throw(ValueError("remote mismatch"))
        task = {"kind": "revision", "title": "Test", "revision_id": 42}
        key = producer.inbox.add(task)
        with self.assertRaisesRegex(ValueError, "remote mismatch"):
            producer.task(key, task)
        self.assertEqual(1, len(list(producer.inbox.pending())))
        self.assertGreater(producer.spool.used_bytes(), 0)

    def test_original_upload_registers_exact_independent_source_but_never_submits(self):
        info = file_info(b"image", archive=True)
        producer = self.producer(lambda query: {"query": {"pages": [{"title": "File:Test.bin", "imageinfo": [info]}]}})
        task = {"kind": "file_history", "title": "File:Test.bin"}
        producer.task(producer.inbox.add(task), task)
        state = export_records(producer.registry)
        self.assertEqual(1, len(state["objects"]))
        row = state["objects"][0]
        self.assertEqual("ready", row["state"])
        self.assertFalse(row["submitted"])
        self.assertEqual(info["url"], row["source"]["url"])
        self.assertEqual(info["timestamp"], row["subject"]["upload_timestamp"])

    def test_history_continuation_is_durable_before_current_task_completion(self):
        producer = self.producer(lambda query: {"query": {"pages": [{"title": "Test", "revisions": [revision()]}]},
                                                "continue": {"rvcontinue": "older", "continue": "||"}})
        task = {"kind": "page_history", "title": "Test"}
        producer.task(producer.inbox.add(task), task)
        pending = list(producer.inbox.pending())
        self.assertEqual(1, len(pending))
        self.assertEqual("older", pending[0][1]["continue"]["rvcontinue"])

    def test_failed_discovery_does_not_prevent_existing_independent_task(self):
        def api(query):
            if query.get("prop", "").startswith("revisions"):
                return {"query": {"pages": [{"title": "Test", "revisions": [revision()]}]}}
            raise RuntimeError("discovery temporarily offline")
        producer = self.producer(api)
        producer.inbox.add({"kind": "revision", "title": "Test", "revision_id": 42})
        status = producer.run(task_limit=1)
        self.assertEqual(1, status["completed_tasks"])
        self.assertEqual(2, len(status["discovery_failures"]))
        self.assertFalse(status["pending"])
        self.assertIsNotNone(status["last_actual_verified_backup_at"])

    def test_bad_item_gets_backoff_while_unrelated_item_continues(self):
        def api(query):
            if not query.get("prop", "").startswith("revisions"):
                raise RuntimeError("no discovery in fixture")
            if query["revids"] == "41":
                raise ValueError("unreadable version")
            return {"query": {"pages": [{"title": "Test", "revisions": [revision()]}]}}
        producer = self.producer(api)
        key = producer.inbox.add({"kind": "revision", "title": "Bad", "revision_id": 41})
        producer.inbox.add({"kind": "revision", "title": "Test", "revision_id": 42})
        result = producer.run(task_limit=2)
        self.assertEqual(1, result["completed_tasks"])
        self.assertEqual(1, len(result["failed_tasks"]))
        self.assertEqual(1, len(list(producer.inbox.pending())))
        self.assertEqual([], list(producer.inbox.pending(due_only=True)))
        self.assertEqual("needs_reconciliation", json.loads((producer.inbox.directory / "issues" / (key + ".json")).read_text())["state"])

    def test_page_history_preserves_current_projection_while_archiving_older_text(self):
        def factory(repo, kind):
            return Projection(repo, kind, guard=lambda repo: contextlib.nullcontext())
        producer = self.producer(lambda query: {"query": {"pages": [{"title": "Test", "lastrevid": 42,
                                    "revisions": [revision(42, "current"), revision(41, "old")]}]}}, projection_factory=factory)
        task = {"kind": "page_history", "title": "Test"}
        producer.task(producer.inbox.add(task), task)
        self.assertEqual(b"current", (self.pages / "pages/Test.wiki").read_bytes())
        self.assertEqual(2, len(list((self.pages / "preservation/versions").glob("*.json"))))

    def test_exact_old_revision_has_no_current_flat_projection(self):
        def factory(repo, kind):
            return Projection(repo, kind, guard=lambda repo: contextlib.nullcontext())
        producer = self.producer(lambda query: {"query": {"pages": [{"title": "Test", "lastrevid": 43,
                                    "revisions": [revision(42, "historical")]}]}}, projection_factory=factory)
        task = {"kind": "revision", "title": "Test", "revision_id": 42}
        producer.task(producer.inbox.add(task), task)
        self.assertFalse((self.pages / "pages/Test.wiki").exists())
        self.assertEqual(1, len(list((self.pages / "preservation/versions").glob("*.json"))))

    def test_two_latest_file_reconciliations_reuse_receipt_and_registration(self):
        def factory(repo, kind):
            return Projection(repo, kind, guard=lambda repo: contextlib.nullcontext())
        producer = self.producer(lambda query: {"query": {"pages": [{"title": "File:Test.bin", "imageinfo": [file_info(b"image")]}]}},
                                 projection_factory=factory)
        calls = []
        def fresh_receipt(subject, storage):
            calls.append(storage)
            result = receipt(subject, storage)
            result["verification"]["verified_at"] = "2026-11-14T00:00:01Z" if len(calls) == 1 else "2026-11-14T00:00:02Z"
            return result
        producer.readback = fresh_receipt
        for generation in (1, 2):
            task = {"kind": "file_history", "title": "File:Test.bin", "generation": generation}
            producer.task(producer.inbox.add(task), task)
        self.assertEqual(1, len(calls))
        state = export_records(producer.registry)
        self.assertEqual(1, len(state["objects"]))
        self.assertEqual("ready", state["objects"][0]["state"])

    def test_peer_projection_skip_has_a_separate_durable_retry(self):
        def factory(repo, kind):
            return Projection(repo, kind, guard=lambda repo: contextlib.nullcontext())
        def api(query):
            target = self.pages / "pages/Test.wiki"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("peer advance", encoding="utf-8")
            return {"query": {"pages": [{"title": "Test", "lastrevid": 42, "revisions": [revision()]}]}}
        producer = self.producer(api, projection_factory=factory)
        task = {"kind": "page_history", "title": "Test"}
        producer.task(producer.inbox.add(task), task)
        pending = list(producer.inbox.pending())
        self.assertEqual(1, len(pending))
        self.assertIn("projection_retry", pending[0][1])
        self.assertTrue((producer.inbox.directory / "issues" / (pending[0][0] + ".json")).exists())
        self.assertEqual("peer advance", (self.pages / "pages/Test.wiki").read_text())

    def test_health_has_backlog_failure_age_and_explicit_partial_counts(self):
        inbox = Inbox(self.root / "health-inbox")
        key = inbox.add({"kind": "revision", "title": "Test", "revision_id": 42})
        inbox.issue(key, "readback needs retry")
        counts = inbox.health_counts()
        self.assertEqual(1, counts["pending_task_count"])
        self.assertEqual(1, counts["failed_pending_task_count"])
        self.assertIsNotNone(counts["oldest_pending_age_seconds_observed"])
        self.assertFalse(counts["task_count_partial"])
        self.assertTrue(inbox.health_counts(scan_limit=0)["task_count_partial"])

    def test_edit_backlog_does_not_starve_images_usage_or_history(self):
        producer = self.producer(lambda query: self.fail("discovery must be mocked"))
        for number in range(20):
            producer.inbox.add({"kind": "revision", "title": "Test", "revision_id": number})
        for kind in ("file_history", "file_usage", "page_history"):
            producer.inbox.add({"kind": kind, "title": "File:Test.bin" if kind != "page_history" else "Test"})
        seen = []
        def complete(key, task):
            seen.append(task["kind"])
            producer.inbox.complete(key, {"state": "synthetic completion"})
        producer.task = complete
        with patch("backup_versions.discover_changes"), patch("backup_versions.reconcile_inventory"):
            result = producer.run(task_limit=8)
        self.assertEqual(8, result["completed_tasks"])
        self.assertEqual(["revision"] * 4, seen[:4])
        self.assertEqual({"revision", "file_history", "file_usage", "page_history"}, set(seen))
        self.assertGreater(result["pending_task_count"], 0)

    def test_fair_scheduling_still_respects_single_task_budget(self):
        producer = self.producer(lambda query: self.fail("discovery must be mocked"))
        producer.inbox.add({"kind": "revision", "title": "Test", "revision_id": 42})
        producer.inbox.add({"kind": "file_history", "title": "File:Test.bin"})
        seen = []
        producer.task = lambda key, task: seen.append(task["kind"])
        with patch("backup_versions.discover_changes"), patch("backup_versions.reconcile_inventory"):
            result = producer.run(task_limit=1)
        self.assertEqual(["revision"], seen)
        self.assertEqual(1, result["completed_tasks"])

    def test_failed_edit_cannot_prevent_independent_history_progress(self):
        producer = self.producer(lambda query: self.fail("discovery must be mocked"))
        producer.inbox.add({"kind": "revision", "title": "Test", "revision_id": 42})
        producer.inbox.add({"kind": "page_history", "title": "Independent"})
        seen = []
        def task(key, value):
            if value["kind"] == "revision":
                raise ValueError("injected source failure")
            seen.append(value["kind"])
            producer.inbox.complete(key, {"state": "synthetic completion"})
        producer.task = task
        with patch("backup_versions.discover_changes"), patch("backup_versions.reconcile_inventory"):
            result = producer.run(task_limit=2)
        self.assertEqual(["page_history"], seen)
        self.assertEqual(1, result["completed_tasks"])
        self.assertEqual(1, len(result["failed_tasks"]))
        self.assertEqual(1, result["failed_pending_task_count"])
        self.assertFalse(result["source_inventory_automatic_consumer_implemented"])


if __name__ == "__main__":
    unittest.main()
