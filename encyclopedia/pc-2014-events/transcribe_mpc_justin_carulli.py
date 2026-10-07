#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Justin Carulli.

Source: MPC-2014-Day-1-Main-Event.pdf pages 27–28 (2013 form, 15 shields).
Username blank.
"""
from __future__ import annotations

PLAYER = "Justin Carulli"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 28
DS_PAGE = 27
LS_SCAN = "2014 Match Play Championship Day 1 Justin Carulli LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Justin Carulli DS.png"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. LIGHT checked. There Is Good In Him / I "
    "Can Save Him dested There Is Good In Him / I Can Save Him. Don't Tread On Me dested "
    "Don't Tread On Me!. SATM & Blast Prof dested Sorry About The Mess & Blaster "
    "Proficiency. Unique overcounts sheet-accurate (Rebel Leadership (V) x2, Let The "
    "Wookiee Win (V) x3, Qui-Gon Jinn With Lightsaber x2, Lando Calrissian, Scoundrel x2, "
    "Han With Heavy Blaster Pistol x2, Speak With The Jedi Council x2, Chewie, Enraged x2, "
    "Blaster Deflection x2, Rebel Barrier x2, A Jedi's Resilience x2, Dark Approach (V) "
    "x2, Sense x2, Wesa Gotta Grand Army x2, Obi-Wan With Lightsaber x2). Watto dested "
    "Watto as written (NO_DEST). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. DARK checked. Kessel line 1; Spice Mine "
    "Operations line 56 dested Spice Mine Operations. Gift of the Master dested Gift Of "
    "The Master. Galen, Secret Apprentice dested Galen Marek, Starkiller. The Mandalorian, "
    "Father of Fett dested Jango Fett, The Assassin. Galen's Lightsaber, Vader's Gift "
    "dested Galen's Lightsaber, Vader's Gift. Moruth Doole dested Moruth Doole, Kessel "
    "Administrator. Spice mine sites dested Kessel: Spice Mines - Administrator's Office "
    "/ Extraction Facility / Prison. Kessel Surveillance System dested Kessel "
    "(unique overcount). Unique overcounts sheet-accurate (Darth Maul With Lightsaber x2, "
    "Short Range Fighters & Watch Your Back! x4, Blizzard 4 x2, Force Field (V) x2, Sonic "
    "Bombardment (V) x3, Emperor Palpatine x3, Galen Marek, Starkiller x2, Dark Maneuvers "
    "x2, Force Lightning x2, Count Dooku x2, Kessel x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Anger, Fear, Aggression", True),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Endor: Landing Platform"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me!"),
    n("Rebel Leadership", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Draw Their Fire"),
    n("Let The Wookiee Win", True, qty=3),
    n("Escape Pod", True),
    n("Home One: War Room"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Admiral Ackbar", True),
    n("Home One"),
    n("Imperial Atrocity", True),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Chewie, Enraged", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Blaster Deflection", qty=2),
    n("Yavin 4: Massassi War Room", True),
    n("Rebel Barrier", qty=2),
    n("Grimtassh"),
    n("A Jedi's Resilience", qty=2),
    n("Leia, Rebel Princess"),
    n("Mechanical Failure"),
    n("Nabrun Leids"),
    n("Dark Approach", True, qty=2),
    n("Naboo: Battle Plains"),
    n("Watto"),  # Light as written (NO_DEST; Watto is Dark)
    n("Clash Of Sabers"),
    n("Houjix"),
    n("Corran Horn"),
    n("Naboo: Boss Nass' Chambers"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Coruscant: Jedi Council Chamber", True),
    n("Sense", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Anakin Skywalker, Padawan Learner"),
    n("Seeking An Audience", True),
    n("Mace Windu, Master Of The Order"),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Affect Mind", True),
    n("Aim High"),
    n("Battle Plan"),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
]
LS_ADD = []


DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Kessel"),
    n("Knowledge And Defense", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Combat Readiness", True),
    n("Gift Of The Master"),
    n("Something Special Planned For Them", True),
    n("Ni Chuba Na??", True),
    n("I'll Take Them Myself"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Dooku's Lightsaber"),
    n("Short Range Fighters & Watch Your Back!", qty=4),
    n("Blizzard 4", qty=2),
    n("Force Field", True, qty=2),
    n("Vader's Lightsaber"),
    n("Sonic Bombardment", True, qty=3),
    n("Emperor Palpatine", qty=3),
    n("Kessel: Spice Mines - Prison"),
    n("Lightsaber Deficiency", True),
    n("Slave I, Symbol Of Fear"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Stop Motion", True),
    n("Force Push", True),
    n("Blaster Rack", True),
    n("Moruth Doole, Kessel Administrator"),
    n("Boba Fett, Prepared Hunter"),
    n("Galen Marek, Starkiller", qty=2),
    n("Jango Fett, The Assassin"),
    n("Garindan", True),
    n("Dark Maneuvers", qty=2),
    n("Force Lightning", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Cloud City: Security Tower", True),
    n("Count Dooku", qty=2),
    n("Sniper & Dark Strike"),
    n("Kessel"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Arica"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Protocol Failure"),
    n("Spice Mine Operations"),
    n("Imperial Justice", True),
    n("Cold Feet", True),
    n("Maul's Sith Infiltrator"),
    n("Alter", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Firepower", True),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
