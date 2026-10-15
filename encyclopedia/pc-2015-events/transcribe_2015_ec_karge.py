#!/usr/bin/env python3
"""2015 European Championship Day 2: Moritz Karge (place 17).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p36 Dark / p37 Light typed 2002 PC forms.
"""
from __future__ import annotations

PLAYER = "Moritz Karge"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 37
DS_PAGE = 36
LS_SCAN = "2015 European Championship Moritz Karge LS.png"
DS_SCAN = "2015 European Championship Moritz Karge DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 17. Typed 2002 PC form (no username box). Player name Karge, Moritz. Event EC 2015 Day 2, date 15/10/17. "
    "Sheet deck titles: DS The Empire strikes out, LS A Game of Throne Room Mains. DS 3:1 / LS 1:3. "
    "(V) printed after card names, transcribed as v=True."
)
LS_NOTE = (
    "Starts Yavin 4: Massassi Throne Room (line 1), matches wiki. "
    "Posted Luke Skywalker (V) dested Luke Skywalker True. Posted Qui-Gon's Lightsaber dested Qui-Gon's Lightsaber as written. "
    "Main 60, shields 15 (3 shields in second column 13-15)."
)
DS_NOTE = (
    "Starts Combat Readiness (V) (line 2), matches wiki Combat Readiness (V). "
    "Posted Hoth: Ice Plains / 5th Marker dested Hoth: Ice Plains (5th Marker). "
    "Posted Hoth: Defensive Perimeter / 3rd Marker dested Hoth: Defensive Perimeter (3rd Marker). "
    "Posted Knowledge And Dense (V) dested Knowledge And Defense True. "
    "Main 60, shields 15 (3 shields in second column 13-15)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Sai'torr Kal Fas", True),
    n("Like My Father Before Me"),
    n("Luke's Lightsaber"),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Luke Skywalker", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Mace Windu's Lightsaber"),
    n("Mace Windu", True, qty=2),
    n("Qui-Gon's Lightsaber"),
    n("Master Qui-Gon", True, qty=3),
    n("Squadron Assignments"),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Azure Angel"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Red Squadron 1"),
    n("Obi-Wan In Radiant VII"),
    n("We Wish To Board At Once"),
    n("Civil Disorder", True),
    n("Draw Their Fire"),
    n("Honor Of The Jedi"),
    n("A Few Maneuvers"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Smoke Screen"),
    n("Escape Pod", True),
    n("Houjix"),
    n("Free Ride & Endor Celebration"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Hear Me Baby, Hold Together", True),
    n("Rebel Barrier"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Out Of Commission & Transmission Terminated"),
    n("Were You Looking For Me?"),
    n("Threepio With His Parts Showing"),
    n("Speak With The Jedi Council", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Wesa Gotta Grand Army", qty=4),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Jar Jar Binks"),
    n("Corran Horn"),
    n("Nar Shaddaa"),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Yoda, Keeper Of The Peace"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Weapons Display"),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Ounee Ta"),
    n("Goldenrod"),
    n("A Tragedy Has Occurred"),
    n("The Republic No Longer Functions"),
    n("Only Jedi Carry That Weapon"),
    n("He Can Go About His Business"),
    n("Ultimatum"),
    n("Aim High"),
    n("Don't Do That Again", True),
]
LS_ADD = []

DS_START = "Combat Readiness"
DS_CARDS = [
    n("Hoth"),
    n("Combat Readiness", True),
    n("Hoth: Ice Plains (5th Marker)"),
    n("Security Precautions"),
    n("Establish Control", True),
    n("You May Start Your Landing"),
    n("Fondor"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Walker Garrison", qty=2),
    n("Blizzard 1"),
    n("Blizzard 2", True),
    n("Trample"),
    n("Tempest 1"),
    n("Blizzard 4", qty=2),
    n("General Veers", True),
    n("General Nevar"),
    n("Commander Igar"),
    n("Grand Moff Tarkin", True, qty=2),
    n("Darth Vader", True),
    n("Grand Admiral Thrawn"),
    n("Captain Godherdt"),
    n("Admiral Motti", True),
    n("Admiral Piett"),
    n("We're In Attack Position Now", qty=2),
    n("Boba Fett, Bounty Hunter"),
    n("Darth Maul With Lightsaber"),
    n("U-3PO (Yoo-Threepio)"),
    n("Imperial Command", qty=3),
    n("We Must Accelerate Our Plans", qty=3),
    n("Blockade Flagship: Bridge"),
    n("Imperial Decree", True),
    n("Do They Have A Code Clearance?"),
    n("No Escape"),
    n("Lateral Damage"),
    n("Alert My Star Destroyer!"),
    n("Image Of The Dark Lord", True),
    n("Masterful Move & Endor Occupation"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Force Push", True, qty=2),
    n("Imperial Barrier"),
    n("Ommni Box & It's Worse"),
    n("Turn It Off! Turn It Off!", True, qty=2),
    n("Flagship Executor"),
    n("Conquest", True, qty=2),
    n("Devastator"),
    n("Zuckuss In Mist Hunter"),
    n("Maul's Sith Infiltrator"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Death Star Sentry"),
    n("Firepower"),
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Vote Of No Confidence"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Fanfare", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Resistance"),
    n("Imperial Detention"),
    n("There Is No Try"),
]
DS_ADD = []
