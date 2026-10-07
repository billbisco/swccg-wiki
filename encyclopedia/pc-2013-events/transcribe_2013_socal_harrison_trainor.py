#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Matthew Harrison-Trainor typed Holotable LS+DS."""
from __future__ import annotations

PLAYER = "Matthew Harrison-Trainor"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 15
DS_PAGE = 17
LS_SCAN = "2013 SoCal Grand Prix Day 1 p15 Matthew Harrison-Trainor LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p17 Matthew Harrison-Trainor DS.png"
LS_EXTRA_SCANS = [
    (
        "2013 SoCal Grand Prix Day 1 p16 Matthew Harrison-Trainor LS.png",
        "Page 16 of [[:File:2013 SoCal Grand Prix Day 1.pdf]].",
    )
]
DS_EXTRA_SCANS = [
    (
        "2013 SoCal Grand Prix Day 1 p18 Matthew Harrison-Trainor DS.png",
        "Page 18 of [[:File:2013 SoCal Grand Prix Day 1.pdf]].",
    )
]
LS_NOTE = (
    "Typed Holotable printout (not a handwritten Xerox form). Header LS WYSv, "
    "signed Matt HT. Continuation page 16. Wise Advice struck, handwritten "
    "He Can Go About His Business (V). Jabba's Prize is the character."
)
DS_NOTE = (
    "Typed Holotable printout (not a handwritten Xerox form). Header DS Walkers, "
    "signed Matt HT. Continuation page 18. Garindan (V) qty handwritten x2. "
    "Ni Chuba Na?? → Ni Chuba Na?. Juno Eclipse, Black Leader as printed. "
    "Prepared Defenses (V) listed under Interrupt; dested with the shields."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("No Questions Asked", True, qty=3),
    n("Palejo Reshad"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Mirax Terrik"),
    n("Dash Rendar", True, qty=2),
    n("Laudica", True),
    n("Mace Windu, Master Of The Order"),
    n("Yoda, Great Warrior"),
    n("Chewie", True),
    n("Jabba's Prize"),
    n("Captain Han Solo"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("General Crix Madine"),
    n("Sergeant Bruckman"),
    n("Corran Horn"),
    n("Romas 'Lock' Navander"),
    n("Leia, Rebel Princess", qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Padme Naberrie", True),
    n("Maris Brood, Fallen Jedi"),
    n("Wokling", True),
    n("Evacuation Control", True),
    n("Seeking An Audience", True),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
    n("Corellian Slip", True),
    n("Punch It!"),
    n("Antilles Maneuver", True, qty=2),
    n("Desperate Reach", True),
    n("Rebel Barrier", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("It's A Trap!"),
    n("Houjix & Out Of Nowhere"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Corellian Retort", True, qty=2),
    n("Heading For The Medical Frigate"),
    n("Let The Wookiee Win", True, qty=2),
    n("Spaceport City"),
    n("Spaceport Docking Bay"),
    n("Spaceport Scoundrels Guild"),
    n("Home One: Docking Bay"),
    n("Spaceport Street"),
    n("Corellia", True),
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Tantive IV", True),
    n("Obi-Wan In Radiant VII"),
    n("Millennium Falcon", True),
    n("Lady Luck"),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Ultimatum"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense"),
    n("Your Ship?"),
    n("Let's Keep A Little Optimism Here", True),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business", True),
]
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("We're In Attack Position Now", qty=2),
    n("Jango Fett, The Assassin"),
    n("Garindan", True, qty=2),
    n("U-3PO (Yoo-Threepio)"),
    n("Veers", True),
    n("Grand Admiral Thrawn"),
    n("General Nevar"),
    n("Grand Moff Tarkin", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Commander Igar", True),
    n("Admiral Piett"),
    n("Juno Eclipse, Black Leader"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("AT-AT Commander"),
    n("Hoth Blockade"),
    n("Do They Have A Code Clearance?"),
    n("Imperial Decree"),
    n("Ni Chuba Na?", True),
    n("Endor Shield", True),
    n("No Escape"),
    n("Image Of The Dark Lord", True),
    n("You May Start Your Landing", True),
    n("Knowledge And Defense", True),
    n("Target The Main Generator"),
    n("He Hasn't Come Back Yet"),
    n("Walker Garrison"),
    n("Force Push", True, qty=2),
    n("Control"),
    n("Sniper & Dark Strike"),
    n("Imperial Command", qty=3),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Stop Motion", True, qty=2),
    n("Cold Feet", True),
    n("Trample", qty=2),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth"),
    n("Imperial Occupation / Imperial Control", True),
    n("Flagship Executor"),
    n("Conquest", True),
    n("Victory", qty=2),
    n("Tempest 1"),
    n("Blizzard 4", qty=2),
    n("Marquand In Blizzard 6"),
    n("Blizzard 2", True),
    n("Blizzard 1", True),
    n("AT-AT Cannon", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Firepower", True),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
    n("Imperial Detention"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("After Her!", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Prepared Defenses", True),
]
DS_ADD = []
