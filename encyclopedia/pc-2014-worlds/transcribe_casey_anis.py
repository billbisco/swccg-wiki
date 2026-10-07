#!/usr/bin/env python3
"""Casey Anis, 2014 Worlds Day 2. Typed Holotable dump (no type headings).

Light Hidden Base: extract/day2/d2p1_p15.png.
  Handwritten sub You've Got A Lot Of Guts Coming Here for He's Tough (V).
Dark Hunt Down: extract/day2/d2p1_p16.png.
Grouped by card type (Emil type_groups shape). Shields are the (1 starting)
block of 15 defensive shields. Hidden Fortress is additional, not reserve.
"""
from __future__ import annotations

PLAYER = "Casey Anis"
USERNAME = ""
KIND = "type_groups"

# --- Light Hidden Base ---
LS_DECK_NAME = "Hidden Base"
LS_SIDE = "Light"
LS_SCAN = "extract/day2/d2p1_p15.png"
LS_PDF = "2014 Worlds Day 2 Part 1.pdf"
LS_PDF_PAGE = 15
LS_STARTING = ("Hidden Base / Systems Will Slip Through Your Fingers", False)

LS_GROUPS = [
    ("Objective", [
        (1, "Hidden Base / Systems Will Slip Through Your Fingers", False),
    ]),
    ("Admiral's Order", [
        (3, "I'll Take The Leader", False),
    ]),
    ("Character", [
        (1, "Anakin Skywalker, Padawan Learner", False),
        (1, "Lando Calrissian, Unlikely Hero", False),
        (1, "Jek Porkins (V)", True),
        (1, "Jaina Solo", False),
        (1, "Wedge Antilles, Red Squadron Leader", False),
        (1, "Mirax Terrik", False),
        (1, "Dash Rendar (V)", True),
        (1, "Chewie (V)", True),
        (1, "General Solo (V)", True),
        (1, "Luke Skywalker (V)", True),
    ]),
    ("Defensive shield", [
        (1, "Affect Mind (V)", True),
        (1, "Your Ship?", False),
        (1, "Your Insight Serves You Well (V)", True),
        (1, "Yavin Sentry (V)", True),
        (1, "Wise Advice", False),
        (1, "Weapons Display (V)", True),
        (1, "Ultimatum", False),
        (1, "The Professor (V)", True),
        (1, "Simple Tricks And Nonsense", False),
        (1, "Let's Keep A Little Optimism Here (V)", True),
        (1, "Do, Or Do Not", False),
        (1, "Chasm (V)", True),
        (1, "Battle Plan", False),
        (1, "Aim High", False),
        (1, "A Tragedy Has Occurred", False),
    ]),
    ("Effect", [
        (1, "Seeking An Audience (V)", True),
        (1, "Anger, Fear, Aggression (V)", True),
        (1, "Much to Learn, You Still Have", False),
        (1, "Our Most Desperate Hour", False),
        (1, "Flash Of Insight (V)", True),
        (1, "You've Got A Lot Of Guts Coming Here", False),
        (1, "Strike Planning", False),
        (1, "Squadron Assignments", False),
        (2, "Projection Of A Skywalker", False),
    ]),
    ("Hidden Fortress", [
        (1, "Hidden Fortress", False),
    ]),
    ("Interrupt", [
        (1, "Moving To Attack Position", False),
        (1, "Power Pivot", False),
        (1, "On The Edge", False),
        (1, "Rebel Artillery", False),
        (1, "Antilles Maneuver & Rebel Reinforcements", False),
        (1, "It's A Hit!", False),
        (1, "We're Doomed", False),
        (1, "It Could Be Worse", False),
        (1, "Hyper Escape", False),
        (1, "Rebel Barrier", False),
        (3, "All Wings Report In & Darklighter Spin", False),
        (2, "A Few Maneuvers", False),
        (1, "Heading For The Medical Frigate", False),
    ]),
    ("Location", [
        (1, "Coruscant", False),
        (1, "Kessel", False),
        (2, "Kashyyyk", False),
        (2, "Tatooine", False),
        (1, "Nar Shaddaa", False),
        (2, "Endor", False),
        (1, "Alderaan (Blown Away)", False),
        (1, "Rendezvous Point", False),
    ]),
    ("Starship", [
        (1, "Azure Angel", False),
        (1, "Lady Luck", False),
        (1, "Red 6", False),
        (1, "Rogue Squadron X-wing", False),
        (1, "Red Squadron 1", False),
        (1, "Pulsar Skate", False),
        (1, "Outrider", False),
        (1, "Millennium Falcon (V)", True),
        (2, "Artoo-Detoo In Red 5", False),
    ]),
    ("Weapon", [
        (2, "X-wing Laser Cannon", False),
    ]),
]

LS_NOTES = (
    "Typed Holotable dump, no type headings; handwritten 'Casey Anis Day 2'. "
    "He's Tough (V) crossed out; handwritten 'You've Got a lot of Guts Coming Here' "
    "kept as the replacement. Hidden Fortress (1 starting) is additional, not reserve. "
    "(1 starting) also on objective, Anger/Fear/Aggression (V), Coruscant, "
    "Kashyyyk/Tatooine/Endor (x2 each), Strike Planning, Squadron Assignments, "
    "Heading For The Medical Frigate, Rendezvous Point, and the 15-shield block. "
    "Typed reserve sums to 63 (not 60); do not invent cuts. "
    "Yavin Sentry (V) written Yavin Sentry (V). Light Kiffex not used."
)
LS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []

# --- Dark Hunt Down ---
DS_DECK_NAME = "Hunt Down"
DS_SIDE = "Dark"
DS_SCAN = "extract/day2/d2p1_p16.png"
DS_PDF = "2014 Worlds Day 2 Part 1.pdf"
DS_PDF_PAGE = 16
DS_STARTING = (
    "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe",
    False,
)

DS_GROUPS = [
    ("Objective", [
        (1, "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", False),
    ]),
    ("Character", [
        (1, "Dengar With Blaster Carbine (V)", True),
        (1, "Mara Jade With Lightsaber", False),
        (2, "Count Dooku", False),
        (1, "Boba Fett, Prepared Hunter", False),
        (1, "Jango Fett, The Assassin", False),
        (3, "Darth Maul With Lightsaber", False),
        (4, "Darth Vader, Dark Lord Of The Sith", False),
        (3, "Emperor Palpatine", False),
        (1, "4-LOM With Concussion Rifle (V)", True),
    ]),
    ("Defensive shield", [
        (1, "You Cannot Hide Forever (V)", True),
        (1, "Fanfare (V)", True),
        (1, "We'll Let Fate-a Decide, Huh?", False),
        (1, "Secret Plans", False),
        (1, "Resistance", False),
        (1, "Leave Them To Me (V)", True),
        (1, "I Find Your Lack Of Faith Disturbing (V)", True),
        (1, "Firepower (V)", True),
        (1, "Death Star Sentry (V)", True),
        (1, "Do They Have A Code Clearance? (V)", True),
        (1, "Come Here You Big Coward", False),
        (1, "Battle Order", False),
        (1, "Allegations Of Corruption", False),
        (1, "A Useless Gesture (V)", True),
        (1, "Abyss (V)", True),
    ]),
    ("Effect", [
        (1, "No Escape", False),
        (1, "The Phantom Menace", False),
        (1, "Emperor's Power (V)", True),
        (1, "Something Special Planned For Them (V)", True),
        (1, "Crush The Rebellion", False),
        (1, "Ni Chuba Na?? (V)", True),
        (2, "Visage Of The Emperor", False),
        (1, "Knowledge And Defense (V)", True),
    ]),
    ("Epic Event", [
        (1, "Revenge Of The Sith", False),
    ]),
    ("Interrupt", [
        (2, "Sith Fury (V)", True),
        (1, "Force Field (V)", True),
        (1, "Protocol Failure", False),
        (1, "Cold Feet (V)", True),
        (2, "Short Range Fighters & Watch Your Back!", False),
        (1, "Maul Strikes", False),
        (1, "Force Push (V)", True),
        (3, "Force Lightning", False),
        (3, "We Must Accelerate Our Plans", False),
        (2, "ComScan Detection (V)", True),
        (3, "Sonic Bombardment (V)", True),
        (1, "Evader & Monnok", False),
        (2, "I Have You Now", False),
        (1, "Prepared Defenses", False),
        (1, "Surface Defense (V)", True),
    ]),
    ("Location", [
        (1, "Death Star: War Room (V)", True),
        (1, "Blockade Flagship: Hallway", False),
        (1, "Blockade Flagship: Bridge", False),
        (1, "Cloud City: Security Tower (V)", True),
        (1, "Executor: Meditation Chamber", False),
        (1, "Executor: Holotheatre", False),
    ]),
    ("Starship", [
        (1, "Slave I, Symbol Of Fear", False),
    ]),
]

DS_NOTES = (
    "Typed Holotable dump, no type headings; handwritten 'Casey Anis Day 2'. "
    "Hunt Down / Executor start. Visage Of The Emperor (x2) (1 starting). "
    "Surface Defense (V) is the starting interrupt, not a 16th shield. "
    "We'll Let Fate-a Decide, Huh? written 'We'll Let Fate-a Decide, Huh?'. "
    "Reserve qty 60 excluding Defensive shield. "
    "(1 starting) also on objective, Crush The Rebellion, Ni Chuba Na?? (V), "
    "Prepared Defenses, Surface Defense (V), Executor sites, Knowledge And Defense (V), "
    "and the 15-shield block."
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
        f"transcribe_casey_anis.py  {PLAYER}\n"
        f"  Light {LS_DECK_NAME}  reserve={_qty(LS_GROUPS)}  shields={_shields(LS_GROUPS)}  "
        f"unread={LS_UNREAD}  no_dest={LS_NO_DEST}\n"
        f"  Dark  {DS_DECK_NAME}  reserve={_qty(DS_GROUPS)}  shields={_shields(DS_GROUPS)}  "
        f"unread={DS_UNREAD}  no_dest={DS_NO_DEST}"
    )
