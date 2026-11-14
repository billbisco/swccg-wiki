import copy
import hashlib
import io
import json
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from preservation_backups import (UnavailablePublicVersion, file_artifact,
                                  independent_receipt, revision_artifact)
from preservation_contracts import validate_backup_receipt


def revision(title="Talk:日本語", revision_id=23, text="日本語の本文\n"):
    page = dict(pageid=12, title=title)
    raw = text.encode()
    data = dict(revid=revision_id, parentid=revision_id - 1,
                timestamp="2026-11-14T00:00:00Z", sha1=hashlib.sha1(raw).hexdigest(),
                slots=dict(main=dict(content=text, contentmodel="wikitext")))
    return page, data


def image(title="File:original.png", timestamp="2026-11-14T00:00:00Z"):
    raw = b"\x89PNG\r\n\x1a\nexact original bytes"
    info = dict(timestamp=timestamp, url="https://wiki.swccg.com/images/archive/a/ab/original.png",
                sha1=hashlib.sha1(raw).hexdigest(), size=len(raw), mime="image/png", archivename="public-version")
    return file_artifact(title, info, raw)


def storage(artifact):
    return dict(kind="git", repository="https://github.com/billbisco/swccg-wiki-files",
                commit="a" * 40, path=artifact.payload_path,
                metadata_path=artifact.metadata_path, metadata_bytes=len(artifact.metadata_bytes()),
                metadata_sha256=hashlib.sha256(artifact.metadata_bytes()).hexdigest())


class ArtifactTests(unittest.TestCase):
    def test_public_talk_and_file_description_revisions_keep_exact_text_and_ids(self):
        for title in ("Talk:日本語", "File:original.png", "File talk:original.png"):
            page, data = revision(title)
            artifact = revision_artifact(page, data)
            self.assertEqual(data["slots"]["main"]["content"].encode(), artifact.payload)
            self.assertEqual(23, artifact.subject["revision_id"])
            self.assertEqual(title, artifact.subject["title"])
            self.assertEqual(data["sha1"], artifact.provenance["wiki_sha1"])

    def test_nonpublic_versions_never_become_public_artifacts(self):
        page, data = revision()
        data["texthidden"] = True
        with self.assertRaises(UnavailablePublicVersion):
            revision_artifact(page, data)

    def test_mismatching_source_hash_or_size_is_rejected(self):
        page, data = revision()
        data["sha1"] = "b" * 40
        with self.assertRaisesRegex(ValueError, "SHA-1"):
            revision_artifact(page, data)
        raw = b"bytes"
        with self.assertRaisesRegex(ValueError, "byte count"):
            file_artifact("File:test.png", dict(size=99), raw)

    def test_same_bytes_deduplicate_payload_while_preserving_all_version_metadata(self):
        first = image()
        second = image("File:another.png")
        third = image(timestamp="2026-11-13T00:00:00Z")
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            for artifact in (first, second, third, first):
                artifact.write(repo)
            self.assertEqual(1, len(list((repo / "preservation/objects").rglob("*.bin"))))
            self.assertEqual(3, len(list((repo / "preservation/versions").glob("*.json"))))
            self.assertEqual(first.payload, (repo / first.payload_path).read_bytes())

    def test_conflicting_local_artifact_is_not_overwritten(self):
        artifact = image()
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            artifact.write(repo)
            (repo / artifact.payload_path).write_bytes(b"different bytes")
            with self.assertRaisesRegex(ValueError, "conflicting"):
                artifact.write(repo)


class IndependentRestoreTests(unittest.TestCase):
    def fake_fetch(self, artifact, *, payload=None, metadata=None, calls=None):
        def fetch(url):
            if calls is not None:
                calls.append(url)
            if url.endswith(artifact.metadata_path):
                return io.BytesIO(artifact.metadata_bytes() if metadata is None else metadata)
            return io.BytesIO(artifact.payload if payload is None else payload)
        return fetch

    def test_article_restore_reads_independent_commit_only_and_restores_metadata(self):
        artifact = revision_artifact(*revision())
        calls = []
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "restored.wiki"
            receipt = independent_receipt(artifact.subject, storage(artifact),
                                          fetch=self.fake_fetch(artifact, calls=calls), restore_to=target)
            self.assertEqual([], validate_backup_receipt(receipt, artifact.subject))
            self.assertEqual(artifact.payload, target.read_bytes())
            self.assertTrue(receipt["verification"]["metadata_matches_subject"])
        self.assertEqual(2, len(calls))
        self.assertTrue(all(url.startswith("https://raw.githubusercontent.com/billbisco/") for url in calls))
        self.assertTrue(all("a" * 40 in url for url in calls))
        self.assertFalse(any("wiki.swccg.com" in url for url in calls))

    def test_image_restore_proves_original_bytes_with_live_source_unavailable(self):
        artifact = image()
        receipt = independent_receipt(artifact.subject, storage(artifact), fetch=self.fake_fetch(artifact))
        self.assertEqual(artifact.subject["content_sha256"], receipt["verification"]["restored_sha256"])
        self.assertEqual(artifact.subject["bytes"], receipt["verification"]["restored_bytes"])

    def test_wrong_hash_does_not_publish_restore_or_receipt(self):
        artifact = image()
        corrupt = bytes([artifact.payload[0] ^ 1]) + artifact.payload[1:]
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "existing.bin"
            target.write_bytes(b"existing restore")
            with self.assertRaisesRegex(ValueError, "SHA-256"):
                independent_receipt(artifact.subject, storage(artifact),
                                    fetch=self.fake_fetch(artifact, payload=corrupt), restore_to=target)
            self.assertEqual(b"existing restore", target.read_bytes())
            self.assertEqual([], list(Path(directory).glob(".restore-*")))

    def test_oversized_or_truncated_backup_is_not_recoverable(self):
        artifact = image()
        for payload in (artifact.payload + b"extra", artifact.payload[:-1]):
            with self.subTest(bytes=len(payload)):
                with self.assertRaisesRegex(ValueError, "byte count"):
                    independent_receipt(artifact.subject, storage(artifact), fetch=self.fake_fetch(artifact, payload=payload))

    def test_wrong_version_metadata_is_rejected_even_if_payload_matches(self):
        artifact = image()
        wrong = json.loads(artifact.metadata_bytes())
        wrong["subject"]["upload_timestamp"] = "2026-11-12T00:00:00Z"
        raw = json.dumps(wrong).encode()
        location = storage(artifact)
        location["metadata_bytes"] = len(raw)
        location["metadata_sha256"] = hashlib.sha256(raw).hexdigest()
        with self.assertRaisesRegex(ValueError, "exact original version"):
            independent_receipt(artifact.subject, location, fetch=self.fake_fetch(artifact, metadata=raw))

    def test_mutable_commit_or_other_repository_is_rejected_before_fetch(self):
        artifact = image()
        for fields in (dict(commit="main"), dict(repository="https://wiki.swccg.com")):
            location = dict(storage(artifact), **fields)
            with self.assertRaises(ValueError):
                independent_receipt(artifact.subject, location,
                                    fetch=lambda url: self.fail("unapproved backup was fetched"))


class ContainerRestoreTests(unittest.TestCase):
    def fixture(self, names=None):
        artifact = revision_artifact(*revision())
        source = io.BytesIO()
        entries = names or [("page.wiki", artifact.payload), ("MANIFEST.json", b'{"files":1}')]
        with tarfile.open(fileobj=source, mode="w:xz") as archive:
            for name, raw in entries:
                info = tarfile.TarInfo(name)
                info.size = len(raw)
                archive.addfile(info, io.BytesIO(raw))
        compressed = source.getvalue()
        location = dict(kind="git", repository="https://github.com/billbisco/swccg-wiki-files",
                        commit="a" * 40, path="source-evidence/source.tar.xz", container="tar.xz",
                        member="page.wiki", artifact_sha256=hashlib.sha256(compressed).hexdigest(),
                        artifact_bytes=len(compressed), uncompressed_bytes=sum(len(raw) for _, raw in entries))
        return artifact, location, compressed

    def test_member_restore_separates_raw_payload_and_compressed_artifact_hashes(self):
        artifact, location, compressed = self.fixture()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "restored.wiki"
            receipt = independent_receipt(artifact.subject, location,
                                          fetch=lambda url: io.BytesIO(compressed), restore_to=target)
            self.assertEqual(artifact.payload, target.read_bytes())
        self.assertEqual([], validate_backup_receipt(receipt, artifact.subject))
        self.assertEqual(artifact.subject["content_sha256"], receipt["verification"]["restored_sha256"])
        self.assertEqual(location["artifact_sha256"], receipt["verification"]["restored_container_sha256"])
        self.assertNotEqual(receipt["verification"]["restored_sha256"], receipt["verification"]["restored_container_sha256"])

    def test_container_hash_or_member_tally_mismatch_cannot_create_receipt(self):
        artifact, location, compressed = self.fixture()
        for change in (dict(artifact_sha256="b" * 64), dict(uncompressed_bytes=len(artifact.payload))):
            with self.subTest(change=change):
                with self.assertRaises(ValueError):
                    independent_receipt(artifact.subject, dict(location, **change), fetch=lambda url: io.BytesIO(compressed))

    def test_unsafe_or_duplicate_member_does_not_escape_or_create_restore(self):
        artifact, _, _ = self.fixture()
        for entries in ([('../escape', b'bad'), ('page.wiki', artifact.payload)],
                        [('page.wiki', artifact.payload), ('page.wiki', artifact.payload)]):
            artifact, location, compressed = self.fixture(entries)
            with tempfile.TemporaryDirectory() as directory:
                target = Path(directory) / "restored.wiki"
                with self.assertRaises(ValueError):
                    independent_receipt(artifact.subject, location, fetch=lambda url: io.BytesIO(compressed), restore_to=target)
                self.assertFalse(target.exists())

    def test_container_receipt_without_independent_container_verification_fails(self):
        artifact, location, compressed = self.fixture()
        receipt = independent_receipt(artifact.subject, location, fetch=lambda url: io.BytesIO(compressed))
        receipt["verification"].pop("restored_container_sha256")
        self.assertTrue(validate_backup_receipt(receipt, artifact.subject))


if __name__ == "__main__":
    unittest.main()
