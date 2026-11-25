import json
import os
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import ia_item_backup as B


class BackupTests(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory(); self.addCleanup(self.t.cleanup)
        self.root = Path(self.t.name) / "files"; (self.root / "a").mkdir(parents=True)
        for i in range(30):
            (self.root / "a" / f"f{i}.txt").write_text(str(i))
        (self.root / "thumb").mkdir(); (self.root / "thumb" / "skip.png").write_text("x")
        self.state = Path(self.t.name) / "state"
        self.p = [patch.object(B, "STATE", self.state),
                  patch.object(B, "items_for", return_value={"it": (self.root, "T", "D")}),
                  patch.object(B, "keys", return_value="LOW a:b"),
                  patch.object(B, "item_owner_ok", return_value=True),
                  patch.object(B, "over_limit", return_value=False),
                  patch.object(B, "GAP_S", 0)]
        for x in self.p: x.start(); self.addCleanup(x.stop)

    def run_main(self, *args):
        with patch.object(sys, "argv", ["x", "--group", "snapshots", *args]):
            B.main()
        return json.loads((self.state / "ledger.json").read_text())

    def test_parallel_upload_all_once_and_skip_thumbs(self):
        calls, first = [], []
        lock = threading.Lock()
        def put(auth, item, name, path, md5, meta, f):
            with lock:
                calls.append(name); first.append(f)
        with patch.object(B, "put", side_effect=put):
            led = self.run_main("--workers", "4")
            self.assertEqual(30, len(calls)); self.assertEqual(30, len(set(calls)))
            self.assertEqual(1, sum(first)); self.assertNotIn("thumb/skip.png", calls)
            self.assertEqual(30, len(led))
            calls.clear(); self.run_main()
            self.assertEqual([], calls)  # unchanged files are not sent again

    def test_stop_halts_run(self):
        n = [0]
        def put(*a):
            n[0] += 1
            if n[0] >= 3: raise B.Stop("429")
        with patch.object(B, "put", side_effect=put):
            led = self.run_main("--workers", "2")
        self.assertLess(len(led), 10)

    def test_verify_marks_matching_sha1(self):
        led = {"it/a/f1.txt": {"item": "it", "name": "a/f1.txt", "sha1": "s1"},
               "it/a/f2.txt": {"item": "it", "name": "a/f2.txt", "sha1": "s2"}}
        class R:
            def __enter__(s): return s
            def __exit__(s, *a): pass
            def read(s): return json.dumps({"result": [{"name": "a/f1.txt", "sha1": "s1"}, {"name": "a/f2.txt", "sha1": "zz"}]}).encode()
        with patch.object(B, "request", return_value=R()), patch.object(B.time, "sleep"):
            st = B.verify(led, ["it"])
        self.assertEqual({"verified": 1, "sha1_differs": 1}, st); self.assertIn("verified", led["it/a/f1.txt"])


if __name__ == "__main__":
    unittest.main()
