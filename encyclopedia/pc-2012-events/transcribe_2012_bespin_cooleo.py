#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Cooleo.

Source: 2012BespinRegionals.pdf pages 9–10 (handwritten 2010 Xerox).
p09 Dark / p10 Light Name Cooleo dested Cooleo analog leftover 2012 Nats /
player-stubs/Cooleo.wiki. Username CooleoAc.
Do not dest as a new person. Do not dest 2012 Nats Cooleo 60s again.
"""
from __future__ import annotations

PLAYER = "Cooleo"
USERNAME = "CooleoAc"
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 10
DS_PAGE = 9
LS_SCAN = "2012 Bespin Regionals Cooleo LS.png"
DS_SCAN = "2012 Bespin Regionals Cooleo DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox p09 Dark / p10 Light. "
    "Name Cooleo dested Cooleo analog leftover 2012 Nats / player-stubs/Cooleo.wiki. "
    "Username CooleoAc. Event Date blank Event Bespin Regional. "
    "Do not dest as a new person. Do not dest 2012 Nats Cooleo 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p10 Light. Name Cooleo dested Cooleo. Username CooleoAc. "
    "LIGHT checked. Deck Name Attrition 16.-- sorry dested off article. "
    "Rebel Strike Team dested Rebel Strike Team / Garrison Destroyed True analog leftover 2012 Nats Cooleo. "
    "Anger, Fear, Aggression True IN THE 60. "
    "Rebel Leadership True line 3 and empty lines 4–5 kept separate. "
    "Antilles Combo dested Antilles Maneuver & Rebel Reinforcements analog leftover Cooleo Nats. "
    "Haash'n dested Major Haash'n analog leftover Cooleo Nats True line 11 and empty line 55 kept separate. "
    "Heading For Frigate dested Heading For The Medical Frigate True analog leftover Cooleo Nats. "
    "General Madine dested General Crix Madine analog leftover Cooleo Nats. "
    "Naboo Leits dested Nabrun Leids analog leftover Lush qty=2. "
    "Rapid Deployment True line 23 and empty lines 24–26 kept separate. "
    "Cpt Yutani w/ Gun dested Captain Yutani With Blaster Cannon analog leftover Lingrell. "
    "That's One dested That's One True analog leftover Cooleo Nats. "
    "Houjix Combo dested Houjix & Out Of Nowhere analog leftover. "
    "Col Cracken dested Colonel Cracken analog leftover Martin. "
    "Luke Skywalker, Rebel Scout True line 49 and empty line 50 kept separate. "
    "Bron Burs True line 13 and empty line 14 kept separate dest as written. "
    "Shield 12 empty skip unique 11 sheet-accurate."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p09 Dark. Name Cooleo dested Cooleo. Username CooleoAc. "
    "DARK checked. Deck Name FLOPS dested off article. "
    "No objective on sheet dested line 1 Executor: Meditation Chamber analog leftover Fred / Ojala. "
    "Prepared Def dested Prepared Defenses True analog leftover. "
    "YCHTF Combo dested You Cannot Hide Forever analog leftover Massung. "
    "Imperial Arrest Combo dested Imperial Arrest Order & Secret Plans analog leftover Bordier. "
    "U3PO dested U-3PO analog leftover. "
    "Lightsaber Def True line 7 and empty line 8 kept separate. "
    "EX:DB dested Executor: Docking Bay. EX: Holo dested Executor: Holotheatre. "
    "EXiComm dested Executor: Comm Station analog leftover Fred. "
    "EXi Hallway dested Executor: Hallway dest as written. "
    "Intense Batteries dested Intensify The Forward Batteries analog leftover Kafer qty=2. "
    "Maul w/ Stick dested Darth Maul With Lightsaber analog leftover Kafer qty=2. "
    "Flops dest as written qty=2. "
    "Drop dested Drop! True analog leftover Light Frank. "
    "Laser Combo dested Laser Cannon Battery analog leftover Kafer. "
    "Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us analog leftover. "
    "Why didn't you dested Why Didn't You Tell Me True line 38 and empty line 39 kept separate analog leftover Kafer. "
    "Mntalonian Fathiers + Fett dested Jango Fett, The Assassin analog leftover Atkin. "
    "Operational As Planned True line 41 and empty lines 42–43 kept separate. "
    "Where Are You Taking dested Where Are You Taking This... Cargo? analog leftover. "
    "Astro Short dested Short Range Fighters True analog leftover Massung. "
    "Executor / Flag Executor dested Flagship Executor analog leftover Baroni qty=2 at first occurrence. "
    "Col Jendon Onyx 1 dested Colonel Jendon In Onyx 1 analog leftover. "
    "Thrawn dested Grand Admiral Thrawn analog leftover. "
    "Knowledge And Defense True IN THE 60. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Rebel Strike Team / Garrison Destroyed"
LS_CARDS = [
    n("Rebel Strike Team / Garrison Destroyed", True),
    n("Anger, Fear, Aggression", True),
    n("Rebel Leadership", True),
    n("Rebel Leadership", qty=2),
    n("Orrimaarko"),
    n("General Solo", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Launching The Assault"),
    n("Sergeant Brooks"),
    n("Major Haash'n", True),
    n("Lieutenant Page"),
    n("Bron Burs", True),
    n("Bron Burs"),
    n("Heading For The Medical Frigate", True),
    n("General Crix Madine"),
    n("Chewbacca Of Kashyyyk"),
    n("Explosive Charge", qty=2),
    n("Deactivate The Shield Generator"),
    n("Nabrun Leids", qty=2),
    n("Rapid Deployment", True),
    n("Rapid Deployment", qty=3),
    n("Home One"),
    n("Bright Hope", True),
    n("Sergeant Junkin"),
    n("Endor: Rebel Landing Site"),
    n("Endor"),
    n("Scrambled Transmission", True),
    n("Corporal Midge"),
    n("Endor: Back Door"),
    n("Captain Yutani With Blaster Cannon"),
    n("Lieutenant Blount", True),
    n("Honor Of The Jedi"),
    n("Endor: Bunker"),
    n("Count Me In", True),
    n("That's One", True),
    n("I Wonder Who They Found", True),
    n("Capital Support"),
    n("Commando Training", True),
    n("Wokling", True),
    n("The Shield Is Down!", True),
    n("I Hope She's All Right", True),
    n("Strike Planning"),
    n("Menace Fades"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke Skywalker, Rebel Scout"),
    n("Houjix & Out Of Nowhere"),
    n("Corporal Delevar"),
    n("Colonel Cracken"),
    n("Toryn Farr", True),
    n("Major Haash'n"),
    n("Imperial Atrocity", True),
    n("Admiral Ackbar", True),
    n("Double Agent"),
    n("Corporal Kensell"),
    n("Daughter Of Skywalker"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Do, Or Do Not", True),
    n("Don't Do That Again", True),
    n("Battle Plan", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("Ultimatum", True),
]
LS_ADD = []

DS_START = "Executor: Meditation Chamber"
DS_CARDS = [
    n("Executor: Meditation Chamber"),
    n("Prepared Defenses", True),
    n("I'll Take Them Myself"),
    n("You Cannot Hide Forever"),
    n("Imperial Arrest Order & Secret Plans"),
    n("U-3PO"),
    n("Lightsaber Deficiency", True),
    n("Lightsaber Deficiency"),
    n("Executor: Docking Bay"),
    n("Executor: Holotheatre"),
    n("Executor: Comm Station"),
    n("Executor: Hallway"),
    n("Yavin 4"),
    n("Hoth"),
    n("Relentless Pursuit", qty=3),
    n("TIE Interceptor", qty=5),
    n("Sonic Bombardment", True),
    n("Intensify The Forward Batteries", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Flops", qty=2),
    n("Imperial Decree"),
    n("Imperial Command", qty=2),
    n("Drop!", True),
    n("Laser Cannon Battery"),
    n("Imperial Stockpile"),
    n("Gal Dorn"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Why Didn't You Tell Me", True),
    n("Why Didn't You Tell Me"),
    n("Jango Fett, The Assassin"),
    n("Operational As Planned", True),
    n("Operational As Planned", qty=2),
    n("Victory"),
    n("Where Are You Taking This... Cargo?"),
    n("Tarkin's Bounty", True),
    n("Image Of The Dark Lord", True),
    n("Flagship Executor", qty=2),
    n("Imperial Propaganda", True),
    n("Short Range Fighters", True),
    n("Protocol Failure"),
    n("OOM-9", True),
    n("Chimaera"),
    n("Accuser"),
    n("Onyx 2", True),
    n("Colonel Jendon In Onyx 1"),
    n("Conquest", True),
    n("Grand Admiral Thrawn"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("There Is No Try", True),
    n("Resistance"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("After Her", True),
]
DS_ADD = []
