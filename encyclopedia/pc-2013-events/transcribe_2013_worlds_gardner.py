#!/usr/bin/env python3
"""2013 World Championship Day 1: Jeremy Gardner Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Jeremy Gardner"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Worlds Day 1.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2013 Worlds Day 1 p03 Jeremy Gardner LS.png"
DS_SCAN = "2013 Worlds Day 1 p04 Jeremy Gardner DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Jeremy Gardner. Username blank. "
    "Event Day 1 Worlds '13. Deck title Like a Virgin. LIGHT/DARK boxes empty; "
    "Hidden Base is Light. "
    "Hidden Base / Systems will slip dested Hidden Base / Systems Will Slip Through Your Fingers. "
    "Heading For The Med Frigat dested Heading For The Medical Frigate. "
    "Mace Windu, MOTO dested Mace Windu, Master Of The Order. "
    "Incom Corp combo dested Incom Corporation & Koensayr Manufacturing. "
    "Sorry about the mess combo dested Sorry About The Mess & Blaster Proficiency. "
    "GL in G1 dested Gold Leader In Gold 1. "
    "Wedge in RS1 dested Wedge In Red Squadron 1. "
    "Army Put Your Weapon dested Away Put Your Weapon. "
    "Houjix combo dested Houjix & Out Of Nowhere. AFA dested Anger, Fear, Aggression. "
    "General Rieekan dested General Carlist Rieekan. "
    "HCFE dested as written. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Jeremy Gardner. Username blank. "
    "Event Day 1 Worlds '13. Deck title Qualifying for the very first time. "
    "LIGHT/DARK boxes empty; Imperial Entanglements is Dark. "
    "Imperial Entanglements / NO one to stop dested Imperial Entanglements / No One To Stop Us This Time. "
    "Commander Brafi dested Commander Praji. "
    "We Have a Prisoner combo dested We Have A Prisoner & I Can't Shake Him!. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Lt Gerrad dested Lieutenant Grond. "
    "Guriadan dested Guri. EED dested Expand The Empire. "
    "Kir Kanos w/ Force Pike dested Kir Kanos With Force Pike. "
    "Captain Godheart dested Captain Godherdt. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers", True),
    n("Uncharted Settlements"),
    n("Tatooine"),
    n("Rebel Cell - Hidden Landing Site"),
    n("Heading For The Medical Frigate"),
    n("Dual Laser Cannon", True),
    n("Rebel Gunrunner"),
    n("Insurrection", True),
    n("A Good Blaster At Your Side"),
    n("Mace Windu, Master Of The Order"),
    n("Lando Calrissian, Scoundrel", True),
    n("Desperate Tactics"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Mos Eisley"),
    n("Rebel Cell - Perimeter"),
    n("Rebel Cell - Monitoring Station"),
    n("Artillery Remote"),
    n("Corporal Beezer"),
    n("General Carlist Rieekan", True),
    n("Medium Repeating Blaster Cannon", qty=2),
    n("Attack Pattern Delta", True),
    n("Attack Pattern Delta"),
    n("Veteran Rogue"),
    n("Incom Corporation & Koensayr Manufacturing"),
    n("Tantive IV", True),
    n("Maneuvering Flaps"),
    n("It's Not My Fault!", True),
    n("Dash In Rogue 10"),
    n("Portable Scanner"),
    n("Medium Repeating Blaster Cannon"),
    n("Combined Fleet Action"),
    n("Return Of The Jedi"),
    n("Tatooine Celebration"),
    n("Veteran Rogue"),
    n("Desperate Tactics"),
    n("Sand Speeder"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Gold Leader In Gold 1", True),
    n("Bright Hope", True),
    n("Planet Defender Ion Cannon", True),
    n("Spiral"),
    n("Luke Skywalker, Jedi Knight"),
    n("Sand Speeder"),
    n("Ben Kenobi"),
    n("Imperial Atrocity", True),
    n("Veteran Rogue"),
    n("Qui-Gon With Lightsaber"),
    n("Republic Gunship Wing"),
    n("Corran Horn"),
    n("Away Put Your Weapon", True),
    n("Tatooine Celebration"),
    n("Sand Speeder"),
    n("Wedge In Red Squadron 1"),
    n("Sand Speeder"),
    n("HCFE", True),
    n("Desperate Tactics"),
    n("Republic Gunship Wing"),
    n("Houjix & Out Of Nowhere"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum", True),
    n("The Professor", True),
    n("Wise Advice"),
    n("Affect Mind", True),
]
LS_ADD = [
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon"),
]


DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("Imperial Entanglements / No One To Stop Us This Time"),
    n("Tatooine"),
    n("Tatooine: Imperial Vanguard Camp"),
    n("Devastator"),
    n("Surface Defense", True),
    n("Admiral Piett"),
    n("We Have A Prisoner & I Can't Shake Him!"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Captain Godherdt"),
    n("Grand Admiral Thrawn", True),
    n("Commander Praji", True),
    n("Commander Desanne"),
    n("Tatooine Occupation"),
    n("Tatooine: Tusken Canyon"),
    n("Imperial Arrest Order"),
    n("Mara Jade With Lightsaber"),
    n("Admiral Ozzel"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Tatooine: Desert Heart"),
    n("Sandwhirl"),
    n("We're In Attack Position Now"),
    n("We Have A Prisoner & I Can't Shake Him!"),
    n("Imperial Commander"),
    n("Dreadnaught-Class Heavy Cruiser"),
    n("Executor"),
    n("We're In Attack Position Now"),
    n("Blizzard Scout 1", True),
    n("ISB Sector Commander"),
    n("General Nevar"),
    n("Kir Kanos With Force Pike"),
    n("Tatooine: Desert"),
    n("Sergeant Barich"),
    n("Admiral Chiraneau"),
    n("Tatooine: Jundland Wastes"),
    n("Grand Moff Tarkin", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Destroyed Homestead"),
    n("Tatooine Occupation"),
    n("Sergeant Irol", True),
    n("AT-AT Commander"),
    n("Tatooine Occupation"),
    n("Deflector Shield Generators", True),
    n("Tempest Scout 6"),
    n("We Have A Prisoner & I Can't Shake Him!"),
    n("Ysanne Isard"),
    n("We Have A Prisoner & I Can't Shake Him!"),
    n("Imperial Commander"),
    n("Lieutenant Grond", True),
    n("Imperial Commander"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Guri", True),
    n("Commander Daine Jir"),
    n("Dreadnaught-Class Heavy Cruiser"),
    n("Commander Merrejk"),
    n("We're In Attack Position Now"),
    n("Tatooine: Desert"),
    n("Tempest Scout 5"),
    n("Commander Nemet", True),
    n("Dreadnaught-Class Heavy Cruiser"),
    n("Expand The Empire", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Abyss", True),
    n("Weapon Of A Sith"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Fanfare"),
    n("A Useless Gesture", True),
]
DS_ADD = [
    n("Do They Have A Code Clearance?", True),
    n("Imperial Detention"),
    n("There Is No Try"),
]
