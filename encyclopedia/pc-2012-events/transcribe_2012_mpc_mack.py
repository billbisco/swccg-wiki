#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Josh Mack.

Source: 2012mpcday1.pdf pages 109–110 (2010 form, 12 shields).
Name MACK / Mack dested Josh Mack (generate_2014_mpc CANON Mack→Josh Mack;
2013 leftover PLAYER=Josh Mack USERNAME=Remaker;
2014 leftover PLAYER=Josh Mack).
p109 Light Plead My Case To The Senate. p110 Dark My Lord, Is That Legal?.
Username Remaker. Pack player-stubs/Josh_Mack.wiki.
Do not dest as Sean Mackin. Do not dest as a new person.
Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Josh Mack"
USERNAME = "Remaker"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 109
DS_PAGE = 110
LS_SCAN = "2012 Match Play Championship Day 1 Josh Mack LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Josh Mack DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form. Username Remaker."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name MACK dested Josh Mack. Username Remaker. "
    "LIGHT checked. Do not dest as Sean Mackin. Do not rewrite 2013 leftovers. "
    "Plead My Case To dested dual Senate In Chaos empty. "
    "DTF dested Draw Their Fire. HCF dested Han, Chewie, And The Falcon. "
    "Queen Amidala, RON dested Queen Amidala, Ruler Of Naboo. "
    "Senator Palps dested Senator Palpatine. Yarna dested Yarua. "
    "LSJK dested Luke Skywalker, Jedi Knight. Atrocity dested Imperial Atrocity. "
    "Dith shuffle dested The Bith Shuffle & Desperate Reach. "
    "Moes combo dested as written. AFA dested Anger, Fear, Aggression True. "
    "Optimism dested Let's Keep A Little Optimism Here True in shields. "
    "Planetary Defense dested Planetary Defenses True. "
    "Shield 12 cropped. Unique 60. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Mack dested Josh Mack. Username Remaker. "
    "LIGHT/DARK boxes empty dest Dark from the 60s. "
    "My Lord Is That Legal dested dual We Will Not Go Quietly empty. "
    "Coruscant, Senate dested Coruscant: Galactic Senate. "
    "Lott Dod x3. EMPS dested Emperor's Personal Shuttle. "
    "Saber 1 dested Vader's Lightsaber. SFS L-s.7.3 dested SFS L-s9.3 Laser Cannons. "
    "DX: War Room dested Death Star: War Room True. DX dested Death Star. "
    "Ability x2 dested Ability, Ability, Ability. Ghhhk True dested Ghhhk without True. "
    "Short Range combo dested Short-range Fighters. WMAOP dested We Must Accelerate Our Plans. "
    "K&D dested Knowledge And Defense True. Scramble dested as written. "
    "Battle Droid dested as written. Motion Supported dested as written. "
    "Accepting Trade Federation dested as written. We Blocked A Pathway dested as written. "
    "Code Clearance dested Do They Have A Code Clearance? True. "
    "Shield 12 cropped. Unique 60. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Senate In Chaos"
LS_CARDS = [
    n("Plead My Case To The Senate / Senate In Chaos"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("Draw Their Fire"),
    n("Wokling", True),
    n("Strike Planning"),
    n("Coruscant: Night Club"),
    n("Kiffex"),
    n("Bravo Fighter", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Han, Chewie, And The Falcon", qty=3),
    n("Queen Amidala, Ruler Of Naboo", qty=4),
    n("Senator Palpatine", qty=3),
    n("Senator Mon Mothma", qty=2),
    n("Horox Ryyder", qty=3),
    n("Yarua"),
    n("Liana Merian"),
    n("Corran Horn", qty=2),
    n("Princess Leia", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=3),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("I Will Not Defer"),
    n("Honor Of The Jedi"),
    n("Imperial Atrocity", True),
    n("Imperial Atrocity"),
    n("Senate Hovercam"),
    n("Your Insight Serves You Well"),
    n("Plea To The Court"),
    n("Ascertaining The Truth"),
    n("The Gravest Of Circumstances"),
    n("Moes Combo"),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Might Of The Republic", qty=3),
    n("A Jedi's Resilience", qty=3),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Do, Or Do Not"),
    n("Weapons Display", True),
    n("Planetary Defenses", True),
    n("Battle Plan"),
    n("Aim High"),
    n("Chasm", True),
    n("The Professor", True),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / We Will Not Go Quietly"
DS_CARDS = [
    n("My Lord, Is That Legal? / We Will Not Go Quietly"),
    n("Blockade Flagship: Bridge"),
    n("Coruscant: Galactic Senate"),
    n("Surface Defense", True),
    n("Lott Dod", qty=3),
    n("Aks Moe", qty=2),
    n("Tikkes"),
    n("Orn Free Taa", qty=2),
    n("Toonbuck Toora", qty=2),
    n("Edcel Bar Gane"),
    n("Baskol Yeesrim"),
    n("Yeb Yeb Adem'thorn"),
    n("Battle Droid Squad"),
    n("Battle Droid"),
    n("Dengar", True),
    n("Emperor Palpatine"),
    n("DS-61-2"),
    n("Darth Vader", True),
    n("Bossk", True),
    n("Darth Maul With Lightsaber", qty=3),
    n("Vader's Lightsaber"),
    n("Punishing One", True),
    n("Vader's Personal Shuttle", True),
    n("Emperor's Personal Shuttle"),
    n("Hound's Tooth", True),
    n("Black 2", True),
    n("SFS L-s9.3 Laser Cannons"),
    n("Kashyyyk"),
    n("Naboo"),
    n("Death Star: War Room", True),
    n("Death Star"),
    n("Ability, Ability, Ability"),
    n("Ghhhk", qty=3),
    n("First Strike"),
    n("Motion Supported"),
    n("This Is Outrageous!"),
    n("Accepting Trade Federation"),
    n("We Blocked A Pathway"),
    n("Scramble", qty=3),
    n("I Have You Now"),
    n("Sense", qty=2),
    n("Short-range Fighters", qty=2),
    n("Limited Resources"),
    n("Vote Now!"),
    n("We Must Accelerate Our Plans"),
    n("Cold Feet", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Firepower", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Leave Them To Me", True),
    n("Fanfare", True),
]
DS_ADD = []
