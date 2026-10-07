#!/usr/bin/env python3
"""2013 World Championship Day 3: Emil Wallin Same as Yesterday with substitutions."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from transcribe_2013_worlds_wallin import (  # noqa: E402
    DS_ADD as D2_DS_ADD,
    DS_CARDS as D2_DS_CARDS,
    DS_SHIELDS as D2_DS_SHIELDS,
    DS_START as D2_DS_START,
    LS_ADD as D2_LS_ADD,
    LS_CARDS as D2_LS_CARDS,
    LS_SHIELDS as D2_LS_SHIELDS,
    LS_START as D2_LS_START,
    n,
)

PLAYER = "Emil Wallin"
USERNAME = "Darth-Link"
STAGE = "Day 3"
PDF = "2013 Worlds Day 3.pdf"
LS_PAGE = 15
DS_PAGE = 16
LS_SCAN = "2013 Worlds Day 3 p15 Emil Wallin LS.png"
DS_SCAN = "2013 Worlds Day 3 p16 Emil Wallin DS.png"
LS_EXTRA_SCANS = [
    (
        "2013 Worlds Day 2 p107 Emil Wallin LS.png",
        "Page 107 of [[:File:2013 Worlds Day 2.pdf]].",
    )
]
DS_EXTRA_SCANS = [
    (
        "2013 Worlds Day 2 p108 Emil Wallin DS.png",
        "Page 108 of [[:File:2013 Worlds Day 2.pdf]].",
    )
]
LS_PUBLIC_NOTE = (
    "Day 3 Light is the same as the Day 2 There Is Good In Him list, with the "
    "substitutions written on the Day 3 sheet."
)
DS_PUBLIC_NOTE = (
    "Day 3 Dark is the same as the Day 2 Imperial Entanglements list, with the "
    "substitutions written on the Day 3 sheet."
)
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Emil Wallin. Username Darth-Link. "
    "LIGHT checked. Deck title Return of the Jedi TIGH. Event Worlds Day 3, "
    "dated 08/11/13. Same As Yesterday with In/Out substitutions. "
    "Do not rewrite the Day 2 Emil Wallin leftover. "
    "OUT Mace Windu (V), Weapon Levitation, one General Solo (V), On The Edge, "
    "You've Got A Lot Of Guts Coming Here, Fallen Portal, one Master Qui-Gon (V), "
    "Nabrun Leids, one Chewie, Enraged, Lando Calrissian, Scoundrel without (V). "
    "IN Republic Gunship Wing, Armed And Dangerous / KDH dested "
    "Armed And Dangerous & Krayt Dragon Howl, Han With Heavy Blaster Pistol, "
    "Antilles Maneuver & Rebel Reinforcements, a second Control & Tunnel Vision, "
    "Out Of Commission & TT dested Out Of Commission & Transmission Terminated, "
    "Corran Horn, Odin Nesloor & First Aid, Chewbacca, Protector, "
    "Away Put Your Weapon (V). "
    "Shield IN Wise Advice. Additional OUT He Can Go About His Business (V). "
    "Struck lines 10-12 are the IN cards rewritten on 45-46. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Emil Wallin. Username Darth.Link "
    "dested Darth-Link. LIGHT/DARK boxes empty. Deck title Imperial Entanglements. "
    "Event Worlds, dated 08/10/13 on the Day 3 PDF page. Same As Yesterday with "
    "In/Out substitutions. Do not rewrite the Day 2 Emil Wallin leftover. "
    "Day 2 sheet line 58 is Onyx 2 (V); the live Day 2 transcribe listed Close Call x3. "
    "Day 3 baseline uses the Day 2 sheet (Onyx 2 (V) and Close Call (V) x2). "
    "OUT Onyx 2 (V), one Close Call (V), Grand Moff Tarkin (V). "
    "IN Cold Feet (V), Something Special Planned For Them (V), Limited Resources. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def _d3_ls():
    out = []
    for qty, name, v in D2_LS_CARDS:
        if name == "Mace Windu" and v:
            continue
        if name == "Weapon Levitation":
            continue
        if name == "General Solo":
            out.append((1, name, v))
            continue
        if name == "On The Edge":
            continue
        if name == "You've Got A Lot Of Guts Coming Here":
            continue
        if name == "Fallen Portal":
            continue
        if name == "Master Qui-Gon":
            out.append((1, name, v))
            continue
        if name == "Nabrun Leids":
            continue
        if name == "Chewie, Enraged":
            out.append((1, name, v))
            continue
        if name == "Lando Calrissian, Scoundrel" and not v:
            continue
        if name == "Control & Tunnel Vision":
            out.append((2, name, v))
            continue
        out.append((qty, name, v))
    out.extend(
        [
            n("Republic Gunship Wing"),
            n("Armed And Dangerous & Krayt Dragon Howl"),
            n("Han With Heavy Blaster Pistol"),
            n("Antilles Maneuver & Rebel Reinforcements"),
            n("Out Of Commission & Transmission Terminated"),
            n("Corran Horn"),
            n("Odin Nesloor & First Aid"),
            n("Chewbacca, Protector"),
            n("Away Put Your Weapon", True),
        ]
    )
    return out


def _d3_ls_sh():
    out = []
    for qty, name, v in D2_LS_SHIELDS:
        if name == "He Can Go About His Business":
            continue
        out.append((qty, name, v))
    out.append(n("Wise Advice"))
    return out


def _d3_ds():
    out = []
    for qty, name, v in D2_DS_CARDS:
        if name == "Grand Moff Tarkin":
            continue
        if name == "Close Call":
            # Day 2 sheet has Close Call x2 + Onyx 2 (V). Live Day 2 listed Close Call x3.
            qty = 2
        out.append((qty, name, v))
    out.append(n("Onyx 2", True))
    filtered = []
    for qty, name, v in out:
        if name == "Onyx 2":
            continue
        if name == "Close Call":
            filtered.append((1, name, v))
            continue
        filtered.append((qty, name, v))
    filtered.extend(
        [
            n("Cold Feet", True),
            n("Something Special Planned For Them", True),
            n("Limited Resources"),
        ]
    )
    return filtered


LS_START = D2_LS_START
LS_CARDS = _d3_ls()
LS_SHIELDS = _d3_ls_sh()
LS_ADD = list(D2_LS_ADD)

DS_START = D2_DS_START
DS_CARDS = _d3_ds()
DS_SHIELDS = list(D2_DS_SHIELDS)
DS_ADD = list(D2_DS_ADD)
