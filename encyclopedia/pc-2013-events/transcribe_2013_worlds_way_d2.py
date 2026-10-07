#!/usr/bin/env python3
"""2013 World Championship Day 2: Nathan Way Xerox Assassins Same as Yesterday."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from transcribe_2013_worlds_way import (  # noqa: E402
    DS_ADD as D1_DS_ADD,
    DS_CARDS as D1_DS_CARDS,
    DS_SHIELDS as D1_DS_SHIELDS,
    DS_START as D1_DS_START,
    n,
)

PLAYER = "Nathan Way"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
DS_PAGE = 104
DS_SCAN = "2013 Worlds Day 2 p104 Nathan Way DS.png"
DS_EXTRA_SCANS = [
    (
        "2013 Worlds Day 1 p12 Nathan Way DS.png",
        "Page 12 of [[:File:2013 Worlds Day 1.pdf]].",
    )
]
DS_PUBLIC_NOTE = (
    "Day 2 Dark is the same as the Day 1 Contract Killers list."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Nathan Way. Username blank. DARK. "
    "Deck title Assassins. Dated 8/10/13. Same as Yesterday. "
    "Copied from the Day 1 Contract Killers 60. Do not rewrite Day 1. "
    "Do not dest as Nathan Wall."
)
DS_START = D1_DS_START
DS_CARDS = list(D1_DS_CARDS)
DS_SHIELDS = list(D1_DS_SHIELDS)
DS_ADD = list(D1_DS_ADD)
LS_CARDS = []
LS_SHIELDS = []
LS_ADD = []
