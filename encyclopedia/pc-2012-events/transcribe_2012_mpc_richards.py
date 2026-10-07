#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Mike Richards.

Source: 2012mpcday1.pdf pages 123–124 (2010 form, 12 shields).
Name Michael Richards dested Mike Richards (generate CANON).
p123 Light Restore Freedom To The Galaxy. p124 Dark Spice Mine Operations.
Username m007agent analog 2013 Worlds sheet mroo7agent.
Pack player-stubs/Mike_Richards.wiki.
Do not dest as a new person. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "Mike Richards"
USERNAME = "m007agent"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 123
DS_PAGE = 124
LS_SCAN = "2012 Match Play Championship Day 1 Mike Richards LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Mike Richards DS.png"
LS_DECK_NAME = "Freedom Jazz"
DS_DECK_NAME = "PPM Spice"
NOTE = "Handwritten 2010 Xerox form. Username m007agent."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Michael Richards dested Mike Richards. "
    "Username dested m007agent analog 2013 Worlds sheet mroo7agent. LIGHT checked. "
    "Deck Name Freedom Jazz. Restore Freedom True dested Restore Freedom To The Galaxy "
    "virtual-only. Yavin IV dested Yavin 4 True. Here's your Baby Hold Together dested "
    "Hear Me Baby, Hold Together True analog Baroni. Rel S dested Rel Sentry analog O'Hare. "
    "AFA True dested in the 60 analog Casey. Communing True dested in the 60 analog Casey. "
    "Rogue Squadron X-wing empty x5 AND True x1 kept separate analog Foth. "
    "Rel Sentry empty AND True kept separate analog Foth. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Michael Richards dested Mike Richards. "
    "Username dested m007agent. DARK checked. Deck Name PPM Spice. "
    "Spice Mine Ops True dested Spice Mine Operations True. "
    "Combat Readiness True dested Combat Readiness / Full Scale Alert True in the 60. "
    "Kessel empty dested Kessel system. Executor crossed dested Devastator True replacement. "
    "The Emp's Reach dested Maarek Stele, The Emperor's Reach True analog Eier. "
    "Mara Jade w/ Saber dested Mara Jade With Lightsaber True. "
    "4-LOM w/ Rifle dested 4-LOM With Concussion Rifle True analog O'Hare. "
    "Control & SFS dested Control & Set For Stun analog O'Hare. "
    "Sniper & DS dested Sniper & Dark Strike analog O'Hare. "
    "MM & EO dested Masterful Move & Endor Occupation analog PMT. "
    "SSTFT dested Something Special Planned For Them True analog PMT. "
    "He Is Not Ready & Imp Prop dested He Is Not Ready & Imperial Propaganda True. "
    "Victory True AND empty kept separate analog Foth. "
    "K&D True dested in the 60 analog Murray. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Restore Freedom To The Galaxy"
LS_CARDS = [
    n("Restore Freedom To The Galaxy", True),
    n("Yavin 4", True),
    n("Imperial Atrocity", True, qty=4),
    n("Obi-Wan's Journal", True),
    n("Power Pivot", qty=2),
    n("Phylis Brandish", True),
    n("Organized Attack", qty=3),
    n("Ewok Sabotage"),
    n("Massassi Base Sentry", True),
    n("Yoda, Great Warrior", True),
    n("Rogue Squadron X-wing", qty=5),
    n("Rogue 1", qty=2),
    n("Yavin 4: Massassi War Room"),
    n("Tatooine"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("R2-K4"),
    n("Darklighter Rebellion", True),
    n("Dash Rendar", True),
    n("It's Not My Fault", True, qty=3),
    n("Rebel Aces", True),
    n("The Crow", True),
    n("Biggs' Rogue Squadron", True),
    n("Rogue Squadron X-wing", True),
    n("Tatooine: City Outskirts"),
    n("Commander Wedge Antilles", True),
    n("Communing", True),
    n("Hear Me Baby, Hold Together", True),
    n("Use The Force", True, qty=2),
    n("Rel Sentry"),
    n("Coruscant"),
    n("Strike Force", True),
    n("Jek Porkins", True),
    n("Corellian Corvette"),
    n("Wedge's Redemption", True),
    n("Squadron Assignments"),
    n("Rebel Barrier"),
    n("Commander Luke Skywalker", True, qty=2),
    n("Lieutenant Tarn Mison"),
    n("Death Barrier", True),
    n("Echo Base Garrison"),
    n("Enhanced Proton Torpedoes", True),
    n("Rel Sentry", True),
    n("Rebel Gunner", True),
    n("Yavin 4: Briefing Room"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("He Can Go About His Business"),
]
LS_ADD = []

DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Spice Mine Operations", True),
    n("Kessel"),
    n("Combat Readiness / Full Scale Alert", True),
    n("Executor"),
    n("Kessel: Spice Mines - Extraction Facility", True),
    n("Kessel: Spice Mines - Prison", True),
    n("Endor Shield", True),
    n("Kuat Drive Yards", True),
    n("I'll Take Them Myself", True),
    n("Kessel: Spice Mines - Administrator's Office", True),
    n("Tractor A Barrier"),
    n("Imperial Command", qty=2),
    n("Close Call", True, qty=3),
    n("Blizzard 1", True),
    n("Blizzard 4"),
    n("U-3PO"),
    n("Blizzard 2", True),
    n("Blockade Support Ship", True),
    n("Dengar In Punishing One"),
    n("Tyrant"),
    n("Devastator", True),
    n("Conquest", True),
    n("Victory", True),
    n("Victory"),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Imperial Gozanti"),
    n("General Veers", True),
    n("Mara Jade With Lightsaber", True),
    n("Grand Moff Tarkin", True),
    n("4-LOM With Concussion Rifle", True),
    n("Grand Admiral Thrawn"),
    n("Darth Vader With Lightsaber", qty=3),
    n("Spice Mine Administrator", True, qty=2),
    n("Kessel: Spice Mines"),
    n("Battle Deployment"),
    n("Kessel Surveillance System", True),
    n("Something Special Planned For Them", True),
    n("Image Of The Dark Lord", True),
    n("Lost In Space"),
    n("He Is Not Ready & Imperial Propaganda", True),
    n("Lateral Damage"),
    n("Protocol Failure", True),
    n("Spice Mines Of Kessel", True),
    n("Operational As Planned", True),
    n("Control & Set For Stun"),
    n("Tempest 1"),
    n("Ghhhk"),
    n("Sniper & Dark Strike"),
    n("You Are Beaten"),
    n("Masterful Move & Endor Occupation"),
    n("Gravity Shadow"),
    n("Cold Feet", True),
    n("Overwhelmed"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Fanfare", True),
    n("Resistance"),
    n("Firepower"),
]
DS_ADD = []
