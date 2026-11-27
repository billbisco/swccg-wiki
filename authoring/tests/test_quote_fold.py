"""swccg-guild/work#1382 (Bill, Option B): card game text and lore keep apostrophes and quote marks exactly
as printed, curly (’ ‘ “ ”) or straight. Tools that compare wiki text with GEMP, swccg-card-json or other
versions treat the styles as equal and never rewrite the page's marks; style_lint reports straight marks
(information only) unless the page records |straight_quotes=."""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import wiki_cardlink as cl  # noqa: E402
import style_lint as L  # noqa: E402

_spec = importlib.util.spec_from_file_location("errgen", HERE.parents[1] / "tools" / "errgen" / "errgen.py")
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)


class FoldQuotes(unittest.TestCase):
    def test_fold(self):
        self.assertEqual(cl.fold_quotes("Lars’ ‘mouse’ “Hi”"), "Lars' 'mouse' \"Hi\"")
        self.assertEqual(cl.fold_quotes(None), "")
        self.assertEqual(E.fold_quotes("Lars’ “x”"), "Lars' \"x\"")

    def test_lookup_key_matches_either_style(self):
        self.assertEqual(cl.lookup_key("•Jabba’s Sail Barge"), cl.lookup_key("Jabba's Sail Barge"))

    def test_index_matches_either_style(self):
        idx = {}
        cl._index_card(idx, {"side": "Dark", "front": {"title": "•Jabba’s Sail Barge", "imageUrl": "x/sailbarge.gif"}})
        self.assertIn(("Dark", "jabba's sail barge"), idx)

    def test_gemp_lookup_either_style(self):
        import gemp_importable as gi
        import gemp_map as gm
        self.assertEqual(gm._norm("Jabba‘s “Prize”"), gm._norm("Jabba's \"Prize\""))
        pool = [{"cardId": "6_99", "title": "Jabba's Prize", "side": "DARK", "cardCategory": "EFFECT"}]
        old = gi.load_cards, gi.load_overrides
        gi.load_cards, gi.load_overrides = (lambda: pool), (lambda: {})
        try:
            self.assertEqual(gi.lookup("Jabba’s Prize", "Dark", None)["cardId"], "6_99")
        finally:
            gi.load_cards, gi.load_overrides = old


class ErrgenQuotes(unittest.TestCase):
    def test_plain_folds(self):
        self.assertEqual(E.plain("Lars’ Moisture Farm"), E.plain("Lars' Moisture Farm"))

    def test_no_highlight_for_quote_style(self):
        w, n, dl = E.diff_hl("Deploys free at Lars' Moisture Farm.", "Deploys free at Lars’ Moisture Farm.")
        self.assertEqual(n, 0)
        self.assertFalse(dl)
        self.assertEqual(w, "Deploys free at Lars’ Moisture Farm.")  # the page's own marks are kept

    def test_real_change_still_highlighted_quote_kept(self):
        w, n, _ = E.diff_hl("Opponent's ‘mouse’ droids.", "Opponent’s 'mouse' Jedi.")
        self.assertEqual(n, 1)
        self.assertEqual(w, "Opponent’s 'mouse' {{Errata hl|1=Jedi}}.")
        w, n, _ = E.diff_hl('Cancels "Hit" here.', "Cancels “Hit” here.")
        self.assertEqual((w, n), ("Cancels “Hit” here.", 0))

    def test_deleted_hl_ignores_quote_style(self):
        w, n = E.deleted_hl("Lars’ farm, now.", "Lars' farm.")
        self.assertEqual(n, 1)
        self.assertIn("Lars’ farm", w)

    def test_quote_swaps(self):
        self.assertEqual(E.quote_swaps("Lars' “x”", "Lars’ “x”"), [("'", "’")])
        self.assertEqual(E.quote_swaps("Lars' farm", "Lars' farm"), [])
        # a real wording change elsewhere neither hides nor fakes a swap
        self.assertEqual(E.quote_swaps("Lars' farm. Power +2.", "Lars’ farm. Power +3."), [("'", "’")])
        self.assertEqual(E.quote_swaps("Power +2.", "Han's power +2."), [])

    def test_straight_quote_fields(self):
        self.assertEqual(E.straight_quote_fields("yes"), {"game_text", "lore"})
        self.assertEqual(E.straight_quote_fields("lore"), {"lore"})
        self.assertEqual(E.straight_quote_fields("game_text, lore <!-- slip -->"), {"game_text", "lore"})
        self.assertEqual(E.straight_quote_fields(None), set())
        self.assertEqual(L.straight_quote_fields("game_text"), {"game_text"})

    def test_quote_verified(self):
        sw = [("'", "’")]
        self.assertFalse(E.quote_verified("game_text", {"__sq": set()}, {"__sq": set()}, sw))
        self.assertTrue(E.quote_verified("game_text", {"__sq": {"game_text"}}, {"__sq": set()}, sw))
        self.assertTrue(E.quote_verified("lore", {"__sq": set()}, {"__sq": set()}, [("‘", "’")]))

    def test_quote_note(self):
        self.assertEqual(E.quote_note("Game text", "Original", "Errata", [("'", "’")]),
                         "Game text: Errata prints ’ where Original prints '; quote style only, not a text change.")


CARD = """{{Card
|title=''Executor''<nowiki/>'s Bridge
|lore=Vader's flagship. <span style="color:red">red</span> <ref name="a">Bill's note</ref>
|game_text=Deploy on ''Executor''. Your '''Admirals''' are power +1.
|errata_history=* '''Original''' (this page)
}}"""


class StyleLintQuotes(unittest.TestCase):
    def test_card_params(self):
        p = L.card_params(CARD)
        self.assertEqual(p["game_text"], "Deploy on ''Executor''. Your '''Admirals''' are power +1.")
        self.assertIn("<ref", p["lore"])

    def test_markup_is_not_a_straight_mark(self):
        info = L.quote_info(CARD, "Executor: Bridge")
        self.assertEqual(len(info), 1)  # lore only: game_text has only italic/bold marks
        self.assertTrue(info[0].startswith("QUOTES   lore: 1 straight mark(s) (1 ')"))
        self.assertNotIn("Bill", info[0])  # <ref> text is not card text

    def test_curly_passes(self):
        text = CARD.replace("Vader's", "Vader’s")
        self.assertEqual(L.quote_info(text, "Executor: Bridge"), [])

    def test_straight_quotes_parameter_skips(self):
        self.assertEqual(L.quote_info(CARD.replace("|lore=", "|straight_quotes=lore\n|lore="), "X"), [])
        self.assertEqual(L.quote_info(CARD.replace("|lore=", "|straight_quotes=yes\n|lore="), "X"), [])
        self.assertEqual(len(L.quote_info(CARD.replace("|lore=", "|straight_quotes=game_text\n|lore="), "X")), 1)

    def test_double_quotes_and_entities(self):
        text = '{{Card\n|game_text=Cancels &quot;Hit&quot; and "Run".\n}}'
        info = L.quote_info(text, "X")
        self.assertEqual(len(info), 1)
        self.assertIn('4 straight mark(s) (4 ")', info[0])

    def test_not_a_card_or_template(self):
        self.assertEqual(L.quote_info("Han's page. ''Executor''", "Han"), [])
        self.assertEqual(L.quote_info(CARD, "Template:Card/doc"), [])

    def test_information_only(self):
        flags, _ = L.lint(CARD, "Executor: Bridge")
        self.assertFalse(any(f.startswith("QUOTES") for f in flags))
        with tempfile.NamedTemporaryFile("w", suffix=".wiki", delete=False, encoding="utf-8") as fh:
            fh.write(CARD)
        r = subprocess.run([sys.executable, str(HERE.parent / "style_lint.py"), fh.name], capture_output=True, text=True)
        Path(fh.name).unlink()
        self.assertIn("QUOTES   lore:", r.stdout)
        self.assertIn("0 flag(s)", r.stdout)
        self.assertEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
