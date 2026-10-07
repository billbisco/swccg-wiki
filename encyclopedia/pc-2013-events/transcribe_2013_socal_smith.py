#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Reid Smith Xerox LS+DS.

Name RSmith, username 3MW8J8.
"""
from __future__ import annotations

PLAYER = "Reid Smith"
USERNAME = "3MW0J8"
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 37
DS_PAGE = 38
LS_SCAN = "2013 SoCal Grand Prix Day 1 p37 Reid Smith LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p38 Reid Smith DS.png"
LS_NOTE = (
    "Handwritten Print Form. Name RSmith, username 3MW8J8. Event SoCal '13, 26 October 2013. "
    "There Is Good In Him / I Can Save Him. Endor: Landing Platform as written. "
    "Sorry About The Mess & Blaster Pro → Sorry About The Mess & Blaster Proficiency. "
    "Sense (Pre) → Sense. Naboo Halls → Naboo: Theed Palace Hallway. "
    "Obi-Wan W/Lightsaber → Obi-Wan With Lightsaber. "
    "Qui-Gon Jinn W/Lightsaber → Qui-Gon Jinn With Lightsaber. "
    "Han W/ Heavy Blaster Pistol → Han With Heavy Blaster Pistol. "
    "Mace Windu, Master Of The Order as written. "
    "Yavin 4: Massassi War Room as written. "
    "A Few Ming in the shield box → A Few Maneuvers. "
    "Only Jedi Carry That Weapon as written. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Print Form. Name RSmith, username 3MW8J8. Starting location Kessel with "
    "Combat Readiness (V). Kessel: Spice Mines Administrator's Office / Extraction Facility / "
    "Prison as written. Ni Chuba Na?? → Ni Chuba Na?. "
    "Galen, Sewer Apprentice → Galen Marek, Starkiller. "
    "Galen's Lightsaber Vader's Gift → Galen's Lightsaber, Vader's Gift. "
    "The Mandalorian Father of Fett → Jango Fett, The Assassin. "
    "Darth Vader, DLOTS → Darth Vader, Dark Lord Of The Sith. "
    "Darth Vader, BOTJ → Darth Vader, Betrayer Of The Jedi. "
    "Ghhh & Those Rebels → Ghhhk & Those Rebels Won't Escape Us. "
    "Sniper & Dark Strike as written. Short Range Fighters & Watch Your Back as written. "
    "CHYBC → Come Here You Big Coward. YCHF → You Cannot Hide Forever. "
    "DTHACC → Do They Have A Code Clearance?. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Imperial Atrocity", True),
    n("Draw Their Fire"),
    n("Seeking An Audience", True),
    n("Speak With The Jedi Council", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("A Jedi's Resilience", qty=2),
    n("Blaster Deflection", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Sense", qty=2),
    n("Escape Pod", True),
    n("Houjix"),
    n("Grimtaash"),
    n("Dark Approach", True, qty=2),
    n("Clash Of Sabers"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Rebel Barrier", qty=2),
    n("Naboo: Theed Palace Hallway"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Leia, Rebel Princess"),
    n("Anakin Skywalker"),
    n("Padme Naberrie", True),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Admiral Ackbar", True),
    n("Chewie, Enraged", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Corran Horn"),
    n("Mace Windu, Master Of The Order"),
    n("Home One"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Home One: War Room"),
    n("Republic Gunship Wing"),
    n("Mechanical Failure"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("The Professor", True),
    n("Chasm", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("A Few Maneuvers", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Aim High"),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("I'll Take Them Myself"),
    n("Ni Chuba Na?", True),
    n("Gift Of The Mentor"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Kessel: Spice Mines - Prison"),
    n("Cloud City: Security Tower", True),
    n("Darth Maul With Lightsaber", qty=3),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Emperor Palpatine", qty=3),
    n("Galen Marek, Starkiller", qty=3),
    n("Blizzard 4", qty=2),
    n("Arica"),
    n("Dr. Evazan & Ponda Baba"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Garindan", True),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Grand Moff Tarkin", True),
    n("Spice Mine Administrator"),
    n("Spice Mine Operations"),
    n("Kessel Surveillance System"),
    n("Imperial Justice", True),
    n("Blaster Rack", True),
    n("Sonic Bombardment", True, qty=3),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Force Field", True, qty=2),
    n("Dark Maneuvers", qty=2),
    n("Sniper & Dark Strike"),
    n("Lightsaber Deficiency", True),
    n("Protocol Failure"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Cold Feet", True),
    n("Force Push", True, qty=2),
    n("Black Sun Fleet"),
    n("Where Are You Taking This Thing?"),
    n("Alter", True),
    n("Force Lightning"),
    n("Why Didn't You Tell Me?", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Secret Plans", True),
    n("Come Here You Big Coward", True),
    n("Allegations Of Corruption", True),
    n("Abyss", True),
    n("Weapon Of A Sith"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture"),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Battle Order"),
    n("There Is No Try", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
]
DS_ADD = []
