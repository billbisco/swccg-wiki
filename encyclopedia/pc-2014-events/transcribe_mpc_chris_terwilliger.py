#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Chris Terwilliger.

Source: MPC-2014-Day-1-Main-Event.pdf pages 113–114 (2013 form, 15 shields).
Name Chris Twigg dested Chris Terwilliger. Username blank.
"""
from __future__ import annotations

PLAYER = "Chris Terwilliger"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 113
DS_PAGE = 114
LS_SCAN = "2014 Match Play Championship Day 1 Chris Terwilliger LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Chris Terwilliger DS.png"
LS_DECK_NAME = "Albany Y4"
DS_DECK_NAME = "Twigg Hoth Cyclone Walkers"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Chris Twigg dested Chris Terwilliger. Username blank. "
    "LIGHT checked. Deck name Albany Y4. IITFYS (V) dested It Is The Future You See (V) / "
    "A Tremor In The Force (V). Lando UH dested Lando Calrissian, Unlikely Hero. "
    "Lando's Luxury Yacht dested Lady Luck. SATM & Blaster Proficiency dested "
    "Sorry About The Mess & Blaster Proficiency. Unique overcounts sheet-accurate "
    "(Let The Wookiee Win (V) x3, A Jedi's Resilience x2, Speak With The Jedi Council x2, "
    "Rebel Leadership (V) x3, Wesa Gotta Grand Army x3, Imperial Atrocity (V) x2, "
    "Escape Pod (V) x2, Mace Windu (V) x2, Master Qui-Gon (V) x2, Luke Skywalker, Jedi Knight x2, "
    "Luke Skywalker, Strong In The Force (V) x2, Clash Of Sabers x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Chris Twigg dested Chris Terwilliger. Username blank. "
    "DARK checked. Deck name Twigg Hoth Cyclone Walkers. Imperial Occupation (V) dested "
    "Imperial Occupation (V) / Imperial Control (V). Control & Set For Stun dested "
    "Control & Set For Stun. Jango Fett The Assassin dested Jango Fett, The Assassin. "
    "Cyclone Walker (V) x3 unique overcount sheet-accurate. Unique overcounts sheet-accurate "
    "(AT-AT Deployment Platform (V) x2, A Dark Time For The Rebellion (V) x2, Imperial Command x3, "
    "Imperial Decree (V) x2, We're In Attack Position Now x2, Cyclone Walker (V) x3, "
    "Blizzard 4 x2, Victory (V) x2, Conquest (V) x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("Home One: War Room"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Yavin 4: Massassi War Room", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Quick Draw", True),
    n("It Is The Future You See / A Tremor In The Force", True),
    n("Let The Wookiee Win", True, qty=3),
    n("A Jedi's Resilience", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Jedi Levitation"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Blaster Deflection"),
    n("Seeking An Audience", True),
    n("What're You Tryin' To Push On Us"),
    n("Sai'torr Kal Fas", True),
    n("Imperial Atrocity", True, qty=2),
    n("Houjix"),
    n("Grimtaash"),
    n("Escape Pod", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Master Qui-Gon", True, qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Luke's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Clash Of Sabers", qty=2),
    n("Weapon Levitation"),
    n("Han, Chewie, And The Falcon", True),
    n("Home One"),
    n("Lady Luck", True),
    n("Artoo-Detoo In Red 5"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Ultimatum", True),
    n("The Professor", True),
    n("There Is Another", True),
    n("Simple Tricks And Nonsense", True),
    n("Only Jedi Carry That Weapon", True),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Aim High", True),
    n("Affect Mind", True),
    n("A Tragedy Has Occurred", True),
]
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth: Ice Plains", True),
    n("Hoth: Main Power Generators", True),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Mountains"),
    n("Hoth"),
    n("AT-AT Deployment Platform", True, qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Control & Set For Stun"),
    n("Cold Feet", True),
    n("Imperial Command", qty=3),
    n("Close Call", True),
    n("Trample"),
    n("Crash Landing"),
    n("Prepared Defenses", True),
    n("Hoth Blockade", True),
    n("No Escape"),
    n("You May Start Your Landing", True),
    n("Image Of The Dark Lord", True),
    n("Endor Shield", True),
    n("Do They Have A Code Clearance"),
    n("Imperial Decree", True, qty=2),
    n("Alert My Star Destroyer!"),
    n("Fleet Security Protocols", True),
    n("Target The Main Generator"),
    n("We're In Attack Position Now", qty=2),
    n("AT-AT Cannon", True),
    n("Cyclone Walker", True, qty=3),
    n("Blizzard 4", qty=2),
    n("Tempest 1"),
    n("Blizzard 2", True),
    n("Victory", True, qty=2),
    n("Flagship Executor"),
    n("Conquest", True, qty=2),
    n("Darth Vader", True),
    n("Grand Moff Tarkin", True),
    n("Jango Fett, The Assassin", True),
    n("Sate Pestage", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("ISB Sector Commander", True),
    n("Veers", True),
    n("Garindan", True),
    n("Commander Igar"),
    n("Admiral Piett"),
    n("Grand Admiral Thrawn"),
    n("Admiral Motti", True),
    n("U-3PO (Yoo-Threepio)"),
    n("AT-AT Commander", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("There Is No Try", True),
    n("Secret Plans", True),
    n("Wipe Them Out, All Of Them", True),
    n("Resistance", True),
    n("Oppressive Enforcement", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Come Here You Big Coward", True),
    n("Battle Order", True),
    n("Allegations Of Corruption", True),
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Death Star Sentry", True),
]
DS_ADD = []
