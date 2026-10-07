#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Tuan Le Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Tuan Le"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 54
DS_PAGE = 53
LS_SCAN = "2013 Match Play Championship p54 Tuan Le LS.png"
DS_SCAN = "2013 Match Play Championship p53 Tuan Le DS.png"
LS_NOTE = (
    "Typed 2010 Xerox Print Form. Tuan Le. Light. "
    "Deck title You Can Either Profit By This... Or Be Destroyed. "
    "You Can Either Profit By This... Or Be Destroyed dested You Can Either Profit By This... / Or Be Destroyed. "
    "Han as written. Artoo as written. Shimi Skywalker dested Shmi Skywalker. "
    "Lando's Luxury Yacht dested Lady Luck. "
    "Tatooine: Lar's Moisture Farm dested Tatooine: Lars' Moisture Farm. "
    "Form left column reprints 37–38 on lines 39–40 are Tatooine and Tatooine: Lars' Moisture Farm. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Typed 2010 Xerox Print Form. Tuan Le. Dark. "
    "Deck title A Stunning Move / A Valuable Hostage. "
    "A Stunning Move / A Valuable Hostage (not Available Hostages). Insidious Prisoner. "
    "Coruscant: Private Plateform dested Coruscant: Private Platform (Docking Bay). "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Cyborg Commander, Hunter Of Jedi dested Grievous, Hunter Of Jedi. "
    "The Mandalorian, Father Of Fett dested Jango Fett, The Assassin. "
    "IG Bodyguard Droid dested IG-100 MagnaGuard. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers. "
    "Sniper as written. Line 50 Rolling, Rolling, Rolling struck dested Short Range Fighters & Watch Your Back. "
    "Form left column reprints 37–38 on lines 39–40 are The Phantom Menace and Lightsaber Parry. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Han", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Jabba's Palace"),
    n("Heading For The Medical Frigate", True),
    n("Seeking An Audience", True),
    n("Quick Draw", True),
    n("I Must Be Allowed To Speak", True),
    n("Anger, Fear, Aggression", True),
    n("Qui-Gon Jinn"),
    n("Yoda, Great Warrior", True),
    n("Ben Kenobi", qty=2),
    n("Master Luke", True, qty=2),
    n("Leia, Rebel Princess"),
    n("Chewbacca, Protector"),
    n("Corran Horn"),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Shmi Skywalker"),
    n("Mirax Terrik"),
    n("Tanus Spijek", True),
    n("Padme Naberrie", True, qty=2),
    n("Threepio With His Parts Showing"),
    n("Artoo"),
    n("Wedge In Red Squadron 1", True),
    n("Lady Luck", True),
    n("Booster In Pulsar Skate", True),
    n("Luke's Lightsaber"),
    n("Anakin's Lightsaber", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Chewbacca's Bowcaster"),
    n("Jedi Lightsaber", True),
    n("Luke's Bionic Hand", True),
    n("Obi-Wan's Journal"),
    n("Tatooine Utility Belt", True),
    n("Tatooine"),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Someone Who Loves You", qty=2),
    n("Honor Of The Jedi"),
    n("Lightsaber Proficiency"),
    n("Mindful Of The Future"),
    n("Speak With The Jedi Council"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Tatooine Celebration"),
    n("Artoo, I Have A Bad Feeling About This"),
    n("Weapon Levitation"),
    n("Draw Their Fire"),
    n("Alter", True),
    n("Swing-And-A-Miss"),
    n("Jedi Presence"),
    n("Skywalkers"),
    n("Don't Forget The Droids", True),
    n("A Gift"),
    n("Rycar Ryjerd", True),
    n("Sai'torr Kal Fas", True),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("Another Pathetic Lifeform", True),
    n("Only Jedi Carry That Weapon"),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Wise Advice"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage", True),
    n("Insidious Prisoner", True),
    n("Coruscant: Private Platform (Docking Bay)", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Galen Marek, Starkiller", True, qty=2),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Boba Fett, Prepared Hunter", True),
    n("Jango Fett, The Assassin", True),
    n("Dr. Evazan & Ponda Baba"),
    n("P-59"),
    n("P-60"),
    n("P-13 & P-14", True),
    n("Destroyer Droid", qty=3),
    n("4-LOM With Concussion Rifle"),
    n("IG-100 MagnaGuard", True, qty=2),
    n("Slave I, Symbol Of Fear", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Grievous' Lightsabers", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Trophy Of A Kill", True, qty=2),
    n("Nal Hutta"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Bridge"),
    n("Prepared Defenses"),
    n("Jabba's Haven", True),
    n("Gift Of The Master", True),
    n("3,720 To 1", True),
    n("Sniper"),
    n("The Phantom Menace", qty=2),
    n("Lightsaber Parry"),
    n("Sith Fury", True),
    n("A Dark Time For The Rebellion", True),
    n("Alter & Collateral Damage"),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Oh, Switch Off"),
    n("Wipe Them Out, All Of Them"),
    n("Blaster Rack", True),
    n("Rolling, Rolling, Rolling"),
    n("Short Range Fighters & Watch Your Back"),
    n("Force Field", True),
    n("Lightsaber Deficiency", True),
    n("Maul Strikes"),
    n("Ability, Ability, Ability", True),
    n("First Strike"),
    n("No Escape"),
    n("Forced Servitude"),
    n("Weapon Levitation"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Abyss", True),
    n("Imperial Detention", True),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
    n("A Useless Gesture"),
    n("Do They Have A Code Clearance?"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
]
DS_ADD = []
