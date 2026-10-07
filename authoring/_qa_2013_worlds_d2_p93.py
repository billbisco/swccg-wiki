#!/usr/bin/env python3
"""Live QA: 2013 Worlds Day 2 leftover Conrad Simmering."""
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
            "[[Conrad Simmering]]",
            "[[Matt Sokol]]",
            "Spice Mine Operations",
            "Communing",
            "2013 Worlds Day 2 Conrad Simmering",
        ),
        (),
    ),
    (
        "2013 Worlds Day 2 Conrad Simmering LS Communing",
        (
            "[[Conrad Simmering]]",
            "Name as written on the Day 2 sheet.",
            "Communing",
            "Inconsequential Barriers",
            "Out Of Commission & Transmission Terminated",
            "[[File:2013 Worlds Day 2 p93 Conrad Simmering LS.png",
        ),
        ("'''Username:'''",),
    ),
    (
        "2013 Worlds Day 2 Conrad Simmering DS Spice Mine Operations",
        (
            "[[Conrad Simmering]]",
            "Spice Mine Operations",
            "[[U-2PO]]",
            "OS-72-10",
            "Black Leader",
            "He Is Not Ready",
            "Where Are You Taking This ... Thing?",
            "[[File:2013 Worlds Day 2 p94 Conrad Simmering DS.png",
        ),
        ("'''Username:'''", "Unknown"),
    ),
    (
        "Conrad Simmering",
        (
            "2013 World Championship",
            "Spice Mine Operations",
            "Communing",
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
