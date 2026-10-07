#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Dalton.

Source: 2012mpcday1.pdf pages 63–64 (2010 form, 12 shields).
Name Dalton dested Dalton (last-name-only; analog empty). Username blank.
p63 Light Anger, Fear, Aggression. p64 Dark My Lord, Is That Legal?.
Pack player-stubs/Dalton.wiki. Do not invent a first name.
"""
from __future__ import annotations

PLAYER = "Dalton"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 63
DS_PAGE = 64
LS_SCAN = "2012 Match Play Championship Day 1 Dalton LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Dalton DS.png"
LS_DECK_NAME = "Profshit"
DS_DECK_NAME = "I heart Gemme"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Dalton dested Dalton. Username blank. LIGHT checked. "
    "Deck Name Profshit. Event MPC. "
    "Anger Fear Aggression dested Anger, Fear, Aggression True. "
    "You Can Either Profit dested You Can Either Profit By This... / Or Be Destroyed empty. "
    "Han True dested Han True. "
    "Captain Han dested Captain Han Solo. "
    "Threepio w/ Parts dested Threepio With His Parts Showing. "
    "Strike Force dested Strikeforce True. "
    "Flash of Insight dested Flash Of Insight True. "
    "Skywalker dested Luke Skywalker. "
    "SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Unique 60. Additional empty. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Dalton dested Dalton. Username blank. "
    "LIGHT/DARK boxes empty; dested Dark from the 60. Deck Name I heart Gemme. Event MPC. "
    "My Lord Is That Legal dested My Lord, Is That Legal? / I Will Make It Legal empty. "
    "Squabbling Delegates dested Squabbling Delegates x3. "
    "Accepting Trade Fed Control dested Accepting Trade Federation Control. "
    "Our Blockade Is Peace Lord dested Our Blockade Is Perfectly Legal. "
    "SRF/W4B dested Short Range Fighters & Watch Your Back x2. "
    "Fallen Portal dested Falling Portal. "
    "Saber 1 dested Saber 1. "
    "Yeb Yeb Ademthorn dested Yeb Yeb Adem'thorn. "
    "Baskol Yeesrim dested Baskol Yeesrim. "
    "Toonbuck Toora dested Toonbuck Toora x2. "
    "Mobility Support dested as written. "
    "Handheld Blaster dested as written True. "
    "Unique 60. Additional empty. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Quick Draw", True),
    n("I Must Be Allowed To Speak", True),
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Heading For The Medical Frigate"),
    n("Han", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Jabba's Palace"),
    n("Rycar Ryjerd", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Obi-Wan's Lightsaber"),
    n("Lando Calrissian, Scoundrel"),
    n("Luke's Lightsaber"),
    n("Chewbacca, Protector"),
    n("Threepio With His Parts Showing"),
    n("Captain Han Solo"),
    n("Leia, Rebel Princess", qty=2),
    n("Luke Skywalker, Strong In The Force", True, qty=4),
    n("Padmé Naberrie", True),
    n("Lando Calrissian, Scoundrel"),
    n("Admiral Ackbar", True),
    n("Artoo-Detoo In Red 5"),
    n("Home One"),
    n("Sai'torr Kal Fas", True),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Lightsaber Deficiency"),
    n("Luke's Bionic Hand", True, qty=2),
    n("Obi-Wan's Journal"),
    n("Strikeforce", True),
    n("Flash Of Insight", True),
    n("Honor Of The Jedi", True),
    n("Houjix", True),
    n("It Could Be Worse", True),
    n("Run Luke, Run!", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("The Force Is Strong With This One"),
    n("Luke Skywalker"),
    n("Weapon Levitation"),
    n("Hear Me Baby, Hold Together", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("Rebel Leadership", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Gift Of The Master"),
    n("Seeking An Audience", True, qty=2),
    n("Grimtaash"),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again"),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense", True),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Knowledge And Defense", True),
    n("We Must Accelerate Our Plans"),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Squabbling Delegates", qty=3),
    n("Tikkes"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Accepting Trade Federation Control"),
    n("Mobility Support"),
    n("This Is Outrageous!"),
    n("Our Blockade Is Perfectly Legal"),
    n("Sense"),
    n("Masterful Move & Endor Occupation"),
    n("Surface Defense"),
    n("Cold Feet", True),
    n("Combat Readiness"),
    n("Come Here You Big Coward", True),
    n("Imperial Propaganda", True),
    n("Sonic Bombardment", qty=2),
    n("Monnok"),
    n("Presence Of The Force"),
    n("Battle Droid Squad", True),
    n("Coruscant Guard", True),
    n("SFS L-s9.3 Laser Cannons", True),
    n("Handheld Blaster", True),
    n("Bossk", True),
    n("Boba Fett", True),
    n("DS-61-2"),
    n("Punishing One", True),
    n("Dengar", True),
    n("Saber 1"),
    n("Baron Soontir Fel"),
    n("Vader's Personal Shuttle", True),
    n("Darth Vader", True),
    n("Falling Portal"),
    n("Orn Free Taa", qty=2),
    n("Aks Moe", qty=2),
    n("Toonbuck Toora", qty=2),
    n("Lott Dod", qty=3),
    n("Yeb Yeb Adem'thorn"),
    n("Baskol Yeesrim"),
    n("Something Special Planned For Them", True),
    n("Blast Door Controls"),
    n("Ability, Ability, Ability"),
    n("First Strike"),
    n("Combat Response", True),
    n("Blockade Flagship: Bridge"),
    n("Coruscant: Galactic Senate"),
    n("Naboo"),
    n("Death Star: War Room"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Battle Order"),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption", True),
    n("Come Here You Big Coward", True),
    n("Oppressive Enforcement", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans"),
]
DS_ADD = []
