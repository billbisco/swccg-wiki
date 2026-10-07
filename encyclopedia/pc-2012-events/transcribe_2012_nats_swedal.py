#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Nick Swedal.

Source: 2012NationalsDay1.pdf pages 74–75 (handwritten 2010 Xerox, shields blank).
p74 Dark / p75 Light Name Nick Swedal Username blank dested Nick Swedal analog leftover
pages/Nick_Swedal.wiki. Pack pages/Nick_Swedal.wiki. Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Nick Swedal"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 75
DS_PAGE = 74
LS_SCAN = "2012 US Nationals Day 1 Nick Swedal LS.png"
DS_SCAN = "2012 US Nationals Day 1 Nick Swedal DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Nick Swedal dested Nick Swedal analog leftover pages/Nick_Swedal.wiki. "
    "Username blank. Event Date blank Event Name blank consecutive Day 1. Do not dest as a new person."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Nick Swedal dested Nick Swedal analog leftover pages/Nick_Swedal.wiki. "
    "Username blank. LIGHT checked. Event Date blank Event Name blank consecutive Day 1. "
    "LS_START Local Uprising / Liberation True analog leftover Jellison. "
    "Hoth System dested Hoth analog leftover Scott. "
    "Hangar Bays dested Hangar Bay analog leftover dest-as-written slang. "
    "Evacuation Control True analog leftover Alex W. "
    "A New Secret Base dested analog leftover Haglund. "
    "Line 13 The Signal x2 crossed dest The Signal once. Line 17 crossed Hoth dests replacement The Signal. "
    "Echo Base Sensors dested Echo Base Sensors analog leftover dest-as-written slang. "
    "Echo Base War Room dested Hoth: Echo Command Center (War Room) analog leftover Amato. "
    "Echo Base Docking Bay dested Hoth: Echo Docking Bay analog leftover Schoenthal. "
    "Sergeant Helis dested Sergeant Irlane analog leftover dest-as-written slang. "
    "Ducta Tank dested Tauntaun analog leftover dest-as-written slang. "
    "Control / Tunnel Vision dested Control & Tunnel Vision analog leftover Buck. "
    "Dual Laser Cannons dested Dual Laser Cannon True analog leftover Herold. "
    "Nice Of You Guys To Drop By dested analog leftover dest-as-written slang. "
    "Line 60 Maneuvering Flaps crossed dests replacement Don't Get Cocky True analog leftover Chu. "
    "Heroic Sacrifice x3 unique overcount. Ice Storm x2. The Signal x2. Mon Calamari Star Cruiser True x2. "
    "Attack Pattern Delta True x2. Shields blank skip. Unique 60. Shields 0."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Nick Swedal dested Nick Swedal analog leftover pages/Nick_Swedal.wiki. "
    "Username blank. DARK checked. Event Date blank Event Name blank consecutive Day 1. "
    "DS_START Endor Operations / Imperial Outpost analog leftover Dubreuil. "
    "Death Star 2 System dested Death Star II analog leftover. "
    "Imperial Arrest Order & Secret Plans dested analog leftover Bordier. "
    "Fondor System dested Fondor analog leftover Burgt. "
    "Tatooine System dested Tatooine analog leftover. "
    "Sullust System dested Sullust analog leftover. "
    "YCHF + Mob Points dested You Cannot Hide Forever & Mobilization Points analog leftover Mack. "
    "Twilek Advisor dested Twi'lek Advisor analog leftover. "
    "SSPT dested Something Special Planned For Them analog leftover Fernando. "
    "SFS L-S7.2 TIE Cannon dested analog leftover dest-as-written slang x2. "
    "It Worse dested It's Worse analog leftover Erwin. "
    "Tractor Beam x3 unique overcount. Imperial Barrier x3. Lateral Damage x2. "
    "They've Shut Down The Main Reactor x2. TIE Interceptor x2. Flawless Marksmanship x2. "
    "Victory-Class Star Destroyer x2. Shields blank skip. Unique 60. Shields 0."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Local Uprising / Liberation"
LS_CARDS = [
    n("Local Uprising / Liberation", True),
    n("Hoth"),
    n("Hoth: North Ridge"),
    n("Heading For The Medical Frigate"),
    n("Hangar Bay"),
    n("Nick Of Time"),
    n("Echo Base Garrison"),
    n("Maneuvering Flaps"),
    n("Insurrection"),
    n("Hoth: Main Power Generators"),
    n("Evacuation Control", True),
    n("A New Secret Base"),
    n("The Signal", qty=2),
    n("Hoth: Echo Corridor"),
    n("Echo Base Sensors"),
    n("Mon Calamari Star Cruiser", True, qty=2),
    n("Hoth Sentry"),
    n("Desperate Tactics"),
    n("General McQuarrie"),
    n("Snowspeeder Garrison", True),
    n("Electrobinoculars"),
    n("Rogue 1"),
    n("Power Harpoon"),
    n("Heroic Sacrifice", qty=3),
    n("Sergeant Irlane"),
    n("Commander Wedge Antilles"),
    n("Rogue 3"),
    n("Redemption", True),
    n("Projection Of A Skywalker"),
    n("Ice Storm", qty=2),
    n("Frostbite", True),
    n("Control & Tunnel Vision"),
    n("Admiral Ackbar", True),
    n("Jedi Presence"),
    n("Zev Senesca"),
    n("Rogue 2"),
    n("Dual Laser Cannon", True),
    n("T-47 Battle Formation"),
    n("Rapid Fire"),
    n("Slight Weapons Malfunction"),
    n("Liberty"),
    n("Attack Pattern Delta", True, qty=2),
    n("Derek 'Hobbie' Klivian"),
    n("Rogue 4"),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Echo Docking Bay"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Tauntaun"),
    n("Commander Luke Skywalker", True),
    n("Hoth: Snow Trench"),
    n("Houjix"),
    n("Narrow Escape"),
    n("Nice Of You Guys To Drop By"),
    n("Don't Get Cocky", True),
]
LS_SHIELDS = []
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Operational As Planned"),
    n("Desperate Counter"),
    n("Death Star II"),
    n("Endor: Landing Platform"),
    n("Endor: Bunker"),
    n("Tractor Beam", qty=3),
    n("Inconsequential Losses"),
    n("Imperial Arrest Order & Secret Plans"),
    n("TIE Interceptor", qty=2),
    n("Fondor"),
    n("Tatooine"),
    n("Flawless Marksmanship", qty=2),
    n("Chimaera"),
    n("Lateral Damage", qty=2),
    n("Limited Resources"),
    n("Imperial Barrier", qty=3),
    n("In Range"),
    n("Dengar In Punishing One"),
    n("Warrant Officer M'Kae"),
    n("You Cannot Hide Forever & Mobilization Points"),
    n("They've Shut Down The Main Reactor", qty=2),
    n("Endor Shield", True),
    n("Devastator", True),
    n("Twi'lek Advisor"),
    n("Darth Vader With Lightsaber"),
    n("Tyrant"),
    n("Gravity Shadow"),
    n("Admiral Piett"),
    n("That Thing's Operational"),
    n("Victory-Class Star Destroyer", qty=2),
    n("SFS L-S7.2 TIE Cannon", qty=2),
    n("Flagship Executor"),
    n("Something Special Planned For Them"),
    n("No Escape"),
    n("Commander Merrejk"),
    n("Sullust"),
    n("Death Star II: Coolant Shaft"),
    n("Death Star II: Capacitors"),
    n("Admiral Chiraneau"),
    n("Kashyyyk"),
    n("Death Star II: Docking Bay"),
    n("Grand Moff Tarkin"),
    n("Moff Jerjerrod"),
    n("Death Star II: Reactor Core"),
    n("Grand Admiral Thrawn"),
    n("Kessel"),
    n("Our First Catch Of The Day"),
    n("It's Worse"),
    n("Imperial-Class Star Destroyer", True),
]
DS_SHIELDS = []
DS_ADD = []
