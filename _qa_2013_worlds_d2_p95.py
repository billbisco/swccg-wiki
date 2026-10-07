#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Nicholas Tobin."""
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
    "Typed 2013 Xerox Print Form",
)
CHECKS = [
    (
        "2013 World Championship",
        (
            "[[Nicholas Tobin]]",
            "[[Conrad Simmering]]",
            "Contract Killers",
            "Plead My Case To The Senate",
            "2013 Worlds Day 2 Nicholas Tobin",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Nicholas Tobin LS Plead My Case To The Senate",
        (
            "[[Nicholas Tobin]]",
            "Name as written on the Day 2 sheet.",
            "Plead My Case To The Senate / Sanity And Compassion",
            "NOOOOOOOOOOOO!",
            "Sai'torr Kal Fas",
            "[[File:2013 Worlds Day 2 p96 Nicholas Tobin LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Nicholas Tobin DS Contract Killers",
        (
            "[[Nicholas Tobin]]",
            "Contract Killers / Feared Throughout The Galaxy",
            "[[Luuke]]",
            "Gift Of The Master",
            "We'll Let Fate-a Decide, Huh?",
            "[[File:2013 Worlds Day 2 p95 Nicholas Tobin DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "Nicholas Tobin",
        (
            "2013 World Championship",
            "2014 World Championship",
            "Contract Killers",
            "Plead My Case To The Senate",
        ),
        ("#REDIRECT",),
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
