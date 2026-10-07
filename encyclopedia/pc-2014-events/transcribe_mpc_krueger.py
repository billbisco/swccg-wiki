#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Kyle Krueger.

Source: MPC-2014-Day-1-Main-Event.pdf pages 67–68 (2013 form, 15 shields).
Name Kyle Krueger. Username Meto.
Dark Carbon Chamber Testing. Light Communing / Tatooine: Slave Quarters.
"""
from __future__ import annotations

PLAYER = "Kyle Krueger"
USERNAME = "Meto"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 68
DS_PAGE = 67
LS_SCAN = "2014 Match Play Championship Day 1 Kyle Krueger LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Kyle Krueger DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Kyle Krueger. Username Meto. LIGHT checked. "
    "Line 1 Tatooine: Slave Quarters. Line 2 Communing dested Communing. "
    "Master Kenobi dested Master Kenobi. The Bith Shuttle combo dested "
    "The Bith Shuttle & Desperate Reach. Yub Yub dested Yub Yub, Commander. "
    "Unique overcounts sheet-accurate (Anakin Skywalker, Padawan Learner x3, "
    "Luke Skywalker, Strong In The Force x3, Padme Naberrie (V) x2, "
    "All Wings Report In & Darklighter Spin x2, Escape Pod (V) x3, "
    "Jedi Levitation (V) x2, Let The Wookiee Win (V) x3, Run Luke Run (V) x2, "
    "Use The Force x2, Wesa Gotta Grand Army x3, Yub Yub, Commander x2, "
    "Artoo-Detoo In Red 5 x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Kyle Krueger. Username Meto. DARK checked. "
    "Carbon Chamber Testing dested Carbon Chamber Testing / My Favorite Decoration. "
    "Dual-title (V) empty. Fettiparr dested Fettiparr Trevaagg's Stun Rifle (V). "
    "Begin Landing dested Begin Landing Your Troops & The Dark Path. "
    "Unique overcounts sheet-accurate (Count Dooku x2, The Emperor (V) x2, "
    "A Dark Time For The Rebellion (V) x2, Defensive Fire (V) x2, Force Lightning x3, "
    "Imperial Artillery x2, Sense x2, Stunning Leader x3, Disarmed x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Jabba's Palace: Audience Chamber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Tatooine"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Anakin Skywalker, Padawan Learner", qty=3),
    n("Corran Horn"),
    n("Dash Rendar", True),
    n("Han With Heavy Blaster Pistol"),
    n("Jaina Solo"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Padme Naberrie", True, qty=2),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Yoda, Great Warrior"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Lady Luck"),
    n("Anakin's Lightsaber"),
    n("Luke's Lightsaber"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Control & Tunnel Vision"),
    n("Either Way, You Win", True),
    n("Escape Pod", True, qty=3),
    n("Houjix"),
    n("Jedi Levitation", True, qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Run Luke, Run!", True, qty=2),
    n("The Bith Shuttle & Desperate Reach"),
    n("Use The Force", qty=2),
    n("Weapon Levitation"),
    n("Wesa Gotta Grand Army", qty=3),
    n("Yub Yub, Commander", qty=2),
    n("Seeking An Audience", True),
    n("Sai'torr Kal Fas", True),
    n("Mantellian Savrip"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Planetary Defenses", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Carbon Chamber Console", True),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: Security Tower", True),
    n("Jabba's Prize"),
    n("Any Methods Necessary"),
    n("Jabba's Palace: Dungeon"),
    n("IG-88", True),
    n("IG-88's Neural Inhibitor", True),
    n("Despair", True),
    n("Blockade Flagship: Bridge"),
    n("Dagobah: Cave"),
    n("Jabba's Palace: Audience Chamber"),
    n("Naboo"),
    n("4-LOM With Concussion Rifle", True),
    n("Boba Fett, Prepared Hunter"),
    n("Count Dooku", qty=2),
    n("Darth Maul"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Dr. Evazan"),
    n("Mara Jade With Lightsaber"),
    n("The Emperor", True, qty=2),
    n("The Mandalorian, Father Of Fett"),
    n("U-3PO"),
    n("Maul's Sith Infiltrator"),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Fettiparr Trevaagg's Stun Rifle", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Close Call", True),
    n("Control & Set For Stun"),
    n("Defensive Fire", True, qty=2),
    n("Lightsaber Deficiency", True),
    n("Overload"),
    n("Elis Helrot"),
    n("Force Lightning", qty=3),
    n("Imperial Artillery", qty=2),
    n("Imperial Barrier"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sense", qty=2),
    n("Sneak Attack", True),
    n("Stunning Leader", qty=3),
    n("We Must Accelerate Our Plans"),
    n("Begin Landing Your Troops & The Dark Path"),
    n("Disarmed", qty=2),
    n("No Escape"),
    n("Protocol Failure"),
    n("Black Sun Fleet"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention"),
    n("Leave Them To Me", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
