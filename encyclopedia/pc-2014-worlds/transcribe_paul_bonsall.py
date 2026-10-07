#!/usr/bin/env python3
"""Paul Bonsall, 2014 Worlds Day 2. Typed Holotable (two pages per side).

Dark: Kessel CR(V) — extract/day2/d2p1_p01.png + d2p1_p02.png.
Light: Communing (Rebel Scout Luke and Saber) — d2p1_p03.png + d2p1_p04.png.
Uniqueness stars stripped. (V) from typed '(V)'. (xN) is qty.
(1 starting) noted; cards still listed. No Objective heading on either printout.
"""
from __future__ import annotations

PLAYER = "Paul Bonsall"
USERNAME = ""
KIND = "type_groups"

# --- Dark: Kessel CR(V) ---
DS_DECK_NAME = "Kessel CR(V)"
DS_SIDE = "Dark"
DS_SCAN = "extract/day2/d2p1_p01.png"
DS_SCAN2 = "extract/day2/d2p1_p02.png"
DS_PDF = "2014 Worlds Day 2 Part 1.pdf"
DS_PDF_PAGE = 1
DS_PDF_PAGE2 = 2
# Printout has no Objective; unique start-of-game is I'll Take Them Myself
# with Kessel + Administrator's Office. Deck title CR(V) = Combat Readiness (V).
DS_STARTING = ("I'll Take Them Myself", False)

DS_GROUPS = [
    ("Character", [
        (1, "Boba Fett, Prepared Hunter", False),
        (1, "Dr. Evazan & Ponda Baba", False),
        (1, "Moruth Doole, Kessel Administrator", False),
        (1, "Jango Fett, The Assassin", False),
        (1, "Garindan (V)", True),
        (1, "Dengar With Blaster Carbine (V)", True),
        (2, "Count Dooku", False),
        (2, "Emperor Palpatine", False),
        (1, "P-59", False),
        (1, "Darth Vader, Betrayer Of The Jedi", False),
        (1, "Darth Vader, Dark Lord Of The Sith", False),
        (2, "Darth Maul With Lightsaber", False),
        (2, "Galen Marek, Starkiller", False),
    ]),
    ("Defensive shield", [
        (1, "Battle Order", False),
        (1, "Abyss (V)", True),
        (1, "Allegations Of Corruption", False),
        (1, "A Useless Gesture (V)", True),
        (1, "You Cannot Hide Forever (V)", True),
        (1, "Weapon Of A Sith", False),
        (1, "Fanfare (V)", True),
        (1, "Firepower (V)", True),
        (1, "I Find Your Lack Of Faith Disturbing (V)", True),
        (1, "Imperial Detention", False),
        (1, "Death Star Sentry (V)", True),
        (1, "Come Here You Big Coward", False),
        (1, "Secret Plans", False),
        (1, "There Is No Try", False),
        (1, "Resistance", False),
    ]),
    ("Device", [
        (1, "Kessel Surveillance System", False),
    ]),
    ("Effect", [
        (1, "I'll Take Them Myself", False),
        (1, "Imperial Justice (V)", True),
        (1, "Blaster Rack (V)", True),
        (1, "Gift Of The Master", False),
        (1, "Ni Chuba Na?? (V)", True),
        (1, "Wipe Them Out, All Of Them (V)", True),
        (1, "Blast Door Controls", False),
        (1, "Knowledge And Defense (V)", True),
    ]),
    ("Interrupt", [
        (1, "Ghhhk", False),
        (1, "Sniper & Dark Strike", False),
        (1, "Force Push (V)", True),
        (1, "Combat Readiness (V)", True),
        (1, "Sith Fury & End This Destructive Conflict", False),
        (1, "Why Didn't You Tell Me? (V)", True),
        (1, "Dark Maneuvers", False),
        (1, "A Dark Time For The Rebellion (V)", True),
        (1, "Stop Motion (V)", True),
        (1, "Sense", False),
        (1, "Blow Parried", False),
        (2, "Sonic Bombardment (V)", True),
        (1, "Masterful Move & Endor Occupation", False),
        (1, "Cold Feet (V)", True),
        (2, "Short Range Fighters & Watch Your Back!", False),
        (2, "Force Lightning", False),
        (1, "Monnok", False),
        (2, "Force Field (V)", True),  # page 2 continuation
    ]),
    ("Location", [
        (1, "Cloud City: Security Tower (V)", True),
        (1, "Kessel: Spice Mines - Administrator's Office", False),
        (1, "Kessel: Spice Mines - Extraction Facility", False),
        (1, "Kessel: Spice Mines - Prison", False),
        (1, "Kessel", False),
    ]),
    ("Mission", [
        (1, "Spice Mine Operations", False),
    ]),
    ("Starship", [
        (1, "Maul's Sith Infiltrator", False),
        (1, "Slave I, Symbol Of Fear", False),
    ]),
    ("Vehicle", [
        (1, "Blizzard 4", False),
    ]),
    ("Weapon", [
        (1, "Galen's Lightsaber, Vader's Gift", False),
        (1, "Dooku's Lightsaber", False),
        (1, "Vader's Lightsaber", False),
    ]),
]

DS_NOTES = (
    "Typed Holotable 'Dark - Kessel CR(V)'; handwritten 'Paul Bonsall Worlds'. "
    "No Objective heading. (1 starting): I'll Take Them Myself, Gift Of The Master, "
    "Ni Chuba Na?? (V), Knowledge And Defense (V), Combat Readiness (V), "
    "Kessel: Spice Mines - Administrator's Office, Kessel, plus all 15 shields. "
    "Force Field (V) (x2) is the first line of page 2 (interrupt continuation). "
    "Reserve qty 60 excluding Defensive shield."
)
DS_UNREAD: list[int] = []
DS_NO_DEST: list[str] = []

# --- Light: Communing (Rebel Scout Luke and Saber) ---
LS_DECK_NAME = "Communing (Rebel Scout Luke and Saber)"
LS_SIDE = "Light"
LS_SCAN = "extract/day2/d2p1_p03.png"
LS_SCAN2 = "extract/day2/d2p1_p04.png"
LS_PDF = "2014 Worlds Day 2 Part 1.pdf"
LS_PDF_PAGE = 3
LS_PDF_PAGE2 = 4
LS_STARTING = ("Communing", False)

LS_GROUPS = [
    ("Character", [
        (1, "Shmi Skywalker", False),
        (1, "Threepio With His Parts Showing", False),
        (1, "Yoda, Great Warrior", False),
        (1, "Jaina Solo", False),
        (3, "Luke Skywalker, Rebel Scout (V)", True),
        (1, "Admiral Ackbar (V)", True),
        (2, "Chewie, Enraged (V)", True),
        (1, "Chewbacca, Protector", False),
        (1, "Corran Horn", False),
        (1, "Master Kenobi", False),
        (1, "Wedge Antilles, Red Squadron Leader", False),
        (1, "Han With Heavy Blaster Pistol", False),
        (1, "Lando Calrissian, Scoundrel (V)", True),
        (1, "Leia, Rebel Princess", False),
        (1, "Padme Naberrie (V)", True),
        (2, "Anakin Skywalker, Padawan Learner", False),
    ]),
    ("Defensive shield", [
        (1, "Your Insight Serves You Well (V)", True),
        (1, "Wise Advice", False),
        (1, "Weapons Display (V)", True),
        (1, "Do, Or Do Not", False),
        (1, "Chasm (V)", True),
        (1, "Battle Plan", False),
        (1, "Aim High", False),
        (1, "Don't Do That Again (V)", True),
        (1, "He Can Go About His Business (V)", True),
        (1, "Only Jedi Carry That Weapon", False),
        (1, "Ultimatum", False),
        (1, "The Professor (V)", True),
        (1, "Simple Tricks And Nonsense", False),
        (1, "Planetary Defenses (V)", True),
        (1, "A Tragedy Has Occurred", False),
    ]),
    ("Effect", [
        (1, "Wokling (V)", True),
        (1, "K'lor'slug (V)", True),
        (1, "Quick Draw (V)", True),
        (1, "Evacuation Control (V)", True),
        (1, "Rebel Gunrunner", False),
        (1, "Sai'torr Kal Fas (V)", True),
        (1, "Seeking An Audience (V)", True),
        (1, "Imperial Atrocity (V)", True),
        (1, "A Gift", False),
        (1, "Anger, Fear, Aggression (V)", True),
    ]),
    ("Epic Event", [
        (1, "Communing", False),
    ]),
    ("Interrupt", [
        (2, "A Jedi's Resilience", False),
        (1, "Houjix", False),
        (2, "Rebel Leadership (V)", True),
        (2, "Escape Pod (V)", True),
        (1, "Desperate Reach (V)", True),
        (1, "Inconsequential Barriers", False),
        (1, "Hear Me Baby, Hold Together (V)", True),
        (2, "Use The Force", False),
        (2, "Run Luke, Run! (V)", True),
        (1, "Grimtaash", False),
        (1, "Sorry About The Mess & Blaster Proficiency", False),
        (1, "Antilles Maneuver & Rebel Reinforcements", False),
        (1, "Out Of Commission & Transmission Terminated", False),  # page 2
        (1, "Let The Wookiee Win (V)", True),  # page 2
    ]),
    ("Location", [
        (1, "Tatooine: Slave Quarters", False),
        (1, "Jabba's Palace: Audience Chamber", False),
        (1, "Home One: War Room", False),
        (1, "Tatooine: Obi-Wan's Hut (V)", True),
        (1, "Tatooine", False),
    ]),
    ("Starship", [
        (1, "Home One", False),
        (1, "Artoo-Detoo In Red 5", False),
    ]),
    ("Weapon", [
        (1, "Luke's Lightsaber", False),
        (1, "Anakin's Lightsaber", False),
        (1, "Chewbacca's Bowcaster", False),
    ]),
]

LS_NOTES = (
    "Typed Holotable 'Light - Communing (Rebel Scout Luke and Saber)'; "
    "handwritten 'Paul Bonsall Worlds'. No Objective heading. "
    "(1 starting): Master Kenobi, Wokling (V), Quick Draw (V), "
    "Anger, Fear, Aggression (V), Communing, Tatooine: Slave Quarters, plus all 15 shields. "
    "Page 2 continues interrupts then Location / Starship / Weapon. "
    "Reserve qty 60 excluding Defensive shield."
)
LS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []

# Aliases the contract names.
SIDE = None  # both sides in this file
GROUPS = None
SCAN = DS_SCAN
PDF = DS_PDF
STARTING = DS_STARTING
NOTES = DS_NOTES
UNREAD = DS_UNREAD
NO_DEST = DS_NO_DEST

_SKIP_HEADINGS = {"Defensive shield", "Hidden Fortress"}


def _qty(groups: list) -> int:
    return sum(
        q
        for heading, cards in groups
        if heading not in _SKIP_HEADINGS
        for q, _n, _v in cards
    )


def _shields(groups: list) -> int:
    return sum(
        q
        for heading, cards in groups
        if heading == "Defensive shield"
        for q, _n, _v in cards
    )


if __name__ == "__main__":
    print(
        f"transcribe_paul_bonsall.py  {PLAYER}\n"
        f"  Dark  {DS_DECK_NAME}  reserve={_qty(DS_GROUPS)}  shields={_shields(DS_GROUPS)}  "
        f"unread={DS_UNREAD}  no_dest={DS_NO_DEST}\n"
        f"  Light {LS_DECK_NAME}  reserve={_qty(LS_GROUPS)}  shields={_shields(LS_GROUPS)}  "
        f"unread={LS_UNREAD}  no_dest={LS_NO_DEST}"
    )
