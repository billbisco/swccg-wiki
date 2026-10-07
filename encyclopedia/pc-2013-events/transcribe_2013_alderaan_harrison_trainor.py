#!/usr/bin/env python3
"""2013 Alderaan Regionals: Matthew Harrison-Trainor handwritten 2010 Xerox LS+DS.

Name field Matt HT. Username blank. Dest Matthew Harrison-Trainor.
Do not rewrite Worlds / SoCal / MPC Harrison-Trainor leftovers.
"""
from __future__ import annotations

PLAYER = "Matthew Harrison-Trainor"
USERNAME = ""
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2013 Alderaan Regionals p01 Matthew Harrison-Trainor LS.png"
DS_SCAN = "2013 Alderaan Regionals p02 Matthew Harrison-Trainor DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). Name Matt HT. "
    "Username blank. Event Alderaan Regional. LIGHT checked. Deck Name WYSv. "
    "WYS True dested Watch Your Step / This Place Can Be A Little Rough True. "
    "Captain Han dested Captain Han Solo. <> Street / Scoundrel's Guild / City / DB "
    "dested Spaceport Street / Spaceport Scoundrels Guild / Spaceport City / "
    "Spaceport Docking Bay. General Crix dested General Crix Madine. "
    "Romas Navander dested Romas 'Lock' Navander. Mirax dested Mirax Terrik. "
    "Mace MotO dested Mace Windu, Master Of The Order. Maris Brood dested "
    "Maris Brood, Fallen Jedi. Leia RP dested Leia, Rebel Princess. "
    "CEC True dested Corellian Engineering Corporation True. "
    "Insurrection + Aim High dested Insurrection & Aim High. "
    "NQA True then two empty dittos dested No Questions Asked True + two empty. "
    "Casellian Retart dested Corellian Retort. Home One : DB dested "
    "Home One: Docking Bay. Antilles Maneuver + Rebel Ren dested "
    "Antilles Maneuver & Rebel Reinforcements. AWRI + DS dested "
    "All Wings Report In & Darklighter Spin. Wedge RSL dested "
    "Wedge Antilles, Red Squadron Leader. L+WW dested Let The Wookiee Win. "
    "LSJK dested Luke Skywalker, Jedi Knight. Yoda GW dested Yoda, Great Warrior. "
    "Padme Naberrie dested Padme Naberrie. Imp Atrocity dested Imperial Atrocity. "
    "HFTMF dested Heading For The Medical Frigate. Houjix dested Houjix. "
    "AFA dested Anger, Fear, Aggression. Ditto checkboxes that differ from the "
    "first named line kept as separate True/empty copies. Additional: Chasm True, "
    "Wise Advice empty, Your ISYW crossed Affect Mind dested Affect Mind empty."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). Name Matt HT. "
    "Username blank. Event Alderaan Regional. Deck Name Walkers. "
    "IO/IC True dested Imperial Occupation / Imperial Control True. "
    "Ni Chuba Na True dested Ni Chuba Na? True. YMSYL dested You May Start Your Landing. "
    "DTHACC dested Do They Have A Code Clearance?. GA Thrawn dested Grand Admiral Thrawn. "
    "Victory dested Victory as written. Hoth: MPG dested "
    "Hoth: Main Power Generators (1st Marker). Hoth: Ice Plains dested "
    "Hoth: Ice Plains (5th Marker). Hoth: Mountains dested "
    "Hoth: Mountains (6th Marker). Hoth: Defensive Perimeter dested "
    "Hoth: Defensive Perimeter (3rd Marker). WIAPN dested We're In Attack Position Now. "
    "MM + EO dested Masterful Move & Endor Occupation. ADTFTR dested "
    "A Dark Time For The Rebellion. GMT dested Grand Moff Tarkin. "
    "HHCBY dested He Hasn't Come Back Yet. Maarek Stele dested "
    "Maarek Stele, The Emperor's Reach. Gen Nevar dested General Nevar. "
    "Juno Eclipse dested Juno Eclipse, Black Leader. Darth Vader True dested "
    "Darth Vader, Dark Lord Of The Sith True. K+D dested Knowledge And Defense. "
    "YCHF dested You Cannot Hide Forever. Opp Enforcement dested Oppressive Enforcement. "
    "Coward dested Come Here You Big Coward. Ditto checkboxes that differ kept separate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Chewie", True),
    n("Corellia", True),
    n("Spaceport Street"),
    n("Spaceport Scoundrels Guild", True),
    n("Spaceport City"),
    n("Spaceport Docking Bay"),
    n("General Crix Madine"),
    n("Romas 'Lock' Navander"),
    n("Mirax Terrik"),
    n("Mace Windu, Master Of The Order"),
    n("Dash Rendar", True),
    n("Dash Rendar"),
    n("Maris Brood, Fallen Jedi"),
    n("Leia, Rebel Princess", qty=2),
    n("Palejo Reshad"),
    n("Tantive IV", True),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("No Questions Asked", True),
    n("No Questions Asked", qty=2),
    n("It's A Trap", qty=2),
    n("Punch It!"),
    n("Grimtaash"),
    n("Wokling", True),
    n("Corellian Retort", True),
    n("Corellian Retort"),
    n("Home One: Docking Bay"),
    n("Laudica", True),
    n("Rebel Barrier", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Corran Horn"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Seeking An Audience", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Spiral"),
    n("Yoda, Great Warrior"),
    n("Escape Pod", True),
    n("Escape Pod"),
    n("Sergeant Bruckman"),
    n("Padme Naberrie", True),
    n("Imperial Atrocity", True),
    n("Heading For The Medical Frigate"),
    n("Antilles Maneuver", True),
    n("Houjix"),
    n("Lady Luck"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Do, Or Do Not"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display"),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Jabba's Prize", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = [
    n("Chasm", True),
    n("Wise Advice"),
    n("Affect Mind"),
]

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Ni Chuba Na?", True),
    n("Imperial Decree"),
    n("You May Start Your Landing", True),
    n("Endor Shield", True),
    n("Do They Have A Code Clearance?"),
    n("Hoth"),
    n("Grand Admiral Thrawn"),
    n("Victory", qty=2),
    n("Hoth: Ice Plains (5th Marker)"),
    n("Hoth: Main Power Generators (1st Marker)"),
    n("Hoth: Mountains (6th Marker)"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Force Push", True),
    n("Force Push"),
    n("Walker Garrison"),
    n("Prepared Defenses", True),
    n("We're In Attack Position Now"),
    n("Masterful Move & Endor Occupation"),
    n("U-3PO (Yoo-Threepio)"),
    n("Tempest 1"),
    n("AT-AT Cannon", True),
    n("Veers", True),
    n("General Nevar"),
    n("Admiral Piett"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Blizzard 4", qty=2),
    n("Blizzard 1", True),
    n("AT-AT Commander"),
    n("A Dark Time For The Rebellion", True),
    n("A Dark Time For The Rebellion"),
    n("Conquest", True),
    n("Grand Moff Tarkin", True),
    n("Grand Moff Tarkin"),
    n("Target The Main Generator"),
    n("Hoth Blockade"),
    n("No Escape"),
    n("He Hasn't Come Back Yet"),
    n("Garindan", True),
    n("Garindan"),
    n("Stop Motion", True),
    n("Stop Motion"),
    n("Cold Feet", True),
    n("Trample", qty=2),
    n("Marquand In Blizzard 6"),
    n("Control"),
    n("We're In Attack Position Now"),
    n("Blizzard 2", True),
    n("Imperial Command", qty=3),
    n("Flagship Executor"),
    n("Image Of The Dark Lord", True),
    n("Commander Igar", True),
    n("Juno Eclipse, Black Leader"),
    n("Darth Vader, Dark Lord Of The Sith", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Battle Order"),
    n("There Is No Try"),
    n("After Her!", True),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = [
    n("Oppressive Enforcement"),
    n("A Useless Gesture"),
    n("Imperial Detention"),
]
