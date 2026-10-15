#!/usr/bin/env python3
"""2015 European Championship Day 2: Eric Spijksma (place 31).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf p29 Dark / p30 Light typed lists.
"""
from __future__ import annotations

PLAYER = "Eric Spijksma"
USERNAME = "Ericobasso"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 18-35.pdf"
LS_PAGE = 30
DS_PAGE = 29
LS_SCAN = "2015 European Championship Eric Spijksma LS.png"
DS_SCAN = "2015 European Championship Eric Spijksma DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 18-35 p29 Dark / p30 Light typed lists, circled 31. "
    "Username Ericobasso on both sheets. Event Europeans 2015, date 17-10-2015. "
    "DS 2:2 / LS 0:4 handwritten."
)
LS_NOTE = (
    "START Quiet Mining Colony/flip side dested Quiet Mining Colony / Independent Operation. "
    "Posted Anger, Fear, Agression (v) dested Anger, Fear, Aggression True. "
    "Posted Lando, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Posted Pecumir Thryss dested Pucumir Thryss. "
    "Posted Path Of The Least Resistance dested Path Of Least Resistance. "
    "Posted Life Dept dested Life Debt. "
    "Posted Millenium Falcon dested Millennium Falcon. "
    "Posted Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Posted Darklighters Spin dested Darklighter Spin. "
    "Main 60, shields 15."
)
DS_NOTE = (
    "START Endor Operations/flip side dested Endor Operations / Imperial Outpost. "
    "Posted Tatooine (ep 1) dested Tatooine (Coruscant). "
    "Posted Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back!. "
    "Posted Omni Box & It's Worse dested Ommni Box & It's Worse. "
    "Posted Masterful Move & Endor Celebration dested Masterful Move & Endor Occupation. "
    "Posted Elis In Hintra dested Elis In Hinthra. "
    "Posted 4-LOM with Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate"),
    n("Squadron Assignments"),
    n("Keeping The Empire Out Forever"),
    n("Beldon's Eye", True),
    n("Cloud City: North Corridor"),
    n("Cloud City: West Gallery"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: East Platform (Docking Bay)"),
    n("Luke Skywalker", True),
    n("Lando Calrissian, Scoundrel"),
    n("Captain Han Solo"),
    n("Chewie", True),
    n("Anakin Skywalker", True),
    n("Yoxgit"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Mirax Terrik"),
    n("Harc Seff", True),
    n("Corran Horn"),
    n("Melas", True),
    n("Pucumir Thryss"),
    n("Leia, Rebel Princess"),
    n("Obi-Wan Kenobi", True),
    n("Yoda, Keeper Of The Peace", True),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Aayla Secura", True),
    n("Princess Leia", True),
    n("Leesub Sirln", True),
    n("Commander Narra", True),
    n("Cloud City Celebration"),
    n("Honor Of The Jedi"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver", True, qty=2),
    n("Path Of Least Resistance", qty=2),
    n("Jedi Levitation", True),
    n("A Few Maneuvers", qty=2),
    n("Sense", qty=2),
    n("Alter", True),
    n("Don't Get Cocky"),
    n("Free Ride & Endor Celebration"),
    n("Life Debt"),
    n("Houjix & Out Of Nowhere"),
    n("Rebel Barrier", qty=2),
    n("Millennium Falcon"),
    n("Artoo-Detoo In Red 5"),
    n("Pulsar Skate"),
    n("Azure Angel", True),
    n("Overseer", True),
    n("Anakin's Lightsaber"),
    n("Landing Claw"),
    n("I'll Take The Leader"),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Weapons Display"),
    n("A Tragedy Has Occurred"),
    n("Affect Mind"),
    n("Ultimatum"),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again"),
    n("Planetary Defenses"),
    n("The Republic No Longer Functions"),
    n("Goldenrod"),
    n("Your Insight Serves You Well"),
    n("Simple Tricks And Nonsense"),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Jabba's Prize"),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Prepared Defenses"),
    n("Endor Shield", True),
    n("Combat Response"),
    n("Something Special Planned For Them", True),
    n("Tatooine (Dark) (Coruscant)"),
    n("Kashyyyk"),
    n("Kessel"),
    n("Emperor Palpatine"),
    n("Count Dooku", True),
    n("Darth Maul", qty=2),
    n("Darth Vader With Lightsaber", qty=2),
    n("Admiral Piett"),
    n("Admiral Ozzel"),
    n("Commander Merrejk"),
    n("Boba Fett, Bounty Hunter"),
    n("Jango Fett", True),
    n("Grand Moff Tarkin", True),
    n("Bossk", True),
    n("Arica"),
    n("4-LOM With Concussion Rifle", True),
    n("Dr. Evazan"),
    n("Wooof", True),
    n("Ponda Baba", True),
    n("P-59"),
    n("Ominous Rumors"),
    n("Imperial Decree", True),
    n("No Escape"),
    n("Image Of The Dark Lord", True),
    n("Presence Of The Force"),
    n("Cease Fire!"),
    n("Force Lightning"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Ghhhk"),
    n("Turn It Off! Turn It Off!", True),
    n("Dark Maneuvers"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sense & Uncertain Is The Future"),
    n("Sith Fury", True),
    n("Elis Helrot"),
    n("Imperial Barrier"),
    n("I Have You Now"),
    n("Ommni Box & It's Worse"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Slave I, Symbol Of Fear", True),
    n("Hound's Tooth", True),
    n("Zuckuss In Mist Hunter"),
    n("Elis In Hinthra"),
    n("Blizzard 2", True),
    n("Black Sun Fleet", qty=3),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Secret Plans"),
    n("A Useless Gesture"),
    n("Death Star Sentry"),
    n("Do They Have A Code Clearance?"),
    n("Oppressive Enforcement"),
    n("Vote Of No Confidence"),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Leave Them To Me"),
    n("Come Here You Big Coward"),
    n("Firepower"),
    n("Allegations Of Corruption"),
    n("Imperial Detention"),
]
DS_ADD = []
