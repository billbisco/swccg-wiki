#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Ben Brummett.

Source: 2012mpcday1.pdf pages 55–56 (2010 form, 12 shields).
Name Ben Brummett dested Ben Brummett. Username blank.
p55 Light TRM Podracing. p56 Dark SYCFA.
Analog grep encyclopedia + player-stubs + generate_*.py returned no Brummett matches.
Dest as written. Pack a new player stub.
"""
from __future__ import annotations

PLAYER = "Ben Brummett"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 55
DS_PAGE = 56
LS_SCAN = "2012 Match Play Championship Day 1 Ben Brummett LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Ben Brummett DS.png"
LS_DECK_NAME = "TRM Podracing"
DS_DECK_NAME = "SYCFA"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Ben Brummett. Username blank. LIGHT checked. "
    "Deck Name TRM Podracing. Event MPC Date 2/11/12. Email [redacted]. "
    "Dest as written. Analog grep returned no prior stub. "
    "Yavin 4 Massassi Throne Room dested Yavin 4: Massassi Throne Room. "
    "Podracer Prep dested Podrace Prep. "
    "I did it dested I Did It!. Sai'torr Kal Fas dested Sai'torr Kal Fas True. "
    "Coruscant Jedi Council Chamber dested Coruscant: Jedi Council Chamber. "
    "Naboo battle plains dested Naboo: Battle Plains. "
    "Naboo Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Home One War Room dested Home One: War Room. "
    "Leia Rebel Princess dested Leia, Rebel Princess. Leia dested Leia True. "
    "Luke Skywalker Strong in the Force dested Luke Skywalker, Strong In The Force True x2. "
    "Yoda Master of the Force dested Yoda, Master Of The Force x2. "
    "Qui-Gon Jinn with lightsaber dested Qui-Gon Jinn With Lightsaber. "
    "Threepio With His Parts Showing dested Threepio With His Parts Showing. "
    "Control and Tunnel Vision dested Control & Tunnel Vision. "
    "Hanjix dested Odin Nesloor & First Aid. "
    "Sorry about the mess & blaster proficiency dested Sorry About The Mess & Blaster Proficiency x2. "
    "Speak with the Jedi Council dested Speak With The Jedi Council x2. "
    "Wesa Gotta Grand Army dested Wesa Gotta Grand Army x2. "
    "Were you looking for me dested Were You Looking For Me?. "
    "NOOOOOOOOOOOO! dested NOOOOOOOOOOOO! True. "
    "Hear me baby, Hold Together dested Hear Me Baby, Hold Together True. "
    "Form 59 Rebel Artillery crossed dest Impressive, Most Impressive True. "
    "Anger, Fear, Aggression dested Anger, Fear, Aggression True. "
    "Unique 60. Shield 12 blank. Additional empty. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Ben Brummett. Username blank. DARK checked. "
    "Deck Name SYCFA. Event MPC Date 2/11/12. Email [redacted]. "
    "Dest as written. Analog grep returned no prior stub. "
    "Set Your Course For Alderaan dested Set Your Course For Alderaan / "
    "The Ultimate Power In The Universe. "
    "Death Star Dockingbay dested Death Star: Docking Bay 327. "
    "Super laser dested Superlaser. "
    "Line 11 CPI plus fury fury dested Commence Primary Ignition True and Sith Fury True "
    "(two titles on one numbered line; True checkbox). "
    "Line 12 Intensify The Forward Batteries crossed with no replacement skipped. "
    "Judiator dested Judicator. Dengar in Punishing One dested Dengar In Punishing One. "
    "Darth Vader DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Why didn't you tell me dested Why Didn't You Tell Me? True x2. "
    "We Must Accelerate Our Plans dested We Must Accelerate Our Plans x2. "
    "Knowledge + Defense dested Knowledge And Defense True. "
    "Unique 60. Shield 12 blank. Additional empty. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Podrace Prep"),
    n("Quick Draw", True),
    n("Tatooine: Podrace Arena"),
    n("Boonta Eve Podrace"),
    n("Anakin's Podracer"),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("I Did It!"),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Battle Plains"),
    n("Malastare"),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Jedi Lightsaber", qty=2),
    n("Luke's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Mace Windu", True, qty=2),
    n("Leia, Rebel Princess"),
    n("Leia", True),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Yoda, Master Of The Force", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Corran Horn"),
    n("Captain Verrack", True),
    n("Admiral Ackbar", True),
    n("Threepio With His Parts Showing"),
    n("Control & Tunnel Vision"),
    n("Odin Nesloor & First Aid"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Sense"),
    n("A Jedi's Resilience", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Blaster Deflection", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Were You Looking For Me?"),
    n("NOOOOOOOOOOOO!", True),
    n("Under Attack", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Escape Pod", True),
    n("Rebel Artillery"),
    n("Impressive, Most Impressive", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Another Pathetic Lifeform", True),
    n("Traffic Control", True),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense", True),
    n("Chasm", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Don't Do That Again"),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Prepared Defenses"),
    n("A Million Voices Crying Out"),
    n("Kuat Drive Yards", True),
    n("Imperial Stockpile", True),
    n("Alderaan"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Superlaser"),
    n("Laser Cannon Battery"),
    n("Commence Primary Ignition", True),
    n("Sith Fury", True),
    n("The Phantom Menace"),
    n("Imperial Propaganda", True),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Rendili"),
    n("Nal Hutta"),
    n("Corulag"),
    n("Fondor"),
    n("Visage"),
    n("Judicator"),
    n("Dengar In Punishing One"),
    n("Chimaera"),
    n("Conquest", True),
    n("Thunderflare"),
    n("Devastator"),
    n("Executor"),
    n("Darth Sidious"),
    n("Emperor Palpatine", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("P-59"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Admiral Motti", True),
    n("Why Didn't You Tell Me?", True, qty=2),
    n("TIE Sentry Ships", True, qty=2),
    n("Force Field", True),
    n("Force Lightning"),
    n("Force Push", True),
    n("Relentless Pursuit", qty=2),
    n("Defensive Fire", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("Cold Feet", True),
    n("Sense", qty=2),
    n("Stop Motion"),
    n("Imperial Barrier", qty=2),
    n("Imperial Command", qty=2),
    n("Podracer Collision", qty=2),
    n("Grand Admiral Thrawn"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Death Star Sentry"),
    n("No Escape"),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Fanfare"),
    n("Reactor Terminal", True),
    n("Come Here You Big Coward", True),
    n("Resistance", True),
    n("Secret Plans", True),
    n("Battle Order", True),
    n("Allegations Of Corruption"),
]
DS_ADD = []
