#!/usr/bin/env python3
"""Philippe Dubreuil, 2014 Worlds Day 2. Typed Holotable dump.

Light worlds day 2 light[1]: extract/day2/d2p2_p13.png + p14
  (handwritten Yavin 4 Sentry (V) on page 2).
Dark Worlds Day 2 ASM 1.5: d2p2_p15.png + p16
  (Fanfare crossed; Death Star Sentry (V) added).
"""
from __future__ import annotations

PLAYER = "Philippe Dubreuil"
USERNAME = ""
KIND = "type_groups"

# --- Light ---
LS_DECK_NAME = "worlds day 2 light[1]"
LS_SIDE = "Light"
LS_SCAN = "extract/day2/d2p2_p13.png"
LS_SCAN2 = "extract/day2/d2p2_p14.png"
LS_PDF = "2014 Worlds Day 2 Part 2.pdf"
LS_PDF_PAGE = 13
LS_PDF_PAGE2 = 14
LS_STARTING = ("Infiltration / Unlikely Allies", False)

LS_GROUPS = [
    ("Objective", [
        (1, "Infiltration / Unlikely Allies", False),
    ]),
    ("Character", [
        (1, "Mirax Terrik", False),
        (2, "Boushh", False),
        (2, "Han Solo, Innocent Scoundrel", False),
        (2, "Lando Calrissian, Scoundrel (V)", True),
        (2, "Corran Horn", False),
        (1, "Redeemed Apprentice", False),
        (1, "Kyle Katarn", False),  # plus AI copy below
        (1, "Kyle Katarn", False),  # sheet Kyle Katarn (AI)
        (1, "Tanus Spijek (V)", True),
    ]),
    ("Defensive shield", [
        (1, "Chasm (V)", True),
        (1, "A Tragedy Has Occurred", False),
        (1, "Battle Plan", False),
        (1, "Don't Do That Again (V)", True),
        (1, "Aim High", False),
        (1, "Wise Advice", False),
        (1, "Jabba's Prize", False),  # typed Jabba's Prize/Jabba's Prize in shield block
        (1, "Affect Mind (V)", True),
        (1, "Simple Tricks And Nonsense", False),
        (1, "The Professor (V)", True),
        (1, "Ultimatum", False),
        (1, "Weapons Display (V)", True),
        (1, "Your Insight Serves You Well (Death Star II) (V)", True),
        (1, "He Can Go About His Business", False),
        (1, "Yavin Sentry (V)", True),  # handwritten Yavin 4 Sentry (V)
    ]),
    ("Effect", [
        (1, "Anger, Fear, Aggression (V)", True),
        (1, "Menace Fades", False),
        (2, "Imperial Atrocity (V)", True),
        (1, "Spaceport Scoundrels Guild", False),
        (1, "Much to Learn, You Still Have", False),
        (1, "Flash Of Insight (V)", True),
        (1, "Scoundrel's Luck", False),
        (1, "Scoundrel's Ingenuity", False),
        (1, "Scoundrel's Charm", False),
        (1, "Scoundrel's Bravado", False),
        (1, "I Can't Believe He's Gone (V)", True),
        (1, "Sai'torr Kal Fas (V)", True),
        (1, "A Good Blaster At Your Side", False),
        (1, "Wokling (V)", True),
        (1, "Imperial Navigation Charts", False),
    ]),
    ("Interrupt", [
        (1, "This Is More Like It (V)", True),
        (1, "Too Close For Comfort", False),
        (1, "Let The Wookiee Win (V)", True),
        (1, "Corellian Retort (V)", True),
        (1, "Dark Approach (V)", True),
        (1, "Heading For The Medical Frigate", False),
        (1, "Starship Levitation (V)", True),
        (1, "Antilles Maneuver & Rebel Reinforcements", False),
        (1, "Double Agent", False),
        (1, "Sorry About The Mess & Blaster Proficiency", False),
        (1, "Jedi Levitation (V)", True),
        (1, "Sabotage (V)", True),
        (1, "Blast The Door, Kid!", False),
        (2, "Out Of Commission & Transmission Terminated", False),
        (2, "We Wish To Board At Once", False),
        (1, "Dodge", False),
    ]),
    ("Location", [
        (1, "Nar Shaddaa: Undercity Street", False),
        (1, "Nar Shaddaa: Undercity", False),
        (1, "Nar Shaddaa: Scoundrel's Rest", False),
        (1, "Nar Shaddaa", False),
    ]),
    ("Starship", [
        (1, "Lady Luck", False),
        (1, "Errant Venture", False),  # sheet Errant Venture (AI)
        (1, "Errant Venture", False),
        (1, "Booster In Pulsar Skate", False),
        (1, "Obi-Wan In Radiant VII", False),
    ]),
    ("Weapon", [
        (1, "Han's Blaster, So Uncivilized", False),
        (1, "Leia's Sporting Blaster (V)", True),
        (1, "Kyle Katarn's Blaster Rifle", False),
    ]),
]

LS_NOTES = (
    "Typed Holotable 'worlds day 2 light[1]'; handwritten Philippe Dubreuil Day 2 Light. "
    "Jabba's Prize/Jabba's Prize sits in the shield block (Light shield, not the Dark "
    "character). Page 2: A Good Blaster At Your Side, Wokling (V), Imperial Navigation "
    "Charts, Infiltration/Unlikely Allies, plus handwritten 'Yavin 4 Sentry (V)' "
    "(card is Yavin Sentry (V)). Kyle Katarn and Errant Venture each have an (AI) copy. "
    "He Can Go About His Business has no typed (V). Reserve qty 60 excluding shields."
)
LS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []

# --- Dark ASM 1.5 ---
DS_DECK_NAME = "Worlds Day 2 ASM 1.5[1]"
DS_SIDE = "Dark"
DS_SCAN = "extract/day2/d2p2_p15.png"
DS_SCAN2 = "extract/day2/d2p2_p16.png"
DS_PDF = "2014 Worlds Day 2 Part 2.pdf"
DS_PDF_PAGE = 15
DS_PDF_PAGE2 = 16
DS_STARTING = ("A Stunning Move / A Valuable Hostage", False)

DS_GROUPS = [
    ("Objective", [
        (1, "A Stunning Move / A Valuable Hostage", False),
    ]),
    ("Character", [
        (1, "Jango Fett, The Assassin", False),  # sheet (AI)
        (1, "Boba Fett, Prepared Hunter", False),
        (2, "Galen Marek, Starkiller", False),  # sheet (AI)
        (2, "IG-100 MagnaGuard", False),
        (1, "4-LOM With Concussion Rifle (V)", True),
        (1, "Dr. Evazan & Ponda Baba", False),
        (1, "P-59", False),
        (2, "Grievous, Hunter Of Jedi", False),
        (2, "Count Dooku", False),
        (1, "Lord Maul", False),
        (2, "Darth Maul, Young Apprentice", False),
        (1, "Battle Droid Squad", False),
    ]),
    ("Defensive shield", [
        (1, "You Cannot Hide Forever (V)", True),
        (1, "Weapon Of A Sith", False),
        (1, "Secret Plans", False),
        (1, "Resistance", False),
        (1, "Oppressive Enforcement", False),
        (1, "I Find Your Lack Of Faith Disturbing (V)", True),
        (1, "Imperial Detention", False),
        (1, "Firepower (V)", True),
        (1, "Death Star Sentry (V)", True),  # Fanfare (V) crossed
        (1, "Do They Have A Code Clearance? (V)", True),
        (1, "Come Here You Big Coward", False),
        (1, "Battle Order", False),
        (1, "Allegations Of Corruption", False),
        (1, "A Useless Gesture (V)", True),
        (1, "Abyss (V)", True),
    ]),
    ("Effect", [
        (1, "Gift Of The Master", False),
        (1, "Blaster Rack (V)", True),
        (1, "No Escape", False),
        (1, "Crush The Rebellion", False),
        (1, "Jabba's Haven", False),
        (1, "Ability, Ability, Ability (V)", True),
        (1, "Imperial Propaganda (V)", True),
        (1, "The Phantom Menace", False),  # sheet (AI)
        (1, "Imperial Decree (V)", True),
        (1, "Knowledge And Defense (V)", True),
    ]),
    ("Epic Event", [
        (1, "Insidious Prisoner", False),
    ]),
    ("Interrupt", [
        (1, "Sith Fury (V)", True),
        (1, "Prepared Defenses (V)", True),
        (1, "Maul Strikes", False),
        (1, "I Have You Now", False),
        (1, "Evader & Monnok", False),
        (1, "Oh, Switch Off", False),
        (1, "Operational As Planned (V)", True),
        (1, "Cold Feet (V)", True),
        (1, "Sniper & Dark Strike", False),
        (1, "Ghhhk & Those Rebels Won't Escape Us", False),
        (1, "Force Lightning", False),
        (1, "You Are Beaten", False),
        (2, "Force Field (V)", True),
        (1, "Lightsaber Deficiency (V)", True),
        (1, "Stop Motion (V)", True),
        (2, "Sonic Bombardment (V)", True),
        (1, "Short Range Fighters & Watch Your Back!", False),
        (1, "Control", False),
    ]),
    ("Location", [
        (1, "Cloud City: Security Tower (V)", True),
        (1, "Nal Hutta", False),
        (1, "Blockade Flagship: Docking Bay", False),
        (1, "Blockade Flagship: Bridge", False),
        (1, "Coruscant: Palpatine's Quarters", False),
        (1, "Coruscant: Private Platform (Docking Bay)", False),
    ]),
    ("Starship", [
        (1, "Slave I, Symbol Of Fear", False),
    ]),
    ("Weapon", [
        (1, "Galen's Lightsaber, Vader's Gift", False),
        (1, "Dark Jedi Lightsaber (V)", True),
        (1, "Dooku's Lightsaber", False),
        (1, "Maul's Double-Bladed Lightsaber", False),
    ]),
]

DS_NOTES = (
    "Typed Holotable 'Worlds Day 2 ASM 1.5[1]'; handwritten Philippe Dubreuil Day 2 Dark. "
    "Fanfare (V) (1 starting) crossed out; Death Star Sentry (V) written in. "
    "Page 2 is the remaining starting shields. (AI) on Jango Fett The Assassin, "
    "Galen Marek Starkiller, and The Phantom Menace — uniqueness stars / AI flags "
    "stripped. MagnaGuard printed with triple-star. Reserve qty 60 excluding shields."
)
DS_UNREAD: list[int] = []
DS_NO_DEST: list[str] = []

SIDE = None
GROUPS = None
SCAN = LS_SCAN
PDF = LS_PDF
STARTING = LS_STARTING
NOTES = LS_NOTES
UNREAD = LS_UNREAD
NO_DEST = LS_NO_DEST

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
        f"transcribe_philippe_dubreuil.py  {PLAYER}\n"
        f"  Light {LS_DECK_NAME}  reserve={_qty(LS_GROUPS)}  shields={_shields(LS_GROUPS)}  "
        f"unread={LS_UNREAD}  no_dest={LS_NO_DEST}\n"
        f"  Dark  {DS_DECK_NAME}  reserve={_qty(DS_GROUPS)}  shields={_shields(DS_GROUPS)}  "
        f"unread={DS_UNREAD}  no_dest={DS_NO_DEST}"
    )
