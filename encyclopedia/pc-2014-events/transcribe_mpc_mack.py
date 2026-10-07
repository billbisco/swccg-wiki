#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Josh Mack.

Source: MPC-2014-Day-1-Main-Event.pdf pages 80–81 (2013 form, 15 shields).
Name Mack dested Josh Mack. Username blank.
Dark Kessel / Combat Readiness. Light Watch Your Step (V).
"""
from __future__ import annotations

PLAYER = "Josh Mack"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 81
DS_PAGE = 80
LS_SCAN = "2014 Match Play Championship Day 1 Josh Mack LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Josh Mack DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2013 Xerox form."
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Mack dested Josh Mack. Username blank. "
    "Line 1 ケッセル dested Kessel. Combat Readiness dested Combat Readiness (V). "
    "Gift Of The Mentor dested Gift Of The Master. Ni Chuba Neecho dested Ni Chuba Na?? (V). "
    "Sniper Combo dested Sniper & Dark Strike. (V) from checkbox."
)
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Mack dested Josh Mack. Username blank. "
    "LIGHT/DARK boxes empty; Light 60 Watch Your Step. WYS (V) dested "
    "Watch Your Step (V) / This Place Can Be A Little Rough (V). "
    "Qualian's Spaceport City dested Spaceport City. CEC (V) dested "
    "Corellian Engineering Corporation (V). Insurrection combo dested "
    "Insurrection & Aim High. Home 1: DB dested Home One: Docking Bay. "
    "Obi in R7 dested Obi-Wan In Radiant VII. Yoda, Great Warrior dested "
    "Yoda, Great Warrior. Mace, MOTO dested Mace Windu, Master Of The Order. "
    "LSJK dested Luke Skywalker, Jedi Knight. Leia, RP dested Leia, Rebel Princess. "
    "Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Romas 'Lock' Navander dested Romas \"Lock\" Navander. Sgt. Bruckman dested "
    "Sergeant Bruckman. Evac Control dested Evacuation Control. NQ Asked dested "
    "No Questions Asked. LTWW dested Let The Wookiee Win. Antilles Man dested "
    "Antilles Maneuver. Antilles combo dested Antilles Maneuver & Rebel Reinforcements. "
    "All Wings combo dested All Wings Report In & Darklighter Spin. Houjix combo dested "
    "Houjix & Out Of Nowhere. Unique overcounts sheet-accurate (No Questions Asked (V) x3, "
    "Let The Wookiee Win (V) x2, Antilles Maneuver (V) x2, Antilles Maneuver & Rebel "
    "Reinforcements x2, All Wings Report In & Darklighter Spin x2, Rebel Barrier x2, "
    "Luke Skywalker, Jedi Knight x2, Dash Rendar (V) x2, Wedge Antilles, Red Squadron "
    "Leader x2, Leia, Rebel Princess x2). NO_DEST Romas 'Lock' Navander. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("Home One: Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Docking Bay"),
    n("Spaceport Scoundrels Guild"),
    n("Obi-Wan In Radiant VII"),
    n("Tantive IV", True),
    n("Lady Luck"),
    n("Yoda, Great Warrior"),
    n("Mace Windu, Master Of The Order"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Maris Brood, Fallen Jedi", True),
    n("Dash Rendar", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Leia, Rebel Princess", qty=2),
    n("Lando Calrissian, Unlikely Hero"),
    n("Mirax Terrik"),
    n("Romas \"Lock\" Navander"),
    n("Padme Naberrie", True),
    n("General Crix Madine"),
    n("Palejo Reshad"),
    n("Sergeant Bruckman"),
    n("Chewie", True),
    n("Laudica", True),
    n("Jaina Solo"),
    n("Evacuation Control", True),
    n("Seeking An Audience", True),
    n("Flash Of Insight", True),
    n("Leia's Blaster Rifle"),
    n("No Questions Asked", True, qty=3),
    n("Corellian Slip", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Antilles Maneuver", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Desperate Reach", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("Corellian Retort", True),
    n("Punch It"),
    n("Rebel Barrier", qty=2),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("There Is Another"),
    n("Do, Or Do Not"),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("I'll Take Them Myself"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Maul's Sith Infiltrator"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Kessel: Spice Mines Administration"),
    n("Spice Mine Operations"),
    n("Galen Marek, Starkiller"),
    n("Dooku's Lightsaber"),
    n("Galen Marek, Starkiller", qty=3),
    n("Count Dooku", qty=3),
    n("Emperor Palpatine", qty=3),
    n("Darth Maul With Lightsaber", qty=2),
    n("U-3PO"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett"),
    n("Garindan", True),
    n("4-LOM With Concussion Rifle", True),
    n("Kessel: Administration Offices"),
    n("Arica"),
    n("Blizzard 4"),
    n("Slave I, Symbol Of Fear"),
    n("Cloud City: Security Tower", True),
    n("Kessel: Prison"),
    n("Kessel: Extraction Facility"),
    n("Kessel Surveillance System"),
    n("Sonic Bombardment", True, qty=3),
    n("Force Push", True, qty=3),
    n("Force Lightning", qty=2),
    n("Sniper & Dark Strike"),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Sense"),
    n("Alter", True),
    n("Cold Feet", True),
    n("Black Sun Fleet"),
    n("Lightsaber Deficiency", True),
    n("Stop Motion"),
    n("Protocol Failure"),
    n("Dark Maneuvers"),
    n("Something Special Planned For Them", True),
    n("Blaster Rack", True),
    n("Imperial Justice", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Death Star Sentry"),
    n("Battle Order"),
    n("Firepower", True),
    n("Weapon Of A Sith"),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("Resistance"),
    n("Fanfare", True),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []

