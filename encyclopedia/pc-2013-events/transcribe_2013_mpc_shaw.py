#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Greg Shaw Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 86
DS_PAGE = 85
LS_SCAN = "2013 Match Play Championship p86 Greg Shaw LS.png"
DS_SCAN = "2013 Match Play Championship p85 Greg Shaw DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Greg Shaw. Light. Deck title #COLO. "
    "There Is Good In Him dested There Is Good In Him / I Can Save Him. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Luke Skywalker, Rebel Scout as written. Sai'torr Kal Fas dested Sai'torr Kal Fas. "
    "Jedi Council Chamber dested Coruscant: Jedi Council Chamber. "
    "Boss Nass Chambers dested Naboo: Boss Nass' Chambers. Battle Plains dested Naboo: Battle Plains. "
    "Obi Wan With Lightsaber dested Obi-Wan With Lightsaber. Master Qui Gon dested Master Qui-Gon. "
    "Princess Leia dested Princess Leia. Han Chewie Falcon dested Han, Chewie, And The Falcon. "
    "Qui Gon's Saber dested Qui-Gon Jinn's Lightsaber. "
    "Sorry About The Mess & Blaster Prof dested Sorry About The Mess & Blaster Proficiency. "
    "Form left column reprints 37–38 on lines 39–40 are Escape Pod. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Greg Shaw. Dark. Deck title 8AM HuntDown. "
    "Hunt Down And Destroy dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Coruscant (SE) dested Coruscant. Coruscant Imperial City dested Coruscant: Imperial City. "
    "Ni Chuba Nah dested Ni Chuba Na. Endor Shield dested Endor Shield. "
    "Hoth Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Galen's Fighter dested Rogue Shadow. Blizzard 11 dested Blizzard 1. "
    "Darth Vader Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Darth Vader DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Galen Secret Apprentice dested Galen Marek, Starkiller. "
    "Black Leader dested Juno Eclipse, Black Leader. General Nevaar dested General Nevar. "
    "Gartendan dested Garindan. Emperor's Power dested Emperor's Power. "
    "Where Are You Taking This Thing dested Where Are You Taking This ... Thing?. "
    "Sniper & Dark Strike as written. Masterful Move & Endor Occ dested Masterful Move & Endor Occupation. "
    "Weapon Lev & The Emperor's dested Weapon Levitation. "
    "Form left column reprints 37–38 on lines 39–40 are No Escape and Protocol Failure. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("I Feel The Conflict"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Heading For The Medical Frigate"),
    n("Colo Claw Fish"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Home One: War Room"),
    n("Luke Skywalker, Jedi Knight"),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Obi-Wan With Lightsaber"),
    n("Master Qui-Gon", True, qty=2),
    n("Princess Leia", True),
    n("Corran Horn"),
    n("Yoda, Master Of The Force"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Admiral Ackbar", True),
    n("Home One"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Seeking An Audience", True),
    n("Imperial Atrocity", True),
    n("Draw Their Fire"),
    n("Scrambled Transmission", True),
    n("Projection Of A Skywalker"),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Impressive, Most Impressive", True),
    n("Wesa Gotta Grand Army", qty=3),
    n("Speak With The Jedi Council"),
    n("Blaster Deflection"),
    n("Sense", qty=3),
    n("Let The Wookiee Win", True, qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Weapon Levitation"),
    n("A Jedi's Resilience"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("The Professor", True),
    n("Aim High"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("Affect Mind", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("A Sith's Plans"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na", True),
    n("Endor Shield", True),
    n("Blaster Rack", True),
    n("Endor"),
    n("Blockade Flagship: Bridge"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Galen's Lightsaber"),
    n("Vader's Lightsaber"),
    n("Victory"),
    n("Rogue Shadow"),
    n("Blizzard 1", qty=2),
    n("Emperor Palpatine", qty=2),
    n("Boba Fett, Bounty Hunter", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Galen Marek, Starkiller", qty=3),
    n("Juno Eclipse, Black Leader"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("General Nevar"),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Dengar With Blaster Carbine", True),
    n("P-59"),
    n("Garindan", True),
    n("Emperor's Power", True),
    n("No Escape"),
    n("Protocol Failure"),
    n("Imperial Justice", True),
    n("Presence Of The Force"),
    n("A Sith's Weapon"),
    n("Where Are You Taking This ... Thing?"),
    n("Revenge Of The Sith"),
    n("Ghhhk"),
    n("Sniper & Dark Strike"),
    n("Cold Feet", True),
    n("Lightsaber Deficiency", True),
    n("Imperial Reinforcements", True),
    n("Masterful Move & Endor Occupation"),
    n("Weapon Levitation"),
    n("Force Field", True),
    n("Force Push", True),
    n("Force Lightning"),
    n("One Beautiful Thing"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Leave Them To Me", True),
    n("There Is No Try"),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
]
DS_ADD = []
