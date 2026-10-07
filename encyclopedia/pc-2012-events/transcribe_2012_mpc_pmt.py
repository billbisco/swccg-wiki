#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: PMT.

Source: 2012mpcday1.pdf pages 93–94 (2010 form).
Name PMT dested PMT (analog empty; pack player-stubs).
p93 Light. p94 Dark. Username box blank.
Do not dest as Johnson (2014 leftover Username PMT). Do not invent a first name.
"""
from __future__ import annotations

PLAYER = "PMT"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 93
DS_PAGE = 94
LS_SCAN = "2012 Match Play Championship Day 1 PMT LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 PMT DS.png"
LS_DECK_NAME = "WHAP"
DS_DECK_NAME = "PMT's ASM"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name PMT dested PMT. Analog empty. "
    "Username box blank. LIGHT checked. Deck Name WHAP. Event Date/Name blank. "
    "Do not dest as Johnson. Do not invent a first name. "
    "Line 1 remnant We Have a Plan dested Careful Planning / We Have A Plan To Combat Them. "
    "Control / Tunnel Vision dested Control & Tunnel Vision x3. "
    "Panaka, Protector of the Queen dested Panaka, Protector Of The Queen x3. "
    "Let the Wookiee Win True then dittos empty kept separate. "
    "Obi-Wan Kenobi Jedi Knight dested Obi-Wan Kenobi, Jedi Knight True then empty. "
    "Sorry About the Mess / Blaster Prof dested Sorry About The Mess & Blaster Proficiency. "
    "Sense / Recoil in Fear dested Sense & Recoil In Fear x2. "
    "Mace Windu True then empty kept separate. "
    "Yoda, MoTF dested Yoda, Master Of The Force. "
    "Qui Gon Jinn w/ Lightsaber dested Qui-Gon Jinn With Lightsaber x2. "
    "Sabe dested Sabe. I Hope She's Alright dested I Hope She's All Right. "
    "Ki Adi Mundi dested Ki-Adi-Mundi True. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi True. "
    "Obi Wan's Lightsaber (I) dested Obi-Wan's Lightsaber. "
    "Jars Jammer dested Jar Jar Binks. "
    "Theed Palace: Courtyard dested Naboo: Theed Palace Courtyard. "
    "Naboo Theed Palace Throne dested Naboo: Theed Palace Throne Room. "
    "Strike Force dested Strikeforce True. "
    "Saitorr Kal Fas dested Sai'torr Kal Fas True. "
    "Unique 60. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name PMT dested PMT. Analog empty. "
    "Username box blank. DARK checked. Deck Name PMT's ASM. Event Date/Name blank. "
    "Do not dest as Johnson. Do not invent a first name. "
    "Line 1 remnant Stunning Move dested A Stunning Move / A Valuable Hostage. "
    "Sith Fury True then empty kept separate. "
    "Imperial Propaganda True then empty kept separate. "
    "Galen Secret Apprentice dested Galen, Secret Apprentice x3. "
    "Darth Maul YA dested Darth Maul, Young Apprentice x3. "
    "Why Didn't You Tell Me dested Why Didn't You Tell Me?. "
    "Masterful Move / Endor Occ dested Masterful Move & Endor Occupation. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi x2. "
    "Something Special dested Something Special Planned For Them True. "
    "I've Lost Artoo dested I've Lost Artoo! True. "
    "Force Field True then empty kept separate. "
    "Weapon Levitation dested Weapon Levitation empty. "
    "Boba Fett, Relentless Bounty Hunter dested Boba Fett, Relentless Bounty Hunter x2. "
    "Sniper / Dark Strike dested Sniper & Dark Strike. "
    "Blockade Support Ship dested Blockade Flagship. "
    "Knowledge And Defense dested Knowledge And Defense True. "
    "Unique 60. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Careful Planning / We Have A Plan To Combat Them"
LS_CARDS = [
    n("Careful Planning / We Have A Plan To Combat Them"),
    n("Control & Tunnel Vision", qty=3),
    n("Panaka, Protector Of The Queen", qty=3),
    n("Flash Of Insight", True),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win", qty=2),
    n("Let's Keep A Little Optimism Here", True),
    n("Honor Of The Jedi"),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Obi-Wan Kenobi, Jedi Knight"),
    n("Smoke Screen", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Heading For The Medical Frigate"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("We Don't Have Time For This"),
    n("Sense & Recoil In Fear", qty=2),
    n("Bravo Fighter", True),
    n("Sio Bibble"),
    n("Mace Windu", True),
    n("Mace Windu"),
    n("Ascension Guns"),
    n("Hear Me Baby, Hold Together", True),
    n("Yoda, Master Of The Force"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Sabe"),
    n("We'll Take The Long Way", qty=2),
    n("Ki-Adi-Mundi", True),
    n("Maris Brood, Fallen Jedi", True),
    n("Queen Amidala", qty=3),
    n("Imperial Atrocity", qty=2),
    n("Obi-Wan's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Jar Jar Binks"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Hallway"),
    n("Naboo: Theed Palace Throne Room"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Strikeforce", True),
    n("Civil Disorder", True),
    n("Sai'torr Kal Fas", True),
    n("I Hope She's All Right"),
    n("Your Insight Serves You Well"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Planetary Defenses", True),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Aim High"),
    n("Only Jedi Carry That Weapon"),
    n("Wise Advice"),
    n("Chasm", True),
    n("Ultimatum"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Cold Feet", True),
    n("Sith Fury", True),
    n("Sith Fury"),
    n("Imperial Propaganda", True),
    n("Imperial Propaganda"),
    n("Galen, Secret Apprentice", qty=3),
    n("The Phantom Menace", qty=2),
    n("Victory", qty=2),
    n("Why Didn't You Tell Me?", True),
    n("Masterful Move & Endor Occupation"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Ket Maliss", qty=2),
    n("A Dark Time For The Rebellion", True),
    n("A Sith's Weapon"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Insidious Prisoner"),
    n("Trophy Of A Kill", qty=2),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Battle Droid Squad", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Dark Jedi Lightsaber", True),
    n("Aurra Sing", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Something Special Planned For Them", True),
    n("Blaster Rack", True),
    n("Gift Of The Master", True),
    n("I've Lost Artoo!", True),
    n("Trained In The Jedi Arts"),
    n("Force Field", True),
    n("Force Field"),
    n("Weapon Levitation"),
    n("Ability, Ability, Ability", True),
    n("Boba Fett, Relentless Bounty Hunter", qty=2),
    n("Maul Strikes"),
    n("Stop Motion", True),
    n("Dr. Evazan & Ponda Baba", qty=2),
    n("Destroying Bolt"),
    n("Boba Fett's Blaster Rifle", True),
    n("Sniper & Dark Strike"),
    n("Prepared Defenses"),
    n("Blockade Flagship"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Weapon Of A Sith"),
    n("Leave Them To Me", True),
    n("There Is No Try"),
    n("Resistance"),
    n("Battle Order"),
    n("A Useless Gesture"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Secret Plans"),
]
DS_ADD = []
