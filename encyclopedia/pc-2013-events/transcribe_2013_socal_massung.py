#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Anthony Massung Xerox LS+DS.

Username starwarsfan. Light deck There is good weather in San Diego.
Dark deck Set Your Course For San Diego.
"""
from __future__ import annotations

PLAYER = "Anthony Massung"
USERNAME = "starwarsfan"
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 27
DS_PAGE = 28
LS_SCAN = "2013 SoCal Grand Prix Day 1 p27 Anthony Massung LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p28 Anthony Massung DS.png"
LS_NOTE = (
    "Handwritten Print Form. Username starwarsfan. Deck title There is good weather in San Diego. "
    "TIGIH / ICSH → There Is Good In Him / I Can Save Him. Landing Platform → "
    "Endor: Landing Platform (Docking Bay). Chief Chirpa's Hut → Endor: Chief Chirpa's Hut. "
    "Luke, Rebel Scout → Luke Skywalker, Rebel Scout. Found Someone You Have combo → "
    "Found Someone You Have & Higher Ground. Wedge in Ship → Wedge In Red Squadron 1. "
    "Mace MOTO → Mace Windu, Master Of The Order. Weapon lev → Weapon Levitation. "
    "Luke, Jedi Knight (Rebel Scout struck) → Luke Skywalker, Jedi Knight. "
    "Sorry About The Mess combo → Sorry About The Mess & Blaster Proficiency. "
    "Yavin IV War Room → Yavin 4: War Room. Endor Back Door → Endor: Back Door. "
    "Jedi Council Chamber → Coruscant: Jedi Council Chamber. Gold Leader in Ship → "
    "Gold Leader In Gold 1. You've got a lot of guts... → You've Got A Lot Of Guts Coming Here. "
    "Warrior's Courage as written. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Print Form. Username starwarsfan. Deck title Set Your Course For San Diego. "
    "SYCFA / TUPITU → Set Your Course For Alderaan / The Ultimate Power In The Universe. "
    "Docking Bay 327 → Death Star: Docking Bay 327. Fendili → Rendili. "
    "DS: Central Core → Death Star: Central Core. DS: War Room → Death Star: War Room. "
    "CPI → Commence Primary Ignition. Ghhhk combo → Ghhhk & Those Rebels Won't Escape Us. "
    "He is Not Ready combo → He Is Not Ready. Overwhelmed (V) box filled then scribbled; dest Overwhelmed. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Obi-Wan Kenobi", True),
    n("Found Someone You Have & Higher Ground"),
    n("Nabrun Leids"),
    n("Speak With The Jedi Council"),
    n("Escape Pod", True),
    n("Wedge In Red Squadron 1"),
    n("Mace Windu, Master Of The Order"),
    n("Home One: War Room"),
    n("Blaster Deflection"),
    n("Houjix"),
    n("Antilles Maneuver", True),
    n("Jedi Presence"),
    n("Weapon Levitation"),
    n("Tantive IV", True),
    n("Imperial Atrocity", True),
    n("Much To Learn, You Still Have"),
    n("Luke Skywalker, Jedi Knight"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Admiral Ackbar", True),
    n("Yavin 4: War Room"),
    n("Home One"),
    n("Mace Windu", True),
    n("Clash Of Sabers"),
    n("Boushh"),
    n("Leia, Rebel Princess"),
    n("Maris Brood, Fallen Jedi"),
    n("Endor: Back Door"),
    n("Seeking An Audience", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Dark Approach", True),
    n("Gold Leader In Gold 1"),
    n("Fallen Portal"),
    n("You've Got A Lot Of Guts Coming Here"),
    n("Chewie, Enraged"),
    n("General Solo", True, qty=2),
    n("Chewie, Enraged"),
    n("Master Qui-Gon", True, qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Elegant Lightsaber", qty=2),
    n("Sense"),
    n("Warrior's Courage"),
    n("Smoke Screen", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Only Jedi Carry That Weapon"),
    n("Do, Or Do Not"),
    n("Chasm"),
    n("Yavin Sentry"),
    n("The Professor"),
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here"),
    n("Your Insight Serves You Well", True),
    n("Battle Plan"),
    n("Weapons Display"),
    n("Don't Do That Again"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Prepared Defenses", True),
    n("Kuat Drive Yards", True),
    n("Laser Cannon Battery"),
    n("Imperial Stockpile"),
    n("A Million Voices Crying Out"),
    n("Death Star: Central Core"),
    n("Death Star: War Room"),
    n("Rendili"),
    n("Nal Hutta"),
    n("Corulag"),
    n("Judicator", qty=2),
    n("Accuser"),
    n("Conquest", True),
    n("Visage"),
    n("Vengeance"),
    n("Thunderflare"),
    n("Devastator", True),
    n("Tyrant"),
    n("Victory"),
    n("U-3PO (Yoo-Threepio)"),
    n("Keder The Black"),
    n("Arica"),
    n("Emperor Palpatine"),
    n("Lord Sidious", qty=2),
    n("Superlaser"),
    n("Commence Primary Ignition", True),
    n("Intensify The Forward Batteries", qty=2),
    n("Imperial Barrier"),
    n("Cease Fire!", qty=2),
    n("Operational As Planned", True),
    n("Lightsaber Deficiency", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Overwhelmed"),
    n("TIE Sentry Ships", True),
    n("Relentless Pursuit", qty=2),
    n("Flawless Marksmanship"),
    n("Force Push", True),
    n("Nevar Yalnal", qty=2),
    n("Protocol Failure"),
    n("He Is Not Ready"),
    n("Imperial Propaganda", True),
    n("Presence Of The Force"),
    n("Dreaded Imperial Starfleet", True),
    n("Tarkin Doctrine"),
    n("Where Are You Taking Them?"),
    n("Lateral Damage", qty=2),
    n("Cease Fire!"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Abyss"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Fanfare"),
    n("You Cannot Hide Forever", True),
    n("Firepower"),
]
DS_ADD = []
