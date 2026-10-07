#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Tim Heffner.

Source: MPC-2014-Day-1-Main-Event.pdf pages 55–56 (2013 form, 15 shields).
Username Darth Tim.
"""
from __future__ import annotations

PLAYER = "Tim Heffner"
USERNAME = "Darth Tim"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 55
DS_PAGE = 56
LS_SCAN = "2014 Match Play Championship Day 1 Tim Heffner LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Tim Heffner DS.png"
LS_DECK_NAME = "Rogue Sabotage"
DS_DECK_NAME = "Separatist Revolt!"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username Darth Tim. Center Of Tyranny / A Liberation dested "
    "Center Of Tyranny / A Liberation. Houjix & Out Of Nowhere dested Houjix & Out Of "
    "Nowhere. Antilles Maneuver & Rebel Reinforcements dested Antilles Maneuver & Rebel "
    "Reinforcements. Commando Training & K'lor'slug dested Commando Training & K'lor'slug. "
    "(V) from checkbox. Unique overcounts sheet-accurate (Luke Skywalker, Rebel Hero x2, "
    "Blast The Door, Kid! x2, Antilles Maneuver & Rebel Reinforcements x2, Yub Nub, "
    "Commander x3)."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username Darth Tim. Separatist Uprising / At War With Itself. "
    "Knowledge And Defense (V) starting. Cyborg Commander, Hunter of Jedi dested Grievous, "
    "Hunter Of Jedi. Jango Fett The Assassin dested Jango Fett, The Assassin. Slave I, "
    "Symbol Of Fear dested Slave I, Symbol Of Fear. Captain Dauntless Dofine dested "
    "Captain Dauntless Dofine. Sil Unch dested Sil Unch. (V) from checkbox. Unique "
    "overcounts sheet-accurate (OOM Command Battle Droid x2, B2 Super Battle Droid x3, "
    "Tank Commander x3, Armored Attack Tank x3, IG-227 Hailfire Droid Tank x2, AAT Laser "
    "Cannon x2, We're In Attack Position Now (V) x2)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Center Of Tyranny / A Liberation"
LS_CARDS = [
    n("Center Of Tyranny / A Liberation"),
    n("Coruscant", True),
    n("Coruscant: Main Power Plant"),
    n("Coruscant: Lower Levels"),
    n("Planetary Shield"),
    n("Rogue Insertion"),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("Bacta Infirmary"),
    n("Rogue Squadron Tactics"),
    n("Declaration Of Rebellion"),
    n("Tycho Celchu", True),
    n("Dash Rendar", True),
    n("Corran Horn"),
    n("Veteran Rogue"),
    n("Luke Skywalker, Rebel Hero", qty=2),
    n("Senator Mon Mothma"),
    n("Wes Janson, Rogue Veteran", True),
    n("Zev Senesca"),
    n("Keir Santage"),
    n("Senator Leia Organa"),
    n("Bail Organa"),
    n("Dack Ralter", True),
    n("Ten Numb", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Commander Wedge Antilles", True),
    n("Derek 'Hobbie' Klivian", True),
    n("Commander Narra"),
    n("Threepio With His Parts Showing"),
    n("Obi-Wan In Radiant VII"),
    n("Artoo-Detoo In Red 5"),
    n("Red Squadron 7", True),
    n("Alderaan Consular Ship"),
    n("Errant Venture"),
    n("Han, Chewie, And The Falcon"),
    n("Disruptor Pistol"),
    n("Luke's Blaster Pistol", True),
    n("Dressel"),
    n("Coruscant: Docking Bay"),
    n("Houjix & Out Of Nowhere"),
    n("Nabrun Leids"),
    n("Corellian Slip", True),
    n("Blast The Door, Kid!", qty=2),
    n("Sabotage", True),
    n("We Wish To Board At Once"),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Desperate Reach", True),
    n("Yub Nub, Commander", qty=3),
    n("Commando Training & K'lor'slug"),
    n("Field Dressing"),
    n("Civil Disorder", True),
    n("Echo Base Garrison"),
    n("Menace Fades"),
    n("Coruscant Celebration"),
    n("Imperial Atrocity", True),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Do, Or Do Not"),
    n("Only Jedi Carry That Weapon"),
    n("Wise Advice"),
    n("Affect Mind", True),
    n("Weapons Display", True),
    n("A Close Race"),
    n("Another Pathetic Lifeform"),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Separatist Uprising / At War With Itself"
DS_CARDS = [
    n("Separatist Uprising / At War With Itself"),
    n("Geonosis: Separatist Council Room"),
    n("War Has Begun"),
    n("Knowledge And Defense", True),
    n("Everything Is Going As Planned"),
    n("Droid Racks"),
    n("Begin Landing Your Troops & The Dark Path"),
    n("Baktoid Armor Workshop"),
    n("Darth Sidious"),
    n("Count Dooku"),
    n("Grievous, Hunter Of Jedi"),
    n("Purge"),
    n("Nute Gunray", True),
    n("Captain Dauntless Dofine"),
    n("Lott Dod"),
    n("Sil Unch"),
    n("Keder The Black"),
    n("Tikkes"),
    n("Aks Moe"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("4-LOM With Concussion Rifle", True),
    n("OOM Command Battle Droid", qty=2),
    n("B2 Super Battle Droid", qty=3),
    n("Tank Commander", qty=3),
    n("Blockade Flagship", True),
    n("Trade Federation Battleship"),
    n("Slave I, Symbol Of Fear"),
    n("Bossk In Hound's Tooth"),
    n("Zuckuss In Mist Hunter"),
    n("Dengar In Punishing One"),
    n("Dooku's Solar Sailer"),
    n("Fanblade Starfighter"),
    n("AAT Assault Leader"),
    n("TT-6"),
    n("Armored Attack Tank", qty=3),
    n("IG-227 Hailfire Droid Tank", qty=2),
    n("Dooku's Lightsaber"),
    n("AAT Laser Cannon", qty=2),
    n("Geonosis"),
    n("Muunilinst"),
    n("Muunilinst: Docking Bay"),
    n("Muunilinst: City Of Harnaidan"),
    n("Muunilinst: Separatist Command Center"),
    n("We're In Attack Position Now", True, qty=2),
    n("Defense Of Muunilinst"),
    n("Rally To Our Cause"),
    n("Force Lightning"),
    n("Self-Destruct Mechanism", True),
    n("Deployment Orders"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Wipe Them Out, All Of Them"),
    n("Fanfare", True),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Weapon Of A Sith"),
    n("Death Star Sentry", True),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("Resistance"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Battle Order"),
]
DS_ADD = []
