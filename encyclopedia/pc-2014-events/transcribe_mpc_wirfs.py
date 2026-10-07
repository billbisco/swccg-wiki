#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Chris Wirfs.

Source: MPC-2014-Day-1-Main-Event.pdf pages 124–125 (2013 form, 15 shields).
Name Chris Wirfs dested Chris Wirfs. Username blank.
"""
from __future__ import annotations

PLAYER = "Chris Wirfs"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 125
DS_PAGE = 124
LS_SCAN = "2014 Match Play Championship Day 1 Chris Wirfs LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Chris Wirfs DS.png"
LS_DECK_NAME = "IITFYS"
DS_DECK_NAME = "Iggy"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Chris Wirfs dested Chris Wirfs. Username blank. "
    "LIGHT checked. Deck name IITFYS. Event MPC. IITFYS (V) dested It Is The Future You See (V) / "
    "A Tremor In The Force (V). Lando's Luxury Yacht dested Lady Luck. "
    "Lando Calrissian, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Sorry About The Mess Combo dested Sorry About The Mess & Blaster Proficiency. "
    "WESA dested Wesa Gotta Grand Army. NOOOOOOOOO dested Wookiee Roar (V). "
    "Yoda, Master of the Force dested Yoda, Master Of The Force. "
    "Unique overcounts sheet-accurate (Rebel Leadership (V) x3, Artoo-Detoo In Red 5 x2, "
    "Mace Windu (V) x2, Sense x2, Leia, Rebel Princess x2, Jedi Levitation (V) x2, "
    "Sorry About The Mess & Blaster Proficiency x3, Wesa Gotta Grand Army x3, "
    "Luke Skywalker, Strong In The Force x2, Escape Pod (V) x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Chris Wirfs dested Chris Wirfs. Username blank. "
    "DARK checked. Deck name Iggy. Event MPC. Carbon Chamber Testing dested "
    "Carbon Chamber Testing / My Favorite Decoration. Feltipern Trevagg's Stun Rifle dested "
    "as written. Reegesh dested Reegesh. Mandalorian Father of Fett dested Jango Fett, The Assassin. "
    "Slave I Symbol of Fear dested Slave I, Symbol Of Fear. Short Range Combo dested "
    "Short Range Fighters & Watch Your Back!. Control x Set For Stun dested Control & Set For Stun. "
    "Begin Landing Your Troops & The Dark Path dested Begin Landing Your Troops & The Dark Path. "
    "Unique overcounts sheet-accurate (The Emperor (V) x2, Count Dooku x2, Imperial Artillery x2, "
    "A Dark Time For The Rebellion (V) x2, Sense x2, Defensive Fire (V) x2, Stunning Leader x2, "
    "Disarmed x2, Force Lightning x3, Sneak Attack (V) x2). NO_DEST Jabba's Prize; A Tragedy Has Occurred (shield). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("Home One: War Room"),
    n("It Is The Future You See / A Tremor In The Force", True),
    n("What're You Tryin' To Push On Us"),
    n("Sai'torr Kal Fas", True),
    n("Jedi Levitation", True),
    n("Rebel Leadership", True),
    n("Naboo: Boss Nass' Chambers", True),
    n("Naboo: Battle Plains"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Lady Luck"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Mace Windu", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Master Qui-Gon", True),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Scrambled Transmission", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Wesa Gotta Grand Army"),
    n("Wookiee Roar", True),
    n("Artoo-Detoo In Red 5"),
    n("Rebel Leadership", True),
    n("A Jedi's Resilience"),
    n("Artoo-Detoo In Red 5"),
    n("Corran Horn"),
    n("Escape Pod", True),
    n("Rebel Leadership", True),
    n("Sense"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Admiral Ackbar", True),
    n("Blaster Deflection"),
    n("Hear Me Baby, Hold Together", True),
    n("Wesa Gotta Grand Army"),
    n("Mace Windu", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force"),
    n("Sense"),
    n("Wesa Gotta Grand Army"),
    n("Weapon Levitation"),
    n("Master Qui-Gon", True),
    n("Corellian Slip", True),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Strong In The Force", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Leia, Rebel Princess"),
    n("Yoda, Master Of The Force"),
    n("Jedi Levitation", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Houjix"),
    n("Imperial Atrocity"),
    n("Escape Pod", True),
    n("Nar Shaddaa Wind Chimes", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Quick Draw", True),
    n("Home One"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Weapons Display"),
    n("Chasm", True),
    n("Ultimatum"),
    n("Planetary Defenses", True),
    n("Your Insight Serves You Well", True),
    n("Disarmed"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Affect Mind", True),
]
LS_ADD = []


DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Feltipern Trevagg's Stun Rifle", True),
    n("Carbonite Chamber Console", True),
    n("Cloud City: Carbonite Chamber"),
    n("IG-88's Neural Inhibitor", True),
    n("Jabba's Prize"),
    n("IG-88", True),
    n("Any Methods Necessary"),
    n("Despair", True),
    n("Naboo"),
    n("The Emperor", True),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Dagobah: Cave"),
    n("Jabba's Palace: Dungeon"),
    n("The Emperor", True),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Vader With Lightsaber"),
    n("4-LOM With Concussion Rifle", True),
    n("Reegesh", True),
    n("Mara Jade With Lightsaber"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Slave I, Symbol Of Fear"),
    n("Jango Fett, The Assassin"),
    n("Dr. Evazan"),
    n("Boba Fett, Prepared Hunter"),
    n("Count Dooku", qty=2),
    n("Darth Maul"),
    n("Black Sun Fleet"),
    n("Maul's Sith Infiltrator"),
    n("We Must Accelerate Our Plans"),
    n("Imperial Artillery", qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Sense", qty=2),
    n("Control & Set For Stun"),
    n("Imperial Barrier"),
    n("Sneak Attack", True),
    n("Lightsaber Deficiency", True),
    n("Defensive Fire", True, qty=2),
    n("Elis Helrot"),
    n("Stunning Leader", qty=2),
    n("U-3PO (Yoo-Threepio)"),
    n("Protocol Failure"),
    n("Disarmed", qty=2),
    n("Begin Landing Your Troops & The Dark Path", True),
    n("Jabba's Haven", True),
    n("Force Lightning", qty=3),
    n("Cold Feet", True),
    n("Sneak Attack", True),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("A Tragedy Has Occurred"),
    n("Battle Order"),
    n("Death Star Sentry", True),
    n("Come Here You Big Coward", True),
    n("Do They Have A Code Clearance"),
    n("Fanfare", True),
    n("Firepower", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
