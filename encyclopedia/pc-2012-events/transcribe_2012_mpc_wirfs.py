#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Chris Wirfs.

Source: 2012mpcday1.pdf pages 147–148 (2010 form, 12 shields).
Name Chris Wirfs dested Chris Wirfs analog leftover WIRFS.
Username itcouldbewirfs.
p147 Light Luck Deck. p148 Dark Wirfs' Walkin'.
Pack player-stubs/Chris_Wirfs.wiki (is_bio False).
Do not dest as a new person.
Do not rewrite 2013 Worlds leftover Hunt Down / Communing.
"""
from __future__ import annotations

PLAYER = "Chris Wirfs"
USERNAME = "itcouldbewirfs"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 147
DS_PAGE = 148
LS_SCAN = "2012 Match Play Championship Day 1 Chris Wirfs LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Chris Wirfs DS.png"
LS_DECK_NAME = "Luck Deck"
DS_DECK_NAME = "Wirfs' Walkin'"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Wirfs dested Chris Wirfs analog leftover WIRFS. "
    "Username itcouldbewirfs. LIGHT checked. Deck Name Luck Deck Event Date 2/12/12 Event Name 2012 MPC. "
    "Do not dest as a new person. "
    "Do not rewrite 2013 Worlds leftover Communing. "
    "Yavin 4: Massassi Throne Room dested analog leftover TRM. "
    "Hindsight True dested Hindsight True analog leftover. "
    "Sorry About the Mess Combo dested Sorry About The Mess & Blaster Proficiency analog leftover. "
    "Luke Skywalker SITF dested Luke Skywalker, Strong In The Force True analog leftover. "
    "Antilles Maneuver & Rebel Reinforcements dested analog leftover. "
    "HCF dested Han, Chewie, And The Falcon analog leftover. "
    "Hear Me Baby dested Hear Me Baby, Hold Together True analog leftover. "
    "AFA True dested Anger, Fear, Aggression True analog leftover IN THE 60. "
    "Rebel Leadership True x3 sheet-accurate. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Wirfs dested Chris Wirfs analog leftover WIRFS. "
    "Username itcouldbewirfs. DARK checked. Deck Name Wirfs' Walkin'. "
    "Do not dest as a new person. "
    "Do not rewrite 2013 Worlds leftover Hunt Down. "
    "Imperial Occupation/Imp Con True dested Imperial Occupation / Imperial Control True analog leftover. "
    "Hoth: Mountains dested Hoth: Mountains (6th Marker) analog leftover. "
    "Endor Shield True dested analog leftover. "
    "U-3PO dested U-3PO analog leftover. "
    "Hoth Blockade True dested analog leftover. "
    "Grindan True dested Garindan True analog leftover. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach analog Eier. "
    "Something Special Planned For The dested Something Special Planned For Them True analog leftover. "
    "General Veers Nevar True dested General Nevar True analog leftover. "
    "Black Leader dested Juno Eclipse, Black Leader analog Eier. "
    "Veers True dested Veers True analog leftover. "
    "Hoth: Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker) analog leftover. "
    "Hoth: Main Generators dested Hoth: Main Power Generators analog leftover. "
    "Alert My Star Destroyer dested analog leftover. "
    "We'll Let Fate Decide dested We'll Let Fate-a Decide, Huh? analog leftover. "
    "K&D True dested Knowledge And Defense True analog leftover IN THE 60. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Hindsight", True),
    n("Hoth: Echo Docking Bay"),
    n("Home One: War Room"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Coruscant: Night Club", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("A Jedi's Plans", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Corran Horn"),
    n("Blaster Deflection"),
    n("Leia's Blaster Rifle"),
    n("Leia, Rebel Princess"),
    n("Mace Windu", True),
    n("Jedi Lightsaber", True),
    n("Sai'torr Kal Fas", True),
    n("Grimtaash"),
    n("Artoo-Detoo In Red 5"),
    n("Hear Me Baby, Hold Together", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Sense"),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel"),
    n("Luke Skywalker, Strong In The Force", True),
    n("Luke's Lightsaber"),
    n("Houjix"),
    n("Sense"),
    n("Blaster Deflection"),
    n("Kiffex"),
    n("A Jedi's Resilience", True),
    n("Rebel Leadership", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("A Jedi's Resilience", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Imperial Atrocity", True),
    n("Admiral Ackbar", True),
    n("Home One"),
    n("Han, Chewie, And The Falcon"),
    n("Luke Skywalker, Strong In The Force", True),
    n("Speak With The Jedi Council"),
    n("Han, Chewie, And The Falcon"),
    n("Rebel Leadership", True),
    n("Ki-Adi-Mundi", True),
    n("Mace Windu", True),
    n("Speak With The Jedi Council"),
    n("Lando Calrissian, Scoundrel"),
    n("Rebel Leadership", True),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience", True),
    n("Escape Pod"),
    n("Scrambled Transmission", True),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Home One: Docking Bay"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense", True),
    n("Yavin Sentry", True),
    n("Aim High", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("We're In Attack Position Now"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Hoth"),
    n("Imperial Decree"),
    n("Endor Shield", True),
    n("You May Start Your Landing"),
    n("Ni Chuba Na??", True),
    n("Do They Have A Code Clearance?", True),
    n("Imperial Command"),
    n("U-3PO"),
    n("Image Of The Dark Lord", True),
    n("Walker Garrison"),
    n("Blizzard 1", True),
    n("Conquest", True),
    n("ISB Sector Commander", True),
    n("Flagship Executor"),
    n("Hoth Blockade", True),
    n("Prepared Defenses"),
    n("Lightsaber Deficiency", True),
    n("Grand Admiral Thrawn"),
    n("Blizzard 2", True),
    n("Masterful Move & Endor Occupation"),
    n("General Veers", True),
    n("Grand Moff Tarkin", True),
    n("Garindan", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Stop Motion", True),
    n("Admiral Motti", True),
    n("Operational As Planned", True),
    n("Imbalance & Kintan Strider", True),
    n("Darth Vader", True),
    n("A Dark Time For The Rebellion", True),
    n("Cold Feet", True),
    n("AT-AT Cannon", True),
    n("Marquand In Blizzard 6", True),
    n("Blizzard 4"),
    n("Protocol Failure", True),
    n("Victory", True),
    n("A Dark Time For The Rebellion", True),
    n("Tempest 1"),
    n("Target The Main Generator"),
    n("Control"),
    n("Something Special Planned For Them", True),
    n("Tarkin's Bounty", True),
    n("Commander Igar", True),
    n("Trample"),
    n("Conquest", True),
    n("Admiral Piett"),
    n("Victory", True),
    n("General Nevar", True),
    n("Control"),
    n("Imperial Command"),
    n("Juno Eclipse, Black Leader"),
    n("Veers", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Main Power Generators"),
    n("Alert My Star Destroyer"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Abyss"),
    n("Secret Plans"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
