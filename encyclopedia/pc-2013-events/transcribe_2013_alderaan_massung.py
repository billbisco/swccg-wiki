#!/usr/bin/env python3
"""2013 Alderaan Regionals: Anthony Massung typed slang LS + handwritten Xerox DS.

Dark leftover Xerox is p24 SYCFA.
"""
from __future__ import annotations

PLAYER = "Anthony Massung"
USERNAME = ""
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 23
DS_PAGE = 24
LS_SCAN = "2013 Alderaan Regionals p23 Anthony Massung LS.png"
DS_SCAN = "2013 Alderaan Regionals p24 Anthony Massung DS.png"
LS_NOTE = (
    "Typed slang printout (not a handwritten Xerox form). Deck title Hyperdrive. "
    "Into the Garbage Shoot Flyboy → Into The Garbage Chute, Flyboy. "
    "Yavin 4 Sentry → Yavin Sentry. Fallen Jedi → Maris Brood, Fallen Jedi. "
    "Sorry About The Mess / Blaster Proficiency is the Reflections combo."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). Name Anthony Massung. "
    "Username blank. Event Regionals. DARK checked. Deck Name SYC. "
    "SYCFA / Ultimate Power empty dested Set Your Course For Alderaan / "
    "The Ultimate Power In The Universe. DS Docking Bay dested Death Star: Docking Bay 327. "
    "Kuat DY dested Kuat Drive Yards. Million Voices dested A Million Voices Crying Out. "
    "Victory dested Victory as written. Presence of the Force dested Presence Of The Force. "
    "Intensify Forward Batteries dested Intensify The Forward Batteries. "
    "He is Not Ready Combo dested He Is Not Ready. Maul w stick dested "
    "Darth Maul With Lightsaber. Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "lat damage dested Lateral Damage. they're coming in too fast dested "
    "They're Coming In Too Fast!. Phantom Menace dested The Phantom Menace. "
    "Tarkin's Doctrine dested as written. CPI dested Commence Primary Ignition. "
    "Op as Planned dested Operational As Planned. You've Never Won a Race dested "
    "You've Never Won A Race (shield). Code Clearance dested Do They Have A Code Clearance?. "
    "Let Fate Decide dested We'll Let Fate-a Decide, Huh?."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


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
    n("Victory"),
    n("Presence Of The Force"),
    n("Intensify The Forward Batteries"),
    n("Thunderflare"),
    n("Dominator", True),
    n("Lord Sidious", qty=3),
    n("Intensify The Forward Batteries"),
    n("Imperial Decree"),
    n("He Is Not Ready"),
    n("Death Star: Central Core"),
    n("Tarkin's Bounty", True),
    n("Relentless Pursuit", qty=2),
    n("Alter", True),
    n("Devastator", True),
    n("Operational As Planned", True, qty=2),
    n("Protocol Failure", qty=2),
    n("Judicator", qty=2),
    n("Lightsaber Deficiency", True, qty=2),
    n("Force Field", True, qty=2),
    n("Death Star: War Room"),
    n("Flawless Marksmanship"),
    n("Elite Squadron Stormtrooper", True),
    n("Force Push", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Kiffex"),
    n("Tyrant"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Enter The Bureaucrat"),
    n("Superlaser"),
    n("Accuser"),
    n("Carida"),
    n("TIE Sentry Ships", True),
    n("Rendili"),
    n("Lateral Damage"),
    n("They're Coming In Too Fast!"),
    n("The Phantom Menace"),
    n("Tarkin's Doctrine"),
    n("Conquest", True),
    n("Commence Primary Ignition", True),
    n("Stalker"),
    n("Why Didn't You Tell Me", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("You've Never Won A Race"),
    n("Abyss", True),
    n("Fanfare", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
    n("Secret Plans", True),
    n("There Is No Try"),
    n("Resistance"),
    n("Firepower", True),
]
DS_ADD = [
    n("Battle Order"),
    n("Allegations Of Corruption"),
]

LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: City Outskirts"),
    n("Credits Will Do Fine"),
    n("Rycar Ryjerd", True),
    n("A Remote Planet", True),
    n("Quick Draw", True),
    n("Heading For The Medical Frigate"),
    n("Into The Garbage Chute, Flyboy", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Let The Wookiee Win", True),
    n("Blaster Deflection", True, qty=2),
    n("Rebel Barrier", qty=2),
    n("Clash Of Sabers", qty=2),
    n("Alter", True),
    n("Found Someone You Have & Higher Ground"),
    n("Might Of The Republic"),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Naboo: Boss Nass' Chambers"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Sorry About The Mess", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Guardian's Lightsaber"),
    n("Obi-Wan's Journal"),
    n("Obi-Wan's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("I Hope She's All Right"),
    n("Lightsaber Proficiency"),
    n("Meditation"),
    n("Advantage"),
    n("Disarmed", qty=2),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Senator Jar Jar Binks"),
    n("Maris Brood, Fallen Jedi", qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Senator Padme Amidala"),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Dark Approach", True),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Chasm", True),
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
    n("He Can Go About His Business", True),
]
LS_ADD = []
