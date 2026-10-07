#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Kyle Krueger.

Source: 2012mpcday1.pdf pages 107–108 (2010 form, 12 shields).
Name Kyle Krueger dested Kyle Krueger (generate_2014_mpc CANON;
2014 leftover PLAYER=Kyle Krueger USERNAME=Meto — do not copy Meto).
p107 Dark Carbon Chamber Testing. p108 Light Plead My Case To The Senate.
Username blank. Pack player-stubs/Kyle_Krueger.wiki.
Do not dest as Kyle Kreuger as written spelling.
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Kyle Krueger"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 108
DS_PAGE = 107
LS_SCAN = "2012 Match Play Championship Day 1 Kyle Krueger LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Kyle Krueger DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form. Username blank."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Kyle Krueger dested Kyle Krueger. "
    "Username blank. LIGHT checked. Do not copy 2014 leftover Username Meto. "
    "Plead My Case To The Senate dested dual Senate In Chaos empty. "
    "Yarna dested Yarua. Nightclub dested Coruscant: Night Club. "
    "Princess Leia True dested Princess Leia True. "
    "Aim High True dested Aim High without True. "
    "Imperial Atrocity True plus ditto empty dested True x1 plus empty x1. "
    "A Jedi's Resilience x3 sheet-accurate. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Kyle Krueger dested Kyle Krueger. "
    "Username blank. DARK checked. Do not copy 2014 leftover Username Meto. "
    "Carbon Chamber Testing dested dual Twin Suns Of Karsan empty. "
    "Any Method Necessary dested Any Methods Necessary. "
    "The Emperor True plus dittos empty dested The Emperor True x1 plus empty x2. "
    "Aiii dested Aiiii! Aaa! Agggggggggg! x4. "
    "The Emperor's Reach dested as written. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Senate In Chaos"
LS_CARDS = [
    n("Plead My Case To The Senate / Senate In Chaos"),
    n("Anger, Fear, Aggression", True),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("Strike Planning"),
    n("Wokling", True),
    n("Draw Their Fire"),
    n("Your Insight Serves You Well"),
    n("Coruscant: Night Club"),
    n("Endor"),
    n("Corran Horn", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=3),
    n("Horox Ryyder", qty=3),
    n("Liana Merian"),
    n("Princess Leia", True),
    n("Queen Amidala, Ruler Of Naboo", qty=4),
    n("Senator Mon Mothma", qty=2),
    n("Senator Palpatine", qty=3),
    n("Yarua"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Bravo Fighter", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("A Jedi's Resilience", qty=3),
    n("Impressive, Most Impressive", True),
    n("Inconsequential Barriers"),
    n("Might Of The Republic", qty=2),
    n("The Bith Shuffle & Desperate Reach"),
    n("Weapon Levitation"),
    n("Ascertaining The Truth"),
    n("Honor Of The Jedi"),
    n("I Will Not Defer"),
    n("Imperial Atrocity", True),
    n("Imperial Atrocity"),
    n("Plea To The Court"),
    n("Seeking An Audience", True),
    n("Senate Hovercam"),
    n("The Gravest Of Circumstances"),
]
LS_SHIELDS = [
    n("He Can Go About His Business", True),
    n("Your Insight Serves You Well", True),
    n("Aim High"),
    n("Wise Advice"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Affect Mind", True),
    n("Simple Tricks And Nonsense", True),
]
LS_ADD = []

DS_START = "Carbon Chamber Testing / Twin Suns Of Karsan"
DS_CARDS = [
    n("Carbon Chamber Testing / Twin Suns Of Karsan"),
    n("Knowledge And Defense", True),
    n("Cloud City: Security Tower"),
    n("Cloud City: Carbonite Chamber"),
    n("Carbonite Chamber Console"),
    n("Any Methods Necessary"),
    n("Jabba's Palace: Dungeon"),
    n("IG-88", True),
    n("IG-88's Neural Inhibitor", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Dagobah: Cave"),
    n("Hoth: Ice Plains", True),
    n("Death Star: War Room", True),
    n("Kashyyyk"),
    n("4-LOM With Concussion Rifle", True),
    n("Grand Admiral Thrawn", qty=2),
    n("The Emperor's Reach"),
    n("Boba Fett, Bounty Hunter"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Sidious"),
    n("Darth Vader", True, qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Mara Jade With Lightsaber", qty=2),
    n("P-59"),
    n("The Emperor", True),
    n("The Emperor", qty=2),
    n("Maul's Sith Infiltrator", qty=2),
    n("Victory", qty=2),
    n("Control & Set For Stun"),
    n("Aiiii! Aaa! Agggggggggg!", qty=4),
    n("Defensive Fire", True, qty=2),
    n("Elis Helrot"),
    n("Force Lightning", qty=2),
    n("I Have You Now"),
    n("Imperial Artillery", qty=2),
    n("Imperial Command"),
    n("Sense", qty=2),
    n("Stunning Leader", qty=3),
    n("First Strike"),
    n("No Escape"),
    n("Search And Destroy"),
    n("Something Special Planned For Them", True),
    n("Special Delivery", True),
    n("The Phantom Menace"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
