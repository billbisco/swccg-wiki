#!/usr/bin/env python3
"""2013 World Championship Day 2: Emil Wallin Xerox TIGH + Imperial Entanglements."""
from __future__ import annotations

PLAYER = "Emil Wallin"
USERNAME = "Darth-Link"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 107
DS_PAGE = 108
LS_SCAN = "2013 Worlds Day 2 p107 Emil Wallin LS.png"
DS_SCAN = "2013 Worlds Day 2 p108 Emil Wallin DS.png"
PUBLIC_NOTE = "Username Darth-Link."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Emil Wallin. Username Darth-Link. Email blank. LIGHT. "
    "Deck title Return of the Jedi. Event Worlds, dated 08/10/13. "
    "There Is Good In Him dested There Is Good In Him / I Can Save Him. "
    "I Feel The Conflict dested I Feel The Conflict. "
    "Luke Skywalker Rebel Scout dested Luke Skywalker, Rebel Scout. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Don't Tread On Me dested Don't Tread On Me. "
    "Mace Windu, Master of the Order dested Mace Windu, Master Of The Order. "
    "Chewie, Enraged dested Chewie, Enraged. "
    "Leia Rebel Princess dested Leia, Rebel Princess. "
    "Lando Calrissian, Scoundrel line 18 checked (V); line 19 unchecked. "
    "Master Qui-Gon dested Master Qui-Gon. "
    "Tanus Spijek dested Tanus Spijek. "
    "Yavin IV: Massassi War Room dested Yavin 4: Massassi War Room. "
    "Antilles Maneuver dested Antilles Maneuver. "
    "Control & Tunnel Vision dested Control & Tunnel Vision. "
    "Found Someone You Have & Higher Ground dested "
    "Found Someone You Have & Higher Ground. "
    "Speak w the Jedi Council dested Speak With The Jedi Council. "
    "Sorry about the mess & Blaster dested "
    "Sorry About The Mess & Blaster Proficiency. "
    "Weapon Levitation dested Weapon Levitation. "
    "You've Got A Lot Of Guts dested You've Got A Lot Of Guts Coming Here. "
    "Jabba's Prize from shields is an extra Character. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Emil Wallin. Username Darth-Link. Email blank. DARK. "
    "Deck title Imperial Entanglements. Event Worlds, dated 08/10/13. "
    "Imperial Entanglements dested Imperial Entanglements / No One To Stop Us This Time. "
    "Tatooine (Premiere) dested Tatooine. "
    "Tatooine: Imperial Vanguard Camp dested Tatooine: Imperial Vanguard Camp. "
    "Tatooine: Cantina dested Tatooine: Cantina. "
    "ISB Sector Commander dested ISB Sector Commander. "
    "A Dark Time For the Rebellion dested A Dark Time For The Rebellion. "
    "Ghhhk & Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Line 44 Imperial Arrest struck; omitted. "
    "We'll Let Fate-a Decide dested We'll Let Fate-a Decide, Huh?. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "I Find Your Lack of Faith Dist. dested I Find Your Lack Of Faith Disturbing. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("I Feel The Conflict"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Don't Tread On Me", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Boushh"),
    n("Admiral Ackbar", True),
    n("Mace Windu, Master Of The Order"),
    n("Obi-Wan Kenobi", True),
    n("General Solo", True, qty=2),
    n("Chewie, Enraged", qty=2),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel", True),
    n("Lando Calrissian, Scoundrel"),
    n("Master Qui-Gon", True, qty=2),
    n("Maris Brood, Fallen Jedi"),
    n("Tanus Spijek", True),
    n("Mace Windu", True),
    n("Elegant Lightsaber", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Home One: War Room"),
    n("Yavin 4: Massassi War Room", True),
    n("Endor: Back Door"),
    n("Antilles Maneuver", True),
    n("Blaster Deflection"),
    n("Clash Of Sabers"),
    n("Control & Tunnel Vision"),
    n("Dark Approach", True),
    n("Escape Pod", True),
    n("Fallen Portal"),
    n("Found Someone You Have & Higher Ground"),
    n("Houjix"),
    n("Nabrun Leids"),
    n("Let The Wookiee Win", True, qty=2),
    n("On The Edge"),
    n("Rebel Leadership", True, qty=3),
    n("Sense", qty=2),
    n("Smoke Screen", qty=2),
    n("Speak With The Jedi Council"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Weapon Levitation"),
    n("Imperial Atrocity", True),
    n("Seeking An Audience"),
    n("You've Got A Lot Of Guts Coming Here"),
    n("Home One"),
    n("Lady Luck"),
    n("Tantive IV", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Chasm", True),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = [
    n("Jabba's Prize"),
]


DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("Imperial Entanglements / No One To Stop Us This Time"),
    n("Devastator"),
    n("Tatooine"),
    n("Imperial Stockpile"),
    n("Imperial Academy Training", True),
    n("Endor Shield", True),
    n("Blaster Rifle", True),
    n("Prepared Defenses", True),
    n("Tatooine: Imperial Vanguard Camp"),
    n("Tatooine: Mos Eisley"),
    n("Tatooine: Mos Espa"),
    n("Tatooine: Cantina"),
    n("Deflector Shield Generators", True),
    n("Laser Cannon Battery"),
    n("Admiral Motti", True),
    n("Admiral Piett"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("ISB Sector Commander"),
    n("Elite Squadron Stormtrooper", True, qty=4),
    n("Imperial Stormtrooper", qty=6),
    n("Imperial Domination", True, qty=2),
    n("Protocol Failure"),
    n("Strategic Reserves", True),
    n("Tatooine Occupation", qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Blast Points"),
    n("Close Call", True, qty=3),
    n("Control"),
    n("Coordinated Attack", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Imperial Command", qty=3),
    n("Lightsaber Deficiency", True, qty=2),
    n("Operational As Planned", True),
    n("Outflank", True, qty=2),
    n("Trooper Assault", qty=2),
    n("Wounded Warrior", qty=2),
    n("Intensify The Forward Batteries", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
