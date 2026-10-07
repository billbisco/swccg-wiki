#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Mike Pistone.

Source: MPC-2014-Day-1-Main-Event.pdf pages 88–89 (2013 form, 15 shields).
Name PISTONE dested Mike Pistone. Username blank.
"""
from __future__ import annotations

PLAYER = "Mike Pistone"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 88
DS_PAGE = 89
LS_SCAN = "2014 Match Play Championship Day 1 Mike Pistone LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Mike Pistone DS.png"
LS_DECK_NAME = "Kim's Cookies"
DS_DECK_NAME = "I'm sorry dip & break your candle"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name PISTONE dested Mike Pistone. Username blank. "
    "LIGHT checked. Deck name Kim's Cookies. IITFYS (V) dested It Is The Future You See (V) / "
    "A Tremor In The Force (V). SATM / BP dested Sorry About The Mess & Blaster Proficiency. "
    "Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero. Lando's Luxury Yacht dested "
    "Lady Luck. Unique overcounts sheet-accurate (Imperial Atrocity (V) x2, Speak With The Jedi "
    "Council x2, Mace Windu (V) x2, Luke Skywalker, Jedi Knight x2, Master Qui-Gon (V) x2, "
    "Luke Skywalker, Strong In The Force x2, Artoo-Detoo In Red 5 x2, Rebel Leadership (V) x3, "
    "Wesa Gotta Grand Army x3, Escape Pod (V) x2, Let The Wookiee Win (V) x3). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Pistone dested Mike Pistone. Username blank. DARK checked. "
    "Deck name I'm sorry dip & break your candle. Hunt Down (V) dested Hunt Down And Destroy The Jedi (V) / "
    "Their Fire Has Gone Out Of The Universe (V). Gift of the Master dested Gift Of The Master. "
    "One Beautiful Wing dested One Beautiful Thing. Masterful Move dested Masterful Move & Endor Occupation. "
    "WMAOP dested We Must Accelerate Our Plans. Janus Betrayer dested Janus Greejatus. "
    "Galen / Secret Apprentice dested Galen Marek, Starkiller. General Nevar dested General Nevar. "
    "DUJOLOS dested Dujolos. Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Mandalorian Lady dested as written. Firepower crossed, We'll Let Fate-a Decide, Huh? replacement. "
    "Unique overcounts sheet-accurate (Masterful Move & Endor Occupation x2, We Must Accelerate Our Plans x3, "
    "Force Field (V) x2, Dujolos x2, Galen Marek, Starkiller x3, Blizzard 4 x2). NO_DEST PotF; Mandalorian Lady; Dujolos. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("Home One: War Room"),
    n("It Is The Future You See / A Tremor In The Force", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Seeking An Audience", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Imperial Atrocity", True, qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Jedi Lightsaber", True),
    n("A Jedi's Resilience"),
    n("Clash Of Sabers"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Mace Windu", True, qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Master Qui-Gon", True, qty=2),
    n("Sai'torr Kal Fas", True),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Battle Plains"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Jedi Levitation", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Home One"),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Blaster Deflection"),
    n("Escape Pod", True, qty=2),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Quick Draw", True),
    n("Mechanical Failure"),
    n("Luke's Lightsaber"),
    n("Let The Wookiee Win", True, qty=3),
    n("Lando Calrissian, Unlikely Hero"),
    n("Houjix"),
    n("Lady Luck"),
    n("Grimtaash"),
    n("Admiral Ackbar", True),
    n("Weapon Levitation"),
    n("Han, Chewie, And The Falcon", True),
    n("Strike Planning", True),
    n("Jaina Solo", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Planetary Defenses", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense"),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Endor"),
    n("Endor: Back Door"),
    n("Blockade Flagship: Bridge"),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Blaster Rack", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Lightsaber Deficiency", True),
    n("Cold Feet", True),
    n("One Beautiful Thing"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Ghhhk"),
    n("Monnok"),
    n("Force Field", True, qty=2),
    n("Force Lightning"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Force Push", True),
    n("Broken Concentration", True),
    n("Something Special Planned For Them", True),
    n("Revenge Of The Sith"),
    n("Wipe Them Out, All Of Them", True),
    n("Protocol Failure"),
    n("PotF"),
    n("Imperial Justice", True),
    n("No Escape"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Mandalorian Lady"),
    n("Dujolos", qty=3),
    n("Janus Greejatus"),
    n("Galen Marek, Starkiller", qty=3),
    n("General Nevar"),
    n("Grand Admiral Thrawn"),
    n("P-59"),
    n("Juno Eclipse, Black Leader"),
    n("Dr. Evazan & Ponda Baba"),
    n("Boba Fett, Bounty Hunter"),
    n("Grand Moff Tarkin", True),
    n("Mara Jade With Lightsaber"),
    n("Dengar With Blaster Carbine", True),
    n("Jango Fett, The Assassin"),
    n("Garindan", True),
    n("Rogue Shadow"),
    n("Victory"),
    n("Blizzard 4", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance", True),
    n("There Is No Try"),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Death Star Sentry", True),
    n("Weapon Of A Sith"),
]
DS_ADD = []
