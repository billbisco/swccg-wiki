#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Michael Thomas.

Source: 2012mpcday1.pdf pages 135–136 (2010 form, 12 shields).
Name Michael Thomas dested Michael Thomas (2013 leftover analog).
Username blank (do not copy 2013 Username mmThomas2).
p135 Light Yavin 4: Massassi Throne Room. p136 Dark A Stunning Move.
Pack player-stubs/Michael_Thomas.wiki.
Do not dest as Thomas Graham. Do not dest as a new person.
Do not rewrite 2013 leftover Local Uprising / Invasion.
"""
from __future__ import annotations

PLAYER = "Michael Thomas"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 135
DS_PAGE = 136
LS_SCAN = "2012 Match Play Championship Day 1 Michael Thomas LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Michael Thomas DS.png"
LS_DECK_NAME = "George Lucas is an Art Criminal"
DS_DECK_NAME = "Fuck TPM 3D"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Michael Thomas dested Michael Thomas. "
    "Username blank. LIGHT checked. Deck Name George Lucas is an Art Criminal. Event Name MPC. "
    "Do not dest as Thomas Graham. Do not copy 2013 Username mmThomas2. "
    "Do not rewrite 2013 leftover Local Uprising. "
    "Yavin 4: Massassi Throne Room dested Yavin 4: Massassi Throne Room. "
    "Rycar Ryjerd True dested Rycar Ryjerd True. Quick Draw True dested analog Kinsey. "
    "Naboo Boss Nass' Chambers dested Naboo: Boss Nass' Chambers analog leftover. "
    "TWHPS dested Threepio With His Parts Showing analog Bollentino. "
    "Blaster Deflection dested analog Kinsey. Smoke Screen x4. "
    "Luke Skywalker, Jedi Knight dested analog leftover. "
    "Let The Wookiee Win True dested analog leftover. "
    "Luke's Bionic Hand True dested analog leftover. "
    "Lines 28-29 crossed Speak With The Jedi Council dest replacement analog leftover. "
    "Jedi Council Chamber dested Coruscant: Jedi Council Chamber analog Booker. "
    "Mace Windu True dested Mace Windu True as written. "
    "Lightsaber Proficiency dested as written. "
    "Hoth Echo Command Center dested Hoth: Echo Command Center (War Room) analog leftover. "
    "Han Chewie and the Falcon dested Han, Chewie, And The Falcon analog leftover. "
    "Leia Rebel Princess dested Leia, Rebel Princess analog leftover. "
    "Luke Skywalker, Strong in the Force dested Luke Skywalker, Strong In The Force analog Kinsey. "
    "Line 60 Anger, Fear, Aggression crossed skipped. Unique 59. Shields 12. "
    "Additional I Play The Fuck Hate Card. Lucas joke skipped. "
    "Traffic Control True dested in shields. Ounee Ta dested analog leftover."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Michael Thomas dested Michael Thomas. "
    "Username blank. DARK checked. Deck Name Fuck TPM 3D. Event Name MPC. "
    "Do not dest as Thomas Graham. Do not copy 2013 Username mmThomas2. "
    "Do not rewrite 2013 leftover Invasion. "
    "A Stunning Move / A Valuable Hostage True dested dual True virtual-only. "
    "Coruscant Private Platform True dested Coruscant: Private Platform True analog leftover. "
    "Coruscant Palpatine's Quarters True dested analog leftover. "
    "Ni Chuba Na True dested Ni Chuba Na?? True analog leftover. "
    "Gift of the Master True dested Gift Of The Master True analog leftover. "
    "Prepared Defenses empty dested in the 60 analog Pistone. "
    "Battle Droid Squad True x3 sheet-accurate. "
    "Sniper Dark Strike dested Sniper & Dark Strike analog leftover. "
    "Stop Motion True dested analog Jourdan. "
    "Cyborg Commander, Hunter of Jedi True dested Grievous, Hunter Of Jedi True analog Casey. "
    "Cyborg Commander's Lightsaber True dested Grievous' Lightsabers True analog Anis. "
    "Darth Maul, YA dested Darth Maul, Young Apprentice analog leftover. "
    "Dr. Evazan + Ponda Baba dested Dr. Evazan & Ponda Baba analog leftover. "
    "Galen Secret Apprentice True dested as written analog leftover. "
    "4-LOM w/ Concussion Rifle True dested 4-LOM With Concussion Rifle True analog leftover. "
    "Oh Switch Off dested Oh, Switch Off analog leftover. "
    "Boba Fett in Slave 1 True dested Boba Fett In Slave I True analog leftover. "
    "IG Body Guard dested IG-100 MagnaGuard analog Jourdan. "
    "Guriadan dested as written. "
    "Where Are You Taking This Thing True dested Where Are You Taking This ... Thing? analog leftover. "
    "Galen's Lightsaber, Vader's Gift True dested analog leftover. "
    "K&D True dested in the 60 analog Murray. Unique 60. Shields 12. "
    "Shield 2 Reactor Terminal crossed Firepower dest replacement empty analog leftover."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Rycar Ryjerd", True),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Imperial Atrocity", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("Threepio With His Parts Showing"),
    n("Obi-Wan With Lightsaber"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Blaster Deflection", qty=2),
    n("Smoke Screen", qty=4),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Luke's Bionic Hand", True),
    n("Speak With The Jedi Council", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Home One"),
    n("Mace Windu", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Lightsaber Proficiency"),
    n("Sense", qty=2),
    n("Tantive IV", True),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan's Journal"),
    n("Luke's Lightsaber"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Naboo: Battle Plains"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Clash Of Sabers", qty=2),
    n("Nabrun Leids"),
    n("Corran Horn"),
    n("Kiffex"),
    n("Leia, Rebel Princess"),
    n("Gold Leader In Gold 1", True),
    n("Padme Naberrie", True),
    n("Admiral Ackbar", True),
    n("Jedi Lightsaber"),
    n("Luke Skywalker, Strong In The Force"),
    n("Home One: War Room"),
]
LS_SHIELDS = [
    n("Traffic Control", True),
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Another Pathetic Lifeform", True),
    n("Your Insight Serves You Well"),
    n("Ultimatum"),
    n("Don't Do That Again"),
    n("Planetary Defenses"),
    n("Ounee Ta"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage", True),
    n("Coruscant: Private Platform", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Insidious Prisoner", True),
    n("Jabba's Haven", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master", True),
    n("Prepared Defenses"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Victory", True),
    n("Battle Droid Squad", True, qty=3),
    n("Ghhhk"),
    n("Sniper & Dark Strike", qty=2),
    n("Stop Motion", True),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Grievous' Lightsabers", True),
    n("Force Field", True, qty=2),
    n("Blockade Flagship: Docking Bay"),
    n("Something Special Planned For Them"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Ability, Ability, Ability", True),
    n("Control", qty=2),
    n("Force Push", True),
    n("Blaster Rack", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Blockade Flagship: Hallway"),
    n("Lateral Damage"),
    n("Weapon Levitation"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Galen, Secret Apprentice", True, qty=3),
    n("The Phantom Menace"),
    n("4-LOM With Concussion Rifle", True),
    n("Oh, Switch Off"),
    n("Nal Hutta"),
    n("Zuckuss In Mist Hunter"),
    n("Boba Fett In Slave I", True),
    n("Cold Feet", True),
    n("A Sith's Weapon", True),
    n("Blockade Flagship: Bridge"),
    n("IG-100 MagnaGuard"),
    n("No Escape"),
    n("Bossk In Hound's Tooth", True),
    n("Guriadan"),
    n("Maul Strikes"),
    n("Where Are You Taking This ... Thing?", True),
    n("Jabba's Space Cruiser", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Firepower"),
    n("Fanfare"),
    n("Weapon Of A Sith"),
    n("A Useless Gesture"),
    n("There Is No Try"),
    n("Do They Have A Code Clearance?"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
