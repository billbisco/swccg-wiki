#!/usr/bin/env python3
"""2013 World Championship Day 2: Matthew Harrison-Trainor typed WYS + Walkers."""
from __future__ import annotations

PLAYER = "Matthew Harrison-Trainor"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 42
DS_PAGE = 43
LS_SCAN = "2013 Worlds Day 2 p42 Matthew Harrison-Trainor LS.png"
DS_SCAN = "2013 Worlds Day 2 p43 Matthew Harrison-Trainor DS.png"
LS_NOTE = (
    "Typed 2013 Print Form (15 shields, Jedi Tests empty, Hidden Fortress empty). "
    "Name Matt HT. Username blank. Deck title WYS V. LIGHT. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough. "
    "Evac Control dested Evacuation Control. "
    "Luke, JK dested Luke Skywalker, Jedi Knight. "
    "Nase, MOTO dested Mace Windu, Master Of The Order. "
    "Maris Brood dested Maris Brood, Fallen Jedi. "
    "Yoda, GW dested Yoda, Great Warrior. "
    "Captain Han dested Captain Han Solo. "
    "Wedge, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Landrie a dested Lando Calrissian. "
    "Romas Lock Navander dested Romas 'Lock' Navander. "
    "Palejo dested Palejo Reshad. "
    "Bruckman dested Sergeant Bruckman. "
    "Crix Madine dested General Crix Madine. "
    "Lando, UH dested Lando Calrissian, Unlikely Hero. "
    "Leia, RP dested Leia, Rebel Princess. "
    "Jedi Luke dested Luke Skywalker. "
    "Obi in Red 7 dested Obi-Wan In Radiant VII. "
    "CEC dested Corellian Engineering Corporation. "
    "Corellian Retro dested Corellian Retort. "
    "Antilles Maneuver + Rebel Reinf dested Antilles Maneuver & Rebel Reinforcements. "
    "Insurrection + Aim High dested Insurrection & Aim High. "
    "All Wings Report In + Dark Spin dested All Wings Report In & Darklighter Spin. "
    "Honor and OTJ dested Honor Of The Jedi. "
    "AFA dested Anger, Fear, Aggression. "
    "Line 55 empty (59 in the 60). "
    "Jabba's Prize in the shield box dested the character. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Typed 2013 Print Form (15 shields, Jedi Tests empty, Hidden Fortress empty). "
    "Name Matt HT. Username blank. Deck title Walkers. DARK. "
    "IO/IC dested Imperial Occupation / Imperial Control. "
    "ADTFTR dested A Dark Time For The Rebellion. "
    "HHCBY dested He Hasn't Come Back Yet. "
    "TTMG dested Target The Main Generator. "
    "WIAPN dested We're In Attack Position Now. "
    "MM + EO dested Masterful Move & Endor Occupation. "
    "GHT dested Grand Moff Tarkin. "
    "Jango Fett, The Assassin dested Jango Fett, The Assassin. "
    "Maarek Stele dested Maarek Stele, The Emperor's Reach. "
    "Comm Igar dested Commander Igar. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "DTHACC dested Do They Have A Code Clearance?. "
    "YMSYL dested You May Start Your Landing. "
    "Hoth Mountains dested Hoth: Mountains (6th Marker). "
    "Imp Decree dested Imperial Decree. "
    "General Nevas dested General Nevar. "
    "Juno Eclipse, BL dested Juno Eclipse, Black Leader. "
    "Marquand in Blizz 6 dested Marquand In Blizzard 6. "
    "Image of the Dark Lord dested Image Of The Dark Lord. "
    "Hoth: Ice Plains dested Hoth: Ice Plains (5th Marker). "
    "Hoth: MPG dested Hoth: Main Power Generators (1st Marker). "
    "Hoth: Def Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "K+D dested Knowledge And Defense. "
    "YCHF dested You Cannot Hide Forever. "
    "DS Sentry dested Death Star Sentry. "
    "We'll Let Fate-a Decide dested We'll Let Fate-a Decide, Huh?. "
    "Imp Detention dested Imperial Detention. "
    "After Her dested After Her!. "
    "Opp Enf dested Oppressive Enforcement. "
    "Hoth Blockade dested Hoth Blockade. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Evacuation Control", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("It's A Trap"),
    n("Antilles Maneuver", True, qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Maris Brood, Fallen Jedi"),
    n("Yoda, Great Warrior"),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("No Questions Asked", True, qty=3),
    n("Punch It!"),
    n("Rebel Barrier", qty=2),
    n("Heading For The Medical Frigate"),
    n("Corran Horn"),
    n("Dash Rendar", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Lando Calrissian", True),
    n("Romas 'Lock' Navander"),
    n("Mirax Terrik"),
    n("Palejo Reshad"),
    n("Sergeant Bruckman"),
    n("General Crix Madine"),
    n("Chewie", True, qty=3),
    n("Padme Naberrie", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Leia, Rebel Princess", qty=2),
    n("Seeking An Audience", True),
    n("Luke Skywalker"),
    n("Obi-Wan In Radiant VII"),
    n("Tantive IV", True),
    n("Corellia", True),
    n("Spaceport Scoundrels Guild"),
    n("Home One: Docking Bay"),
    n("Spaceport City"),
    n("Spaceport Street"),
    n("Spaceport Docking Bay"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("Wokling", True),
    n("Corellian Retort", True, qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Imperial Atrocity"),
    n("Desperate Reach"),
    n("Honor Of The Jedi"),
    n("Corellian Slip", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not"),
    n("Jabba's Prize", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display"),
    n("Chasm"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Prepared Defenses", True),
    n("Force Push", True, qty=2),
    n("Blizzard 2"),
    n("Stop Motion", True, qty=2),
    n("Victory", qty=2),
    n("Conquest", True),
    n("Garindan"),
    n("He Hasn't Come Back Yet"),
    n("Target The Main Generator"),
    n("Admiral Piett"),
    n("We're In Attack Position Now", qty=2),
    n("Imperial Command", qty=3),
    n("Masterful Move & Endor Occupation"),
    n("Control"),
    n("Grand Moff Tarkin", True),
    n("Jango Fett, The Assassin"),
    n("Grand Admiral Thrawn"),
    n("Walker Garrison"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Blizzard 1", True),
    n("No Escape"),
    n("Trample", qty=2),
    n("Blizzard 4", qty=2),
    n("Cold Feet", True),
    n("Commander Igar", True),
    n("Ni Chuba Na??", True),
    n("Do They Have A Code Clearance?"),
    n("Endor Shield", True),
    n("You May Start Your Landing", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Imperial Decree"),
    n("General Nevar"),
    n("Juno Eclipse, Black Leader"),
    n("Flagship Executor"),
    n("Tempest 1"),
    n("Veers", True),
    n("AT-AT Cannon", True),
    n("Marquand In Blizzard 6"),
    n("Image Of The Dark Lord", True),
    n("AT-AT Commander"),
    n("Hoth Blockade"),
    n("Hoth: Ice Plains (5th Marker)"),
    n("U-3PO (Yoo-Threepio)"),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Hoth"),
    n("Garindan", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("Imperial Detention", True),
    n("After Her!", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Firepower", True),
    n("Battle Order"),
    n("Abyss", True),
    n("A Useless Gesture"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
