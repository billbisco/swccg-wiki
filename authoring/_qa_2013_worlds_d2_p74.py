#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Pistone / Drew Powers / Mike Richards."""
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
            "[[Pistone]]",
            "[[Drew Powers]]",
            "[[Mike Richards]]",
            "Watch Your Step (V)",
            "Imperial Occupation (V)",
            "Rescue The Princess",
            "Agents Of Black Sun",
            "Quiet Mining Colony",
            "Hunt Down And Destroy The Jedi (V)",
            "2013 Worlds Day 2 Matt Paragano",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Pistone LS Watch Your Step (V)",
        (
            "[[Pistone]]",
            "Name as written on the Day 2 sheet.",
            "Watch Your Step (V) / This Place Can Be A Little Rough (V)",
            "Captain Han Solo",
            "Chewie, Enraged",
            "Palejo Reshad",
            "Corellian Slip",
            "Jabba's Prize",
            "[[File:2013 Worlds Day 2 p74 Pistone LS.png",
        ),
        ("'''Username:'''", "Mike Pistone"),
    ),
    (
        "2013 Worlds Day 2 Pistone DS Imperial Occupation (V)",
        (
            "[[Pistone]]",
            "Imperial Occupation (V) / Imperial Control (V)",
            "We're In Attack Position Now",
            "Maarek Stele, The Emperor's Reach",
            "Black Leader",
            "Hoth: Ice Plains (5th Marker)",
            "You May Start Your Landing",
            "[[File:2013 Worlds Day 2 p75 Pistone DS.png",
        ),
        ("'''Username:'''", "Hunt Down And Destroy The Jedi", "Mike Pistone"),
    ),
    (
        "2013 Worlds Day 2 Drew Powers LS Rescue The Princess",
        (
            "[[Drew Powers]]",
            "Day 2 Light is the same as the Day 1 Rescue The Princess list",
            "Rescue The Princess / Sometimes I Amaze Even Myself",
            "[[Clutch]]",
            "Smoke Screen",
            "[[File:2013 Worlds Day 2 p77 Drew Powers LS.png",
            "[[File:2013 Worlds Day 1 p09 Drew Powers LS.png",
        ),
        ("'''Username:'''", "Houjix"),
    ),
    (
        "2013 Worlds Day 2 Drew Powers DS Agents Of Black Sun",
        (
            "[[Drew Powers]]",
            "Day 2 Dark is the same as the Day 1 Agents Of Black Sun list.",
            "Agents Of Black Sun / Vengeance Of The Dark Prince",
            "Start Your Engines",
            "[[File:2013 Worlds Day 2 p76 Drew Powers DS.png",
            "[[File:2013 Worlds Day 1 p10 Drew Powers DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Mike Richards LS Quiet Mining Colony",
        (
            "[[Mike Richards]]",
            "'''Username:''' m007agent",
            "Quiet Mining Colony / Independent Operation",
            "Beldon's Eye",
            "The Bith Shuffle & Desperate Reach",
            "Tatooine: Cantina",
            "Pucumir Thryss",
            "Artoo, Brave Little Droid",
            "[[File:2013 Worlds Day 2 p81 Mike Richards LS.png",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Mike Richards DS Hunt Down And Destroy The Jedi (V)",
        (
            "[[Mike Richards]]",
            "'''Username:''' m007agent",
            "Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V)",
            "Galen, Secret Apprentice (V)",
            "Juno Eclipse, Black Leader",
            "Asoca (V)",
            "Drop!",
            "[[File:2013 Worlds Day 2 p80 Mike Richards DS.png",
        ),
        (),
    ),
    (
        "Pistone",
        ("2013 World Championship", "Imperial Occupation (V)", "Watch Your Step (V)"),
        ("#REDIRECT",),
    ),
    (
        "Drew Powers",
        ("2013 World Championship", "Rescue The Princess", "Agents Of Black Sun"),
        (),
    ),
    (
        "Mike Richards",
        ("2013 World Championship", "Quiet Mining Colony"),
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
