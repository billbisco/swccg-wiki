import base64
import copy
import hashlib
import json
import sys
import tempfile
import time
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "tools"), str(ROOT / "ops"), str(ROOT / "tests")]
from test_preservation_registration import fixture
from preservation_contracts import canonical_bytes, source_backup_subject
from preservation_registry import register, export_records, atomic_json
from preservation_capture_adoption import validate_bundle, adopt
from preservation_owner_receipts import load_event, store_event
from preservation_owner import OwnerAdapter
from wayback_control import Control, Busy
import wayback_worker as worker


class AdoptionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.directory = self.root / "control"
        self.registry = self.directory / "registry"
        self.payload = b"%PDF-1.4\nfixture native bytes\n%%EOF"
        self.source = {"url":"https://example.org/a%27b.pdf",
                       "sha256":hashlib.sha256(self.payload).hexdigest(), "bytes":len(self.payload)}
        self.subject = source_backup_subject(self.source)
        self.request = fixture()
        self.request.update(subject=self.subject, source=dict(self.source, checked_evidence={"path":"proof.json", "sha256":"b"*64}))
        self.request["backup_receipt"]["subject"] = copy.deepcopy(self.subject)
        self.request["backup_receipt"]["verification"].update(restored_sha256=self.source["sha256"], restored_bytes=len(self.payload))
        self.request["backup_receipt"]["storage"]["path"] = "sources/native.pdf"
        self.result = register(self.registry, self.request)
        self.binding = {"object_id":self.result["object_id"], "subject_id":self.result["subject_id"],
                        "request_id":self.result["request_id"], "subject":self.subject}
        original = "https://example.org/a'b.pdf"
        self.capture = {"url":"https://web.archive.org/web/20211005192408/"+original,
                        "timestamp":"20211005192408", "capture_original_url":original}
        params = {"url":self.source["url"], "output":"json", "fl":"timestamp,original,mimetype,statuscode,digest,length",
                  "filter":"statuscode:200", "collapse":"digest", "limit":"10"}
        row = {"timestamp":self.capture["timestamp"], "original":original, "mimetype":"application/pdf",
               "statuscode":"200", "digest":base64.b32encode(hashlib.sha1(self.payload).digest()).decode().rstrip("=")}
        self.proof = {"target":self.source["url"], "cdx_parameters":params,
                      "cdx_requested_url":"https://web.archive.org/cdx/search/cdx?"+urlencode(params),
                      "cdx_status":200, "capture_verified":True, "selected_candidate":row, "rows":[row],
                      "replay_url":"https://web.archive.org/web/20211005192408id_/"+original,
                      "replay_status":200, "redirects_followed":0, "replay_sha256":self.source["sha256"],
                      "replay_bytes":len(self.payload),
                      "replay_headers":{"Content-Type":"application/pdf", "Memento-Datetime":"Tue, 05 Oct 2021 19:24:08 GMT"}}
        self.bundle = {"schema_version":1, "kind":"checked_native_capture_adoption", "approval_scope":{"ticket":854},
                       "source":self.source, "bindings":[self.binding], "capture":self.capture,
                       "payload":{"path":"native.pdf", "sha256":self.source["sha256"], "bytes":len(self.payload),
                                  "backup_receipt":copy.deepcopy(self.request["backup_receipt"])}}
        (self.root / "native.pdf").write_bytes(self.payload)
        self.manifest = self.root / "manifest.json"
        self.rewrite()
        self.saved, self.commits = {}, []
        def persist(repo, done, changed, baseline):
            self.commits.append(copy.deepcopy(changed))
            self.saved.update(copy.deepcopy(changed))
        self.client = SimpleNamespace(load=lambda repo:([],copy.deepcopy(self.saved)), persist_changes=persist)

    def rewrite(self):
        raw = canonical_bytes(self.proof)
        (self.root / "proof.json").write_bytes(raw)
        subject = source_backup_subject({"url":"https://example.org/generated-observation.json",
                                         "sha256":hashlib.sha256(raw).hexdigest(), "bytes":len(raw)})
        receipt = copy.deepcopy(self.request["backup_receipt"])
        receipt.update(subject=subject)
        receipt["storage"]["path"] = "proof/observation.json"
        receipt["verification"].update(restored_sha256=subject["content_sha256"], restored_bytes=len(raw))
        self.bundle["proof"] = {"path":"proof.json", "sha256":subject["content_sha256"], "bytes":len(raw), "backup_receipt":receipt}
        self.manifest.write_bytes(canonical_bytes(self.bundle))
        self.approved = hashlib.sha256(self.manifest.read_bytes()).hexdigest()

    def execute(self, control=None):
        if control:
            return adopt(self.client, self.repo, control, self.manifest, self.approved)
        with Control(self.directory, None) as owner:
            return self.execute(owner)

    def test_no_prior_done_exact_native_adoption_and_idempotent_restart(self):
        self.execute()
        self.assertEqual("verified", self.saved[self.source["url"]]["status"])
        row = export_records(self.registry, object_ids={self.result["object_id"]})["objects"][0]
        self.assertEqual("verified", row["state"])
        self.assertFalse(row["submitted"])
        self.assertEqual(self.capture["capture_original_url"],row["capture_original_url"])
        before = canonical_bytes(self.saved)
        self.assertNotIn(b"backup_receipt", before)
        self.assertNotIn(b"storage", before)
        self.execute()
        self.assertEqual(before, canonical_bytes(self.saved))
        self.assertEqual({}, self.commits[-1])
        self.assertFalse((self.directory / "pending-updates.json").exists())

    def test_payload_pointer_and_other_same_payload_object_are_unchanged(self):
        event = {"source_sha256":self.source["sha256"], "source_bytes":len(self.payload),
                 "job_id":"payload:"+self.source["sha256"], "approved_object_ids":["a"*64],
                 "state":"needs_attention", "reason":"unrelated URL"}
        store_event(self.registry, event)
        pointer = (self.registry / "owner-jobs" / (self.source["sha256"]+".json")).read_bytes()
        self.execute()
        self.assertEqual(pointer, (self.registry / "owner-jobs" / (self.source["sha256"]+".json")).read_bytes())
        self.assertEqual(event, load_event(self.registry, self.request["source"]))

    def test_request_subject_and_source_binding_fail_before_any_write(self):
        cases = [("request_id", "f"*64), ("subject_id", "f"*64), ("object_id", "f"*64),
                 ("subject", dict(self.subject,title="different"))]
        for key,value in cases:
            with self.subTest(key=key):
                self.bundle["bindings"] = [dict(self.binding, **{key:value})]
                self.rewrite()
                with self.assertRaises(ValueError): self.execute()
                self.assertEqual([],self.commits)
                self.assertFalse((self.registry / "owner-objects").exists())

    def test_partial_batch_is_rejected_before_first_object_is_written(self):
        self.bundle["bindings"].append(dict(self.binding,object_id="f"*64))
        self.rewrite()
        with self.assertRaises(ValueError): self.execute()
        self.assertFalse(self.saved)
        self.assertFalse((self.directory / "pending-updates.json").exists())

    def test_manifest_approval_and_payload_tampering_fail(self):
        self.manifest.write_bytes(self.manifest.read_bytes()+b" ")
        with self.assertRaises(ValueError): self.execute()
        self.rewrite()
        (self.root / "native.pdf").write_bytes(b"x"*len(self.payload))
        with self.assertRaises(ValueError): self.execute()
        self.assertFalse(self.saved)

    def test_cdx_replay_and_memento_proof_failures(self):
        changes = [("target", "https://example.org/other"), ("cdx_status",429),
                   ("replay_status",302), ("replay_url",self.capture["url"]),
                   ("replay_sha256","f"*64), ("replay_bytes",1), ("redirects_followed",1),
                   ("capture_verified",False),
                   ("replay_headers",{"Content-Type":"text/html", "Memento-Datetime":"Tue, 05 Oct 2021 19:24:08 GMT"}),
                   ("replay_headers",{"Content-Type":"application/pdf", "Memento-Datetime":"Wed, 06 Oct 2021 19:24:08 GMT"})]
        initial = copy.deepcopy(self.proof)
        for key,value in changes:
            with self.subTest(key=key,value=value):
                self.proof = dict(copy.deepcopy(initial), **{key:value})
                self.rewrite()
                with self.assertRaises(ValueError): self.execute()
                self.assertFalse(self.saved)
        self.proof = initial
        for key,value in [("statuscode","404"),("timestamp","20211006192408"),("digest","WRONG"),
                          ("original","https://example.org/other"),("mimetype","text/html")]:
            with self.subTest(row=key):
                self.proof = copy.deepcopy(initial)
                self.proof["selected_candidate"][key] = value
                self.rewrite()
                with self.assertRaises(ValueError): self.execute()

    def test_query_source_and_raw_capture_original_remain_distinct(self):
        result = validate_bundle(self.manifest,self.approved,self.registry)
        self.assertNotEqual(result["source"]["url"],result["capture"]["capture_original_url"])
        self.proof["cdx_parameters"]["url"] = self.capture["capture_original_url"]
        self.rewrite()
        with self.assertRaises(ValueError): self.execute()

    def test_backup_storage_and_independent_receipt_are_required(self):
        for field,value in [("independent",False),("restored_sha256","f"*64)]:
            self.bundle["payload"]["backup_receipt"]["verification"][field] = value
            self.rewrite()
            with self.assertRaises(ValueError): self.execute()
        self.assertFalse(self.saved)

    def test_pending_job_or_other_capture_is_not_overwritten(self):
        for old in [{"status":"pending","job_id":"accepted"},
                    {"status":"ok","capture":"https://web.archive.org/web/20200101000000/https://example.org/other"}]:
            self.saved = {self.source["url"]:old}
            before = copy.deepcopy(self.saved)
            with self.assertRaises(ValueError): self.execute()
            self.assertEqual(before,self.saved)

    def test_control_cooldown_canary_and_pacing_bytes_unchanged(self):
        with Control(self.directory,None) as owner:
            owner.state.update(mode="half_open", probe_url="https://example.org/canary",
                               next_attempt=9999999999,next_submission_at=9999999999)
            owner.save()
            before = (self.directory / "control.json").read_bytes()
            self.execute(owner)
            self.assertEqual(before,(self.directory / "control.json").read_bytes())

    def test_unrelated_pending_journal_is_persisted_not_discarded(self):
        unrelated = {"status":"pending", "job_id":"previous-job"}
        atomic_json(self.directory / "pending-updates.json",{"schema":1,"base":{"other":None},"updates":{"other":unrelated}})
        self.execute()
        self.assertEqual(unrelated,self.saved["other"])

    def test_real_owner_lock_excludes_another_process_context(self):
        with Control(self.directory,None):
            with self.assertRaises(Busy):
                with Control(self.directory,None): self.fail("second owner")

    def test_paths_symlinks_and_size_guards(self):
        for path in ["../native.pdf","/native.pdf","a/../native.pdf","a\\native.pdf","./native.pdf","C:relative.pdf","C:/native.pdf"]:
            self.bundle["payload"]["path"] = path
            self.rewrite()
            with self.assertRaises(ValueError): self.execute()
        self.bundle["payload"]["path"] = "link.pdf"
        (self.root / "link.pdf").symlink_to(self.root / "native.pdf")
        self.rewrite()
        with self.assertRaises(ValueError): self.execute()

    def test_inbox_missing_conflict_and_malformed_receipts_remain_retrievable(self):
        with Control(self.directory,None) as owner:
            inbox = worker.verify_inbox_dir(owner)
            receipt = {"schema":1,"updates":{
                "missing":{"status":"verified","capture":"capture"},
                "conflict":{"status":"verified","capture":"new"},
                "valid":{"status":"verified","capture":"same","verify":{"sha256":"legacy"}}}}
            raw = canonical_bytes(receipt)
            path = inbox / "mixed.json"
            path.write_bytes(raw)
            bad = inbox / "bad.json"
            bad.write_bytes(b"not json")
            done = {"conflict":{"status":"pending","capture":"old"},"valid":{"status":"ok","capture":"same"}}
            changed = {}
            self.assertEqual(1,worker.apply_verify_inbox(owner,done,changed))
            self.assertTrue(path.exists())
            self.assertTrue(bad.exists())
            self.assertEqual("verified",done["valid"]["status"])
            directory = self.directory / "verify-receipts" / hashlib.sha256(raw).hexdigest()
            retained = json.loads((directory / "original.json").read_text())
            self.assertEqual(raw,base64.b64decode(retained["original_base64"]))
            dispositions = [json.loads(x.read_text()) for x in directory.glob("*.json") if x.name!="original.json"]
            self.assertEqual("missing_prior_done_or_capture",dispositions[0]["dispositions"]["missing"])
            self.assertEqual("capture_conflict",dispositions[0]["dispositions"]["conflict"])

    def test_legacy_receipt_checkpoint_survives_crash_before_unlink(self):
        with Control(self.directory,None) as owner:
            inbox = worker.verify_inbox_dir(owner)
            raw = canonical_bytes({"schema":1,"updates":{"url":{"status":"verified","capture":"same"}}})
            path = inbox / "receipt.json"
            path.write_bytes(raw)
            done = {"url":{"status":"ok","capture":"same"}}
            before = copy.deepcopy(done)
            owner.initial_done = copy.deepcopy(done)
            with patch.object(Path,"unlink",side_effect=RuntimeError("injected crash")):
                with self.assertRaises(RuntimeError):
                    worker.apply_verify_inbox(owner,done,{})
            self.assertTrue(path.exists())
            restored = copy.deepcopy(before)
            owner.restore_updates(restored)
            self.assertEqual("verified",restored["url"]["status"])
            self.assertEqual(0,worker.apply_verify_inbox(owner,restored,{}))
            self.assertFalse(path.exists())

    def test_legacy_oversize_receipt_stays_in_inbox_without_mutation(self):
        with Control(self.directory,None) as owner:
            path = worker.verify_inbox_dir(owner) / "large.json"
            with path.open("wb") as out:
                out.truncate(8*1024*1024+1)
            self.assertEqual(0,worker.apply_verify_inbox(owner,{},{}))
            self.assertTrue(path.exists())

    def test_old_object_pointer_generation_advance_rejects_before_ledger_write(self):
        self.execute()
        old_saved = copy.deepcopy(self.saved)
        followup = copy.deepcopy(self.request)
        followup.update(generation=1, previous_request_id=self.result["request_id"])
        followup["continuation"] = "New source observation"
        result = register(self.registry,followup)
        self.bundle["bindings"][0]["request_id"] = result["request_id"]
        self.rewrite()
        count = len(self.commits)
        with self.assertRaisesRegex(ValueError,"different request"):
            self.execute()
        self.assertEqual(count,len(self.commits))
        self.assertEqual(old_saved,self.saved)

    def test_wrong_registered_payload_metadata_rejected(self):
        for metadata in [{"registered_payload_sha256":"f"*64}, {"registry_job_id":"payload:"+"f"*64}]:
            self.saved = {self.source["url"]:dict(status="ok",**metadata)}
            old = copy.deepcopy(self.saved)
            with self.assertRaisesRegex(ValueError,"registration metadata"):
                self.execute()
            self.assertEqual(old,self.saved)

    def test_failed_git_persist_leaves_journal_and_no_verified_export(self):
        self.client.persist_changes = lambda *a: (_ for _ in ()).throw(RuntimeError("Git unavailable"))
        with self.assertRaises(RuntimeError): self.execute()
        self.assertTrue((self.directory / "pending-updates.json").exists())
        self.assertFalse((self.registry / "owner-objects").exists())
        self.assertEqual("ready",export_records(self.registry,object_ids={self.result["object_id"]})["objects"][0]["state"])

    def test_recovery_after_ledger_persist_before_object_receipt(self):
        with patch("preservation_capture_adoption.store_object_event",side_effect=RuntimeError("injected crash")):
            with self.assertRaises(RuntimeError): self.execute()
        self.assertEqual("verified",self.saved[self.source["url"]]["status"])
        self.execute()
        self.assertEqual("verified",export_records(self.registry,object_ids={self.result["object_id"]})["objects"][0]["state"])

    def test_http_or_html_observation_cannot_borrow_native_receipt(self):
        self.proof["selected_candidate"]["statuscode"] = "200"
        self.proof["replay_headers"]["Content-Type"] = "text/html"
        self.rewrite()
        with self.assertRaises(ValueError): self.execute()

    def test_normal_owner_prepare_and_finish_skip_exact_adopted_object_without_network(self):
        with Control(self.directory,None) as owner:
            self.execute(owner)
            owner.state["mode"] = "healthy"
            owner.done = copy.deepcopy(self.saved)
            self.client.ACTIVE_CONTROL = owner
            self.client.fetch = lambda *a: self.fail("adopted object fetched again")
            adapter = OwnerAdapter(self.client,self.repo,owner,{self.binding["object_id"]},work=self.root/"work")
            self.assertEqual(0,adapter.prepare(time.monotonic()+300)["prepared"])
            self.assertEqual(0,adapter.finish(time.monotonic()+300))

    def test_scoped_event_cannot_borrow_a_different_subject(self):
        self.execute()
        with self.assertRaises(ValueError):
            load_event(self.registry,self.request["source"],object_id=self.binding["object_id"],
                       request_id=self.binding["request_id"],subject=dict(self.subject,title="different"))

    def test_normal_owner_keeps_other_same_payload_objects_eligible(self):
        self.execute()
        other = copy.deepcopy(self.request)
        other["subject"] = dict(self.subject,title="Another publication")
        other["backup_receipt"]["subject"] = other["subject"]
        other["source_backup_receipt"] = copy.deepcopy(self.request["backup_receipt"])
        result = register(self.registry,other)
        with Control(self.directory,None) as owner:
            self.client.ACTIVE_CONTROL = owner
            adapter = OwnerAdapter(self.client,self.repo,owner,{self.binding["object_id"],result["object_id"]},work=self.root/"work")
            groups = adapter._groups()
            self.assertEqual([result["object_id"]],list(groups.values())[0]["objects"])


if __name__ == "__main__":
    unittest.main()
