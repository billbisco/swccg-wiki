#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Jake Nelson / Wieland / Paragano."""
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
            "[[Jake Nelson]]",
            "[[Mitch Wieland]]",
            "[[Matt Paragano]]",
            "Quiet Mining Colony",
            "No Money, No Parts, No Deal!",
            "Contract Killers",
            "The Hyperdrive Generator's Gone",
            "2013 Worlds Day 2 Aaron Nelson",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Jake Nelson LS Quiet Mining Colony",
        (
            "[[Jake Nelson]]",
            "Quiet Mining Colony / Independent Operation",
            "Ellorrs Madak (V)",
            "What're You Tryin' To Push On Us?",
            "Projection Of A Skywalker",
            "Uutik",
            "[[File:2013 Worlds Day 2 p69 Jake Nelson LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Jake Nelson DS No Money, No Parts, No Deal!",
        (
            "[[Jake Nelson]]",
            "No Money, No Parts, No Deal! / You're A Slave?",
            "J'Quille (V)",
            "P-59",
            "Gravel Storm",
            "Dr. Evazan",
            "Garindan",
            "First Strike",
            "[[File:2013 Worlds Day 2 p68 Jake Nelson DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Mitch Wieland LS Quiet Mining Colony",
        (
            "[[Mitch Wieland]]",
            "Quiet Mining Colony / Independent Operation",
            "Rug Hug (V)",
            "Jabba's Prize",
            "He Can Go About His Business",
            "[[File:2013 Worlds Day 2 p70 Mitch Wieland LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Mitch Wieland DS No Money, No Parts, No Deal!",
        (
            "[[Mitch Wieland]]",
            "No Money, No Parts, No Deal! / You're A Slave?",
            "IG-88 (V)",
            "The Mandalorian",
            "Lord Sidious",
            "Your Ship?",
            "We'll Let Fate-a Decide, Huh?",
            "[[File:2013 Worlds Day 2 p71 Mitch Wieland DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Matt Paragano LS The Hyperdrive Generator's Gone",
        (
            "[[Matt Paragano]]",
            "'''Username:''' GunganStyle",
            "The Hyperdrive Generator's Gone / We'll Need A New One",
            "Rycar Ryjerd (V)",
            "Credits Will Do Fine",
            "Elegant Lightsaber",
            "[[File:2013 Worlds Day 2 p73 Matt Paragano LS.png",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Matt Paragano DS Contract Killers",
        (
            "[[Matt Paragano]]",
            "'''Username:''' GunganStyle",
            "Contract Killers / Feared Throughout The Galaxy",
            "Coruscant: Sub City Lair",
            "Stop Motion (V)",
            "Lana Dobreed",
            "Inaccurate?",
            "Boba Fett, Prepared Hunter",
            "[[File:2013 Worlds Day 2 p72 Matt Paragano DS.png",
        ),
        (),
    ),
    (
        "Jake Nelson",
        ("2013 World Championship", "Quiet Mining Colony"),
        (),
    ),
    (
        "Mitch Wieland",
        ("2013 World Championship", "Quiet Mining Colony"),
        (),
    ),
    (
        "Matt Paragano",
        ("2013 World Championship", "Contract Killers"),
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
