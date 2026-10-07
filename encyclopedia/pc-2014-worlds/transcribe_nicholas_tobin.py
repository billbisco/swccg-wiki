#!/usr/bin/env python3
"""Day 2 Xerox: Nicholas Tobin (NinjaElf6) Light Rogues + Dark Palpatine's Ops.

Source: extract/day2_upright/d2p3_p09.png (Light) and
extract/day2_upright/d2p3_p10.png (Dark). 2013 form, 2014 Worlds 8/23/14.
(V) follows the sheet checkbox. Typed/print handwriting.
"""
from __future__ import annotations

import sys
from pathlib import Path


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Nicholas Tobin"
USERNAME = "NinjaElf6"
LS_DECK_NAME = "Rogues Never Die"
DS_DECK_NAME = "Palpatine's Ops"
LS_SIDE = "Light"
DS_SIDE = "Dark"
FORM = "xerox_2013"
LS_SCAN = "extract/day2_upright/d2p3_p09.png"
DS_SCAN = "extract/day2_upright/d2p3_p10.png"
PDF = "2014 Worlds Day 2 Part 3.pdf"
LS_PDF_PAGE = 9
DS_PDF_PAGE = 10
LS_STARTING = ("Center Of Tyranny / A Liberated World", False)
DS_STARTING = ("Endor Operations / Imperial Outpost", False)


# --- Light: d2p3_p09.png upright. LIGHT checked. Center Of Tyranny. ---

LS_RESERVE = [
    n("Anger, Fear, Aggression", True),  # 1
    n("Center Of Tyranny / A Liberated World"),  # 2  written Liberated World
    n("Coruscant", True),  # 3
    n("Coruscant: Main Power Plant"),  # 4
    n("Coruscant: Lower Levels"),  # 5
    n("Planetary Shield"),  # 6
    n("Rogue Insertion"),  # 7
    n("Heading For The Medical Frigate"),  # 8
    n("Bacta Infirmary"),  # 9
    n("Declaration Of Rebellion"),  # 10
    n("Rogue Squadron Tactics"),  # 11
    n("Commander Luke Skywalker", True),  # 12
    n("Commander Luke Skywalker", True),  # 13
    n("Wedge Antilles, Red Squadron Leader"),  # 14
    n("Wedge Antilles, Red Squadron Leader"),  # 15
    n("Dash Rendar", True),  # 16
    n("Corran Horn"),  # 17
    n("Jaina Solo"),  # 18
    n("Biggs, Rogue Legend"),  # 19
    n("Commander Nara"),  # 20  written Commader Nara
    n("Derek 'Hobbie' Klivian", True),  # 21
    n("Tycho Celchu", True),  # 22
    n("Dack Ralter", True),  # 23
    n("Ten Numb", True),  # 24
    n("Zev Senesca"),  # 25
    n("Veteran Rogue"),  # 26
    n("Veteran Rogue"),  # 27
    n("Leia, Rebel Princess"),  # 28
    n("Lando Calrissian, Unlikely Hero"),  # 29
    n("Han, Chewie, And The Falcon", True),  # 30
    n("Red 6"),  # 31
    n("Tantive IV", True),  # 32
    n("Spiral"),  # 33
    n("Artoo-Detoo In Red 5"),  # 34
    n("Lady Luck"),  # 35
    n("Echo Base Garrison"),  # 36
    n("Commando Training & K'lor'slug"),  # 37
    n("Menace Fades"),  # 38
    n("Coruscant Celebration"),  # 39
    n("Field Dressing"),  # 40
    n("Imperial Atrocity", True),  # 41
    n("Draw Their Fire"),  # 42
    n("Strikeforce", True),  # 43
    n("Antilles Maneuver & Rebel Reinforcements"),  # 44
    n("Inconsequential Barriers"),  # 45
    n("Odin Nesloor & First Aid"),  # 46
    n("Yub Yub, Commander"),  # 47
    n("Yub Yub, Commander"),  # 48
    n("Yub Yub, Commander"),  # 49
    n("Yub Yub, Commander"),  # 50
    n("Houjix & Out Of Nowhere"),  # 51
    n("Desperate Reach", True),  # 52
    n("Blast The Door, Kid!"),  # 53
    n("Rebel Barrier"),  # 54
    n("Rebel Barrier", True),  # 55
    n("Hear Me Baby, Hold Together", True),  # 56
    n("Out Of Commission & Transmission Terminated"),  # 57
    n("Rogue 1"),  # 58
    n("Dressel"),  # 59
    n("Coruscant: Jedi Council Chamber"),  # 60
]

LS_SHIELDS = [
    n("Aim High"),  # 1
    n("Your Insight Serves You Well", True),  # 2  written Insights Serve
    n("Don't Do That Again", True),  # 3
    n("Yavin Sentry", True),  # 4
    n("Weapons Display", True),  # 5
    n("Ultimatum"),  # 6
    n("Let's Keep A Little Optimism Here", True),  # 7
    n("Chasm", True),  # 8
    n("Affect Mind", True),  # 9
    n("A Tragedy Has Occurred"),  # 10
    n("Simple Tricks And Nonsense"),  # 11
    n("The Professor", True),  # 12
    n("He Can Go About His Business", True),  # 13
    n("Battle Plan"),  # 14
    n("Do, Or Do Not"),  # 15
]

LS_ADD: list = []


# --- Dark: d2p3_p10.png upright. DARK checked. Endor Operations. ---

DS_RESERVE = [
    n("Knowledge And Defense", True),  # 1
    n("Endor Operations / Imperial Outpost"),  # 2
    n("Endor"),  # 3
    n("Endor: Bunker"),  # 4
    n("Endor: Landing Platform"),  # 5
    n("According To My Design"),  # 6
    n("Emperor Palpatine"),  # 7
    n("Ni Chuba Na??", True),  # 8
    n("Establish Control", True),  # 9
    n("Endor Shield", True),  # 10
    n("Darth Vader", True),  # 11
    n("Darth Vader With Lightsaber"),  # 12
    n("General Veers", True),  # 13
    n("Admiral Ozzel"),  # 14
    n("Darth Maul With Lightsaber"),  # 15
    n("Darth Maul With Lightsaber"),  # 16
    n("DS-61-2"),  # 17
    n("Baron Soontir Fel"),  # 18
    n("Grand Moff Tarkin", True),  # 19
    n("Jango Fett, The Assassin"),  # 20
    n("Boba Fett, Prepared Hunter"),  # 21
    n("Mara Jade With Lightsaber"),  # 22
    n("Juno Eclipse, Black Leader"),  # 23
    n("U-3PO"),  # 24
    n("Saber 1"),  # 25
    n("Colonel Jendon In Onyx 1"),  # 26  written in Onyx 1
    n("Black 2", True),  # 27
    n("Rogue Shadow"),  # 28
    n("Dengar In Punishing One"),  # 29
    n("Vader's Personal Shuttle", True),  # 30
    n("Slave I, Symbol Of Fear"),  # 31
    n("Blizzard 2", True),  # 32
    n("Blizzard 4"),  # 33
    n("Blizzard Scout 1", True),  # 34
    n("Imperial Decree"),  # 35
    n("Combat Response", True),  # 36
    n("Ominous Rumors"),  # 37
    n("Establish Secret Base", True),  # 38
    n("Lateral Damage"),  # 39
    n("Image Of The Dark Lord", True),  # 40
    n("Control & Set For Stun"),  # 41
    n("Imperial Barrier"),  # 42
    n("Imperial Barrier"),  # 43
    n("Short Range Fighters & Watch Your Back!"),  # 44
    n("Short Range Fighters & Watch Your Back!"),  # 45
    n("Short Range Fighters & Watch Your Back!"),  # 46
    n("Sense"),  # 47
    n("Sense & Uncertain Is The Future"),  # 48
    n("A Dark Time For The Rebellion", True),  # 49
    n("A Dark Time For The Rebellion", True),  # 50
    n("Trample"),  # 51
    n("Why Didn't You Tell Me?", True),  # 52
    n("Sonic Bombardment", True),  # 53
    n("Sonic Bombardment", True),  # 54
    n("Masterful Move & Endor Occupation"),  # 55
    n("Force Lightning"),  # 56
    n("Cloud City: Security Tower", True),  # 57
    n("Fondor"),  # 58
    n("Fighters Coming In"),  # 59
    n("Fighters Coming In"),  # 60
]

DS_SHIELDS = [
    n("Death Star Sentry", True),  # 1
    n("Secret Plans"),  # 2
    n("You Cannot Hide Forever", True),  # 3
    n("Do They Have A Code Clearance?", True),  # 4
    n("A Useless Gesture", True),  # 5
    n("There Is No Try"),  # 6
    n("Firepower", True),  # 7
    n("Imperial Detention"),  # 8
    n("Abyss", True),  # 9
    n("Allegations Of Corruption"),  # 10
    n("Battle Order"),  # 11
    n("Come Here You Big Coward"),  # 12
    n("We'll Let Fate-a Decide, Huh?", True),  # 13
    n("I Find Your Lack Of Faith Disturbing", True),  # 14
    n("Resistance"),  # 15
]

DS_ADD: list = []

LS_UNREAD: list[int] = []
DS_UNREAD: list[int] = []
NO_DEST: list[str] = []  # Center Of Tyranny uses printed back A Liberated World

NOTES = """
Nicholas Tobin / NinjaElf6, 2014 Worlds Day 2 8/23/14, 2013 form.
Light d2p3_p09 Rogues Never Die (LIGHT checked). Center Of Tyranny / Rogue Squadron.
Dark d2p3_p10 Palpatine's Ops (DARK checked). Endor Operations.
Hidden Fortress / Jedi Tests blank on both sides.
LS line 2 written Center Of Tyranny / Liberated World (printed A Liberated World).
LS line 20 Commader Nara dest Commander Narra.
LS shield 2 written Your Insights Serve You Well.
LS line 55 Rebel Barrier (V) vs line 54 unchecked copy.
""".strip()


def _lookup_side(side: str, rows: list, prefer_sh: bool = False) -> list[str]:
    root = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(root))
    from generate_2014_worlds import _lookup  # noqa: E402

    miss: list[str] = []
    for name, is_v in rows:
        if not name:
            continue
        dest = _lookup(name, side, is_v, prefer_sh=prefer_sh)
        if not dest:
            miss.append(f"{side}\t{int(is_v)}\t{name}")
            print("NO_DEST", side, int(is_v), name)
        else:
            print("OK", side, int(is_v), name, "->", dest)
    return miss


if __name__ == "__main__":
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 15, len(LS_SHIELDS)
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 15, len(DS_SHIELDS)
    miss = []
    miss += _lookup_side("Light", LS_RESERVE)
    miss += _lookup_side("Light", LS_SHIELDS, prefer_sh=True)
    miss += _lookup_side("Dark", DS_RESERVE)
    miss += _lookup_side("Dark", DS_SHIELDS, prefer_sh=True)
    print("FILE", Path(__file__).name)
    print("LS", PLAYER, LS_SIDE, len(LS_RESERVE), len(LS_SHIELDS), "unread", LS_UNREAD)
    print("DS", PLAYER, DS_SIDE, len(DS_RESERVE), len(DS_SHIELDS), "unread", DS_UNREAD)
    print("NO_DEST", miss or "none")
