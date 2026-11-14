import contextlib
import json
import sys
import tempfile
import tracemalloc
import unittest
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parents[1]), str(Path(__file__).resolve().parents[2] / "tools")]
from backup_projection import Projection
from backup_projection import MAX_TABLE_BYTES
from preservation_backups import revision_artifact, file_artifact
from test_backup_versions import revision, file_info


class ProjectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def projector(self, kind="page"):
        return Projection(self.root, kind, guard=lambda repo: contextlib.nullcontext())

    def test_latest_revision_updates_existing_compatible_index_path(self):
        directory = self.root / "pages/player-stubs"
        directory.mkdir(parents=True)
        (directory / "Example.wiki").write_text("old", encoding="utf-8")
        (self.root / "pages/INDEX.tsv").write_text("Example\tpages/player-stubs/Example.wiki\n", encoding="utf-8")
        projector = self.projector()
        observed = projector.observe("Example")
        artifact = revision_artifact({"title": "Example"}, revision())
        paths = projector.write(artifact, observed)
        self.assertIn("pages/player-stubs/Example.wiki", paths)
        self.assertEqual(artifact.payload, (directory / "Example.wiki").read_bytes())
        self.assertIn("Example\tpages/player-stubs/Example.wiki", (self.root / "pages/INDEX.tsv").read_text())

    def test_peer_flat_file_advance_is_preserved(self):
        projector = self.projector()
        observed = projector.observe("Example")
        target = self.root / observed["relative"]
        target.parent.mkdir(parents=True)
        target.write_text("peer's newer live text", encoding="utf-8")
        self.assertEqual([], projector.write(revision_artifact({"title": "Example"}, revision()), observed))
        self.assertEqual("peer's newer live text", target.read_text())
        self.assertIn("peer advanced", projector.deferred_reason)

    def test_peer_index_move_is_preserved_even_when_old_target_bytes_did_not_change(self):
        projector = self.projector()
        artifact = revision_artifact({"title": "Example"}, revision())
        projector.write(artifact, projector.observe("Example"))
        observed = projector.observe("Example")
        index = self.root / "pages/INDEX.tsv"
        index.write_text("Example\tpages/moved.wiki\nOther\tpages/Other.wiki\n", encoding="utf-8")
        self.assertEqual([], projector.write(artifact, observed))
        self.assertIn("pages/moved.wiki", index.read_text())
        self.assertIn("index mapping", projector.deferred_reason)

    def test_unrelated_peer_index_addition_is_merged(self):
        projector = self.projector()
        artifact = revision_artifact({"title": "Example"}, revision())
        observed = projector.observe("Example")
        (self.root / "pages").mkdir()
        (self.root / "pages/INDEX.tsv").write_text("Other\tpages/Other.wiki\n", encoding="utf-8")
        self.assertTrue(projector.write(artifact, observed))
        self.assertIn("Other\tpages/Other.wiki", (self.root / "pages/INDEX.tsv").read_text())

    def test_historical_revision_cannot_move_projection_backwards(self):
        projector = self.projector()
        latest = revision_artifact({"title": "Example"}, revision(50, "new"))
        projector.write(latest, projector.observe("Example"))
        old = revision_artifact({"title": "Example"}, revision(49, "old"))
        self.assertEqual([], projector.write(old, projector.observe("Example")))
        self.assertEqual(b"new", (self.root / "pages/Example.wiki").read_bytes())

    def test_filename_collision_gets_separate_compatible_index_row(self):
        projector = self.projector()
        first = revision_artifact({"title": "A/B"}, revision())
        projector.write(first, projector.observe("A/B"))
        second = revision_artifact({"title": "A B"}, revision(43, "second"))
        observed = projector.observe("A B")
        self.assertNotEqual("pages/A_B.wiki", observed["relative"])
        projector.write(second, observed)
        self.assertEqual(first.payload, (self.root / "pages/A_B.wiki").read_bytes())
        self.assertEqual(2, len((self.root / "pages/INDEX.tsv").read_text().splitlines()))

    def test_replacement_updates_current_file_index_and_keeps_old_usage(self):
        projector = self.projector("file")
        first = file_artifact("File:Test.bin", file_info(b"old"), b"old")
        projector.write(first, projector.observe("File:Test.bin"))
        second = file_artifact("File:Test.bin", file_info(b"new content", "2026-11-15T00:00:00Z"), b"new content")
        projector.write(second, projector.observe("File:Test.bin"))
        self.assertEqual(b"new content", (self.root / "files/Test.bin").read_bytes())
        index = (self.root / "files/INDEX.tsv").read_text().splitlines()
        self.assertEqual(["Test.bin\tTest.bin\tapplication/octet-stream\t11"], index)
        projector.usage("File:Test.bin", [{"title": "Old Article"}])
        projector.usage("File:Test.bin", [{"title": "New Article"}])
        self.assertEqual({"Test.bin\tOld Article", "Test.bin\tNew Article"}, set((self.root / "files/USAGE.tsv").read_text().splitlines()))

    def test_oversize_metadata_input_is_rejected_before_unbounded_split(self):
        directory = self.root / "pages"
        directory.mkdir()
        path = directory / "INDEX.tsv"
        with path.open("wb") as stream:
            stream.truncate(MAX_TABLE_BYTES + 1)
        with self.assertRaisesRegex(ValueError, "16 MiB"):
            self.projector().observe("Example")

    def test_current_sized_usage_table_has_measured_memory_budget(self):
        directory = self.root / "files"
        directory.mkdir()
        path = directory / "USAGE.tsv"
        with path.open("w", encoding="utf-8") as stream:
            for number in range(56000):
                stream.write(f"File{number:06}.gif\tSome article with a representative title {number:06}\n")
        self.assertGreater(path.stat().st_size, 3 * 1024 * 1024)
        tracemalloc.start()
        try:
            self.projector("file").usage("File:Test.bin", [{"title": "New"}])
            _, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()
        self.assertLess(peak, 64 * 1024 * 1024)


if __name__ == "__main__":
    unittest.main()
