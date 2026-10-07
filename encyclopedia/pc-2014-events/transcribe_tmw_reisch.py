#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 2 typed printouts: Nick Reisch.

Source: 2014-TMW-Day-2.pdf pages 3–4 (typed, not Xerox forms).
Handwritten header Nick Reisch LS / Nick Reisch DS.
(V) follows a trailing (v) on the printout.
"""
from __future__ import annotations

PLAYER = "Nick Reisch"
USERNAME = ""
STAGE = "Day 2"
PDF = "2014 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2014 Texas Mini Worlds Day 2 p03 Nick Reisch LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 2 p04 Nick Reisch DS.png"


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
    n("What About That Blue One?"),
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
    n("R2-D2", True),
    n("Harvest", True),
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


DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir"),
    n("Kuat Drive Yards", True),
    n("Endor Shield", True),
    n("Insignificant Rebellion", True),
    n("Prepared Defenses", True),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Prefect's Office"),
    n("Ralltiir: Spaceport Financial District"),
    n("Endor"),
    n("Kashyyyk"),
    n("Ghhhk"),
    n("He Hasn't Come Back Yet"),
    n("Evacuate", True),
    n("Trample"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Close Call", True),
    n("Outflank", True),
    n("Cold Feet", True),
    n("Imperial Barrier"),
    n("Imperial Command", qty=2),
    n("Stop Motion", True),
    n("Control & Set For Stun"),
    n("Masterful Move & Endor Occupation"),
    n("Sunsdown & Too Cold For Speeders"),
    n("Empire's New Order", True),
    n("Imperial Justice", True),
    n("Imperial Domination", True),
    n("Where Are You Taking This ... Thing?"),
    n("Blizzard 1", True),
    n("Blizzard 4"),
    n("Blizzard 2", True),
    n("Tempest 1"),
    n("Tyrant"),
    n("Victory"),
    n("Conquest", True),
    n("Devastator", True),
    n("Emperor Palpatine", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Kir Kanos With Force Pike"),
    n("Arica"),
    n("Grand Admiral Thrawn"),
    n("Garindan", True),
    n("The Emperor's Reach"),
    n("Iceheart"),
    n("Grand Moff Tarkin", True),
    n("Lieutenant Commander Ardan"),
    n("General Veers", True),
    n("Admiral Motti", True),
    n("Janus Greejatus"),
    n("General Nevar", True),
    n("Admiral Ozzel"),
    n("Colonel Davod Jon"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Imbalance & Kintan Strider"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("There Is No Try"),
    n("Abyss", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Secret Plans"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Do They Have A Code Clearance?", True),
    n("Oppressive Enforcement"),
]
DS_ADD = []
