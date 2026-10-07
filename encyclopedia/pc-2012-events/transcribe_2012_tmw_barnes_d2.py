#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 2 leftover Xerox: James Barnes.

Source: 2012TMWDay2.pdf pages 7–8 (typed slang printout, not a handwritten
Xerox form). Name James Barnes dested James Barnes analog leftover Day 1
CANON / player-stubs/James_Barnes.wiki. Username blank.
p07 Dark Imperial Occupation (typed header says Light Day 2). p08 Light
Center Of Tyranny. Do not dest as a new person.
Do not dest Day 1 TMW / 2013 TMW Barnes 60s again.
"""
from __future__ import annotations

PLAYER = "James Barnes"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2012 Texas Mini Worlds Day 2 James Barnes LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 2 James Barnes DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed slang printout p07 Dark / p08 Light (not a handwritten Xerox form). "
    "Name James Barnes dested James Barnes analog leftover Day 1 CANON. "
    "Username blank. Typed header both pages Light Day 2; dest Dark from Imperial Occupation 60. "
    "Do not dest as a new person. Do not dest Day 1 TMW / 2013 TMW Barnes 60s again."
)
LS_NOTE = (
    "Typed slang printout p08 Light. Name James Barnes dested James Barnes. Username blank. "
    "Anger, Fear, Aggression empty dested analog leftover Anderson IN THE 60. "
    "Center of Tyranny dested Center Of Tyranny analog leftover. "
    "Corsucant: Main Power Plant dested Coruscant: Main Power Plant analog leftover. "
    "Luke Skywalker, Rebel Hero dested analog leftover Alperstein qty=3. "
    "Wedge Antilles, Red Squadron Leader dested analog leftover Nathan qty=2. "
    "Biggs, Rogue Legend dested analog leftover MPC Herold. "
    "Derek 'Hobbie' Klivian dested Derek \"Hobbie\" Klivian analog leftover. "
    "Han, Chewie, and the Falcon dested Han, Chewie, And The Falcon analog leftover Barnes qty=2. "
    "Obi-Wan in Radiant VII dested Obi-Wan In Radiant VII analog leftover. "
    "Commando Training & K'Lor'slug dested Commando Training & K'lor'slug analog leftover Joe. "
    "Yub Yub, Commander dested analog leftover Nathan qty=4. "
    "Odin Nesloor & First Aid dested analog leftover Yanaga. "
    "Houjix & Out of Nowhere dested Houjix & Out Of Nowhere analog leftover Lingrell. "
    "Shield Simple Tricks dested Simple Tricks And Nonsense analog leftover. "
    "Shield Do Or Do Not dested Do, Or Do Not analog leftover Barnes Day 1. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed slang printout p07 Dark (typed header Light Day 2). Name James Barnes dested James Barnes. Username blank. "
    "Knowledge & Defense dested Knowledge And Defense analog leftover True IN THE 60. "
    "Imperial Occupation dested Imperial Occupation / Imperial Control analog leftover Adam K True. "
    "Hoth: Main Power Generators (LS) dested Hoth: Main Power Generators analog leftover. "
    "Ni Chuba Na? dested Ni Chuba Na?? analog leftover Banger. "
    "Admiral Pellaeon dested Captain Gilad Pellaeon analog leftover. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach analog leftover Nelson Day 2. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Hendon. "
    "Galen's Fighter dested Rogue Shadow analog leftover Tenneson. "
    "Marquand in Blizzard 6 dested Marquand In Blizzard 6 analog leftover Schwartz. "
    "Short Range Fighters & Watch Your Back dested analog leftover Bali. "
    "Control x2 dested Control analog leftover Lingrell qty=2. "
    "Do They Have A Code Clearance dested analog leftover IN THE 60. "
    "Shield After Her dested After Her! analog leftover Dambrosio. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Center Of Tyranny"
LS_CARDS = [
    n("Anger, Fear, Aggression"),
    n("Center Of Tyranny"),
    n("Rogue Insertion"),
    n("Coruscant", True),
    n("Planetary Shield"),
    n("Coruscant: Lower Levels"),
    n("Coruscant: Main Power Plant"),
    n("Heading For The Medical Frigate"),
    n("Rogue Squadron Tactics"),
    n("Declaration Of Rebellion"),
    n("Bacta Infirmary"),
    n("Luke Skywalker, Rebel Hero", qty=3),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Corran Horn"),
    n("Biggs, Rogue Legend"),
    n("Tycho Celchu", True),
    n("Ten Numb", True),
    n("Derek \"Hobbie\" Klivian", True),
    n("Dack Ralter", True),
    n("Keir Santage"),
    n("Wes Janson, Rogue Veteran"),
    n("Commander Narra"),
    n("Dash Rendar", True),
    n("Veteran Rogue", qty=2),
    n("Leia, Rebel Princess"),
    n("Leia", True),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Bright Hope", True),
    n("Tantive IV", True),
    n("Spiral"),
    n("Obi-Wan In Radiant VII"),
    n("Luke's Blaster Pistol", True),
    n("Imperial Atrocity", True),
    n("Hindsight", True),
    n("Menace Fades"),
    n("Field Dressing"),
    n("Civil Disorder", True),
    n("Commando Training & K'lor'slug"),
    n("Yub Yub, Commander", qty=4),
    n("Desperate Reach", True, qty=2),
    n("We Wish To Board At Once", qty=2),
    n("Too Close For Comfort"),
    n("Hear Me Baby, Hold Together", True),
    n("Blast The Door Kid", qty=3),
    n("Odin Nesloor & First Aid"),
    n("Houjix & Out Of Nowhere"),
    n("Dressel"),
    n("Coruscant: Jedi Council Chamber"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Do, Or Do Not"),
    n("Jabba's Prize", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
]
LS_ADD = []

DS_START = "Imperial Occupation"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Main Power Generators"),
    n("Hoth: Ice Plains", True),
    n("Imperial Decree", True),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("You May Start Your Landing"),
    n("Endor Shield", True),
    n("Darth Maul", qty=2),
    n("Garindan", True, qty=2),
    n("Captain Gilad Pellaeon"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Admiral Piett"),
    n("Admiral Motti", True),
    n("Juno Eclipse, Black Leader"),
    n("Commander Igar", True),
    n("Grand Moff Tarkin", True, qty=2),
    n("Veers", True),
    n("General Nevar"),
    n("Justifier"),
    n("Maul's Sith Infiltrator"),
    n("Rogue Shadow"),
    n("Tempest 1"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4", True),
    n("Marquand In Blizzard 6"),
    n("AT-AT Cannon", True),
    n("Target The Main Generator"),
    n("We're In Attack Position Now", qty=2),
    n("Battle Deployment"),
    n("Imperial Propaganda", True),
    n("Prepare For A Surface Attack"),
    n("Do They Have A Code Clearance?"),
    n("Protocol Failure"),
    n("No Escape"),
    n("Hoth Blockade"),
    n("Stop Motion", True),
    n("Cold Feet", True, qty=2),
    n("Short Range Fighters & Watch Your Back"),
    n("Trample", qty=2),
    n("He Hasn't Come Back Yet", qty=2),
    n("Imperial Command", qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Walker Garrison"),
    n("Control", qty=2),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Mountains"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Secret Plans"),
    n("Firepower", True),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("After Her!", True),
    n("Abyss", True),
]
DS_ADD = []
