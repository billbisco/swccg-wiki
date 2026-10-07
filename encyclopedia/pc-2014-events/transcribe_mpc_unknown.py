#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Unknown Player Dark Walkers.

Source: MPC-2014-Day-1-Main-Event.pdf page 110 (typed Holotable list +
handwritten shields). Name blank. Sandwich Shumaker p109 / Brian Terwilliger p111.
Facing + Username + identity fail. Distinct from p114 Chris Terwilliger Cyclone Walkers.
"""
from __future__ import annotations

PLAYER = "Unknown Player"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 0
DS_PAGE = 110
LS_SCAN = ""
DS_SCAN = "2014 Match Play Championship Day 1 Unknown Player DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Typed Holotable-style Dark Walkers list. Name blank."
PUBLIC_NOTE = "Name blank on the Day 1 sheet."
DS_NOTE = (
    "Typed Holotable list plus handwritten shields. Name blank. Username blank. "
    "Sandwich Shumaker p109 / Brian Terwilliger p111. Dest Unknown Player. "
    "Imperial Occupation/Imperial Control (V) dested Imperial Occupation (V) / Imperial Control (V). "
    "Darth Maul crossed, Cyborg Commander dested Grievous, Hunter Of Jedi. "
    "Walker Garrison (V) crossed, Trample dested Trample. "
    "Handwritten Tempest 1, Blizzard 1 (V), AT-AT Cannon (V) added. "
    "(AI) without (V) dested without (V). Distinct from p114 Cyclone Walker x3 list. "
    "(V) from typed (V) or checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = ""
LS_CARDS = []
LS_SHIELDS = []
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("We're In Attack Position Now"),
    n("Garindan", True, qty=2),
    n("Count Dooku"),
    n("Commander Igar", True),
    n("Myn Kyneugh", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Grand Moff Tarkin", True),
    n("ISB Sector Commander"),
    n("General Nevar"),
    n("Veers", True),
    n("Juno Eclipse, Black Leader"),
    n("Darth Vader", True),
    n("Grievous, Hunter Of Jedi"),
    n("Imperial Decree"),
    n("Hoth Blockade"),
    n("Combat Response"),
    n("Do They Have A Code Clearance"),
    n("You May Start Your Landing", True),
    n("Prepare For A Surface Attack"),
    n("No Escape"),
    n("Image Of The Dark Lord", True),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Imperial Decree", True),
    n("Knowledge And Defense", True),
    n("Target The Main Generator"),
    n("Control & Set For Stun"),
    n("Force Push", True),
    n("Trample"),
    n("Stop Motion", True),
    n("Imperial Command", qty=2),
    n("Sith Fury & End This Destructive Conflict"),
    n("A Dark Time For The Rebellion", True),
    n("Cold Feet", True),
    n("Close Call", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Prepared Defenses", True),
    n("Hoth: Main Power Generators", True),
    n("Hoth: Ice Plains", True),
    n("Hoth: Mountains"),
    n("Hoth: Defensive Perimeter"),
    n("Hoth"),
    n("Imperial Occupation / Imperial Control", True),
    n("Conquest", True),
    n("Victory"),
    n("Maul's Sith Infiltrator"),
    n("Maul's Sith Infiltrator"),
    n("Dooku's Solar Sailer"),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Imperial Walker", qty=2),
    n("Marquand In Blizzard 6"),
    n("Tempest 1"),
    n("Blizzard 1", True),
    n("AT-AT Cannon", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss"),
    n("Secret Plans"),
    n("Battle Order"),
    n("You Cannot Hide Forever"),
    n("Resistance"),
    n("Firepower"),
    n("A Useless Gesture"),
    n("Fanfare"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Leave Them To Me"),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
