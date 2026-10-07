#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Sam Marlow.

Source: 2012mpcday1.pdf pages 111–112 (2010 form, 12 shields).
Name Sam Marlow dested Sam Marlow (generate_2013_mpc CANON;
2013 leftover PLAYER=Sam Marlow USERNAME=Hari Seldon).
p111 Light Coruscant: Night Club. p112 Dark A Stunning Move.
Username Hari Seldon. Pack player-stubs/Sam_Marlow.wiki.
Do not dest as a new person. Do not rewrite 2013 leftovers.
Event Name MPC 2011 is a year typo; Date 2/11/12 dest as 2012 leftover.
"""
from __future__ import annotations

PLAYER = "Sam Marlow"
USERNAME = "Hari Seldon"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 111
DS_PAGE = 112
LS_SCAN = "2012 Match Play Championship Day 1 Sam Marlow LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Sam Marlow DS.png"
LS_DECK_NAME = "2/2"
DS_DECK_NAME = "ASM"
NOTE = "Handwritten 2010 Xerox form. Username Hari Seldon."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Sam Marlow dested Sam Marlow. "
    "Username Hari Seldon. LIGHT checked. Deck Name 2/2. "
    "Event Date 2/11/12 Event Name MPC 2011 year typo dest as 2012 leftover. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Line 1 Coruscant: Night Club dested starting location. "
    "BP & DTF dested Battle Plan & Draw Their Fire. "
    "DoDN & WA dested Do, Or Do Not & Wise Advice. "
    "Luke, SITF dested Luke Skywalker, Strong In The Force x4. "
    "Yoda, MOTF dested Yoda, Master Of The Force x4. "
    "Speak WTJC dested Speak With The Jedi Council x5. "
    "Sorry about the mess combo dested Sorry About The Mess & Blaster Proficiency x2. "
    "Threepio WHPS dested Threepio With His Parts Showing. "
    "Wesa GGA dested Wesa Gotta Grand Army x3. "
    "Control / TV dested Control & Tunnel Vision. "
    "Han, Chewie, Falcon dested Han, Chewie, And The Falcon True. "
    "Are You brain Dead dested Are You Brain Dead? x2. "
    "AFA dested Anger, Fear, Aggression True. "
    "Simple Tricks dested Simple Tricks And Nonsense. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Sam Marlow dested Sam Marlow. "
    "Username Hari Seldon. DARK checked. Deck Name ASM. "
    "Event Date 2/11/12 Event Name MPC. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "ASM dested dual A Stunning Move / A Valuable Hostage empty. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi x2. "
    "Galen, SA dested Galen, Secret Apprentice x3. "
    "DM, YA dested Darth Maul, Young Apprentice x3. "
    "MM & EO dested Masterful Move & Endor Occupation analog PMT. "
    "A Dark Time FTR dested A Dark Time For The Rebellion True x2. "
    "Sniper & DS dested Sniper & Dark Strike x2. "
    "Ability x3 dested Ability, Ability, Ability True. "
    "Propaganda True dested Imperial Propaganda True. "
    "Lat Damage dested Lateral Damage. "
    "TF Flagship: Bridge dested Blockade Flagship: Bridge. "
    "BF: DB dested Blockade Flagship: Docking Bay. "
    "BF in SI dested Boba Fett In Slave I. "
    "Maul's Double Bladed LS dested Maul's Double-Bladed Lightsaber. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Ni Chuba Na dested Ni Chuba Na?? True. "
    "YCHF dested You Cannot Hide Forever True. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Coruscant: Night Club"
LS_CARDS = [
    n("Coruscant: Night Club"),
    n("It Is The Future You See", True),
    n("Quick Draw", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Sai'torr Kal Fas", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Luke Skywalker, Strong In The Force", qty=4),
    n("Luke's Lightsaber"),
    n("Coruscant: Jedi Council Chamber"),
    n("Yoda, Master Of The Force", qty=4),
    n("Jedi Lightsaber", True, qty=2),
    n("Speak With The Jedi Council", qty=5),
    n("Threepio With His Parts Showing"),
    n("Mace Windu", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Were You Looking For Me?", qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("Corran Horn"),
    n("Leia, Rebel Princess", qty=2),
    n("Scrambled Transmission", True),
    n("Blaster Deflection", qty=2),
    n("Imperial Atrocity", True),
    n("Control & Tunnel Vision"),
    n("Hear Me Baby, Hold Together", True),
    n("Master Qui-Gon", True, qty=2),
    n("Leia's Blaster Rifle"),
    n("Han, Chewie, And The Falcon", True),
    n("Qui-Gon's Lightsaber"),
    n("Armed And Dangerous"),
    n("Hindsight", True),
    n("Let The Wookiee Win", True, qty=3),
    n("Sense", qty=2),
    n("Are You Brain Dead?", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("He Can Go About His Business", True),
    n("Only Jedi Carry That Weapon"),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Insidious Prisoner"),
    n("P-59"),
    n("Garindan", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Battle Droid Squad", qty=2),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Ghhhk"),
    n("Maul Strikes"),
    n("Weapon Levitation"),
    n("Force Push", True),
    n("We Must Accelerate Our Plans"),
    n("Masterful Move & Endor Occupation"),
    n("Cold Feet", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Stop Motion", True),
    n("Sith Fury", True),
    n("Elis Helrot"),
    n("Sniper & Dark Strike", qty=2),
    n("Force Field", True, qty=2),
    n("Control", qty=2),
    n("Blaster Rack", True),
    n("No Escape"),
    n("Ability, Ability, Ability", True),
    n("The Phantom Menace", qty=2),
    n("Imperial Propaganda", True),
    n("A Sith's Weapon"),
    n("Lateral Damage"),
    n("Blockade Flagship: Bridge"),
    n("Nal Hutta"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Hallway"),
    n("Boba Fett In Slave I"),
    n("Zuckuss In Mist Hunter"),
    n("Victory"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Dark Jedi Lightsaber"),
    n("Prepared Defenses"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Bossk In Hound's Tooth", True),
    n("4-LOM With Concussion Rifle", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Wipe Them Out, All Of Them", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Abyss", True),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
