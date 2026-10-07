#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Marty Terwilliger.

Source: 2012mpcday1.pdf pages 133–134 (2010 form, 12 shields).
Name Marty Terwilliger dested Marty Terwilliger (analog generate empty).
Username blank. Pack player-stubs/Marty_Terwilliger.wiki.
Do not dest as Brian Terwilliger (p27/p28). Do not dest as Chris Terwilliger.
"""
from __future__ import annotations

PLAYER = "Marty Terwilliger"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 133
DS_PAGE = 134
LS_SCAN = "2012 Match Play Championship Day 1 Marty Terwilliger LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Marty Terwilliger DS.png"
LS_DECK_NAME = "3 Tw. Hops Twist Went To Market."
DS_DECK_NAME = "Vader uses Gecio"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Marty Terwilliger dested Marty Terwilliger. "
    "Username blank. LIGHT checked. Deck Name 3 Tw. Hops Twist Went To Market. "
    "Analog generate empty dest as written. Do not dest as Brian Terwilliger. "
    "Do not dest as Chris Terwilliger. "
    "Ultimate Communing True dested Communing True virtual-only. "
    "Slave Quarters - Tatooine dested Tatooine: Slave Quarters. "
    "Ansr Fear Agg True dested Anger, Fear, Aggression True in the 60 analog Casey. "
    "3PO dested C-3PO analog leftover. Strike Force True dested Strikeforce True. "
    "Alderaan Con Ship True dested Alderaan Consular Ship True analog Montgomery. "
    "2X Chewie Protector True dested Chewbacca, Protector True x2. "
    "W y ron Sentry True dested Yavin Sentry True in the 60 analog leftover. "
    "Chewie Enraged True dested Chewbacca, Enraged True. "
    "Landan Calr Ssoardd True dested Lando Calrissian, Scoundrel True. "
    "Blind Jedi True dested as written analog Foth. "
    "Han w/ Pistol dested Han With Heavy Blaster Pistol analog leftover. "
    "2X Imp Atrocity dested Imperial Atrocity x2. "
    "2X Seeking Audience dested Seeking An Audience x2. "
    "Wedge Red Sqd dested Wedge In Red Squadron 1 analog leftover. "
    "Fallen Jedi dested as written analog Harpster. "
    "Sorry Mess / Blaster Prof dested Sorry About The Mess & Blaster Proficiency. "
    "Hear me hold together True dested Hear Me Baby, Hold Together True in the 60 analog Richards. "
    "Your Insight dested Your Insight Serves You Well analog Smith in the 60. "
    "Honor Jedi dested Honor Of The Jedi analog leftover. "
    "3X Luke Skywalker True dested Luke Skywalker True x3. "
    "Houjix / Out of Nowhere dested Houjix & Out Of Nowhere analog Srodoski. "
    "Luke Blaster dested Luke With Blaster Rifle as written. "
    "War Room - Home One dested Home One: War Room. "
    "Tatooine - Obi's Hut dested Tatooine: Obi-Wan's Hut analog leftover. "
    "Lines 54-60 empty diagonal skipped. Unique 60. Shields 12. "
    "Shield Gifted Mind True dested as written. "
    "Yavin Sentry True in the 60 AND shield 12 kept separate analog Foth."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Marty Terwilliger dested Marty Terwilliger. "
    "Username blank. DARK checked. Deck Name Vader uses Gecio. "
    "Establish Control True dested as written analog Gogolen. "
    "Incorg Losses True dested Inconsequential Losses True analog Gogolen. "
    "Attraction Corp True dested Aratech Corporation True analog Gogolen. "
    "Endor Operations empty dested Endor Operations / Imperial Outpost. "
    "Imperial Arrest dested Imperial Arrest Order analog leftover. "
    "Grim Rumors dested as written. "
    "Galen Fighter dested Rogue Shadow analog leftover. "
    "Tempest 5 / 2X Tempest 1 / ditto 2 / Tempest 3 / 6 / 4 dested Tempest Scout analog Gogolen. "
    "AT Cannon True dested AT-AT Cannon True analog leftover. "
    "2X Lightsaber Defy True dested Lightsaber Deficiency True analog leftover. "
    "DSG 1 dested Death Star Gunner analog leftover. "
    "Short range / watch dested Short Range Fighters & Watch Your Back! analog Gogolen. "
    "2X Fighter Come In dested Fighters Coming In analog Gogolen. "
    "Black Leader dested Juno Eclipse, Black Leader analog Eier. "
    "ISB Commander dested as written. "
    "Victory dested Victory analog Kinsey. "
    "Prepar Defense dested Prepared Defenses analog Pistone in the 60. "
    "K&D True dested in the 60 analog Murray. "
    "K&D empty Additional AND True in the 60 kept separate analog Foth. "
    "Additional Endor Operations empty extra sheet-accurate. "
    "Lines 57-60 empty diagonal skipped. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Communing", True),
    n("Master Kenobi", True),
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
    n("C-3PO"),
    n("Commando Training", True),
    n("It's Not My Fault", True),
    n("Strikeforce", True),
    n("Artoo-Detoo In Red 5"),
    n("Alderaan Consular Ship", True),
    n("Tantive IV", True),
    n("Chewbacca, Protector", True, qty=2),
    n("Yavin Sentry", True),
    n("Chewbacca, Enraged", True),
    n("Admiral Ackbar", True),
    n("Shmi Skywalker"),
    n("Yoda, Great Warrior", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Blind Jedi", True),
    n("Han With Heavy Blaster Pistol"),
    n("Imperial Atrocity", qty=2),
    n("Seeking An Audience", qty=2),
    n("We're Doomed"),
    n("Padme Naberrie", True),
    n("Corran Horn"),
    n("Wedge In Red Squadron 1"),
    n("Senator Leia Organa", True),
    n("Fallen Jedi"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Rebel Barrier", True),
    n("Chewbacca's Bowcaster"),
    n("Security Breach", True),
    n("Hear Me Baby, Hold Together", True),
    n("Your Insight Serves You Well"),
    n("Honor Of The Jedi"),
    n("Luke Skywalker", True, qty=3),
    n("Houjix & Out Of Nowhere"),
    n("Jedi Levitation", True, qty=2),
    n("Flash Of Insight", True),
    n("It Could Be Worse"),
    n("Use The Force", True, qty=2),
    n("Run Luke, Run!", True, qty=2),
    n("Rebel Leadership", True),
    n("Nabrun Leids"),
    n("Spiral"),
    n("Home One"),
    n("Luke With Blaster Rifle"),
    n("Sabotage"),
    n("Home One: War Room"),
    n("Tatooine: Obi-Wan's Hut"),
    n("Tatooine: Cantina"),
    n("Tatooine"),
]
LS_SHIELDS = [
    n("Ultimatum", True),
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan", True),
    n("The Professor"),
    n("Aim High"),
    n("Simple Tricks And Nonsense", True),
    n("Gifted Mind", True),
    n("Let's Keep A Little Optimism Here"),
    n("Do, Or Do Not", True),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Establish Control", True),
    n("Inconsequential Losses", True),
    n("Aratech Corporation", True),
    n("Knowledge And Defense", True),
    n("Endor Operations / Imperial Outpost"),
    n("Combat Response", True),
    n("Imperial Arrest Order"),
    n("Establish Secret Base", True),
    n("Grim Rumors"),
    n("Endor Shield", True),
    n("Endor: Bunker"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Back Door"),
    n("Endor", qty=2),
    n("Rogue Shadow"),
    n("Tempest Scout 5"),
    n("Sergeant Irol", True),
    n("AT-AT Cannon", True),
    n("Tempest Scout 1", qty=2),
    n("Tempest Scout 2"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Defensive Fire", True, qty=2),
    n("Sneak Attack", True, qty=2),
    n("Lieutenant Arnet"),
    n("Death Star Gunner"),
    n("Sergeant Barich"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Darth Vader", True),
    n("Trample", qty=2),
    n("ISB Commander"),
    n("Fighters Coming In", qty=2),
    n("Baron Soontir Fel"),
    n("Saber 1"),
    n("Blizzard 1", True),
    n("Grand Admiral Thrawn"),
    n("Tempest Scout 3"),
    n("Corporal Drelosyn"),
    n("General Nevar", True),
    n("Tempest Scout 6"),
    n("Tempest Scout 4"),
    n("U-3PO"),
    n("Major Marquand"),
    n("Imperial Decree"),
    n("Juno Eclipse, Black Leader"),
    n("Zuckuss In Mist Hunter"),
    n("Black 2", True),
    n("Admiral Ozzel"),
    n("Vader's Personal Shuttle", True),
    n("Victory"),
    n("Lieutenant Watts"),
    n("Protocol Failure"),
    n("Prepared Defenses"),
]
DS_SHIELDS = [
    n("There Is No Try", True),
    n("Come Here You Big Coward", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Battle Order", True),
    n("Abyss", True),
    n("Fanfare"),
    n("Allegations Of Corruption", True),
    n("Secret Plans", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower"),
    n("A Useless Gesture", True),
    n("Resistance", True),
]
DS_ADD = [
    n("Knowledge And Defense"),
    n("Endor Operations / Imperial Outpost"),
]
