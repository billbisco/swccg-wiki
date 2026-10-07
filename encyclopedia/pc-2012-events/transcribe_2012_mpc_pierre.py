#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Pierre Dubreuil.

Source: 2012mpcday1.pdf pages 67–68.
Name Pierre Dubreuil dested Pierre Dubreuil (BRINGHIMB4ME analog).
Do not dest as Philippe Dubreuil. Do not dest as a new person.
p67 Light Restore Freedom To The Galaxy (2010 Xerox). p68 Dark A Stunning Move (2002 DECK LIST).
Pack player-stubs/Pierre_Dubreuil.wiki.
"""
from __future__ import annotations

PLAYER = "Pierre Dubreuil"
USERNAME = "BRINGHIMB4ME"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 67
DS_PAGE = 68
LS_SCAN = "2012 Match Play Championship Day 1 Pierre Dubreuil LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Pierre Dubreuil DS.png"
LS_DECK_NAME = "Restore The Freedom To Y4"
DS_DECK_NAME = "STM"
NOTE = "p67 handwritten 2010 Xerox; p68 handwritten 2002 DECK LIST print form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Pierre Dubreuil dested Pierre Dubreuil. "
    "Username BRINGHIMB4ME. LIGHT/DARK boxes empty; dested Light from the 60. "
    "Deck Name Restore The Freedom To Y4. "
    "Restore Freedom dested Restore Freedom To The Galaxy True. "
    "Luke Skywalker R/S dested Luke Skywalker, Rebel Scout True x2. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "Leia Reb dested Leia, Rebel Princess. "
    "H.C. and F dested Han, Chewie, And The Falcon True. "
    "Alderaan Consular Ship dested Radiant VII True. "
    "Captain Venack dested Captain Verrack True. "
    "Gold Sqdn Y-wings dested Gold Squadron 1 x3. "
    "Wedge in Red Sq 1 dested Wedge In Red Squadron 1 True. "
    "Like Trust Me dested Trust Me True. "
    "Yavin 4 War Room dested Yavin 4: Massassi War Room. "
    "Obi with L/S dested Obi-Wan With Lightsaber. "
    "Qui-Gon Jn w/ L/S dested Qui-Gon Jinn With Lightsaber. "
    "Sergeant Doalyn dested Sergeant Doallyn True. "
    "Unique 60. Shields 11 written. Additional empty. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2002 DECK LIST. Name Pierre Dubreuil (BRINGHIMB4ME) dested Pierre Dubreuil. "
    "Username BRINGHIMB4ME. LIGHT/DARK boxes empty; dested Dark from the 60. "
    "Deck Title STM. Event MPC 2012. "
    "AISM dested A Stunning Move / A Valuable Hostage True. "
    "Prepared Defence dested Prepared Defenses True. "
    "Ni Chuba Na dested Ni Chuba Na?? True. "
    "Nalhutta dested Nal Hutta. "
    "IG Bodyguard Droid dested IG-100 MagnaGuard True. "
    "Galen Secret App dested Galen, Secret Apprentice True x2. "
    "Galen's L/S Vader's Gift dested Galen's Lightsaber, Vader's Gift True. "
    "Cyborg Commander's L/S dested Grievous' Lightsabers True. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi True x2. "
    "Darth Maul Young Apprentice dested Darth Maul, Young Apprentice x2. "
    "Darth Maul's Double Bladed L/S dested Maul's Double-Bladed Lightsaber. "
    "Bossk in Hound's Tooth dested Bossk In Hound's Tooth. "
    "Boba Fett in Slave I dested Boba Fett In Slave I True. "
    "Dengar in Punishing 1 dested Dengar In Punishing One. "
    "Sniper Dark Strike dested Sniper & Dark Strike. "
    "AAA dested Ability, Ability, Ability True. "
    "A Dark Time True x2. (V) written dests True. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Restore Freedom To The Galaxy"
LS_CARDS = [
    n("Quick Draw", True),
    n("The Camp", True),
    n("Sai'torr Kal Fas", True),
    n("Massassi Base Sentry", True),
    n("Haven"),
    n("Luke's Lightsaber"),
    n("Luke Skywalker, Rebel Scout", True, qty=2),
    n("Yavin 4", True),
    n("Yavin 4: Jedi Academy"),
    n("Restore Freedom To The Galaxy", True),
    n("Yavin 4: Massassi War Room"),
    n("Dressel", True),
    n("Rescue", True),
    n("Gold Leader In Gold 1", True),
    n("Wedge In Red Squadron 1", True),
    n("What Are You Trying To Push On Us?", True),
    n("Rebel Barrier", qty=2),
    n("Escape Pod", True),
    n("Flash Of Insight", True, qty=2),
    n("Radiant VII", True),
    n("Home One"),
    n("Captain Verrack", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Houjix"),
    n("Leia, Rebel Princess"),
    n("Melas", True),
    n("Han, Chewie, And The Falcon", True),
    n("A Jedi's Resilience", qty=2),
    n("Gold Squadron 1", qty=3),
    n("Tantive IV", True),
    n("Out Of Commission"),
    n("Menace Fades"),
    n("Liberty"),
    n("Sense", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Launching The Assault"),
    n("Blaster Deflection", qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Bright Hope", True),
    n("Admiral Ackbar", True),
    n("Sergeant Doallyn", True),
    n("The Signal"),
    n("Hear Me Baby, Hold Together", True),
    n("Organized Attack"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Wokling", True),
    n("Spiral"),
    n("Trust Me", True),
    n("Corran Horn"),
    n("Scrambled Transmission", True),
    n("Careful Planning", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Crossing", True),
    n("Wise Advice"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Affect Mind", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("Prepared Defenses", True),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??", True),
    n("Jabba's Haven", True),
    n("A Stunning Move / A Valuable Hostage", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Coruscant: Private Platform", True),
    n("Insidious Prisoner", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Nal Hutta"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("IG-100 MagnaGuard", True),
    n("Garindan", True),
    n("Dr. Evazan & Ponda Baba", True),
    n("P-59", True),
    n("Galen, Secret Apprentice", True, qty=2),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Grievous' Lightsabers", True),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Battle Droid Squad", True, qty=3),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Maul's Double-Bladed Lightsaber"),
    n("Bossk In Hound's Tooth"),
    n("Victory", True),
    n("Zuckuss In Mist Hunter"),
    n("Boba Fett In Slave I", True),
    n("Dengar In Punishing One"),
    n("Jabba's Space Cruiser", True),
    n("The Phantom Menace"),
    n("No Escape"),
    n("Tarkin's Bounty", True),
    n("Sith Fury", True),
    n("Force Field", True, qty=2),
    n("Ability, Ability, Ability", True),
    n("Imperial Propaganda", True),
    n("Blaster Rack", True),
    n("Cold Feet", True),
    n("Stop Motion", True),
    n("Ghhhk"),
    n("Control", qty=2),
    n("Maul Strikes"),
    n("Masterful Move"),
    n("Weapon Levitation"),
    n("Lightsaber Deficiency", True),
    n("4-LOM With Concussion Rifle", True),
    n("Sniper & Dark Strike"),
    n("Limited Resources"),
    n("Imperial Arrest Order"),
    n("Operational As Planned", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Fanfare", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("Weapon Of A Sith", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
