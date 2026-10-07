#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Olaf Schroeder (signed Joe Freedom pair).

Source: 2014-TMW-Day-1.pdf pages 29–30 (2013 form).
Second Day 1 pair (Schultz pair is transcribe_tmw_schroeder_d1.py).
"""
from __future__ import annotations

PLAYER = "Olaf Schroeder"
USERNAME = "Joe Freedom"
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 29
DS_PAGE = 30
LS_SCAN = "2014 Texas Mini Worlds Day 1 p29 Olaf Schroeder LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p30 Olaf Schroeder DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields). Signed Olaf Schroeder / Joe Freedom."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress After Her!, Jedi Tests empty). "
    "Name Olaf Schroeder. Username Joe Freedom. Email OSchroeder2004. LIGHT checked. "
    "Event TX Mini 5/13/14. Deck Name Gift of the Mentor dested Gift Of The Master. "
    "There Is Good In Him / ICSH dested There Is Good In Him / I Can Save Him. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Luke Skywalker, Rebel Sc dested Luke Skywalker, Rebel Scout. "
    "Luke's LS dested Luke's Lightsaber. "
    "Elegant Light Saber dested Elegant Lightsaber. "
    "Cor: Jedi Council Ch dested Coruscant: Jedi Council Chamber. "
    "Chewie Enraged dested Chewie, Enraged. "
    "Lando Cal, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Maris Brood (Fallen Jedi) dested Maris Brood, Fallen Jedi. "
    "General Solo dested General Solo as written. "
    "Luke Skywalker JK dested Luke Skywalker, Jedi Knight. "
    "Mace Windu, MOTO dested Mace Windu, Master Of The Order. "
    "Tantive IV dested Tantive IV. "
    "You're Quite Clever For A Human dested You're Quite Clever For A Human. "
    "Found Someone You Have / HG dested Found Someone You Have & Higher Ground. "
    "Control + TV dested Control & Tunnel Vision. "
    "Antilles Maneuver dested Antilles Maneuver. "
    "Blaster Def dested Blaster Deflection. "
    "Sorry About The Mess / BP dested Sorry About The Mess & Blaster Proficiency. "
    "Gift of the Master dested Gift Of The Master. "
    "Jedi's Prize dested Jabba's Prize. "
    "Your Insight dested Your Insight Serves You Well. "
    "Lets Keep dested Let's Keep A Little Optimism Here. "
    "Unique overcounts sheet-accurate (Elegant Lightsaber x2, Master Qui-Gon x2, "
    "Chewie, Enraged x2, Lando Calrissian, Scoundrel x2, General Solo x2, "
    "Rebel Leadership x4, Smoke Screen x2, Let The Wookiee Win x2, Sense x2). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress After Her!, Jedi Tests empty). "
    "Name Olaf Schroeder. Username Joe Freedom. DARK checked. "
    "Deck Name Blue Clones. "
    "Imperial Entanglements / NOTSUTT dested Imperial Entanglements / No One To Stop Us This Time. "
    "Blaster Rifle (Dark) dested Blaster Rifle. "
    "Tatooine (Premiere) dested Tatooine. "
    "Tat: Imperial Occupied Camp dested Tatooine: Imperial Occupation Camp. "
    "Deflector Shield Gen dested Deflector Shield Generators. "
    "Tat: Cantina (Pre) dested Tatooine: Cantina. "
    "Tat: Mos Espa (JP) dested Tatooine: Mos Espa. "
    "NO_DEST remaining: You're Quite Clever For A Human, Gift Of The Master (Light), "
    "After Her! (Light Hidden Fortress), Tatooine: Imperial Occupation Camp. "
    "Tat: Mos Eisley (Pre) dested Tatooine: Mos Eisley. "
    "Control & Set For Stun dested Control & Set For Stun. "
    "Ice-Heart / Ysanne Isard dested Ysanne Isard. "
    "Darth Vader (Pre) dested Darth Vader. "
    "Ghhhk & TRWEU dested Ghhhk & Those Rebels Won't Escape Us. "
    "Tat Occupation dested Tatooine Occupation. "
    "Oper As Planned dested Operational As Planned. "
    "Out Flank dested Outflank. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Come Here You Big Caw dested Come Here You Big Coward. "
    "I Find Your Lack of F D dested I Find Your Lack Of Faith Disturbing. "
    "There Is No Try dested There Is No Try. "
    "You Can't Hide Forever dested You Cannot Hide Forever. "
    "Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Weapon Of A Sith dested Weapon Of A Sith. "
    "Unique overcounts sheet-accurate (Elite Squadron Stormtrooper x4, "
    "Imperial Stormtrooper x6, Intensify The Forward Batteries x2, Trooper Assault x2, "
    "Ghhhk & Those Rebels Won't Escape Us x2, Tatooine Occupation x2, "
    "Imperial Domination x2, Operational As Planned x2, Imperial Command x3, "
    "Lightsaber Deficiency x2, Outflank x2, Wounded Warrior x2, Coordinated Attack x2). "
    "(V) from the checkbox."
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
    n("Yavin 4: Massassi War Room", True),
    n("Home One: War Room"),
    n("Elegant Lightsaber", True, qty=2),
    n("Endor: Back Door"),
    n("Coruscant: Jedi Council Chamber"),
    n("Obi-Wan Kenobi", True),
    n("Master Qui-Gon", True, qty=2),
    n("Chewie, Enraged", qty=2),
    n("Lando Calrissian, Scoundrel", True, qty=2),
    n("Leia, Rebel Princess"),
    n("Boushh"),
    n("Maris Brood, Fallen Jedi", True),
    n("General Solo", True, qty=2),
    n("Admiral Ackbar", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Mace Windu, Master Of The Order"),
    n("Mace Windu", True),
    n("Lady Luck", True),
    n("Home One"),
    n("Tantive IV", True),
    n("Rebel Leadership", True, qty=4),
    n("Smoke Screen", True, qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Don't Tread On Me", True),
    n("You're Quite Clever For A Human"),
    n("Weapon Levitation"),
    n("Found Someone You Have & Higher Ground", True),
    n("Sense", qty=2),
    n("Fallen Portal"),
    n("Control & Tunnel Vision"),
    n("Imperial Atrocity", True),
    n("Dark Approach", True),
    n("Speak With The Jedi Council"),
    n("Nabrun Leids"),
    n("Antilles Maneuver"),
    n("Blaster Deflection"),
    n("Clash Of Sabers"),
    n("Grimtaash"),
    n("Escape Pod", True),
    n("Houjix"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Gift Of The Master"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize"),
    n("Aim High"),
    n("Don't Do That Again"),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("Wise Advice"),
    n("Affect Mind", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = [
    n("After Her!", True),
]


DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("Imperial Entanglements / No One To Stop Us This Time"),
    n("Prepared Defenses"),
    n("Endor Shield", True),
    n("Imperial Academy Training", True),
    n("Imperial Stockpile", True),
    n("Blaster Rifle", True),
    n("Tatooine"),
    n("Tatooine: Imperial Occupation Camp", True),
    n("Devastator"),
    n("Deflector Shield Generators", True),
    n("Onyx 2"),
    n("Tatooine: Cantina"),
    n("Tatooine: Mos Espa"),
    n("Tatooine: Mos Eisley"),
    n("Elite Squadron Stormtrooper", True, qty=4),
    n("Imperial Stormtrooper", True, qty=6),
    n("Blast Points", True),
    n("Control & Set For Stun", True),
    n("Ysanne Isard", True),
    n("Darth Vader", True),
    n("Admiral Motti", True),
    n("Grand Moff Tarkin"),
    n("Grand Admiral Thrawn"),
    n("Admiral Piett"),
    n("ISB Sector Commander", True),
    n("Strategic Reserves", True),
    n("Intensify The Forward Batteries", qty=2),
    n("Trooper Assault", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Tatooine Occupation", qty=2),
    n("Imperial Domination", True, qty=2),
    n("Protocol Failure", True),
    n("Operational As Planned", True, qty=2),
    n("Imperial Command", True, qty=3),
    n("Laser Cannon Battery"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Outflank", True, qty=2),
    n("Wounded Warrior", qty=2),
    n("Coordinated Attack", True, qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Fanfare", True),
    n("Firepower"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Weapon Of A Sith"),
]
DS_ADD = [
    n("After Her!", True),
]
