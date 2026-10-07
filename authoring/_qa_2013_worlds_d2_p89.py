#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover RSmith."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
DUMP = (
    " dested ",
    "dittos inherit",
    "Handwritten 2010 Xerox Print Form",
    "Handwritten 2013 Xerox Print Form",
)
CHECKS = [
    (
        "2013 World Championship",
        (
            "[[RSmith]]",
            "[[Reid Smith]]",
            "[[Steve Skilton]]",
            "2013 Worlds Day 2 RSmith DS Kessel",
            "2013 Worlds Day 2 RSmith LS Plead My Case To The Senate",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 RSmith LS Plead My Case To The Senate",
        (
            "[[RSmith]]",
            "Name as written on the Day 2 sheet.",
            "'''Username:''' Conway East",
            "Plead My Case To The Senate / Sanity And Compassion",
            "Jabba's Prize",
            "Do, Or Do Not",
            "Commando Training & K'lor'slug",
            "[[File:2013 Worlds Day 2 p89 RSmith LS.png",
        ),
        ("Reid Smith", "3MW0J8", "Buck Faston"),
    ),
    (
        "2013 Worlds Day 2 RSmith DS Kessel",
        (
            "[[RSmith]]",
            "'''Username:''' Buck Faston",
            "[[Kessel (Dark)|Kessel]]",
            "Black Sun Fleet",
            "Spice Mine Administrator",
            "[[Victory]]",
            "The Mandalorian",
            "Dr. Evazan & Ponda Baba",
            "[[File:2013 Worlds Day 2 p90 RSmith DS.png",
        ),
        ("Reid Smith", "3MW0J8", "Conway East"),
    ),
    (
        "RSmith",
        (
            "2013 World Championship",
            "Kessel",
            "Plead My Case To The Senate",
        ),
        ("#REDIRECT", "Reid Smith"),
    ),
]


def raw(title: str) -> str:
    q = urllib.parse.urlencode(
        {"action": "parse", "page": title, "prop": "wikitext", "format": "json"}
    )
    with urllib.request.urlopen(f"{API}?{q}", timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data.get("parse", {}).get("wikitext", {}).get("*", "") or ""


def main() -> None:
    fails = 0
    for title, need, forbid in CHECKS:
        text = raw(title)
        print("PAGE", title, "len", len(text))
        if not text:
            print("  FAIL empty")
            fails += 1
            continue
        for s in need:
            if s not in text:
                print("  FAIL missing", s)
                fails += 1
        for s in forbid:
            if s in text:
                print("  FAIL forbidden", s)
                fails += 1
        for s in DUMP:
            if s in text:
                print("  FAIL dump", s)
                fails += 1
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
