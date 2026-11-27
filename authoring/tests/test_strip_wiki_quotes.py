"""swccg-guild/work#1380: card |title=/|model=/|subtype= carry printed italics; readers strip them."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wiki_cardlink import strip_wiki_quotes  # noqa: E402

CASES = {
    "''Executor''": "Executor",
    "''Executor'': Comm Station": "Executor: Comm Station",
    "Boba Fett In ''Slave I''": "Boba Fett In Slave I",
    "''Executor''<nowiki/>'s Bridge": "Executor's Bridge",
    "''Executor'''s Bridge": "Executor's Bridge",
    "''Kom'rk''-Class Fighter/transport": "Kom'rk-Class Fighter/transport",
    "''Intimidator'' & •''Persecutor''": "Intimidator & •Persecutor",
    "'''''Millenium Falcon'''''": "Millenium Falcon",
    "Capital: ''Imperial''-Class Star Destroyer": "Capital: Imperial-Class Star Destroyer",
    "Jabba's Sail Barge": "Jabba's Sail Barge",
    "<nowiki>''</nowiki>x": "''x",
    "[[Starship]]<nowiki> </nowiki>— [[Starfighter]]": "[[Starship]] — [[Starfighter]]",
    "": "",
}


class StripWikiQuotes(unittest.TestCase):
    def test_cases(self):
        for raw, want in CASES.items():
            self.assertEqual(strip_wiki_quotes(raw), want, raw)

    def test_none(self):
        self.assertEqual(strip_wiki_quotes(None), "")


if __name__ == "__main__":
    unittest.main()
