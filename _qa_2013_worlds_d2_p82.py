#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Shannon hub / Schwartz / Greg Shaw."""
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
            "[[Kevin Shannon]]",
            "[[Schwartz]]",
            "[[Greg Shaw]]",
            "Wookiee Slaving Operation",
            "You Can Either Profit By This...",
            "2013 Worlds Day 2 Mike Richards",
        ),
        ("Matt Schmaltz",),
    ),
    (
        "2013 Worlds Day 2 Schwartz LS You Can Either Profit By This...",
        (
            "[[Schwartz]]",
            "Name as written on the Day 2 sheet.",
            "You Can Either Profit By This... / Or Be Destroyed",
            "Stop! Stop! (V)",
            "Swing-And-A-Miss",
            "Home One",
            "Son Of Skywalker",
            "[[File:2013 Worlds Day 2 p84 Schwartz LS.png",
        ),
        ("'''Username:'''", "Matt Schmaltz", "Tom Haid"),
    ),
    (
        "2013 Worlds Day 2 Schwartz DS Wookiee Slaving Operation",
        (
            "[[Schwartz]]",
            "Wookiee Slaving Operation / Indentured To The Empire",
            "Nal Hutta",
            "Ability, Ability, Ability",
            "Jango Fett, The Assassin",
            "Bossk With Mortar Gun (V)",
            "Dengar With Blaster Carbine",
            "Reegesk (V)",
            "Look Sir, Droids",
            "[[File:2013 Worlds Day 2 p83 Schwartz DS.png",
        ),
        ("'''Username:'''", "Ree-Yees", "Matt Schmaltz", "Tom Haid"),
    ),
    (
        "2013 Worlds Day 2 Greg Shaw LS You Can Either Profit By This...",
        (
            "[[Greg Shaw]]",
            "You Can Either Profit By This... / Or Be Destroyed",
            "Luke Skywalker, Strong In The Force",
            "Lando With Vibro-Ax",
            "R-3PO (Ar-Threepio)",
            "Trooper Utris M'Toc",
            "Artoo-Detoo In Red 5",
            "[[File:2013 Worlds Day 2 p86 Greg Shaw LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Greg Shaw DS Wookiee Slaving Operation",
        (
            "[[Greg Shaw]]",
            "Wookiee Slaving Operation / Indentured To The Empire",
            "Jango Fett, The Assassin",
            "Reegesk (V)",
            "[[File:2013 Worlds Day 2 p85 Greg Shaw DS.png",
        ),
        ("'''Username:'''", "Ree-Yees"),
    ),
    (
        "Schwartz",
        ("2013 World Championship", "Wookiee Slaving Operation", "You Can Either Profit By This..."),
        ("#REDIRECT", "Matt Schmaltz"),
    ),
    (
        "Greg Shaw",
        ("2013 World Championship", "Wookiee Slaving Operation"),
        (),
    ),
    (
        "Kevin Shannon",
        (
            "[[2013 World Championship]] (Day 2)",
            "[[2013 World Championship]] (Day 3)",
        ),
        (),
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
