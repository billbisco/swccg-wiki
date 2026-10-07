#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Mike Richards.

Source: MPC-2014-Day-1-Main-Event.pdf pages 90–91 (2013 form, 15 shields).
Name Michael Richards dested Mike Richards. Username woofagent.
"""
from __future__ import annotations

PLAYER = "Mike Richards"
USERNAME = "woofagent"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 90
DS_PAGE = 91
LS_SCAN = "2014 Match Play Championship Day 1 Mike Richards LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Mike Richards DS.png"
LS_DECK_NAME = "Communing"
DS_DECK_NAME = "Double D's"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Michael Richards dested Mike Richards. Username woofagent. "
    "LIGHT checked. Deck name Communing. Tatooine Slave Quarters dested Tatooine: Slave Quarters "
    "(starting location). Communing dested Communing. Master Kenobi dested Master Kenobi. "
    "Threepio Parts Showing dested Threepio With His Parts Showing. Lando's Luxury Yacht dested "
    "Lady Luck. All My Urchins dested All My Urchins & Cloud City Celebration. "
    "Nar Shaddaa Wind Chimes dested Nar Shaddaa Wind Chimes. Unique overcounts sheet-accurate "
    "(Padme Naberrie x2, Luke Skywalker (V) x2, Baragwin x2, Fire Extinguisher x5, Use The Force (V) x2, "
    "Rebel Leadership (V) x4, Either Way, You Win (V) x2, Let The Wookiee Win (V) x2). "
    "(V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Michael Richards dested Mike Richards. Username woofagent. "
    "DARK checked (LIGHT crossed). Deck name Double D's. Invasion dested Invasion / In Complete Control. "
    "Where Are The Droidekas dested Where Are Those Droidekas?!. At last we are getting results dested "
    "At Last We Are Getting Results. Rolling Rolling x3 dested Rolling, Rolling, Rolling qty=3 on one line. "
    "Master Destroyers dested Masterful Move & Endor Occupation analog Master Destroyers. "
    "The Mandalorian Father of Fett dested Jango Fett, The Assassin. 3P0 & Artoo dested "
    "See-Threepio & Artoo-Detoo. Unique overcounts sheet-accurate (P-60 x2, Destroyer Droid x9, "
    "Imperial Barrier x2, Master Destroyers x2, Guri x2, P-59 x2, We Must Accelerate Our Plans x2). "
    "Rolling, Rolling, Rolling x3 on one line sheet-accurate. NO_DEST Master Destroyers; See-Threepio & Artoo-Detoo (V). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Tatooine"),
    n("Tatooine: City Outskirts"),
    n("Home One: War Room"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Master Kenobi", True),
    n("Wokling", True),
    n("Communing", True),
    n("Cell 2187", True),
    n("Padme Naberrie", True, qty=2),
    n("Luke Skywalker", True, qty=2),
    n("Han With Heavy Blaster Pistol"),
    n("Admiral Ackbar", True),
    n("First Officer Thaneespi"),
    n("Leia, Rebel Princess"),
    n("Yoda, Great Warrior", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Threepio With His Parts Showing"),
    n("Figrin D'an"),
    n("Shmi Skywalker"),
    n("Harc Seff"),
    n("Baragwin", qty=2),
    n("Artoo-Detoo In Red 5", True),
    n("Home One"),
    n("Fire Extinguisher", qty=5),
    n("Use The Force", True, qty=2),
    n("Escape Pod", True),
    n("Rebel Leadership", True, qty=4),
    n("Droid Shutdown"),
    n("Seeking An Audience", True),
    n("Imperial Atrocity", True),
    n("All My Urchins & Cloud City Celebration"),
    n("Dash Rendar", True),
    n("Lady Luck", True),
    n("Senator Leia Organa", True),
    n("Nar Shaddaa Wind Chimes", True),
    n("Luke's Bionic Hand", True),
    n("Either Way, You Win", True, qty=2),
    n("Control & Tunnel Vision"),
    n("Inconsequential Barriers"),
    n("Houjix"),
    n("Anakin Skywalker", True),
    n("Launching The Assault"),
    n("Let The Wookiee Win", True, qty=2),
    n("Droid Shutdown"),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Do, Or Do Not"),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Aim High"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here"),
    n("Affect Mind", True),
    n("Chasm", True),
    n("Ultimatum"),
]
LS_ADD = []


DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Naboo: Swamp"),
    n("Naboo"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Throne Room"),
    n("Blockade Flagship"),
    n("Where Are Those Droidekas?!", True),
    n("At Last We Are Getting Results", True),
    n("Droid Racks", True),
    n("Crossfire"),
    n("Blockade Support Ship", True),
    n("Masterful Move & Endor Occupation"),
    n("You Cannot Hide Forever"),
    n("P-60", qty=2),
    n("Self-Destruct Mechanism"),
    n("Maul's Sith Infiltrator"),
    n("Rolling, Rolling, Rolling", qty=3),
    n("Oh, Switch Off"),
    n("Darth Maul"),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("P-13 & P-14"),
    n("Destroyer Droid", qty=9),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Master Destroyers", qty=2),
    n("Elis Helrot"),
    n("Imperial Barrier", qty=2),
    n("P-59", qty=2),
    n("Naboo: Battle Plains"),
    n("See-Threepio & Artoo-Detoo", True),
    n("Tey How"),
    n("Outflank", True),
    n("Those Rebels Won't Escape Us", True),
    n("Guri", qty=2),
    n("Stinger", True),
    n("Prepared Defenses"),
    n("Forced Servitude"),
    n("Daultay Dofine", True),
    n("Sniper & Dark Strike"),
    n("Jango Fett, The Assassin", True),
    n("Blockade Flagship: Bridge"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Blockade Support Ship"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Resistance"),
    n("Abyss", True),
    n("Do They Have A Code Clearance", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Fanfare", True),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Restricted Access", True),
]
DS_ADD = []
