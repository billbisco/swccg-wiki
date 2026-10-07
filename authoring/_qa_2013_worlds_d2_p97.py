#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Chris Terwilliger (Chris Twigg)."""
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
            "[[Chris Terwilliger]]",
            "[[Nicholas Tobin]]",
            "Imperial Occupation (V)",
            "The Hyperdrive Generator's Gone",
            "2013 Worlds Day 2 Chris Terwilliger",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Chris Terwilliger LS The Hyperdrive Generator's Gone",
        (
            "[[Chris Terwilliger]]",
            "Name box on the Day 2 sheet is Chris Twigg.",
            "The Hyperdrive Generator's Gone / We'll Need A New One",
            "Guardian's Lightsaber",
            "Republic Gunship Wing",
            "[[File:2013 Worlds Day 2 p97 Chris Twigg LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Chris Terwilliger DS Imperial Occupation (V)",
        (
            "[[Chris Terwilliger]]",
            "Imperial Occupation (V) / Imperial Control (V)",
            "Cyclone Walker",
            "Juno Eclipse, Black Leader",
            "Maarek Stele, The Emperor's Reach",
            "[[File:2013 Worlds Day 2 p98 Chris Twigg DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "Chris Terwilliger",
        (
            "2013 World Championship",
            "Chris Twigg",
            "Imperial Occupation (V)",
            "The Hyperdrive Generator's Gone",
        ),
        ("#REDIRECT", "BTwigg"),
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
