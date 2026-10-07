#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Matt Sokol.

Source: Nationals-2014-day-1.pdf pages 7–8 (2010 form).
Name Sokol. Username blank. Dest Matt Sokol.
"""
from __future__ import annotations

PLAYER = "Matt Sokol"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 7
DS_PAGE = 8
LS_SCAN = "2014 US Nationals Day 1 p07 Matt Sokol LS.png"
DS_SCAN = "2014 US Nationals Day 1 p08 Matt Sokol DS.png"
NOTE = "Handwritten 2010 Xerox. Name Sokol dested Matt Sokol."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Sokol. Username blank. Deck name Light. "
    "Restore Freedom dested Restore Freedom To The Galaxy. "
    "AM & R. Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "POS dested Projection Of A Skywalker. LTWW dested Let The Wookiee Win. "
    "Control & TV dested Control & Tunnel Vision. AWR & DS dested All Wings Report In & Darklighter Spin. "
    "GL in G1 dested Gold Leader In Gold 1. Lando UH dested Lando Calrissian, Unlikely Hero. "
    "AFA dested Anger, Fear, Aggression. 15 Shields written, no individual shields. "
    "Unique overcounts sheet-accurate (Let The Wookiee Win x2, Rebel Barrier x4, "
    "All Wings Report In & Darklighter Spin x3, Outrider x2, Projection Of A Skywalker x2, "
    "Organized Attack x2, Imperial Atrocity x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Sokol. Username blank. Deck name Dark. "
    "Endor Ops dested Endor Operations / Imperial Outpost. "
    "Endor: DB dested Endor: Landing Platform (Docking Bay). "
    "YCFTF & TRWEU dested You Can Follow Them & Those Rebel Pilots. "
    "SRF & WYB dested Short Range Fighters & Watch Your Back!. "
    "ADTFTB dested A Dark Time For The Rebellion. ESB dested Establish Control. "
    "Slave I, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Hound's Tooth dested Hound's Tooth. Rogue Shadow dested Rogue Shadow. "
    "Mist Hunter dested Mist Hunter. Cyclone Walker dested Cyclone Walker. "
    "K+D dested Knowledge And Defense. 15 Shields written, no individual shields. "
    "Unique overcounts sheet-accurate (AT-AT Deployment Platform x2, Imperial Propaganda x2, "
    "Close Call x2, Short Range Fighters & Watch Your Back! x3, Battle Deployment x3, "
    "Fighters Coming In x2, Garindan x2, Cyclone Walker x3). (V) from checkbox. "
    "NO_DEST (2014 index): You Can Follow Them & Those Rebel Pilots; Line In The Sand (V); "
    "Daut Nund (V); General Nune."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Restore Freedom To The Galaxy"
LS_CARDS = [
    n("Yavin 4"),
    n("Yavin 4: Massassi Headquarters"),
    n("Luke's T-16 Skyhopper"),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("Careful Planning", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Projection Of A Skywalker"),
    n("Let The Wookiee Win", True),
    n("Imperial Atrocity", True),
    n("Red 6"),
    n("Let The Wookiee Win", True),
    n("Rebel Barrier"),
    n("Dash Rendar", True),
    n("Legendary Starfighter"),
    n("Haven"),
    n("Control & Tunnel Vision"),
    n("Massassi Base Sentry"),
    n("Red Squadron 4"),
    n("Organized Attack"),
    n("S-foils", True),
    n("Escape Pod", True),
    n("Red Squadron 1", True),
    n("Jek Porkins", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Jaina Solo"),
    n("Biggs Darklighter", True),
    n("Rogue Squadron X-wing"),
    n("X-wing Laser Cannon"),
    n("Chewbacca", True),
    n("Rebel Barrier"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Captain Han Solo"),
    n("Tycho Celchu"),
    n("Millennium Falcon", True),
    n("Outrider", True, qty=2),
    n("Lady Luck"),
    n("Nar Shaddaa"),
    n("Rebel Barrier"),
    n("Artoo-Detoo In Red 5"),
    n("Corran Horn"),
    n("Luke Skywalker", True),
    n("Derek 'Hobbie' Klivian", True),
    n("Tatooine"),
    n("Kessel"),
    n("Lieutenant Blount"),
    n("Red 3", True),
    n("Imperial Atrocity", True),
    n("Gold Leader In Gold 1"),
    n("Projection Of A Skywalker"),
    n("Houjix"),
    n("Restore Freedom To The Galaxy"),
    n("Yavin 4: Massassi War Room", True),
    n("Rebel Barrier"),
    n("Organized Attack"),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = []
LS_ADD = []


DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Forest Clearing"),
    n("Endor: Back Door"),
    n("Kessel"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Bunker"),
    n("AT-AT Deployment Platform", qty=2),
    n("Ominous Rumors"),
    n("Fleet Security Protocols"),
    n("Protocol Failure"),
    n("Imperial Propaganda", True, qty=2),
    n("Combat Response"),
    n("Establish Control", True),
    n("Endor Shield", True),
    n("You Can Follow Them & Those Rebel Pilots"),
    n("According To My Design"),
    n("Close Call", True, qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("A Dark Time For The Rebellion", True),
    n("Force Push", True),
    n("Line In The Sand", True),
    n("Battle Deployment", qty=3),
    n("Fighters Coming In", qty=2),
    n("Emperor Palpatine"),
    n("Black 2"),
    n("Daut Nund", True),
    n("4-LOM", True),
    n("Bossk", True),
    n("Baron Soontir Fel"),
    n("Admiral Ozzel"),
    n("General Nune"),
    n("U-3PO (Yoo-Threepio)"),
    n("Boba Fett"),
    n("Garindan", True, qty=2),
    n("Arica"),
    n("General Veers", True),
    n("Dengar", True),
    n("IG-88"),
    n("Darth Vader", True),
    n("Slave I, Symbol Of Fear"),
    n("Dengar In Punishing One", True),
    n("Vader's Personal Shuttle", True),
    n("Hound's Tooth"),
    n("Rogue Shadow", True),
    n("Mist Hunter"),
    n("Slave I", True),
    n("Cyclone Walker", qty=3),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = []
DS_ADD = []
