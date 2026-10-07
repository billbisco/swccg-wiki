#!/usr/bin/env python3
"""Day 2 Xerox: Alex O'Shea (Thursday) Dark RIP Spice + Light RIP Communing.

Source: extract/day2_upright/d2p3_p15.png (Dark) and
extract/day2_upright/d2p3_p16.png (Light). 2013 form, 2014 Worlds Day 2 8/23/14.
LIGHT/DARK unchecked on both; side from cards. (V) follows the sheet checkbox.
"""
from __future__ import annotations

import sys
from pathlib import Path


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Alex O'Shea"
USERNAME = "Thursday"
LS_DECK_NAME = "RIP Communing"
DS_DECK_NAME = "RIP Spice"
LS_SIDE = "Light"
DS_SIDE = "Dark"
FORM = "xerox_2013"
LS_SCAN = "extract/day2_upright/d2p3_p16.png"
DS_SCAN = "extract/day2_upright/d2p3_p15.png"
PDF = "2014 Worlds Day 2 Part 3.pdf"
LS_PDF_PAGE = 16
DS_PDF_PAGE = 15
LS_STARTING = ("Communing", True)
DS_STARTING = ("Kessel", False)


# --- Dark: d2p3_p15.png upright. RIP Spice / Kessel. ---

DS_RESERVE = [
    n("Kessel"),  # 1
    n("Combat Readiness", True),  # 2
    n("Kessel: Spice Mines - Administrator's Office", True),  # 3
    n("Gift Of The Master", True),  # 4
    n("I'll Take Them Myself", True),  # 5
    n("Ni Chuba Na??", True),  # 6
    n("4-LOM With Concussion Rifle", True),  # 7
    n("Boba Fett, Prepared Hunter", True),  # 8
    n("Count Dooku", True),  # 9
    n("Count Dooku", True),  # 10
    n("Count Dooku", True),  # 11
    n("Darth Maul With Lightsaber"),  # 12
    n("Darth Maul With Lightsaber"),  # 13
    n("Darth Vader, Dark Lord Of The Sith"),  # 14
    n("Darth Vader, Dark Lord Of The Sith"),  # 15
    n("Darth Vader, Dark Lord Of The Sith"),  # 16
    n("Dengar With Blaster Carbine", True),  # 17
    n("Dr. Evazan & Ponda Baba"),  # 18
    n("Emperor Palpatine"),  # 19
    n("Emperor Palpatine"),  # 20
    n("Emperor Palpatine"),  # 21
    n("Garindan", True),  # 22
    n("Jango Fett, The Assassin", True),  # 23
    n("Moruth Doole, Kessel Administrator", True),  # 24
    n("P-59"),  # 25
    n("Maul's Sith Infiltrator"),  # 26
    n("Slave I, Symbol Of Fear", True),  # 27
    n("Dooku's Lightsaber", True),  # 28
    n("Vader's Lightsaber"),  # 29
    n("Kessel Surveillance System", True),  # 30
    n("Blow Parried"),  # 31
    n("Force Field", True),  # 32
    n("Force Field", True),  # 33
    n("Force Lightning"),  # 34
    n("Force Lightning"),  # 35
    n("Force Push", True),  # 36
    n("Ghhhk"),  # 37
    n("I Have You Now", True),  # 38
    n("Masterful Move & Endor Occupation"),  # 39
    n("Monnok"),  # 40
    n("Sense & Uncertain Is The Future"),  # 41
    n("Short Range Fighters & Watch Your Back!"),  # 42
    n("Short Range Fighters & Watch Your Back!"),  # 43
    n("Sith Fury & End This Destructive Conflict", True),  # 44
    n("Sniper & Dark Strike"),  # 45
    n("Sonic Bombardment", True),  # 46
    n("Sonic Bombardment", True),  # 47
    n("We Must Accelerate Our Plans"),  # 48
    n("We Must Accelerate Our Plans"),  # 49
    n("Blast Door Controls"),  # 50
    n("Blaster Rack", True),  # 51
    n("Imperial Justice", True),  # 52
    n("Revenge Of The Sith", True),  # 53
    n("The Phantom Menace"),  # 54
    n("Spice Mine Operations", True),  # 55
    n("Blockade Flagship: Bridge"),  # 56
    n("Cloud City: Security Tower", True),  # 57
    n("Kessel: Spice Mines - Extraction Facility", True),  # 58
    n("Kessel: Spice Mines - Prison", True),  # 59
    n("Knowledge And Defense", True),  # 60
]

DS_SHIELDS = [
    n("Abyss", True),  # 1
    n("Allegations Of Corruption"),  # 2
    n("Battle Order", True),  # 3
    n("Come Here You Big Coward"),  # 4
    n("Death Star Sentry", True),  # 5
    n("Do They Have A Code Clearance?", True),  # 6
    n("Fanfare"),  # 7
    n("Firepower", True),  # 8
    n("I Find Your Lack Of Faith Disturbing", True),  # 9
    n("Resistance"),  # 10
    n("Secret Plans"),  # 11
    n("There Is No Try"),  # 12
    n("Weapon Of A Sith"),  # 13
    n("We'll Let Fate-a Decide, Huh?", True),  # 14
    n("You Cannot Hide Forever", True),  # 15
]

DS_ADD: list = []


# --- Light: d2p3_p16.png upright. RIP Communing. ---

LS_RESERVE = [
    n("Tatooine: Slave Quarters"),  # 1
    n("Communing", True),  # 2
    n("Master Kenobi", True),  # 3
    n("Commando Training & K'lor'slug", True),  # 4
    n("Draw Their Fire"),  # 5
    n("Scrambled Transmission", True),  # 6
    n("Wokling", True),  # 7
    n("Admiral Ackbar", True),  # 8
    n("Chewie, Enraged", True),  # 9
    n("Chewie, Enraged", True),  # 10
    n("Chewie, Enraged", True),  # 11
    n("Chewie, Enraged", True),  # 12
    n("Corran Horn"),  # 13
    n("Corran Horn"),  # 14
    n("Han With Heavy Blaster Pistol"),  # 15
    n("Lando Calrissian, Scoundrel", True),  # 16
    n("Luke With Lightsaber"),  # 17
    n("Luke With Lightsaber"),  # 18
    n("Luke With Lightsaber"),  # 19
    n("Padme Naberrie", True),  # 20
    n("Senator Leia Organa", True),  # 21
    n("Shmi Skywalker"),  # 22
    n("Threepio With His Parts Showing"),  # 23
    n("Wedge Antilles, Red Squadron Leader"),  # 24
    n("Yoda, Great Warrior", True),  # 25
    n("Alderaan Consular Ship", True),  # 26
    n("Artoo-Detoo In Red 5"),  # 27
    n("Artoo-Detoo In Red 5"),  # 28
    n("Home One"),  # 29
    n("Chewbacca's Bowcaster"),  # 30
    n("A Jedi's Resilience"),  # 31
    n("A Jedi's Resilience"),  # 32
    n("Escape Pod", True),  # 33
    n("Escape Pod", True),  # 34
    n("Houjix"),  # 35
    n("Houjix"),  # 36
    n("Let The Wookiee Win", True),  # 37
    n("Let The Wookiee Win", True),  # 38
    n("Rebel Leadership", True),  # 39
    n("Rebel Leadership", True),  # 40
    n("Rebel Leadership", True),  # 41
    n("Rebel Leadership", True),  # 42
    n("Run Luke, Run!", True),  # 43
    n("Run Luke, Run!", True),  # 44
    n("Run Luke, Run!", True),  # 45
    n("The Bith Shuffle & Desperate Reach"),  # 46
    n("Use The Force", True),  # 47
    n("Use The Force", True),  # 48
    n("A Gift"),  # 49
    n("Evacuation Control", True),  # 50
    n("Imperial Atrocity", True),  # 51
    n("Imperial Atrocity", True),  # 52
    n("Projection Of A Skywalker"),  # 53
    n("Rebel Gunrunner", True),  # 54
    n("Home One: War Room"),  # 55
    n("Jabba's Palace: Audience Chamber"),  # 56
    n("Tatooine: Cantina"),  # 57
    n("Tatooine: Obi-Wan's Hut", True),  # 58
    n("Tatooine"),  # 59  written Tatooine (Coruscant)
    n("Anger, Fear, Aggression", True),  # 60
]

LS_SHIELDS = [
    n("A Tragedy Has Occurred"),  # 1
    n("Aim High"),  # 2
    n("Battle Plan", True),  # 3
    n("Chasm", True),  # 4
    n("Do, Or Do Not"),  # 5
    n("Don't Do That Again", True),  # 6
    n("Let's Keep A Little Optimism Here", True),  # 7
    n("Simple Tricks And Nonsense", True),  # 8
    n("The Professor", True),  # 9
    n("Ultimatum"),  # 10
    n("Weapons Display", True),  # 11
    n("Wise Advice"),  # 12
    n("Yavin Sentry", True),  # 13
    n("Your Insight Serves You Well", True),  # 14
    n("Your Ship?"),  # 15
]

LS_ADD: list = []

LS_UNREAD: list[int] = []
DS_UNREAD: list[int] = []
NO_DEST: list[str] = []

NOTES = """
Alex O'Shea / Thursday, 2014 Worlds Day 2 8/23/14, 2013 form.
Dark d2p3_p15 RIP Spice (LIGHT/DARK unchecked). Kessel.
Light d2p3_p16 RIP Communing (LIGHT/DARK unchecked). Communing.
Hidden Fortress / Jedi Tests blank on both sides.
LS line 59 written Tatooine (Coruscant) — Tatooine system, SE/Coruscant printing note.
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
    miss += _lookup_side("Dark", DS_RESERVE)
    miss += _lookup_side("Dark", DS_SHIELDS, prefer_sh=True)
    miss += _lookup_side("Light", LS_RESERVE)
    miss += _lookup_side("Light", LS_SHIELDS, prefer_sh=True)
    print("FILE", Path(__file__).name)
    print("DS", PLAYER, DS_SIDE, len(DS_RESERVE), len(DS_SHIELDS), "unread", DS_UNREAD)
    print("LS", PLAYER, LS_SIDE, len(LS_RESERVE), len(LS_SHIELDS), "unread", LS_UNREAD)
    print("NO_DEST", miss or "none")
