#!/usr/bin/env python3
"""2015 European Championship leftover Xerox: Joe Olson Day 2.

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf pages 2–5 typed dumps.
p01 EC Final Standings skip card text. p02–p03 Dark / p04–p05 Light
Name Joe Olson Euros 2015 dested Joe Olson analog leftover generate_2015_2016.py CANON /
player-stubs/Joe_Olson.wiki.
Username blank. Pack existing Joe Olson.
"""
from __future__ import annotations

PLAYER = "Joe Olson"
USERNAME = ""
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 4
DS_PAGE = 2
LS_SCAN = "2015 European Championship Joe Olson LS.png"
DS_SCAN = "2015 European Championship Joe Olson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 01-17 p01 EC Final Standings skip card text. "
    "p02–p03 Dark 1/2 2/2 / p04–p05 Light 1/2 2/2 typed dumps dest from full-page rasters analog leftover Howard. "
    "Header Joe Olson Euros 2015 dested Joe Olson analog leftover generate_2015_2016.py CANON / player-stubs/Joe_Olson.wiki. "
    "Username blank. Event Day 2 circled 1 dest hub Day 2 Place 1. "
    "DS 3:1 / LS 4:0 dest notes. "
    "Pack existing Joe Olson. "
    "Do not dest as a new person. "
    "Do not dest 2015 EC Day 3 Joe Olson wrap dests. "
    "Do not rewrite wrap hub."
)
LS_NOTE = (
    "Typed dump p04–p05 Light 1/2 2/2 dest from full-page rasters analog leftover Howard. "
    "Name Joe Olson Euros 2015 LS dested Joe Olson. Username blank. LS Day 2 1/2 circled 1. LS 4:0 dest notes. "
    "START dested Watch Your Step / This Place Can Be A Little Rough generate label Watch Your Step. "
    "Anger, Fear, Aggression (v) dested Anger, Fear, Aggression True. "
    "Tatooine (EP 1) dested Tatooine (Coruscant). "
    "Heading For The Medical Frigate (+3 effects) dested Heading For The Medical Frigate dest 1; +3 effects dest notes. "
    "R2-D2 (Artoo-Detoo) (v) dested R2-D2 True. "
    "Pulsar Skate dested Booster In Pulsar Skate analog leftover Price dest as written slang. "
    "Obi-wan's Journal dested Obi-Wan's Journal. "
    "Houjix combo dested Houjix analog leftover dest as written slang. "
    "Luke Skywalker, Jedi Knight dest qty=4 unique overcounts sheet-accurate. "
    "Shields 15. Unique 60 shields 15."
)
DS_NOTE = (
    "Typed dump p02–p03 Dark 1/2 2/2 dest from full-page rasters analog leftover Howard. "
    "Name Joe Olson Euros 2015 DS dested Joe Olson. Username blank. DS Day 2 1/2 circled 1. DS 3:1 dest notes. "
    "START dested Endor Operations / Imperial Outpost generate label Endor Operations analog leftover Howard dual-title. "
    "Endor: Landing Platform (Docking Bay) dested Endor: Landing Platform. "
    "Dr Evazan & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Ominous Rumors dested Ominous Rumblings analog leftover dest as written slang. "
    "Short Range Fighters & Watch Your Back! dested Short-Range Fighters & Watch Your Back. "
    "SFS L-s9.3 Laser Cannon dested SFS L-s9.3 Laser Cannons. "
    "We'll Let Fate-a Decide, Huh? dested We'll Let Fate Decide, Huh?. "
    "Darth Maul with Lightsaber dest qty=3 unique overcounts sheet-accurate. Emperor Palpatine dest qty=3. "
    "Shields 15. Unique 60 shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine (Coruscant)"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Heading For The Medical Frigate"),
    n("Kessel"),
    n("Naboo: Boss Nass' Chambers"),
    n("Tatooine: Mos Eisley"),
    n("Captain Han Solo"),
    n("Dash Rendar"),
    n("Lando Calrissian", True),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("Melas", True, qty=2),
    n("Mirax Terrik"),
    n("Obi-Wan Kenobi", True, qty=2),
    n("R2-D2", True),
    n("Talon Karrde"),
    n("Threepio With His Parts Showing"),
    n("Wedge Antilles", True),
    n("Millennium Falcon"),
    n("Outrider"),
    n("Booster In Pulsar Skate"),
    n("Luke's Lightsaber"),
    n("Luke's Bionic Hand", qty=2),
    n("Obi-Wan's Journal"),
    n("I'll Take The Leader"),
    n("Like My Father Before Me"),
    n("Ounee Ta"),
    n("Squadron Assignments"),
    n("Tatooine Celebration"),
    n("Wokling", True),
    n("A Few Maneuvers", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Blaster Deflection"),
    n("Control & Tunnel Vision", qty=2),
    n("Dodge"),
    n("Free Ride & Endor Celebration"),
    n("It Could Be Worse"),
    n("It's A Hit!"),
    n("Houjix"),
    n("Moving To Attack Position", qty=2),
    n("On The Edge"),
    n("Rebel Barrier"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Mindful Of The Future"),
    n("Were You Looking For Me?"),
    n("Wesa Gotta Grand Army", qty=2),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Goldenrod"),
    n("He Can Go About His Business"),
    n("Jabba's Prize", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("The Republic No Longer Functions"),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Your Ship?"),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform"),
    n("Fondor"),
    n("Admiral Ozzel"),
    n("Baron Soontir Fel", qty=2),
    n("Major Turr Phennir"),
    n("DS-61-2"),
    n("Darth Maul With Lightsaber", qty=3),
    n("Darth Vader", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Emperor Palpatine", qty=3),
    n("Grand Moff Tarkin", True),
    n("Mara Jade With Lightsaber"),
    n("P-59"),
    n("Janus Greejatus"),
    n("Stormtrooper Garrison"),
    n("Ability, Ability, Ability", True),
    n("Combat Response", True),
    n("Endor Shield", True),
    n("Establish Control", True),
    n("Imperial Decree", True),
    n("Ominous Rumors"),
    n("Knowledge And Defense", True),
    n("Something Special Planned For Them", True),
    n("All Power To Weapons", qty=2),
    n("Close Call", True, qty=2),
    n("Dark Maneuvers"),
    n("Force Lightning"),
    n("Force Push", True),
    n("Ghhhk"),
    n("Masterful Move & Endor Occupation"),
    n("Prepared Defenses"),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("I Have You Now"),
    n("Sith Fury", True),
    n("Sense"),
    n("According To My Design", True),
    n("Black 2", True),
    n("Maul's Sith Infiltrator"),
    n("Saber 1", qty=2),
    n("Saber 2"),
    n("Vader's Personal Shuttle", True),
    n("Blizzard 4", qty=2),
    n("Fighters Coming In", qty=2),
    n("SFS L-s9.3 Laser Cannons", qty=2),
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
    n("Vote Of No Confidence"),
    n("Imperial Detention"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
