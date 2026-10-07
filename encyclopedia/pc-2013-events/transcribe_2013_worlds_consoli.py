#!/usr/bin/env python3
"""2013 World Championship Day 2: Angelo Consoli Xerox DS + informal overlay LS."""
from __future__ import annotations

PLAYER = "Angelo Consoli"
USERNAME = "Gravityslada"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 29
DS_PAGE = 28
LS_SCAN = "2013 Worlds Day 2 p29 Angelo Consoli LS.png"
DS_SCAN = "2013 Worlds Day 2 p28 Angelo Consoli DS.png"
LS_NOTE = (
    "Informal typed overlay (rotated), not a 2010 Xerox Print Form. "
    "Angelo LS. Worlds '13. Username Gravityslada on the Dark Xerox. "
    "You Can Either Profit By This.../Or Be Destroyed dested "
    "You Can Either Profit By This... / Or Be Destroyed. "
    "Han (V) dested Han (V). Tanus Spijek dested Tanus Spijek. "
    "Owen Lars & Beru Lars struck omitted. Home One: War Room struck dested "
    "Yavin 4: Massassi War Room. "
    "He Can Go About His Business and Planetary Defenses struck dested "
    "Yavin Sentry / Your Insight Serves You Well / Affect Mind. "
    "Clash Of Sabers and Let The Wookiee Win handwritten. "
    "Boushh and Yoda, Great Warrior handwritten. "
    "15 defensive-shield slots on this overlay."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Angelo. Username Gravityslada. "
    "Event Worlds '13. Deck title Slaves. DARK. "
    "Wookiee Slaving Opo dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Den of Thieves + SD dested Den Of Thieves & Special Delivery. "
    "Mercenary Slaves dested Mercenary Slavers. "
    "Kashyyyk: Slaving Camp HQ dested Kashyyyk: Slaving Camp Headquarters. "
    "Jabba's Sail Barge: PD dested Jabba's Sail Barge: Passenger Deck. "
    "Boosk dested Bossk. Jango Fett TA dested Jango Fett, The Assassin. "
    "Boba Fett PH dested Boba Fett, Prepared Hunter. "
    "4-Lom with CR dested 4-LOM With Concussion Rifle. "
    "R2-A5 dested R2-A5 (Artoo-Ayfive). "
    "Turn it Off! x2 dested Turn It Off! Turn It Off! (one copy; that is the title). "
    "Imbalance Combo dested Imbalance & Kintan Strider. "
    "Short Range Fighters Combo dested Short Range Fighters & Watch Your Back!. "
    "Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Breached Def Combo dested Breached Defenses & Molator. "
    "Slave I SOF dested Slave I, Symbol Of Fear. "
    "Zuckuss in MH dested Zuckuss In Mist Hunter. "
    "CHYNC dested Come Here You Big Coward. "
    "We'll Let Fate dested We'll Let Fate-a Decide, Huh?. "
    "Form left column reprints 37-38 on lines 39-40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Han", True),
    n("Tawss Khaa", True),
    n("Tarfful, Wookiee Insurgent"),
    n("Sergeant Doallyn", True),
    n("Tanus Spijek", True),
    n("IL-19"),
    n("Threepio With His Parts Showing"),
    n("Artoo, Brave Little Droid", True),
    n("Chewbacca, Protector", True),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel", True),
    n("Luke Skywalker, Strong In The Force", qty=4),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Padme Naberrie", True),
    n("Boushh"),
    n("Yoda, Great Warrior"),
    n("Luke's Bionic Hand"),
    n("Tatooine Utility Belt", True),
    n("Obi-Wan's Journal"),
    n("I Must Be Allowed To Speak", True),
    n("Seeking An Audience", True),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Imperial Atrocity", True),
    n("A Gift"),
    n("Anger, Fear, Aggression", True),
    n("Rebel Barrier", qty=2),
    n("Nabrun Leids"),
    n("Sense", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Speak With The Jedi Council"),
    n("Don't Forget The Droids", True, qty=2),
    n("Blaster Deflection"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Harvest", True),
    n("Heading For The Medical Frigate"),
    n("Clash Of Sabers"),
    n("Let The Wookiee Win", True),
    n("Tatooine: Jabba's Palace"),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Yavin 4: Massassi War Room", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber"),
    n("Jabba's Palace: Audience Chamber"),
    n("Luke's Lightsaber"),
    n("Anakin's Lightsaber", True),
    n("Obi-Wan's Lightsaber"),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("Aim High", True),
    n("A Tragedy Has Occurred"),
    n("Do, Or Do Not"),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
]
LS_ADD = []

DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Den Of Thieves & Special Delivery"),
    n("Wookiee Subjugation"),
    n("Power Of The Hutt"),
    n("Jabba's Haven"),
    n("Mercenary Slavers"),
    n("Kashyyyk: Skyhook Platform"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Nal Hutta"),
    n("Outer Rim Scout", qty=5),
    n("Ponda Baba", True, qty=2),
    n("Mercenary Pilot"),
    n("IG-88 With Riot Gun"),
    n("Bossk", True),
    n("Jango Fett, The Assassin"),
    n("Dengar With Blaster Carbine", True),
    n("Prince Xizor"),
    n("Boba Fett, Prepared Hunter"),
    n("4-LOM With Concussion Rifle"),
    n("Jabba The Hutt", True),
    n("Reegesk", True),
    n("Lady Valarian"),
    n("Probot"),
    n("P-59"),
    n("Velken Tezeri", True),
    n("Ephant Mon"),
    n("Giran", True),
    n("R2-A5 (Artoo-Ayfive)", True),
    n("Lightsaber Deficiency", True, qty=2),
    n("Imperial Barrier", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Abyssin Ornament"),
    n("Turn It Off! Turn It Off!"),
    n("Imbalance & Kintan Strider"),
    n("Elis Helrot", qty=2),
    n("Force Push", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Scum And Villainy", qty=2),
    n("Hutt Bounty", True),
    n("Breached Defenses & Molator"),
    n("Protocol Failure"),
    n("Jabba's Sail Barge", True),
    n("Jabba's Space Cruiser", True),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Battle Order"),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
]
DS_ADD = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Secret Plans"),
]
