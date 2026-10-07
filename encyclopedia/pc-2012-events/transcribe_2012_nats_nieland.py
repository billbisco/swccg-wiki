#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Mitch Nieland.

Source: 2012NationalsDay1.pdf pages 50–51 (handwritten 2010 Xerox, 12 shields).
p50 Light Name Mitch Nieland / p51 Dark Name Mitch dested Mitch Nieland analog leftover
2014 Worlds. Username blank. LIGHT/DARK boxes empty; side from card lists.
Do not dest as Mitch Wieland.
Pack player-stubs/Mitch_Nieland.wiki.
"""
from __future__ import annotations

PLAYER = "Mitch Nieland"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 50
DS_PAGE = 51
LS_SCAN = "2012 US Nationals Day 1 Mitch Nieland LS.png"
DS_SCAN = "2012 US Nationals Day 1 Mitch Nieland DS.png"
LS_DECK_NAME = "Quiet Merc'n Colony"
DS_DECK_NAME = "R.I. Pieces"
NOTE = (
    "Handwritten 2010 Xerox. Name Mitch Nieland / Mitch dested Mitch Nieland analog leftover "
    "2014 Worlds. Username blank. LIGHT/DARK boxes empty. Do not dest as Mitch Wieland."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Mitch Nieland dested Mitch Nieland analog leftover 2014 Worlds. "
    "Username blank. LIGHT/DARK boxes empty; side from QMC card list. "
    "Do not dest as Mitch Wieland. Deck Name Quiet Merc'n Colony. "
    "LS_START Quiet Mining Colony / Independent Operation analog leftover QMC line 1. "
    "Qui-Gon with Lightsaber dested Qui-Gon Jinn With Lightsaber analog leftover Graham x2. "
    "Obi Wan with Lightsaber dested Obi-Wan With Lightsaber analog leftover Jake Nelson x2. "
    "Luke with Lightsaber dested Luke With Lightsaber analog leftover x2. "
    "Pucimer Thryss dested Pucumir Thryss analog leftover Jake Nelson 2013. "
    "Kalfalnendros dested Kal'Falnl C'ndros analog leftover. "
    "Artoo, Brave Little Droid dested Artoo, Brave Little Droid analog leftover. "
    "Gold Leader in Gold 1 dested Gold Leader In Gold 1 analog leftover. "
    "Han Chewie and the Falcon dested Han, Chewie, And The Falcon analog leftover. "
    "Houjix & Out Of Nowhere dested Houjix & Out Of Nowhere analog leftover. "
    "Out Of Commission & Transmission Terminated dested Out Of Commission & Transmission Terminated analog leftover Sokol. "
    "Anger, Fear, Aggression dested Anger, Fear, Aggression analog leftover Cooleo IN THE 60. "
    "Shield Dont do that again dested Don't Do That Again analog leftover. "
    "A tragedy has occured dested A Tragedy Has Occurred analog leftover. "
    "your insights serve you well dested Your Insight Serves You Well analog leftover. "
    "do or do not dested Do, Or Do Not analog leftover. "
    "simple tricks and nonsense dested Simple Tricks And Nonsense analog leftover. "
    "Shields 1–12. Unique 60."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Mitch dested Mitch Nieland analog leftover 2014 Worlds. "
    "Username blank. LIGHT/DARK boxes empty; side from Death Star card list. "
    "Do not dest as Mitch Wieland. Deck Name R.I. Pieces. "
    "DS_START Set Your Course For Alderaan / The Ultimate Power In The Universe analog leftover Wehner line 1. "
    "Docking Bay dested Death Star: Docking Bay 327 analog leftover. "
    "Imperial Trooper Guard Diansom dested Imperial Trooper Guard analog leftover McCune. "
    "Control & Set For Stun dested Control & Set For Stun analog leftover Burgt x2. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us analog leftover Morgan. "
    "Dreaded Imperial Fleet dested Dreaded Imperial Starfleet analog leftover McCune. "
    "Knowledge And Defense dested Knowledge And Defense analog leftover Cooleo IN THE 60. "
    "Shield Come here you big coward dested Come Here You Big Coward analog leftover. "
    "Do they have a code clearance dested Do They Have A Code Clearance? analog leftover Anderson. "
    "Allegations of corruption dested Allegations Of Corruption analog leftover. "
    "There is no try dested There Is No Try analog leftover. "
    "Shields 1–12. Unique 60."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate"),
    n("Keeping The Empire Out Forever"),
    n("Wokling"),
    n("Beldon's Eye"),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: North Corridor"),
    n("Kessel"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Lando Calrissian"),
    n("Pucumir Thryss"),
    n("Tanus Spijek"),
    n("Kebyc"),
    n("Kal'Falnl C'ndros"),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Artoo, Brave Little Droid"),
    n("Harc Seff"),
    n("Overseer"),
    n("Tantive IV"),
    n("Spiral"),
    n("Gold Leader In Gold 1"),
    n("Han, Chewie, And The Falcon"),
    n("Houjix & Out Of Nowhere"),
    n("Off The Edge"),
    n("Clash Of Sabers", qty=2),
    n("Dodge", qty=2),
    n("Alternatives To Fighting", qty=3),
    n("Jedi Levitation"),
    n("Rebel Barrier"),
    n("It Could Be Worse"),
    n("We're Doomed"),
    n("Narrow Escape", qty=2),
    n("Path Of Least Resistance", qty=4),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Cloud City Celebration"),
    n("Projection Of A Skywalker"),
    n("Lando's Not A System, He's A Man"),
    n("Imperial Atrocity", qty=2),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Aim High"),
    n("The Professor"),
    n("Wise Advice"),
    n("Weapons Display"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well"),
    n("Do, Or Do Not"),
    n("Battle Plan"),
    n("Ultimatum"),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Prepared Defenses"),
    n("Kuat Drive Yards"),
    n("A Million Voices Crying Out"),
    n("Imperial Stockpile"),
    n("Laser Cannon Battery"),
    n("Commence Primary Ignition"),
    n("Superlaser"),
    n("Death Star: Central Core"),
    n("Death Star: War Room"),
    n("Carida"),
    n("Rendili"),
    n("Kiffex"),
    n("Imperial Trooper Guard"),
    n("Devastator"),
    n("Conquest"),
    n("Thunderflare"),
    n("Avenger"),
    n("Stalker"),
    n("Judicator"),
    n("Visage"),
    n("Accuser"),
    n("Tyrant"),
    n("Vengeance"),
    n("Victory"),
    n("Control & Set For Stun", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Flawless Marksmanship", qty=3),
    n("Relentless Pursuit", qty=4),
    n("A Dark Time For The Rebellion", qty=2),
    n("Lightsaber Deficiency", qty=2),
    n("Limited Resources", qty=2),
    n("Operational As Planned", qty=2),
    n("Dreaded Imperial Starfleet"),
    n("No Escape"),
    n("Lateral Damage"),
    n("Tarkin's Doctrine", qty=2),
    n("Protocol Failure", qty=2),
    n("Enter The Bureaucrat"),
    n("Imperial Propaganda"),
    n("Image Of The Dark Lord"),
    n("Intensify The Forward Batteries", qty=3),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("A Useless Gesture"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss"),
    n("Fanfare"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Do They Have A Code Clearance?"),
    n("Firepower"),
]
DS_ADD = []
