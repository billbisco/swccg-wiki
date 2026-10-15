#!/usr/bin/env python3
"""2015 European Championship: Lukasz Saczek Day 2 (place 13).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p28 Dark / p29 Light (handwritten).
"""
from __future__ import annotations

PLAYER = "Lukasz Saczek"
USERNAME = "Fon-Q"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 29
DS_PAGE = 28
LS_SCAN = "2015 European Championship Lukasz Saczek LS.png"
DS_SCAN = "2015 European Championship Lukasz Saczek DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 13 circled. p28 Dark / p29 Light handwritten. Name 'Saczek Lukasz', Username Fon-Q on both, email on sheet (not transcribed). "
    "Event Date 10/17/2015, Event Name EC Bochum 2015. DS 2:2 / LS 3:1. Sheet deck name 'Back To The Roots' both sides (not used as DECK_NAME)."
)
LS_NOTE = (
    "START We'll Handle This / Duel Of The Fates (line 1 'We'll Handle This / Duel of The Fates'). "
    "TITLE MISMATCH: wiki says Combat Preparedness, sheet starts We'll Handle This. "
    "Posted R-2 In Red 5 (lines 12, 15, 22, 35, 57) dested Artoo-Detoo In Red 5 x5 (unique overcount sheet-accurate). "
    "Posted Qui-Gon's Lightsaber REF3 dested Qui-Gon's Lightsaber x2. Posted All Wings Report In & Darklighter Spin kept (x1). "
    "Qui-Gon Jinn, Jedi Master x3 and Yoda, Master Of The Force x2 (sheet-accurate). "
    "Posted Blast The Door, Kid dested Blast The Door, Kid! x2. Posted Antilles Maneuver kept. "
    "Posted The Bith Shuffle & Desperate Reach kept. Posted Nar Shaddea dested Nar Shaddaa. "
    "Shields: Do, Or Do Not; Goldenrod kept as written. Main 60, shields 15."
)
DS_NOTE = (
    "START Let Them Make The First Move / At Last We Will Have Revenge (sheet 'Let Them Make First Move'). "
    "TITLE MISMATCH: wiki says Combat Readiness, sheet starts Let Them Make The First Move (Combat Readiness not on the sheet). "
    "Posted Omni Box & It's Worse dested Ommni Box & It's Worse. Posted Maul Strike dested Maul Strikes x2. "
    "Posted Phantom Menace dested The Phantom Menace (x3 total). Posted Ghhhk kept. "
    "Line 46 Weapon Levitation crossed out, 'A Dark Time For A Rebellion' written with V checked: dested A Dark Time For The Rebellion V. "
    "Lord Maul x3, Count Dooku x3, Emperor Palpatine x3 (unique overcounts sheet-accurate). Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates"),
    n("Anger, Fear, Aggression", True),
    n("Inner Strength"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("A New Secret Base", True),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("Heading For The Medical Frigate"),
    n("On The Edge"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Artoo-Detoo In Red 5", qty=5),
    n("Qui-Gon's Lightsaber", qty=2),
    n("X-wing Laser Cannon"),
    n("Escape Pod", True, qty=2),
    n("Yoda, Master Of The Force", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Blast The Door, Kid!", qty=2),
    n("A Few Maneuvers"),
    n("Alter", True),
    n("Sense", qty=2),
    n("Leia, Rebel Princess"),
    n("Yoxgit"),
    n("Jedi Levitation", True, qty=2),
    n("Qui-Gon Jinn, Jedi Master", qty=3),
    n("The Bith Shuffle & Desperate Reach"),
    n("Corran Horn"),
    n("Green Leader In Green Squadron 1"),
    n("Control & Tunnel Vision"),
    n("Evacuation Control", True),
    n("Antilles Maneuver", True),
    n("Rebel Barrier"),
    n("We're Doomed"),
    n("Ascension Guns", True),
    n("It Could Be Worse"),
    n("Blaster Deflection"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Free Ride & Endor Celebration"),
    n("Obi-Wan Kenobi, Jedi Knight"),
    n("Dodge"),
    n("Luke Skywalker", True, qty=2),
    n("Han, Chewie, And The Falcon"),
    n("Lando Calrissian, Scoundrel"),
    n("Red Squadron 1"),
    n("Houjix"),
    n("Threepio With His Parts Showing"),
    n("Nar Shaddaa"),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("He Can Go About His Business"),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Do, Or Do Not"),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("Goldenrod"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("The Republic No Longer Functions"),
]
LS_ADD = []

DS_START = "Let Them Make The First Move / At Last We Will Have Revenge"
DS_CARDS = [
    n("Let Them Make The First Move / At Last We Will Have Revenge"),
    n("Knowledge And Defense", True),
    n("Deep Hatred"),
    n("According To My Design"),
    n("Emperor Palpatine", qty=3),
    n("Wipe Them Out, All Of Them"),
    n("Blaster Rack", True),
    n("Crush The Rebellion"),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Bridge"),
    n("Lord Maul", qty=3),
    n("Darth Maul"),
    n("Count Dooku", qty=3),
    n("4-LOM With Concussion Rifle", True),
    n("P-59"),
    n("Janus Greejatus"),
    n("Darth Vader With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Mara Jade With Lightsaber"),
    n("Maul Strikes", qty=2),
    n("Ommni Box & It's Worse"),
    n("Sith Fury", True, qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Masterful Move"),
    n("Imperial Barrier"),
    n("Force Push", True),
    n("I Have You Now", qty=2),
    n("Force Field", True, qty=2),
    n("Ghhhk"),
    n("Force Lightning", qty=2),
    n("The Circle Is Now Complete"),
    n("Stunning Leader", qty=2),
    n("A Dark Time For The Rebellion", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("Emperor's Personal Shuttle"),
    n("Maul's Sith Infiltrator"),
    n("Dooku's Lightsaber"),
    n("Maul's Double-Bladed Lightsaber", qty=2),
    n("The Phantom Menace", qty=3),
    n("Image Of The Dark Lord", True),
    n("Disarmed"),
    n("Search And Destroy"),
    n("Qui-Gon's End"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Vote Of No Confidence", True),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?"),
]
DS_ADD = []
