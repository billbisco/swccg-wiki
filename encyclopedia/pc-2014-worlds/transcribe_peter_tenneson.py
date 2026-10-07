#!/usr/bin/env python3
"""Day 2 Xerox: Peter Tenneson (patmagrain) Light Y42 Mains + Dark Hunt Down.

Source: extract/day2_upright/d2p3_p07.png (Light) and
extract/day2_upright/d2p3_p08.png (Dark). 2010 form, Worlds 2014 08/23/14.
(V) follows the sheet checkbox. Dittos expanded. Duplicate 37/38 line
numbers on both sides expanded to slots 39–40.
"""
from __future__ import annotations

import sys
from pathlib import Path


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Peter Tenneson"
USERNAME = "patmagrain"
LS_DECK_NAME = "Y42 Mains"
DS_DECK_NAME = "Last time I can use this deck"
LS_SIDE = "Light"
DS_SIDE = "Dark"
FORM = "xerox_2010"
LS_SCAN = "extract/day2_upright/d2p3_p07.png"
DS_SCAN = "extract/day2_upright/d2p3_p08.png"
PDF = "2014 Worlds Day 2 Part 3.pdf"
LS_PDF_PAGE = 7
DS_PDF_PAGE = 8
LS_STARTING = ("Watch Your Step / This Place Can Be A Little Rough", True)
DS_STARTING = ("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True)


# --- Light: d2p3_p07.png upright. LIGHT checked. Watch Your Step. ---

LS_RESERVE = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),  # 1
    n("Corellia", True),  # 2
    n("Heading For The Medical Frigate"),  # 3  HFTMF
    n("Spaceport City"),  # 4
    n("Endor: Back Door"),  # 5
    n("Luke Skywalker, Jedi Knight"),  # 6
    n("That's One", True),  # 7
    n("Lando Calrissian, Scoundrel"),  # 8  Lando, Scoundrel
    n("Sorry About The Mess & Blaster Proficiency"),  # 9  SATM combo
    n("Houjix & Out Of Nowhere"),  # 10  Houjix combo
    n("Punch It!"),  # 11
    n("Rebel Leadership", True),  # 12
    n("Desperate Reach", True),  # 13
    n("Punch It!"),  # 14
    n("Leia, Rebel Princess"),  # 15
    n("Antilles Maneuver & Rebel Reinforcements", True),  # 16  Ant Man combo
    n("Luke Skywalker, Jedi Knight"),  # 17
    n("Antilles Maneuver", True),  # 18  Ant Man (not combo)
    n("Luke's Lightsaber"),  # 19
    n("Corran Horn"),  # 20
    n("Hear Me Baby, Hold Together", True),  # 21  replacement; prior title crossed
    n("Naboo: Boss Nass' Chambers"),  # 22
    n("Admiral Ackbar", True),  # 23
    n("A Jedi's Resilience"),  # 24
    n("Qui-Gon Jinn With Lightsaber"),  # 25  EPP Qui Gon
    n("A Jedi's Resilience"),  # 26
    n("Sorry About The Mess & Blaster Proficiency"),  # 27  SATM combo
    n("Menace Fades"),  # 28
    n("Luke Skywalker, Strong In The Force", True),  # 29  Luke, SITF
    n("Mace Windu", True),  # 30
    n("Wesa Gotta Grand Army"),  # 31
    n("Padme Naberrie", True),  # 32
    n("Luke's Bionic Hand", True),  # 33
    n("Rebel Leadership", True),  # 34
    n("Blaster Deflection"),  # 35
    n("Let The Wookiee Win", True),  # 36
    n("Temporary Foothold", True),  # 37
    n("Wesa Gotta Grand Army"),  # 38
    n("Rebel Leadership", True),  # 39  second 37 on the sheet
    n("Wokling", True),  # 40  second 38 on the sheet
    n("Rycar Ryjerd", True),  # 41
    n("Quick Draw", True),  # 42
    n("Leia, Rebel Princess"),  # 43
    n("Home One"),  # 44
    n("Let The Wookiee Win", True),  # 45
    n("Seeking An Audience", True),  # 46
    n("Home One: War Room"),  # 47
    n("Sai'torr Kal Fas", True),  # 48  Sai'tor
    n("Jedi Lightsaber", True),  # 49
    n("Obi-Wan Kenobi", True),  # 50
    n("Obi-Wan's Lightsaber"),  # 51  (Prem)
    n("Obi-Wan's Journal"),  # 52
    n("Obi-Wan Kenobi", True),  # 53
    n("Millennium Falcon", True),  # 54
    n("Han's Toolkit", True),  # 55
    n("Leia's Blaster Rifle"),  # 56
    n("General Solo", True),  # 57
    n("Chewbacca", True),  # 58  Chewie
    n("Mace Windu", True),  # 59
    n("Anger, Fear, Aggression", True),  # 60
]

LS_SHIELDS = [
    n("Jabba's Prize", True),  # 1  shield box; not a shield printing
    n("Let's Keep A Little Optimism Here", True),  # 2
    n("Your Insight Serves You Well", True),  # 3
    n("Ultimatum"),  # 4
    n("Do, Or Do Not"),  # 5
    n("Only Jedi Carry That Weapon"),  # 6
    n("Weapons Display", True),  # 8  slot 7 He Can Go About His Business crossed
    n("Simple Tricks And Nonsense", True),  # 9
    n("Aim High"),  # 10
    n("Battle Plan"),  # 11
    n("The Professor", True),  # 12
]

LS_ADD = [
    n("A Tragedy Has Occurred"),  # 2  slot 1 Don't Do That Again crossed
    n("Wise Advice"),  # 3
    n("There Is Another", True),  # 4
    n("Yavin Sentry", True),  # 5
]


# --- Dark: d2p3_p08.png upright. DARK checked. Hunt Down. ---

DS_RESERVE = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),  # 1
    n("Dengar With Blaster Carbine", True),  # 2
    n("Juno Eclipse, Black Leader", True),  # 3
    n("Force Lightning"),  # 4
    n("First Strike"),  # 5
    n("Presence Of The Force"),  # 6
    n("Jango Fett, The Assassin", True),  # 7  written Father of Fett
    n("Masterful Move"),  # 8
    n("Force Push", True),  # 9
    n("Victory", True),  # 10
    n("No Escape"),  # 11
    n("Boba Fett, Bounty Hunter"),  # 12
    n("Darth Vader, Dark Lord Of The Sith"),  # 13  DVDLOTS
    n("Vader's Lightsaber"),  # 14
    n("Emperor Palpatine"),  # 15
    n("Blockade Flagship: Bridge"),  # 16  Flagship: Bridge
    n("Mara Jade With Lightsaber", True),  # 17
    n("Garindan", True),  # 18
    n("Masterful Move"),  # 19
    n("Ghhhk"),  # 20
    n("Darth Vader, Dark Lord Of The Sith"),  # 21  DVDLOTS
    n("Revenge Of The Sith", True),  # 22
    n("Galen Marek, Starkiller", True),  # 23  Galen, Secret Apprentice
    n("Galen's Lightsaber, Vader's Gift", True),  # 24
    n("Prepared Defenses", True),  # 25
    n("Coruscant"),  # 26  Coruscant (Spec. Ed)
    n("We Must Accelerate Our Plans"),  # 27  WMAOP
    n("Force Field", True),  # 28
    n("Galen Marek, Starkiller", True),  # 29
    n("Force Field", True),  # 30
    n("Coruscant: Imperial City"),  # 31
    n("P-59"),  # 32
    n("We Must Accelerate Our Plans"),  # 33  WMAOP
    n("Darth Vader, Dark Lord Of The Sith"),  # 34  DVDLOTS
    n("Ni Chuba Na??", True),  # 35
    n("Galen Marek, Starkiller", True),  # 36
    n("Dr. Evazan & Ponda Baba"),  # 37  Dr. E + Ponda B
    n("Blizzard 4"),  # 38
    n("Sith Fury & End This Destructive Conflict", True),  # 39  second 37
    n("Weapon Levitation & The Empire's Back", True),  # 40  second 38
    n("We Must Accelerate Our Plans"),  # 41  WMAOP
    n("Cold Feet", True),  # 42
    n("Sniper & Dark Strike"),  # 43
    n("One Beautiful Thing", True),  # 44
    n("Monnok"),  # 45
    n("General Nevar", True),  # 46
    n("A Sith's Plans", True),  # 47
    n("Emperor Palpatine"),  # 48
    n("Naboo: Theed Palace Generator Core"),  # 49
    n("I Have You Now", True),  # 50
    n("Endor Shield", True),  # 51
    n("A Sith's Weapon", True),  # 52
    n("Rogue Shadow", True),  # 53  Galen's Fighter (Rogue Shadow)
    n("Dengar With Blaster Carbine", True),  # 54
    n("Grand Admiral Thrawn"),  # 55
    n("Blaster Rack", True),  # 56
    n("Gift Of The Master", True),  # 57
    n("Endor"),  # 58
    n("Emperor Palpatine"),  # 59
    n("Knowledge And Defense", True),  # 60
]

DS_SHIELDS = [
    n("Secret Plans"),  # 1
    n("Battle Order"),  # 2
    n("Weapon Of A Sith"),  # 3
    n("Abyss", True),  # 4
    n("Allegations Of Corruption"),  # 5
    n("A Useless Gesture", True),  # 6
    n("Leave Them To Me", True),  # 7
    n("You Cannot Hide Forever", True),  # 8
    n("There Is No Try"),  # 9
    n("Come Here You Big Coward"),  # 10
    n("Resistance"),  # 11
    n("We'll Let Fate-a Decide, Huh?"),  # 12
]

DS_ADD = [
    n("Firepower", True),  # 1
    n("Do They Have A Code Clearance?", True),  # 2
    n("Death Star Sentry", True),  # 3
]

LS_UNREAD: list[int] = []
DS_UNREAD: list[int] = []
NO_DEST: list[str] = []

NOTES = """
Peter Tenneson / patmagrain, 2014 Worlds Day 2 08/23/14, 2010 form.
Light d2p3_p07 Y42 Mains (LIGHT checked). Watch Your Step.
Dark d2p3_p08 Last time I can use this deck (DARK checked). Hunt Down.

LS: both columns used a second 37/38 for slots 39–40 (Rebel Leadership, Wokling).
Line 16 Ant Man combo vs line 18 Ant Man (Antilles Maneuver (V) only).
Line 21 prior title crossed; Hear Me Baby, Hold Together (V) kept.
Line 29 Luke, SITF = Luke Skywalker, Strong In The Force.
Line 58 Chewie taken as Chewbacca (V).
Shield 7 He Can Go About His Business fully crossed, omitted.
ADD 1 Don't Do That Again fully crossed, omitted.
Shield 1 Jabba's Prize in the shield box (not a shield printing).

DS: second 37/38 are Sith Fury combo and Weapon Levitation combo (slots 39–40).
Line 7 written Jango Fett, Father of Fett; dest Jango Fett, The Assassin (V).
Galen, Secret Apprentice dest Galen Marek, Starkiller (V).
Line 53 Galen's Fighter (Rogue Shadow) = Rogue Shadow.
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
    assert len(LS_SHIELDS) == 11, len(LS_SHIELDS)
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 12, len(DS_SHIELDS)
    miss = []
    miss += _lookup_side("Light", LS_RESERVE)
    miss += _lookup_side("Light", LS_SHIELDS, prefer_sh=True)
    miss += _lookup_side("Light", LS_ADD, prefer_sh=True)
    miss += _lookup_side("Dark", DS_RESERVE)
    miss += _lookup_side("Dark", DS_SHIELDS, prefer_sh=True)
    miss += _lookup_side("Dark", DS_ADD, prefer_sh=True)
    print("FILE", Path(__file__).name)
    print("LS", PLAYER, LS_SIDE, len(LS_RESERVE), len(LS_SHIELDS), "unread", LS_UNREAD)
    print("DS", PLAYER, DS_SIDE, len(DS_RESERVE), len(DS_SHIELDS), "unread", DS_UNREAD)
    print("NO_DEST", miss or "none")
