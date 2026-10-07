#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Matt Jourdan.

Source: 2012mpcday1.pdf pages 97–98.
Name Matt Jourdan dested Matt Jourdan (analog empty; pack player-stubs).
p97 Light notebook. p98 Dark 2010 Xerox. Username Fishfteas on Light; Dark Username scribbled.
"""
from __future__ import annotations

PLAYER = "Matt Jourdan"
USERNAME = "Fishfteas"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 97
DS_PAGE = 98
LS_SCAN = "2012 Match Play Championship Day 1 Matt Jourdan LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Matt Jourdan DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = "Worlds Day 2"
NOTE = "p97 handwritten notebook Light. p98 handwritten 2010 Xerox Dark."
LS_NOTE = (
    "Handwritten notebook. Name Matt Jourdan dested Matt Jourdan. "
    "Analog empty. Username Fishfteas. Date 2-11-12. "
    "Line 1 Yavin IV v dested Yavin 4 True. "
    "Line 5 Yavin 4: BR dested Yavin 4: Briefing Room. "
    "Line 6 AFA crossed dested Yavin 4: Massassi Throne Room replacement. "
    "Threepio With HPS dested Threepio With His Parts Showing. "
    "Projection of Sky dested Projection Of A Skywalker. "
    "Wedge, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Lando, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Han, Chewie, Falcon dested Han, Chewie, And The Falcon. "
    "SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Leia (v) dested Leia True. "
    "Alderaan Counselor Ship dested Alderaan Consular Ship. "
    "Gold leader in G1 dested Gold Leader In Gold 1 True. "
    "Padme V dested Padme Naberrie True. "
    "Eject Eject / Imp Atr V dested Eject! Eject! Eject! & Imperial Atrocity True. "
    "Were you looking at me? dested Were You Looking For Me?. "
    "IL-10 dested as written. "
    "Unique 60. Shields 11 (11 blank)."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Matt Jourdan dested Matt Jourdan. "
    "Analog empty. Username scribbled; dest Fishfteas from Light. "
    "DARK checked. Deck Name Worlds Day 2. Event Name MPC-12. Date 2-11-12. "
    "Line 1 A Stunning Move/A Valuable Hostage empty dested dual without True. "
    "Coruscant: Private Platform (Docking Bay) dested Coruscant: Private Platform. "
    "Ni Chuba Na?? dested Ni Chuba Na?? True. "
    "Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi. "
    "IG Bodyguard Droid dested IG-100 MagnaGuard. "
    "Dr Evazan + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Galen, Secret Apprentice dested as written. "
    "Galen's Lightsaber, Vader's Gift dested as written. "
    "Snay Motion dested Stop Motion True. "
    "Masterful Move & Endor Occupation dested Masterful Move & Endor Occupation. "
    "Knowledge And Defense True dested Knowledge And Defense (V). "
    "Shield 11 crossed skipped. Unique 60. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4"
LS_CARDS = [
    n("Yavin 4", True),
    n("Massassi Base Sentry"),
    n("Restore Freedom To The Galaxy"),
    n("Yavin 4: Massassi War Room"),
    n("Yavin 4: Briefing Room"),
    n("Yavin 4: Massassi Throne Room"),
    n("Yavin 4: Massassi Headquarters"),
    n("Threepio With His Parts Showing"),
    n("Careful Planning", True),
    n("Luke, Trust Me"),
    n("Wokling", True),
    n("Rogue Squadron Tactics"),
    n("Projection Of A Skywalker"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Lando Calrissian, Scoundrel"),
    n("Tantive IV", True, qty=2),
    n("Han, Chewie, And The Falcon"),
    n("Dressel"),
    n("A Jedi's Resilience", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Flash Of Insight", True),
    n("Life Debt"),
    n("Corran Horn"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Jedi Survivor"),
    n("Grimtaash"),
    n("Leia", True),
    n("Alderaan Consular Ship"),
    n("Gold Leader In Gold 1", True),
    n("Imperial Atrocity", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Naboo: Theed Palace Generator"),
    n("Clash Of Sabers"),
    n("Escape Pod", True, qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Inconsequential Barriers"),
    n("Vengeance In The Force"),
    n("Draw Their Fire"),
    n("Padme Naberrie", True),
    n("Eject! Eject! Eject! & Imperial Atrocity", True),
    n("Were You Looking For Me?"),
    n("Let The Wookiee Win", True, qty=2),
    n("Sense"),
    n("Civil Disorder", True),
    n("IL-10"),
    n("Bright Hope", True),
    n("Seeking An Audience", True),
    n("Sabotage", True),
    n("Houjix"),
    n("Evacuation Control", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("The Professor"),
    n("Don't Do That Again"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Do, Or Do Not"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform"),
    n("Insidious Prisoner"),
    n("Prepared Defenses"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Jabba's Haven"),
    n("Blockade Flagship: Hallway"),
    n("Nal Hutta"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Battle Droid Squad", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Garindan", True),
    n("IG-100 MagnaGuard"),
    n("Dr. Evazan & Ponda Baba"),
    n("4-LOM With Concussion Rifle", True),
    n("Bossk In Hound's Tooth", True),
    n("Jabba's Space Cruiser", True),
    n("Victory"),
    n("Boba Fett In Slave I", True),
    n("Zuckuss In Mist Hunter"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Dark Jedi Lightsaber", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Control", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Force Field", True, qty=2),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Sniper & Dark Strike", qty=2),
    n("Weapon Levitation"),
    n("Force Push", True),
    n("We Must Accelerate Our Plans"),
    n("Oh, Switch Off"),
    n("Maul Strikes"),
    n("Ghhhk"),
    n("The Phantom Menace"),
    n("Imperial Arrest Order"),
    n("Blaster Rack", True),
    n("No Escape"),
    n("Lateral Damage"),
    n("Ability, Ability, Ability", True),
    n("A Sith's Weapon"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption", True),
    n("A Useless Gesture", True),
    n("Battle Order", True),
    n("Secret Plans", True),
    n("Weapon Of A Sith"),
    n("Fanfare", True),
    n("Come Here You Big Coward", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Resistance", True),
]
DS_ADD = []
