#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Reid Smith.

Source: MPC-2014-Day-1-Main-Event.pdf pages 102–103 (2013 form, 15 shields).
Name RSmith dested Reid Smith. Username blank.
"""
from __future__ import annotations

PLAYER = "Reid Smith"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 102
DS_PAGE = 103
LS_SCAN = "2014 Match Play Championship Day 1 Reid Smith LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Reid Smith DS.png"
LS_DECK_NAME = "yrr"
DS_DECK_NAME = "KC SO"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name RSmith dested Reid Smith. Username blank. LIGHT checked. "
    "Deck name yrr. There Is Good In Him / I Can Save You dested There Is Good In Him / I Can Save Him. "
    "Endor Chief Chirpa Hut dested Endor: Chief Chirpa's Hut. Unique overcounts sheet-accurate "
    "(Chewie, Enraged x2, Qui-Gon Jinn With Lightsaber x2, Obi-Wan With Lightsaber x2, "
    "Han With Heavy Blaster Pistol x2, Let The Wookiee Win (V) x3, Rebel Barrier x2, "
    "Blaster Deflection x2, Sense x2, A Jedi's Resilience x2, Speak With The Jedi Council x2, "
    "Dark Approach (V) x2, Rebel Leadership (V) x2, Lando Calrissian, Scoundrel x2, "
    "Wesa Gotta Grand Army x3). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name RSmith dested Reid Smith. Username blank. DARK checked. "
    "Deck name KC SO. The Mandalorian Father Of Fett dested Jango Fett, The Assassin. "
    "Slave I, Symbol Of Fear dested Slave I, Symbol Of Fear. Short Range Fighters & Watch Your Back "
    "dested Short Range Fighters & Watch Your Back!. Galen Secret Apprentice dested "
    "Galen Marek, Starkiller. Unique overcounts sheet-accurate (Force Lightning x2, Count Dooku x2, "
    "Sonic Bombardment (V) x3, Dark Maneuvers x2, Short Range Fighters & Watch Your Back! x3, "
    "Darth Maul With Lightsaber x2, Blizzard 4 x2, Galen Marek, Starkiller x2, Emperor Palpatine x3, "
    "Force Field (V) x2, Force Push (V) x2). NO_DEST Spice Mine Administrator. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Imperial Atrocity", True),
    n("Grimtaash"),
    n("Mechanical Failure"),
    n("Chewie, Enraged", qty=2),
    n("Naboo: Battle Plains"),
    n("Mace Windu, Master Of The Order"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Naboo: Boss Nass' Chambers"),
    n("Tarfful, Wookiee Insurgent"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Admiral Ackbar", True),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Rebel Barrier", qty=2),
    n("Blaster Deflection", qty=2),
    n("Sense", qty=2),
    n("Anakin Skywalker, Padawan Learner"),
    n("Home One"),
    n("Corran Horn"),
    n("Coruscant: Jedi Council Chamber", True),
    n("A Jedi's Resilience", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Dark Approach", True, qty=2),
    n("Home One: War Room"),
    n("Rebel Leadership", True, qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Houjix"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Seeking An Audience", True),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Escape Pod", True),
    n("Clash Of Sabers"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Jedi Knight"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("He Can Go About His Business", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("Ultimatum", True),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
]
LS_ADD = []


DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("I'll Take Them Myself"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Force Lightning", qty=2),
    n("Blaster Rack", True),
    n("Vader's Lightsaber"),
    n("Sniper & Dark Strike"),
    n("Spice Mine Operations"),
    n("Count Dooku", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Garindan", True),
    n("Slave I, Symbol Of Fear"),
    n("Stop Motion", True),
    n("Cloud City: Security Tower", True),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Dark Maneuvers", qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Maul's Sith Infiltrator"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Blizzard 4", qty=2),
    n("Cold Feet", True),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Dooku's Lightsaber"),
    n("Something Special Planned For Them", True),
    n("Galen Marek, Starkiller", qty=2),
    n("Emperor Palpatine", qty=3),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Force Field", True, qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Force Push", True, qty=2),
    n("Protocol Failure"),
    n("Lightsaber Deficiency", True),
    n("Alter", True),
    n("Kessel: Spice Mines - Prison"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Spice Mine Administrator"),
    n("Arica"),
    n("Kessel Surveillance System"),
    n("Black Sun Fleet"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("Battle Order", True),
    n("Come Here You Big Coward", True),
    n("Do They Have A Code Clearance", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("There Is No Try", True),
    n("Resistance", True),
    n("Secret Plans"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
