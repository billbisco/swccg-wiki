#!/usr/bin/env python3
"""2013 World Championship Day 2: Justin Desai Xerox DS Walkers + LS MWYHL p31."""
from __future__ import annotations

PLAYER = "Justin Desai"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 31
DS_PAGE = 30
LS_SCAN = "2013 Worlds Day 2 p31 Justin Desai LS.png"
DS_SCAN = "2013 Worlds Day 2 p30 Justin Desai DS.png"
LS_PUBLIC_NOTE = (
    "Name box on the Day 2 Light sheet is blank. Deck Name is Same as Yest."
)
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name/Username/Email blank. "
    "Deck Name Same as Yest (two-line scribble). Event Name Worlds. "
    "LIGHT and DARK both unchecked; dest Light from MWYHL/SYTC. "
    "Dest Justin Desai (adjacent p30 Dark Walkers). "
    "MWYHL/SYTC dested Mind What You Have Learned / Save You It Can. "
    "Strong is Vader dested Strong Is Vader. "
    "AFA dested Anger, Fear, Aggression. "
    "Battle plan / DTF dested Battle Plan & Draw Their Fire. "
    "Do or do not / WA dested Do, Or Do Not & Wise Advice. "
    "It is the Future dested It Is The Future You See (Epic Event in the 60). "
    "Strike force dested Strikeforce. "
    "Republic gunship wing dested Republic Gunship Wing. "
    "Obi wan Kenobi JK dested Obi-Wan Kenobi, Jedi Knight. "
    "Artoo in R5 dested Artoo-Detoo In Red 5. "
    "HCF dested Heading For The Medical Frigate. "
    "Master Qui gon dested Master Qui-Gon. "
    "Qui Gon's Lightsaber dested Qui-Gon's Lightsaber. "
    "Line 21 Escape pod struck, wookiee win dested Let The Wookiee Win. "
    "Jedi lightsaber dested Jedi Lightsaber. "
    "Luke SITF dested Luke Skywalker, Strong In The Force. "
    "Luke Skywalker JK dested Luke Skywalker, Jedi Knight. "
    "AJR dested A Jedi's Resilience. "
    "Mech Failure dested Mechanical Failure. "
    "Surprise Assault dested Surprise Assault. "
    "Weapon lev dested Weapon Levitation. "
    "Form left column reprints 37-38 on lines 39-40: "
    "weesa got a grand A dested Wesa Gotta Grand Army; "
    "let the wookiee win dested Let The Wookiee Win. "
    "Mace Windu MOTO dested Mace Windu, Master Of The Order. "
    "Honor of the Jedi dested Honor Of The Jedi. "
    "Naboo battle plains dested Naboo: Battle Plains. "
    "Careful Planning dested Careful Planning. "
    "Lady Luck dested Lady Luck. "
    "Planetary Defenses dested Planetary Defenses. "
    "Y Insight Serves dested Your Insight Serves You Well. "
    "He can go dested He Can Go About His Business. "
    "Additional Your Insight dested Your Insight Serves You Well. "
    "Additional tests 1-6 dested the six Jedi Tests. "
    "Unique overcounts sheet-accurate: Luke SITF x3, Mace Windu x2 + MOTO, "
    "Let The Wookiee Win x4, Escape Pod x3, Houjix x2. "
    "Form left column reprints 37-38 on lines 39-40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Desai. Event box Justin. "
    "Username blank. Deck title Walkers. DARK. "
    "Imperial Occupation/IC dested Imperial Occupation / Imperial Control. "
    "Line 3 struck omitted; margin He Will Die For You dested as written. "
    "A dark time dested A Dark Time For The Rebellion. "
    "We're in attk pos dested We're In Attack Position Now. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "You May Start Your dested You May Start Your Landing. "
    "Blizz Leader dested Commander Igar. "
    "Hoth: Main Power gen dested Hoth: Main Power Generators (1st Marker). "
    "Hoth: Defensive Perim dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth Ice Plains dested Hoth: Ice Plains (5th Marker). "
    "Hoth Mountains dested Hoth: Mountains (6th Marker). "
    "Executor Holotheater dested Executor: Holotheatre. "
    "Dr Evazan / Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Hoth Echo Base dested Hoth: Echo Command Center (War Room). "
    "Wipe Them Out dested Wipe Them Out, All Of Them. "
    "SSB Sector Commander dested ISB Sector Commander. "
    "Lieutenant in Bliz 6 dested Marquand In Blizzard 6. "
    "Image of the DL dested Image Of The Dark Lord. "
    "No Escape dested No Escape. "
    "We'll let fate decide dested We'll Let Fate-a Decide, Huh?. "
    "Form left column reprints 37-38 on lines 39-40. "
    "(V) from the checkbox. Light is Day 2 p31 MWYHL."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Strong Is Vader", True),
    n("Dagobah"),
    n("Anger, Fear, Aggression", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Quick Draw", True),
    n("It Is The Future You See", True),
    n("Strikeforce", True),
    n("Republic Gunship Wing", True, qty=2),
    n("Obi-Wan Kenobi, Jedi Knight"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Heading For The Medical Frigate", True),
    n("Master Qui-Gon", True, qty=2),
    n("Qui-Gon's Lightsaber"),
    n("Escape Pod", True, qty=3),
    n("Let The Wookiee Win", True, qty=4),
    n("Houjix", qty=2),
    n("Jedi Lightsaber", True),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke's Lightsaber"),
    n("A Jedi's Resilience", qty=2),
    n("Corran Horn"),
    n("It Could Be Worse"),
    n("Mechanical Failure", qty=2),
    n("Surprise Assault", True),
    n("Clash Of Sabers"),
    n("Weapon Levitation"),
    n("Wesa Gotta Grand Army"),
    n("Scrambled Transmission", True),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order", True),
    n("Projection Of A Skywalker"),
    n("Sai'torr Kal Fas", True),
    n("Luke's Backpack"),
    n("The Way Of Things"),
    n("Daughter Of Skywalker", True),
    n("Honor Of The Jedi"),
    n("Yoda", True),
    n("Naboo: Battle Plains"),
    n("Dagobah: Yoda's Hut"),
    n("Dagobah: Jungle"),
    n("Dagobah: Bog Clearing"),
    n("Careful Planning", True),
    n("Lady Luck", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Don't Do That Again"),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Planetary Defenses"),
    n("Only Jedi Carry That Weapon"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business", True),
]
LS_ADD = [
    n("Chasm", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well"),
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
]

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Cold Feet", True),
    n("He Will Die For You", True),
    n("A Dark Time For The Rebellion", True),
    n("Darth Maul With Lightsaber"),
    n("Imperial Decree", True),
    n("Stop Motion", True),
    n("We're In Attack Position Now", qty=2),
    n("Blizzard 4"),
    n("AT-AT Cannon", True),
    n("Imperial Artillery"),
    n("Imperial Command"),
    n("Jango Fett, The Assassin"),
    n("Flagship Executor"),
    n("Trample"),
    n("Mara Jade With Lightsaber", True),
    n("Ni Chuba Na??", True),
    n("Knowledge And Defense", True),
    n("Endor Shield", True),
    n("You May Start Your Landing", True),
    n("Imperial Decree"),
    n("Imperial Arrest Order"),
    n("Hoth"),
    n("Commander Igar", True),
    n("Grand Admiral Thrawn"),
    n("Conquest", True),
    n("Hoth: Main Power Generators (1st Marker)"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Darth Vader With Lightsaber"),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Blizzard 1"),
    n("Hoth: Mountains (6th Marker)"),
    n("Executor: Holotheatre"),
    n("Grand Moff Tarkin", True),
    n("Blizzard 2"),
    n("Dr. Evazan & Ponda Baba", True),
    n("Victory"),
    n("Target The Main Generator"),
    n("Alert My Star Destroyer!"),
    n("Hoth: Echo Command Center (War Room)", True),
    n("A Dark Time For The Rebellion", True),
    n("Wipe Them Out, All Of Them", True),
    n("Garindan", True),
    n("Admiral Chiraneau"),
    n("ISB Sector Commander", True),
    n("Blizzard 2", True),
    n("Grand Moff Tarkin", True),
    n("Marquand In Blizzard 6"),
    n("Tempest 1"),
    n("General Veers", True),
    n("Force Push", True),
    n("Imperial Command"),
    n("A Dark Time For The Rebellion", True),
    n("Flagship Executor"),
    n("Emperor Palpatine", True),
    n("Prepared Defenses", True),
    n("Veers"),
    n("Image Of The Dark Lord", True),
    n("No Escape"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Resistance"),
    n("Allegations Of Corruption"),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
]
DS_ADD = [
    n("Battle Order"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("A Useless Gesture"),
]
