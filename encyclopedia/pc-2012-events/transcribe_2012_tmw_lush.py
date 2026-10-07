#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Matt Lush.

Source: 2012TMWDay1.pdf pages 15–16 (typed slang printout, not a handwritten
Xerox form). Name Matt Lush dested Matt Lush analog leftover generate_2015_2016
CANON / player-stubs/Matt_Lush.wiki. Username blank. p15 Dark. p16 Light.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Matt Lush"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 16
DS_PAGE = 15
LS_SCAN = "2012 Texas Mini Worlds Day 1 Matt Lush LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Matt Lush DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed slang printout (not a handwritten Xerox form). "
    "Name Matt Lush dested Matt Lush analog leftover player-stubs/Matt_Lush.wiki. "
    "Username blank. Do not dest as a new person."
)
LS_NOTE = (
    "Typed slang printout. Name Matt Lush dested Matt Lush. Username blank. "
    "Anger, Fear, Agression True dested Anger, Fear, Aggression analog leftover True. "
    "Yavin IV: Massassi Throne Room dested Yavin 4: Massassi Throne Room analog leftover Anderson. "
    "Hoth: War Room dested Hoth: Echo War Room analog leftover Barnes. "
    "Naboo: Boss Nass's Chambers dested Naboo: Boss Nass' Chambers analog leftover. "
    "Kiffex crossed skip. "
    "Qui-gon with Lightsaber dested Qui-Gon Jinn With Lightsaber analog leftover Nats qty=2. "
    "Luke Skywalker, Strong in the Force x2 crossed dest replacement Luke Skywalker, Jedi Knight qty=3 analog leftover Nats. "
    "Obi-wan with Lightsaber dested Obi-Wan With Lightsaber analog leftover Nats. "
    "Sai Tor Kal Fas dested Sai'torr Kal Fas analog leftover True. "
    "Grimtaash qty=2 analog leftover. "
    "Wesa Gotta Grand Army dested Wesa Gotta Grand Army analog leftover Anderson qty=2. "
    "Hear Me Baby, Hold Together True crossed skip. "
    "Smoke Screen x4 crossed to x3 dest qty=3 unique overcount sheet-accurate. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency analog leftover Anderson. "
    "Krayt Dragon Howl & Armed and Dangerous crossed skip. "
    "Nabrun dested Nabrun Leids analog leftover qty=2. "
    "Shield Yavin Sentry True dested Yavin Sentry analog leftover Nats True. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed slang printout. Name Matt Lush dested Matt Lush. Username blank. "
    "Knowledge & Defense dested Knowledge And Defense analog leftover True IN THE 60. "
    "Hunt Down and Destroy The Jedi empty dested Hunt Down And Destroy The Jedi analog leftover. "
    "Ni Chuba Na(V) dested Ni Chuba Na?? analog leftover True. "
    "U-3PO dested U-3PO analog leftover Bordier. "
    "Endor: Back Door dested analog leftover. "
    "EPP Maul x3 dested Darth Maul With Lightsaber analog leftover Barnes qty=3 "
    "(replacement for crossed Darth Maul, Young Apprentice x3). "
    "Darth Vader, Dark Lord of the Sith x4 unique overcount sheet-accurate. "
    "Emperor Palpatine x2 crossed to 1 dest qty=1. "
    "Dr. Evazan & Ponda Boba dested Dr. Evazan & Ponda Baba analog leftover. "
    "Bane Malar dested Bane Malar analog leftover True. "
    "Kir Kanos with Force Pike dested Kir Kanos With Force Pike analog leftover Alperstein. "
    "4LOM with Concussion Rifle dested 4-LOM With Concussion Rifle analog leftover True. "
    "Boba, BH (Upkeep) x2 dested Boba Fett, Bounty Hunter analog leftover Baroni qty=2 "
    "(replacement for crossed Maul's Sith Infiltrator x2). "
    "Maul's Double-bladed Lightsaber crossed skip. "
    "Sidious's Lightsaber dested Sidious' Lightsaber analog leftover SoCal Anderson. "
    "Ability, Ability, Ability dested analog leftover Anis True. "
    "Elis dested Elis Helrot analog leftover qty=2. "
    "Shield We'll Let-a Fate Decide, HUH? dested We'll Let Fate-a Decide, Huh? analog leftover Richards. "
    "Shield Weapon of a Sith dested Weapon Of A Sith analog leftover. "
    "Unique 61 sheet-accurate. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Home One: War Room"),
    n("Hoth: Echo War Room"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Mace Windu", True, qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Admiral Ackbar", True),
    n("Padme Naberrie", True),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Luke's Bionic Hand"),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Journal"),
    n("Jedi Lightsaber", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Home One"),
    n("Tantive IV", True),
    n("Sai'torr Kal Fas", True),
    n("Hindsight", True),
    n("Civil Disorder", True),
    n("Scrambled Transmission", True),
    n("Draw Their Fire"),
    n("Grimtaash", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=2),
    n("Smoke Screen", qty=3),
    n("Clash Of Sabers"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Blaster Deflection", qty=2),
    n("Sense", qty=2),
    n("Nabrun Leids", qty=2),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Only Jedi Carry That Weapon"),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hunt Down And Destroy The Jedi"),
    n("Executor: Meditation Chamber"),
    n("Executor: Holotheatre"),
    n("Visage Of The Empire"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Conduct Your Search"),
    n("U-3PO"),
    n("Endor: Back Door"),
    n("Blockade Flagship: Bridge"),
    n("Death Star: War Room", True),
    n("Darth Maul With Lightsaber", qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=4),
    n("Darth Sidious", qty=2),
    n("Emperor Palpatine"),
    n("Mara Jade With Lightsaber"),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Bane Malar", True),
    n("Kir Kanos With Force Pike"),
    n("4-LOM With Concussion Rifle", True),
    n("Boba Fett, Bounty Hunter", qty=2),
    n("Blizzard 4", qty=2),
    n("Darth Vader's Lightsaber"),
    n("Sidious' Lightsaber"),
    n("Restraining Bolt"),
    n("Visage Of The Emperor", qty=2),
    n("The Phantom Menace", qty=2),
    n("Emperor's Power", True),
    n("Blast Door Controls"),
    n("Tarkin's Bounty", True),
    n("Ability, Ability, Ability", True),
    n("No Escape"),
    n("First Strike"),
    n("Blaster Rack", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("I Have You Now", qty=2),
    n("Force Lightning"),
    n("Masterful Move & Endor Occupation"),
    n("Force Push", True),
    n("Force Field", True, qty=2),
    n("Comscan Detection", True, qty=2),
    n("Elis Helrot", qty=2),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Weapon Of A Sith"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = []
