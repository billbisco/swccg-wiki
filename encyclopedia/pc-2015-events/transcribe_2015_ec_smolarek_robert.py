#!/usr/bin/env python3
"""2015 European Championship: Robert Smolarek Day 2 (place 12).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p26 Dark / p27 Light (handwritten, 2014 PC form).
File slug smolarek_robert because transcribe_2015_ec_smolarek.py is Julian Smolarek (place 23).
"""
from __future__ import annotations

PLAYER = "Robert Smolarek"
USERNAME = "Babba the Hutt"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 27
DS_PAGE = 26
LS_SCAN = "2015 European Championship Robert Smolarek LS.png"
DS_SCAN = "2015 European Championship Robert Smolarek DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 12 circled. p26 Dark / p27 Light handwritten. Name Robert Smolarek, Username 'Babba the Hutt' (could be 'Bobba'), "
    "email on sheet (not transcribed). Event Date 17/10/2015, Event Name Europeans. DS 3:1 / LS 2:2. "
    "Sheet deck names: DS 'Let Them Make The First Move', LS 'Naboo w/ Careful Planning' (not used as DECK_NAME)."
)
LS_NOTE = (
    "No objective; START Careful Planning (line 2, V checked = Careful Planning (V)). "
    "TITLE MISMATCH: wiki says Combat Preparedness (V), sheet starts Careful Planning (V) (Naboo / Theed Palace Generator start). "
    "Posted TP Generator dested Naboo: Theed Palace Generator. Posted Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Posted Corulag (sheet 'Carulag') dested Corulag. Posted Obi-Wan WLS (+2 ditto) dested Obi-Wan With Lightsaber x3. "
    "Posted Qui Gon Jinn WLS (+3 ditto) dested Qui-Gon Jinn With Lightsaber x4 (unique overcounts sheet-accurate). "
    "Posted Anakin Skywalker Pad-L. dested Anakin Skywalker, Padawan Learner. Posted Threepio With HPS dested Threepio With His Parts Showing. "
    "Posted Conan Horn dested Corran Horn. Posted Wedge Antilles, Red Squ. Leader dested Wedge Antilles, Red Squadron Leader. "
    "Posted All Wings Report In & DS dested All Wings Report In & Darklighter Spin. Posted Free Ride & EC dested Free Ride & Endor Celebration. "
    "Posted Out Of Commission & TT dested Out Of Commission & Transmission Terminated. Posted Sorry About The Mess & BP dested Sorry About The Mess & Blaster Proficiency. "
    "Shields: Do Or Do Not dested Do, Or Do Not; Goldenrod (V) kept as written; Yavin Sentry V. Main 60, shields 15."
)
DS_NOTE = (
    "START Let Them Make The First Move / At Last We Will Have Revenge (line 2). "
    "TITLE MISMATCH: wiki says Combat Readiness, sheet starts Let Them Make The First Move (Combat Readiness not on the sheet). "
    "Posted TP Generator / TP Generator Core dested Naboo: Theed Palace Generator / Generator Core. Posted 4-LOM WCR dested 4-LOM With Concussion Rifle. "
    "Posted CC: Security Tower dested Cloud City: Security Tower. Posted Darth Vader With LS dested Darth Vader With Lightsaber x3. "
    "Lord Maul x4, Count Dooku x3, Darth Sidious x2, The Phantom Menace x4 (unique overcounts sheet-accurate). "
    "Posted Mara Jade With LS dested Mara Jade With Lightsaber; line 24 scribbled-out word then ditto with V checked: x2 both V. "
    "Posted Masterful Move & EO dested Masterful Move & Endor Occupation. "
    "Line 45 Sneak Attack crossed out, Lightsaber Parry written, V box scribbled out: dested Lightsaber Parry non-V (total 2). "
    "Posted Mauls Double-Bladed LS dested Maul's Double-Bladed Lightsaber x2. Posted Dooku's Lightsaber kept. "
    "Posted Aurra Sing's Blaster Rifle kept. Line 60 Sith Fury V (total 3 Sith Fury V). "
    "Shields: Come Here You Big Coward; Imperial Detention kept (wiki title). Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Careful Planning"
LS_CARDS = [
    n("Naboo"),
    n("Careful Planning", True),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Boss Nass' Chambers"),
    n("Corulag"),
    n("Mon Calamari"),
    n("Obi-Wan With Lightsaber", qty=3),
    n("Qui-Gon Jinn With Lightsaber", qty=4),
    n("Anakin Skywalker, Padawan Learner"),
    n("Mace Windu", True),
    n("Yoda, Keeper Of The Peace"),
    n("Luke Skywalker", True),
    n("Captain Han Solo"),
    n("Lando Calrissian", True),
    n("Lando Calrissian, Scoundrel"),
    n("Threepio With His Parts Showing"),
    n("Corran Horn"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Dash Rendar"),
    n("A New Secret Base", True),
    n("Civil Disorder", True),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("A Few Maneuvers"),
    n("A Jedi's Concentration"),
    n("A Jedi's Resilience", qty=3),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Clash Of Sabers"),
    n("Escape Pod", True, qty=2),
    n("Free Ride & Endor Celebration"),
    n("Houjix"),
    n("Jedi Levitation", True, qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Rebel Artillery", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Were You Looking For Me?"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Millennium Falcon"),
    n("Red Squadron 1"),
    n("Outrider"),
    n("Azure Angel"),
    n("X-wing Laser Cannon"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Goldenrod", True),
    n("He Can Go About His Business"),
    n("Let's Keep A Little Optimism Here"),
    n("Planetary Defenses"),
    n("Simple Tricks And Nonsense", True),
    n("The Republic No Longer Functions", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Let Them Make The First Move / At Last We Will Have Revenge"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Let Them Make The First Move / At Last We Will Have Revenge"),
    n("Deep Hatred"),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Theed Palace Generator Core"),
    n("Any Methods Necessary"),
    n("4-LOM With Concussion Rifle", True),
    n("Cloud City: Security Tower", True),
    n("Darth Vader With Lightsaber", qty=3),
    n("Lord Maul", qty=4),
    n("Darth Sidious", qty=2),
    n("Count Dooku", qty=3),
    n("Emperor Palpatine", qty=2),
    n("Mara Jade With Lightsaber", True, qty=2),
    n("Search And Destroy"),
    n("The Phantom Menace", qty=4),
    n("Force Lightning", qty=2),
    n("Force Push", True),
    n("Ghhhk"),
    n("I Have You Now"),
    n("Lightsaber Parry", qty=2),
    n("Force Field", True),
    n("Masterful Move", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Maul Strikes", qty=3),
    n("Sith Fury", True, qty=3),
    n("Stunning Leader", qty=3),
    n("We Must Accelerate Our Plans", qty=3),
    n("Weapon Levitation"),
    n("Blaster Rack", True),
    n("Blockade Flagship: Bridge"),
    n("Maul's Double-Bladed Lightsaber", qty=2),
    n("Dooku's Lightsaber"),
    n("Aurra Sing's Blaster Rifle"),
    n("Intruder Missile"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention"),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Vote Of No Confidence", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
