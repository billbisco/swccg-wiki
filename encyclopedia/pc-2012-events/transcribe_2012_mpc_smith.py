#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Reid Smith.

Source: 2012mpcday1.pdf pages 127–128 (2010 form, 12 shields).
Name Smith dested Reid Smith (Username 3MW0J8 analog 2013 leftover).
p127 Light Plead My Case To The Senate. p128 Dark My Lord, Is That Legal?.
Pack player-stubs/Reid_Smith.wiki.
Do not dest as a new person. Do not rewrite 2013 leftovers (Communing / Kessel).
Do not dest as 2013 Worlds RSmith (that Username is Conway East / Buck Faston).
"""
from __future__ import annotations

PLAYER = "Reid Smith"
USERNAME = "3MW0J8"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 127
DS_PAGE = 128
LS_SCAN = "2012 Match Play Championship Day 1 Reid Smith LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Reid Smith DS.png"
LS_DECK_NAME = "Aloha Senate"
DS_DECK_NAME = "Haters Gonna Hate"
NOTE = "Handwritten 2010 Xerox form. Username 3MW0J8."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Smith dested Reid Smith. Username 3MW0J8. "
    "LIGHT checked. Deck Name Aloha Senate. Event Name MPC 2012. "
    "Plead My Case / Sanity dested Plead My Case To The Senate / Sanity And Compassion analog Bollentino. "
    "Senator Palpatine x3. Queen Amidala, Ruler Of Naboo x4. Horox Ryyder x3. "
    "Yarna dested Yarua analog Krueger. Princess Leia True dested Princess Leia True. "
    "Han, Chewie, AND THE FALCON dested Han, Chewie, And The Falcon. "
    "Senate Hovercar dested Senate Hovercam. AFA True dested in the 60 analog Casey. "
    "HFTMF empty dested in the 60 analog Casey. Your Insight empty in the 60 AND True in shields kept separate analog Foth. "
    "Do not copy 2013 leftover Communing. Unique 60. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Smith dested Reid Smith. Username 3MW0J8. "
    "DARK checked. Deck Name Haters Gonna Hate. Event Name MPC 2012. "
    "My Lord Is That Legal dested My Lord, Is That Legal? / I Will Make It Legal empty. "
    "Lott Dod x3. Orn Free Taa x2. Aks Moe x2. Tusken Raider dested as written. "
    "Job Yob Aden Thorn dested Jabba The Hutt. Baskol dested Baskol Yeesrim. "
    "Eeth Bar Gune dested as written. Howlrunner dested OS-72-1 In Obsidian 1 analog lore call sign. "
    "Squabbling Delegates x3 analog Dalton. Sense (Prem) dested Sense. "
    "Senate Hovercar dested Senate Hovercam. Combat Response True dested as written. "
    "K&D True dested in the 60 analog Murray. Motion Supported dested as written analog Mack. "
    "Accepting Trade Federation Control dested as written analog Mack. "
    "Do not copy 2013 leftover Kessel. Unique 60. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("Draw Their Fire"),
    n("Strike Planning"),
    n("Houjix", True),
    n("Coruscant: Night Club"),
    n("Kiffex"),
    n("Senator Palpatine", qty=3),
    n("Queen Amidala, Ruler Of Naboo", qty=4),
    n("Horox Ryyder", qty=3),
    n("Senator Mon Mothma", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=3),
    n("Luke With Lightsaber", qty=3),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Corran Horn", qty=2),
    n("Liana Merian"),
    n("Yarua"),
    n("Princess Leia", True),
    n("Lando Calrissian, Scoundrel"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Bravo Fighter", True),
    n("Might Of The Republic", qty=3),
    n("A Jedi's Resilience", qty=3),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Skywalkers"),
    n("Imperial Atrocity", True, qty=2),
    n("Your Insight Serves You Well"),
    n("Ascertaining The Truth"),
    n("The Gravest Of Circumstances"),
    n("Plea To The Court"),
    n("I Will Not Defer"),
    n("Honor Of The Jedi"),
    n("Senate Hovercam"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("He Can Go About His Business", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Planetary Defenses", True),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Blockade Flagship: Bridge"),
    n("Kashyyyk"),
    n("Naboo"),
    n("Death Star"),
    n("Death Star: War Room", True),
    n("Lott Dod", qty=3),
    n("Orn Free Taa", qty=2),
    n("Aks Moe", qty=2),
    n("Darth Maul With Lightsaber", qty=3),
    n("Tusken Raider", qty=2),
    n("Battle Droid Squad"),
    n("Boba Fett"),
    n("Jabba The Hutt"),
    n("Emperor Palpatine"),
    n("Darth Vader", True),
    n("Dengar", True),
    n("Eeth Bar Gune"),
    n("Baskol Yeesrim"),
    n("Tikkes"),
    n("Bossk", True),
    n("DS-61-2"),
    n("Black 2", True),
    n("Emperor's Personal Shuttle"),
    n("Vader's Personal Shuttle", True),
    n("OS-72-1 In Obsidian 1", True),
    n("Punishing One", True),
    n("Saber 1"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Squabbling Delegates", qty=3),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Sense", qty=2),
    n("Cold Feet", True),
    n("I Have You Now"),
    n("Vote Now!"),
    n("Surface Defense", True),
    n("Limited Resources"),
    n("We Must Accelerate Our Plans"),
    n("Senate Hovercam", qty=2),
    n("First Strike"),
    n("Motion Supported"),
    n("Ability, Ability, Ability"),
    n("Our Blockade Is Perfectly Legal"),
    n("This Is Outrageous!"),
    n("Accepting Trade Federation Control"),
    n("Combat Response", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Order Enforcement"),
]
DS_ADD = []
