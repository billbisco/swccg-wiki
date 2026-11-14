"""Chunk profile regression fixtures. All fetches are memory-only, no external IO."""
import copy
import hashlib
import io
import json
import socket
import sys
import tempfile
import unittest
import urllib.parse
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import preservation_chunks as chunks
import preservation_chunk_profile as profile
from preservation_backups import independent_receipt
from preservation_backups import _fetch
from preservation_contracts import canonical_bytes, validate_backup_receipt


class ChunkTests(unittest.TestCase):
    def setUp(self):
        self.no_network = patch.object(socket.socket, "connect", side_effect=AssertionError("external network forbidden"))
        self.no_network.start()
        self.addCleanup(self.no_network.stop)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.data = b"%PDF-1.7\n" + bytes(range(256)) + b"\n%%EOF"
        self.subject = dict(kind="source_snapshot", title="complete public source", bytes=len(self.data),
                            content_sha256=hashlib.sha256(self.data).hexdigest())
        self.source = self.root / "source.pdf"
        self.source.write_bytes(self.data)
        self.stage = self.root / "stage"
        result = chunks.stage(self.subject, self.source, self.stage, part_bytes=64)
        self.manifest = result["manifest"]
        self.storage = dict(kind=profile.KIND, repository="https://github.com/billbisco/swccg-wiki",
                            commit="a" * 40, path=result["manifest_path"], manifest_sha256=result["manifest_sha256"],
                            manifest_bytes=result["manifest_bytes"], parts=result["manifest"]["parts"])
        self.files = {str(p.relative_to(self.stage)).replace("\\", "/"): p.read_bytes() for p in self.stage.rglob("*") if p.is_file()}
        self.calls = []
        self.meta_override = {}

    def fetch(self, url):
        self.calls.append(url)
        repo = self.storage["repository"].removeprefix("https://github.com/")
        if url.startswith("https://api.github.com/repos/" + repo + "/contents/"):
            tail = url.split("/contents/", 1)[1]
            path, query = tail.split("?", 1)
            self.assertEqual(query, "ref=" + self.storage["commit"])
            path = urllib.parse.unquote(path)
            if path not in self.files:
                raise FileNotFoundError(path)
            data = self.files[path]
            git = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            meta = dict(type="file", path=path, size=len(data), sha=git,
                        git_url="https://api.github.com/repos/" + repo + "/git/blobs/" + git,
                        download_url="https://raw.githubusercontent.com/" + repo + "/" + self.storage["commit"] + "/" + urllib.parse.quote(path, safe="/"))
            meta.update(self.meta_override)
            return io.BytesIO(canonical_bytes(meta))
        prefix = "https://raw.githubusercontent.com/" + repo + "/" + self.storage["commit"] + "/"
        self.assertTrue(url.startswith(prefix))
        path = urllib.parse.unquote(url.removeprefix(prefix))
        if path not in self.files:
            raise FileNotFoundError(path)
        return io.BytesIO(self.files[path])

    def recover(self, **kwargs):
        return independent_receipt(self.subject, self.storage, fetch=self.fetch, **kwargs)

    def manifest_update(self, manifest):
        raw = canonical_bytes(manifest) + b"\n"
        self.files[self.storage["path"]] = raw
        self.storage.update(manifest_sha256=hashlib.sha256(raw).hexdigest(), manifest_bytes=len(raw))

    def test_full_independent_metadata_every_part_and_atomic_restore(self):
        out = self.root / "restored.pdf"
        r = self.recover(restore_to=out)
        self.assertEqual(out.read_bytes(), self.data)
        self.assertEqual(validate_backup_receipt(r, self.subject), [])
        self.assertEqual(len(r["verification"]["part_readbacks"]), len(self.storage["parts"]))
        self.assertEqual(len(self.calls), 2 * (1 + len(self.storage["parts"])))
        self.assertTrue(all("a" * 40 in u for u in self.calls))

    def test_failed_restore_never_replaces_existing_destination(self):
        out = self.root / "restored.pdf"
        out.write_bytes(b"previous")
        self.files[self.storage["parts"][-1]["path"]] = b"broken"
        with self.assertRaises(ValueError):
            self.recover(restore_to=out)
        self.assertEqual(out.read_bytes(), b"previous")
        self.assertFalse(list(self.root.glob(".chunks-*")))

    def test_default_full_budget_cannot_be_bypassed_by_small_parts(self):
        subject = {**self.subject, "bytes": 315358312}
        with self.assertRaisesRegex(ValueError, "budget"):
            independent_receipt(subject, self.storage, fetch=self.fetch)
        self.assertEqual(self.calls, [])

    def test_explicit_manual_budget_still_checks_subject(self):
        with self.assertRaises(ValueError):
            self.recover(chunk_max_total_bytes=self.subject["bytes"] - 1)
        self.assertEqual(self.calls, [])
        self.recover(chunk_max_total_bytes=self.subject["bytes"])

    def test_storage_unknown_fields_profiles_repos_and_commit(self):
        for change in [dict(kind="git_raw_chunks_v2"), dict(commit="main"), dict(repository="https://github.com/other/repo"),
                       dict(container="tar.xz"), dict(path="../manifest.json"), dict(path="C:/file"),
                       dict(manifest_bytes=True), dict(manifest_bytes=profile.MANIFEST_LIMIT + 1)]:
            storage = {**self.storage, **change}
            with self.subTest(change=change), self.assertRaises(ValueError):
                independent_receipt(self.subject, storage, fetch=self.fetch)

    def test_strict_order_paths_offsets_and_bounds(self):
        for field, value in [("index", 1), ("index", True), ("offset", 1), ("offset", -1), ("path", "../part"),
                             ("path", "/part"), ("path", "part\\bad"), ("path", "part//bad"),
                             ("bytes", profile.PART_LIMIT + 1), ("bytes", 0), ("bytes", True),
                             ("sha256", "0"), ("commit", "b" * 40), ("repository", "https://github.com/other/repo")]:
            storage = copy.deepcopy(self.storage)
            storage["parts"][0][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                independent_receipt(self.subject, storage, fetch=self.fetch)
        for parts in [[], self.storage["parts"][:-1], list(reversed(self.storage["parts"])),
                      [self.storage["parts"][0]] * len(self.storage["parts"])]:
            with self.subTest(parts=parts), self.assertRaises(ValueError):
                independent_receipt(self.subject, {**self.storage, "parts": parts}, fetch=self.fetch)

    def test_manifest_subject_version_unknown_fields_and_part_order(self):
        for key, value in [("schema_version", True), ("schema_version", 2), ("profile", "other"),
                           ("subject", {**self.subject, "title": "different original"}),
                           ("parts", list(reversed(self.manifest["parts"]))), ("ignored", True)]:
            with self.subTest(key=key):
                manifest = {**self.manifest, key: value}
                self.manifest_update(manifest)
                with self.assertRaises(ValueError):
                    self.recover()

    def test_wrong_manifest_hash_missing_manifest_and_json_as_raw_source(self):
        original = self.files[self.storage["path"]]
        self.files[self.storage["path"]] = original.replace(b"source_snapshot", b"source_snapshou")
        with self.assertRaises(ValueError):
            self.recover()
        del self.files[self.storage["path"]]
        with self.assertRaises(FileNotFoundError):
            self.recover()
        self.files[self.storage["path"]] = original
        self.files[self.storage["parts"][0]["path"]] = original  # manifest is not the original PDF
        with self.assertRaises(ValueError):
            self.recover()

    def test_missing_truncated_extended_and_modified_parts(self):
        path = self.storage["parts"][1]["path"]
        original = self.files[path]
        for changed in [original[:-1], original + b"x", bytes([original[0] ^ 1]) + original[1:]]:
            self.files[path] = changed
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                self.recover()
        del self.files[path]
        with self.assertRaises(FileNotFoundError):
            self.recover()

    def test_wrong_full_hash_rejected_even_when_every_part_is_valid(self):
        self.subject = {**self.subject, "content_sha256": "0" * 64}
        self.manifest_update({**self.manifest, "subject": self.subject})
        with self.assertRaisesRegex(ValueError, "COMPLETE"):
            self.recover()

    def test_git_metadata_path_sha_type_size_and_mixed_commit_rejected(self):
        for override in [dict(path="other"), dict(sha="b" * 40), dict(type="symlink"), dict(size=True),
                         dict(sha="b" * 40, git_url="https://api.github.com/repos/billbisco/swccg-wiki/git/blobs/" + "b" * 40),
                         dict(download_url="https://raw.githubusercontent.com/billbisco/swccg-wiki/" + "b" * 40 + "/x"),
                         dict(git_url="https://api.github.com/repos/other/repo/git/blobs/" + "a" * 40)]:
            self.meta_override = override
            with self.subTest(override=override), self.assertRaises(ValueError):
                self.recover()

    def test_lfs_source_and_part_rejected(self):
        pointer = chunks.LFS_HEADER + b"\noid sha256:" + b"a" * 64 + b"\nsize 9999\n"
        self.source.write_bytes(pointer)
        subject = {**self.subject, "bytes": len(pointer), "content_sha256": hashlib.sha256(pointer).hexdigest()}
        with self.assertRaisesRegex(ValueError, "LFS"):
            chunks.stage(subject, self.source, self.root / "pointer", part_bytes=4)
        self.files[self.storage["path"]] = pointer
        self.storage.update(manifest_sha256=hashlib.sha256(pointer).hexdigest(), manifest_bytes=len(pointer))
        with self.assertRaisesRegex(ValueError, "LFS"):
            self.recover()

    def test_local_only_or_incomplete_proof_and_ignored_fields_fail(self):
        r = self.recover()
        for field, value in [("independent", False), ("method", "local concat"), ("part_readbacks", []),
                             ("ignored_extra", True), ("restored_bytes", True)]:
            changed = copy.deepcopy(r)
            changed["verification"][field] = value
            self.assertTrue(validate_backup_receipt(changed, self.subject), field)
        for field, value in [("commit", "b" * 40), ("repository", "https://github.com/other/repo"), ("index", True)]:
            changed = copy.deepcopy(r)
            changed["verification"]["part_readbacks"][0][field] = value
            self.assertTrue(validate_backup_receipt(changed, self.subject), field)

    def test_stage_wrong_source_size_hash_budget_paths_and_existing_output(self):
        for subject in [{**self.subject, "bytes": len(self.data) + 1}, {**self.subject, "content_sha256": "0" * 64}]:
            with self.assertRaises(ValueError):
                chunks.stage(subject, self.source, self.root / subject["content_sha256"], part_bytes=64)
        for size in [0, True, profile.PART_LIMIT + 1]:
            with self.assertRaises(ValueError):
                chunks.stage(self.subject, self.source, self.root / "invalid", part_bytes=size)
        with self.assertRaises(ValueError):
            chunks.stage(self.subject, self.source, self.root / "unsafe", prefix="../escape")
        with self.assertRaises(FileExistsError):
            chunks.stage(self.subject, self.source, self.stage)

    def test_json_duplicate_and_nonfinite_fields_are_not_ignored(self):
        for raw in [b'{"a":1,"a":1}', b'{"a":NaN}', b'{"a":Infinity}']:
            with self.assertRaises(ValueError):
                chunks._strict_json(raw)

    def test_symlink_source_and_excessive_part_count_rejected_before_writes(self):
        with patch.object(Path, "is_symlink", return_value=True), self.assertRaises(ValueError):
            chunks.stage(self.subject, self.source, self.root / "link")
        subject = {**self.subject, "bytes": profile.PART_COUNT_LIMIT + 1}
        with self.assertRaisesRegex(ValueError, "too many"):
            chunks.stage(subject, self.source, self.root / "many", part_bytes=1)
        self.assertFalse((self.root / "many").exists())

    def test_streams_never_request_unbounded_or_part_sized_buffers(self):
        original = self.fetch
        class Bounded(io.BytesIO):
            def read(stream, size=-1):
                self.assertGreater(size, 0)
                self.assertLessEqual(size, chunks.BUFFER)
                return super().read(size)
        def bounded(url):
            return Bounded(original(url).getvalue())
        independent_receipt(self.subject, self.storage, fetch=bounded)

    def test_second_existing_repository_uses_same_exact_contract(self):
        self.storage["repository"] = "https://github.com/billbisco/swccg-wiki-files"
        self.assertEqual(validate_backup_receipt(self.recover(), self.subject), [])

    def test_partial_installed_contract_without_new_module_fails_closed(self):
        receipt = self.recover()
        with patch.dict(sys.modules, {"preservation_chunk_profile": None}):
            self.assertTrue(any("integration is incomplete" in e for e in validate_backup_receipt(receipt, self.subject)))

    def test_large_contents_metadata_uses_supported_media_raw_git_unchanged(self):
        # GitHub documents the object/raw media requirement for 1–100MB files.
        self.meta_override = dict(encoding="none", content="")
        self.assertEqual(validate_backup_receipt(self.recover(), self.subject), [])
        self.meta_override = {}  # Missing inline content is also valid metadata.
        self.assertEqual(validate_backup_receipt(self.recover(), self.subject), [])
        with patch("preservation_backups.urllib.request.build_opener") as opener:
            _fetch("https://api.github.com/repos/billbisco/swccg-wiki/contents/large.bin?ref=" + "a" * 40)
            request = opener.return_value.open.call_args.args[0]
            self.assertEqual(request.get_header("Accept"), "application/vnd.github.object+json")
            _fetch("https://raw.githubusercontent.com/billbisco/swccg-wiki/" + "a" * 40 + "/large.bin")
            self.assertIsNone(opener.return_value.open.call_args.args[0].get_header("Accept"))

    def test_manifest_cannot_smuggle_boolean_numbers_through_python_equality(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["parts"][0]["index"] = False  # False == 0 is insufficient.
        self.assertTrue(profile.manifest_errors(manifest, self.storage, self.subject))
        tiny = {**self.subject, "bytes": 1}
        self.assertFalse(profile.exact_subject({**tiny, "bytes": True}, tiny))
        self.assertFalse(profile.exact_subject({**tiny, "bytes": 1.0}, tiny))


if __name__ == "__main__":
    unittest.main()
