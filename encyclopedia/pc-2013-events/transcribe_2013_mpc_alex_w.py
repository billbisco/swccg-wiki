#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Alex W Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Alex W"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 113
DS_PAGE = 114
LS_SCAN = "2013 Match Play Championship p113 Alex W LS.png"
DS_SCAN = "2013 Match Play Championship p114 Alex W DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Typed-looking 2010 Xerox Print Form. Alex W. Light. Deck title Lando Luxury Lines. "
    "Quiet Mining Colony dested Quiet Mining Colony / Independent Operation (Decipher; (V) unchecked). "
    "Leesub Sirlin dested Leesub Sirln (V). Lando Clarissian dested Lando Calrissian, Unlikely Hero. "
    "(V) written in the title and checked dested with n(name, True); (V) not kept in the name string. "
    "Luke Skywalker, Rebel Heo dested Luke Skywalker, Rebel Hero. "
    "Obi-Wan with Lightsaber dested Obi-Wan With Lightsaber. "
    "Seeking an Audience dested Seeking An Audience (V). Honor of the Jedi dested Honor Of The Jedi. "
    "Beldon's Eye (V). Evacuation Control (V). Anger, Fear, Aggression (V). "
    "Path of Least Resistance dested Path Of Least Resistance. Corellian Slip (V). "
    "Alternativesto Fighting dested Alternatives To Fighting. Quite a Mercenary dested Quite A Mercenary. "
    "Antilles Maneuver & Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Sorry About the Mess & Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "Houjix & Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Heading for the Medical Frigate dested Heading For The Medical Frigate. "
    "Lando's Luxury Yacht dested Lady Luck. Gold Leader in Gold 1 dested Gold Leader In Gold 1 (V). "
    "Wedge in Red Squadron 1 dested Wedge In Red Squadron 1. "
    "Han, Chewie, and the Falcon dested Han, Chewie, And The Falcon. "
    "Simple Tricks and Nonsense dested Simple Tricks And Nonsense. Do, Or Do Not as written. "
    "Form lines 39–40 numbered as 39–40 (typed). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Typed-looking 2010 Xerox Print Form. Alex W. Dark. Deck title LATOR - Losses Are Their Own Reward. "
    "Wookiee Slaving Operation dested Wookiee Slaving Operation / Indentured To The Empire (Decipher; (V) unchecked). "
    "We're In Attach Position Now dested We're In Attack Position Now. "
    "Jabba the Hutt dested Jabba The Hutt (V). "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Bossk with Mortar Gun dested Bossk With Mortar Gun (V). "
    "Power of the Hutt dested Power Of The Hutt. Jabba's Haven as written. "
    "Baktoid Armor Workship dested Baktoid Armor Workshop. "
    "Den of Thieves & Special Delivery dested Den Of Thieves & Special Delivery. "
    "T'doshok Hunting Vow as written. Scum and Villany dested Scum And Villainy. "
    "Knowledge and Defense dested Knowledge And Defense (V). "
    "Operational as Planned dested Operational As Planned (V). "
    "Abyssin Ornament as written. Cease Fire! as written. "
    "Sith Fury & End This Destructive Conflict dested Sith Fury & End This Destructive Conflict. "
    "Kashyyyk: Skyhook Platofrm dested Kashyyyk: Skyhook Platform. "
    "Slave 1, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Elis in Hinthra dested Mist Hunter (V). "
    "Defensive Shields blank. "
    "Form lines 39–40 numbered as 39–40 (typed). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Yoxgit"),
    n("Leesub Sirln", True),
    n("Mirax Terrik"),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Harc Seff", True),
    n("Pucumir Thryss"),
    n("Kebyc", True),
    n("Yoda, Great Warrior"),
    n("Princess Leia", True, qty=2),
    n("Luke Skywalker, Rebel Hero", qty=2),
    n("Corran Horn"),
    n("Obi-Wan With Lightsaber"),
    n("Padme Naberrie", True),
    n("Wokling", True),
    n("Cloud City Celebration", qty=2),
    n("Seeking An Audience", True),
    n("Keeping The Empire Out Forever"),
    n("Menace Fades"),
    n("Honor Of The Jedi"),
    n("Beldon's Eye", True),
    n("Evacuation Control", True),
    n("Imperial Atrocity"),
    n("Anger, Fear, Aggression", True),
    n("Path Of Least Resistance", qty=2),
    n("Corellian Slip", True),
    n("Blast The Door, Kid!", qty=2),
    n("Alternatives To Fighting"),
    n("Choke"),
    n("Quite A Mercenary"),
    n("Rebel Barrier", qty=2),
    n("Desperate Reach", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Houjix & Out Of Nowhere", qty=2),
    n("Heading For The Medical Frigate"),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: West Gallery"),
    n("Cloud City: Guest Quarters"),
    n("Cloud City: North Corridor"),
    n("Bespin"),
    n("Booster's Star Destroyer"),
    n("Spiral", qty=2),
    n("Overseer"),
    n("Booster In Pulsar Skate"),
    n("Lady Luck"),
    n("Gold Leader In Gold 1", True),
    n("Wedge In Red Squadron 1"),
    n("Han, Chewie, And The Falcon"),
    n("Leia's Blaster Rifle"),
    n("Luke's Blaster Pistol"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Yavin Sentry", True),
    n("Don't Do That Again"),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Chasm", True),
    n("Do, Or Do Not"),
]
LS_ADD = []

DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("We're In Attack Position Now", qty=2),
    n("Jabba The Hutt", True),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Chevin", True, qty=2),
    n("Bossk With Mortar Gun", True, qty=2),
    n("Ephant Mon"),
    n("Mercenary Pilot"),
    n("Ponda Baba", True),
    n("Gela Yeens", True),
    n("Trandoshan", qty=7),
    n("OOM Command Battle Droid", qty=2),
    n("OOM-9", True),
    n("Mercenary Slavers"),
    n("Power Of The Hutt"),
    n("Hutt Influence"),
    n("Jabba's Haven"),
    n("Baktoid Armor Workshop"),
    n("Deployment Orders"),
    n("Molator", True),
    n("Den Of Thieves & Special Delivery"),
    n("T'doshok Hunting Vow"),
    n("Scum And Villainy"),
    n("Protocol Failure"),
    n("Knowledge And Defense", True),
    n("Operational As Planned", True),
    n("Abyssin Ornament"),
    n("Cease Fire!"),
    n("Sonic Bombardment", True, qty=3),
    n("Outflank", True, qty=2),
    n("Sith Fury & End This Destructive Conflict"),
    n("Kashyyyk: Forest Maze"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Skyhook Platform"),
    n("Kashyyyk"),
    n("Jabba's Space Cruiser"),
    n("Slave I, Symbol Of Fear"),
    n("Mist Hunter", True),
    n("Wookiee Subjugation"),
    n("Armored Attack Tank", qty=3),
    n("AAT Assault Leader"),
    n("Jabba's Sail Barge"),
]
DS_SHIELDS = []
DS_ADD = []
