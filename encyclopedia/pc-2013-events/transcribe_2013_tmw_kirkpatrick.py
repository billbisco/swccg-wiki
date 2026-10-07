#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1 typed slang printout: Evan Kirkpatrick LS+DS."""
from __future__ import annotations

PLAYER = "Evan Kirkpatrick"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 18
DS_PAGE = 19
LS_SCAN = "2013 Texas Mini Worlds Day 1 p18 Evan Kirkpatrick LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p19 Evan Kirkpatrick DS.png"
NOTE = "Typed slang printout (not a handwritten Xerox form)."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Commando Training"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Cantina"),
    n("Tatooine"),
    n("Home One: War Room"),
    n("Chewie, Enraged", True, qty=4),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Leia, Rebel Princess"),
    n("Han With Heavy Blaster Pistol"),
    n("Admiral Ackbar", True),
    n("Commander Wedge Antilles", True),
    n("Corran Horn"),
    n("Yoda, Great Warrior"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Artoo In Red 5", qty=2),
    n("Lady Luck"),
    n("Home One"),
    n("Tantive IV", True),
    n("Chewbacca's Bowcaster"),
    n("Imperial Atrocity", True, qty=3),
    n("Redeemed Apprentice"),
    n("Draw Their Fire"),
    n("Rebel Gunrunner"),
    n("Strikeforce", True),
    n("Escape Pod", True, qty=3),
    n("Run Luke, Run!", True, qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Use The Force", qty=2),
    n("A Jedi's Resilience"),
    n("Houjix", qty=2),
    n("The Bith Shuffle & Desperate Reach"),
    n("Out Of Commission & Transmission Terminated"),
    n("Hear Me Baby, Hold Together", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Found Someone You Have & Higher Ground"),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("Ultimatum"),
    n("Affect Mind", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("Do, Or Do Not"),
    n("Weapons Display"),
    n("Jabba's Prize", True),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Death Star: Docking Bay"),
    n("Alderaan"),
    n("Prepared Defenses", True),
    n("Kuat Drive Yards", True),
    n("A Million Voices Crying Out"),
    n("Imperial Stockpile"),
    n("Laser Cannon Battery"),
    n("Superlaser"),
    n("Commence Primary Ignition"),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Kiffex"),
    n("Corulag"),
    n("Rendili"),
    n("Darth Sidious", qty=3),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Arica"),
    n("Garindan", True),
    n("Judicator", qty=2),
    n("Tyrant"),
    n("Thunderflare"),
    n("Conquest", True),
    n("Devastator", True),
    n("Stalker", True),
    n("Visage Of The Emperor"),
    n("Victory"),
    n("Intensify The Forward Batteries", qty=2),
    n("Imperial Propaganda", True, qty=2),
    n("He Is Not Ready & Imperial Propaganda"),
    n("The Phantom Menace"),
    n("Tarkin Doctrine"),
    n("Presence Of The Force"),
    n("Protocol Failure"),
    n("Lateral Damage"),
    n("Image Of The Dark Lord", True),
    n("Relentless Pursuit", qty=2),
    n("Masterful Move"),
    n("Imperial Barrier"),
    n("Stunning Leader", qty=2),
    n("Lightsaber Deficiency", True, qty=2),
    n("Cease Fire!"),
    n("Operational As Planned"),
    n("Ghhhk & All Too Easy"),
    n("Overwhelmed", qty=2),
    n("Force Push", True),
    n("Force Field", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Resistance"),
    n("Do They Have A Code Clearance?"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Fanfare", True),
    n("Abyss", True),
]
DS_ADD = []
