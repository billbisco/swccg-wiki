#!/usr/bin/env python3
"""2013 World Championship Day 2: Greg Shaw Xerox Wookiee Slaving + Profit."""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 86
DS_PAGE = 85
LS_SCAN = "2013 Worlds Day 2 p86 Greg Shaw LS.png"
DS_SCAN = "2013 Worlds Day 2 p85 Greg Shaw DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Greg Shaw. Username blank. LIGHT. "
    "Deck title Not Slavers. Do not rewrite the 2013 MPC Greg Shaw leftover. "
    "You Can Either Profit By This dested You Can Either Profit By This... / Or Be Destroyed. "
    "Luke Skywalker Strong in the Force dested Luke Skywalker, Strong In The Force. "
    "Lando with Vibro Ax dested Lando With Vibro-Ax. "
    "R-3PO dested R-3PO (Ar-Threepio). "
    "Don't Forget The Droids dested Don't Forget The Droids. "
    "Gift of the Mentor dested Gift Of The Mentor. "
    "Sense (Premiere) dested Sense. Trooper Utris dested Trooper Utris M'Toc. "
    "Artoo Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Additional Only Jedi Carry That Weapon / Battle Plan / A Tragedy Has Occurred "
    "moved to Light shields. "
    "Form left column reprints 37-38 on lines 39-40 are Wesa Gotta Grand Army and Harvest. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Greg Shaw. Username blank. DARK. "
    "Deck title NX Slavers. Do not rewrite the 2013 MPC Greg Shaw leftover. "
    "Wookiee Slaving Operation dested Wookiee Slaving Operation / Indentured To The Empire. "
    "The Mandalorian, FOF dested Jango Fett, The Assassin. "
    "Reegesk dested Reegesk. Ability Ability Ability dested Ability, Ability, Ability. "
    "Additional Death Star Sentry / Firepower / Secret Plans moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40 are Wookiee Subjugation and Garindan. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han Solo", True),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience", True),
    n("Quick Draw", True),
    n("I Must Be Allowed To Speak", True),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Yoda, Great Warrior", qty=2),
    n("Leia, Rebel Princess", qty=2),
    n("Chewbacca, Protector", qty=2),
    n("Corran Horn"),
    n("Padme Naberrie", True, qty=2),
    n("Lando With Vibro-Ax"),
    n("Threepio With His Parts Showing"),
    n("R-3PO (Ar-Threepio)"),
    n("Artoo, Brave Little Droid", True),
    n("Obi-Wan's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Tatooine Utility Belt", True),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=2),
    n("Harvest", True),
    n("Nabrun Leids", qty=2),
    n("Clash Of Sabers", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Don't Forget The Droids", True, qty=2),
    n("It Could Be Worse"),
    n("Jedi Levitation", True),
    n("Gift Of The Mentor"),
    n("Sense"),
    n("Trooper Utris M'Toc"),
    n("Artoo-Detoo In Red 5"),
    n("Mechanical Failure"),
    n("A Gift"),
    n("Imperial Atrocity", True, qty=3),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Weapons Display", True),
    n("He Can Go About His Business", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Wise Advice"),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Only Jedi Carry That Weapon"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Mercenary Slavers"),
    n("Jabba's Haven"),
    n("Power Of The Hutt"),
    n("Den Of Thieves & Special Delivery"),
    n("Abyssin Ornament", qty=2),
    n("Jabba The Hutt", True),
    n("Lightsaber Deficiency", True, qty=3),
    n("Breached Defenses & Molator"),
    n("Scum And Villainy"),
    n("Outer Rim Scout", qty=5),
    n("Velken Tezeri", True),
    n("Lady Valarian"),
    n("Boba Fett, Prepared Hunter"),
    n("Protocol Failure"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Imperial Barrier", qty=3),
    n("4-LOM With Concussion Rifle"),
    n("Ponda Baba", True),
    n("Sonic Bombardment", True, qty=3),
    n("Probot"),
    n("Mercenary Pilot", True),
    n("Jango Fett, The Assassin"),
    n("Prince Xizor"),
    n("Dengar With Blaster Carbine", True),
    n("Wookiee Subjugation"),
    n("Garindan", True),
    n("Ability, Ability, Ability"),
    n("Ket Maliss, Shadow Killer"),
    n("Dr. Evazan"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Slave I, Symbol Of Fear"),
    n("Kashyyyk: Skyhook Platform"),
    n("P-59"),
    n("Jabba's Space Cruiser", True),
    n("Reegesk", True),
    n("Nal Hutta"),
    n("Zuckuss In Mist Hunter"),
    n("Hutt Bounty", True),
    n("Jabba's Sail Barge", True),
    n("Ephant Mon"),
    n("Bossk With Mortar Gun", True),
    n("Look Sir, Droids"),
    n("Force Push", True),
    n("Laser Cannon Battery"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Oppressive Enforcement"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Abyss", True),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Death Star Sentry", True),
    n("Firepower"),
    n("Secret Plans"),
]
DS_ADD = []
