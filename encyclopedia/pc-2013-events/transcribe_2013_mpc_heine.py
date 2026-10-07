#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Jerry Heine Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Jerry Heine"
USERNAME = "quesoSauce37"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 42
DS_PAGE = 41
LS_SCAN = "2013 Match Play Championship p42 Jerry Heine LS.png"
DS_SCAN = "2013 Match Play Championship p41 Jerry Heine DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username quesoSauce37. "
    "Deck title You got a smile that can light this town, and we might need it. Light. "
    "We'll Handle This / Duel Of The Fates. "
    "Generator Core dested Naboo: Theed Palace Generator Core. "
    "Generator dested Naboo: Theed Palace Generator. "
    "AJR dested A Jedi's Resilience. R2 in Red 5 dested Artoo-Detoo In Red 5. "
    "Nooooooooo dested NOOOOOOOOOOOO!. Yoda mofo dested Yoda, Master Of The Force. "
    "Bith Shuffle & Desperate Reach as written. Jedi Lev dested Jedi Levitation. "
    "Qui-Gon Jinn JM dested Master Qui-Gon. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username quesoSauce37. "
    "Deck title tears over beers. Dark. "
    "Set Your Course For Alderaan / The Ultimate Power In The Universe. "
    "Tarkin Doctrine as written. Stockpile dested Imperial Stockpile. "
    "Ghhhk / Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. "
    "Thunder fail dested Thunderflare. Intensity fwd Batteries dested Intensify The Forward Batteries. "
    "Vindicator dested Imperial-Class Star Destroyer. CPI dested Combat Readiness. "
    "DB 327 dested Death Star: Detention Block Corridor. "
    "Imbalance / Kintan Strider dested Imbalance & Kintan Strider. "
    "Knowledge + defense dested Knowledge And Defense. "
    "Shield Coward dested Come Here You Big Coward. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("Inner Strength"),
    n("Podrace Prep"),
    n("Tatooine: Podrace Arena"),
    n("Anakin's Podracer"),
    n("Boonta Eve Podrace"),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Rebel Barrier"),
    n("Desperate Reach", True),
    n("Houjix"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Qui-Gon's Lightsaber"),
    n("Mace Windu, Master Of The Order"),
    n("Leia, Rebel Princess"),
    n("Luke's Lightsaber"),
    n("Naboo: Boss Nass' Chambers"),
    n("A Jedi's Resilience"),
    n("Artoo-Detoo In Red 5"),
    n("NOOOOOOOOOOOO!", True),
    n("Luke's Bionic Hand"),
    n("Disarmed"),
    n("Obi-Wan Kenobi", True),
    n("Artoo-Detoo In Red 5"),
    n("Sense"),
    n("Control & Tunnel Vision"),
    n("Jedi Lightsaber", True),
    n("Mace Windu", True),
    n("Qui-Gon's Lightsaber"),
    n("Wesa Gotta Grand Army"),
    n("Dodge"),
    n("Goo Nee Tay"),
    n("Clinging To The Edge", True),
    n("I Did It!"),
    n("Imperial Atrocity", True),
    n("Yoda, Master Of The Force"),
    n("Master Qui-Gon"),
    n("Blaster Deflection"),
    n("Yoda, Master Of The Force"),
    n("Let The Wookiee Win", True),
    n("Blaster Deflection"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Wesa Gotta Grand Army"),
    n("Sense"),
    n("Imperial Atrocity", True),
    n("The Bith Shuffle & Desperate Reach"),
    n("Imperial Atrocity", True),
    n("Projection Of A Skywalker"),
    n("Weapon Levitation"),
    n("Jedi Lightsaber", True),
    n("Mace Windu", True),
    n("Master Qui-Gon"),
    n("Yoda, Master Of The Force"),
    n("Luke Skywalker, Jedi Knight"),
    n("Jedi Levitation"),
    n("Corran Horn"),
    n("Alter"),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Ultimatum", True),
    n("Only Jedi Carry That Weapon"),
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense", True),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Tarkin Doctrine"),
    n("Image Of The Dark Lord", True),
    n("Laser Cannon Battery"),
    n("A Million Voices Crying Out"),
    n("Imperial Stockpile"),
    n("Kuat Drive Yards", True),
    n("Lateral Damage"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Visage Of The Emperor"),
    n("Victory"),
    n("Force Push", True),
    n("Devastator", True),
    n("Limited Resources"),
    n("Imperial Barrier"),
    n("Imperial Propaganda", True),
    n("Operational As Planned", True),
    n("Protocol Failure", True),
    n("Lightsaber Deficiency", True),
    n("Thunderflare"),
    n("U-3PO"),
    n("Intensify The Forward Batteries"),
    n("Garindan", True),
    n("Conquest", True),
    n("Prepared Defenses"),
    n("Imperial-Class Star Destroyer"),
    n("Cold Feet", True),
    n("Arica"),
    n("Control"),
    n("Why Didn't You Tell Me", True),
    n("Something Special Planned For Them", True),
    n("A Dark Time For The Rebellion"),
    n("TIE Sentry Ships", True),
    n("Force Field", True),
    n("Combat Readiness", True),
    n("Superlaser"),
    n("Alderaan"),
    n("Death Star"),
    n("Corulag"),
    n("Nal Hutta"),
    n("Darth Sidious"),
    n("Death Star: Detention Block Corridor"),
    n("Darth Maul With Lightsaber"),
    n("Kiffex"),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Lord Sidious"),
    n("Close Call", True),
    n("Garindan", True),
    n("Accuser"),
    n("Darth Sidious"),
    n("Intensify The Forward Batteries"),
    n("Darth Maul With Lightsaber"),
    n("The Phantom Menace"),
    n("Imbalance & Kintan Strider"),
    n("Tyrant"),
    n("Overwhelmed"),
    n("Dreaded Imperial Starfleet", True),
    n("Rendili"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Death Star Sentry"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Fanfare", True),
    n("Leave Them To Me", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Resistance"),
]
DS_ADD = []
