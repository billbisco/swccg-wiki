#!/usr/bin/env python3
"""2013 World Championship Day 2 typed Print Form: Vikram Bali LS+DS."""
from __future__ import annotations

PLAYER = "Vikram Bali"
USERNAME = "DVD ROTS"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 12
DS_PAGE = 11
LS_SCAN = "2013 Worlds Day 2 p12 Vikram Bali LS.png"
DS_SCAN = "2013 Worlds Day 2 p11 Vikram Bali DS.png"
NOTE = (
    "Typed 2013 Xerox Print Form. Name field Vikram Ball dested Vikram Bali. "
    "Username DVD ROTS. Deck name You Got A Problem? on Dark. "
    "Shield 15 Affect Mind struck dested Your Insight Serves You Well. "
    "Yavin 4: Massassi War Rom dested Yavin 4: Massassi War Room. "
    "Simple Tricks and Nonsesne dested Simple Tricks And Nonsense. "
    "A Tragedy Has Occured dested A Tragedy Has Occurred."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Anger, Fear, Aggression", True),
    n("Podrace Prep"),
    n("Tatooine: Podrace Arena"),
    n("Anakin's Podracer"),
    n("Boonta Eve Podrace"),
    n("Civil Disorder", True),
    n("Goo Nee Tay"),
    n("Honor Of The Jedi"),
    n("I Did It!"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Padme Naberrie", True),
    n("Leia", True),
    n("Corran Horn"),
    n("Dash Rendar", True),
    n("Admiral Ackbar", True),
    n("Threepio With His Parts Showing"),
    n("Home One"),
    n("Han, Chewie, And The Falcon"),
    n("Han, Chewie, And The Falcon", True),
    n("Tantive IV", True),
    n("Spiral"),
    n("Wedge In Red Squadron 1"),
    n("Gold Leader In Gold 1", True),
    n("Draw Their Fire"),
    n("Down With The Emperor!", True),
    n("Strikeforce", True),
    n("Seeking An Audience", True),
    n("Revolution", qty=5),
    n("Mantellian Savrip"),
    n("Escape Pod", True),
    n("Hear Me Baby, Hold Together", True),
    n("Clash Of Sabers"),
    n("Houjix"),
    n("A Jedi's Resilience", True),
    n("A Jedi's Resilience", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Hoth: Echo Command Center (War Room)"),
    n("Malastare"),
    n("Naboo: Boss Nass' Chambers"),
    n("Yavin 4: Massassi War Room", True),
    n("Home One: War Room"),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("Ultimatum"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("He Can Go About His Business", True),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Knowledge And Defense", True),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Prepared Defenses", True),
    n("Kuat Drive Yards", True),
    n("Imperial Stockpile"),
    n("A Million Voices Crying Out"),
    n("Laser Cannon Battery"),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Commence Primary Ignition", True),
    n("Superlaser"),
    n("Nal Hutta"),
    n("Corulag"),
    n("Rendili"),
    n("Emperor Palpatine", qty=2),
    n("Darth Sidious"),
    n("Arica"),
    n("Keder The Black"),
    n("U-3PO (Yoo-Threepio)"),
    n("Judicator", qty=2),
    n("Victory"),
    n("Accuser"),
    n("Conquest", True),
    n("Devastator", True),
    n("Thunderflare"),
    n("Tyrant"),
    n("Vengeance"),
    n("Visage"),
    n("Lateral Damage", qty=2),
    n("Protocol Failure"),
    n("He Is Not Ready", True),
    n("Imperial Propaganda", True),
    n("Tarkin Doctrine"),
    n("Where Are You Taking Them?"),
    n("Dreaded Imperial Starfleet", True),
    n("Presence Of The Force"),
    n("Cease Fire", qty=3),
    n("Nevar Yalnal", qty=2),
    n("Imperial Barrier"),
    n("Lightsaber Deficiency", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Operational As Planned", True),
    n("TIE Sentry Ships", True),
    n("Relentless Pursuit", qty=2),
    n("Overwhelmed", qty=2),
    n("Force Push", True),
    n("Intensify The Forward Batteries", qty=2),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
