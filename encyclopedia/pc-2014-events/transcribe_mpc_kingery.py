#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Aaron Kingery.

Source: MPC-2014-Day-1-Main-Event.pdf pages 63–64 (2013 form, 15 shields).
Name Aaron Kingery dested as written from the Name box. Username blank.
Dark Separatist Uprising. Light Yavin 4.
"""
from __future__ import annotations

PLAYER = "Aaron Kingery"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 64
DS_PAGE = 63
LS_SCAN = "2014 Match Play Championship Day 1 Aaron Kingery LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Aaron Kingery DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Aaron Kingery dested as written. Username blank. "
    "LIGHT checked. Yavin 4 dested Yavin 4 (V). Jawiq Se'ol dested Jawiq Se'ol. "
    "Luke Trust Me dested Trust Me (V). Restore Freedom dested Restore Freedom To The Galaxy (V). "
    "Antilles Maneuver & Rebel Barrier dested Antilles Maneuver & Rebel Reinforcements (V). "
    "(V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Aaron Kingery dested as written. Username blank. "
    "Separatist Uprising dested Separatist Uprising / At War With Itself. Virtual-only "
    "objective dested without (V). Dom-9 dested OOM-9 (V). Along With Concussion dested "
    "4-LOM With Concussion Rifle (V). Dread Pact dested Dread Pact (V). "
    "Mara Jade Endor Occupant dested Mara Jade, The Emperor's Hand. "
    "The Mandalorian Father Of Fett dested The Mandalorian, Father Of Fett (V). "
    "Muunilinst: City Of Hearts dested Muunilinst: City Of Harnaidan (V). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4"
LS_CARDS = [
    n("Yavin 4", True),
    n("Kiffex"),
    n("Jawiq Se'ol"),
    n("Rogue Squadron X-Wing", True, qty=2),
    n("Red 6"),
    n("Red 7"),
    n("Rebel Aces", True),
    n("Kier Santage"),
    n("S-foils", True),
    n("Control & Tunnel Vision"),
    n("Trust Me", True),
    n("Restore Freedom To The Galaxy", True),
    n("Outrider"),
    n("Organized Attack", qty=2),
    n("Millennium Falcon", True),
    n("Luke Skywalker"),
    n("Yavin 4: Massassi Ruins"),
    n("Yavin 4: Massassi War Room", True),
    n("Rebel Barrier"),
    n("Projection Of A Skywalker", qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Wokling", True),
    n("X-Wing Laser Cannon"),
    n("Massassi Base Sentry", True),
    n("Jek Porkins", True),
    n("Squadron Assignments"),
    n("All Wings Report In & Darklighter Spin"),
    n("Imperial Atrocity"),
    n("Let The Wookiee Win", True, qty=2),
    n("Legendary Starfighter"),
    n("Captain Han Solo"),
    n("Booster In Pulsar Skate"),
    n("Corran Horn", True),
    n("Artoo-Detoo In Red 5"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Honor Of The Jedi"),
    n("Nar Shaddaa", True),
    n("Undercover", True),
    n("Flash Of Insight", True),
    n("Undercover"),
    n("Escape Pod", True),
    n("Imperial Atrocity", True),
    n("I'll Take The Leader"),
    n("Houjix & Out Of Nowhere"),
    n("Double Agent", qty=2),
    n("Dash Rendar", True),
    n("Haven"),
    n("Gold Leader In Gold 1", True),
    n("Corran Horn"),
    n("Commander Vanden Willard", True),
    n("Chewie", True),
    n("Careful Planning", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Lando's Luxury Yacht", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again"),
    n("Chasm", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Aim High", True),
    n("Wise Advice", True),
]
LS_ADD = []


DS_START = "Separatist Uprising / At War With Itself"
DS_CARDS = [
    n("Separatist Uprising / At War With Itself"),
    n("Imperial Propaganda", True),
    n("Imperial Artillery", qty=4),
    n("Defense Of Muunilinst", True),
    n("OOM-9", True),
    n("4-LOM With Concussion Rifle", True),
    n("Cold Feet", True),
    n("Dread Pact", True),
    n("Operational As Planned", True),
    n("Heavy Fire Zone", qty=2),
    n("AAT With Rockets"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("AAT Assault Leader"),
    n("Maul's Sith Infiltrator", qty=3),
    n("Imperial Barrier", qty=3),
    n("AAT Laser Cannon", qty=3),
    n("Mara Jade, The Emperor's Hand"),
    n("Sneak Attack", True),
    n("Outflank", True, qty=2),
    n("Self-Destruct Mechanism", True, qty=2),
    n("Armored Attack Tank", qty=3),
    n("Tank Commander", qty=3),
    n("U-3PO"),
    n("There They Are"),
    n("Ni Chuba Na??", True),
    n("The Mandalorian, Father Of Fett", True),
    n("Captain Tarpals"),
    n("Darth Maul", qty=2),
    n("Muunilinst: City Of Harnaidan", True),
    n("Muunilinst: Harnaidan Plains", True),
    n("Coruscant: Separatist Council", True),
    n("OOM-9", True),
    n("Protocol Failure", True),
    n("Everything Is Going As Planned", True),
    n("The War Has Begun", True),
    n("Lightsaber Deficiency", True),
    n("Deployment"),
    n("3P8-SSC"),
    n("783-10JY"),
    n("Battlefield Arena"),
    n("Master Separatist Council"),
    n("Captain Needa"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Fanfare"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Reactor Terminal", True),
    n("You Cannot Hide Forever", True),
    n("Leave Them To Me", True),
    n("Wipe Them Out, All Of Them", True),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("A Useless Gesture"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
]
DS_ADD = []
