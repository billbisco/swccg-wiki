#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Brian Brodsky Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Brian Brodsky"
USERNAME = "bbrodsky50"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 15
DS_PAGE = 16
LS_SCAN = "2013 Match Play Championship p15 Brian Brodsky LS.png"
DS_SCAN = "2013 Match Play Championship p16 Brian Brodsky DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username bbrodsky50. Event MPC 2013, dated 1/26/13. "
    "Deck title 'cause Honey Badgers just don't give a shit!. Light. "
    "You Can Either Profit By This... / Or Be Destroyed. Han dested Han With Heavy Blaster Pistol. "
    "Krayt Dragon Howl + Armed/Dangerous → Armed And Dangerous & Krayt Dragon Howl. "
    "AGTP dested A Gift. Antilles Maneuver + Rebel Reinforcements as written. "
    "Run Luke Run dested Run Luke, Run!. Line 54 Tatooine site dested Tatooine: Docking Bay 94. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username bbrodsky50. Event MPC 2013, dated 1/26/13. "
    "Deck title My son calls this deck Consoco Ansaskae. Dark. "
    "Set Your Course For Alderaan / The Ultimate Power In The Universe. "
    "Alderaan and Death Star: Docking Bay 327 marked Jap Premiere. "
    "Corindan dested Chimaera. He Is Not Ready / Imperial Propagandist dested He Is Not Ready. "
    "Ghhhk + Those Rebels Won't Escape Us as written. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Tatooine: Jabba's Palace"),
    n("Han With Heavy Blaster Pistol", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Heading For The Medical Frigate"),
    n("I Must Be Allowed To Speak", True),
    n("Quick Draw", True),
    n("Seeking An Audience", True),
    n("Wesa Gotta Grand Army"),
    n("Jedi Presence"),
    n("Imperial Atrocity", True),
    n("Mechanical Failure"),
    n("Home One"),
    n("Obi-Wan Kenobi", True),
    n("Obi-Wan's Lightsaber"),
    n("Lando Calrissian, Scoundrel"),
    n("Threepio With His Parts Showing"),
    n("Chewbacca, Protector"),
    n("Flash Of Insight", True),
    n("Jedi Lightsaber", True),
    n("Rebel Leadership", True),
    n("Master Luke"),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Jedi Presence"),
    n("Run Luke, Run!"),
    n("Master Luke"),
    n("Sorry About The Mess"),
    n("Padme Naberrie", True),
    n("Yoda, Great Warrior", True),
    n("A Gift"),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Leia, Rebel Princess"),
    n("Inconsequential Barriers"),
    n("Sense"),
    n("Obi-Wan Kenobi", True),
    n("Jedi Lightsaber", True),
    n("Dodge"),
    n("Yoda, Great Warrior", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Imperial Atrocity", True),
    n("Luke's Bionic Hand", True),
    n("Master Luke"),
    n("Nabrun Leids"),
    n("A Jedi's Resilience"),
    n("Sai'torr Kal Fas", True),
    n("Admiral Ackbar", True),
    n("Tatooine: Lars' Moisture Farm", True),
    n("A Jedi's Concentration"),
    n("Courage Of A Skywalker"),
    n("Anakin's Lightsaber", True),
    n("Let The Wookiee Win", True),
    n("Rebel Leadership", True),
    n("Tatooine: Docking Bay 94", True),
    n("Home One: War Room"),
    n("Jedi Presence"),
    n("Sense"),
    n("Naboo: Boss Nass' Chambers"),
    n("Courage Of A Skywalker"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Jabba's Prize"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Ultimatum", True),
    n("Wise Advice"),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Alderaan"),
    n("Death Star: Docking Bay 327"),
    n("Prepared Defenses", True),
    n("A Million Voices Crying Out"),
    n("Imperial Stockpile", True),
    n("Laser Cannon Battery"),
    n("Kuat Drive Yards", True),
    n("Knowledge And Defense", True),
    n("Myn Kyneugh", True),
    n("Commence Primary Ignition"),
    n("Overwhelmed"),
    n("Darth Maul With Lightsaber"),
    n("TIE Sentry Ships", True),
    n("Imperial Barrier"),
    n("Tarkin Doctrine", True),
    n("Accuser", True),
    n("Darth Sidious"),
    n("Emperor Palpatine"),
    n("Control"),
    n("Force Lightning"),
    n("Tyrant"),
    n("Conquest", True),
    n("Chimaera", True),
    n("Dreaded Imperial Starfleet", True),
    n("TIE Sentry Ships", True),
    n("Victory", True),
    n("Sith Fury"),
    n("Superlaser"),
    n("Stalker"),
    n("Presence Of The Force"),
    n("Masterful Move"),
    n("A Dark Time For The Rebellion", True),
    n("Intensify The Forward Batteries"),
    n("Death Star: Central Core", True),
    n("Operational As Planned", True),
    n("Lateral Damage"),
    n("Lightsaber Deficiency", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Imperial Command", True),
    n("Cold Feet", True),
    n("Nal Hutta"),
    n("Imperial Propaganda", True),
    n("Judicator"),
    n("They're Coming In Too Fast!"),
    n("Intensify The Forward Batteries"),
    n("Devastator", True),
    n("Grand Admiral Thrawn"),
    n("Vengeance"),
    n("Operational As Planned", True),
    n("Something Special Planned For Them", True),
    n("The Phantom Menace"),
    n("Rendili"),
    n("Death Star: War Room", True),
    n("Overwhelmed"),
    n("Image Of The Dark Lord", True),
    n("He Is Not Ready", True),
    n("Thunderflare"),
    n("Darth Maul With Lightsaber"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("Fanfare", True),
    n("Firepower", True),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever"),
]
DS_ADD = []
