#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Mack / Menzel / Nelson."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
DUMP = (
    " dested ",
    "dittos inherit",
    "Handwritten 2010 Xerox Print Form",
)
CHECKS = [
    (
        "2013 World Championship",
        (
            "[[Josh Mack]]",
            "[[Chris Menzel]]",
            "[[Aaron Nelson]]",
            "Watch Your Step",
            "Hunt Down And Destroy The Jedi",
            "Plead My Case To The Senate",
            "2013 Worlds Day 2 Cole Lepine",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Josh Mack LS Watch Your Step",
        (
            "[[Josh Mack]]",
            "Day 2 name box is Mack.",
            "Watch Your Step / This Place Can Be A Little Rough",
            "Wedge Antilles (V)",
            "Infinity",
            "There Is Another",
            "Jabba's Prize",
            "[[File:2013 Worlds Day 2 p62 Josh Mack LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Josh Mack DS Kessel",
        (
            "[[Josh Mack]]",
            "I'll Take The Leader",
            "Spice Mine Administrator",
            "Kessel: Cave",
            "We'll Let Fate-a Decide, Huh?",
            "[[File:2013 Worlds Day 2 p63 Josh Mack DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Chris Menzel LS Plead My Case To The Senate",
        (
            "[[Chris Menzel]]",
            "Plead My Case To The Senate / Sanity And Compassion",
            "StrikeForce (V)",
            "Nocoo!",
            "Panic (V)",
            "Affect Mind (V)",
            "[[File:2013 Worlds Day 2 p65 Chris Menzel LS.png",
        ),
        ("'''Username:'''", "Senator Palpatine"),
    ),
    (
        "2013 Worlds Day 2 Chris Menzel DS Hunt Down And Destroy The Jedi",
        (
            "[[Chris Menzel]]",
            "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe",
            "Grand Admiral Thrawn",
            "Evacuate? (V)",
            "Death Star Sentry (V)",
            "[[File:2013 Worlds Day 2 p64 Chris Menzel DS.png",
        ),
        ("'''Username:'''", "Weapon Of A Sith"),
    ),
    (
        "2013 Worlds Day 2 Aaron Nelson LS Watch Your Step (V)",
        (
            "[[Aaron Nelson]]",
            "'''Username:''' Airdog2003",
            "Watch Your Step (V) / This Place Can Be A Little Rough (V)",
            "Romas 'Lock' Navander",
            "Errant Venture",
            "Evacuation Control (V)",
            "[[File:2013 Worlds Day 2 p66 Aaron Nelson LS.png",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Aaron Nelson DS Kessel",
        (
            "[[Aaron Nelson]]",
            "'''Username:''' Airdog2003",
            "The Emperor (V)",
            "Where Are You Taking This ... Thing?",
            "Death Star Sentry (V)",
            "[[File:2013 Worlds Day 2 p67 Aaron Nelson DS.png",
        ),
        (),
    ),
    (
        "Josh Mack",
        ("2013 Worlds Day 2 Josh Mack LS Watch Your Step",),
        (),
    ),
    (
        "Chris Menzel",
        ("2013 Worlds Day 2 Chris Menzel LS Plead My Case To The Senate",),
        (),
    ),
    (
        "Aaron Nelson",
        ("2013 Worlds Day 2 Aaron Nelson LS Watch Your Step (V)",),
        (),
    ),
]


def fetch(title: str) -> str:
    q = urllib.parse.urlencode(
        {
            "action": "parse",
            "page": title,
            "prop": "wikitext",
            "format": "json",
            "disablelimitreport": "1",
        }
    )
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data.get("parse", {}).get("wikitext", {}).get("*", "") or ""


def main() -> None:
    fails = 0
    for title, need, forbid in CHECKS:
        text = fetch(title)
        print("PAGE", title, "len", len(text))
        if not text:
            print("  FAIL empty")
            fails += 1
            continue
        for s in DUMP:
            if s in text:
                print("  FAIL dump", repr(s))
                fails += 1
        for s in need:
            if s not in text:
                print("  FAIL missing", repr(s))
                fails += 1
        for s in forbid:
            if s in text:
                print("  FAIL forbidden", repr(s))
                fails += 1
    print("TOTAL", fails)


if __name__ == "__main__":
    main()
