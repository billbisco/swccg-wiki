#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Vikram Bali.

Source: MPC-2014-Day-1-Main-Event.pdf pages 11–14 (typed two-column 60s).
Username blank.
"""
from __future__ import annotations

PLAYER = "Vikram Bali"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 13
DS_PAGE = 11
LS_SCAN = "2014 Match Play Championship Day 1 Vikram Bali LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Vikram Bali DS.png"
NOTE = "Typed leftover Xerox (two pages per side)."
LS_NOTE = (
    "Typed leftover Xerox p13–p14. Username blank. Don't Tread On Me! (V) dested "
    "Don't Tread On Me! (virtual-only, v=False). AFA (V) dested Anger, Fear, Aggression "
    "(V). Threepio WHPS dested Threepio With His Parts Showing. Gift of the Mentor dested "
    "Gift Of The Mentor. Han, Chewie and the Falcon dested Han, Chewie, And The Falcon. "
    "Speak with the Jedi Council dested Speak With The Jedi Council. Unique overcounts "
    "sheet-accurate (Qui-Gon Jinn With Lightsaber x2, Obi-Wan With Lightsaber x2, Lando "
    "Calrissian, Scoundrel x2, Imperial Atrocity (V) x2, A Jedi's Resilience x3, Let The "
    "Wookiee Win (V) x2, Rebel Leadership (V) x3, Wesa Gotta Grand Army x2, Escape Pod (V) "
    "x2). (V) from typed trailing V."
)
DS_NOTE = (
    "Typed leftover Xerox p11–p12. Username blank. HDADTJ/TFHGOOTU dested Hunt Down And "
    "Destroy The Jedi / Their Fire Has Gone Out Of The Universe. Knowledge & Defense (V) "
    "dested Knowledge And Defense (V) in the 60. Holotheater dested Holotheatre. Ni Chuba "
    "Na! (V) dested Ni Chuba Na?? (V). Gift of the Master dested Gift Of The Master. "
    "DLOTS dested Darth Vader, Dark Lord Of The Sith. BOTJ dested Darth Vader, Betrayer "
    "Of The Jedi. Darth Maul w/ Lightsaber dested Darth Maul With Lightsaber. 4-LOM w/ "
    "Concussion Rifle dested 4-LOM With Concussion Rifle. Galen's Lightsaber, Vader's Gift "
    "dested Galen's Lightsaber, Vader's Gift. Unique overcounts sheet-accurate (Darth "
    "Vader, Dark Lord Of The Sith x2, Emperor Palpatine x3, Darth Maul With Lightsaber x3, "
    "Galen Marek, Starkiller x3, Darth Sidious x2, Blizzard 4 x2, Maul's Sith Infiltrator "
    "x2, Visage Of The Emperor x3, I Have You Now x2, We Must Accelerate Our Plans x2, "
    "Sonic Bombardment (V) x2). (V) from typed trailing V."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Don't Tread On Me!"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Yavin 4: Massassi Throne Room"),
    n("Don't Tread On Me!"),
    n("Han, Chewie, And The Falcon"),
    n("Home One: War Room"),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Nar Shaddaa"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Draw Their Fire"),
    n("Mace Windu, Master Of The Order"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Luke With Lightsaber"),
    n("Luke Skywalker", True),
    n("Jaina Solo"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Dash Rendar", True),
    n("Corran Horn"),
    n("General Bel Iblis"),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Padme Naberrie", True),
    n("Leia, Rebel Princess"),
    n("Threepio With His Parts Showing"),
    n("Home One"),
    n("Tantive IV", True),
    n("Jedi Lightsaber", True),
    n("Seeking An Audience", True),
    n("Strikeforce", True),
    n("Scrambled Transmission", True),
    n("Mechanical Failure"),
    n("Mantellian Savrip"),
    n("Imperial Atrocity", True, qty=2),
    n("A Jedi's Resilience", qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=2),
    n("Speak With The Jedi Council"),
    n("Control & Tunnel Vision"),
    n("Impressive, Most Impressive", True),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Out Of Commission & Transmission Terminated"),
    n("Gift Of The Mentor"),
    n("Yub Yub Commander"),
    n("Corellian Retort", True),
    n("Hear Me Baby, Hold Together", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry"),
    n("He Can Go About His Business", True),
    n("Aim High"),
    n("Chasm"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("The Professor"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Weapons Display"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Holotheatre"),
    n("Executor: Meditation Chamber"),
    n("Visage Of The Emperor"),
    n("Prepared Defenses"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Conduct Your Search"),
    n("Crush The Rebellion"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Endor: Back Door"),
    n("Blast Door Controls"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Lord Vader"),
    n("Emperor Palpatine", qty=3),
    n("Darth Maul With Lightsaber", qty=3),
    n("Galen Marek, Starkiller", qty=3),
    n("Darth Sidious", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("4-LOM With Concussion Rifle", True),
    n("Blizzard 4", qty=2),
    n("Maul's Sith Infiltrator", qty=2),
    n("Vader's Lightsaber"),
    n("Sidious' Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Visage Of The Emperor", qty=2),
    n("The Phantom Menace"),
    n("Revenge Of The Sith"),
    n("Emperor's Power", True),
    n("Blaster Rack", True),
    n("Image Of The Dark Lord", True),
    n("Force Push", True),
    n("Maul Strikes"),
    n("I Have You Now", qty=2),
    n("Sith Fury & End This Destructive Conflict"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Sith Fury", True),
    n("Evader & Monnok"),
    n("Force Lightning"),
    n("Force Field", True),
]
DS_SHIELDS = [
    n("Leave Them To Me"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("Weapon Of A Sith"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Firepower", True),
    n("Secret Plans"),
    n("Abyss"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Imperial Detention"),
]
DS_ADD = []
