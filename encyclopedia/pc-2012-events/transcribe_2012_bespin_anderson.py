#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: John Anderson.

Source: 2012BespinRegionals.pdf pages 29–30.
p29 Light typed 2010 Xerox / p30 Dark typed 2010 Xerox.
Name John Anderson dested John Anderson analog leftover TMW/Nats/MPC /
player-stubs/John_Anderson.wiki. Username puck71 dested Puck71 analog leftover TMW.
Do not dest as a new person. Do not dest TMW Day 1 / TMW Day 2 / 2012 Nats /
2012 MPC Anderson 60s again. Pack player-stubs/John_Anderson.wiki.
"""
from __future__ import annotations

PLAYER = "John Anderson"
USERNAME = "Puck71"
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 29
DS_PAGE = 30
LS_SCAN = "2012 Bespin Regionals John Anderson LS.png"
DS_SCAN = "2012 Bespin Regionals John Anderson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p29 Light typed 2010 Xerox / p30 Dark typed 2010 Xerox. "
    "Name John Anderson dested John Anderson analog leftover TMW/Nats/MPC / "
    "player-stubs/John_Anderson.wiki. Username puck71 dested Puck71 analog leftover TMW. "
    "Event Date 7/14/12 / 07/14/2012 Event bespin regionals. "
    "Deck Name trm / dumb walkers dested off article dest both as Bespin facing pair. "
    "Do not dest as a new person. Do not dest TMW Day 1 / TMW Day 2 / 2012 Nats / "
    "2012 MPC Anderson 60s again. Pack player-stubs/John_Anderson.wiki."
)
LS_NOTE = (
    "Typed 2010 Xerox p29 Light. Name John Anderson dested John Anderson. Username puck71 dested Puck71. "
    "LIGHT checked. Event Date 7/14/12 Event bespin regionals. Deck Name trm dested off article. "
    "Line 1 clipped dest Yavin 4: Massassi Throne Room analog leftover TMW Anderson (starting location, no Objective). "
    "Line 11 Sorry About The Mess & Blaster Proficiency dest analog leftover TMW Anderson. "
    "Sheet Naboo: Boss Nass Chambers dested Naboo: Boss Nass' Chambers analog leftover TMW. "
    "Line 31 Naboo: Theed Palace Throne Room crossed dest Sense empty analog leftover TMW Anderson. "
    "Line 41 Hindsight True dest analog leftover TMW Anderson. "
    "Line 55 Coruscant: Night Club dest analog leftover Peterson. "
    "Armed And Dangerous & Krayt Dragon Howl dest analog leftover TMW Anderson. "
    "Bron Burs True dest as written analog leftover Cooleo. "
    "Anger, Fear, Aggression True IN THE 60. "
    "Shield 12 empty skip unique 11 sheet-accurate analog leftover clip. Unique 60 shields 11."
)
DS_NOTE = (
    "Typed 2010 Xerox p30 Dark. Name John Anderson dested John Anderson. Username puck71 dested Puck71. "
    "DARK checked. Event Date 07/14/2012 Event bespin regionals. Deck Name dumb walkers dested off article. "
    "Line 1 clipped dest Imperial Occupation / Imperial Control True analog leftover Peterson/Rambo walker. "
    "Imperial Decree empty line 5 and True line 6 kept separate. "
    "Ni Chuba Na? True dest analog leftover leftover_xerox. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach analog leftover Peterson. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Peterson. "
    "We're In Attack Position Now empty qty=2 covering 30–31. "
    "Line 41 clipped dest Imperial Command empty qty=2 covering 41–42 analog leftover Rambo. "
    "Line 54 the Mandalorian Father of Fett dested Jango Fett, The Assassin analog leftover 2013 Shannon. "
    "Line 59 crossed dest Tarkin's Bounty True analog leftover leftover_xerox. "
    "Knowledge And Defense True IN THE 60. "
    "Shield 12 empty skip unique 11 sheet-accurate analog leftover clip. Unique 60 shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Wokling", True),
    n("Smoke Screen", qty=3),
    n("Clash Of Sabers", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Mace Windu", True, qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke Skywalker, Strong In The Force"),
    n("Lando Calrissian, Scoundrel"),
    n("Home One"),
    n("Admiral Ackbar", True),
    n("Rebel Leadership", True, qty=3),
    n("Speak With The Jedi Council", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber"),
    n("Home One: War Room"),
    n("Kiffex"),
    n("Sense"),
    n("A Jedi's Plans"),
    n("Obi-Wan's Journal"),
    n("Luke's Bionic Hand"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Menace Fades"),
    n("Draw Their Fire"),
    n("Hindsight", True),
    n("Seeking An Audience", True),
    n("Scrambled Transmission", True),
    n("Obi-Wan With Lightsaber"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Yoda, Master Of The Force"),
    n("Alter", True),
    n("A Jedi's Resilience"),
    n("Sai'torr Kal Fas", True),
    n("IL-19"),
    n("Blaster Deflection"),
    n("Han, Chewie, And The Falcon"),
    n("Tantive IV", True),
    n("Coruscant: Night Club"),
    n("Let The Wookiee Win", True),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Demotion"),
    n("Bron Burs", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Weapon"),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("The Professor", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Main Power Generators"),
    n("Imperial Decree"),
    n("Imperial Decree", True),
    n("Prepared Defenses", True),
    n("You May Start Your Landing"),
    n("Ni Chuba Na?", True),
    n("Endor Shield", True),
    n("Hoth: Mountains"),
    n("Tempest 1"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Marquand In Blizzard 6"),
    n("Walker Garrison"),
    n("Hoth: Defensive Perimeter"),
    n("Veers", True),
    n("General Nevar"),
    n("Grand Admiral Thrawn"),
    n("Admiral Motti", True),
    n("Do They Have A Code Clearance?"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Juno Eclipse, Black Leader"),
    n("Darth Vader", True),
    n("Commander Igar", True),
    n("Grand Moff Tarkin", True),
    n("Admiral Piett"),
    n("We're In Attack Position Now", qty=2),
    n("Cold Feet", True),
    n("Stop Motion", True),
    n("He Hasn't Come Back Yet"),
    n("Trample"),
    n("Alert My Star Destroyer!"),
    n("Operational As Planned", True),
    n("Imperial Justice", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Imperial Command", qty=2),
    n("Flagship Executor"),
    n("Conquest", True),
    n("Victory"),
    n("Blockade Support Ship"),
    n("Hoth Blockade"),
    n("Target The Main Generator"),
    n("AT-AT Cannon", True),
    n("Cloud City: Security Tower", True),
    n("Close Call", True),
    n("Sonic Bombardment", True, qty=2),
    n("Jango Fett, The Assassin"),
    n("Garindan", True),
    n("No Escape"),
    n("Slave I, Symbol Of Fear"),
    n("Boba Fett, Prepared Hunter"),
    n("Tarkin's Bounty", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Resistance"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
]
DS_ADD = []
