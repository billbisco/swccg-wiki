#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Amar Banger.

Source: 2012mpcday1.pdf pages 45–46 (typed Dropbox HTML print, 12 shields).
Name Amar Banger dested Amar Banger. Username blank (no Username box).
p45 Light TRM / Anger, Fear, Aggression. p46 Dark HD(V) / Hunt Down (V).
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Amar Banger"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 45
DS_PAGE = 46
LS_SCAN = "2012 Match Play Championship Day 1 Amar Banger LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Amar Banger DS.png"
LS_DECK_NAME = "TRM"
DS_DECK_NAME = "HD(V)"
NOTE = "Typed Dropbox HTML print form."
LS_NOTE = (
    "Typed leftover Xerox p45. Name Amar Banger dested Amar Banger. "
    "Username blank (2002 DECK LIST print; do not copy abanger from 2013). "
    "Event MPC 2012. LIGHT SIDE checked. Deck Title TRM. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Anger, Fear, Aggression (V4) dested Anger, Fear, Aggression True. "
    "Don't Tread On Me (V1) dested Don't Tread On Me True (virtual-only). "
    "Luke Skywalker, Strong In The Force (V6) dested Luke Skywalker, Strong In The Force True x3. "
    "NOOOOOOOOOOOO! (V2) dested NOOOOOOOOOOOO! True. "
    "Speak With The Jedi Council dested Speak With The Jedi Council. "
    "Sorry About The Mess & Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency x2. "
    "LS_START Anger, Fear, Aggression. Unique 60. (V) from typed (Vn)."
)
DS_NOTE = (
    "Typed leftover Xerox p46. Name Amar Banger dested Amar Banger. "
    "Username blank. Event MPC 2012. DARK SIDE checked. Deck Title HD(V). "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Hunt Down And Destroy The Jedi/Their Fire Has Gone Out Of The Universe (V4) dested "
    "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe True. "
    "Cyborg Commander, Hunter Of Jedi dested Grievous, Hunter Of Jedi True x2. "
    "Galen, Secret Apprentice dested as written True x3. "
    "Ni Chuba Na?? dested Ni Chuba Na?? True. "
    "Boba Fett In Slave I dested Boba Fett In Slave I True. "
    "We'll Let Fate-a Decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "Unique 60. (V) from typed (Vn)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Don't Tread On Me", True),
    n("Yavin 4: Massassi Throne Room"),
    n("A Jedi's Resilience", qty=2),
    n("Admiral Ackbar", True),
    n("Artoo-Detoo In Red 5"),
    n("Blaster Deflection", qty=2),
    n("Corran Horn"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Draw Their Fire"),
    n("Han, Chewie, And The Falcon"),
    n("Hear Me Baby, Hold Together", True),
    n("Home One"),
    n("Home One: War Room"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Imperial Atrocity", True),
    n("Jedi Lightsaber", True),
    n("Kiffex"),
    n("Lando Calrissian, Scoundrel"),
    n("Leia's Blaster Rifle"),
    n("Leia, Rebel Princess", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Luke's Lightsaber"),
    n("Mace Windu", True, qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("NOOOOOOOOOOOO!", True),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Obi-Wan With Lightsaber"),
    n("Padmé Naberrie", True),
    n("Qui-Gon's Lightsaber"),
    n("Quick Draw", True),
    n("Rebel Leadership", True, qty=3),
    n("Sai'torr Kal Fas", True),
    n("Scrambled Transmission", True),
    n("Seeking An Audience", True),
    n("Sense", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Speak With The Jedi Council"),
    n("Strikeforce", True),
    n("Tantive IV", True),
    n("Threepio With His Parts Showing"),
    n("Under Attack"),
    n("Were You Looking For Me?"),
    n("Wesa Gotta Grand Army", qty=2),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense", True),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("A Sith's Plans", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Endor Shield", True),
    n("Gift Of The Master", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Knowledge And Defense", True),
    n("Ni Chuba Na??", True),
    n("Prepared Defenses", True),
    n("4-LOM With Concussion Rifle", True),
    n("A Sith's Weapon", True),
    n("Battle Droid Squad", True),
    n("Blaster Rack", True),
    n("Blockade Flagship: Bridge"),
    n("Boba Fett In Slave I", True),
    n("ComScan Detection", True),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Dark Jedi Lightsaber", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Death Star: War Room", True),
    n("Disarmed"),
    n("Dr. Evazan & Ponda Baba"),
    n("Emperor Palpatine", qty=2),
    n("Endor"),
    n("First Strike"),
    n("Force Field", True, qty=2),
    n("Force Lightning"),
    n("Force Push", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Galen, Secret Apprentice", True, qty=3),
    n("General Nevar", True),
    n("Ghhhk"),
    n("Grand Admiral Thrawn"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Mara Jade With Lightsaber", True),
    n("Masterful Move & Endor Occupation"),
    n("Myn Kyneugh", True),
    n("Naboo: Theed Palace Generator Core"),
    n("No Escape"),
    n("Protocol Failure", True),
    n("Revenge Of The Sith", True),
    n("Sense & Uncertain Is The Future"),
    n("Sniper & Dark Strike"),
    n("Something Special Planned For Them", True),
    n("Tarkin's Bounty", True),
    n("Vader's Lightsaber"),
    n("Victory", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Zuckuss In Mist Hunter"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
