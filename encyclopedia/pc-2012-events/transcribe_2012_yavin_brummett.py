#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Ben Brummett.

Source: Yavin42012.pdf pages 23–24.
p23 Dark handwritten 2010 Xerox / p24 Light handwritten 2010 Xerox.
Name Ben Brummett dested Ben Brummett analog leftover generate_2012_mpc.py
CANON / player-stubs/Ben_Brummett.wiki / transcribe_2012_mpc_brummett.py.
Username blank. Pack player-stubs/Ben_Brummett.wiki.
Do not dest as a new person. Do not dest 2012 MPC Day 1 Ben Brummett 60s again.
"""
from __future__ import annotations

PLAYER = "Ben Brummett"
USERNAME = ""
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 24
DS_PAGE = 23
LS_SCAN = "2012 Yavin 4 Regionals Ben Brummett LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Ben Brummett DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p23 Dark handwritten 2010 Xerox / p24 Light handwritten 2010 Xerox. "
    "Name Ben Brummett dested Ben Brummett analog leftover generate_2012_mpc.py "
    "CANON / player-stubs/Ben_Brummett.wiki. Username blank. "
    "Event Date 6/30/12 Event Name Yavin 4 Regionals dest Yavin 4 facing pair analog leftover Orthner. "
    "Deck Name obj walkers / The I didn't know what to play deck dested off article. "
    "Do not dest as a new person. Do not dest 2012 MPC Day 1 Ben Brummett 60s again. "
    "Pack player-stubs/Ben_Brummett.wiki."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p24 Light. Name Ben Brummett Username blank. "
    "Event Date 6/30/12 Event Name Yavin 4 Regionals dest Yavin 4 facing pair. LIGHT checked. "
    "Local Uprising / Liberation dested analog leftover BTwigg True. "
    "Maneuvering Flaps + Trick Of The Trade dested Maneuvering Flaps & Trick Of The Trade analog leftover dest as written combo. "
    "Derek Hobbie Klivian dested Derek \"Hobbie\" Klivian analog leftover TYPE_OVERRIDE. "
    "General Callist Rieckan dested General Carlist Rieekan analog leftover dest as written slang. "
    "Rebel Trooper Recruit empty qty=2. Rebel Leadership True qty=2 lines 19/22 dest qty at first analog leftover non-consecutive. "
    "NOOOOO dested Noooooooooooo analog leftover Peterson True qty=2. "
    "Projection Of A Skywalker empty qty=2. Imperial Atrocity True qty=2. Escape Pod True qty=2. Rebel Artillery empty qty=2. "
    "Rebel Barrier empty lines 31/33 dest qty=2 at first analog leftover non-consecutive. "
    "Antilles Maneuver + Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements analog leftover Cooleo. "
    "Dash \"Rogue 10\" dested Dash Rendar In Rogue 10 analog leftover dest as written. "
    "Han Chewie + the Falcon dested Han, Chewie, And The Falcon analog leftover Amato. "
    "Gold Leader in Gold 1 dested Gold Leader In Gold 1 analog leftover Bali. "
    "Obi Wan in Radiant VII dested Obi-Wan In Radiant VII analog leftover dest as written. "
    "Hoth: Echo Command War Room dested Hoth: Echo Command Center (War Room) analog leftover Amato. "
    "Hoth: Main Generators dested Hoth: Main Power Generators analog leftover Rambo. "
    "Hoth: 3rd Marker dested Hoth: Defensive Perimeter analog leftover Anderson. "
    "Hoth: 2nd Marker dested Hoth: Echo Docking Bay analog leftover Swedal. "
    "Hoth: 4th Marker dested Hoth: North Ridge analog leftover dest as written. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Westergard. "
    "Shields 1–11 filled shield 12 empty skip analog leftover Dwyer. Unique 60 shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p23 Dark. Name Ben Brummett Username blank. "
    "Event Date 6/30/12 Event Name Yavin 4 Regionals dest Yavin 4 facing pair. DARK checked. "
    "Imperial Occupation / Imp dested Imperial Occupation / Imperial Control True analog leftover Anderson. "
    "Knowledge And Defense True dested analog leftover Anderson IN THE 60. "
    "Tempest 1 dested Tempest Scout 1 analog leftover Mike. "
    "Line 14 crossed dest Podracer Collision analog leftover crossed-with-replacement empty qty=2 lines 14/26 dest qty at first. "
    "AT-At Canon dested AT-AT Cannon analog leftover dest as written slang. "
    "Control + Set For Stun dested Control & Set For Stun analog leftover Westergard. "
    "Do They Have A Code Clearance dested analog leftover Anderson IN THE 60. "
    "Stop Motion True lines 13/36 dest qty=2 at first analog leftover non-consecutive. "
    "Imperial Artillery empty lines 31/40 dest qty=2 at first. "
    "Imperial Command empty lines 27/52 dest qty=2 at first. "
    "Executer dested Executor analog leftover dest as written slang. "
    "Veers dested General Veers analog leftover Westergard. "
    "Hoth: 3rd Marker dested Hoth: Defensive Perimeter analog leftover Anderson. "
    "Captain Gilad Palleon dested Captain Gilad Pellaeon analog leftover dest as written slang. "
    "Blizzard Scont 1 dested Blizzard Scout 1 analog leftover dest as written slang. "
    "The Mandalorian, Father Of Fett dested Jango Fett, The Assassin analog leftover Nieland. "
    "We Must Accelerate Our Plans empty qty=2. "
    "Shields 1–11 filled shield 12 empty skip analog leftover Dwyer. Unique 60 shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Local Uprising / Liberation"
LS_CARDS = [
    n("Local Uprising / Liberation", True),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Strike Planning"),
    n("Rebel Gunrunner", True),
    n("Maneuvering Flaps & Trick Of The Trade", True),
    n("Echo Base Garrison"),
    n("Planet Defender Ion Cannon", True),
    n("Dual Laser Cannon", True),
    n("Derek \"Hobbie\" Klivian", True),
    n("Commander Luke Skywalker", True),
    n("General Carlist Rieekan", True),
    n("Zev Senesca"),
    n("Commander Wedge Antilles", True),
    n("Corran Horn"),
    n("Rebel Trooper Recruit", qty=2),
    n("Haven"),
    n("Rebel Leadership", True, qty=2),
    n("Noooooooooooo", True, qty=2),
    n("Projection Of A Skywalker", qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("Rebel Artillery", qty=2),
    n("Rebel Barrier", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("T-47 Battle Formation"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Lone Rogue"),
    n("Rendezvous Point"),
    n("Desperate Tactics"),
    n("Rogue 4"),
    n("Rogue 3"),
    n("Dash Rendar In Rogue 10", True),
    n("Rogue 2"),
    n("Rogue 1"),
    n("Han, Chewie, And The Falcon"),
    n("Gold Leader In Gold 1"),
    n("Tantive IV", True),
    n("Obi-Wan In Radiant VII"),
    n("Liberty"),
    n("Spiral"),
    n("Bright Hope", True),
    n("Frostbite", True),
    n("Hoth: Echo Command Center (War Room)", True),
    n("Hoth: Main Power Generators"),
    n("Echo Base Sensors"),
    n("Hoth"),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Echo Docking Bay"),
    n("Hoth: North Ridge"),
    n("Lando Calrissian, Scoundrel"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Another Pathetic Lifeform", True),
    n("Traffic Control", True),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("The Professor", True),
    n("Aim High"),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Knowledge And Defense", True),
    n("Prepared Defenses"),
    n("You May Start Your Landing"),
    n("Prepare For A Surface Attack"),
    n("Endor Shield", True),
    n("Hoth: Main Power Generators"),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Imperial Decree"),
    n("Tempest Scout 1"),
    n("Cold Feet", True),
    n("Stop Motion", True, qty=2),
    n("Podracer Collision", qty=2),
    n("Close Call", True),
    n("AT-AT Cannon", True),
    n("Imperial Barrier"),
    n("Control & Set For Stun"),
    n("Walker Garrison"),
    n("Target The Main Generator"),
    n("Do They Have A Code Clearance?"),
    n("Why Didn't You Tell Me", True),
    n("Hoth: Mountains"),
    n("A Dark Time For The Rebellion", True),
    n("Trample"),
    n("Imperial Command", qty=2),
    n("Crash Landing"),
    n("Grand Moff Tarkin", True),
    n("Furry Fury"),
    n("Imperial Artillery", qty=2),
    n("Executor"),
    n("Hoth Blockade", True),
    n("Blizzard 4"),
    n("He Hasn't Come Back Yet"),
    n("General Veers", True),
    n("General Nevar", True),
    n("Marquand In Blizzard 6", True),
    n("Masterful Move"),
    n("Imperial Propaganda", True),
    n("Victory", True),
    n("Hoth: Defensive Perimeter"),
    n("Commander Igar"),
    n("Captain Gilad Pellaeon"),
    n("Blizzard 1", True),
    n("Desperate Counter", True),
    n("Blizzard Scout 1", True),
    n("Grand Admiral Thrawn"),
    n("Alert My Star Destroyer"),
    n("The Emperor's Reach", True),
    n("Blizzard 2"),
    n("Slave I, Symbol Of Fear", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("Sonic Bombardment", True),
    n("We Must Accelerate Our Plans", qty=2),
]
DS_SHIELDS = [
    n("No Escape"),
    n("A Useless Gesture", True),
    n("Reactor Terminal", True),
    n("Death Star Sentry", True),
    n("Resistance", True),
    n("Fanfare"),
    n("Secret Plans", True),
    n("Battle Order", True),
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("Come Here You Big Coward"),
]
DS_ADD = []
