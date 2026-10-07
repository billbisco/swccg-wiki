#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Chris Schoenthal.

Source: 2012NationalsDay1.pdf pages 64–65 (handwritten 2010 Xerox, 12 shields).
p64 Light / p65 Dark Name Chris Schoenthal Username imrahil327 dested Chris Schoenthal analog leftover 2012 MPC / 2013 Alderaan / 2014 TMW.
Pack pages/Chris_Schoenthal.wiki (is_bio True Tournament Advocate).
"""
from __future__ import annotations

PLAYER = "Chris Schoenthal"
USERNAME = "imrahil327"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 64
DS_PAGE = 65
LS_SCAN = "2012 US Nationals Day 1 Chris Schoenthal LS.png"
DS_SCAN = "2012 US Nationals Day 1 Chris Schoenthal DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Chris Schoenthal dested Chris Schoenthal analog leftover 2012 MPC. "
    "Username imrahil327. Event Date 6/9/12 Event Name Nationals. Do not dest as Chris Haglund."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Schoenthal dested Chris Schoenthal analog leftover 2012 MPC. "
    "Username imrahil327. LIGHT checked. Event Date 6/9/12 Event Name Nationals. "
    "Deck Name Un-Nedly stays off the article. "
    "LS_START Yavin 4: Massassi Throne Room analog leftover Anderson. "
    "Insurrection & Aim High dested Insurrection & Aim High analog leftover Morgan. "
    "Sai'torr dested Sai'torr Kal Fas True analog leftover Olson Virtual Block. "
    "Line 7 crossed dest Hindsight True analog leftover replacement. "
    "A Jedi's Plans dested A Jedi's Plans analog leftover Anderson. "
    "Han Chewie and the Falcon dested Han, Chewie, And The Falcon analog leftover x2. "
    "Antilles combo dested Antilles Maneuver & Rebel Reinforcements analog leftover MPC Schoenthal. "
    "SATM&BP dested Sorry About The Mess & Blaster Proficiency analog leftover x2 unique overcount. "
    "Wesa Gotta dested Wesa Gotta Grand Army analog leftover Brady. "
    "Leia dested Princess Leia True analog leftover Olson. "
    "Leia RP dested Leia, Rebel Princess analog leftover Anderson. "
    "AFA dested Anger, Fear, Aggression True analog leftover Cooleo IN THE 60. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Schoenthal dested Chris Schoenthal analog leftover 2012 MPC. "
    "Username imrahil327. DARK checked. Event Date 6/9/12 Event Name Nationals. "
    "Deck Name The Iron Price stays off the article. "
    "DS_START Set Your Course For Alderaan / Flip dested Set Your Course For Alderaan / The Ultimate Power In The Universe analog leftover Jake Nelson. "
    "Front Drive Yards dested Kuat Drive Yards True analog leftover Hanson. "
    "A Million Voices dested A Million Voices Crying Out analog leftover McCune. "
    "Darth Maul With Lightsaber dested analog leftover Brady x2. "
    "Darth Sidious dested Darth Sidious analog leftover Herold x3. "
    "Operational As Planned dested Operational As Planned True analog leftover Jake. "
    "Force Field dested Force Field True analog leftover Brady. "
    "Why Didn't You Tell Me dested Why Didn't You Tell Me? True analog leftover Anderson. "
    "TIE Sentry dested TIE Sentry Ships True analog leftover Jake. "
    "A Bright Center dested A Bright Center To The Universe analog leftover Aue. "
    "K&D dested Knowledge And Defense analog leftover Cooleo IN THE 60. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Quick Draw", True),
    n("Heading For The Medical Frigate"),
    n("Sai'torr Kal Fas", True),
    n("Hindsight", True),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("A Jedi's Plans"),
    n("Jedi Lightsaber", True),
    n("Leia's Blaster Rifle"),
    n("Luke's Lightsaber"),
    n("Home One"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Tantive IV", True),
    n("Grimtaash"),
    n("Home One: War Room"),
    n("Coruscant: Night Club"),
    n("Kiffex"),
    n("Home One: Docking Bay"),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Hoth: Echo Docking Bay"),
    n("Scrambled Transmission", True),
    n("Escape Pod", True),
    n("Houjix"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Sense", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Were You Looking For Me?"),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Blaster Deflection", qty=2),
    n("Wesa Gotta Grand Army"),
    n("Speak With The Jedi Council"),
    n("Rebel Leadership", True, qty=2),
    n("Princess Leia", True),
    n("Leia, Rebel Princess"),
    n("Admiral Ackbar", True),
    n("Threepio With His Parts Showing"),
    n("Padmé Naberrie", True),
    n("Corran Horn"),
    n("Lando Calrissian, Scoundrel"),
    n("Yoda, Master Of The Force"),
    n("Obi-Wan With Lightsaber"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Mace Windu", True),
    n("Mace Windu"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("A Tragedy Has Occurred", True),
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Battle Plan", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("A Million Voices Crying Out"),
    n("Kuat Drive Yards", True),
    n("Imperial Stockpile"),
    n("Laser Cannon Battery"),
    n("Prepared Defenses", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Sidious", qty=3),
    n("Garindan", True),
    n("Garindan"),
    n("Arica"),
    n("U-3PO"),
    n("Avenger"),
    n("Judicator", qty=2),
    n("Stalker", True),
    n("Thunderflare"),
    n("Accuser"),
    n("Conquest", True),
    n("Devastator", True),
    n("Victory"),
    n("Kiffex"),
    n("Corulag"),
    n("Nal Hutta"),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Intensify The Forward Batteries", qty=2),
    n("Superlaser"),
    n("Commence Primary Ignition"),
    n("Relentless Pursuit", qty=2),
    n("Overwhelmed"),
    n("Operational As Planned", True),
    n("Force Field", True),
    n("Imperial Barrier"),
    n("Ghhhk"),
    n("Control"),
    n("Why Didn't You Tell Me?", True),
    n("Cold Feet", True),
    n("Lightsaber Deficiency", True),
    n("Lightsaber Deficiency"),
    n("Force Push", True),
    n("Close Call", True),
    n("TIE Sentry Ships", True),
    n("Something Special Planned For Them", True),
    n("Lateral Damage"),
    n("A Bright Center To The Universe"),
    n("The Phantom Menace"),
    n("Imperial Propaganda", True),
    n("Imperial Propaganda"),
    n("Image Of The Dark Lord", True),
    n("Protocol Failure"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("There Is No Try"),
    n("Fanfare", True),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Firepower", True),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Allegations Of Corruption"),
]
DS_ADD = []
