#!/usr/bin/env python3
"""2014 US Nationals Day 2 typed printouts: Matthew Harrison-Trainor.

Source: Nationals-2014-day-2.pdf pages 1–2 (typed, not Xerox forms).
(V) follows a trailing v / (V) on the printout.
"""
from __future__ import annotations

PLAYER = "Matthew Harrison-Trainor"
USERNAME = ""
STAGE = "Day 2"
PDF = "2014 US Nationals Day 2.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2014 US Nationals Day 2 p01 Matthew Harrison-Trainor LS.png"
DS_SCAN = "2014 US Nationals Day 2 p02 Matthew Harrison-Trainor DS.png"


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


# --- Light: Republic At War / Clone Wars gunships. Typed. ---

LS_START = "Republic At War / Aggressive Negotiations"
LS_CARDS = [
    n("Republic At War / Aggressive Negotiations"),
    n("Begun, The Clone War Has"),
    n("Rogue Squadron Tactics"),
    n("Assault On Muunilinst"),
    n("Wokling"),
    n("Nick Of Time", True),
    n("Dressel"),
    n("Chewbacca, Walking Carpet"),
    n("Lady Luck"),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Geonosis: Forward Command Center"),
    n("Muunilinst: Harnaidan Plains"),
    n("Muunilinst: City Of Harnaidan"),
    n("Muunilinst: Republic Landing Site"),
    n("Projection Of A Skywalker"),
    n("AT-RT", qty=7),
    n("Dual Laser Cannon", qty=5),
    n("Slight Weapons Malfunction", qty=2),
    n("Rebel Cell / Hidden Landing Site"),
    n("Let The Wookiee Win", qty=3),
    n("Houjix"),
    n("Dash Rendar", True),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Han Solo, Innocent Scoundrel"),
    n("Rebel Artillery", qty=2),
    n("Acclamator-Class Assault Ship"),
    n("Imperial Atrocity", True),
    n("Hear Me Baby, Hold Together", True),
    n("Away Put Your Weapon", True),
    n("Alderaan Consular Ship"),
    n("Hiding In The Garbage", True),
    n("Desperate Tactics"),
    n("Lucky Shot", True),
    n("Anakin Skywalker, Padawan Learner"),
    n("Dash In Rogue 10"),
    n("Escape Pod", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sorry About The Mess"),
    n("Heading For The Medical Frigate"),
    n("Jaina Solo"),
    n("Republic Gunship Wing"),
    n("Low-Altitude Assault Transport"),
    n("Mace Windu, Master Of The Order"),
]
LS_SHIELDS = [
    n("Anger, Fear, Aggression", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Planetary Defenses", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Jabba's Prize", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Battle Plan", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
]
LS_ADD = [
    n("Wise Advice"),
]


# --- Dark: Hunt Down. Typed. ---

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Conduct Your Search"),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master", True),
    n("Something Special Planned For Them", True),
    n("Blaster Rack", True),
    n("Prepared Defenses"),
    n("Force Field"),
    n("Executor: Holotheatre"),
    n("Blockade Flagship: Bridge"),
    n("Executor: Meditation Chamber"),
    n("Cloud City: Security Tower", True),
    n("Visage Of The Emperor"),
    n("Endor: Back Door"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Count Dooku", qty=3),
    n("Dooku's Lightsaber"),
    n("Blizzard 4", qty=2),
    n("Masterful Move", qty=2),
    n("Blast Door Controls"),
    n("Revenge Of The Sith"),
    n("The Phantom Menace"),
    n("Short Range Fighters & Watch Your Back"),
    n("Force Lightning", qty=2),
    n("Force Push", True, qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", qty=2),
    n("Vader's Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("Mara Jade With Lightsaber"),
    n("Dengar With Blaster Carbine"),
    n("4-LOM With Concussion Rifle"),
    n("Emperor Palpatine", qty=3),
    n("Maul's Sith Infiltrator"),
    n("Slave I, Symbol Of Fear"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sonic Bombardment", qty=3),
    n("No Escape"),
    n("Flare-S Racing Swoop"),
    n("Empire's New Order", True),
    n("A Sith's Weapon"),
]
DS_SHIELDS = [
    n("Knowledge And Defense", True),
    n("Weapon Of A Sith"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Imperial Detention", True),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
]
DS_ADD = [
    n("Firepower", True),
]
