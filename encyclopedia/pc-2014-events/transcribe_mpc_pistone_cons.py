#!/usr/bin/env python3
"""2014 Match Play Championship Consolation Xerox: Mike Pistone.

Source: MPC-2014-Day-2-Consolation-Event.pdf pages 1–2 (2013 form, 15 shields).
Name PISTONE dested Mike Pistone. Username blank.
Light Same as Yesterday with In/Out from Day 1 Light.
Dark full 60 Imperial Occupation.
"""
from __future__ import annotations

PLAYER = "Mike Pistone"
USERNAME = ""
STAGE = "Consolation"
PDF = "2014 Match Play Championship Consolation.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2014 Match Play Championship Consolation Mike Pistone LS.png"
DS_SCAN = "2014 Match Play Championship Consolation Mike Pistone DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2013 Xerox. Light Same as Yesterday with In/Out."
LS_PUBLIC_NOTE = (
    "Same as Day 1 Light with In/Out substitutions listed on the scan."
)
LS_NOTE = (
    "Handwritten 2013 Xerox. Name PISTONE dested Mike Pistone. Username blank. LIGHT checked. "
    "Same as Yesterday. OUT Weapon Levitation, Qui-Gon Jinn's Lightsaber, Strike Planning (V), "
    "Mechanical Failure. IN Leia, Rebel Princess (second copy), What're You Tryin' To Push On Us, "
    "Qui-Gon Jinn's Lightsaber (V), Clash Of Sabers (second copy). "
    "STRIKEFORCE (V) dested Strike Planning (V) as the Day 1 OUT. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name PISTONE dested Mike Pistone. Username blank. DARK checked. "
    "Imperial Occupation (V) dested Imperial Occupation (V) / Imperial Control (V). "
    "Grand Admiral crossed, Grand Moff Tarkin (V) replacement. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "Blast My Star Destroyer dested Alert My Star Destroyer!. "
    "YMSYL dested You May Start Your Landing. "
    "AT-AT Cannon checkbox True with NON V note dested AT-AT Cannon without (V). "
    "Line 27 empty skipped. Unique overcounts sheet-accurate (Cyclone Walker (V) x3, "
    "Conquest (V) x2, Blizzard 4 x2, Imperial Command x3, We're In Attack Position Now x2). "
    "NO_DEST AT-AT Deployment Platform; Fleet Security Protocols. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("Home One: War Room"),
    n("It Is The Future You See / A Tremor In The Force", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Seeking An Audience", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Leia, Rebel Princess", qty=2),
    n("Corran Horn"),
    n("Imperial Atrocity", True, qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Jedi Lightsaber", True),
    n("A Jedi's Resilience"),
    n("Clash Of Sabers", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Mace Windu", True, qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Master Qui-Gon", True, qty=2),
    n("Sai'torr Kal Fas", True),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Battle Plains"),
    n("Qui-Gon Jinn's Lightsaber", True),
    n("Hoth: Echo Command Center (War Room)"),
    n("Jedi Levitation", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Home One"),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Blaster Deflection"),
    n("Escape Pod", True, qty=2),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Quick Draw", True),
    n("Luke's Lightsaber"),
    n("Let The Wookiee Win", True, qty=3),
    n("Lando Calrissian, Unlikely Hero"),
    n("Houjix"),
    n("Lady Luck"),
    n("Grimtaash"),
    n("Admiral Ackbar", True),
    n("Han, Chewie, And The Falcon", True),
    n("Jaina Solo", True),
    n("Anger, Fear, Aggression", True),
    n("What're You Tryin' To Push On Us"),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Planetary Defenses", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense"),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("No Escape"),
    n("Imperial Command"),
    n("Blizzard 2", True),
    n("Grand Admiral Thrawn"),
    n("Darth Vader", True),
    n("Tempest 1"),
    n("Cyclone Walker", True, qty=3),
    n("Conquest", True, qty=2),
    n("Grand Moff Tarkin", True),
    n("Sate Pestage"),
    n("Victory"),
    n("Devastator", True),
    n("AT-AT Commander"),
    n("Walker Garrison"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Blizzard 4", qty=2),
    n("Veers"),
    n("Garindan", True),
    n("Jango Fett, The Assassin"),
    n("Trample"),
    n("AT-AT Deployment Platform"),
    n("Imperial Command"),
    n("Close Call", True),
    n("Cold Feet", True),
    n("A Dark Time For The Rebellion", True),
    n("We're In Attack Position Now", qty=2),
    n("Admiral Piett"),
    n("Imperial Command"),
    n("Flagship Executor"),
    n("Target The Main Generator"),
    n("Prepared Defenses", True),
    n("Commander Igar", True),
    n("AT-AT Cannon"),
    n("Hoth: Main Power Generators"),
    n("U-3PO"),
    n("Hoth: North Ridge (3rd Marker)"),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Hoth: Ice Plains"),
    n("Hoth"),
    n("Admiral Motti"),
    n("Alert My Star Destroyer!", True),
    n("Do They Have A Code Clearance"),
    n("Fleet Security Protocols"),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("You May Start Your Landing", True),
    n("Control & Set For Stun", True),
    n("Stop Motion", True),
    n("Imperial Barrier"),
    n("He Hasn't Come Back Yet"),
    n("Something Special Planned For Them", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Imperial Detention"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("A Useless Gesture", True),
    n("Fanfare", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Resistance"),
    n("Death Star Sentry", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Firepower", True),
    n("There Is No Try"),
    n("Abyss", True),
    n("Chasm"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
