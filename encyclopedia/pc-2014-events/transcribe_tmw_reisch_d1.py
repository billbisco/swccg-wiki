#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 typed printouts: Nick Reisch.

Source: 2014-TMW-Day-1.pdf pages 7–8 (typed, not Xerox forms).
Handwritten header Nick Reisch DS / Nick Reisch LS.
(V) follows a trailing (v) on the printout.
Day 1 Light is Profit (Cell 2187 instead of What About That Blue One;
two R2-D2 instead of R2-D2 + Harvest). Day 1 Dark is Court.
"""
from __future__ import annotations

PLAYER = "Nick Reisch"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2014 Texas Mini Worlds Day 1 p08 Nick Reisch LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p07 Nick Reisch DS.png"
NOTE = "Typed printout (not a handwritten Xerox form)."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Han", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Jabba's Palace"),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience", True),
    n("I Must Be Allowed To Speak", True),
    n("Cell 2187", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True, qty=2),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Yavin 4: Massassi War Room", True),
    n("Wesa Gotta Grand Army"),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber"),
    n("See-Threepio", True, qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Speak With The Jedi Council"),
    n("Visored Vision", qty=2),
    n("Nabrun Leids"),
    n("Don't Forget The Droids"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sense", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Clash Of Sabers"),
    n("Leia, Rebel Princess"),
    n("Blaster Deflection"),
    n("Lando Calrissian, Scoundrel"),
    n("Yoda, Great Warrior"),
    n("Corran Horn"),
    n("Obi-Wan's Lightsaber"),
    n("R2-D2", True, qty=2),
    n("Yoda Stew & You Do Have Your Moments"),
    n("A Gift"),
    n("Houjix"),
    n("Grimtaash"),
    n("Tawss Khaa"),
    n("Chewbacca, Protector"),
    n("Tanus Spijek", True),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Boushh"),
    n("Padmé Naberrie", True),
    n("Luke's Bionic Hand"),
    n("Obi-Wan's Journal"),
    n("Luke's Lightsaber"),
    n("Tatooine Utility Belt", True),
    n("Anakin's Lightsaber", True),
    n("Sai'torr Kal Fas"),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Affect Mind", True),
    n("Battle Plan"),
    n("Your Ship?"),
    n("He Can Go About His Business", True),
    n("Chasm", True),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []


DS_START = "Court Of The Vile Gangster / I Must Be Allowed To Speak"
DS_CARDS = [
    n("Court Of The Vile Gangster / I Must Be Allowed To Speak"),
    n("Jabba's Palace: Audience Chamber"),
    n("Tatooine: Great Pit Of Carkoon"),
    n("Jabba's Palace: Dungeon"),
    n("Twi'lek Advisor", True),
    n("Jabba's Haven"),
    n("Ni Chuba Na", True),
    n("Power Of The Hutt"),
    n("Prepared Defenses"),
    n("Desilijic Tattoo"),
    n("4-LOM With Concussion Rifle"),
    n("Probot"),
    n("P-59"),
    n("IG-88 With Riot Gun"),
    n("R2-A5", True),
    n("OOM-9"),
    n("Bane Malar, Spice Addict"),
    n("Jango Fett, The Assassin"),
    n("Ket Maliss, Shadow Killer"),
    n("Gela Yeens", True),
    n("Jodo Kast", True),
    n("Ephant Mon"),
    n("Prince Xizor"),
    n("Boba Fett, Bounty Hunter"),
    n("Garindan", True),
    n("Jabba The Hutt", True),
    n("Bib Fortuna"),
    n("Danz Borin", True),
    n("Arica", True),
    n("Boba Fett In Slave 1", True),
    n("Elis In Hinthra"),
    n("Zuckuss In Mist Hunter"),
    n("Dengar In Punishing One"),
    n("Coruscant: Docking Bay"),
    n("Coruscant: Private Platform"),
    n("Jabba's Palace: Sail Barge Passenger Deck"),
    n("Nal Hutta"),
    n("Jabba's Sail Barge", True),
    n("Sonic Bombardment", True),
    n("Operational As Planned", True),
    n("Stunning Leader"),
    n("Imperial Barrier"),
    n("Cold Feet", True),
    n("Defensive Fire & Hutt Smooch"),
    n("Imbalance & Kintan Strider", qty=2),
    n("Cease Fire"),
    n("Protocol Failure"),
    n("Lightsaber Deficiency", True),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Scum And Villainy"),
    n("Hutt Bounty", True),
    n("Hutt Influence"),
    n("First Strike"),
    n("Bossk In Hound's Tooth", True),
    n("Jabba's Space Cruiser", True),
    n("Reegesk", True),
    n("Thok & Thug", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Resistance"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Leave Them To Me", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
]
DS_ADD = []
