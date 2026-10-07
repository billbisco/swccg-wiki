#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Tim Simon.

Source: MPC-2014-Day-1-Main-Event.pdf pages 98–99 (2013 form, 15 shields).
Username Aylets.
"""
from __future__ import annotations

PLAYER = "Tim Simon"
USERNAME = "Aylets"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 98
DS_PAGE = 99
LS_SCAN = "2014 Match Play Championship Day 1 Tim Simon LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Tim Simon DS.png"
LS_DECK_NAME = "RTP"
DS_DECK_NAME = "Stunning, Truly"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Tim Simon. Username Aylets. LIGHT checked. "
    "Deck name RTP. We'll Handle This / Duel of the Fates dested We'll Handle This / Duel Of The Fates. "
    "Lando Calrissian, Unlikely Hero dested Lando Calrissian, Unlikely Hero. Lady Luck dested Lady Luck. "
    "Ayyy Put Your Weapon dested Ayyy, Put Your Weapon Down. I'm With You Too dested I'm With You Too. "
    "Bothan Shuffle and Desperate Reach dested Bothan Shuffle & Desperate Reach. "
    "Unique overcounts sheet-accurate (Let The Wookiee Win (V) x3, Luke Skywalker, Strong In The Force x3, "
    "Wesa Gotta Grand Army x2, Mace Windu, Master Of The Order x2, Qui-Gon Jinn, Jedi Master x3, "
    "Escape Pod (V) x2, Aayla Secura x2, Artoo-Detoo In Red 5 x3, Bothan Shuffle & Desperate Reach x2, "
    "Blast The Door, Kid! x2, Blaster Deflection x2, Luke's Bionic Hand x2). NO_DEST Ayyy, Put Your Weapon Down (V); Bothan Shuffle & Desperate Reach. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Tim Simon. Username Aylets. DARK checked. "
    "Deck name Stunning, Truly. ASM dested A Stunning Move / A Valuable Hostage. "
    "Coruscant: Palpatine's Quarters dested Coruscant: Palpatine's Quarters. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi. Galen Marek, Starkiller dested "
    "Galen Marek, Starkiller. Galen's Lightsaber Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "The Phantom Menace at line 11 and line 60. Unique overcounts sheet-accurate "
    "(Darth Maul With Lightsaber x2, Count Dooku x3, Grievous, Hunter Of Jedi x2, "
    "Galen Marek, Starkiller x2, Force Field (V) x2, Sonic Bombardment (V) x2, "
    "Battle Droid Squad x2, Force Lightning x2, Disarmed x2, Dr. Evazan & Ponda Baba x2, "
    "The Phantom Menace x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates"),
    n("Inner Strength"),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Theed Palace Generator Core"),
    n("Heading For The Medical Frigate"),
    n("Rycar Ryjerd", True),
    n("Sai'torr Kal Fas", True),
    n("Wokling", True),
    n("Let The Wookiee Win", True, qty=3),
    n("Lando Calrissian, Scoundrel"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Lightsaber Proficiency"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Luke Skywalker, Jedi Knight"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Naboo: Boss Nass' Chambers"),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Qui-Gon Jinn, Jedi Master", qty=3),
    n("Undercover", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Jedi Lightsaber", True),
    n("Escape Pod", True, qty=2),
    n("Ayyy, Put Your Weapon Down", True),
    n("Aayla Secura", qty=2),
    n("Han, Chewie, And The Falcon"),
    n("I'm With You Too", True),
    n("Guardian's Lightsaber"),
    n("Artoo-Detoo In Red 5", qty=3),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Bothan Shuffle & Desperate Reach", qty=2),
    n("Jedi Levitation", True),
    n("Clinging To The Edge", True),
    n("Blast The Door, Kid!", qty=2),
    n("Blaster Deflection", qty=2),
    n("Corran Horn"),
    n("Houjix"),
    n("Obi-Wan's Journal"),
    n("Luke's Lightsaber"),
    n("Mercenary Armor", True),
    n("Weapon Levitation"),
    n("Imperial Atrocity", True),
    n("Luke's Bionic Hand", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Battle Plan"),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Planetary Defenses", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
]
LS_ADD = []


DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Ni Chuba Na??", True),
    n("Blaster Rack", True),
    n("Imperial Justice", True),
    n("The Phantom Menace"),
    n("Maul's Sith Infiltrator"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Count Dooku", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen Marek, Starkiller", qty=2),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Dooku's Lightsaber"),
    n("Grievous' Lightsabers"),
    n("Nal Hutta"),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Force Field", True, qty=2),
    n("Operational As Planned", True),
    n("Protocol Failure"),
    n("A Sith's Weapon"),
    n("Victory"),
    n("Dengar With Blaster Carbine", True),
    n("Ghhhk"),
    n("Lightsaber Deficiency", True),
    n("Masterful Move & Endor Occupation"),
    n("Sonic Bombardment", True, qty=2),
    n("Knowledge And Defense", True),
    n("Battle Droid Squad", qty=2),
    n("Force Lightning", qty=2),
    n("Presence Of The Force"),
    n("Disarmed", qty=2),
    n("Dr. Evazan & Ponda Baba", qty=2),
    n("Ket Maliss, Shadow Killer"),
    n("IG-100 MagnaGuard"),
    n("Garindan", True),
    n("Trophy Of A Kill"),
    n("Cold Feet", True),
    n("No Escape"),
    n("Force Push", True),
    n("Imperial Barrier"),
    n("Sniper & Dark Strike"),
    n("The Phantom Menace"),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance", True),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Firepower", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
    n("Battle Order"),
]
DS_ADD = []
