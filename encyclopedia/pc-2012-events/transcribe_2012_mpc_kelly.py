#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Chris Kelly.

Source: 2012mpcday1.pdf pages 99–100.
p99 typed GEMP dump Light TIGIH. p100 typed GEMP dump Dark ASM.
Handwritten Chris Kelly / Chris Kelly - OS. Username blank.
Dest Chris Kelly (existing stub). Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Chris Kelly"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 99
DS_PAGE = 100
LS_SCAN = "2012 Match Play Championship Day 1 Chris Kelly LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Chris Kelly DS.png"
LS_DECK_NAME = "TIGIH"
DS_DECK_NAME = "ASM"
NOTE = "p99 typed GEMP dump TIGIH; p100 typed GEMP dump ASM. Username blank."
LS_NOTE = (
    "Typed GEMP dump. Handwritten Chris Kelly dested Chris Kelly. "
    "Username blank. Deck Name TIGIH. Do not dest as a new person. "
    "There Is Good In Him/I Can Save Him empty dested dual without True. "
    "Don't Tread On Me (V) (1 starting) dested Don't Tread On Me True in the 60. "
    "AFA (V) (1 starting) dested Anger, Fear, Aggression True in the 60. "
    "Endor: Landing Platform (Docking Bay) dested Endor: Landing Platform (Docking Bay). "
    "Qui-Gon Jinn With Lightsaber handwritten 3 over typed x2 dested x3. "
    "Mace Windu (V) dested Mace Windu True. "
    "Mace Windu, (V)(AI) crossed Master of The Order dested "
    "Mace Windu, Master Of The Order. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Boon-Burs True and Tano crossed dested Lucky Shot True x2. "
    "Houjix Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Fallen Portal crossed skipped. Nabrun Leids crossed skipped. "
    "Evacuation Control True crossed dested Desperate Reach True x2. "
    "Wedge In Red Squadron 1 dested without True. "
    "Affect Mind True crossed dested Ultimatum. "
    "Yavin Sentry True margin extra next to Aim High. "
    "He Can Go About His Business True crossed dested Simple Tricks And Nonsense. "
    "Let's Keep A Little Optimism Here True crossed skipped. "
    "Wise Advice crossed dested Only Jedi Carry That Weapon. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed GEMP dump. Handwritten Chris Kelly - OS dested Chris Kelly. "
    "- OS is a tag not a username. Username blank. Deck Name ASM. "
    "Do not dest as a new person. "
    "A Stunning Move/A Valuable Hostage empty dested dual without True. "
    "Coruscant: Private Platform (Docking Bay) dested "
    "Coruscant: Private Platform (Docking Bay). "
    "Darth Maul, Young Apprentice x2 plus (AI) dested x2 "
    "(AI is image variant of unique). "
    "Cyborg Commander, Hunter Of Jedi dested Grievous, Hunter Of Jedi. "
    "Galen, Secret Apprentice dested as written. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers. "
    "Maul's Sith Infiltrator crossed dested First Strike. "
    "Maul Strikes crossed dested Where Are You Taking This ... Thing?. "
    "Much Anger In Him crossed dested Ability, Ability, Ability True. "
    "The Phantom Menace x2 plus (AI) dested x3 (unrestricted extra). "
    "4-LOM With Concussion Rifle empty dested empty. "
    "Reegesk True handwritten dested Reegesk True. "
    "Oppressive Enforcement crossed dested That's No Moon. "
    "Leave Them To Me True crossed dested Fanfare True. "
    "Do They Have A Code Clearance? crossed dested Firepower True. "
    "Unique 59 (Maul AI variant). Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=3),
    n("Mace Windu", True),
    n("Mace Windu, Master Of The Order"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Maris Brood, Fallen Jedi"),
    n("Corran Horn"),
    n("Lucky Shot", True, qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Threepio With His Parts Showing"),
    n("Jedi Lightsaber", True),
    n("Houjix & Out Of Nowhere"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Clash Of Sabers"),
    n("Smoke Screen", qty=2),
    n("Our Only Hope", True),
    n("Blaster Deflection"),
    n("Speak With The Jedi Council", qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("Were You Looking For Me?"),
    n("Hear Me Baby, Hold Together", True),
    n("The Signal", True),
    n("A Jedi's Patience", True),
    n("A Jedi's Resilience", qty=3),
    n("Desperate Reach", True, qty=2),
    n("Lightsaber Proficiency"),
    n("Honor Of The Jedi"),
    n("Projection Of A Skywalker"),
    n("Imperial Atrocity", True, qty=2),
    n("I'm With You Too", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Han, Chewie, And The Falcon", True, qty=2),
    n("Wedge In Red Squadron 1"),
    n("Let The Wookiee Win", True),
    n("Scrambled Transmission", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Aim High"),
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Only Jedi Carry That Weapon"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Knowledge And Defense", True),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Dengar With Blaster Carbine", True),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("P-59"),
    n("Battle Droid Squad", qty=2),
    n("4-LOM With Concussion Rifle"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Trophy Of A Kill"),
    n("Restraining Bolt"),
    n("First Strike"),
    n("Boba Fett In Slave I", True),
    n("Zuckuss In Mist Hunter"),
    n("Bossk In Hound's Tooth", True),
    n("Victory"),
    n("Control & Set For Stun"),
    n("Sniper & Dark Strike"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Sith Fury", True, qty=2),
    n("Force Field", True, qty=2),
    n("Where Are You Taking This ... Thing?"),
    n("Cold Feet", True),
    n("Limited Resources"),
    n("Force Push", True),
    n("Masterful Move & Endor Occupation"),
    n("Your Powers Are Weak, Old Man", True),
    n("Imperial Justice", True),
    n("No Escape"),
    n("Ability, Ability, Ability", True),
    n("Blaster Rack", True),
    n("Imperial Propaganda", True),
    n("The Phantom Menace", qty=3),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Nal Hutta"),
    n("Reegesk", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Abyss", True),
    n("That's No Moon"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Weapon Of A Sith"),
    n("Firepower", True),
    n("A Useless Gesture", True),
]
DS_ADD = []
