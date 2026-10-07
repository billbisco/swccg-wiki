#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 2: Reid Smith Xerox LS+DS.

Name RSmith, username 3MW8J8.
"""
from __future__ import annotations

PLAYER = "Reid Smith"
USERNAME = "3MW0J8"
STAGE = "Day 2"
PDF = "2013 SoCal Grand Prix Day 2.pdf"
LS_PAGE = 6
DS_PAGE = 7
LS_SCAN = "2013 SoCal Grand Prix Day 2 p06 Reid Smith LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 2 p07 Reid Smith DS.png"
LS_NOTE = (
    "Handwritten Print Form. Name RSmith, username 3MW8J8. Event SoCal Grand Prix, 27 October 2013. "
    "Line 1 Home One: War Room, line 2 It Is The Future You See (V). "
    "Lando's Luxury Yacht → Lady Luck. Sai'torr Kal Fas as written. "
    "What Are You Trying To Push? as written. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Print Form. A Stunning Move / A Valuable Hostage. "
    "Jabba' Shaven → Jabba's Haven. Ni Chuba Na?? → Ni Chuba Na?. "
    "Galen, Secret Apprentice → Galen Marek, Starkiller. "
    "Cyborg Commander, Hunter Of Jedi → General Grievous. "
    "The Mandalorian, Father Of Fett → Jango Fett, The Assassin. "
    "Cyborg Commander's Lightsaber → Grievous' Lightsabers. "
    "Masterful Move & Endor Occ → Masterful Move & Endor Celebration. "
    "You Swindled Me! as written. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See"
LS_CARDS = [
    n("Home One: War Room"),
    n("It Is The Future You See", True),
    n("Quick Draw", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Yavin 4: Massassi War Room", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Master Qui-Gon", True, qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Leia, Rebel Princess"),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Lady Luck"),
    n("Han, Chewie, And The Falcon", True),
    n("Home One"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Let The Wookiee Win", True, qty=3),
    n("A Jedi's Resilience", qty=2),
    n("Grimtaash"),
    n("Speak With The Jedi Council", qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Jedi Levitation", True),
    n("Clash Of Sabers"),
    n("Blaster Deflection"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Weapon Levitation"),
    n("What're You Tryin' To Push On Us?"),
    n("Sai'torr Kal Fas", True),
    n("Imperial Atrocity", True, qty=2),
    n("Seeking An Audience", True),
    n("Mechanical Failure"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Only Jedi Carry That Weapon"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Planetary Defenses", True),
    n("Affect Mind", True),
    n("Ultimatum", True),
    n("He Can Go About His Business", True),
]
LS_ADD = []


DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Coruscant: Private Platform"),
    n("Prepared Defenses", True),
    n("Jabba's Haven"),
    n("Gift Of The Mentor"),
    n("Ni Chuba Na?", True),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Cloud City: Security Tower", True),
    n("Nal Hutta"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Galen Marek, Starkiller", qty=3),
    n("General Grievous", qty=2),
    n("Boba Fett, Prepared Hunter", qty=2),
    n("Jango Fett, The Assassin", qty=2),
    n("Garindan", True),
    n("Keder The Black"),
    n("Battle Droid Squad"),
    n("Ket Maliss, Shadow Killer"),
    n("OOM-9", True),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Slave I, Symbol Of Fear"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Sonic Bombardment", True, qty=3),
    n("Force Lightning"),
    n("Force Field", True, qty=2),
    n("Masterful Move & Endor Celebration", qty=2),
    n("Monnok"),
    n("Ghhhk"),
    n("Why Didn't You Tell Me?", True),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Force Push", True),
    n("You Swindled Me!", True),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Sniper & Dark Strike"),
    n("Blaster Rack", True),
    n("Where Are You Taking This Thing?"),
    n("The Phantom Menace", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward", True),
    n("Secret Plans"),
    n("Firepower", True),
    n("Abyss", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Battle Order", True),
    n("There Is No Try", True),
    n("Fanfare", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Do They Have A Code Clearance?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
]
DS_ADD = []
