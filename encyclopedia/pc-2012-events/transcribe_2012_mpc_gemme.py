#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Mike Gemme.

Source: 2012mpcday1.pdf pages 73–74 (2010 form, 12 shields).
Name Gemme / Username Mike Gemme dested Mike Gemme (generate_2015_2016 analog).
p73 Light Communing. p74 Dark A Stunning Move.
Do not dest as a new person. Pack player-stubs/Mike_Gemme.wiki.
"""
from __future__ import annotations

PLAYER = "Mike Gemme"
USERNAME = "Mike Gemme"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 73
DS_PAGE = 74
LS_SCAN = "2012 Match Play Championship Day 1 Mike Gemme LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Mike Gemme DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Gemme dested Mike Gemme. Username blank on Light. "
    "LIGHT checked. Deck Name blank. Event Date/Name blank. "
    "Do not dest as a new person. "
    "Communing empty dested Communing. "
    "Commando Train & Klorslug dested Commando Training & K'lor'slug. "
    "Run Luke Run dested Run Luke, Run! True then ditto empty. "
    "Leia EPP dested Leia With Blaster Rifle. "
    "Yoda GW dested Yoda, Great Warrior. "
    "Tat: Obi Wan's hut dested Tatooine: Obi-Wan's Hut True. "
    "OOC/TT dested Out Of Commission & Transmission Terminated. "
    "Bith Shuttle / DL dested The Bith Shuffle & Desperate Reach x2. "
    "Tatooine cpl dested Tatooine: City Outskirts. "
    "Lando w/ Ax dested Lando With Vibro-Ax. "
    "Chewie Enraged dested Chewie, Enraged True then ditto empty. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5 x2. "
    "Dittos with differing checkboxes kept separate. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name DECK; Username Mike Gemme dested Mike Gemme. "
    "DARK checked. Deck Name blank. Event Date/Name blank. "
    "Do not dest as a new person. "
    "A Stunning Move dested A Stunning Move / A Valuable Hostage empty. "
    "Wipe them out dested Wipe Them Out, All Of Them True. "
    "N: Chuba Neh dested Ni Chuba Na?? True. "
    "Gift of The Mesh dested Gift Of The Master True. "
    "3720-1 dested 3,720 To 1 True. "
    "Elis in Hinthra dested Elis In Hinthra. "
    "Blaster Racks dested Blaster Rack True. "
    "Darth Maul YA dested Darth Maul, Young Apprentice x3. "
    "IG Bodyguard Droid dested IG-100 MagnaGuard x3. "
    "Galen SA dested Galen, Secret Apprentice x3. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi x2. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers. "
    "Galen's Lightsaber Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Sniper Dark Strike dested Sniper & Dark Strike. "
    "4 Lom w/ concussion rifle dested 4-LOM With Concussion Rifle True. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Communing"),
    n("Commando Training & K'lor'slug"),
    n("Let's Keep A Little Optimism Here", True),
    n("Houjix"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Run Luke, Run!", True),
    n("Run Luke, Run!"),
    n("Leia With Blaster Rifle"),
    n("Yoda, Great Warrior"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Grimtaash"),
    n("Draw Their Fire"),
    n("Hindsight", True),
    n("Wookiee Roar", True, qty=2),
    n("Master Kenobi"),
    n("Rebel Leadership", True),
    n("Rebel Leadership", qty=2),
    n("Use The Force", True),
    n("Use The Force"),
    n("Hear Me Baby, Hold Together", True),
    n("Rebel Gunrunner"),
    n("Chewbacca Of Kashyyyk", True),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Luke's Blaster Pistol", True),
    n("Jedi Levitation", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Escape Pod", True),
    n("Escape Pod"),
    n("Tatooine: City Outskirts"),
    n("Shmi Skywalker"),
    n("Admiral Ackbar", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Captain Verrack", True),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Chewbacca", True),
    n("Lando With Vibro-Ax"),
    n("Lando Calrissian, Scoundrel", True),
    n("Slight Weapons Malfunction"),
    n("Luke Skywalker, Rebel Hero", True),
    n("Luke Skywalker, Rebel Hero", qty=2),
    n("The Force Is Strong With This One"),
    n("Tatooine: Slave Quarters"),
    n("Threepio With His Parts Showing"),
    n("Tatooine: Cantina"),
    n("Chewie, Enraged", True),
    n("Chewie, Enraged"),
    n("Chewbacca's Bowcaster"),
    n("Strike Planning", True),
    n("Home One: War Room"),
    n("Launching The Assault"),
    n("Wokling", True),
    n("Sabotage", True),
    n("Anger, Fear, Aggression", True),
    n("Home One"),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Affect Mind"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Aim High", True),
    n("Do, Or Do Not"),
    n("Chasm"),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Wipe Them Out, All Of Them", True),
    n("Ni Chuba Na??", True),
    n("Insidious Prisoner"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform"),
    n("Prepared Defenses", True),
    n("Gift Of The Master", True),
    n("3,720 To 1", True),
    n("Elis In Hinthra"),
    n("Blaster Rack", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("P-60"),
    n("Force Push", True),
    n("IG-100 MagnaGuard", qty=3),
    n("Oh, Switch Off", qty=2),
    n("Stop Motion", True),
    n("Force Field", True, qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("No Escape"),
    n("Self-Destruct Mechanism"),
    n("Sniper & Dark Strike"),
    n("Ability, Ability, Ability", True),
    n("Where Are You Taking This ... Thing?"),
    n("Victory"),
    n("The Phantom Menace", qty=2),
    n("Tarkin's Bounty", True),
    n("Battle Droid Squad", qty=3),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul Strikes"),
    n("Grievous' Lightsabers"),
    n("Cold Feet", True),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Operational As Planned", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("P-59"),
    n("Masterful Move"),
    n("Forced Servitude"),
    n("Ghhhk"),
    n("A Sith's Weapon"),
    n("4-LOM With Concussion Rifle", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Weapon Of A Sith"),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Oppressive Enforcement", True),
    n("Secret Plans", True),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare"),
]
DS_ADD = []
