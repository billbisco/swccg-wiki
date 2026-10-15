#!/usr/bin/env python3
"""2015 European Championship Day 2: Cedrik Vanderhaegen (place 24).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p15 DS / p16 LS handwritten deck list forms.
"""
from __future__ import annotations

PLAYER = "Cedrik Vanderhaegen"
USERNAME = "Cologlin"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 16
DS_PAGE = 15
LS_SCAN = "2015 European Championship Cedrik Vanderhaegen LS.png"
DS_SCAN = "2015 European Championship Cedrik Vanderhaegen DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 24 circled. Forms signed 'Cedrik' only, event 'Euro 15', no date. "
    "Username DS 'Cologlin' (scrawl; LS looks like 'Callaglin') — REVIEWED: CONFIRM 'Cologlin' (DS box clear; LS same hand). "
    "DS deck name 'TTON' (?), DS 2:2. LS deck name 'TRG' (?), LS 1:3."
)
LS_NOTE = (
    "Form 60 lines + 15 shields; ditto marks expanded. Heavy abbreviations. "
    "Posted Yavin 4: MTR dested Yavin 4: Massassi Throne Room. "
    "Posted Squad Ass dested Squadron Assignments. Posted Heading FTMF dested Heading For The Medical Frigate. "
    "Posted Naboo: Otoh Gungan Entrance / \" : Boss Nass' Ch. dested Naboo: Otoh Gunga Entrance / Naboo: Boss Nass' Chambers. "
    "REVIEWED: CONFIRM line 8 \"Nar Shdaa\" scrawl (LS system, fits Naboo/Gungan deck) dested Nar Shaddaa. "
    "Posted Projection OAS dested Projection Of A Skywalker. "
    "Posted Fanbow x2 dested Fambaa. "
    "Posted EPP Quigon x2 dested Qui-Gon Jinn With Lightsaber; EPP OB dested Obi-Wan With Lightsaber. "
    "Posted 3PO w HPS dested Threepio With His Parts Showing. Posted Anakin Skywalker, PL dested Anakin Skywalker, Padawan Learner. "
    "Posted Wedge Antilles RSL dested Wedge Antilles, Red Squadron Leader. Posted Red Squad 4 / \" 1 dested Red Squadron 4 / Red Squadron 1. "
    "Posted Artoo-Detoo in Red 5 x2 dested Artoo-Detoo In Red 5. "
    "Posted Sorry About The Mess & BP dested Sorry About The Mess & Blaster Proficiency. "
    "Posted All Wings Report In & DS dested All Wings Report In & Darklighter Spin (one copy V, one not). "
    "Posted Organised Attack dested Organized Attack. Posted YISYW dested Your Insight Serves You Well. "
    "Luke Skywalker (V) written twice (lines 30, 33) — kept as written."
)
DS_NOTE = (
    "Form 60 lines + 15 shields; ditto marks expanded. "
    "Line 26 crossed out; arrow to margin '26. Knowledge & Defense (V)' dests the replacement. "
    "Posted Endor Operations dested Endor Operations / Imperial Outpost. Posted Ability x3 dested Ability, Ability, Ability. "
    "Posted EPP Maul x3 dested Darth Maul With Lightsaber. Posted Vader's Shuttle dested Vader's Personal Shuttle. "
    "Posted SFS L-s9.3 Laser Cannon dested SFS L-s9.3 Laser Cannons. Posted Ominous Rumours dested Ominous Rumors. "
    "Posted Omni Box & It's Worse dested Ommni Box & It's Worse. "
    "Posted Short Range Fighters & WYB dested Short-Range Fighters & Watch Your Back. "
    "Posted Turn It Off x2! dested Turn It Off! Turn It Off!. Posted A Dark Time For The R. dested A Dark Time For The Rebellion. "
    "Posted DS-181-4 as written."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Wokling", True),
    n("Squadron Assignments"),
    n("A New Secret Base", True),
    n("Naboo: Battle Plains"),
    n("Naboo: Otoh Gunga Entrance"),
    n("Naboo: Boss Nass' Chambers"),
    n("Nar Shaddaa"),
    n("Heading For The Medical Frigate"),
    n("Gungan Energy Shield", qty=2),
    n("Steady, Steady"),
    n("Projection Of A Skywalker"),
    n("K'lor'slug", True),
    n("Fambaa", qty=2),
    n("X-wing Laser Cannon", qty=2),
    n("Corran Horn"),
    n("Rep Been"),
    n("Aayla Secura"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber"),
    n("Gungan General", qty=2),
    n("Boss Nass"),
    n("Threepio With His Parts Showing"),
    n("Jar Jar Binks"),
    n("Luke Skywalker", True, qty=2),
    n("Anakin Skywalker, Padawan Learner"),
    n("Lando Calrissian, Scoundrel"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Derek 'Hobbie' Klivian", True),
    n("Red Squadron 4"),
    n("Red Squadron 1"),
    n("Azure Angel"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Houjix"),
    n("Rebel Barrier"),
    n("A Jedi's Resilience"),
    n("A Few Maneuvers"),
    n("Direct Assault"),
    n("Escape Pod", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("All Wings Report In & Darklighter Spin", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Organized Attack"),
    n("Jedi Levitation", True),
    n("Were You Looking For Me?"),
    n("Wesa Gotta Grand Army", qty=6),
    n("Rebel Leadership"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Wise Advice"),
    n("Goldenrod"),
    n("Aim High"),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Affect Mind", True),
    n("He Can Go About His Business"),
    n("Ounee Ta"),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform"),
    n("Endor"),
    n("Force Lightning"),
    n("Ability, Ability, Ability", True),
    n("Force Field", True),
    n("Darth Vader", True),
    n("Admiral Piett"),
    n("Darth Maul With Lightsaber", qty=3),
    n("Count Dooku"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Masterful Move & Endor Occupation"),
    n("Maul's Sith Infiltrator"),
    n("Black 2", True),
    n("Vader's Personal Shuttle", True),
    n("Saber 1"),
    n("Dark Maneuvers", qty=2),
    n("Saber 4"),
    n("Emperor Palpatine", qty=2),
    n("SFS L-s9.3 Laser Cannons"),
    n("Knowledge And Defense", True),
    n("Fighters Coming In"),
    n("Ominous Rumors"),
    n("Ommni Box & It's Worse"),
    n("Ghhhk"),
    n("Maul Strikes", qty=2),
    n("Stormtrooper Garrison"),
    n("Force Push", True),
    n("The Phantom Menace"),
    n("P-59"),
    n("Blockade Flagship: Bridge"),
    n("Fondor"),
    n("Baron Soontir Fel", qty=2),
    n("All Power To Weapons", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Grand Moff Tarkin", True),
    n("DS-61-2"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Turn It Off! Turn It Off!", True),
    n("Count Dooku", True),
    n("I Have You Now"),
    n("A Dark Time For The Rebellion", True),
    n("DS-181-4"),
    n("Security Precautions"),
    n("According To My Design", True),
    n("Prepared Defenses"),
    n("Establish Control", True),
    n("Combat Response", True),
    n("Endor Shield", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Resistance"),
    n("Allegations Of Corruption"),
    n("Vote Of No Confidence"),
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention"),
    n("Do They Have A Code Clearance?"),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("Fanfare", True),
]
DS_ADD = []
