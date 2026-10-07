#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Joe Pinto.

Source: MPC-2014-Day-1-Main-Event.pdf pages 86–87 (typed Holotable lists +
handwritten 15 shields). Username blank.
"""
from __future__ import annotations

PLAYER = "Joe Pinto"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 86
DS_PAGE = 87
LS_SCAN = "2014 Match Play Championship Day 1 Joe Pinto LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Joe Pinto DS.png"
LS_DECK_NAME = "dags"
DS_DECK_NAME = "spice"
NOTE = "Typed Holotable-style lists with handwritten 15 shields."
LS_NOTE = (
    "Typed Holotable list plus handwritten shields. Name Joe Pinto. Username blank. "
    "Deck name dags. MWYHL/SYIC (V) dested Mind What You Have Learned (V) / Save You It Can (V). "
    "(AI) without (V) dested without (V). Master Qui-Gon (V) (AI) dested Master Qui-Gon (V). "
    "NOOOOOOOOOOOO! (V) dested Wookiee Roar (V). legendary starfighter dested Legendary Starfighter. "
    "Jedi Tests 1–6 dested Great Warrior, A Jedi's Strength, Domain Of Evil, Size Matters Not, "
    "It Is The Future You See, You Must Confront Vader. YDSYW dested Your Insight Serves You Well. "
    "Unique overcounts sheet-accurate (Master Qui-Gon (V) x2, Mace Windu (V) x2, "
    "Luke Skywalker, Strong In The Force x3, A Jedi's Resilience x2, Clash Of Sabers x2, "
    "Houjix x2, Escape Pod (V) x3, Wesa Gotta Grand Army x2, Let The Wookiee Win (V) x3, "
    "Artoo-Detoo In Red 5 x2, Republic Gunship Wing x2). (V) from typed (V) or checkbox."
)
DS_NOTE = (
    "Typed Holotable list plus handwritten shields. Name Joe Pinto. Username blank. "
    "Deck name spice. Spice Mine Operations starting Mission. (AI) without (V) dested "
    "without (V). Jango Fett, The Assassin (AI) dested Jango Fett, The Assassin. "
    "Galen Marek, Starkiller (AI) dested Galen Marek, Starkiller. Alter (Premiere) (V) dested "
    "Alter (V). Short Range Fighters & Watch Your Back! dested Short Range Fighters & Watch Your Back!. "
    "Code Cl. dested Do They Have A Code Clearance. CHYBC dested Come Here You Big Coward. "
    "YCHF dested You Cannot Hide Forever. Imp. Detention dested Imperial Detention. "
    "Unique overcounts sheet-accurate (Darth Sidious (AI) x2, Count Dooku x2, "
    "Darth Maul With Lightsaber x2, Galen Marek, Starkiller x2, Dark Maneuvers x2, "
    "Sonic Bombardment (V) x2, Short Range Fighters & Watch Your Back! x2, Force Lightning x2, "
    "Force Field (V) x2, Fighters Coming In x2). (V) from typed (V) or checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Lando Calrissian, Unlikely Hero"),
    n("Yoda", True),
    n("Mace Windu, Master Of The Order"),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu", True, qty=2),
    n("Corran Horn"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Luke Skywalker, Jedi Knight"),
    n("Daughter Of Skywalker", True),
    n("Obi-Wan Kenobi, Jedi Knight"),
    n("Luke's Backpack"),
    n("Battle Plan & Draw Their Fire"),
    n("Reflection", True),
    n("The Way Of Things"),
    n("Quick Draw", True),
    n("Projection Of A Skywalker"),
    n("Do, Or Do Not & Wise Advice"),
    n("Sai'torr Kal Fas", True),
    n("Legendary Starfighter"),
    n("Anger, Fear, Aggression", True),
    n("It Is The Future You See", True),
    n("Strong Is Vader"),
    n("A Jedi's Resilience", qty=2),
    n("Clash Of Sabers", qty=2),
    n("Houjix", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Escape Pod", True, qty=3),
    n("It Could Be Worse"),
    n("Wookiee Roar", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("Weapon Levitation"),
    n("A Jedi's Focus"),
    n("Let The Wookiee Win", True, qty=3),
    n("Dagobah: Jungle"),
    n("Dagobah: Yoda's Hut"),
    n("Naboo: Battle Plains"),
    n("Dagobah: Swamp"),
    n("Dagobah"),
    n("Mind What You Have Learned / Save You It Can", True),
    n("Lady Luck"),
    n("Han, Chewie, And The Falcon", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Republic Gunship Wing", qty=2),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
]
LS_SHIELDS = [
    n("Another Pathetic Lifeform", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("Chasm", True),
    n("Massassi Base Sentry", True),
    n("Only Jedi Carry That Weapon"),
    n("Jabba's Prize", True),
    n("Yavin Sentry", True),
    n("Weapons Display"),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here"),
    n("The Professor"),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred", True),
]
LS_ADD = [
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
]


DS_START = "Spice Mine Operations"
DS_CARDS = [
    n("Fighters Coming In", qty=2),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Garindan", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Darth Sidious", qty=2),
    n("Count Dooku", qty=2),
    n("Emperor Palpatine"),
    n("The Emperor", True),
    n("Darth Vader", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Galen Marek, Starkiller", qty=2),
    n("Kessel Surveillance System"),
    n("Blaster Rack", True),
    n("Ni Chuba Na??", True),
    n("Much Anger In Him"),
    n("I'll Take Them Myself"),
    n("Gift Of The Master"),
    n("Imperial Justice", True),
    n("Begin Landing Your Troops & The Dark Path"),
    n("Where Are You Taking This ... Thing?"),
    n("Protocol Failure"),
    n("Knowledge And Defense", True),
    n("Force Push", True),
    n("Combat Readiness", True),
    n("Cold Feet", True),
    n("Dark Maneuvers", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Lightsaber Deficiency", True),
    n("Sense"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Alter", True),
    n("Force Lightning", qty=2),
    n("Force Field", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Weapon Levitation"),
    n("Kessel: Spice Mines - Prison"),
    n("Cloud City: Security Tower", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Kessel: Spice Mines - Docking Bay"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Kessel"),
    n("Spice Mine Operations"),
    n("Victory"),
    n("Maul's Sith Infiltrator"),
    n("Dengar In Punishing One"),
    n("Slave I, Symbol Of Fear"),
    n("Sidious' Lightsaber"),
    n("Dooku's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("Do They Have A Code Clearance", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Secret Plans"),
    n("You Cannot Hide Forever"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Imperial Detention"),
]
DS_ADD = []
