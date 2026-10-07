#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Matt Schmaltz Xerox LS+DS.

Name field Schwartz. Username dashmudtz is Matt Schmaltz
(2014 Philadelphia Premiere Event Matt Schmaltz LS EBO).
"""
from __future__ import annotations

PLAYER = "Matt Schmaltz"
USERNAME = "dashmudtz"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 79
DS_PAGE = 80
LS_SCAN = "2013 Match Play Championship p79 Schwartz LS.png"
DS_SCAN = "2013 Match Play Championship p80 Schwartz DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Schwartz. Username dashmudtz. Light. "
    "Deck title Restore horrible decks to the MPC. Starting Yavin 4. "
    "Endor Back Door dested Endor: Back Door. Home One War Room dested Home One: War Room. "
    "Yavin 4 Massassi Headquarters dested Yavin 4: Massassi Headquarters. "
    "Yavin 4 Massassi War Room dested Yavin 4: Massassi War Room. "
    "Artoo Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Wedge in Red Squadron 1 dested Wedge In Red Squadron 1. "
    "Chewie dested Chewie, Enraged. Lando Calrissian Scoundrel dested Lando Calrissian, Scoundrel. "
    "Obiwan with Lightsaber dested Obi-Wan With Lightsaber. "
    "Xwing Laser Cannon dested X-wing Laser Cannon. "
    "Concentrate all Fire dested Concentrate All Fire. "
    "Luke Told Me as written. Strike Planning dested Strike Planning. "
    "Strikeforce dested Strikeforce. "
    "All wings report in + Darklighter Spin dested All Wings Report In & Darklighter Spin. "
    "Antilles Maneuver + Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "It's not My Fault dested It's Not My Fault!. Punch It! dested Punch It!. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Another Pathetic Lifeform dested Another Pathetic Lifeform. "
    "Do or Do not dested Do, Or Do Not. Don't Do That Again dested Don't Do That Again. "
    "He Can Go About His Business dested He Can Go About His Business. "
    "Simple Tricks & Nonsense dested Simple Tricks And Nonsense. "
    "Form left column reprints 37–38 on lines 39–40 are Seeking An Audience and Squadron Assignments. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Schwartz. Username dashmudtz. Dark. "
    "Deck title Walkers. Imperial Occupation / Imperial Control. "
    "Target the Main Generator dested Target The Main Generator. "
    "Hoth Main Power Generators dested Hoth: Main Power Generators (1st Marker). "
    "Hoth Mountains dested Hoth: Mountains (6th Marker). "
    "Hoth Ice plains dested Hoth: Ice Plains (5th Marker). "
    "Hoth Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Marquand in Blizzard 6 dested Marquand In Blizzard 6. Teampest 1 dested Tempest 1. "
    "General Veers dested General Veers. Darth Vader dested Darth Vader. "
    "ISB Sector Commander dested ISB Sector Commander. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "We're in attack Position dested We're In Attack Position Now. "
    "Alert My Star Destroyer dested Alert My Star Destroyer!. "
    "Do they have a code clearance dested Do They Have A Code Clearance?. "
    "Endor Shield dested Endor Shield. Well Earned Command dested Well-earned Command. "
    "Wipe them Out All of Them dested Wipe Them Out, All Of Them. "
    "You cannot hide forever + Mob Points dested You Cannot Hide Forever & Mobilization Points. "
    "You May Start Your Landing dested You May Start Your Landing. "
    "A Dark Time For The Rebellion dested A Dark Time For The Rebellion. "
    "Control + Set For Stun dested Control & Set For Stun. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "We'll let Fate Decide huh? dested We'll Let Fate-a Decide, Huh?. "
    "Form left column reprints 37–38 on lines 39–40 are You May Start Your Landing and Scanning Crew. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Yavin 4", True),
    n("Naboo"),
    n("Endor"),
    n("Endor: Back Door"),
    n("Home One: War Room"),
    n("Yavin 4: Massassi Headquarters"),
    n("Yavin 4: Massassi War Room", True),
    n("Restore Freedom To The Galaxy", True),
    n("Artoo-Detoo In Red 5"),
    n("Home One"),
    n("Millennium Falcon", True),
    n("Red 1", True),
    n("Red 6"),
    n("Wedge In Red Squadron 1", True, qty=2),
    n("Admiral Ackbar", True),
    n("Chewie, Enraged", True),
    n("General Dodonna", True),
    n("General Solo", True),
    n("Jek Porkins", True),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker", True),
    n("Obi-Wan With Lightsaber"),
    n("Red Leader"),
    n("Yoda, Great Warrior", True),
    n("X-wing Laser Cannon", qty=2),
    n("Concentrate All Fire"),
    n("Haven"),
    n("Imperial Atrocity", True, qty=3),
    n("Imperial Atrocity"),
    n("Launching The Assault"),
    n("Luke Told Me", True),
    n("Massassi Base Sentry", True),
    n("Projection Of A Skywalker"),
    n("Seeking An Audience", True),
    n("Squadron Assignments"),
    n("Strike Planning"),
    n("Strikeforce", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Careful Planning", True),
    n("Escape Pod", True),
    n("Fallen Portal", qty=2),
    n("Houjix"),
    n("It's Not My Fault!", True, qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Punch It!"),
    n("Rebel Leadership", True, qty=3),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Another Pathetic Lifeform", True),
    n("Battle Plan"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Target The Main Generator"),
    n("Hoth"),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("AT-AT Cannon", True),
    n("Flagship Executor"),
    n("Victory", True),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Marquand In Blizzard 6", True),
    n("Tempest 1"),
    n("Blizzard 4", qty=2),
    n("Admiral Piett"),
    n("Commander Igar"),
    n("General Veers", True),
    n("Darth Vader", True),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True, qty=2),
    n("ISB Sector Commander", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Veers", True),
    n("We're In Attack Position Now", qty=3),
    n("Alert My Star Destroyer!"),
    n("Do They Have A Code Clearance?"),
    n("Endor Shield", True),
    n("Hoth Blockade", True),
    n("Imperial Decree"),
    n("No Escape"),
    n("Well-earned Command", True),
    n("Wipe Them Out, All Of Them", True),
    n("You Cannot Hide Forever & Mobilization Points"),
    n("You May Start Your Landing", True),
    n("Scanning Crew"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Cold Feet", True),
    n("Control & Set For Stun"),
    n("Force Push", True),
    n("Imperial Artillery", qty=5),
    n("Imperial Command", qty=3),
    n("Operational As Planned", True),
    n("Prepared Defenses", True),
    n("Trample", qty=3),
    n("Walker Garrison"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Firepower", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
