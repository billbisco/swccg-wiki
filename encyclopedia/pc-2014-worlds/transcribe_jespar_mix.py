#!/usr/bin/env python3
"""Day 2 Xerox: Mean Jespar Mix Light (p05) + unnamed Dark pair (p06).

Source: extract/day2_upright/d2p3_p05.png (Light, WYS) and
extract/day2_upright/d2p3_p06.png (Dark, Court / Cloud City). 2010 form.
Name as written on p05; p06 name box blank (likely pair). (V) follows the
sheet checkbox or a handwritten V beside the title. Dittos expanded.
"""
from __future__ import annotations

import sys
from pathlib import Path


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Mean Jespar Mix"
DS_PLAYER = None
USERNAME = "rlx"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
LS_SIDE = "Light"
DS_SIDE = "Dark"
FORM = "xerox_2010"
LS_SCAN = "extract/day2_upright/d2p3_p05.png"
DS_SCAN = "extract/day2_upright/d2p3_p06.png"
PDF = "2014 Worlds Day 2 Part 3.pdf"
LS_PDF_PAGE = 5
DS_PDF_PAGE = 6
LS_STARTING = ("Watch Your Step / This Place Can Be A Little Rough", True)
DS_STARTING = ("Court Of The Vile Gangster / I Shall Enjoy Watching You Die", False)


# --- Light: d2p3_p05.png upright. LIGHT/DARK unchecked. WYS. ---

LS_RESERVE = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),  # 1  WYS; handwritten V
    n("Corellia", True),  # 2  handwritten V
    n("Spaceport City"),  # 3
    n("Millennium Falcon", True),  # 4  handwritten V
    n("General Solo", True),  # 5  handwritten V
    n("Podrace Prep"),  # 6
    n("Tatooine: Podrace Arena"),  # 7
    n("Anakin's Podracer"),  # 8  written Andies Palace
    n("Boonta Eve Podrace"),  # 9
    n("Quick Draw", True),  # 10  handwritten V
    n("Endor: Back Door"),  # 11
    n(None),  # 12  location scrawl unread (Dagobah/Desperate)
    n("Naboo: Boss Nass' Chambers"),  # 13
    n("Home One: War Room"),  # 14  H1: War Room
    n("I Did It!"),  # 15
    n("Home One"),  # 16  H1
    n("Luke Skywalker, Jedi Knight"),  # 17
    n("Luke Skywalker, Jedi Knight"),  # 18  ditto
    n("Luke Skywalker, Jedi Knight"),  # 19  ditto
    n("Mace Windu", True),  # 20  handwritten V
    n("Mace Windu", True),  # 21  ditto
    n("Lando Calrissian, Scoundrel"),  # 22
    n("Jaina Solo"),  # 23
    n("Chewie With Bowcaster"),  # 24  EPP Chewie
    n("Qui-Gon Jinn With Lightsaber"),  # 25  EPP Qui
    n("Corran Horn"),  # 26
    n("Leia, Rebel Princess"),  # 27
    n("Padme Naberrie", True),  # 28  handwritten V
    n("Chewie, Enraged", True),  # 29  Chewie; handwritten V
    n("Luke's Lightsaber"),  # 30
    n("Jedi Lightsaber", True),  # 31  handwritten V
    n("Luke's Bionic Hand"),  # 32
    n("Imperial Atrocity", True),  # 33  handwritten V
    n("Projection Of A Skywalker"),  # 34
    n("That's One"),  # 35
    n("Seeking An Audience", True),  # 36  handwritten V
    n("Temporary Foothold"),  # 37
    n("Sai'torr Kal Fas"),  # 38  Sai'torr
    n("Rebel Leadership", True),  # 39  handwritten V
    n("Rebel Leadership", True),  # 40  ditto
    n("Wesa Gotta Grand Army"),  # 41
    n("Wesa Gotta Grand Army"),  # 42  ditto
    n("Let The Wookiee Win", True),  # 43  LTWW; handwritten V
    n("Let The Wookiee Win", True),  # 44  ditto
    n("Escape Pod", True),  # 45  handwritten V
    n("Escape Pod", True),  # 46  ditto
    n("Houjix"),  # 47
    n("Grimtaash"),  # 48
    n("Rebel Barrier"),  # 49
    n("Punch It!", True),  # 50  handwritten V
    n("Blaster Deflection"),  # 51
    n("Sorry About The Mess & Blaster Proficiency"),  # 52  SATM combo
    n("A Jedi's Resilience"),  # 53
    n("Clash Of Sabers"),  # 54
    n("Punch It!"),  # 55
    n("Antilles Maneuver & Rebel Reinforcements"),  # 56  Antilles Maneuver combo
    n("Antilles Maneuver & Rebel Reinforcements"),  # 57  ditto
    n("Admiral Ackbar", True),  # 58  handwritten V
    n("Lando Calrissian, Scoundrel"),  # 59
    n("Anger, Fear, Aggression", True),  # 60  AFA; handwritten V
]

LS_SHIELDS = [
    n("There Is Another"),  # 1
    n("Jabba's Prize"),  # 2  shield box; not a shield printing
    n("Aim High"),  # 3
    n("Only Jedi Carry That Weapon"),  # 4
    n("Simple Tricks And Nonsense"),  # 5
    n("Weapons Display", True),  # 6  handwritten V
    n("Do, Or Do Not"),  # 7
    n("Chasm", True),  # 8  handwritten V
    n("A Tragedy Has Occurred"),  # 9  Tragedy
    n("Ultimatum"),  # 10
    n("Don't Do That Again", True),  # 11  handwritten V
    n("Battle Plan"),  # 12
]

LS_ADD = [
    n("The Professor"),  # 1
    n("Let's Keep A Little Optimism Here", True),  # 2  Optimism; handwritten V
    n("Wise Advice"),  # 3
]


# --- Dark: d2p3_p06.png upright. Name blank. Court / Cloud City. ---

DS_RESERVE = [
    n("Court Of The Vile Gangster / I Shall Enjoy Watching You Die"),  # 1  CT
    n("Cloud City: Carbonite Chamber"),  # 2  CC Carbonite Chamber
    n("Cloud City: Security Tower", True),  # 3  handwritten V
    n("Carbonite Chamber Console", True),  # 4  handwritten V
    n("Jabba's Prize"),  # 5
    n("Any Methods Necessary"),  # 6
    n("IG-88", True),  # 7  handwritten V
    n("IG-88 With Blaster Rifle", True),  # 8  IG-88 w/ Blaster; handwritten V
    n("Jabba's Palace: Dungeon"),  # 9
    n("Despair", True),  # 10  handwritten V
    n("Death Star"),  # 11
    n("Kashyyyk"),  # 12
    n("Jabba's Palace: Audience Chamber"),  # 13  Aud Ch
    n("Slave I, Symbol Of Fear"),  # 14  Slave I SoF
    n("Victory"),  # 15
    n(None),  # 16  He's All Yours, Bounty Hunter fully crossed
    n("To The Emperor", True),  # 17  handwritten V
    n("To The Emperor", True),  # 18  ditto
    n("Count Dooku"),  # 19
    n("Darth Maul With Lightsaber"),  # 20  Darth Maul with LS
    n("Darth Vader With Lightsaber"),  # 21  EPP Vader
    n("Grand Admiral Thrawn"),  # 22
    n("Grand Moff Tarkin", True),  # 23  handwritten V
    n("Arica"),  # 24
    n("4-LOM With Concussion Rifle"),  # 25  4-LOM w/ TCR
    n("Prince Xizor"),  # 26
    n("Dengar With Blaster Carbine", True),  # 27  EPP Dengar; handwritten V
    n("Boba Fett, Prepared Hunter"),  # 28
    n("Garindan", True),  # 29  handwritten V
    n("Jango Fett, The Assassin"),  # 30
    n("Reegesk", True),  # 31  handwritten V
    n("P-59"),  # 32
    n("U-3PO"),  # 33
    n("4-LOM With Concussion Rifle", True),  # 34  EPP 4-LOM; handwritten V
    n("First Strike"),  # 35
    n("Jabba's Haven"),  # 36
    n("Lateral Damage"),  # 37
    n("Ni Chuba Na??", True),  # 38  Ni Chuba Na; handwritten V
    n("Imperial Justice", True),  # 39  handwritten V
    n("Force Lightning"),  # 40
    n("Force Lightning"),  # 41  ditto
    n("Imperial Barrier"),  # 42
    n("Imperial Barrier"),  # 43  ditto
    n("Stunning Leader"),  # 44
    n("Stunning Leader"),  # 45  ditto
    n("Masterful Move"),  # 46
    n("Monnok"),  # 47
    n("Ghhhk"),  # 48
    n("Sonic Bombardment", True),  # 49  handwritten V
    n("A Dark Time For The Rebellion", True),  # 50  handwritten V
    n("Defensive Fire", True),  # 51  handwritten V
    n("Short Range Fighters & Watch Your Back!"),  # 52  Short Range Fighters combo
    n("Cold Feet", True),  # 53  handwritten V
    n("Imperial Artillery"),  # 54
    n("Sense"),  # 55
    n("Imbalance & Kintan Strider"),  # 56  Imbalance combo
    n("Control & Set For Stun"),  # 57  Control combo
    n("Close Call", True),  # 58  handwritten V
    n("Nute Gunray"),  # 59  written Never Valiant
    n("Knowledge And Defense", True),  # 60  K&D; handwritten V
]

DS_SHIELDS = [
    n("Secret Plans"),  # 1
    n("Come Here You Big Coward"),  # 2  Coward
    n("Allegations Of Corruption"),  # 3  Allegations
    n("Abyss", True),  # 4  handwritten V
    n("You Cannot Hide Forever", True),  # 5  handwritten V
    n("Battle Order"),  # 6
    n("Resistance"),  # 7
    n("A Useless Gesture"),  # 8
    n("Do They Have A Code Clearance?", True),  # 9  Code Clearance; handwritten V
    n("We'll Let Fate-a Decide, Huh?"),  # 10  Fate-a Decide
    n("Oppressive Enforcement"),  # 11
    n("Fanfare", True),  # 12  handwritten V
]

DS_ADD = [
    n("Firepower", True),  # 1  handwritten V
    n("Imperial Detention"),  # 2
    n("There Is No Try"),  # 3
    n("Oh, Switch Off"),  # 5  slot 4 blank
    n("Imperial Propaganda", True),  # 6  handwritten V
]

LS_UNREAD = [12]
DS_UNREAD = [16]
NO_DEST = [
    "Chewie With Bowcaster",
    "Jabba's Prize",  # Dark list; dests Light-only
    "IG-88 With Blaster Rifle",
    "To The Emperor",
]

NOTES = """
Mean Jespar Mix / rlx, 2014 Worlds Day 2, 2010 form.
Light d2p3_p05 (LIGHT/DARK unchecked). Name as written; deck name blank.
Dark d2p3_p06 name/side/deck blank; Court of the Vile Gangster / Cloud City.
Likely pair with p05.

LS: (V) boxes empty; handwritten V beside titles counted as is_v.
Line 8 Anakin's Podracer (written like Andies Palace).
Line 12 unread location (colon + long subtitle; not guessed).
Line 24 EPP Chewie = Chewie With Bowcaster.
Line 29 Chewie + V taken as Chewie, Enraged (V) (separate from 24).
Line 52 SATM combo = Sorry About The Mess & Blaster Proficiency.
Shield 2 Jabba's Prize in the shield box (not a shield printing).

DS: p06 name box blank (PLAYER None); likely pair with p05.
Line 16 He's All Yours, Bounty Hunter fully crossed, no replacement.
Line 59 Nute Gunray (scrawl Never Valiant).
NO_DEST remaining: Chewie With Bowcaster (SE; not in 2014 dests),
Dark Jabba's Prize (Light card), IG-88 With Blaster Rifle, To The Emperor.
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
    assert len(LS_SHIELDS) == 12, len(LS_SHIELDS)
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
    print("DS", DS_PLAYER, DS_SIDE, len(DS_RESERVE), len(DS_SHIELDS), "unread", DS_UNREAD)
    print("NO_DEST", miss or "none")
