#!/usr/bin/env python3
"""2012 US Nationals Day 2 leftover Xerox: Aaron Nelson.

Source: 2012NationalsDay2.pdf pages 7–8 (handwritten 2010 Xerox, 12 shields).
Name Aaron Nelson dested Aaron Nelson analog leftover Day 1 / 2012 MPC.
Username Airdog 2003 dested Airdog2003. p07 Dark Walkers. p08 Light TIGIH.
Do not dest as Brian Herold. Do not dest as Jake Nelson.
Do not dest Day 1 Nelson 60s again.
"""
from __future__ import annotations

PLAYER = "Aaron Nelson"
USERNAME = "Airdog2003"
STAGE = "Day 2"
PDF = "2012 US Nationals Day 2.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2012 US Nationals Day 2 Aaron Nelson LS.png"
DS_SCAN = "2012 US Nationals Day 2 Aaron Nelson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Nelson dested Aaron Nelson analog leftover Day 1 / 2012 MPC. "
    "Username Airdog 2003 dested Airdog2003. p07 LIGHT empty dest Dark from filled 60s. "
    "p08 LIGHT checked. Do not dest as Brian Herold. Do not dest Day 1 Nelson 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Nelson dested Aaron Nelson analog leftover Day 1. "
    "Username Airdog2003. LIGHT checked. Deck Name SoCal TIGIH. "
    "TIGIH / ICSIT dested There Is Good In Him / I Can Save Him analog leftover Kurten. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay) analog leftover Kelly. "
    "Luke's Fighter dested Luke's X-wing analog leftover. "
    "Hand Socket dested I'll Take The Hand Socket analog leftover. "
    "Wesa Gotta Grand Army dested analog leftover Kelly qty=3. "
    "Yoda MOTJF dested Yoda, Master Of The Force analog leftover Scott Morgan. "
    "Home One : WH dested Home One: War Room analog leftover. "
    "WWTBAC dested We Wish To Board At Once analog leftover Veasey. "
    "Leia dested Princess Leia True analog leftover Veasey. "
    "Antilles Maneuver combo dested Antilles Maneuver & Rebel Reinforcements analog leftover McCune. "
    "Luke JK dested Luke Skywalker, Jedi Knight analog leftover Kelly. "
    "Jedi Saber dested Jedi Lightsaber analog leftover Kelly. "
    "SATM Combo dested Sorry About The Mess & Blaster Proficiency analog leftover Day 1 Nelson. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi analog leftover Kelly. "
    "LTWW dested Let The Wookiee Win True analog leftover Day 1 Nelson. "
    "Twin BT dested Dual Laser Cannon analog leftover Veasey. "
    "Obi in Red VII dested Obi-Wan In Radiant VII analog leftover Day 1 Nelson. "
    "ATP dested Anakin's Podracer analog leftover. "
    "HCF dested Han, Chewie, And The Falcon analog leftover Kelly. "
    "HFAMF dested Heading For The Medical Frigate analog leftover Day 1 Nelson. "
    "Dunk Down dested Wokling True analog leftover Kelly. "
    "Wookiee dested Wookiee Roar True analog leftover Kurten. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Nelson dested Aaron Nelson analog leftover Day 1. "
    "Username Airdog2003. LIGHT empty dest from filled Dark 60s. Deck Name SoCal Walkers. "
    "Imperial Occupation True dested Imperial Occupation / Imperial Control True analog leftover Rambo. "
    "MPCs (Light) dested Hoth: Main Power Generators analog leftover Rambo. "
    "Emperor's Reach dested Maarek Stele, The Emperor's Reach analog leftover Rambo. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Rambo. "
    "General Never dested General Nevar analog leftover Rambo. "
    "Tender Shield dested Endor Shield True analog leftover Rambo. "
    "Boba Prepared Hunter dested Boba Fett, Renowned Bounty Hunter analog leftover Hunter. "
    "Mandalorian FoF dested Jango Fett, The Assassin analog leftover. "
    "Ni Chuba Na dested Ni Chuba Na?? analog leftover Rambo. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's X-wing"),
    n("I'll Take The Hand Socket", True),
    n("Admiral Ackbar", True),
    n("Home One"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Yoda, Master Of The Force"),
    n("I Can't Believe He's Gone", True),
    n("Home One: War Room"),
    n("We Wish To Board At Once", qty=2),
    n("Princess Leia", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Luke Skywalker, Jedi Knight"),
    n("Jedi Lightsaber"),
    n("Sense"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Projection Of A Skywalker"),
    n("Maris Brood, Fallen Jedi"),
    n("Let The Wookiee Win", True),
    n("Disarmed"),
    n("Dual Laser Cannon"),
    n("Lando Calrissian, Scoundrel"),
    n("Corran Horn"),
    n("Naboo: Battle Plains"),
    n("JITHSAR"),
    n("Seeking An Audience", True),
    n("Scrambled Transmission", True),
    n("Mace Windu", True, qty=2),
    n("Sai'torr Kal Fas", True),
    n("Draw Their Fire"),
    n("Aroundley", True),
    n("AP-59"),
    n("I Feel The Conflict"),
    n("Naboo: Boss Nass' Chambers"),
    n("Impressive, Most Impressive", True),
    n("Obi-Wan In Radiant VII"),
    n("Master Qui-Gon", True),
    n("Luke's Blaster Rifle"),
    n("Master Qui-Gon"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Blaster Deflection", qty=2),
    n("Anakin's Podracer"),
    n("Han, Chewie, And The Falcon"),
    n("Your Insight Serves You Well"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Wookiee Roar", True),
    n("More Bullet", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("Do, Or Do Not", True),
    n("Battle Plan", True),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Ultimatum"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Main Power Generators"),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Mountains"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Imperial Justice", True),
    n("Operational As Planned", True),
    n("Imperial Command"),
    n("Ni Chuba Na??", True),
    n("Stop Motion", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Cold Feet", True),
    n("No Escape"),
    n("Juno Eclipse, Black Leader"),
    n("He Hasn't Come Back Yet"),
    n("Close Call", True),
    n("Hoth Blockade"),
    n("A Dark Time For The Rebellion", True),
    n("A Dark Time For The Rebellion"),
    n("Blizzard 4", qty=2),
    n("Alert My Star Destroyer"),
    n("Target The Main Generator"),
    n("Tempest 1"),
    n("Marquand In Blizzard 6"),
    n("Control"),
    n("Do They Have A Code Clearance?"),
    n("Walker Garrison"),
    n("We're In Attack Position Now"),
    n("Why Didn't You Tell Me", True),
    n("Admiral Motti", True),
    n("AT-AT Cannon", True),
    n("Blizzard 1", True),
    n("General Nevar"),
    n("Conquest", True),
    n("Imperial Decree", True),
    n("Flagship Executor"),
    n("Veers", True),
    n("Image Of The Dark Lord", True),
    n("Blizzard 2", True),
    n("Trample"),
    n("Victory"),
    n("Commander Igar", True),
    n("Admiral Piett"),
    n("Prepared Defenses", True),
    n("Imperial Decree"),
    n("Endor Shield", True),
    n("You May Start Your Landing"),
    n("Garindan", True),
    n("Sonic Bombardment", True, qty=2),
    n("Cloud City: Security Tower", True),
    n("Boba Fett, Renowned Bounty Hunter"),
    n("Jango Fett, The Assassin"),
    n("Slave I, Symbol Of Fear"),
    n("Tarkin's Bounty", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("That's It. Wipe Them Out"),
    n("A Useless Gesture", True),
    n("Battle Order", True),
    n("Allegations Of Corruption", True),
    n("Secret Plans"),
    n("Abyss", True),
    n("Fanfare", True, qty=2),
    n("You Cannot Hide Forever", True),
    n("Leave Them To Me", True),
    n("Oppressive Enforcement"),
]
DS_ADD = []
