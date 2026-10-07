#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Mark Peterson.

Source: 2012NationalsDay1.pdf pages 58–59 (handwritten 2010 Xerox, 12 shields).
p58 Dark / p59 Light Name Mark Peterson Username Lukes Bionic Hand dested Mark Peterson analog leftover 2008 Worlds.
Pack player-stubs/Mark_Peterson.wiki.
"""
from __future__ import annotations

PLAYER = "Mark Peterson"
USERNAME = "Lukes Bionic Hand"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 59
DS_PAGE = 58
LS_SCAN = "2012 US Nationals Day 1 Mark Peterson LS.png"
DS_SCAN = "2012 US Nationals Day 1 Mark Peterson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Mark Peterson dested Mark Peterson analog leftover 2008 Worlds. "
    "Username Lukes Bionic Hand. Event Date 6/9/12 Event Name US Nats."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Mark Peterson dested Mark Peterson analog leftover 2008 Worlds. "
    "Username Lukes Bionic Hand. LIGHT checked. Event Date 6/9/12 Event Name US Nats. "
    "Deck Name Bail Hearing stays off the article. "
    "LS_START Plead My Case To The Senate dested Plead My Case To The Senate / Sanity And Compassion analog leftover Jake Nelson. "
    "AFA dested Anger, Fear, Aggression True analog leftover Cooleo IN THE 60. "
    "Coruscant nightclub dested Coruscant: Night Club analog leftover Jake Nelson. "
    "Bail Organa Father Of Rebellion dested Bail Organa, Father Of The Rebellion leftover_xerox dest-as-written x2. "
    "Senator Jar Jar dested Senator Jar Jar Binks analog leftover Fernando. "
    "Major Haashn dested Major Haash'n analog leftover Cooleo. "
    "Sai tor kal fas dested Sai'torr Kal Fas True analog leftover Olson Virtual Block. "
    "Sorry About The Mess combo dested Sorry About The Mess & Blaster Proficiency analog leftover Anderson. "
    "Shield Optimism dested Let's Keep A Little Optimism Here True analog leftover. "
    "Shield Insight dested Your Insight Serves You Well True analog leftover. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Mark Peterson dested Mark Peterson analog leftover 2008 Worlds. "
    "Username Lukes Bionic Hand. DARK checked. Event Date 6/9/12 Event Name US Nats. "
    "Deck Name Wisconsin Recall AKA Stop The Imperial Walker stays off the article. "
    "Imperial Occupation dested Imperial Occupation / Imperial Control True analog leftover Olson Twigg. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Ni Chuba Na dested Ni Chuba Na?? True analog leftover. "
    "Masterful Move And Endor Occupation dested Masterful Move & Endor Occupation analog leftover Morgan. "
    "Cease Fire dested Cease Fire! analog leftover MPC x2. "
    "Where Are You Taking This dested Where Are You Taking This ... Thing? analog leftover Gemme. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover George. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach analog leftover MPC Bollentino. "
    "Imperial Command dested Imperial Command analog leftover Brady x3 unique overcount. "
    "Shield Fate dested We'll Let Fate-a Decide, Huh? analog leftover Kurten. "
    "Shield 12 blank skip. Unique 60. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Anger, Fear, Aggression", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Strike Planning"),
    n("Quick Draw", True),
    n("Naboo: Battle Plains"),
    n("Coruscant: Night Club"),
    n("Coruscant (Episode I)"),
    n("Home One: War Room"),
    n("Home One"),
    n("Han, Chewie, And The Falcon"),
    n("Wedge In Red Squadron 1"),
    n("Bail Organa, Father Of The Rebellion", qty=2),
    n("Senator Leia Organa"),
    n("Senator Padmé Amidala"),
    n("Senator Jar Jar Binks"),
    n("Mas Amedda"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Mace Windu", True, qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Plo Koon"),
    n("Corran Horn"),
    n("Lando Calrissian, Scoundrel"),
    n("Admiral Ackbar", True),
    n("Major Haash'n"),
    n("Coruscant Guard"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Scrambled Transmission", True),
    n("Sai'torr Kal Fas", True),
    n("Imperial Atrocity", True),
    n("Hindsight", True),
    n("Senate Hovercam"),
    n("Seeking An Audience", True),
    n("Launching The Assault"),
    n("So This Is How Liberty Dies"),
    n("Menace Fades"),
    n("Under Attack"),
    n("Blaster Deflection", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Might Of The Republic", qty=3),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Rebel Leadership", True, qty=2),
    n("Senator Mon Mothma"),
    n("Jedi Levitation", True),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business", True),
    n("Ultimatum"),
    n("Only Jedi Carry That Weapon"),
    n("Aim High"),
    n("The Professor", True),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Knowledge And Defense", True),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Main Power Generators"),
    n("Imperial Decree"),
    n("You May Start Your Landing"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Hoth: Mountains"),
    n("Target The Main Generator"),
    n("AT-AT Cannon", True),
    n("Masterful Move & Endor Occupation"),
    n("Cease Fire!", qty=2),
    n("Where Are You Taking This ... Thing?"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Garindan", True),
    n("Commander Igar", True),
    n("Blockade Support Ship"),
    n("Imperial Decree", True),
    n("Conquest", True),
    n("Victory"),
    n("Cold Feet", True, qty=2),
    n("Image Of The Dark Lord", True),
    n("Hoth Blockade"),
    n("Grand Moff Tarkin", True),
    n("Admiral Motti", True),
    n("Juno Eclipse, Black Leader"),
    n("Darth Vader", True),
    n("General Nevar"),
    n("Veers", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Marquand In Blizzard 6"),
    n("Tempest 1"),
    n("Hoth: Defensive Perimeter"),
    n("U-3PO"),
    n("Grand Admiral Thrawn"),
    n("Admiral Piett"),
    n("We're In Attack Position Now", qty=2),
    n("No Escape"),
    n("Do They Have A Code Clearance?"),
    n("Control", qty=2),
    n("Walker Garrison"),
    n("Prepared Defenses"),
    n("Trample", qty=2),
    n("Flagship Executor", qty=2),
    n("Alert My Star Destroyer"),
    n("Imperial Command", qty=3),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Imperial Detention"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Fanfare", True),
    n("Secret Plans"),
]
DS_ADD = []
