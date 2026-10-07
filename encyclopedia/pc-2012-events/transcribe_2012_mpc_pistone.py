#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Mike Pistone.

Source: 2012mpcday1.pdf pages 121–122 (2010 form, 12 shields).
Name PISTONE dested Mike Pistone (skill / generate CANON Pistone).
p121 Light Watch Your Step. p122 Dark Imperial Occupation / Imperial Control.
Username Jack McCoy (Light) / Jack Bauer (Dark).
Pack player-stubs/Mike_Pistone.wiki.
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Mike Pistone"
USERNAME = "Jack McCoy"
LS_USERNAME = "Jack McCoy"
DS_USERNAME = "Jack Bauer"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 121
DS_PAGE = 122
LS_SCAN = "2012 Match Play Championship Day 1 Mike Pistone LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Mike Pistone DS.png"
LS_DECK_NAME = "WYS V"
DS_DECK_NAME = '"Agnos"-TIC'
NOTE = "Handwritten 2010 Xerox form. Username Jack McCoy / Jack Bauer."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name PISTONE dested Mike Pistone. "
    "Username JACK McCOY dested Jack McCoy. LIGHT checked. Deck Name WYS V. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough empty. "
    "Spaceport: City dested Spaceport City. Insurrection & Aim High dested analog O'Hare. "
    "AM & RR empty AND True kept separate analog Foth. "
    "Booster In Pulsar Skate dested without True virtual-only analog Pinto. "
    "BoShek's Modified Freighter dested as written analog Shannon. "
    "Look Towards dested as written. Lando, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi analog Kelly. "
    "Chewie dested Chewie True analog Lepine. "
    "Evacuation Control True dested Evacuation Control (V). "
    "AFA True dested Anger, Fear, Aggression True in the 60 analog Casey. "
    "Unique 60. Shields 12. Jabba's Prize True dested without True analog O'Hare. "
    "Do, Or Do Not empty dested without True analog Murray."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name PISTONE dested Mike Pistone. "
    "Username JACK BAUER dested Jack Bauer. DARK checked. Deck Name \"Agnos\"-TIC. "
    "IO/IC True dested Imperial Occupation / Imperial Control True. "
    "Protocol Failure dested without True analog Pinto. "
    "Imperial Decree True AND empty kept separate analog Foth. "
    "Omni Box & It's Worse dested Ommni Box & It's Worse analog Hollingworth. "
    "Black Leader dested Juno Eclipse, Black Leader analog Eier. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach analog Eier. "
    "Gatchin Bay True dested Hoth: Echo Docking Bay analog walker missing site. "
    "Veers True dested General Veers True x2. "
    "Hoth defensive perimeter dested Hoth: Defensive Perimeter (3rd Marker) analog Eier. "
    "Hoth mountains dested Hoth: Mountains (6th Marker) analog Eier. "
    "Prepared Defenses True dested in the 60 analog Casey. "
    "Do They Have A Code Clearance? empty dested in the 60 analog Casey. "
    "K&D True dested Knowledge And Defense True in the 60 analog Murray. "
    "We'll Let Fate-a Decide, Huh? dested analog Cullen. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Captain Han Solo"),
    n("Millennium Falcon", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("Yoda, Great Warrior", qty=2),
    n("Enhanced Proton Torpedoes", True),
    n("Corellian Slip", True),
    n("Imperial Atrocity", True, qty=3),
    n("Chewie", True),
    n("Tantive IV", True),
    n("Spaceport Scoundrels Guild"),
    n("Dash Rendar", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("No Questions Asked", True, qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Barrier"),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Booster In Pulsar Skate"),
    n("Grimtaash"),
    n("BoShek's Modified Freighter"),
    n("K'lor'slug", True),
    n("Evacuation Control", True),
    n("Spaceport Street"),
    n("Houjix"),
    n("Leia, Rebel Princess"),
    n("Antilles Maneuver", True),
    n("Lando Calrissian, Scoundrel"),
    n("Look Towards"),
    n("Menace Fades"),
    n("Maris Brood, Fallen Jedi"),
    n("Spaceport Docking Bay"),
    n("Laudica", True),
    n("BoShek, Brash Smuggler"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Corran Horn", qty=2),
    n("Seeking An Audience", True),
    n("Palejo Reshad"),
    n("Spiral"),
    n("Mirax Terrik"),
    n("Home One: Docking Bay"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Protocol Failure"),
    n("Imperial Decree", True),
    n("Tarkin's Bounty", True),
    n("Why Didn't You Tell Me?", True),
    n("Marquand In Blizzard 6"),
    n("Cold Feet", True),
    n("Imperial Command", qty=3),
    n("Katana"),
    n("Operational As Planned", True),
    n("Victory", qty=2),
    n("Trample", qty=2),
    n("Control", qty=2),
    n("Target The Main Generator"),
    n("Admiral Motti", True),
    n("Ommni Box & It's Worse"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("No Escape"),
    n("Blizzard 1", True),
    n("Walker Garrison"),
    n("General Veers", True, qty=2),
    n("Maarek Stele, The Emperor's Reach"),
    n("Blizzard 4"),
    n("We're In Attack Position Now", qty=2),
    n("Juno Eclipse, Black Leader"),
    n("Grand Moff Tarkin", True, qty=2),
    n("Blockade Support Ship"),
    n("Force Push", True),
    n("Conquest", True),
    n("Devastator", True),
    n("Darth Vader", True),
    n("Grand Admiral Thrawn"),
    n("Commander Igar", True),
    n("Hoth: Echo Docking Bay", True),
    n("Hoth"),
    n("Hoth Blockade"),
    n("Hoth: Main Power Generators"),
    n("General Nevar"),
    n("AT-AT Cannon", True),
    n("Tempest 1"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Mountains (6th Marker)"),
    n("Hoth: Ice Plains", True),
    n("Blizzard 2", True),
    n("Prepared Defenses", True),
    n("Imperial Decree"),
    n("Ni Chuba Na??", True),
    n("You May Start Your Landing"),
    n("Endor Shield", True),
    n("Do They Have A Code Clearance?"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Death Star Sentry", True),
    n("Firepower", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("There Is No Try"),
]
DS_ADD = []
