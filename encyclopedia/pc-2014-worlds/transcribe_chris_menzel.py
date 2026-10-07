#!/usr/bin/env python3
"""Chris Menzel, 2014 Worlds Day 2. Excel/spreadsheet printouts.

Light Never Change A Losing System: extract/day2/d2p2_p21.png
  Dash Rendar 1→0; Seeking An Audience and Evacuation Control struck; Kal'Falnl struck.
Dark Hunt Down and Destroy zee Germans: extract/day2/d2p2_p22.png
  I Have You Now struck; Weapon Of A Sith crossed on shields.
"""
from __future__ import annotations

PLAYER = "Chris Menzel"
USERNAME = ""
KIND = "type_groups"

# --- Light Rebel Senate ---
LS_DECK_NAME = "Never Change A Losing System"
LS_SIDE = "Light"
LS_SCAN = "extract/day2/d2p2_p21.png"
LS_PDF = "2014 Worlds Day 2 Part 2.pdf"
LS_PDF_PAGE = 21
LS_STARTING = ("Plead My Case To The Senate / Sanity And Compassion", False)

LS_GROUPS = [
    ("Objective", [
        (1, "Plead My Case To The Senate / Sanity And Compassion", False),
    ]),
    ("Admiral's Order", [
        (1, "Combined Fleet Action", False),
    ]),
    ("Character", [
        (3, "Bail Organa, Father Of Rebellion", False),  # sheet Father of the Rebellion (V)
        (1, "Senator Mon Mothma (V)", True),
        (1, "Senator Padme Amidala (V)", True),
        (1, "Mas Amedda", False),
        (1, "Princess Leia (V)", True),
        (1, "Lando Calrissian, Unlikely Hero (V)", True),
        (2, "Han Solo, Courageous Smuggler (V)", True),
        (2, "Commander Luke Skywalker (V)", True),
        (1, "Wedge Antilles, Red Squadron Leader", False),
        (1, "Yoda, Master Of The Force", False),  # sheet Yoda: Master of the Force
        (1, "Corran Horn", False),
        (1, "Admiral Ackbar (V)", True),
        (1, "Chewie (V)", True),
        # Dash Rendar (V) 1→0 omitted
        # Kal'Falnl C'ndros (V) struck omitted
    ]),
    ("Defensive shield", [
        (1, "A Tragedy Has Occurred", False),  # sheet Occured
        (1, "Weapons Display (V)", True),
        (1, "Your Insight Serves You Well (V)", True),
        (1, "The Professor (V)", True),
        (1, "Simple Tricks And Nonsense (V)", True),  # sheet Simple Tricks And Knowledge (V)
        (1, "Let's Keep A Little Optimism Here (V)", True),
        (1, "Wise Advice", False),
        (1, "Aim High", False),
        (1, "Don't Do That Again", False),
        (1, "Battle Plan", False),
        (1, "Ultimatum", False),
        (1, "Affect Mind (V)", True),
        (1, "Chasm (V)", True),
        (1, "Yavin Sentry (V)", True),
        (1, "Jabba's Prize (V)", True),  # sheet Jabbas Prize (V)
    ]),
    ("Effect", [
        (1, "Anger, Fear, Aggression (V)", True),
        (1, "Senate Hovercam", False),
        (1, "Imperial Atrocity (V)", True),
        (1, "Strikeforce (V)", True),
        (1, "So This Is How Liberty Dies (V)", True),  # sheet So, This Is How Liberty Dies (V)
        (1, "Menace Fades", False),
        (1, "Echo Base Garrison", False),
        (1, "Leia Of Alderaan (V)", True),
        # Seeking An Audience (V) struck
        # Evacuation Control (V) struck
    ]),
    ("Interrupt", [
        (1, "Don't Tread On Me (V)", True),  # starting 1/2 Hand Start
        (4, "Might Of The Republic", False),
        (2, "Rebel Leadership (V)", True),
        (2, "All Wings Report In & Darklighter Spin", False),
        (1, "Control & Tunnel Vision", False),
        (1, "Corellian Retort (V)", True),
        (1, "Attack Pattern Delta (V)", True),
        (1, "Alter (Coruscant) (V)", True),  # sheet Alter (Episode 1) (V)
        (1, "Sense", False),
        (1, "Yoda Stew & You Do Have Your Moments", False),
        (1, "Don't Tread On Me (V)", True),  # 2nd copy
        (2, "Let The Wookiee Win (V)", True),  # sheet Let The Wookie Win
    ]),
    ("Location", [
        (1, "Coruscant: Galactic Senate", False),
        (1, "Coruscant: Jedi Council Chamber", False),
        (1, "Coruscant", False),  # sheet Coruscant (System) (Special Edition)
        (1, "Coruscant: Senate Landing Platform", False),
        (1, "Home One: War Room", False),
        (1, "Yavin 4: Massassi War Room (V)", True),
    ]),
    ("Starship", [
        (1, "Home One", False),
        (1, "Millennium Falcon", False),  # sheet Millenium Falcon
        (1, "Lady Luck (V)", True),
        (2, "Rogue 1", False),
        (2, "Republic Gunship Wing (V)", True),
    ]),
    ("Weapon", [
        (1, "Dual Laser Cannon", False),
    ]),
]

LS_NOTES = (
    "Spreadsheet 'LS Rebel Senate Deck 2014 - Never Change A Losing System' VB 09.02; "
    "Worlds 2014 23.08.2014 Chris Menzel. Header 60. "
    "Dash Rendar (V) qty 1→0 omitted. Kal'Falnl C'ndros (V) fully struck omitted. "
    "Seeking An Audience (V) and Evacuation Control (V) struck (qty 0). "
    "Don't Tread On Me (V) is a starting 1/2 Hand Start plus a 2nd interrupt copy. "
    "Simple Tricks And Knowledge (V) → Simple Tricks And Nonsense. "
    "Alter (Episode 1) (V) → Alter (Coruscant) (V). "
    "So, This Is How Liberty Dies → So This Is How Liberty Dies. "
    "Bail Organa, Father of the Rebellion (V) → Bail Organa, Father Of Rebellion. "
    "After strikethroughs reserve sums to 59; do not invent a card."
)
LS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []

# --- Dark Hunt Down ---
DS_DECK_NAME = "Hunt Down and Destroy zee Germans"
DS_SIDE = "Dark"
DS_SCAN = "extract/day2/d2p2_p22.png"
DS_PDF = "2014 Worlds Day 2 Part 2.pdf"
DS_PDF_PAGE = 22
DS_STARTING = (
    "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe",
    False,
)

DS_GROUPS = [
    ("Objective", [
        (1, "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", False),
    ]),
    ("Character", [
        (2, "Darth Vader, Dark Lord Of The Sith", False),
        (2, "Darth Vader With Lightsaber", False),
        (1, "Mara Jade With Lightsaber (V)", True),
        (2, "Darth Maul With Lightsaber", False),
        (2, "Battle Droid Squad (V)", True),
        (2, "P-59", False),
        (1, "Boba Fett, Prepared Hunter (V)", True),
        (2, "Jango Fett (V)", True),  # sheet The Mandalorian, Father of Fett (V)
        (1, "4-LOM With Concussion Rifle (V)", True),
        (1, "Grand Admiral Thrawn", False),
        (1, "Garindan (V)", True),
    ]),
    ("Defensive shield", [
        (1, "Abyss (V)", True),
        (1, "Allegations Of Corruption", False),
        (1, "After Her! (V)", True),  # sheet After Her (V)
        (1, "A Useless Gesture (V)", True),
        (1, "Battle Order", False),
        (1, "Come Here You Big Coward", False),
        (1, "Do They Have A Code Clearance? (V)", True),
        (1, "Firepower (V)", True),
        (1, "I Find Your Lack Of Faith Disturbing (V)", True),
        (1, "Imperial Detention (V)", True),
        (1, "Oppressive Enforcement", False),
        (1, "Resistance", False),
        (1, "Secret Plans", False),
        # Weapon Of A Sith struck
        (1, "You Cannot Hide Forever (V)", True),
        (1, "Fanfare", False),
    ]),
    ("Effect", [
        (1, "Visage Of The Emperor", False),
        (1, "Knowledge And Defense (V)", True),
        (1, "Imperial Propaganda (V)", True),
        (1, "The Phantom Menace", False),
        (1, "Imperial Justice (V)", True),
        (1, "No Escape", False),
        (1, "Program Trap", False),
        (1, "Presence Of The Force", False),
        (1, "Something Special Planned For Them (V)", True),
    ]),
    ("Epic Event", [
        (1, "Revenge Of The Sith (V)", True),
    ]),
    ("Interrupt", [
        (1, "Surface Defense (V)", True),  # 1/2 Hand Start
        (3, "We Must Accelerate Our Plans", False),
        (2, "Why Didn't You Tell Me? (V)", True),
        (2, "Sonic Bombardment (V)", True),
        (2, "They're Still Coming Through!", False),
        (2, "Masterful Move & Endor Occupation", False),
        (1, "Ghhhk", False),
        (1, "Vader's Obsession", False),
        (1, "Sith Fury & End This Destructive Conflict (V)", True),
        (1, "Alter (V)", True),
        (1, "Force Push (V)", True),
        (1, "A Dark Time For The Rebellion (V)", True),
        (1, "You Swindled Me! (V)", True),
        (1, "Imbalance & Kintan Strider (V)", True),
        (1, "You Are Beaten", False),
        (1, "Sense", False),
        (1, "Cold Feet (V)", True),
        (1, "Stop Motion (V)", True),
        (1, "Force Field (V)", True),
        # I Have You Now (V) struck
    ]),
    ("Location", [
        (1, "Executor: Holotheatre", False),
        (1, "Executor: Meditation Chamber (V)", True),
        (1, "Blockade Flagship: Bridge", False),
        (1, "Cloud City: Security Tower (V)", True),
        (1, "Imperial Holotable", False),
    ]),
    ("Starship", [
        (1, "Slave I, Symbol Of Fear (V)", True),
        (1, "Victory (V)", True),
    ]),
]

DS_NOTES = (
    "Spreadsheet 'Hunt Down and Destroy zee Germans' Worlds 2014 23.08.2014 V 9.02. "
    "I Have You Now (V) fully struck (header Interrupts 24 matches remaining). "
    "Weapon Of A Sith crossed on shields (14 shields remain). "
    "The Mandalorian, Father of Fett (V) → Jango Fett (V) (vb5 lore nickname; same as Aaron Day 2). "
    "After Her (V) → After Her! (V). Surface Defense (V) is the 1/2 Hand Start. "
    "Starting 6 include objective, Holotheatre, Meditation Chamber (V), Visage, "
    "Surface Defense (V), Knowledge And Defense (V). Reserve qty 60 excluding shields."
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
        f"transcribe_chris_menzel.py  {PLAYER}\n"
        f"  Light {LS_DECK_NAME}  reserve={_qty(LS_GROUPS)}  shields={_shields(LS_GROUPS)}  "
        f"unread={LS_UNREAD}  no_dest={LS_NO_DEST}\n"
        f"  Dark  {DS_DECK_NAME}  reserve={_qty(DS_GROUPS)}  shields={_shields(DS_GROUPS)}  "
        f"unread={DS_UNREAD}  no_dest={DS_NO_DEST}"
    )
