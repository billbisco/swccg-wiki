#!/usr/bin/env python3
"""2014 Alderaan Regionals Xerox: Ganden Yanaga (Cam Solusar).

Source: 2014-Alderaan-Regionals.pdf pages 1–2 (2010 form).
"""
from __future__ import annotations

PLAYER = "Ganden Yanaga"
USERNAME = "Cam Solusar"
STAGE = ""
PDF = "2014 Alderaan Regionals.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2014 Alderaan Regionals p01 Ganden Yanaga LS.png"
DS_SCAN = "2014 Alderaan Regionals p02 Ganden Yanaga DS.png"
NOTE = "Handwritten Xerox form."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We Have A Plan / They Will Be Lost And Confused"
LS_CARDS = [
    n("We Have A Plan / They Will Be Lost And Confused"),
    n("Naboo: Theed Palace Throne Room"),
    n("Naboo: Theed Palace Hallway"),
    n("Naboo: Theed Palace Courtyard"),
    n("Scomp Link Access", True),
    n("We'll Take The Long Way"),
    n("Quick Draw", True),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Queen Amidala", qty=2),
    n("Odin Nesloor & First Aid"),
    n("Found Someone You Have"),
    n("Houjix"),
    n("Field Dressing"),
    n("Control & Tunnel Vision"),
    n("Mace Windu", True, qty=2),
    n("Jedi Lightsaber", True),
    n("Voolvif Monn"),
    n("2-1B", True),
    n("Sai'torr Kal Fas", True),
    n("Dejarik Hologame Board"),
    n("I've Decided To Go Back", True, qty=2),
    n("Wesa Gotta Grand Army", qty=3),
    n("A Jedi's Resilience"),
    n("Hear Me Baby, Hold Together", True),
    n("K'lor'slug", True),
    n("Naboo: Battle Plains"),
    n("Panaka, Protector Of The Queen", qty=2),
    n("Jedi Levitation", True),
    n("Escape Pod", True, qty=2),
    n("Disarmed"),
    n("Imperial Atrocity", True),
    n("Jerus Jannick", qty=2),
    n("Imperial Barrier"),
    n("Dorme"),
    n("Let The Wookiee Win", True, qty=2),
    n("Either Way, You Win", True),
    n("Anakin's Lightsaber"),
    n("Under Attack"),
    n("Ascension Guns", True),
    n("Nabrun Leids"),
    n("Panaka's Blaster"),
    n("Captain Panaka"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Hiding In The Garbage", True),
    n("Dodge"),
    n("Queen Amidala"),
    n("Bravo Fighter", True),
    n("Landing Claw"),
    n("Naboo: Boss Nass' Chambers"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("Affect Mind"),
    n("The Professor"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Planetary Defenses", True),
]
LS_ADD = [
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Wise Advice"),
]


DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("Imperial Entanglements / No One To Stop Us This Time"),
    n("Tatooine"),
    n("Devastator"),
    n("Tatooine: Imperial Vanguard Camp"),
    n("Prepared Defenses", True),
    n("Imperial Stockpile", True),
    n("Blaster Rifle", True),
    n("Imperial Academy Training", True),
    n("Endor Shield", True),
    n("Coordinated Attack", True),
    n("Coordinated Attack"),
    n("Imperial Command", qty=3),
    n("A Dark Time For The Rebellion", True),
    n("A Dark Time For The Rebellion"),
    n("Trooper Assault", qty=2),
    n("Outflank", True),
    n("Outflank"),
    n("Lightsaber Deficiency", True),
    n("Lightsaber Deficiency"),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Wounded Warrior", qty=2),
    n("Tatooine Occupation", qty=2),
    n("Imperial Domination", True),
    n("Imperial Domination"),
    n("Imperial Stormtrooper", qty=6),
    n("Elite Squadron Stormtrooper", True, qty=4),
    n("Intensify The Forward Batteries", qty=2),
    n("Laser Cannon Battery"),
    n("Tatooine: Mos Espa"),
    n("Grand Moff Tarkin", True),
    n("Blast Points"),
    n("Control"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Admiral Piett"),
    n("Strategic Reserves", True),
    n("Operational As Planned", True),
    n("Protocol Failure"),
    n("Deflector Shield Generators", True),
    n("Grand Admiral Thrawn"),
    n("Admiral Motti", True),
    n("Tatooine: Cantina"),
    n("Tatooine: Imperial Outpost"),
    n("ISB Sector Commander"),
    n("Sith Fury & End This Destructive Conflict"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try"),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = [
    n("Leave Them To Me", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("A Useless Gesture", True),
]
