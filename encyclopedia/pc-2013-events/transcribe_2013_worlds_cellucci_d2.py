#!/usr/bin/env python3
"""2013 World Championship Day 2: Stephen Cellucci informal DS + Same as Yesterday LS."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from transcribe_2013_worlds_cellucci import (  # noqa: E402
    LS_ADD,
    LS_CARDS,
    LS_SHIELDS,
    LS_START,
    n,
)

PLAYER = "Stephen Cellucci"
USERNAME = "Nolimit"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 25
DS_PAGE = 25
LS_SCAN = "2013 Worlds Day 2 p25 Stephen Cellucci DS.png"
DS_SCAN = "2013 Worlds Day 2 p25 Stephen Cellucci DS.png"
LS_EXTRA_SCANS = [
    (
        "2013 Worlds Day 1 p01 Stephen Cellucci LS.png",
        "Page 1 of [[:File:2013 Worlds Day 1.pdf]].",
    )
]
LS_PUBLIC_NOTE = (
    "Day 2 Light is the same as the Day 1 Plead My Case To The Senate list."
)
LS_NOTE = (
    "Day 2 informal overlay headed LS: same as yesterday. Username Nolimit. "
    "The 60 is copied from Day 1 page 1."
)
DS_NOTE = (
    "Informal typed overlay, not a 2010 Xerox Print Form. "
    "Stephen Cellucci DS Decklist. Username Nolimit. Worlds Day 2. "
    "Endor ops dested Endor Operations / Imperial Outpost. "
    "Breached defenses and molator dested Breached Defenses & Molator. "
    "Short range fighters and watch your back dested "
    "Short Range Fighters & Watch Your Back!. "
    "Corporal misik dested Corporal Misik. "
    "Endor: Landing platform dested Endor: Landing Platform (Docking Bay). "
    "Vader's Custom TIE struck dested Vader's Personal Shuttle. "
    "Black leader dested Juno Eclipse, Black Leader. "
    "Baron soontir fel dested Baron Soontir Fel. "
    "Fighters Coming In dested Fighters Coming In. "
    "15 defensive-shield slots on this overlay. "
    "LS: same as yesterday written at the foot of this Dark sheet."
)

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Establish Control", True),
    n("Endor Shield", True),
    n("Prepared Defenses"),
    n("Blast Points", qty=2),
    n("Imperial Stockpile"),
    n("Scout Blaster"),
    n("Compact Firepower", qty=2),
    n("Cold Feet", True),
    n("Dark Maneuvers"),
    n("Sergeant Elsek", qty=2),
    n("Aratech Corporation", True),
    n("Breached Defenses & Molator"),
    n("Perimeter Patrol"),
    n("Ominous Rumors", True),
    n("Establish Secret Base", True),
    n("Endor: Bunker"),
    n("Admiral Ozzel"),
    n("Saber 2"),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Corporal Drelosyn"),
    n("Why Didn't You Tell Me?", True),
    n("Imperial Barrier"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Security Precautions", True),
    n("Protocol Failure"),
    n("Speeder Bike", qty=3),
    n("Endor: Landing Platform"),
    n("Corporal Misik"),
    n("Sergeant Barich"),
    n("Sergeant Irol"),
    n("Grand Moff Tarkin", True),
    n("Navy Trooper Fenson"),
    n("Endor: Forest Clearing"),
    n("General Tagge", True),
    n("Fondor"),
    n("Vader's Personal Shuttle", True),
    n("Combat Response", True),
    n("Juno Eclipse, Black Leader"),
    n("Stormtrooper Garrison"),
    n("Imperial Domination", True),
    n("Baron Soontir Fel"),
    n("Darth Vader", True),
    n("Garindan", True),
    n("Black 2", True),
    n("Black 1"),
    n("Saber 1"),
    n("Knowledge And Defense", True),
    n("Major Turr Phennir"),
    n("Fighters Coming In"),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Secret Plans"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("Imperial Detention"),
    n("Fanfare", True),
    n("Resistance"),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = [
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("A Useless Gesture"),
]
