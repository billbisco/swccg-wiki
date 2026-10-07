#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Michael Thomas Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Michael Thomas"
USERNAME = "mmThomas2"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 97
DS_PAGE = 98
LS_SCAN = "2013 Match Play Championship p97 Michael Thomas LS.png"
DS_SCAN = "2013 Match Play Championship p98 Michael Thomas DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Michael Thomas. Light. Deck title Speeder Yo Butts. "
    "Username mmThomas2. Local Uprising / Liberation dested Local Uprising / Liberation. "
    "Hoth: Main Power Generator dested Hoth: Main Power Generators. "
    "Maneuvering Flaps + Nick Of Time dested Maneuvering Flaps & Nick Of Time. "
    "Yub-Yub Commander dested Yub Yub, Commander. "
    "All Wings Report In + Darklighter Spin dested All Wings Report In & Darklighter Spin. "
    "Wedge Antilles, Red Squadron Commander dested Wedge Antilles, Red Squadron Leader. "
    "I'm With You Too dested I'm With You Too. Dual Laser Cannons dested Dual Laser Cannon. "
    "T-47 Battle Formation as written. Planetary Defense dested Planetary Defenses. "
    "Form left column reprints 37–38 on lines 39–40 are Obi-Wan In Radiant VII and Lando Calrissian, Scoundrel. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Michael Thomas. Dark. Deck title Naboo Belongs to the Mutants. "
    "Username mmThomas2. Invasion / In Complete Control as written. "
    "Naboo Swamp dested Naboo: Swamp. At Last We're Getting Results dested At Last We Are Getting Results. "
    "32700 To 1 dested 3,720 To 1. Sniper + Dark Strike dested Sniper & Dark Strike. "
    "The Mandalorian Father of the Fett dested Jango Fett, The Assassin. "
    "He Is Not Ready + Imperial Propaganda dested He Is Not Ready. "
    "P13 + P14 dested P-13 & P-14. Master Destroyers dested Master, Destroyers!. "
    "Trade Federation Blockade Support Ship dested Blockade Support Ship. "
    "Imbalance + Kintan Strider dested Imbalance & Kintan Strider. "
    "Form left column reprints 37–38 on lines 39–40 are Wounded Warrior. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Local Uprising / Liberation"
LS_CARDS = [
    n("Local Uprising / Liberation", True),
    n("Hoth"),
    n("Hoth: Main Power Generators", True),
    n("Hoth: North Ridge"),
    n("Heading For The Medical Frigate"),
    n("Rycar Ryjerd", True),
    n("Wokling", True),
    n("Get To Your Ships"),
    n("Maneuvering Flaps & Nick Of Time", True),
    n("Echo Base Garrison"),
    n("Hoth: Echo Docking Bay"),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Snow Trench"),
    n("Frostbite", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("I'll Take The Leader", qty=2),
    n("Projection Of A Skywalker", qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("We Wish To Board At Once", qty=2),
    n("Commander Luke Skywalker", True, qty=2),
    n("Red 6", qty=2),
    n("Yub Yub, Commander", True, qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Ice Storm"),
    n("Jek Porkins", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("I'm With You Too", True),
    n("Gold Leader In Gold 1", True),
    n("Snowspeeder Garrison", True),
    n("Obi-Wan In Radiant VII", True),
    n("Lando Calrissian, Scoundrel"),
    n("Haven"),
    n("We're Doomed"),
    n("Rogue 2"),
    n("Rebel Barrier"),
    n("Menace Fades"),
    n("Corran Horn"),
    n("Rogue 4"),
    n("Dash Rendar"),
    n("Imperial Atrocity", True),
    n("Derek 'Hobbie' Klivian", True),
    n("T-47 Battle Formation"),
    n("Han, Chewie, And The Falcon"),
    n("Dual Laser Cannon", True),
    n("Wrist Comlink"),
    n("Zev Senesca"),
    n("Rogue 1"),
    n("A Few Maneuvers"),
    n("Rogue 3"),
    n("Veteran Rogue", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense", True),
    n("Aim High", True),
    n("Ounee Ta"),
    n("Planetary Defenses"),
    n("Let's Keep A Little Optimism Here"),
    n("Traffic Control", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Another Pathetic Lifeform", True),
]
LS_ADD = []

DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Naboo"),
    n("Naboo: Swamp"),
    n("Blockade Flagship", True),
    n("Droid Racks", True),
    n("Where Are Those Droidekas?!", True),
    n("At Last We Are Getting Results", True),
    n("3,720 To 1", True),
    n("Prepared Defenses", True),
    n("Naboo: Theed Palace Throne Room"),
    n("Naboo: Theed Palace Generator"),
    n("Blockade Flagship: Bridge"),
    n("Sniper & Dark Strike"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sith Fury", True),
    n("Jango Fett, The Assassin", True),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("Forced Servitude"),
    n("Elis Helrot"),
    n("Imperial Justice", True),
    n("Darth Maul"),
    n("Self-Destruct Mechanism"),
    n("Masterful Move & Endor Occupation"),
    n("Protocol Failure", True),
    n("He Is Not Ready", True),
    n("Captain Daultay Dofine"),
    n("P-13 & P-14", True),
    n("Lightsaber Deficiency", True),
    n("Slave I, Symbol Of Fear", True),
    n("Destroyer Droid", qty=9),
    n("Wounded Warrior", qty=2),
    n("P-60", qty=2),
    n("Oh, Switch Off", qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Rolling, Rolling, Rolling", qty=2),
    n("Guri", qty=2),
    n("P-59", qty=2),
    n("Master, Destroyers!", qty=3),
    n("Blockade Support Ship", qty=2),
    n("Imbalance & Kintan Strider", qty=2),
    n("Sudden Impact", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
