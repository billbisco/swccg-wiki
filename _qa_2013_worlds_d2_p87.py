#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Steve Skilton."""
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
            "[[Steve Skilton]]",
            "[[Greg Shaw]]",
            "Wookiee Slaving Operation",
            "You Can Either Profit By This...",
            "2013 Worlds Day 2 Steve Skilton",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Steve Skilton LS You Can Either Profit By This...",
        (
            "[[Steve Skilton]]",
            "Name box on the Day 2 sheet is the Username stevetotheizzo.",
            "You Can Either Profit By This... / Or Be Destroyed",
            "[[Stop! Stop!]]",
            "They're Still Coming Through!",
            "Swing-And-A-Miss",
            "Son Of Skywalker",
            "[[File:2013 Worlds Day 2 p88 Steve Skilton LS.png",
        ),
        ("'''Username:'''", "Stop! Stop! (V)"),
    ),
    (
        "2013 Worlds Day 2 Steve Skilton DS Wookiee Slaving Operation",
        (
            "[[Steve Skilton]]",
            "Wookiee Slaving Operation / Indentured To The Empire",
            "Nal Hutta",
            "Ability, Ability, Ability",
            "Jango Fett, The Assassin",
            "Bossk With Mortar Gun (V)",
            "Dengar With Blaster Carbine (V)",
            "[[Reegesk]]",
            "Look Sir, Droids",
            "[[File:2013 Worlds Day 2 p87 Steve Skilton DS.png",
        ),
        ("'''Username:'''", "Ree-Yees"),
    ),
    (
        "Steve Skilton",
        (
            "2013 World Championship",
            "Wookiee Slaving Operation",
            "You Can Either Profit By This...",
            "Contract Killers",
            "We'll Handle This",
            "Hunt Down And Destroy The Jedi",
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
        if "Tom Haid" in title or title.startswith("2013 Worlds Day 2 Steve Skilton"):
            if "Tom Haid" in text:
                print("  FAIL forbidden Tom Haid dest")
                fails += 1
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
