#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 2: Clayton Atkin Same as Yesterday (copy Day 1)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from transcribe_2013_socal_atkin import (  # noqa: E402
    DS_ADD,
    DS_CARDS,
    DS_SHIELDS,
    DS_START,
    LS_ADD,
    LS_CARDS,
    LS_SHIELDS,
    LS_START,
)

PLAYER = "Clayton Atkin"
USERNAME = "Clayton Atkin"
STAGE = "Day 2"
PDF = "2013 SoCal Grand Prix Day 2.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2013 SoCal Grand Prix Day 2 p01 Clayton Atkin LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 2 p02 Clayton Atkin DS.png"
LS_EXTRA_SCANS = [
    (
        "2013 SoCal Grand Prix Day 1 p07 Clayton Atkin LS.png",
        "Page 7 of [[:File:2013 SoCal Grand Prix Day 1.pdf]].",
    )
]
DS_EXTRA_SCANS = [
    (
        "2013 SoCal Grand Prix Day 1 p08 Clayton Atkin DS.png",
        "Page 8 of [[:File:2013 SoCal Grand Prix Day 1.pdf]].",
    )
]
LS_NOTE = (
    "Day 2 Final Four Light form headed Same as Yesterday (the Day 1 Communing list). "
    "Deck Name Day 1 1/2. Username same as above. The 60 is copied from Day 1 page 7."
)
DS_NOTE = (
    "Day 2 Final Four Dark form headed Same as Yesterday (the Day 1 Hunt Down And Destroy "
    "The Jedi (V) list). Deck Name Day 1 1/2. The 60 is copied from Day 1 page 8."
)
