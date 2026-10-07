#!/usr/bin/env python3
"""2012 US Nationals Day 2 leftover Xerox: Brian Herold.

Source: 2012NationalsDay2.pdf pages 5–6 (handwritten 2010 Xerox, 12 shields).
Name Brian Herold dested Brian Herold analog leftover Day 1 / 2013 Worlds/MPC/TMW/SoCal.
Username blank. p05 Light Yavin 4. p06 Dark Kessel.
Do not dest as Aaron Nelson. Do not dest as a new person.
Do not dest Day 1 Herold 60s again.
"""
from __future__ import annotations

PLAYER = "Brian Herold"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 US Nationals Day 2.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2012 US Nationals Day 2 Brian Herold LS.png"
DS_SCAN = "2012 US Nationals Day 2 Brian Herold DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Brian Herold. Username blank. "
    "p06 LIGHT/DARK dest from filled 60s / Name Brian Herold. "
    "Do not dest as Aaron Nelson. Do not dest Day 1 Herold 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Herold dested Brian Herold analog leftover Day 1. "
    "Username blank. LIGHT checked. Do not dest as Aaron Nelson. "
    "Yavin 4 True dested Yavin 4: Massassi Throne Room True analog leftover Hanson. "
    "Communin dested Communing True analog leftover Stenerson IN THE 60. "
    "Master Kenobi dested analog leftover Stenerson. "
    "Yoda GW dested Yoda, Great Warrior analog leftover Stenerson. "
    "Coruscant (ep1) dested Coruscant True analog leftover Consoli Day 2. "
    "Tatooine: Obi's Hut dested Tatooine: Obi-Wan's Hut analog leftover. "
    "Restore Freedom To Da Galaxy dested Restore Freedom To The Galaxy analog leftover virtual-only. "
    "Tatooine (ep1) dested Tatooine True analog leftover. "
    "Imp Atrocity dested Imperial Atrocity analog leftover Day 1 empty x2 True x2. "
    "It's Not My Fault dested It's Not My Fault! analog leftover. "
    "Derek Klivian dested Derek \"Hobbie\" Klivian analog leftover Jan. "
    "Man Flaps dested Maneuvering Flaps analog leftover 2012 MPC Herold. "
    "He Can Go About His Bidness dested He Can Go About His Business True analog leftover Day 1. "
    "Simple Trix & Nonsense dested Simple Tricks And Nonsense True analog leftover Day 1. "
    "Let's Keep A Lil Optimism dested Let's Keep A Little Optimism Here analog leftover. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Herold dested Brian Herold analog leftover Day 1. "
    "Username blank. LIGHT empty dest from filled Dark 60s. "
    "Kessel dested Kessel / Spice Mines Of Kessel analog leftover Finley. "
    "Combat Readiness True dested Combat Readiness / Full Scale Alert True analog leftover Day 1 IN THE 60. "
    "Kessel Spice Mines Admin Office dested Kessel: Spice Mines - Administrator's Office analog leftover Day 1. "
    "MM & EO crossed dested Weapon Levitation analog leftover. "
    "Retraining Bolt dested Restraining Bolt analog leftover Day 1. "
    "The Mando, Father of Farts dested Jango Fett, The Assassin analog leftover Day 1. "
    "Boba Prepared Hunter dested Boba Fett, Renowned Bounty Hunter analog leftover Hunter. "
    "Cylon Commander dested Grievous, Hunter Of Jedi analog leftover Day 1. "
    "Spice Mine Admin dested Moruth Doole, Kessel Administrator analog leftover Day 1. "
    "Sonic Bombardment dested analog leftover Day 1 unique overcount. "
    "Control & Set 4 Stun dested Control & Set For Stun analog leftover Day 1. "
    "Admiral Pellaeon dested analog leftover Day 1. "
    "4-LOM w gun dested 4-LOM With Concussion Rifle True analog leftover Day 1. "
    "CC: Security Tower dested Cloud City: Security Tower True analog leftover Day 1. "
    "Knowledge dested Knowledge And Defense True analog leftover Day 1 IN THE 60. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room", True),
    n("Master Kenobi"),
    n("Communing", True),
    n("The Camp"),
    n("Squadron Assignments"),
    n("Power Pivot", True),
    n("Hear Me Baby, Hold Together"),
    n("Yoda, Great Warrior"),
    n("Coruscant", True),
    n("Phylo Gandish"),
    n("Tatooine: City Outskirts", True),
    n("Commander Luke Skywalker"),
    n("Yavin 4: Briefing Room"),
    n("Kin Kian"),
    n("Rogue Squadron X-wing", True, qty=3),
    n("Red Squadron 7", True),
    n("Dual Laser Cannon", True),
    n("Imperial Atrocity", qty=2),
    n("Rogue Squadron X-wing", qty=3),
    n("Rebel Gunrunner"),
    n("Commander Luke Skywalker", True),
    n("Dash Rendar", True),
    n("Jek Porkins"),
    n("Corran Horn", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Dack Ralter"),
    n("Keir Santage", True),
    n("Obi-Wan's Apparition"),
    n("Rebel Aces"),
    n("Rebel Fleet"),
    n("Rogue 1", True),
    n("Derek \"Hobbie\" Klivian"),
    n("Organized Attack", qty=2),
    n("Organized Attack", True),
    n("Enhanced Proton Torpedoes", True),
    n("It's Not My Fault!", qty=3),
    n("Rogue 2"),
    n("Commander Wedge Antilles", True),
    n("Restore Freedom To The Galaxy"),
    n("Power Pivot"),
    n("Yavin 4: Massassi War Room"),
    n("Biggs, Rogue Legend"),
    n("Lieutenant Tarn Mison"),
    n("Massassi Base Sentry"),
    n("Red 6"),
    n("Maneuvering Flaps"),
    n("Echo Base Garrison", True),
    n("Imperial Atrocity", True, qty=2),
    n("Tatooine", True),
    n("Flash Of Insight", True),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High", True),
    n("Battle Plan"),
    n("Do, Or Do Not", True),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor"),
    n("Ultimatum", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well"),
]
LS_ADD = []

DS_START = "Kessel / Spice Mines Of Kessel"
DS_CARDS = [
    n("Kessel / Spice Mines Of Kessel"),
    n("Combat Readiness / Full Scale Alert", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Security Precautions"),
    n("I'll Take Them Myself"),
    n("Gift Of The Master"),
    n("Sense", qty=2),
    n("Weapon Levitation"),
    n("Restraining Bolt"),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Darth Maul", qty=2),
    n("Jango Fett, The Assassin", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Darth Sidious", qty=2),
    n("Justifier"),
    n("Boba Fett, Renowned Bounty Hunter"),
    n("Sniper & Dark Strike"),
    n("Grievous, Hunter Of Jedi", qty=3),
    n("Garindan", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Moruth Doole, Kessel Administrator"),
    n("Ghhhk"),
    n("Kessel Surveillance System"),
    n("Sidious' Lightsaber"),
    n("Control & Set For Stun"),
    n("Cold Feet", True),
    n("Lightsaber Deficiency"),
    n("Arica"),
    n("Grievous' Lightsabers"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Imperial Barrier"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Slave I, Symbol Of Fear"),
    n("Blaster Rack", True),
    n("Kessel: Spice Mines - Prison"),
    n("Protocol Failure"),
    n("Disarmed"),
    n("Spice Mine Operations"),
    n("Admiral Pellaeon"),
    n("Dr. Evazan & Ponda Baba"),
    n("Darth Vader With Lightsaber"),
    n("Force Field", True),
    n("Close Call", True),
    n("4-LOM With Concussion Rifle", True),
    n("Cloud City: Security Tower", True),
    n("Maul's Sith Infiltrator"),
    n("You Are Beaten"),
    n("Alter", True),
    n("Imperial Command"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Allegations Of Corruption", True),
    n("Firepower", True),
]
DS_ADD = []
