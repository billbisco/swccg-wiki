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
        r = patch.object(L.IA, "STATE", self.repo / "no-ia-ledger")  # never the real ledger
        r.start()
        self.addCleanup(r.stop)

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


# ---------------------------------------------------------------- #1375 D2: archive.org item copies

SHA = "d329667c2639f150ed60473c5d2e11db9ece605e"
IA_ITEM, IA_NAME = "swccg-wiki-images-0", "00/2007_Kashyyyk_Regionals_Lee_LS.png"
IA_URL = "https://archive.org/download/swccg-wiki-images-0/00/2007_Kashyyyk_Regionals_Lee_LS.png"
IA_TITLE = "File:2007 Kashyyyk Regionals Lee LS.png"


def row(item=IA_ITEM, name=IA_NAME, sha=SHA, verified="2026-11-25T00:48:24Z"):
    r = {"item": item, "name": name, "sha1": sha, "size": 1, "mtime": 1, "put": "2026-11-25T00:13:13Z"}
    if verified:
        r["verified"] = verified
    return r


class IAMapping(unittest.TestCase):
    def test_url_to_ledger_key(self):
        k = L.IA.ledger_key_for_url
        self.assertEqual(k("https://swccg.com/wiki/images/0/00/2007_Kashyyyk_Regionals_Lee_LS.png"),
                         IA_ITEM + "/" + IA_NAME)
        self.assertEqual(k("https://wiki.swccg.com/images/a/ab/Foo_bar.jpg"), "swccg-wiki-images-a/ab/Foo_bar.jpg")
        self.assertEqual(k("https://swccg.com/wiki/images/8/81/Beer_Wars_rules_%28Team_Wales%2C_2019%29.pdf"),
                         "swccg-wiki-images-8/81/Beer_Wars_rules_(Team_Wales,_2019).pdf")
        self.assertEqual(k("https://swccg.com/wiki/images/c/c3/Caf%C3%A9_card.png"), "swccg-wiki-images-c/c3/Café_card.png")
        self.assertEqual(k("https://swccg.com/wiki/images/c/c3/A%20b.png"), "swccg-wiki-images-c/c3/A_b.png")
        self.assertEqual(k("https://swccg.com/wiki/images/archive/f/f6/20261116121319%21Icon-set-Dagobah.png"),
                         "swccg-wiki-images-archive/f/f6/20261116121319!Icon-set-Dagobah.png")
        self.assertEqual(k("https://swccg.com/snapshots/forum/p1245707.html"), "swccg-com-snapshots/forum/p1245707.html")
        self.assertEqual(k("https://swccg.com/snapshots/x/a%20b.pdf"), "swccg-com-snapshots/x/a b.pdf")
        for bad in ("https://swccg.com/wiki/images/thumb/a/ab/Foo.jpg/200px-Foo.jpg",
                    "https://swccg.com/wiki/images/a/bc/Foo.jpg", "https://swccg.com/wiki/images/a/ab/Foo.jpg?x=1",
                    "https://swccg.com/snapshots/../etc/passwd", "https://swccg.com/snapshots/forum/",
                    "https://example.com/wiki/images/a/ab/Foo.jpg", ""):
            self.assertIsNone(k(bad), bad)

    def test_download_url_and_title(self):
        self.assertEqual(L.IA.download_url(IA_ITEM, IA_NAME), IA_URL)
        self.assertEqual(L.IA.download_url("swccg-wiki-images-c", "c3/Café (x) 100%.png"),
                         "https://archive.org/download/swccg-wiki-images-c/c3/Caf%C3%A9%20%28x%29%20100%25.png")
        self.assertEqual(L.ia_title(IA_ITEM, IA_NAME), IA_TITLE)
        self.assertEqual(L.ia_title("swccg-wiki-images-c", "c3/Café_card.png"), "File:Café card.png")
        self.assertIsNone(L.ia_title("swccg-wiki-images-archive", "0/00/20261116121319!X.png"))
        self.assertIsNone(L.ia_title("swccg-com-snapshots", "forum/p1.html"))
        self.assertIsNone(L.ia_title("swccg-wiki-images-0", "10/X.png"))

    def test_plan_only_verified_current(self):
        led = {"a": row(), "b": row(item="swccg-wiki-images-archive", name="0/00/1!X.png"),
               "c": row(item="swccg-com-snapshots", name="forum/p1.html")}
        jobs = L.plan_ia_jobs(led)
        self.assertEqual([(j["title"], j["key"]) for j in jobs], [(IA_TITLE, "ia|%s|%s" % (IA_TITLE, SHA))])

    def test_load_verified_missing_and_filters(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "ledger.json"
            self.assertIsNone(L.IA.load_verified(p))
            p.write_text("{not json")
            self.assertIsNone(L.IA.load_verified(p))
            p.write_text(json.dumps({"k1": row(), "k2": row(verified=None)}))
            self.assertEqual(list(L.IA.load_verified(p)), ["k1"])


class IALine(unittest.TestCase):
    LINE = L.IA_LINE % IA_URL

    def test_line_text(self):
        self.assertEqual(self.LINE, "archive.org copy of this exact original (SHA-1 checked by archive.org): "
                                    "[%s Internet Archive item]." % IA_URL)

    def test_new_section_before_categories_and_idempotent(self):
        new = L.add_ia_line("Desc\n[[Category:Photos]]", IA_ITEM, IA_NAME)
        self.assertIn("== Preservation ==\n" + self.LINE + "\n\n[[Category:Photos]]", new)
        self.assertIsNone(L.add_ia_line(new, IA_ITEM, IA_NAME))

    def test_no_categories_appends_section(self):
        self.assertEqual(L.add_ia_line("Desc\n", IA_ITEM, IA_NAME), "Desc\n\n== Preservation ==\n" + self.LINE + "\n")

    def test_existing_section_keeps_wayback_line(self):
        text = "x\n== Preservation ==\n" + L.ORIGINAL_LINE % CAP_IMG + "\n[[Category:A]]"
        new = L.add_ia_line(text, IA_ITEM, IA_NAME)
        self.assertIn("== Preservation ==\n" + self.LINE + "\n" + L.ORIGINAL_LINE % CAP_IMG, new)
        self.assertEqual(new.count("== Preservation =="), 1)
        # and a later Wayback capture still gets its own line
        self.assertIn(CAP_IMG.replace("20261123010101", "20261201010101"),
                      L.add_original_line(new.replace(CAP_IMG, "x"), CAP_IMG.replace("20261123010101", "20261201010101"), IMG))

    def test_placeholder_replaced(self):
        text = "== Preservation ==\n" + L.PRESERVATION_PENDING + "\n"
        self.assertEqual(L.add_ia_line(text, IA_ITEM, IA_NAME), "== Preservation ==\n" + self.LINE + "\n")

    def test_unencoded_url_counts_as_present(self):
        text = "[https://archive.org/download/swccg-wiki-images-c/c3/Café_card.png x]"
        self.assertIsNone(L.add_ia_line(text, "swccg-wiki-images-c", "c3/Café_card.png"))


class FakeIAWiki(FakeWiki):
    def __init__(self, pages, shas):
        super().__init__(pages)
        self.shas = shas
        self.sha_calls = []
        self.summaries = []

    def sha1s(self, titles):
        self.sha_calls.append(list(titles))
        return {t: self.shas.get(t) for t in titles}

    def edit(self, t, text, base, start, summary):
        self.summaries.append(summary)
        return super().edit(t, text, base, start, summary)


class IARun(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.d = Path(self.tmp.name)
        for obj, attr, val in ((L, "STATE_FILE", self.d / "state" / "linker.json"), (L, "PACE", 0),
                               (L.IA, "STATE", self.d / "ia")):
            p = patch.object(obj, attr, val)
            p.start()
            self.addCleanup(p.stop)
        (self.d / "ia").mkdir()

    def ledger(self, rows):
        (self.d / "ia" / "ledger.json").write_text(json.dumps({r["item"] + "/" + r["name"]: r for r in rows}))

    def summary(self):
        return json.loads((self.d / "state" / "ia-links.json").read_text())

    def test_edit_once_skip_mismatch_and_summary(self):
        other = row(name="00/Other.png", sha="1" * 40)
        self.ledger([row(), other, row(name="00/Gone.png"),
                     row(item="swccg-wiki-images-archive", name="0/00/1!X.png"), row(name="00/Unver.png", verified=None)])
        w = FakeIAWiki({IA_TITLE: "x\n[[Category:A]]", "File:Other.png": "y"},
                       {IA_TITLE: SHA, "File:Other.png": "2" * 40})
        c = L.link_ia(L.load_state(), lambda: w, seconds=60, limit=10)
        self.assertEqual((c["jobs"], c["edited"], c["sha-mismatch"], c["missing"]), (3, 1, 1, 1))
        self.assertEqual(w.edits, [IA_TITLE])
        self.assertEqual(w.summaries, ["#1375: add verified archive.org item copy"])
        self.assertIn(L.IA_LINE % IA_URL, w.pages[IA_TITLE])
        self.assertEqual(w.pages["File:Other.png"], "y")
        s = self.summary()
        self.assertEqual(set(s), {"schema_version", "updated_at", "ia_verified_current", "linked", "todo",
                                  "skipped_sha_mismatch", "last_run_edits"})
        self.assertEqual((s["schema_version"], s["ia_verified_current"], s["linked"], s["todo"],
                          s["skipped_sha_mismatch"], s["last_run_edits"]), (1, 3, 1, 0, 1, 1))
        self.assertEqual(L.load_state()["ia|%s|%s" % (IA_TITLE, SHA)], "edited")
        c2 = L.link_ia(L.load_state(), lambda: w, seconds=60, limit=10)  # second run: nothing to do
        self.assertEqual((c2["todo"], len(w.edits), self.summary()["last_run_edits"]), (0, 1, 0))

    def test_page_already_has_copy(self):
        self.ledger([row()])
        w = FakeIAWiki({IA_TITLE: "== Preservation ==\n[%s IA]" % IA_URL}, {IA_TITLE: SHA})
        c = L.link_ia({}, lambda: w, seconds=60, limit=10)
        self.assertEqual((c["already"], w.edits), (1, []))

    def test_budget_stops_by_edits_and_batches_of_50(self):
        rows = [row(name="00/F%03d.png" % i) for i in range(120)]
        self.ledger(rows)
        titles = ["File:F%03d.png" % i for i in range(120)]
        w = FakeIAWiki({t: "x" for t in titles}, {t: SHA for t in titles})
        c = L.link_ia(L.load_state(), lambda: w, seconds=60, limit=60)
        self.assertEqual((c["edited"], len(w.edits)), (60, 60))
        self.assertEqual([len(b) for b in w.sha_calls], [50, 50])
        self.assertEqual((self.summary()["todo"], self.summary()["linked"]), (60, 60))
        L.link_ia(L.load_state(), lambda: w, seconds=60, limit=60)
        self.assertEqual((len(w.edits), self.summary()["todo"]), (120, 0))

    def test_budget_stops_by_seconds(self):
        self.ledger([row()])
        w = FakeIAWiki({IA_TITLE: "x"}, {IA_TITLE: SHA})
        c = L.link_ia({}, lambda: w, seconds=-1, limit=10)
        self.assertEqual((c["todo"], c["edited"], w.sha_calls), (1, 0, []))

    def test_conflict_retried_next_run(self):
        self.ledger([row()])
        w = FakeIAWiki({IA_TITLE: "x"}, {IA_TITLE: SHA})
        with patch.object(w, "edit", return_value="error:editconflict"):
            L.link_ia(L.load_state(), lambda: w, seconds=60, limit=10)
        self.assertEqual(self.summary()["todo"], 1)
        L.link_ia(L.load_state(), lambda: w, seconds=60, limit=10)
        self.assertEqual((w.edits, self.summary()["linked"]), ([IA_TITLE], 1))

    def test_dry_run_no_edit_no_state(self):
        self.ledger([row()])
        w = FakeIAWiki({IA_TITLE: "x"}, {IA_TITLE: SHA})
        c = L.link_ia({}, lambda: w, seconds=60, limit=10, dry_run=True)
        self.assertEqual((c["dry"], w.edits), (1, []))
        self.assertFalse((self.d / "state").exists())

    def test_missing_ledger_skips(self):
        self.assertEqual(L.link_ia({}, lambda: self.fail("no wiki needed"), seconds=60, limit=10), {})

    def test_link_runs_ia_phase_after_wayback(self):
        repo = self.d / "repo"
        (repo / "ops/wayback").mkdir(parents=True)
        (repo / L.DONE).write_text(json.dumps({IMG: {"status": "verified", "capture": CAP_IMG}}))
        self.ledger([row()])
        w = FakeIAWiki({"File:Foo bar.jpg": "x", IA_TITLE: "y"}, {IA_TITLE: SHA})
        c = L.link(repo, wiki=w, cites={}, ia_limit=5)
        self.assertEqual((c["edited"], c["ia"]["edited"]), (1, 1))
        self.assertEqual(w.summaries, [L.SUMMARY, L.IA_SUMMARY])
        c2 = L.link(repo, wiki=w, cites={})  # wayback has nothing to do; item phase still runs
        self.assertEqual((c2["todo"], c2["ia"]["todo"]), (0, 0))


if __name__ == "__main__":
    unittest.main()
