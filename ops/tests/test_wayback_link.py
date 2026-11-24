"""Offline tests for ops/wayback_link.py (Story swccg-guild/work#1320). No network, no DB."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wayback_link as L

CAP_IMG = "https://web.archive.org/web/20261123010101/https://swccg.com/wiki/images/a/ab/Foo_bar.jpg"
IMG = "https://swccg.com/wiki/images/a/ab/Foo_bar.jpg"
SNAP = "https://swccg.com/snapshots/forum/p1245707.html"
CAP_SNAP = "https://web.archive.org/web/20261124024845/https://swccg.com/snapshots/forum/p1245707.html"
PC = "Preserved copy: [%s Internet Archive]" % CAP_SNAP


class Pure(unittest.TestCase):
    def test_file_title(self):
        self.assertEqual(L.file_title(IMG), "File:Foo bar.jpg")
        self.assertEqual(L.file_title("https://swccg.com/wiki/images/a/ab/X%27s_card.png"), "File:X's card.png")
        self.assertIsNone(L.file_title("https://swccg.com/wiki/images/thumb/a/ab/Foo.jpg/200px-Foo.jpg"))

    def test_forum_key(self):
        self.assertEqual(L.forum_key("https://org.starwarsccg.forum./viewtopic.php?p=1245707#p1245707"), ("p", "1245707"))
        self.assertEqual(L.forum_key("https://forum.starwarsccg.org/viewtopic.php?f=1&t=56104&p=9"), ("p", "9"))
        self.assertEqual(L.forum_key("https://forum.starwarsccg.org/viewtopic.php?t=56104"), ("t", "56104"))
        self.assertIsNone(L.forum_key("https://forum.starwarsccg.org/index.php"))

    def test_original_line_added_once(self):
        text = "Desc\n[[Category:Photos]]"
        new = L.add_original_line(text, CAP_IMG, IMG)
        self.assertIn("== Preservation ==\n" + L.ORIGINAL_LINE % CAP_IMG + "\n\n[[Category:Photos]]", new)
        self.assertIsNone(L.add_original_line(new, CAP_IMG, IMG))  # AC3 idempotent

    def test_original_line_other_capture_counts(self):
        other = "x [https://web.archive.org/web/20250101000000/https://swccg.com/wiki/images/a/ab/Foo_bar.jpg y]"
        self.assertIsNone(L.add_original_line(other, CAP_IMG, IMG))

    def test_original_pending_line_replaced(self):
        text = "== Preservation ==\n" + L.PRESERVATION_PENDING + "\n"
        new = L.add_original_line(text, CAP_IMG, IMG)
        self.assertNotIn(L.PRESERVATION_PENDING, new)
        self.assertEqual(new.count(CAP_IMG), 1)

    def test_ref_append(self):
        text = ('a<ref>[https://forum.starwarsccg.org/viewtopic.php?p=1245707#p1245707 Post], 2019.</ref> b'
                '<ref name="x">[https://forum.starwarsccg.org/viewtopic.php?p=1271192#p1271192 Other]</ref>'
                '<ref>[https://forum.starwarsccg.org/viewtopic.php?p=12457070 Not this]</ref>')
        keys = L.snapshot_keys(SNAP, {SNAP: {"posts": ["1271192"]}})
        new, n = L.add_preserved_copy(text, keys, CAP_SNAP, SNAP)
        self.assertEqual(n, 2)
        self.assertIn("Post], 2019. " + PC + "</ref>", new)
        self.assertIn("Other]. " + PC + "</ref>", new)
        self.assertIn("12457070 Not this]</ref>", new)
        again, n2 = L.add_preserved_copy(new, keys, CAP_SNAP, SNAP)  # AC3
        self.assertEqual((again, n2), (new, 0))

    def test_ref_with_existing_wayback_untouched(self):
        text = ('<ref>[https://forum.starwarsccg.org/viewtopic.php?p=1245707 P] Preserved copy: '
                '[https://web.archive.org/web/2019/https://forum.starwarsccg.org/viewtopic.php?p=1245707 IA]</ref>')
        self.assertEqual(L.add_preserved_copy(text, [("p", "1245707")], CAP_SNAP, SNAP), (text, 0))

    def test_line_outside_ref_and_placeholder(self):
        text = ("|source=[https://forum.starwarsccg.org/viewtopic.php?p=1245707 Forum post] | next\n"
                "* [https://forum.starwarsccg.org/viewtopic.php?t=56104 Thread] "
                "(Thread snapshot not yet archived on the Wayback Machine.)\n")
        keys = [("p", "1245707"), ("t", "56104")]
        new, n = L.add_preserved_copy(text, keys, CAP_SNAP, SNAP)
        self.assertEqual(n, 2)
        self.assertIn("Forum post] " + PC + " | next", new)
        self.assertIn("Thread] " + PC + "\n", new)
        self.assertNotIn("not yet archived", new)

    def test_plain_line_appends_at_end(self):
        text = "Posted: [https://forum.starwarsccg.org/viewtopic.php?p=1245707#p1245707 Post], by x, 2016.\nNext"
        new, n = L.add_preserved_copy(text, [("p", "1245707")], CAP_SNAP, SNAP)
        self.assertEqual(new, "Posted: [https://forum.starwarsccg.org/viewtopic.php?p=1245707#p1245707 Post], "
                              "by x, 2016. " + PC + "\nNext")

    def test_thread_key_ignores_post_links(self):
        text = "[https://forum.starwarsccg.org/viewtopic.php?t=56104&p=99 x]"
        self.assertEqual(L.add_preserved_copy(text, [("t", "56104")], CAP_SNAP, SNAP), (text, 0))

    def test_plan_only_verified(self):  # AC4
        done = {IMG: {"status": "verified", "capture": CAP_IMG},
                SNAP: {"status": "verified", "capture": CAP_SNAP},
                "https://swccg.com/snapshots/forum/p5.html": {"status": "unverified", "capture": "https://web.archive.org/web/1/x"},
                "https://swccg.com/wiki/images/b/bc/Z.png": {"status": "failed", "capture": ""}}
        cites = {("p", "1245707"): {"John Anderson"}, ("p", "5"): {"Other"}, ("p", "1271192"): {"2019 NAC"}}
        jobs = L.plan_jobs(done, cites, {SNAP: {"posts": ["1271192"]}})
        self.assertEqual(sorted(j["title"] for j in jobs), ["2019 NAC", "File:Foo bar.jpg", "John Anderson"])


class FakeWiki:
    def __init__(self, pages):
        self.pages = dict(pages)
        self.edits = []

    def page(self, t):
        return (self.pages[t], "2026-01-01T00:00:00Z", "2026-01-02T00:00:00Z") if t in self.pages else (None, None, None)

    def edit(self, t, text, base, start, summary):
        self.pages[t] = text
        self.edits.append(t)
        return "edited"


class Run(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        (self.repo / "ops/wayback").mkdir(parents=True)
        (self.repo / L.DONE).write_text(json.dumps({
            IMG: {"status": "verified", "capture": CAP_IMG},
            SNAP: {"status": "verified", "capture": CAP_SNAP}}))
        p = patch.object(L, "STATE_FILE", self.repo / "state.json")
        p.start()
        self.addCleanup(p.stop)
        q = patch.object(L, "PACE", 0)
        q.start()
        self.addCleanup(q.stop)

    def test_two_runs_edit_once(self):  # AC1-AC3 offline
        w = FakeWiki({"File:Foo bar.jpg": "x\n[[Category:A]]",
                      "John Anderson": "<ref>[https://forum.starwarsccg.org/viewtopic.php?p=1245707 P]</ref>",
                      "Gone": "<ref>[https://forum.starwarsccg.org/viewtopic.php?p=1245707 P]</ref>"})
        cites = {("p", "1245707"): {"John Anderson", "Missing page"}}
        c1 = L.link(self.repo, wiki=w, cites=cites)
        self.assertEqual((c1["edited"], c1["missing"]), (2, 1))
        self.assertIn(PC, w.pages["John Anderson"])
        c2 = L.link(self.repo, wiki=w, cites=cites)
        self.assertEqual(c2["todo"], 0)
        self.assertEqual(len(w.edits), 2)

    def test_dry_run_no_edit_no_state(self):
        w = FakeWiki({"File:Foo bar.jpg": "x"})
        c = L.link(self.repo, wiki=w, cites={}, dry_run=True)
        self.assertEqual((c["dry"], w.edits), (1, []))
        self.assertFalse((self.repo / "state.json").exists())

    def test_run_safe_without_credentials(self):
        with patch.object(L, "ENV_FILE", self.repo / "nope.env"):
            L.run_safe(self.repo)  # must not raise


if __name__ == "__main__":
    unittest.main()
