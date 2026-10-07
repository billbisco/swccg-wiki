#!/usr/bin/env python3
"""2013 World Championship Day 2: Drew Powers Same as Day 1 with Light substitutions."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from transcribe_2013_worlds_powers import (  # noqa: E402
    DS_ADD as D1_DS_ADD,
    DS_CARDS as D1_DS_CARDS,
    DS_SHIELDS as D1_DS_SHIELDS,
    DS_START as D1_DS_START,
    LS_ADD as D1_LS_ADD,
    LS_CARDS as D1_LS_CARDS,
    LS_SHIELDS as D1_LS_SHIELDS,
    LS_START as D1_LS_START,
    n,
)

PLAYER = "Drew Powers"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 77
DS_PAGE = 76
LS_SCAN = "2013 Worlds Day 2 p77 Drew Powers LS.png"
DS_SCAN = "2013 Worlds Day 2 p76 Drew Powers DS.png"
LS_EXTRA_SCANS = [
    (
        "2013 Worlds Day 1 p09 Drew Powers LS.png",
        "Page 9 of [[:File:2013 Worlds Day 1.pdf]].",
    )
]
DS_EXTRA_SCANS = [
    (
        "2013 Worlds Day 1 p10 Drew Powers DS.png",
        "Page 10 of [[:File:2013 Worlds Day 1.pdf]].",
    )
]
LS_PUBLIC_NOTE = (
    "Day 2 Light is the same as the Day 1 Rescue The Princess list, with the "
    "substitutions written on the Day 2 sheet."
)
DS_PUBLIC_NOTE = (
    "Day 2 Dark is the same as the Day 1 Agents Of Black Sun list."
)
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Drew Powers. Username blank. LIGHT. "
    "Deck name Same As D1 with substitutions. "
    "Do not rewrite the Day 1 Drew Powers leftover (Username Rebort). "
    "OUT Electromat Collusion dested Collision!; not present on the Day 1 60. "
    "OUT Houjix. IN Smoke Screen. IN Clutch. "
    "The Day 2 sheet is otherwise a copy of Day 1 page 9."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Drew Powers. Username blank. DARK. "
    "Deck name Same As Day 1. "
    "Do not rewrite the Day 1 Drew Powers leftover. "
    "The 60 is copied from Day 1 page 10."
)


def _d2_rescue():
    out = []
    for qty, name, v in D1_LS_CARDS:
        if name == "Houjix":
            continue
        if name == "Smoke Screen":
            out.append((qty + 1, name, v))
            continue
        out.append((qty, name, v))
    out.append(n("Clutch"))
    return out


LS_START = D1_LS_START
LS_CARDS = _d2_rescue()
LS_SHIELDS = list(D1_LS_SHIELDS)
LS_ADD = list(D1_LS_ADD)

DS_START = D1_DS_START
DS_CARDS = list(D1_DS_CARDS)
DS_SHIELDS = list(D1_DS_SHIELDS)
DS_ADD = list(D1_DS_ADD)
