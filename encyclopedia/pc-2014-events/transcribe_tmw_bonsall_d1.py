#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 typed printout: Paul Bonsall Dark.

Source: 2014-TMW-Day-1.pdf pages 11–12 (type-grouped printout).
Handwritten header Paul Bonsall / Dark Bro / Texas Mini-Worlds 2014.
Light Side was not published on this pair of pages.
Crossed-out shields are dested as the handwritten replacement.
"""
from __future__ import annotations

PLAYER = "Paul Bonsall"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 0
DS_PAGE = 11
LS_SCAN = ""
DS_SCAN = "2014 Texas Mini Worlds Day 1 p11 Paul Bonsall DS.png"
DS_SCAN2 = "2014 Texas Mini Worlds Day 1 p12 Paul Bonsall DS.png"
NOTE = "Typed printout (not a handwritten Xerox form). Light Side was not published."
EXTRA_SCANS = [
    ("2014 Texas Mini Worlds Day 1 p12 Paul Bonsall DS.png", "Page 12 of [[:File:2014 Texas Mini Worlds Day 1.pdf]]."),
]


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = ""
LS_CARDS = []
LS_SHIELDS = []
LS_ADD = []

DS_START = "Separatist Uprising / At War With Itself"
DS_CARDS = [
    n("Separatist Uprising / At War With Itself"),
    n("Boba Fett, Prepared Hunter"),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("Jango Fett, The Assassin"),
    n("Darth Sidious"),
    n("Count Dooku", qty=2),
    n("P-59"),
    n("Keder The Black"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Trophy Of A Kill"),
    n("Gift Of The Master"),
    n("Ni Chuba Na", True),
    n("Arena Pillars"),
    n("Blaster Rack", True),
    n("The Phantom Menace"),
    n("War Has Begun"),
    n("Blast Door Controls"),
    n("Jabba's Haven"),
    n("Knowledge And Defense", True),
    n("Ghhhk"),
    n("Force Push", True),
    n("Control & Set For Stun"),
    n("Sniper & Dark Strike"),
    n("Imbalance & Kintan Strider", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Cold Feet", True),
    n("Operational As Planned", True),
    n("Sith Fury & End This Destructive Conflict"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Monnok"),
    n("Alter (Coruscant)", True),
    n("Force Field", True, qty=2),
    n("Force Lightning"),
    n("Abyssin Ornament", True),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Prepared Defenses", True),
    n("Cloud City: Security Tower", True),
    n("Geonosis: Separatist Council Room"),
    n("Naboo: Theed Palace Generator Core"),
    n("Geonosis: Petranaki Arena"),
    n("Nal Hutta"),
    n("Arena Execution"),
    n("Zuckuss In Mist Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Aurra Sing's Blaster Rifle"),
    n("Dooku's Lightsaber"),
    n("Dark Jedi Lightsaber", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Secret Plans"),
    n("Firepower", True),
    n("There Is No Try"),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = []
