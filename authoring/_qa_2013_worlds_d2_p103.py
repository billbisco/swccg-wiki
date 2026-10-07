#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Nathan Wall / Nathan Way."""
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
            "[[Nathan Wall]]",
            "[[Nathan Way]]",
            "[[Micah Wall]]",
            "2013 Worlds Day 2 Nathan Wall",
            "2013 Worlds Day 2 Nathan Way",
            "The Hyperdrive Generator's Gone",
            "Contract Killers",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Nathan Wall LS The Hyperdrive Generator's Gone",
        (
            "[[Nathan Wall]]",
            "The Hyperdrive Generator's Gone / We'll Need A New One",
            "Aayla Secura",
            "Shoo! Shoo!",
            "[[File:2013 Worlds Day 2 p103 Nathan Wall LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Nathan Way DS Contract Killers",
        (
            "[[Nathan Way]]",
            "Day 2 Dark is the same as the Day 1 Contract Killers list.",
            "Contract Killers / Feared Throughout The Galaxy",
            "[[File:2013 Worlds Day 2 p104 Nathan Way DS.png",
            "[[File:2013 Worlds Day 1 p12 Nathan Way DS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "Nathan Wall",
        (
            "2013 World Championship",
            "The Hyperdrive Generator's Gone",
        ),
        ("#REDIRECT",),
    ),
    (
        "Nathan Way",
        (
            "2013 World Championship",
            "Contract Killers",
            "Day 2",
            "Day 1",
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
