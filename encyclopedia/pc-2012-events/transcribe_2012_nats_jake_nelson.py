#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Jake Nelson.

Source: 2012NationalsDay1.pdf pages 48–49 (handwritten 2010 Xerox, 12 shields blank).
p48 Light / p49 Dark Name Jake N dested Jake Nelson analog leftover 2013 Worlds.
Username blank. LIGHT/DARK boxes empty; side from card lists.
Do not dest as Aaron Nelson.
Pack player-stubs/Jake_Nelson.wiki.
"""
from __future__ import annotations

PLAYER = "Jake Nelson"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 48
DS_PAGE = 49
LS_SCAN = "2012 US Nationals Day 1 Jake Nelson LS.png"
DS_SCAN = "2012 US Nationals Day 1 Jake Nelson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Jake N dested Jake Nelson analog leftover 2013 Worlds. "
    "Username blank. LIGHT/DARK boxes empty. Shields blank skip."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Jake N dested Jake Nelson analog leftover 2013 Worlds. "
    "Username blank. LIGHT/DARK boxes empty; side from Senate card list. "
    "Do not dest as Aaron Nelson. Line 1 Han Chewie Falcon empty. "
    "LS_START Plead My Case To The Senate / Sanity And Compassion analog leftover Senate sites "
    "(Palpatine, Senate, Council Chamber, Amidala, Gungans) not written on line 1. "
    "The Bith Shuffle Combo dested The Bith Shuffle & Desperate Reach analog leftover x2. "
    "Insurrection combo dested Insurrection & Aim High analog leftover Morgan. "
    "Luke w/ stick dested Luke With Lightsaber analog leftover x2. "
    "Obi w/ stick dested Obi-Wan With Lightsaber analog leftover Graham x4. "
    "Honor dested Honor Of The Jedi analog leftover Skilton. "
    "Weapon Lev dested Weapon Levitation analog leftover Brady. "
    "Atrocity dested Imperial Atrocity analog leftover. "
    "Medical Frigate dested Heading For The Medical Frigate analog leftover. "
    "Council Chamber dested Coruscant: Jedi Council Chamber analog leftover Morgan. "
    "Senate dested Coruscant: Galactic Senate analog leftover. "
    "Jar Jar dested Senator Jar Jar Binks analog leftover Brodsky x2. "
    "Night Club dested Coruscant: Night Club analog leftover Morgan. "
    "Palpatine dested Senator Palpatine analog leftover x4. "
    "Yoda dested Yoda, Senior Council Member analog leftover Frafjord. "
    "Gungan dested Gungan Warrior analog leftover Aue x3. "
    "Hear Me Baby dested Hear Me Baby, Hold Together analog leftover. "
    "Shields 1–12 blank skip. Unique 60."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Jake N dested Jake Nelson analog leftover 2013 Worlds. "
    "Username blank. LIGHT/DARK boxes empty; side from Death Star card list. "
    "Do not dest as Aaron Nelson. Line 1 Death Star empty. "
    "DS_START Set Your Course For Alderaan / The Ultimate Power In The Universe analog leftover Wehner. "
    "Docking Bay dested Death Star: Docking Bay 327 analog leftover. "
    "Super DS dested Superlaser Mark II analog leftover Baroni. "
    "Forward Batteries dested Intensify The Forward Batteries analog leftover Massung. "
    "Executor dested Flagship Executor analog leftover Burgt. "
    "Central Core dested Death Star: Central Core analog leftover. "
    "Let Them dested Let Them Make The First Move analog leftover Molitor. "
    "Control + SFS dested Control & Set For Stun analog leftover Burgt. "
    "LS Deficiency dested Lightsaber Deficiency analog leftover Brady. "
    "Planet Defender dested Planet Defender Ion Cannon analog leftover Jeffrey. "
    "Trooper Guard dested Imperial Trooper Guard analog leftover. "
    "Set Your Course For Alderaan dested Set Your Course For Alderaan analog leftover line 59. "
    "Knowledge And Defense dested Knowledge And Defense analog leftover Cooleo IN THE 60. "
    "Shields 1–12 blank skip. Unique 60."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Han, Chewie, And The Falcon"),
    n("Artoo-Detoo In Red 5"),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Might Of The Republic", qty=3),
    n("Impressive, Most Impressive"),
    n("A Jedi's Resilience", qty=3),
    n("Insurrection & Aim High"),
    n("Your Insight Serves You Well"),
    n("Luke Skywalker, Jedi Knight"),
    n("Corran Horn", qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=4),
    n("Lando Calrissian, Scoundrel"),
    n("Poly Effect", qty=4),
    n("Houjix"),
    n("Honor Of The Jedi"),
    n("Weapon Levitation"),
    n("Imperial Atrocity"),
    n("Heading For The Medical Frigate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("Strike Planning"),
    n("Wokling"),
    n("Bail Organa"),
    n("Senator Jar Jar Binks", qty=2),
    n("Coruscant: Night Club"),
    n("Senator Palpatine", qty=4),
    n("Mon Mothma", qty=2),
    n("Gungan Orb"),
    n("Queen Amidala, Ruler Of Naboo", qty=5),
    n("Yoda, Senior Council Member"),
    n("Gungan Warrior", qty=3),
    n("Prince 55"),
    n("Hear Me Baby, Hold Together"),
    n("Gungan Fighter"),
    n("Knowledge"),
]
LS_SHIELDS = []
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Superlaser"),
    n("Superlaser Mark II"),
    n("Laser Cannon"),
    n("Trash Pit"),
    n("Intensify The Forward Batteries"),
    n("No Escape"),
    n("Dreaded Star Fleet"),
    n("Conquest"),
    n("Victory"),
    n("Flagship Executor"),
    n("Superlaser"),
    n("Presence Of Force"),
    n("Commander Igar"),
    n("Traitor"),
    n("Death Star: War Room"),
    n("Death Star: Central Core"),
    n("Avenger"),
    n("Vengeance"),
    n("Relentless Pursuit"),
    n("Let Them Make The First Move"),
    n("Power Pivot"),
    n("TIE Sentry Ships"),
    n("Flawless Marksmanship"),
    n("Tarkin's Doctrine"),
    n("Operational As Planned"),
    n("Control & Set For Stun"),
    n("Flawless Marksmanship", qty=2),
    n("Sidious"),
    n("Coruscant"),
    n("Victory"),
    n("Thunderflare"),
    n("Relentless Pursuit"),
    n("Something Special Planned For Them"),
    n("Stalker"),
    n("A Dark Time For The Rebellion"),
    n("Tyrant"),
    n("Lightsaber Deficiency"),
    n("Rendili"),
    n("Sneak Attack"),
    n("Control & Set For Stun"),
    n("Devastator"),
    n("Image Of The Dark Lord"),
    n("Tyrant"),
    n("Planet Defender Ion Cannon", qty=2),
    n("Thunderflare"),
    n("Intensify The Forward Batteries"),
    n("Lightsaber Deficiency"),
    n("Relentless Pursuit"),
    n("Flagship Executor"),
    n("Operational As Planned"),
    n("Imperial Trooper Guard"),
    n("He Is Not Ready"),
    n("Tarkin's Doctrine"),
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = []
DS_ADD = []
