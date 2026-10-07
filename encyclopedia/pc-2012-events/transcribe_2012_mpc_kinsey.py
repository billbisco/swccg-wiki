#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Aaron Kinsey.

Source: 2012mpcday1.pdf pages 103–104 (2010 form, 12 shields).
Name Aaron Kinsey dested Aaron Kinsey (analog generate empty).
p103 Light Yavin 4: Massassi Throne Room. p104 Dark Endor Operations.
Username blank. Pack player-stubs/Aaron_Kinsey.wiki.
Do not dest as Aaron Kingery / Aaron Kia.
"""
from __future__ import annotations

PLAYER = "Aaron Kinsey"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 103
DS_PAGE = 104
LS_SCAN = "2012 Match Play Championship Day 1 Aaron Kinsey LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Aaron Kinsey DS.png"
LS_DECK_NAME = "Y4: Albany"
DS_DECK_NAME = "J. Edgar"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Kinsey dested Aaron Kinsey. "
    "Username blank. LIGHT/DARK boxes empty dest Light from the 60s. "
    "Deck Name Y4: Albany. Event Name MPC. Analog generate empty. "
    "Do not dest as Aaron Kingery / Aaron Kia. "
    "Yavin 4: Massassi Throne Room dested Yavin 4: Massassi Throne Room. "
    "Luke Skywalker, Jedi Knight True dested Luke Skywalker, Jedi Knight. "
    "Mace Windu, Master Of The Order True dested Mace Windu, Master Of The Order. "
    "Blaster Reflection dested Blaster Deflection. "
    "Luke Skywalker, Strong In The Force True dested Luke Skywalker, Strong In The Force. "
    "Rescue Rangers dested as written. "
    "Wesa Gotta Grand Army dested Wesa Gotta Grand Army x2. "
    "Shield 12 cropped. Unique 60. Shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Aaron Kinsey dested Aaron Kinsey. "
    "Username blank. LIGHT/DARK boxes empty dest Dark from the 60s. "
    "Deck Name J. Edgar. Event Name MPC. Analog generate empty. "
    "Endor Operations / Imperial Outpost dested Endor Operations / Imperial Outpost. "
    "Executor Bunker dested Endor: Bunker. Area dested Avenger. "
    "Thunderer dested Thunderer as written. Do PO dested as written. "
    "Evacuate empty dested Evacuate. "
    "Shield 1 Reactor Terminal crossed Come Here You Big Coward dest replacement True. "
    "Shield 5 Knowledge And Defense crossed Wipe Them Out, All Of Them dest replacement True. "
    "You Cannot Hide Forever True x2 sheet-accurate. "
    "Shield 12 cropped. Unique 60. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Luke's Bionic Hand", True),
    n("Corran Horn"),
    n("Obi-Wan's Journal", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Clash Of Sabers", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Smoke Screen", qty=3),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Sense", qty=3),
    n("Blaster Deflection", qty=2),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Luke's Lightsaber"),
    n("Imperial Atrocity", True, qty=2),
    n("Lucky Shot", True),
    n("Obi-Wan With Lightsaber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Kiffex"),
    n("Leia, Rebel Princess"),
    n("Speak With The Jedi Council", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Tantive IV", True),
    n("Under Attack"),
    n("Jedi Lightsaber", True),
    n("Luke Skywalker, Strong In The Force"),
    n("Home One"),
    n("Admiral Ackbar", True),
    n("Gold Leader In Gold 1", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Threepio With His Parts Showing"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Let The Wookiee Win", True),
    n("Home One: War Room"),
    n("Heading For The Medical Frigate"),
    n("Rescue Rangers", True),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Nabrun Leids"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here"),
    n("Aim High"),
    n("Simple Tricks And Nonsense", True),
    n("Chasm", True),
    n("Ultimatum"),
    n("He Can Go About His Business"),
    n("The Professor", True),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("According To My Design"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Establish Secret Base", True),
    n("Close Call", True),
    n("Admiral Motti", True),
    n("Imperial Stockpile"),
    n("Victory"),
    n("Conquest", True),
    n("Devastator", True),
    n("Kuat Drive Yards", True),
    n("Laser Cannon Battery"),
    n("Flawless Marksmanship", qty=3),
    n("Endor: Bunker"),
    n("Avenger"),
    n("Our First Catch Of The Day", qty=2),
    n("Image Of The Dark Lord", True),
    n("Endor: Landing Platform"),
    n("Nevar Yalnal", qty=2),
    n("Imperial Decree"),
    n("In Range", qty=2),
    n("Imperial Command", qty=2),
    n("Emperor Palpatine"),
    n("Thunderer"),
    n("Endor Shield", True),
    n("They've Shut Down The Main Reactor", qty=3),
    n("Relentless Pursuit", qty=3),
    n("Sense"),
    n("Evacuate"),
    n("Do PO"),
    n("Intensify The Forward Batteries", qty=3),
    n("Masterful Move"),
    n("Grand Admiral Thrawn"),
    n("Tractor Beam", qty=2),
    n("Ominous Rumors"),
    n("Endor"),
    n("Naboo"),
    n("Nal Hutta"),
    n("Kessel"),
    n("Control"),
    n("I Can't Shake Him!", qty=2),
    n("Twi'lek Advisor"),
    n("Ghhhk"),
    n("Admiral Chiraneau"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward", True),
    n("You Cannot Hide Forever", True, qty=2),
    n("Secret Plans"),
    n("Do They Have A Code Clearance", True),
    n("Wipe Them Out, All Of Them", True),
    n("Allegations Of Corruption"),
    n("Oppressive Enforcement"),
    n("Imperial Detention"),
    n("Resistance"),
    n("Leave Them To Me"),
]
DS_ADD = []
