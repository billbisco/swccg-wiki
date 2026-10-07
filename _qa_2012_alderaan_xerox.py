#!/usr/bin/env python3
"""Live QA for 2012 Alderaan Regionals leftover Xerox dests.

python _qa_2012_alderaan_xerox.py --delta   # last pair + hub
python _qa_2012_alderaan_xerox.py --full    # every CHECK (default)
"""
from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    (
        "2012 Alderaan Regionals Clayton Atkin LS Hidden Base (V)",
        ["Hidden Base", "Yavin 4", "Clayton Atkin"],
    ),
    (
        "2012 Alderaan Regionals Clayton Atkin DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense", "Clayton Atkin"],
    ),
    (
        "2012 Alderaan Regionals Anthony Massung LS Watch Your Step (V)",
        ["Watch Your Step", "Cantina", "Anthony Massung"],
    ),
    (
        "2012 Alderaan Regionals Anthony Massung DS A Stunning Move",
        ["A Stunning Move", "Knowledge And Defense", "Anthony Massung"],
    ),
    (
        "2012 Alderaan Regionals Chris Schoenthal LS Infiltration",
        ["Infiltration", "Nar Shaddaa", "Chris Schoenthal"],
    ),
    (
        "2012 Alderaan Regionals Chris Schoenthal DS Kessel",
        ["Kessel", "Knowledge And Defense", "Chris Schoenthal"],
    ),
    (
        "2012 Alderaan Regionals Bill Kafer LS Infiltration",
        ["Infiltration", "Nar Shaddaa", "Bill Kafer"],
    ),
    (
        "2012 Alderaan Regionals Bill Kafer DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Knowledge And Defense", "Bill Kafer"],
    ),
    (
        "2012 Alderaan Regionals Ganden Yanaga LS We Have A Plan",
        ["We Have A Plan", "Naboo", "Ganden Yanaga"],
    ),
    (
        "2012 Alderaan Regionals Ganden Yanaga DS Contract Killers",
        ["Contract Killers", "Knowledge And Defense", "Ganden Yanaga"],
    ),
    (
        "2012 Alderaan Regionals",
        ["Clayton Atkin", "Anthony Massung", "Chris Schoenthal", "Bill Kafer", "Ganden Yanaga", "7 July 2012"],
    ),
]


def parse(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "parse",
            "page": title,
            "prop": "text|revid|displaytitle",
            "format": "json",
            "disablelimitreport": 1,
        }
    )
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def flagged(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "query",
            "titles": title,
            "prop": "info|flagged",
            "format": "json",
        }
    )
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    pages = data.get("query", {}).get("pages", {})
    return next(iter(pages.values()))


def select_checks(delta: bool) -> list:
    if not delta:
        return CHECKS
    hub = [c for c in CHECKS if c[0] == "2012 Alderaan Regionals"]
    decks = [c for c in CHECKS if c[0] != "2012 Alderaan Regionals"]
    return decks[-2:] + hub


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--delta", action="store_true", help="last pair + hub")
    ap.add_argument("--full", action="store_true", help="every CHECK (default)")
    args = ap.parse_args()
    checks = select_checks(args.delta and not args.full)
    fail = 0
    for title, needles in checks:
        data = parse(title)
        if "error" in data:
            print("FAIL", title, data["error"])
            fail += 1
            continue
        html = data["parse"]["text"]["*"]
        missing = [n for n in needles if n not in html]
        fl = flagged(title)
        latest = fl.get("lastrevid")
        stable = (fl.get("flagged") or {}).get("stable_revid")
        fr = "OK" if latest and stable and int(latest) == int(stable) else f"latest={latest} stable={stable}"
        if missing or fr != "OK":
            print("FAIL", title, "missing", missing, "fr", fr)
            fail += 1
        else:
            print("OK", title, "fr", fr)
    mode = "delta" if args.delta and not args.full else "full"
    print("TOTAL", fail, "n", len(checks), mode)


if __name__ == "__main__":
    main()
