#!/usr/bin/env python3
"""Nick Reisch, 2014 Worlds Day 2. Typed Holotable dump.

Dark Have Gun, Will Travel: extract/day2_upright/d2p3_p13.png (Part 3 MUST use upright).
Light Communing / It's The Future You See: extract/day2_upright/d2p3_p14.png.
"""
from __future__ import annotations

PLAYER = "Nick Reisch"
USERNAME = ""
KIND = "type_groups"

# --- Dark CCT ---
DS_DECK_NAME = "Have Gun, Will Travel!"
DS_SIDE = "Dark"
DS_SCAN = "extract/day2_upright/d2p3_p13.png"
DS_PDF = "2014 Worlds Day 2 Part 3.pdf"
DS_PDF_PAGE = 13
DS_STARTING = ("Carbon Chamber Testing / My Favorite Decoration", False)

DS_GROUPS = [
    ("Objective", [
        (1, "Carbon Chamber Testing / My Favorite Decoration", False),
    ]),
    ("Character", [
        (1, "Emperor Palpatine", False),
        (8, "Imperial Stormtrooper", False),
        (1, "Darth Vader, Betrayer Of The Jedi", False),  # sheet Darth Vader, Betrayer
        (1, "Darth Vader, Dark Lord Of The Sith", False),
        (3, "Elite Squadron Stormtrooper (V)", True),
    ]),
    ("Defensive shield", [
        (1, "I Find Your Lack Of Faith Disturbing (V)", True),
        (1, "You Cannot Hide Forever (V)", True),
        (1, "We'll Let Fate-a Decide, Huh? (V)", True),  # sheet We'll Let Fate Decide (V)
        (1, "A Useless Gesture (V)", True),
        (1, "Leave Them To Me (V)", True),
        (1, "After Her! (V)", True),  # sheet After Her (V)
        (1, "Resistance", False),
        (1, "Oppressive Enforcement", False),
        (1, "Imperial Detention (V)", True),
        (1, "Come Here You Big Coward", False),
        (1, "Battle Order", False),
        (1, "Secret Plans", False),
        (1, "Allegations Of Corruption", False),
        (1, "Abyss (V)", True),
        (1, "Firepower (V)", True),
    ]),
    ("Device", [
        (1, "Carbonite Chamber Console (V)", True),  # sheet Carbon Chamber Console (V)
    ]),
    ("Effect", [
        (1, "Special Delivery (V)", True),
        (1, "Imperial Stockpile", False),
        (1, "Imperial Academy Training (V)", True),
        (1, "Ni Chuba Na?? (V)", True),  # sheet Ni Chuba Na (V)
        (1, "Imperial Domination (V)", True),
        (1, "Presence Of The Force", False),
        (1, "Search And Destroy", False),
        (1, "Crush The Rebellion", False),
        (1, "Forced Servitude (V)", True),
        (1, "Strategic Reserves (V)", True),
        (1, "Knowledge And Defense (V)", True),
    ]),
    ("Interrupt", [
        (1, "According To My Design", False),
        (1, "Breached Defenses & Molator", False),  # sheet Molitor
        (2, "Voyeur (V)", True),
        (1, "Force Lightning", False),
        (3, "Sense", False),
        (2, "Coordinated Attack (V)", True),
        (3, "Blast Points", False),
        (3, "Defensive Fire (V)", True),
        (3, "A Dark Time For The Rebellion (V)", True),
        (1, "Lightsaber Deficiency (V)", True),
        (2, "Ghhhk & Those Rebels Won't Escape Us", False),
        (1, "Evader & Monnok", False),
        (2, "Wounded Warrior", False),
        (2, "Trooper Assault", False),
        (2, "Imperial Artillery", False),
    ]),
    ("Location", [
        (1, "Cloud City Prison (V)", True),  # as written; no dest expected
        (1, "Cloud City: Carbonite Chamber", False),  # sheet Cloud City: Carbon Chamber
        (1, "Jabba's Palace: Audience Chamber", False),
    ]),
    ("Weapon", [
        (1, "Blaster Rifle (V)", True),
    ]),
]

DS_NOTES = (
    "Upright scan extract/day2_upright/d2p3_p13.png (source page inverted in Part 3). "
    "Header Nick Reisch-DS 'Have Gun, Will Travel'. Objective expanded to "
    "Carbon Chamber Testing / My Favorite Decoration. "
    "Cloud City Prison (V) as written (no matching title; not invented as Security Tower). "
    "Carbon Chamber Console (V) → Carbonite Chamber Console (V). "
    "Breached Defenses & Molitor → Molator. Ni Chuba Na (V) → Ni Chuba Na?? (V). "
    "We'll Let Fate Decide (V) → We'll Let Fate-a Decide, Huh? (V). "
    "After Her (V) → After Her! (V). Darth Vader, Betrayer → Betrayer Of The Jedi. "
    "Shield block has a 16th line Blaster Rifle (V) already in reserve; omitted from shields. "
    "Voyeur listed as two lines (not (x2)). Reserve qty 60 excluding shields."
)
DS_UNREAD: list[int] = []
DS_NO_DEST = ["Cloud City Prison (V)"]

# --- Light IITFYS / Communing ---
LS_DECK_NAME = "Communing"
LS_SIDE = "Light"
LS_SCAN = "extract/day2_upright/d2p3_p14.png"
LS_PDF = "2014 Worlds Day 2 Part 3.pdf"
LS_PDF_PAGE = 14
LS_STARTING = ("It Is The Future You See (V)", True)

LS_GROUPS = [
    ("Character", [
        (1, "Admiral Ackbar (V)", True),
        (1, "Corran Horn", False),
        (2, "Luke Skywalker, Jedi Knight", False),
        (1, "Leia, Rebel Princess", False),
        (2, "Master Qui-Gon (V)", True),
        (1, "Mace Windu, Master Of The Order", False),
        (1, "Mace Windu, Master Of The Order (V)", True),  # sheet (V) MOTO
        (2, "Luke Skywalker, Strong In The Force", False),  # sheet SITF
        (1, "Lando Calrissian, Unlikely Hero", False),  # sheet UH
        (1, "Mace Windu, Master Of The Order", False),  # Down With The Emperor (V) replaced
    ]),
    ("Defensive shield", [
        (1, "Jabba's Prize", False),  # Let's Keep A Little Optimism Here (V) crossed
        (1, "Don't Do That Again (V)", True),
        (1, "Your Insight Serves You Well (V)", True),
        (1, "The Professor (V)", True),
        (1, "Weapons Display (V)", True),
        (1, "Simple Tricks And Nonsense (V)", True),  # sheet (V)
        (1, "Aim High", False),
        (1, "A Tragedy Has Occurred", False),
        (1, "Ultimatum", False),
        (1, "Yavin Sentry (V)", True),  # sheet Yavin 4 Sentry (V)
        (1, "There Is Another", False),  # Battle Plan crossed
        (1, "Affect Mind (V)", True),  # Do, Or Do Not crossed
        (1, "He Can Go About His Business (V)", True),
        (1, "Chasm (V)", True),
        (1, "Only Jedi Carry That Weapon", False),
    ]),
    ("Effect", [
        (1, "Quick Draw (V)", True),
        (1, "Seeking An Audience (V)", True),
        (1, "Strikeforce (V)", True),
        (1, "Imperial Atrocity (V)", True),
        (1, "Anger, Fear, Aggression (V)", True),  # sheet Agression
        (1, "Sai'torr Kal Fas (V)", True),
    ]),
    ("Epic Event", [
        (1, "It Is The Future You See (V)", True),
    ]),
    ("Interrupt", [
        (1, "Do, Or Do Not & Wise Advice", False),
        (1, "Battle Plan & Draw Their Fire", False),
        (3, "Rebel Leadership (V)", True),
        (3, "Wesa Gotta Grand Army", False),
        (2, "Let The Wookiee Win (V)", True),
        (1, "Antilles Maneuver & Rebel Reinforcements", False),
        (1, "Hear Me Baby, Hold Together (V)", True),
        (1, "Weapon Levitation", False),
        (1, "Jedi Levitation (V)", True),
        (1, "Blaster Deflection", False),
        (1, "Clash Of Sabers", False),
        (1, "Sorry About The Mess & Blaster Proficiency", False),
        (2, "Escape Pod (V)", True),
        (2, "A Jedi's Resilience", False),
        (2, "Speak With The Jedi Council", False),
        (1, "Houjix", False),  # Jedi's Lightsaber (V) crossed
        (1, "What're You Tryin' To Push On Us?", False),
        (1, "Mechanical Failure", False),
    ]),
    ("Location", [
        (1, "Dagobah: Yoda's Hut", False),
        (1, "Naboo: Battle Plains", False),
        (1, "Naboo: Boss Nass' Chambers", False),
        (1, "Yavin 4: Massassi War Room (V)", True),
        (1, "Home One: War Room", False),
        (1, "Coruscant: Jedi Council Chamber (V)", True),  # sheet Chambers
    ]),
    ("Starship", [
        (1, "Home One", False),
        (1, "Han, Chewie, And The Falcon (V)", True),
        (1, "Lady Luck", False),  # sheet Lando's Luxury Yacht
        (2, "Artoo-Detoo In Red 5", False),
    ]),
    ("Weapon", [
        (1, "Anakin's Lightsaber", False),  # Jedi Lightsaber (V) crossed
        (1, "Qui-Gon's Lightsaber", False),  # sheet (Ref III)
        (1, "Luke's Lightsaber", False),
    ]),
]

LS_NOTES = (
    "Upright scan extract/day2_upright/d2p3_p14.png. Header 'Nick Reisch LS' plus "
    "handwritten Comm (V) / Somm (V); list is It's The Future You See, not a Communing "
    "card in the 60. Jedi Lightsaber (V) → Anakin's Lightsaber; Jedi's Lightsaber (V) → "
    "Houjix; Down With The Emperor (V) → Mace Windu, Master Of The Order (third copy). "
    "Lando's Luxury Yacht → Lady Luck. SITF → Luke Skywalker, Strong In The Force. "
    "UH → Lando Calrissian, Unlikely Hero. MOTO → Mace Windu, Master Of The Order. "
    "Shields: Let's Keep crossed for Jabba's Prize; Battle Plan → There Is Another; "
    "Do, Or Do Not → Affect Mind (V). Yavin 4 Sentry (V) → Yavin Sentry (V). "
    "Simple Tricks And Nonsense typed with (V). Reserve qty 60 excluding shields."
)
LS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []

SIDE = None
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
        f"transcribe_nick_reisch.py  {PLAYER}\n"
        f"  Dark  {DS_DECK_NAME}  reserve={_qty(DS_GROUPS)}  shields={_shields(DS_GROUPS)}  "
        f"unread={DS_UNREAD}  no_dest={DS_NO_DEST}\n"
        f"  Light {LS_DECK_NAME}  reserve={_qty(LS_GROUPS)}  shields={_shields(LS_GROUPS)}  "
        f"unread={LS_UNREAD}  no_dest={LS_NO_DEST}"
    )
