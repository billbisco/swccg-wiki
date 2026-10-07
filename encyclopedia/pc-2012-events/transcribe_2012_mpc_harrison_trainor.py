#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Matthew Harrison-Trainor.

Source: 2012mpcday1.pdf pages 7–8 (2010 form, 12 shields).
Name Matthew Harrison-Trainor. Username Blay.
p07 LIGHT checked. Deck Name TRM.
p08 LIGHT/DARK both empty — dest Dark by pairing with p07 Light. Deck Name HDV.
Event MPC 2012. Date 11/02/12.
"""
from __future__ import annotations

PLAYER = "Matthew Harrison-Trainor"
USERNAME = "Blay"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 7
DS_PAGE = 8
LS_SCAN = "2012 Match Play Championship Day 1 Matthew Harrison-Trainor LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Matthew Harrison-Trainor DS.png"
LS_DECK_NAME = "TRM"
DS_DECK_NAME = "HDV"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Matthew Harrison-Trainor. Username Blay. LIGHT checked. "
    "Deck Name TRM. Event MPC 2012 11/02/12. "
    "Y4 Throne Room dested Yavin 4: Massassi Throne Room. "
    "Luke SITF dested Luke Skywalker, Strong In The Force. Luke JK dested Luke Skywalker, Jedi Knight. "
    "Obi w/ Saber dested Obi-Wan With Lightsaber. Qui w/ Saber dested Qui-Gon Jinn With Lightsaber. "
    "Leia RP dested Leia, Rebel Princess. Lando Scoundrel dested Lando Calrissian, Scoundrel. "
    "HCF dested Hoth: Echo Docking Bay. H1 War Room dested Home One: War Room. "
    "Hoth Echo Cmd Center dested Hoth: Echo Command Center (War Room). "
    "Cor JCC dested Coruscant: Jedi Council Chamber. H1 DB dested Home One: Docking Bay. "
    "Speak with the Council dested Speak With The Jedi Council. Wesa dested Wesa Gotta Grand Army. "
    "SATM+BP dested Sorry About The Mess & Blaster Proficiency. "
    "3PO WHPS dested C-3PO (See-Threepio). ATR dested Attack Run. "
    "Houjix Combo dested Houjix & Out Of Nowhere. Strike Force dested Strikeforce. "
    "HMBHT dested Hear Me Baby, Hold Together. HFTMF dested Heading For The Medical Frigate. "
    "Unique overcounts sheet-accurate (Luke Skywalker, Strong In The Force x2, Mace Windu x2, "
    "Obi-Wan With Lightsaber x2, Qui-Gon Jinn With Lightsaber x2, Lando Calrissian, Scoundrel x2, "
    "Rebel Leadership x2, Wesa Gotta Grand Army x2, Let The Wookiee Win x2, Blaster Deflection x2, "
    "Under Attack x2, Sorry About The Mess & Blaster Proficiency x2, Attack Run x2). "
    "(V) from checkbox; dittos inherit."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Matthew Harrison-Trainor. Username Blay. "
    "LIGHT/DARK both empty; dest Dark by pairing with p07 Light. Deck Name HDV. "
    "Hunt Down dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Naboo Generator Core dested Naboo: Theed Palace Generator Core. "
    "Tat Cantina dested Tatooine: Cantina. DUDLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Vader Betrayer dested Darth Vader, Betrayer Of The Jedi. Galen dested Galen Marek, Starkiller. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi. Mara w/ Saber dested Mara Jade With Lightsaber. "
    "Kir Kanos w/ Force Pike dested Kir Kanos With Force Pike. "
    "Dengar w/ Blaster Carbine dested Dengar With Blaster Carbine. "
    "Vader's Lightsaber (Premiere) dested Vader's Lightsaber. "
    "Galen's Saber Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Dark Jedi Saber dested Dark Jedi Lightsaber. POTF dested Presence Of The Force. "
    "They're Still Coming Through dested They're Still Coming Through!. "
    "Masterful Move Combo dested Masterful Move & Endor Occupation. "
    "Coruscant Detention dested as written. WMAOP dested We Must Accelerate Our Plans. "
    "EPP 4-lom dested 4-LOM With Concussion Rifle. "
    "Weapon Levitation Combo dested Weapon Levitation & The Empire's Back. "
    "Presence Trap dested Program Trap. YCHF dested You Cannot Hide Forever. "
    "Coward dested Come Here You Big Coward. "
    "Unique overcounts sheet-accurate (Darth Vader, Dark Lord Of The Sith x3, "
    "Galen Marek, Starkiller x3, Emperor Palpatine x3, We Must Accelerate Our Plans x3, "
    "Grievous, Hunter Of Jedi x2, Force Field x2, Trophy Of A Kill x2, Revenge Of The Sith x2). "
    "(V) from checkbox; dittos inherit."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas"),
    n("Heading For The Medical Frigate"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Mace Windu", True, qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Princess Leia"),
    n("Leia, Rebel Princess", True),
    n("Corran Horn"),
    n("Admiral Ackbar"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Home One"),
    n("Artoo-Detoo In Red 5"),
    n("Hoth: Echo Docking Bay"),
    n("Home One: War Room"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Home One: Docking Bay"),
    n("Kiffex"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Leia's Blaster Rifle"),
    n("Speak With The Jedi Council"),
    n("Rebel Leadership", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Blaster Deflection", qty=2),
    n("Under Attack", qty=2),
    n("Hear Me Baby, Hold Together"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Were You Looking For Me?"),
    n("C-3PO (See-Threepio)"),
    n("Attack Run", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("Desperate Reach", True),
    n("Seeking An Audience", True),
    n("Scrambled Transmission"),
    n("Imperial Atrocity", True),
    n("Honor Of The Jedi"),
    n("Strikeforce", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again"),
    n("Only Jedi Carry That Weapon"),
    n("The Professor", True),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Blockade Flagship: Bridge"),
    n("Death Star: War Room"),
    n("Naboo: Theed Palace Generator Core"),
    n("Tatooine: Cantina"),
    n("Gift Of The Master", True),
    n("Blaster Rack", True),
    n("Ni Chuba Na??", True),
    n("I've Lost Artoo!", True),
    n("First Strike"),
    n("Prepared Defenses", True),
    n("A Sith's Weapon", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Galen Marek, Starkiller", qty=3),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Emperor Palpatine", qty=3),
    n("Mara Jade With Lightsaber", True),
    n("Kir Kanos With Force Pike", True),
    n("Dengar With Blaster Carbine"),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Dark Jedi Lightsaber", True),
    n("Force Field", True, qty=2),
    n("Force Lightning"),
    n("Presence Of The Force"),
    n("They're Still Coming Through!"),
    n("Masterful Move & Endor Occupation"),
    n("Coruscant Detention", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("4-LOM With Concussion Rifle", True),
    n("Weapon Levitation & The Empire's Back"),
    n("Force Push", True),
    n("Trophy Of A Kill", qty=2),
    n("Restraining Bolt"),
    n("Imperial Propaganda", True),
    n("Imperial Justice", True),
    n("No Escape"),
    n("A Sith's Plans", True),
    n("Program Trap", True),
    n("Revenge Of The Sith", True, qty=2),
    n("The Emperor's Prize", True),
    n("Emperor's Power", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Oppressive Enforcement", True),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("Firepower"),
]
DS_ADD = []
