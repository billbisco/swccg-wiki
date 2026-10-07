#!/usr/bin/env python3
"""2013 World Championship Day 2: Micah Wall Xerox Walkers + Profit."""
from __future__ import annotations

PLAYER = "Micah Wall"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 102
DS_PAGE = 101
LS_SCAN = "2013 Worlds Day 2 p102 Micah Wall LS.png"
DS_SCAN = "2013 Worlds Day 2 p101 Micah Wall DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Micah Wall. Username blank. Email blank. Neither Light/Dark box checked; dest Light. "
    "Do not rewrite the 2013 MPC Micah Wall leftover. "
    "Profit dested You Can Either Profit By This... / Or Be Destroyed. "
    "I Must Be Allowed To Speak dested I Must Be Allowed To Speak. "
    "Skywalker Avenger dested as written. "
    "Heading For Medical Frigate dested Heading For The Medical Frigate. "
    "Tatooine Jabba's Palace dested Tatooine: Jabba's Palace. "
    "Projection Sky dested Projection Of A Skywalker. "
    "Massassi Ruins dested Yavin 4: Massassi Ruins. "
    "Han Blaster on line 14 struck through, omitted. "
    "Ben Kenobi x2 on line 15. Line 60 writes line 15 (another Ben Kenobi). "
    "Han's Heavy Blaster dested Han With Heavy Blaster Pistol. "
    "Yoda Great Warrior dested Yoda, Great Warrior. "
    "Tatooine Utility Belt dested Tatooine Utility Belt. "
    "Don't Forget The Droids dested Don't Forget The Droids. "
    "Luke Skywalker SF dested Luke Skywalker, Rebel Scout. "
    "Lightsaber Proficiency dested Lightsaber Proficiency. "
    "Let The Wookiee Win dested Let The Wookiee Win. "
    "Blaster Deflection dested Blaster Deflection. Line 59 writes line 34. "
    "Sorry About The Mess dested Sorry About The Mess. "
    "Luke's Bionic Hand dested Luke's Bionic Hand. "
    "Hoth Echo Corridor dested Hoth: Echo Corridor. "
    "A Gift dested A Gift. "
    "R2-D2 dested R2-D2 (Artoo-Detoo). "
    "R-3PO dested R-3PO (Ar-Threepio). "
    "Sai'torr Kal Fas dested Sai'torr Kal Fas. "
    "The Force Is Strong dested The Force Is Strong With This One. "
    "Form left column reprints 37-38 on lines 39-40 are Another Weapon x2. "
    "Additional Ounee Ta / Do, Or Do Not moved to Light shields. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Micah Wall. Username blank. Email blank. Neither Light/Dark box checked; dest Dark. "
    "Do not rewrite the 2013 MPC Micah Wall leftover. "
    "Imperial Control dested Imperial Occupation / Imperial Control. "
    "Grand Admiral T dested Grand Admiral Thrawn. "
    "Marquand in BB dested Marquand In Blizzard 6. "
    "He hasn't come back dested He Hasn't Come Back Yet. "
    "WHABYE Blizzard 1 dested Blizzard 1. "
    "Slave I SoF dested Slave I, Symbol Of Fear. "
    "TM, FoF dested The Mandalorian. "
    "ISB Sec Commander dested ISB Sector Commander. "
    "Hoth Ice Plains dested Hoth: Ice Plains (5th Marker). "
    "Powergen dested Hoth: Main Power Generators (1st Marker). "
    "YMSTL dested You May Start Your Landing. "
    "Maul, YA dested Darth Maul, Young Apprentice. "
    "MJ, TEH dested Mara Jade, The Emperor's Hand. "
    "DV, DLoTS dested Darth Vader, Dark Lord Of The Sith. "
    "BP, DH dested as written. "
    "U-3PO dested U-3PO (Yoo-Threepio). "
    "Imp Walker dested Imperial Walker. "
    "Overseeing It P dested Overseeing It Personally. "
    "PoTF dested Presence Of The Force. "
    "Vader's Stick dested Vader's Lightsaber. "
    "Maul's '' dested Maul's Double-Bladed Lightsaber. "
    "IoTDL dested Image Of The Dark Lord. "
    "WIAPN dested We're In Attack Position Now. "
    "Emp Pulp dested Imperial Command. "
    "Hoth Defensive Per dested Hoth: Defensive Perimeter (3rd Marker). "
    "ADT FTR dested A Dark Time For The Rebellion. "
    "Grand Moff T dested Grand Moff Tarkin. "
    "Trample on line 50 struck; Imp Barrier dested Imperial Barrier. "
    "Flagship Ex dested Flagship Executor. "
    "Goochinal as Planet dested Coruscant. "
    "Mara's Saber dested Mara Jade's Lightsaber. "
    "Hoth Mountains dested Hoth: Mountains (6th Marker). "
    "K+D dested Knowledge And Defense. "
    "Form left column reprints 37-38 on lines 39-40 are Blizzard 4 and "
    "We're In Attack Position Now. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("I Must Be Allowed To Speak", True),
    n("Skywalker Avenger", True),
    n("Quick Draw", True),
    n("Heading For The Medical Frigate", True),
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Han Solo", True),
    n("Jabba's Palace", True),
    n("Tatooine: Jabba's Palace", True),
    n("Projection Of A Skywalker", True),
    n("Yavin 4: Massassi Ruins"),
    n("Anakin's Lightsaber", True),
    n("Padme Naberrie", True),
    n("Ben Kenobi", qty=3),
    n("Han With Heavy Blaster Pistol", True),
    n("Flash Of Insight", True, qty=2),
    n("Yoda, Great Warrior", True),
    n("Tatooine Utility Belt", True),
    n("Don't Forget The Droids"),
    n("A Jedi's Resilience"),
    n("Rycar Ryjerd", True),
    n("Rebel Barrier"),
    n("Houjix"),
    n("Luke Skywalker, Rebel Scout", qty=3),
    n("Luke's Lightsaber"),
    n("Lightsaber Proficiency"),
    n("Threepio With His Parts Showing"),
    n("Let The Wookiee Win", True),
    n("Princess Leia", True, qty=2),
    n("Blaster Deflection", qty=2),
    n("Obi-Wan Kenobi", qty=2),
    n("Another Weapon", qty=2),
    n("Chewbacca"),
    n("Sorry About The Mess"),
    n("Luke's Bionic Hand"),
    n("Hoth: Echo Corridor"),
    n("Obi-Wan's Lightsaber"),
    n("A Gift", True),
    n("Escape Pod", True),
    n("R2-D2 (Artoo-Detoo)", True),
    n("Nabrun Leids"),
    n("Chewbacca's Bowcaster"),
    n("R-3PO (Ar-Threepio)"),
    n("Fallen Portal"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Sai'torr Kal Fas", True),
    n("The Force Is Strong With This One"),
    n("Jedi Lightsaber", True),
    n("Droid Shutdown"),
]
LS_SHIELDS = [
    n("Yavin Sentry"),
    n("Aim High"),
    n("Ultimatum"),
    n("Only Jedi Carry That Weapon", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("There Is Another"),
    n("Planetary Defenses"),
    n("Don't Do That Again"),
    n("Ounee Ta"),
    n("Do, Or Do Not"),
]
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control"),
    n("Grand Admiral Thrawn"),
    n("Protocol Failure"),
    n("Marquand In Blizzard 6"),
    n("He Hasn't Come Back Yet"),
    n("Blizzard 1"),
    n("Imperial Justice"),
    n("Emperor Palpatine"),
    n("Slave I, Symbol Of Fear"),
    n("The Mandalorian"),
    n("ISB Sector Commander"),
    n("Hoth"),
    n("Hoth: Ice Plains (5th Marker)"),
    n("Hoth: Main Power Generators (1st Marker)"),
    n("Prepared Defenses", True),
    n("Blaster Rack", True),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("You May Start Your Landing"),
    n("Darth Maul, Young Apprentice"),
    n("AT-AT Cannon"),
    n("Blizzard 2", True),
    n("Mara Jade, The Emperor's Hand"),
    n("Admiral Piett"),
    n("Force Lightning", qty=2),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("BP, DH", qty=2),
    n("U-3PO (Yoo-Threepio)"),
    n("Trample"),
    n("Tempest 1"),
    n("Imperial Walker"),
    n("Overseeing It Personally"),
    n("Presence Of The Force"),
    n("Vader's Lightsaber"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Veers", True),
    n("Image Of The Dark Lord", True),
    n("Blizzard 4", True),
    n("We're In Attack Position Now"),
    n("General Veers"),
    n("Walker Garrison", qty=2),
    n("Imperial Propaganda"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("A Dark Time For The Rebellion"),
    n("Imperial Command"),
    n("Grand Moff Tarkin", True),
    n("Target The Main Generator"),
    n("Imperial Barrier"),
    n("Victory"),
    n("Hoth Blockade"),
    n("Flagship Executor"),
    n("Commander Igar"),
    n("Coruscant"),
    n("Ghhhk"),
    n("Mara Jade's Lightsaber"),
    n("Hoth: Mountains (6th Marker)"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Firepower"),
    n("Reactor Terminal"),
    n("Secret Plans"),
    n("Leave Them To Me"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("You Cannot Hide Forever"),
    n("There Is No Try"),
]
DS_ADD = []
