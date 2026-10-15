#!/usr/bin/env python3
"""2015 European Championship Day 2: Julian Smolarek (place 23).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p13 DS / p14 LS handwritten 2014-format deck list forms.
"""
from __future__ import annotations

PLAYER = "Julian Smolarek"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 14
DS_PAGE = 13
LS_SCAN = "2015 European Championship Julian Smolarek LS.png"
DS_SCAN = "2015 European Championship Julian Smolarek DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 23 circled. Forms signed 'Julian-Andrés Smolarek', username blank, event European Championship 2015, no date. "
    "DS deck name 'Bring Him Before Me', DS 2:2. LS deck name 'There Is Good In Him', LS 1:3."
)
LS_NOTE = (
    "Form 60 lines + 15 shields, one copy per line. "
    "TITLE MISMATCH: wiki says This Is Getting Out Of Hand, sheet starts There Is Good In Him / I Can Save Him. "
    "Posted Endor: Chief Chirpa's Hut, Endor: Landing Platform (Docking Bay) dested Endor: Chief Chirpa's Hut, Endor: Landing Platform. "
    "Posted Free Ride / Endor Celebration dested Free Ride & Endor Celebration. "
    "Posted Out Of Commission / Transmission Terminated dested Out Of Commission & Transmission Terminated. "
    "Posted Sorry About The Mess / Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "Posted A Tragedy Has Occured dested A Tragedy Has Occurred."
)
DS_NOTE = (
    "Form 60 lines + 15 shields, one copy per line. "
    "Posted Bring Him Before Me / Take Your Father's Place dested as dual title. "
    "Posted Hoth: Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Posted Masterful Move / Endor Occupation dested Masterful Move & Endor Occupation. "
    "Posted Woof dested Wooof."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Endor: Landing Platform"),
    n("I Feel The Conflict"),
    n("Heading For The Medical Frigate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Corran Horn"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Jedi Knight"),
    n("Mace Windu", True, qty=2),
    n("Master Qui-Gon", True, qty=3),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Threepio With His Parts Showing"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Anakin's Lightsaber"),
    n("Mace Windu's Lightsaber"),
    n("Qui-Gon's Lightsaber"),
    n("Civil Disorder", True),
    n("Crash Site Memorial"),
    n("Draw Their Fire"),
    n("Mechanical Failure"),
    n("Sai'torr Kal Fas", True),
    n("Wokling", True),
    n("A Jedi's Resilience"),
    n("Blaster Deflection", qty=2),
    n("Clash Of Sabers"),
    n("Escape Pod", True),
    n("Free Ride & Endor Celebration"),
    n("Hear Me Baby, Hold Together", True),
    n("Houjix"),
    n("Impressive, Most Impressive", True),
    n("Jedi Levitation", True),
    n("Nabrun Leids", qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Sense", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Were You Looking For Me?"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Affect Mind"),
    n("Aim High"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Goldenrod"),
    n("Only Jedi Carry That Weapon"),
    n("Planetary Defenses"),
    n("Simple Tricks And Nonsense"),
    n("The Republic No Longer Functions"),
    n("Ultimatum"),
    n("Weapons Display"),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Your Ship?"),
]
LS_ADD = []

DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Death Star II: Throne Room"),
    n("Insignificant Rebellion"),
    n("Your Destiny"),
    n("Surface Defense", True),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Cloud City: Security Tower", True),
    n("Endor"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Boba Fett, Bounty Hunter"),
    n("Count Dooku", qty=2),
    n("Darth Maul With Lightsaber", qty=3),
    n("Darth Vader With Lightsaber", qty=3),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Emperor Palpatine"),
    n("Grand Moff Tarkin", True),
    n("Mara Jade With Lightsaber"),
    n("P-60"),
    n("Sith Probe Droid", True, qty=2),
    n("Wooof", True),
    n("Bossk In Hound's Tooth", True),
    n("Dengar In Punishing One"),
    n("Elis In Hinthra"),
    n("Maul's Sith Infiltrator"),
    n("Zuckuss In Mist Hunter"),
    n("Ability, Ability, Ability", True),
    n("Blast Door Controls"),
    n("Emperor's Power"),
    n("First Strike"),
    n("No Escape"),
    n("Search And Destroy"),
    n("The Phantom Menace"),
    n("Close Call", True),
    n("Dark Maneuvers", qty=2),
    n("Force Field", True, qty=2),
    n("Force Lightning", qty=2),
    n("Force Push", True),
    n("Ghhhk"),
    n("Masterful Move & Endor Occupation"),
    n("Maul Strikes"),
    n("Neimoidian Advisor"),
    n("Sith Fury", True),
    n("Sonic Bombardment", qty=2),
    n("Turn It Off! Turn It Off!", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Firepower"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Vote Of No Confidence"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
