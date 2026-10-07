#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Matt Thornton.

Source: 2012mpcday1.pdf pages 131–132 (2010 form, 12 shields).
p131 Name MT Username BD Light TRM facing p132 Name Matt Thornton
Username Ben Derlin Dark DS Senate dest [[Matt Thornton]].
USERNAME=Ben Derlin (p132 full; p131 BD is the same handle abbreviated).
p131 LIGHT/DARK empty dest Light from the 60s (Throne Room TRM).
p132 DARK checked dest Dark from the box AND the 60s (My Lord, Is That Legal?).
Pack player-stubs/Matt_Thornton.wiki.
Do not dest as a new person. Do not dest as Matthew Harrison-Trainor.
Do not rewrite 2013 SoCal leftover Watch Your Step (V) / My Lord, Is That Legal.
"""
from __future__ import annotations

PLAYER = "Matt Thornton"
USERNAME = "Ben Derlin"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 131
DS_PAGE = 132
LS_SCAN = "2012 Match Play Championship Day 1 Matt Thornton LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Matt Thornton DS.png"
LS_DECK_NAME = "TRM"
DS_DECK_NAME = "DS Senate"
NOTE = "Handwritten 2010 Xerox form. Username Ben Derlin."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name MT dested Matt Thornton facing p132. "
    "Username BD dested Ben Derlin from p132 Username box. LIGHT/DARK empty dest Light from the 60s. "
    "Deck Name TRM. Event Name MPC. "
    "TRoom dested Yavin 4: Massassi Throne Room analog Graham. "
    "Folate dested Restore Freedom To The Galaxy analog TRM sandwich. "
    "QD True dested Quiet Digging True. TWHPS dested Threepio With His Parts Showing analog Bollentino. "
    "SCC True dested Coruscant: Jedi Council Chamber True analog Booker. "
    "Rel. Leadership True dested Rebel Leadership True analog Graham. "
    "Don't Fear Fire dested Don't Tread On Me analog Casey. "
    "Insurrection + Adm Hats dested Insurrection & Aim High. "
    "Late SITE dested Yavin 4: Massassi Ruins analog leftover. "
    "Ell Qui dested Qui-Gon Jinn With Lightsaber analog Graham. "
    "Speak dested Speak With The Jedi Council analog Graham. "
    "Maneuver Wind, Master order dested Mace Windu, Master Of The Order analog Kinsey. "
    "IL-10 dested I'll Take The Odds analog Graham. "
    "Houjix Combo dested Houjix analog 2013 Thornton slang. "
    "WHAP True dested We Have A Plan True. Leia True dested Princess Leia True analog Smith. "
    "HFTMF True dested in the 60 analog Casey. Hear me baby True dested in the 60 analog Richards. "
    "AFA True dested in the 60 analog Casey. Line 11 crossed skipped. Unique 59. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Matt Thornton dested Matt Thornton. Username Ben Derlin. "
    "DARK checked. Deck Name DS Senate. Event Name MPC. "
    "My Lord, Is That Legal? dested dual I Will Make It Legal empty analog Mack. "
    "Senate dested Coruscant: Galactic Senate. T. Tickets dested Tikkes analog Graham. "
    "Lousy Argue dested Passel Argente. MMPEO dested Masterful Move & Endor Occupation analog Marlow. "
    "Super 1 dested Saber 1 analog Graham. Baron dested Baron Soontir Fel analog Graham. "
    "Blasts dested Blaster Rack. Blast 2 dested Black 2 analog Graham. "
    "Zimp dested Zuckuss In Mist Hunter analog Anderson. Clouds dested TIE Fighters. "
    "SFS Cannons For Baron dested SFS L-s9.3 Laser Cannons analog Graham. "
    "OS-72-1 In O1 dested OS-72-1 In Obsidian 1 analog Smith. "
    "Prepared Defenses crossed skipped. OS-72-1 In O2 crossed skipped. "
    "K&D True dested in the 60 analog Murray. Unique 58. Shields 10."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Restore Freedom To The Galaxy"),
    n("Quiet Digging", True),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Imperial Atrocity", True),
    n("Gungan Lightsaber"),
    n("Don't Tread On Me"),
    n("Heading For The Medical Frigate", True),
    n("Sai'torr Kal Fas", True),
    n("Kiffex"),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Threepio With His Parts Showing"),
    n("Home One: War Room"),
    n("Home One: Docking Bay"),
    n("A Few Maneuvers", True),
    n("Wesa Gotta Grand Army"),
    n("Obi-Wan's Lightsaber"),
    n("Rebel Leadership", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Sense", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Torture", True),
    n("Strikeforce", True),
    n("Yavin 4: Massassi Ruins", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("NOOOOOOOOOOOO!", True),
    n("Speak With The Jedi Council"),
    n("Blaster Deflection"),
    n("Mace Windu, Master Of The Order"),
    n("I'll Take The Odds"),
    n("Hear Me Baby, Hold Together", True),
    n("Leia, Rebel Princess"),
    n("Leia's Blaster Rifle"),
    n("Wesa Ready To Do Our-Sa Part"),
    n("Lucky Shot"),
    n("Were You Looking For Me?"),
    n("Rebel Leadership"),
    n("Jedi Lightsaber", True),
    n("Clash Of Sabers"),
    n("Desperate Reach", True),
    n("Home One"),
    n("Crash Course", True),
    n("We Have A Plan", True),
    n("Naboo: Battle Plains"),
    n("Path Of Least Resistance"),
    n("Princess Leia", True),
    n("Houjix"),
    n("Corran Horn"),
    n("Obi-Wan's Lightsaber"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Planetary Defenses", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Wise Advice"),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Naboo"),
    n("Coruscant: Galactic Senate"),
    n("Ni Chuba Na??"),
    n("I'm Sorry", True),
    n("Combat Response", True),
    n("Our Blockade Is Perfectly Legal"),
    n("This Is Outrageous!"),
    n("Motion Supported"),
    n("Accepting Trade Federation Control"),
    n("Coruscant Guard"),
    n("Lott Dod", qty=3),
    n("Baskol Yeesrim", qty=2),
    n("Toonbuck Toora", qty=2),
    n("Aks Moe"),
    n("Yeb Yeb Adem'thorn"),
    n("Tikkes", qty=2),
    n("Orn Free Taa"),
    n("Passel Argente"),
    n("Darth Vader"),
    n("Vader's Personal Shuttle", True),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Limited Resources"),
    n("Carbon Combo", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Control", qty=2),
    n("Squabbling Delegates", qty=3),
    n("All Power To Weapons", qty=2),
    n("Saber 1"),
    n("Baron Soontir Fel"),
    n("Blaster Rack"),
    n("DS-61-3"),
    n("Black 2"),
    n("DS-61-2"),
    n("OS-72-10"),
    n("Orn Free Taa"),
    n("OS-72-1 In Obsidian 1"),
    n("Planetary Defenses", qty=2),
    n("Senate Hovercam"),
    n("Obsidian 10"),
    n("The Fight Is Cancelled"),
    n("Zuckuss In Mist Hunter"),
    n("TIE Fighters"),
    n("Storm Clouds"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Resistance"),
    n("Abyss", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("You've Lost", True),
    n("Allegations Of Corruption"),
    n("Bith", True),
    n("Secret Plans"),
    n("Battle Order"),
]
DS_ADD = []
