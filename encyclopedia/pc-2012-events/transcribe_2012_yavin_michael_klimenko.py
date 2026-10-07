#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Michael Klimenko.

Source: Yavin42012.pdf pages 31–32.
p31 Dark typed 2010 Xerox / p32 Light typed 2010 Xerox.
Name Michael Klimenko dested Michael Klimenko analog leftover dest as written.
Username blank. Pack player-stubs/Michael_Klimenko.wiki.
Do not dest as Alex Klimenko. Do not dest Yavin p18–p22 Alex Klimenko 60s again.
"""
from __future__ import annotations

PLAYER = "Michael Klimenko"
USERNAME = ""
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 32
DS_PAGE = 31
LS_SCAN = "2012 Yavin 4 Regionals Michael Klimenko LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Michael Klimenko DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p31 Dark typed 2010 Xerox / p32 Light typed 2010 Xerox. "
    "Name Michael Klimenko dested Michael Klimenko analog leftover dest as written. "
    "Username blank. Event Date 06/30/12 Event Name Yavin 4 Regional dest Yavin 4 facing pair analog leftover Orthner. "
    "Deck Name Big Blue/Big Explosion / Hoth Defense/Speeder Zoom Zoom dested off article. "
    "Do not dest as Alex Klimenko. Pack player-stubs/Michael_Klimenko.wiki."
)
LS_NOTE = (
    "Typed 2010 Xerox p32 Light. Name Michael Klimenko Username blank. "
    "Event Date 06/30/12 Event Name Yavin 4 Regional dest Yavin 4 facing pair. LIGHT checked. "
    "Local Uprising/Liberation dested Local Uprising / Liberation True analog leftover Brummett. "
    "Hoth North Ridge dested Hoth: North Ridge analog leftover dest as written. "
    "Hoth Main Power Generators dested Hoth: Main Power Generators analog leftover dest as written. "
    "Hoth Echo Command Center dested Hoth: Echo Command Center (War Room) analog leftover dest as written Amato. "
    "Derek Hobbie Klivian dested Derek \"Hobbie\" Klivian analog leftover TYPE_OVERRIDE. "
    "Dual Laser Cannon True qty=2 analog leftover consecutive. "
    "Hoth Snow Trench dested Hoth: Snow Trench analog leftover dest as written. "
    "Hoth Defensive Perimeter dested Hoth: Defensive Perimeter analog leftover dest as written. "
    "Eject Eject/Imperial Atrocity dested Eject! Eject! & Imperial Atrocity analog leftover TYPE_OVERRIDE. "
    "Rebel Barrier empty qty=2 analog leftover consecutive. "
    "It Could Be Worse empty qty=2 analog leftover consecutive. "
    "The Bith Shuffle/Desperate Reach dested The Bith Shuffle & Desperate Reach analog leftover dest as written combo qty=2. "
    "Antilles Maneuver/Rebel Reinforments dested Antilles Maneuver & Rebel Reinforcements analog leftover dest as written combo Cooleo. "
    "Out Of Commission/Transmission Terminated dested analog leftover dest as written combo. "
    "Capitol Support dested Capital Support analog leftover dest as written slang. "
    "Only Jedi Carry That Weapon dested Only Jedi Carry That Kind Of Firepower analog leftover dest as written slang. "
    "Your Insights Serves You Well dested Your Insights Serve You Well analog leftover dest as written slang. "
    "Shields 1–9 filled 10–12 empty skip analog leftover Dwyer. Unique 60 shields 9."
)
DS_NOTE = (
    "Typed 2010 Xerox p31 Dark. Name Michael Klimenko Username blank. "
    "Event Date 06/30/12 Event Name Yavin 4 Regional dest Yavin 4 facing pair. DARK checked. "
    "Set Your Course For Alderaan dested analog leftover dest as written empty. "
    "Death Star Docking Bay 327 dested Death Star: Docking Bay 327 analog leftover Nelson. "
    "Tarkin dested Grand Moff Tarkin analog leftover dest as written slang. "
    "Death Star Gunner True qty=2 analog leftover consecutive. "
    "Boba Fett Bounty Hunter dested Boba Fett, Bounty Hunter analog leftover dest as written. "
    "Visage dested Visage Of The Emperor analog leftover dest as written slang. "
    "Tarkin Doctrine dested Tarkin's Doctrine analog leftover TYPE_OVERRIDE. "
    "Twilek Advisor dested Twi'lek Advisor analog leftover dest as written slang. "
    "Dr. Evazan and Ponda Baba dested Dr. Evazan & Ponda Baba analog leftover dest as written combo. "
    "Its Worse dested It's Worse analog leftover dest as written slang. "
    "Sense/Uncertain Is The Future dested Sense & Uncertain Is The Future analog leftover dest as written combo. "
    "Death Star War Room dested Death Star: War Room analog leftover dest as written. "
    "He Is Not Ready/Imperial Propaganda dested He Is Not Ready & Imperial Propaganda analog leftover dest as written combo. "
    "Ghhhk / Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us analog leftover dest as written combo. "
    "Death Star Central Core dested Death Star: Central Core analog leftover dest as written. "
    "Captain Gilad Pellaon dested Captain Gilad Pellaeon analog leftover dest as written slang. "
    "Put All Sections On Alert empty lines 34/47 dest qty=2 at first analog leftover non-consecutive. "
    "Imperial Barrier empty lines 24/56 dest qty=2 at first analog leftover non-consecutive. "
    "Deflector Shield Generators True lines 25/60 dest qty=2 at first analog leftover non-consecutive. "
    "Come Here You Big Cowerd dested Come Here You Big Coward analog leftover dest as written slang. "
    "Shields 1–6 filled 7–12 empty skip analog leftover Dwyer. Unique 60 shields 6."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Local Uprising / Liberation"
LS_CARDS = [
    n("Local Uprising / Liberation", True),
    n("Hoth"),
    n("Hoth: North Ridge"),
    n("Hoth: Main Power Generators", True),
    n("Heading For The Medical Frigate"),
    n("Echo Base Garrison"),
    n("Menace Fades"),
    n("Strike Planning"),
    n("An Unusual Amount Of Fear"),
    n("General Carlist Rieekan", True),
    n("Hoth: Echo Command Center (War Room)"),
    n("Spiral"),
    n("Tantive IV", True),
    n("Booster's Star Destroyer"),
    n("Redemption", True),
    n("Rogue 4"),
    n("Derek \"Hobbie\" Klivian"),
    n("Snowspeeder Garrison"),
    n("Dual Laser Cannon", True, qty=2),
    n("Power Harpoon"),
    n("Haven"),
    n("Hoth: Snow Trench"),
    n("Hoth: Defensive Perimeter"),
    n("T-47 Battle Formation"),
    n("Eject! Eject! & Imperial Atrocity", True),
    n("Commander Wedge Antilles"),
    n("Rebel Barrier", qty=2),
    n("It Could Be Worse", qty=2),
    n("Captain Antilles", True),
    n("Commander Luke Skywalker", True),
    n("Dash Rendar", True),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("General Calrissian"),
    n("Planet Defender Ion Cannon", True),
    n("Rogue 2"),
    n("Rebel Artillery"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Corran Horn"),
    n("Massanya"),
    n("Out Of Commission & Transmission Terminated"),
    n("Bright Hope", True),
    n("Capital Support"),
    n("Liberty"),
    n("Mon Calamari Star Cruiser", True),
    n("Rogue 3"),
    n("Toryn Farr", True),
    n("Frostbite", True),
    n("Tigran Jamiro", True),
    n("Desperate Tactics"),
    n("Rogue 1"),
    n("Escape Pod", True),
    n("Quite A Mercenary"),
    n("Rapid Fire"),
    n("Zev Senesca"),
    n("Houjix"),
    n("Changing The Odds", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Kind Of Firepower"),
    n("Don't Do That Again"),
    n("Your Insights Serve You Well"),
    n("Ultimatum"),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Weapons Display"),
    n("Chasm"),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan"
DS_CARDS = [
    n("Set Your Course For Alderaan"),
    n("Death Star: Docking Bay 327"),
    n("Death Star"),
    n("Alderaan"),
    n("Prepared Defenses"),
    n("Kuat Drive Yards", True),
    n("Alert My Star Destroyer", True),
    n("A Million Voices Crying Out"),
    n("Fear Is My Ally"),
    n("We're In Attack Position Now"),
    n("Imperial Decree"),
    n("Grand Moff Tarkin", True),
    n("Death Star Gunner", True, qty=2),
    n("Fondor"),
    n("Hoth"),
    n("Yavin 4"),
    n("Boba Fett, Bounty Hunter", True),
    n("Admiral Chiraneau"),
    n("Visage Of The Emperor"),
    n("Grand Admiral Thrawn"),
    n("Darth Vader With Lightsaber"),
    n("Tarkin's Doctrine", True),
    n("Imperial Barrier", qty=2),
    n("Deflector Shield Generators", True, qty=2),
    n("Twi'lek Advisor"),
    n("Captain Lennox", True),
    n("Mara Jade With Lightsaber", True),
    n("Superlaser"),
    n("Accuser"),
    n("Commence Primary Ignition", True),
    n("Vengeance"),
    n("Admiral Motti, Battlestation Coordinator", True),
    n("Put All Sections On Alert", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("It's Worse"),
    n("U-3PO"),
    n("Masterful Move"),
    n("Thunderflare"),
    n("Projective Telepathy"),
    n("Sense & Uncertain Is The Future"),
    n("Death Star: War Room", True),
    n("Executor"),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Imperial Command"),
    n("Kashyyyk"),
    n("Death Star: Central Core", True),
    n("Corulag"),
    n("Avenger"),
    n("Admiral Piett"),
    n("Chimaera"),
    n("Devastator", True),
    n("Sacrifice"),
    n("Captain Gilad Pellaeon"),
    n("Tyrant"),
    n("Officer Evax"),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
]
DS_ADD = []
