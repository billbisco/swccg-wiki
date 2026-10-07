#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Matt Spear.

Source: MPC-2014-Day-1-Main-Event.pdf pages 106–107 (2013 form, 15 shields).
Username blank.
"""
from __future__ import annotations

PLAYER = "Matt Spear"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 107
DS_PAGE = 106
LS_SCAN = "2014 Match Play Championship Day 1 Matt Spear LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Matt Spear DS.png"
LS_DECK_NAME = "The Cryer myser"
DS_DECK_NAME = "Set Your Course For Alderaan"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Matt Spear. Username blank. LIGHT checked. "
    "Deck name The Cryer myser. IITFYS (V) dested It Is The Future You See (V) / "
    "A Tremor In The Force (V). Lando UH dested Lando Calrissian, Unlikely Hero. "
    "Lando's Luxury Yacht dested Lady Luck (V). SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Unique overcounts sheet-accurate (Imperial Atrocity (V) x2, Blaster Deflection x2, "
    "Rebel Leadership (V) x3, Luke Skywalker, Strong In The Force (V) x2, Mace Windu (V) x3, "
    "A Jedi's Resilience x2, Artoo-Detoo In Red 5 x2, Let The Wookiee Win (V) x3, "
    "Speak With The Jedi Council x2, Wesa Gotta Grand Army x3, Escape Pod (V) x2, "
    "Luke Skywalker, Jedi Knight x2, Master Qui-Gon (V) x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Matt Spear. Username blank. DARK checked. "
    "Deck name Set Your Course For Alderaan. SYCFA dested Set Your Course For Alderaan / "
    "The Ultimate Power In The Universe. Starting location annotation Death Star. "
    "Line 24 Lateral Damage is a margin note, skipped. Superlaser dested Superlaser. "
    "U-3PO dested U-3PO (Yoo-Threepio). Visage dested Visage Of The Emperor. "
    "Unique overcounts sheet-accurate (Imperial Propaganda (V) x3, Imperial Barrier x2, "
    "Imperial Command x2, Cease Fire x2, Stunning Leader x3, Darth Sidious x2, "
    "TIE Sentry Ships (V) x2, Lord Sidious x2, Darth Maul With Lightsaber x2). "
    "(V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("It Is The Future You See / A Tremor In The Force", True),
    n("Hoth: Echo Command Center (War Room)"),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Corran Horn"),
    n("Naboo: Boss Nass' Chambers"),
    n("Imperial Atrocity", True, qty=2),
    n("Blaster Deflection", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Hoth: Echo Command Center (War Room)"),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Han, Chewie, And The Falcon", True),
    n("What're You Tryin' To Push On Us"),
    n("Seeking An Audience", True),
    n("Mace Windu", True, qty=3),
    n("A Jedi's Resilience", qty=2),
    n("Weapon Levitation"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Speak With The Jedi Council", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Jedi Levitation", True),
    n("Naboo: Battle Plains"),
    n("Clash Of Sabers"),
    n("Yavin 4: Massassi War Room", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Hear Me Baby, Hold Together", True),
    n("Escape Pod", True, qty=2),
    n("Luke's Lightsaber"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Jedi Lightsaber", True),
    n("Master Qui-Gon", True, qty=2),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Home One"),
    n("Admiral Ackbar", True),
    n("Leia, Rebel Princess"),
    n("Lady Luck", True),
    n("Houjix"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred", True),
    n("The Professor", True),
    n("Chasm", True),
    n("Aim High", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense", True),
    n("Only Jedi Carry That Weapon", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum", True),
    n("Planetary Defenses", True),
    n("He Can Go About His Business", True),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("Yavin Sentry", True),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Dreaded Imperial Starfleet", True),
    n("A Million Voices Crying Out"),
    n("Kuat Drive Yards", True),
    n("Superlaser"),
    n("Commence Primary Ignition"),
    n("Imperial Propaganda", True, qty=3),
    n("Imperial Justice", True),
    n("Imperial Barrier", qty=2),
    n("Imperial Command", qty=2),
    n("Conquest", True),
    n("Cease Fire", qty=2),
    n("Stunning Leader", qty=3),
    n("Dominator", True),
    n("Stalker", True),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("He Is Not Ready", True),
    n("Darth Sidious", qty=2),
    n("TIE Sentry Ships", True, qty=2),
    n("U-3PO (Yoo-Threepio)"),
    n("Kiffex"),
    n("Nal Hutta"),
    n("Rendili"),
    n("Vengeance"),
    n("Avenger"),
    n("Visage Of The Emperor"),
    n("Cold Feet", True),
    n("Devastator", True),
    n("The Phantom Menace", True),
    n("Admiral Motti", True),
    n("Force Push", True),
    n("Chimaera"),
    n("Lord Sidious", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Thunderflare"),
    n("Tyrant"),
    n("Carida"),
    n("Accuser", True),
    n("Tarkin Doctrine"),
    n("Judicator"),
    n("Victory"),
    n("Disarmed"),
    n("Prepared Defenses"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Fanfare", True),
    n("Leave Them To Me", True),
    n("There Is No Try"),
    n("Firepower", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Death Star Sentry", True),
]
DS_ADD = []
