#!/usr/bin/env python3
"""2014 US Nationals Day 1 Xerox: Matthew Harrison-Trainor.

Source: Nationals-2014-day-1.pdf pages 15–16 (2010 form).
Name MHT dested Matthew Harrison-Trainor. Day 2 already dested in transcribe_nats_mht.py.
"""
from __future__ import annotations

PLAYER = "Matthew Harrison-Trainor"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 16
DS_PAGE = 15
LS_SCAN = "2014 US Nationals Day 1 p16 Matthew Harrison-Trainor LS.png"
DS_SCAN = "2014 US Nationals Day 1 p15 Matthew Harrison-Trainor DS.png"
NOTE = "Handwritten 2010 Xerox. Name MHT dested Matthew Harrison-Trainor."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name MHT. Username blank. Deck name Nots. LIGHT Watch Your Step. "
    "WYS dested Watch Your Step. All Wings Combo dested All Wings Report In & Darklighter Spin. "
    "NQA dested No Questions Asked. LSTV dested Luke Skywalker, Jedi Knight. "
    "Mace, Moto dested Mace Windu, Master Of The Order. Insurrection & AH dested Insurrection & Aim High. "
    "HFTMF dested Heading For The Medical Frigate. Houjix & OON dested Houjix & Out Of Nowhere. "
    "Lando UH dested Lando Calrissian, Unlikely Hero. Obi in Red VII dested Obi-Wan In Red 7. "
    "CEC dested Corellian Engineering Corporation. AFA dested Anger, Fear, Aggression. "
    "DDTA dested Don't Do That Again. Unique overcounts sheet-accurate "
    "(Imperial Atrocity x2, No Questions Asked x3, Luke Skywalker, Jedi Knight x4, "
    "Antilles Maneuver x2, Wedge Antilles, Red Squadron Leader x2, Rebel Barrier x2). "
    "(V) from checkbox. "
    "NO_DEST (2014 index): You've Gotta Lot Of Guts; Obi-Wan In Red 7."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name MHT. Username blank. Deck name Nots. DARK Slavers. "
    "Slavers dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Den of Thieves & SD dested Den Of Thieves & Special Delivery. "
    "SRF + WYB dested Short Range Fighters & Watch Your Back!. "
    "Jango Fett, TA dested Jango Fett, The Assassin. Boba PH dested Boba Fett, Prepared Hunter. "
    "EPP Dengar dested Dengar With Blaster Carbine. Slave I SOF dested Slave I, Symbol Of Fear. "
    "K+D dested Knowledge And Defense. WAYITT dested Where Are You Taking This... Thing?. "
    "Jabba's Palace dested Tatooine: Jabba's Palace. "
    "IFYLOFD dested I Find Your Lack Of Faith Disturbing. Unique overcounts sheet-accurate "
    "(Masterful Move x2, Jabba The Hutt x2, Scum And Villainy x2, Sonic Bombardment x3, "
    "Outer Rim Scout x6, Short Range Fighters x3). (V) from checkbox. "
    "NO_DEST (2014 index): Daut Nund; Evading The Hutt."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step"
LS_CARDS = [
    n("Watch Your Step", True),
    n("Hiding In The Garbage", True),
    n("Corellian Retort", True),
    n("Corellian Slip"),
    n("Master Qui-Gon", True),
    n("Tarfful, Wookiee Insurgent"),
    n("You've Gotta Lot Of Guts"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("No Questions Asked", True, qty=3),
    n("Wokling", True),
    n("Palejo Reshad"),
    n("Leesub Sirln", True),
    n("Sergeant Bruckman"),
    n("Lady Luck"),
    n("Luke Skywalker, Jedi Knight", True, qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Seeking An Audience"),
    n("Insurrection & Aim High"),
    n("Heading For The Medical Frigate"),
    n("Houjix & Out Of Nowhere"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Antilles Maneuver", True, qty=2),
    n("Desperate Reach", True),
    n("Spaceport Docking Bay"),
    n("Corellia", True),
    n("Spaceport Scoundrels Guild"),
    n("Jaina Solo"),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Corran Horn"),
    n("Mirax Terrik"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Boushh"),
    n("Padme Naberrie", True),
    n("Captain Han Solo"),
    n("Chewbacca", True),
    n("Leia, Rebel Princess"),
    n("Yoda, Great Warrior"),
    n("Obi-Wan In Red 7"),
    n("Tantive IV"),
    n("Corellian Engineering Corporation", True),
    n("Spaceport City"),
    n("Spaceport Street"),
    n("Home One: Docking Bay"),
    n("Millennium Falcon", True),
    n("General Crix Madine"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Rebel Barrier", qty=2),
    n("Punch It!"),
    n("Dash Rendar"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Planetary Defenses", True),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Do, Or Do Not"),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Jabba's Prize", True),
    n("Don't Do That Again", True),
]
LS_ADD = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Affect Mind", True),
]


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Den Of Thieves & Special Delivery"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Nal Hutta"),
    n("Kashyyyk"),
    n("Kashyyyk: Skyhook Platform"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Mercenary Slavers"),
    n("Jabba's Haven"),
    n("Daut Nund"),
    n("Masterful Move", qty=2),
    n("Prince Xizor"),
    n("Velken Tezeri", True),
    n("Mercenary Pilot", True),
    n("Jabba The Hutt", True, qty=2),
    n("Hutt Bounty", True),
    n("Scum And Villainy", qty=2),
    n("Ket Maliss, Shadow Killer"),
    n("Sonic Bombardment", True, qty=3),
    n("Where Are You Taking This... Thing?"),
    n("Abyssin Ornament"),
    n("Outer Rim Scout", qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Short Range Fighters", qty=3),
    n("Sneak Attack", True),
    n("Evading The Hutt"),
    n("Ghhhk"),
    n("Monnok"),
    n("Wookiee Subjugation"),
    n("Jabba's Space Cruiser", True),
    n("Tatooine: Jabba's Palace"),
    n("Outer Rim Scout", qty=4),
    n("Bossk", True),
    n("Ephant Mon"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("OOM-9", True),
    n("Ponda Baba"),
    n("Arica"),
    n("Probe Droid"),
    n("Garindan", True),
    n("P-59"),
    n("IG-88 With Riot Gun"),
    n("Dengar With Blaster Carbine", True),
    n("U-3PO (Yoo-Threepio)"),
    n("4-LOM With Concussion Rifle"),
    n("Slave I, Symbol Of Fear"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Battle Order"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Abyss", True),
    n("There Is No Try", True),
    n("Secret Plans"),
]
DS_ADD = [
    n("Firepower", True),
    n("Allegations Of Corruption"),
    n("Oppressive Enforcement"),
]
