#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Justin Carulli.

Source: Nationals-2014-day-1.pdf pages 21–22 (2010 form).
Name Justin Carulli.
"""
from __future__ import annotations

PLAYER = "Justin Carulli"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 21
DS_PAGE = 22
LS_SCAN = "2014 US Nationals Day 1 p21 Justin Carulli LS.png"
DS_SCAN = "2014 US Nationals Day 1 p22 Justin Carulli DS.png"
NOTE = "Handwritten 2010 Xerox. Name Justin Carulli."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Justin Carulli. Username blank. "
    "TIGIH dested There Is Good In Him / I Can Save Him. "
    "Endor: Chirpa's Hut dested Endor: Chief Chirpa's Hut. Endor: DB dested Endor: Landing Platform (Docking Bay). "
    "Luke Skywalker, Rebel Scout dested Luke Skywalker, Rebel Scout. SATM/BP dested Sorry About The Mess & Blaster Proficiency. "
    "Anakin Padawan dested Anakin Skywalker, Padawan Learner. Leia RP dested Leia, Rebel Princess. "
    "A Jedi's Resilience dested A Jedi's Resilience. Hoth: War Room dested Hoth: Echo Command Center (War Room). "
    "Hoth: DB dested Hoth: Echo Docking Bay. Line 51 Corran dested Corran Horn. "
    "Unique overcounts sheet-accurate "
    "(Rebel Barrier x2, Sense x2, Let The Wookiee Win x3, Rebel Leadership x2, "
    "Speak With The Jedi Council x2, Wesa Gotta Grand Army x2, Blaster Deflection x2, "
    "Chewie, Enraged x2, Obi-Wan With Lightsaber x2, Dark Approach x2, "
    "Qui-Gon Jinn With Lightsaber x2, Lando Calrissian, Scoundrel x2, "
    "Han With Heavy Blaster Pistol x2, A Jedi's Resilience x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Justin Carulli. Username blank. "
    "Force Unleashed dested The Force Unleashed. K+D dested Knowledge And Defense. "
    "Gift of the Master dested Gift Of The Master. Ni Chuba Na dested Ni Chuba Na??. "
    "Short Range Combo dested Short Range Fighters & Watch Your Back!. "
    "Galen's Saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Slave I, SOF dested Slave I, Symbol Of Fear. Galen dested Galen Marek, Starkiller. "
    "BF Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Mandalorian FOF dested Jango Fett, The Assassin. Emp New Order dested Empire's New Order. "
    "Unique overcounts sheet-accurate (Force Push x2, Force Lightning x2, Sense x2, "
    "Force Field x2, Short Range Fighters & Watch Your Back! x3, Sonic Bombardment x3, "
    "Emperor Palpatine x3, Dooku x2, Galen Marek, Starkiller x2, EPP Maul x2). (V) from checkbox. "
    "NO_DEST (2014 index): Kessel: Spice Mines Administration; Cloud City: Prison (V); "
    "Kessel: Extraction; Kessel: Spice Mines; Kessel System."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Anger, Fear, Aggression", True),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Rebel Barrier", qty=2),
    n("Sense", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Let The Wookiee Win", True, qty=3),
    n("Rebel Leadership", True, qty=2),
    n("Grimtaash"),
    n("Clash Of Sabers"),
    n("A Jedi's Resilience"),
    n("Speak With The Jedi Council", qty=2),
    n("Escape Pod", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("Blaster Deflection", qty=2),
    n("Houjix"),
    n("Nabrun Leids"),
    n("Dark Approach", True, qty=2),
    n("Seeking An Audience", True),
    n("Mechanical Failure"),
    n("Imperial Atrocity", True),
    n("Draw Their Fire"),
    n("Naboo: Battle Plains"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Hoth: Echo Docking Bay"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Chewie, Enraged", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Tarfful, Wookiee Insurgent"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Corran Horn"),
    n("Mace Windu, Master Of The Order"),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Admiral Ackbar"),
    n("Luke Skywalker, Jedi Knight"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Leia, Rebel Princess"),
    n("A Jedi's Resilience"),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here"),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("He Can Go About His Business"),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense", True),
    n("Battle Plan"),
    n("The Professor"),
    n("Ultimatum"),
    n("Chasm", True),
]
LS_ADD = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Weapons Display"),
]


DS_START = "The Force Unleashed"
DS_CARDS = [
    n("The Force Unleashed"),
    n("Knowledge And Defense", True),
    n("Kessel: Spice Mines Administration"),
    n("Combat Readiness", True),
    n("I'll Take Them Myself"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Dark Maneuvers", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Force Push", True, qty=2),
    n("Force Lightning", qty=2),
    n("Monnok"),
    n("Ghhhk"),
    n("Alter", True),
    n("Sense", True),
    n("Sense"),
    n("Sniper & Dark Strike"),
    n("Cold Feet", True),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Force Field", True, qty=2),
    n("Blaster Rack", True),
    n("Force Pike", True),
    n("Cloud City: Prison", True),
    n("Kessel: Extraction"),
    n("Kessel: Spice Mines"),
    n("Spice Mine Operations"),
    n("Kessel System"),
    n("Dooku's Lightsaber"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Black Sun Fleet"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Blizzard 4"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Arica"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Mara Jade, The Emperor's Hand"),
    n("Galen Marek, Starkiller", qty=2),
    n("Count Dooku", qty=2),
    n("Emperor Palpatine", qty=3),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("Empire's New Order", True),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Firepower", True),
    n("Imperial Detention"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Weapon Of A Sith"),
    n("Do They Have A Code Clearance?"),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = [
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever"),
]
