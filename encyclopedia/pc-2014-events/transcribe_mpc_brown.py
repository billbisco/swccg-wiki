#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Keith Brown.

Source: MPC-2014-Day-1-Main-Event.pdf pages 25–26 (2013 form, 15 shields).
Username djk11.
"""
from __future__ import annotations

PLAYER = "Keith Brown"
USERNAME = "djk11"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 25
DS_PAGE = 26
LS_SCAN = "2014 Match Play Championship Day 1 Keith Brown LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Keith Brown DS.png"
LS_DECK_NAME = "Sorry About the Mess"
DS_DECK_NAME = "Here Goes Nothing"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username djk11. LIGHT checked. Deck Sorry About the Mess. "
    "Republic At War / Aggressive Neg dested Republic At War / Aggressive Negotiations. "
    "Begin The Clone War Has dested Begun, The Clone War Has. HFTMF dested Heading For "
    "The Medical Frigate. Alderaan Consular Ship dested Radiant VII. Accelerator-Class "
    "Assault Ship dested Accelerator-Class Assault Ship as written (NO_DEST). Unique "
    "overcounts sheet-accurate (Dual Laser Cannon (V) x5, "
    "Accelerator-Class Assault Ship (V) x2, "
    "AT-RT (V) x10, All Wings Report In & Darklighter Spin x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username djk11. DARK checked. Deck Here Goes Nothing. "
    "Separatist Uprising / At War dested Separatist Uprising / At War With Itself. War "
    "Has Begun dested Begun, The Clone War Has (NO_DEST Dark). Gift of the Master dested Gift Of The "
    "Master. They're Still Coming dested They're Still Coming Through!. Where Are You "
    "Taking This Thing? dested Where Are You Taking This ... Thing?. "
    "Jango Fett, The Assassin dested Jango Fett, The Assassin. Grievous, Hunter of Jedi "
    "dested Grievous, Hunter Of Jedi. Slave I Symbol of Fear dested Slave I, Symbol Of "
    "Fear. SRF & WYB dested Short Range Fighters & Watch Your Back!. K+D dested Knowledge "
    "And Defense. Geonosis: Conference Room dested Geonosis: Conference Room as written "
    "(NO_DEST). Firespray-31 dested Firespray-31 as written (NO_DEST). Unique overcounts "
    "sheet-accurate (Firespray-31 (V) x2, Darth Maul With "
    "Lightsaber x2, Count Dooku (V) x2, Darth Sidious x2, Force Field (V) x2, Squabbling "
    "Delegates x2, Sonic Bombardment (V) x3). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Republic At War / Aggressive Negotiations"
LS_CARDS = [
    n("Republic At War / Aggressive Negotiations", True),
    n("Begun, The Clone War Has", True),
    n("Geonosis: Forward Command Center", True),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Nick Of Time", True),
    n("Rogue Squadron Tactics", True),
    n("Muunilinst: City Of Harnaidan", True),
    n("Muunilinst: Harnaidan Plains", True),
    n("Muunilinst: Docking Bay", True),
    n("Muunilinst: Republic Landing Site", True),
    n("Dressel", True),
    n("Assault On Muunilinst", True),
    n("Dual Laser Cannon", True, qty=5),
    n("Lady Luck", True),
    n("Radiant VII", True),
    n("Accelerator-Class Assault Ship", True, qty=2),
    n("Azure Angel", True),
    n("AT-RT", True, qty=10),
    n("Phylo Gandish", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Plo Koon", True),
    n("Anakin Solo", True),
    n("Jaina Solo", True),
    n("Obi-Wan Kenobi", True),
    n("Anakin Skywalker, Padawan Learner", True),
    n("Seeking An Audience", True),
    n("Projection Of A Skywalker"),
    n("Crash Site Memorial", True),
    n("Imperial Atrocity", True),
    n("Sabotage", True),
    n("Houjix"),
    n("Sorry About The Mess"),
    n("Rebel Barrier"),
    n("Rebel Artillery"),
    n("Lucky Shot", True),
    n("Desperate Tactics"),
    n("Escape Pod", True),
    n("It's Not My Fault", True),
    n("Dark Approach", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Away Put Your Weapon", True),
    n("Weapon Levitation"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Battle Plan"),
    n("The Professor", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Weapons Display", True),
    n("Do, Or Do Not"),
    n("Affect Mind", True),
    n("Wise Advice"),
    n("He Can Go About His Business", True),
]
LS_ADD = []


DS_START = "Separatist Uprising / At War With Itself"
DS_CARDS = [
    n("Separatist Uprising / At War With Itself", True),
    n("Begun, The Clone War Has", True),
    n("Geonosis: Conference Room", True),
    n("Prepared Defenses"),
    n("Crush The Rebellion"),
    n("You Cannot Hide Forever"),
    n("Gift Of The Master", True),
    n("Geonosis", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Cloud City: Security Tower", True),
    n("Rally To Our Cause", True),
    n("Boba Fett, Bounty Hunter"),
    n("Firespray-31", True, qty=2),
    n("Slave I, Symbol Of Fear", True),
    n("Dark Jedi Lightsaber", True),
    n("Dooku's Lightsaber", True),
    n("Probe Droid", True),
    n("Garindan", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("Grievous, Hunter Of Jedi", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Count Dooku", True, qty=2),
    n("Darth Sidious", qty=2),
    n("Nute Gunray", True),
    n("Baskol Yeesrim"),
    n("Aks Moe"),
    n("Tikkes"),
    n("Edcel Bar Gane"),
    n("Yeb Yeb Adem'thorn"),
    n("Orn Free Taa"),
    n("Lott Dod"),
    n("Imperial Decree", True),
    n("Security Precautions", True),
    n("Imperial Propaganda", True),
    n("Something Special Planned For Them", True),
    n("Blaster Rack", True),
    n("The Phantom Menace", True),
    n("Where Are You Taking This ... Thing?", True),
    n("Force Push", True),
    n("Evader & Monnok"),
    n("They're Still Coming Through!"),
    n("Force Lightning"),
    n("Cold Feet", True),
    n("I Have You Now"),
    n("Sith Fury"),
    n("Sith Fury & End This Destructive Conflict"),
    n("Force Field", True, qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Squabbling Delegates", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Imperial Detention", True),
    n("Death Star Sentry", True),
    n("Weapon Of A Sith"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Secret Plans"),
    n("Abyss", True),
    n("There Is No Try"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Resistance"),
]
DS_ADD = []
