#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Casey Anis.

Source: 2012mpcday1.pdf pages 37–38.
p37 typed GEMP dump Light (handwritten Casey Anis). p38 2010 Xerox Dark (Name Casey).
Username blank. Dest Casey Anis. Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Casey Anis"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 37
DS_PAGE = 38
LS_SCAN = "2012 Match Play Championship Day 1 Casey Anis LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Casey Anis DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "p37 typed GEMP dump; p38 handwritten 2010 Xerox."
LS_NOTE = (
    "Typed GEMP dump (Page 1 of 1; mail-attachment dated 2/9/2012). "
    "Handwritten Casey Anis dested Casey Anis. Username blank. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Dark Approach (V) dested Dark Approach True (Light vb6). "
    "Jedi Levitation (V) dested Jedi Levitation True. "
    "Scrambled Transmission (V) dested Scrambled Transmission True. "
    "SATM dested Sorry About The Mess & Blaster Proficiency. "
    "Speak with the Council dested Speak With The Jedi Council. "
    "HC + F dested Han, Chewie, And The Falcon. "
    "Luke Skywalker, Strong In The Force dested Luke Skywalker, Strong In The Force. "
    "NOOOOOOOOOOOO! (V) dested NOOOOOOOOOOOO! True. "
    "Don't Tread On Me (V) (1 starting) dested Don't Tread On Me True in the 60. "
    "Yavin 4: Massassi Throne Room (1 starting) dested in the 60. "
    "AFA (V) (1 starting) dested Anger, Fear, Aggression True in the 60. "
    "LS_START Anger, Fear, Aggression matching 2013 Worlds Anis analog. "
    "12 shields after Verrack all marked (1 starting). Unique 60."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Casey dested Casey Anis. Username blank. "
    "Event Name blank. DARK checked. Do not dest as a new person. "
    "Do not rewrite 2013 leftovers. "
    "Hunt Down True dested Hunt Down And Destroy The Jedi True. "
    "Imperial City dested Coruscant: Imperial City. "
    "Prep Defenses dested Prepared Defenses True. "
    "Gift of a Master dested Gift Of The Master. "
    "Ni Chuba dested Ni Chuba Na?? True. "
    "Vader DLOTS dested Darth Vader, Dark Lord Of The Sith x2. "
    "Galen's Fighter dested Rogue Shadow. "
    "Accelerate crossed, WMAOP dest replacement + ditto empty dested "
    "We Must Accelerate Our Plans x2. "
    "Thrawn dested Grand Admiral Thrawn. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi x2 "
    "(2012 same-event analog; do not copy 2013 Anis Vader dest). "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "AAA dested Ability, Ability, Ability True. "
    "Nevar dested General Nevar. "
    "Sniper + Dark Strike dested Sniper & Dark Strike. "
    "Bridge dested Blockade Flagship: Bridge. "
    "MM + Endor Occupation dested Masterful Move & Endor Occupation. "
    "Death Star: WR dested Death Star: War Room True. "
    "Hoth: 3rd Marker dested Hoth: Defensive Perimeter (3rd Marker). "
    "Coruscant Detention dested as written True. "
    "Emperor Palpatine form 10 + form 37 dested Emperor Palpatine x2. "
    "EPP Dengar dested Dengar With Blaster Carbine True. "
    "A Sith Fury dested Sith Fury True. "
    "One Beautiful Thing dested as written. "
    "EPP 4-LOM dested 4-LOM With Concussion Rifle True. "
    "Restoring Bolt dested Restraining Bolt. "
    "Galen dested Galen Marek, Starkiller x2. "
    "Galen's Saber, VG dested Galen's Lightsaber, Vader's Gift. "
    "Dark Time dested A Dark Time For The Rebellion True. "
    "Light Saber Def dested Lightsaber Deficiency True. "
    "YPA Wom True / ditto empty dested Your Powers Are Weak, Old Man True + empty "
    "(differing checkboxes stay separate). "
    "Cyborg Lightsabers dested Grievous' Lightsabers. "
    "K+D dested Knowledge And Defense empty. "
    "BO dested Battle Order. Coward dested Come Here You Big Coward. "
    "Plans dested Secret Plans. Fire Power dested Firepower True. "
    "YCHF dested You Cannot Hide Forever True. Unique 60."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Dark Approach", True),
    n("Jedi Levitation", True),
    n("Scrambled Transmission", True),
    n("Lucky Shot", True),
    n("Captain Verrack", True),
    n("Demotion"),
    n("Jedi Lightsaber", True),
    n("Qui-Gon's Lightsaber"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Luke's Lightsaber"),
    n("Artoo-Detoo In Red 5"),
    n("Han, Chewie, And The Falcon"),
    n("Tantive IV", True),
    n("Home One"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu", True, qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Threepio With His Parts Showing"),
    n("Under Attack", qty=2),
    n("Blaster Deflection", qty=2),
    n("Imperial Atrocity", True),
    n("NOOOOOOOOOOOO!", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Clash Of Sabers"),
    n("A Jedi's Resilience", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Wesa Gotta Grand Army", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Speak With The Jedi Council"),
    n("Were You Looking For Me?"),
    n("Sense", qty=2),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Kiffex"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Home One: War Room"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Don't Tread On Me", True),
    n("Yavin 4: Massassi Throne Room"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Victory"),
    n("Emperor Palpatine", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Rogue Shadow"),
    n("Sense", qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Endor"),
    n("Grand Admiral Thrawn"),
    n("Darth Vader's Lightsaber"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Juno Eclipse, Black Leader"),
    n("Force Lightning"),
    n("Ability, Ability, Ability", True),
    n("General Nevar"),
    n("Sniper & Dark Strike"),
    n("Force Field", True, qty=2),
    n("P-59"),
    n("Blockade Flagship: Bridge"),
    n("Blaster Rack", True),
    n("Masterful Move & Endor Occupation"),
    n("Death Star: War Room", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Coruscant Detention", True),
    n("Dengar With Blaster Carbine", True),
    n("Revenge Of The Sith"),
    n("Protocol Failure"),
    n("Sith Fury", True),
    n("One Beautiful Thing"),
    n("4-LOM With Concussion Rifle", True),
    n("Restraining Bolt"),
    n("Ghhhk"),
    n("Galen Marek, Starkiller", qty=2),
    n("Galen's Lightsaber, Vader's Gift"),
    n("A Dark Time For The Rebellion", True),
    n("Cold Feet", True),
    n("Why Didn't You Tell Me?", True),
    n("Lightsaber Deficiency", True),
    n("Tarkin's Bounty", True),
    n("Your Powers Are Weak, Old Man", True),
    n("Your Powers Are Weak, Old Man"),
    n("No Escape"),
    n("I Have You Now"),
    n("Trophy Of A Kill"),
    n("Grievous' Lightsabers"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Oppressive Enforcement"),
    n("Weapon Of A Sith"),
    n("Fanfare", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Leave Them To Me", True),
]
DS_ADD = []
