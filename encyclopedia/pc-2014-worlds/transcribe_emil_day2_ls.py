#!/usr/bin/env python3
"""Day 2 Xerox transcription: Emil Wallin Light only.

Source scan: extract/day2_upright/d2p3_p01.png (Light, Communing Girl Scouts).
2010 form, Worlds Day 2. Username Darth-Link on the sheet.
Skip Emil Dark xerox d2p3_p02 (typed Holotable Day 2 DS already exists).
(V) follows the sheet checkbox. Dittos expanded.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Emil Wallin"
USERNAME = "Darth-Link"
FORM = "xerox_2010"
PDF = "2014 Worlds Day 2 Part 3.pdf"

EMIL_D2_PLAYER = PLAYER
EMIL_D2_USERNAME = USERNAME
EMIL_D2_LS_DECK_NAME = "Communing Girl Scouts"


# --- Light: day2_upright/d2p3_p01.png. LIGHT checked. Communing. ---

EMIL_D2_LS_SCAN = "extract/day2_upright/d2p3_p01.png"
EMIL_D2_LS_PDF_PAGE = 1
EMIL_D2_LS_SIDE = "Light"
EMIL_D2_LS_STARTING = n("It Is The Future You See")

EMIL_D2_LS_RESERVE = [
    n("It Is The Future You See"),  # 1  Communing
    n("Home One: War Room"),  # 2
    n("Master Kenobi"),  # 3
    n("Strike Planning"),  # 4
    n("Commando Training & K'lor'slug"),  # 5  Commando Training & KS
    n("I Hope She's All Right", True),  # 6  Alright
    n("I Wonder Who They Found", True),  # 7
    n("That's One", True),  # 8
    n("Civil Disorder"),  # 9
    n("Imperial Atrocity", True),  # 10
    n("Rebel Gunner"),  # 11  as written
    n("Admiral Ackbar", True),  # 12
    n("Captain Yutani With Blaster Cannon"),  # 13
    n("Chewbacca Of Kashyyyk"),  # 14
    n("Corporal Midge"),  # 15
    n("Lieutenant Greeve"),  # 16
    n("Lieutenant Blount", True),  # 17
    n("General Airen Cracken"),  # 18
    n("General Crix Madine"),  # 19
    n("General Solo", True),  # 20
    n("General Solo", True),  # 21
    n("Luke Skywalker, Jedi Knight"),  # 22
    n("Luke Skywalker, Rebel Scout", True),  # 23
    n("Orrimaarko", True),  # 24
    n("Threepio With His Parts Showing"),  # 25
    n("A280 Sharpshooter Rifle", True),  # 26
    n("A280 Sharpshooter Rifle", True),  # 27
    n("Endor"),  # 28
    n("Endor: Back Door"),  # 29
    n("Endor: Rebel Landing Site"),  # 30
    n("Yavin 4: Massassi War Room", True),  # 31
    n("Tatooine: Obi-Wan's Hut", True),  # 32
    n("Home One"),  # 33
    n("Flash Of Insight", True),  # 34
    n("Seeking An Audience", True),  # 35
    n("You've Got A Lot Of Guts Coming Here"),  # 36
    n("Shocking Information & Grimtaash"),  # 37
    n("Antilles Maneuver", True),  # 38
    n("Control & Tunnel Vision"),  # 39
    n("Desperate Reach", True),  # 40
    n("Desperate Reach", True),  # 41
    n("It Could Be Worse"),  # 42
    n("Hear Me Baby, Hold Together", True),  # 43
    n("Hyper Escape"),  # 44
    n("Houjix & Out Of Nowhere"),  # 45
    n("Houjix & Out Of Nowhere"),  # 46
    n("Insertion Planning"),  # 47
    n("It's A Trap!"),  # 48
    n("Let The Wookiee Win", True),  # 49
    n("Let The Wookiee Win", True),  # 50
    n("Rebel Leadership", True),  # 51
    n("Rebel Leadership", True),  # 52
    n("Rebel Leadership", True),  # 53
    n("Rebel Leadership", True),  # 54
    n("Precise Hit", True),  # 55
    n("Precise Hit", True),  # 56
    n("Were You Looking For Me?"),  # 57
    n("Use The Force"),  # 58
    n("Use The Force"),  # 59
    n("Anger, Fear, Aggression", True),  # 60
]

EMIL_D2_LS_SHIELDS = [
    n("A Tragedy Has Occurred"),  # 1
    n("Affect Mind", True),  # 2
    n("Aim High"),  # 3
    n("Battle Plan"),  # 4
    n("Chasm", True),  # 5
    n("Do, Or Do Not"),  # 6
    n("Don't Do That Again", True),  # 7
    n("Jabba's Prize", True),  # 8
    n("Let's Keep A Little Optimism Here", True),  # 9
    n("Simple Tricks And Nonsense"),  # 10
    n("The Professor", True),  # 11
    n("Ultimatum"),  # 12
]

EMIL_D2_LS_ADD = [
    n("Weapons Display", True),  # 1
    n("Wise Advice"),  # 2
    n("Your Insight Serves You Well", True),  # 3
]


EMIL_D2_LS_UNREAD: list[int] = []
EMIL_D2_LS_NO_DEST = ["Rebel Gunner"]

NOTES = """
Emil Wallin, 2014 Worlds Day 2 Light, 2010 form.
Name Emil W. Deck Communing Girl Scouts. LIGHT checked.
Username on sheet Darth-Link (index Dark-Link).
Dark xerox d2p3_p02 skipped (typed Holotable Day 2 DS already exists).

Line 1 Communing → It Is The Future You See; (V) empty.
Line 5 Commando Training & KS → Commando Training & K'lor'slug.
Line 6 I Hope She's Alright → I Hope She's All Right (V).
Line 11 Rebel Gunner as written (NO_DEST; not Rogue Gunner).
Line 13 Captain Yutani w Blaster Cannon → Captain Yutani With Blaster Cannon.
Lines 51–54 four Rebel Leadership (V) as written.
""".strip()


if __name__ == "__main__":
    assert len(EMIL_D2_LS_RESERVE) == 60, len(EMIL_D2_LS_RESERVE)
    assert len(EMIL_D2_LS_SHIELDS) == 12, len(EMIL_D2_LS_SHIELDS)
    print("transcribe_emil_day2_ls.py", PLAYER)
    print("  Light Communing Girl Scouts reserve", len(EMIL_D2_LS_RESERVE), "shields", len(EMIL_D2_LS_SHIELDS), "add", len(EMIL_D2_LS_ADD), "unread", EMIL_D2_LS_UNREAD, "no_dest", EMIL_D2_LS_NO_DEST)
