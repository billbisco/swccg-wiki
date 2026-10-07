#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Greg Shaw Xerox Hunt Down. Light empty."""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2013 Texas Mini Worlds Day 1 p08 Greg Shaw LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p07 Greg Shaw DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name G Shaw 9/12. Username blank. "
    "Deck Name Light. LIGHT boxes empty. Main 60 blank except Same as Barry. "
    "No Light 60. Do not copy Barry Alperstein. Hub Light stays empty. "
    "Do not rewrite the 2013 MPC, Worlds, or SoCal Greg Shaw leftovers."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name G Shaw 9/12. Username blank. "
    "Deck Name Dark. DARK. Event TMW 2013. "
    "Do not rewrite the 2013 MPC, Worlds, or SoCal Greg Shaw leftovers. "
    "HDv dested Hunt Down And Destroy The Jedi (V). "
    "Hoth Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Rader dested Endor. "
    "Galen's Fighter dested Rogue Shadow. "
    "Galen Marek Vader's 9th dested Galen Marek, Starkiller. "
    "Vader's Saber dested Vader's Lightsaber. "
    "Mara w/ Saber dested Mara Jade With Lightsaber. "
    "Dengar w/ Blaster Carbine dested Dengar With Blaster Carbine. "
    "DV DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Vader Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Dr E Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "4lom dested 4-LOM With Concussion Rifle. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Nevar dested General Nevar. "
    "LS Deficiency dested Lightsaber Deficiency. "
    "MM+EO dested Masterful Move & Endor Occupation. "
    "Weapon Lev Empire Back dested Weapon Levitation. "
    "One Beautiful Thing dested One Beautiful Thing. "
    "Sith Fury + End This Pest Cont dested Sith Fury & End This Destructive Conflict. "
    "Sniper + Dark Strike dested Sniper & Dark Strike. "
    "Gift of the Mentor dested Gift Of The Master. "
    "YCHFF dested You Cannot Hide Forever. "
    "IFYLOFD dested I Find Your Lack Of Faith Disturbing. "
    "W LFD H dested We'll Let Fate-a Decide, Huh?. "
    "CHYBC dested Come Here You Big Coward. "
    "DTHCC dested Do They Have A Code Clearance?. "
    "Your Destiny / Useless Gesture dested A Useless Gesture. "
    "W of a Sith dested Weapon Of A Sith. "
    "Unique overcounts sheet-accurate: Galen Marek, Starkiller x4, "
    "Darth Vader, Dark Lord Of The Sith x2, Force Field x2, "
    "We Must Accelerate Our Plans x3. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = ""
LS_CARDS = []
LS_SHIELDS = []
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Coruscant"),
    n("Endor"),
    n("Coruscant: Imperial City"),
    n("Blockade Flagship: Bridge"),
    n("Victory"),
    n("Rogue Shadow"),
    n("Blizzard 4"),
    n("Galen Marek, Starkiller", qty=4),
    n("Vader's Lightsaber"),
    n("Mara Jade With Lightsaber"),
    n("Dengar With Blaster Carbine", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Boba Fett, Bounty Hunter"),
    n("Dr. Evazan & Ponda Baba"),
    n("4-LOM With Concussion Rifle", True),
    n("Grand Moff Tarkin", True),
    n("Juno Eclipse, Black Leader"),
    n("Grand Admiral Thrawn"),
    n("Garindan", True),
    n("General Nevar"),
    n("Emperor Palpatine"),
    n("Prepared Defenses", True),
    n("You Are Beaten"),
    n("They're Still Coming Through!"),
    n("Lightsaber Deficiency", True),
    n("Masterful Move & Endor Occupation"),
    n("Force Field", True, qty=2),
    n("Weapon Levitation", True),
    n("Ghhhk"),
    n("Force Lightning"),
    n("One Beautiful Thing"),
    n("Sith Fury & End This Destructive Conflict"),
    n("Force Pike", True),
    n("Sniper & Dark Strike"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sense", qty=2),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Imperial Barrier"),
    n("Ni Chuba Na??", True),
    n("Protocol Failure"),
    n("No Escape"),
    n("Blaster Rack", True),
    n("Imperial Justice", True),
    n("Presence Of The Force"),
    n("A Sith's Weapon"),
    n("Revenge Of The Sith"),
    n("A Sith's Plans"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
]
DS_ADD = [
    n("Abyss", True),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
]
