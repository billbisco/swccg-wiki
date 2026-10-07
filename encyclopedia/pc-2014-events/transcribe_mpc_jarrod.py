#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 typed GEMP: Jarrod.

Source: MPC-2014-Day-1-Main-Event.pdf pages 65–66 (typed GEMP).
First-name-only dest as written.
"""
from __future__ import annotations

PLAYER = "Jarrod"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 66
DS_PAGE = 65
LS_SCAN = "2014 Match Play Championship Day 1 Jarrod LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Jarrod DS.png"
LS_DECK_NAME = "Untitled"
DS_DECK_NAME = "Untitled"
NOTE = "Typed GEMP list. Name first-name-only as written."
LS_NOTE = (
    "Typed GEMP. Name Jarrod as written. Republic At War / Aggressive Negotiations. "
    "He Can Go About His Business (V) crossed, Planetary Defenses (V) dested "
    "Planetary Defenses (V). Dual Laser Cannon (V) x5 unique overcount. AT-RT x10 "
    "unique overcount. Unique * is uniqueness, not (V). (V) from written (V)."
)
DS_NOTE = (
    "Typed GEMP. Name Jarrod as written. Separatist Uprising / At War With Itself. "
    "Passel Argente crossed, skipped. Tarkin's Orders crossed, Imperial Propaganda "
    "(V) dested Imperial Propaganda (V). They're Still Coming Through handwritten "
    "in interrupts dested They're Still Coming Through. You Cannot Hide Forever "
    "listed in Effects and Shields; dested once as shield (V). Cyborg Commander "
    "analog Grievous, Hunter Of Jedi dested Grievous, Hunter Of Jedi. Squabbling "
    "Delegates dested Squabbling Delegates. Unique overcounts sheet-accurate "
    "(Count Dooku x2, Darth Sidious x2, Darth Maul With Lightsaber x2, Sonic "
    "Bombardment (V) x3, Force Field (V) x2, Short Range Fighters & Watch Your "
    "Back! x2, Sith Fury (V) x2, Fanblade Starfighter x2). (V) from written (V)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Republic At War / Aggressive Negotiations"
LS_CARDS = [
    n("Phylo Gandish", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Anakin Solo"),
    n("Jaina Solo"),
    n("Voolvif Monn"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Wokling", True),
    n("Nick Of Time", True),
    n("Seeking An Audience", True),
    n("Crash Site Memorial"),
    n("Projection Of A Skywalker"),
    n("Rogue Squadron Tactics"),
    n("Begun, The Clone War Has"),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
    n("Sabotage", True, qty=2),
    n("Houjix"),
    n("Sorry About The Mess"),
    n("Lucky Shot", True),
    n("Desperate Tactics"),
    n("Dark Approach", True),
    n("Escape Pod", True),
    n("It's Not My Fault!"),
    n("Rebel Artillery"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Away Put Your Weapon", True, qty=2),
    n("Heading For The Medical Frigate"),
    n("Geonosis: Forward Command Center"),
    n("Muunilinst: Docking Bay"),
    n("Muunilinst: City Of Harnaidan"),
    n("Muunilinst: Harnaidan Plains"),
    n("Muunilinst: Republic Landing Site"),
    n("Dressel"),
    n("Assault On Muunilinst"),
    n("Republic At War / Aggressive Negotiations"),
    n("Alderaan Consular Ship"),
    n("Acclamator-Class Assault Ship", qty=2),
    n("Azure Angel"),
    n("Lady Luck"),
    n("AT-RT", qty=10),
    n("Dual Laser Cannon", True, qty=5),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Ultimatum"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Affect Mind", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Planetary Defenses", True),
]
LS_ADD = []


DS_START = "Separatist Uprising / At War With Itself"
DS_CARDS = [
    n("Garindan", True),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Count Dooku", qty=2),
    n("Darth Sidious", qty=2),
    n("Probot"),
    n("Grievous, Hunter Of Jedi"),
    n("Baskol Yeesrim"),
    n("Lott Dod"),
    n("Tikkes"),
    n("Yeb Yeb Adem'thorn"),
    n("Nute Gunray", True),
    n("Edcel Bar Gane"),
    n("Orn Free Taa"),
    n("Aks Moe"),
    n("Darth Maul With Lightsaber", qty=2),
    n("War Has Begun"),
    n("Something Special Planned For Them", True),
    n("Imperial Decree", True),
    n("Security Precautions", True),
    n("The Phantom Menace"),
    n("Blaster Rack", True),
    n("Crush The Rebellion"),
    n("Gift Of The Master"),
    n("Imperial Propaganda", True),
    n("Where Are You Taking This... Thing?"),
    n("Knowledge And Defense", True),
    n("Force Push", True),
    n("They're Still Coming Through"),
    n("I Have You Now"),
    n("Sonic Bombardment", True, qty=3),
    n("Squabbling Delegates"),
    n("Cold Feet", True),
    n("Evader & Monnok"),
    n("Force Field", True, qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Sith Fury", True, qty=2),
    n("Force Lightning"),
    n("Prepared Defenses"),
    n("Cloud City: Security Tower", True),
    n("Geonosis: Separatist Council Room"),
    n("Naboo: Theed Palace Generator"),
    n("Geonosis"),
    n("Rally To Our Cause"),
    n("Separatist Uprising / At War With Itself"),
    n("Fanblade Starfighter", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("Dooku's Lightsaber"),
    n("Dark Jedi Lightsaber", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention"),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Firepower", True),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Abyss", True),
]
DS_ADD = []
