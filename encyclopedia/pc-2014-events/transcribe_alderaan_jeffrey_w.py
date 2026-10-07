#!/usr/bin/env python3
"""2014 Alderaan Regionals Xerox: Jeffrey W (Istagrem).

Source: 2014-Alderaan-Regionals.pdf pages 17–18 (2013 Print Form).
Name Jeffrey W dested as written. Username Istagrem. Do not invent a last name.
"""
from __future__ import annotations

PLAYER = "Jeffrey W"
USERNAME = "Istagrem"
STAGE = ""
PDF = "2014 Alderaan Regionals.pdf"
LS_PAGE = 17
DS_PAGE = 18
LS_SCAN = "2014 Alderaan Regionals p17 Jeffrey W LS.png"
DS_SCAN = "2014 Alderaan Regionals p18 Jeffrey W DS.png"
NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Jeffrey W dested as written. Username Istagrem. Email [redacted]. "
    "LS no objective; START dested Hoth from line 1. Careful Planning is the starting interrupt. "
    "DS Endor Operations dested Endor Operations / Imperial Outpost. "
    "Anger, Fear Aggression dested Anger, Fear, Aggression. "
    "Hoth: Echo Med Lab dested Hoth: Echo Med Lab. "
    "Corporal Monk dested as written (NO_DEST). "
    "Commander Marajik dested as written (NO_DEST). "
    "Commander Marajik, Pride Of The Empire dested as written (NO_DEST). "
    "Pondo/Panda dested Fondor. "
    "Gold Squadron Y-wing dested Gold Squadron Y-Wing. "
    "WED-9-M1 Bantha Droid dested WED-9-M1 'Bantha' Droid. "
    "Galen Marek Starkiller dested Galen Marek, Starkiller. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back!. "
    "We'll Let Fate-a Decide Huh? dested We'll Let Fate-a Decide, Huh?. "
    "I Can't Shake Him dested I Can't Shake Him!. "
    "(V) from the checkbox. Unique overcounts sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hoth"
LS_CARDS = [
    n("Hoth"),
    n("Careful Planning", True),
    n("Hoth: Main Power Generators"),
    n("Hoth: North Ridge"),
    n("A New Secret Base"),
    n("Strike Planning"),
    n("Rebel Gunrunner", True),
    n("Dual Laser Cannon", True),
    n("Anger, Fear, Aggression", True),
    n("Commander Luke Skywalker", True),
    n("Mon Mothma"),
    n("Biggs, Rogue Legend", True),
    n("Zev Senesca"),
    n("Echo Base Sensors"),
    n("Spiral"),
    n("Mon Calamari Star Cruiser", True),
    n("Gray Squadron Y-wing Pilot"),
    n("Commander Narra", True),
    n("Spiral"),
    n("Han With Heavy Blaster Pistol"),
    n("Dack Ralter"),
    n("Echo Base Garrison"),
    n("Incom Engineer"),
    n("Chandrila"),
    n("Red 3"),
    n("Gold Leader In Gold 1"),
    n("Corulag"),
    n("Hoth: Echo Docking Bay"),
    n("General Carlist Rieekan"),
    n("Hoth: Echo Command Center"),
    n("Hoth: Echo Med Lab"),
    n("Derek 'Hobbie' Klivian", True),
    n("Rogue 1"),
    n("Mon Calamari"),
    n("Echo Base Trooper"),
    n("Organized Attack"),
    n("Echo Base Operations"),
    n("Gold Squadron Y-Wing"),
    n("A Few Maneuvers"),
    n("Veteran Rogue", True),
    n("Rogue 2"),
    n("Wes Janson", True),
    n("Planet Defender Ion Cannon", True),
    n("Commander Wedge Antilles"),
    n("Snowspeeder Garrison", True),
    n("Tantive IV"),
    n("Rogue 4"),
    n("Rogue 3"),
    n("Corellian Corvette"),
    n("Veteran Rogue", True),
    n("Liberty"),
    n("WED-9-M1 'Bantha' Droid"),
    n("Red Squadron 4"),
    n("Toryn Farr"),
    n("Star Destroyer!"),
    n("Red 2"),
    n("Red 5"),
    n("Desperate Tactics"),
    n("Haven"),
    n("Red 6"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Ultimatum", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Planetary Defenses", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Don't Do That Again"),
    n("Wise Advice"),
]
LS_ADD = []


DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform"),
    n("Prepared Defenses"),
    n("TIE Fighter Construction Facility", True),
    n("Crossfire", True),
    n("Combat Response", True),
    n("Knowledge And Defense", True),
    n("Galen Marek, Starkiller", True),
    n("Victory-Class Star Destroyer"),
    n("Black 1", True),
    n("Juno Eclipse, Black Leader", True),
    n("TIE Avenger", True),
    n("Commander Marajik"),
    n("Executor"),
    n("Ominous Rumors"),
    n("Establish Secret Base", True),
    n("Endor Shield", True),
    n("Onyx 2", True),
    n("Speeder Bike"),
    n("Corporal Monk"),
    n("Sergeant Barich"),
    n("Speeder Bike"),
    n("Imperial Pilot", True),
    n("Tatooine"),
    n("Corulag"),
    n("Vader's Custom TIE"),
    n("Tempest Scout 6"),
    n("Tempest Scout 4"),
    n("Grand Moff Tarkin"),
    n("Imperial Pilot", True),
    n("Operational As Planned"),
    n("Scythe Squadron TIE"),
    n("TIE Defender Mark I"),
    n("All Power To Weapons"),
    n("I Can't Shake Him!"),
    n("Commander Marajik, Pride Of The Empire"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Stormtrooper Garrison"),
    n("Trample"),
    n("TIE Avenger", True),
    n("The Empire's Back"),
    n("Aratech Corporation", True),
    n("Kessel"),
    n("Battle Deployment"),
    n("The Emperor's Shield"),
    n("Blizzard 2", True),
    n("Admiral Piett"),
    n("Endor Occupation"),
    n("Dark Maneuvers"),
    n("Scythe Squadron TIE"),
    n("Black Squadron TIE"),
    n("Watch Your Back!"),
    n("General Nevar", True),
    n("Darth Vader"),
    n("Rendili"),
    n("Fondor"),
    n("Victory-Class Star Destroyer"),
    n("Grand Admiral Thrawn"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Resistance", True),
    n("Wipe Them Out, All Of Them", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("Imperial Detention", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?"),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
]
DS_ADD = []
