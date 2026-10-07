#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Shumaker.

Source: MPC-2014-Day-1-Main-Event.pdf pages 108–109 (2013 form, 15 shields).
Name Shumaker last-name-only dested Shumaker. Username blank.
"""
from __future__ import annotations

PLAYER = "Shumaker"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 108
DS_PAGE = 109
LS_SCAN = "2014 Match Play Championship Day 1 Shumaker LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Shumaker DS.png"
LS_DECK_NAME = "8:57"
DS_DECK_NAME = "9:04"
NOTE = "Handwritten 2013 Xerox form."
PUBLIC_NOTE = "Name as written on the sheet."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Shumaker dested Shumaker. Username blank. "
    "LIGHT checked. Deck name 8:57. TIGIH dested There Is Good In Him / I Can Save Him. "
    "Help Me dested Help Me Obi-Wan Kenobi. "
    "Obi-Wan w/ Lightsaber dested Obi-Wan With Lightsaber. "
    "Qui-Gon w/ Lightsaber dested Qui-Gon Jinn With Lightsaber. "
    "AJR dested A Jedi's Resilience. SATM + BP dested "
    "Sorry About The Mess & Blaster Proficiency. Lando, Scoundrel dested "
    "Lando Calrissian, Scoundrel. Admiral Ackbar dested Admiral Ackbar. "
    "N: Battle Plains dested Naboo: Battle Plains. C: Docking Bay dested "
    "Cloud City: Platform 327 (Docking Bay). C: Chirpa's Hut dested "
    "Endor: Chief Chirpa's Hut. C: Jedi Council Chamber dested "
    "Coruscant: Jedi Council Chamber. N: Boss Nass Chambers dested "
    "Naboo: Boss Nass' Chambers. Y4 War Room dested Yavin 4: Massassi War Room. "
    "Speak w/ Jedi Council dested Speak With The Jedi Council. "
    "Tarfful Wookiee Insurgent dested Tarfful, Wookiee Insurgent. "
    "Prop Armor dested Imperial Atrocity. AFA dested Anger, Fear, Aggression. "
    "NO_DEST Let's Ride; Another Chance. "
    "Ditto (V) empty dested without (V). Unique overcounts sheet-accurate "
    "(Help Me Obi-Wan Kenobi x2, Chewie, Enraged x2, "
    "Sense x2, Rebel Barrier x2, Obi-Wan With Lightsaber x2, Wesa Gotta Grand Army x2, "
    "Qui-Gon Jinn With Lightsaber x2, A Jedi's Resilience x2, Lando Calrissian, Scoundrel x2, "
    "Speak With The Jedi Council x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Shumaker dested Shumaker. Username blank. "
    "DARK checked. Deck name 9:04. Imperial Occupancy dested Imperial Occupation / "
    "Imperial Control. Super Bombardment dested Sonic Bombardment. "
    "Armored Attack Tank dested Armored Attack Tank. AAT Laser Cannon dested "
    "AAT Laser Cannon. Commander dested Imperial Command. "
    "Bespin City Center dested Bespin: Cloud City. Mining Upper Plaza dested "
    "Cloud City: Upper Plaza Corridor. CC: Security Tower dested Cloud City: Security Tower. "
    "M: City of Heroes dested Cloud City: Downtown Plaza. M: Mining Camp HQ dested "
    "Kessel: Spice Mines - Administrator's Office. We're Fine Time dested "
    "We're All Fine Here Now, Thank You. Vader Commander dested "
    "Darth Vader, Dark Lord Of The Sith. Slave I Symbol of Fear dested "
    "Slave I, Symbol Of Fear. Everything is proceeding as planned dested I Have You Now. "
    "Apaja Rest The Throne dested A Stunning Move / A Valuable Hostage. "
    "Mandalorian Father dested Jango Fett, The Assassin. Deployment Corridor dested "
    "AT-AT Deployment Platform. Now They Began dested Now This Is Podracing. "
    "Restricted Area Workshop dested Restricted Access. Defense of Mining dested Surface Defense. "
    "AAT Assault Team dested Infantry Battle Droid. Open Fire dested Open Fire!. "
    "K+D dested Knowledge And Defense. "
    "NO_DEST Under The Black; We're All Fine Here Now, Thank You; Now This Is Podracing. "
    "Shield We Have A Plan on CC dested I Find Your Lack Of Faith Disturbing. "
    "Vader's Costume dested Vader's Cape. Unique overcounts sheet-accurate "
    "(Armored Attack Tank x4, AAT Laser Cannon x3, Darth Maul With Lightsaber x3, "
    "We're All Fine Here Now, Thank You x2, Darth Vader, Dark Lord Of The Sith x2, "
    "Defensive Fire x2, Tank Commander x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Dark Approach", True),
    n("Dark Approach"),
    n("Help Me Obi-Wan Kenobi", qty=2),
    n("Chewie, Enraged", qty=2),
    n("Rebel Leadership", True),
    n("Rebel Leadership"),
    n("Nabrun Leids"),
    n("Sense", qty=2),
    n("Home One: War Room"),
    n("Blaster Deflection", True),
    n("Blaster Deflection"),
    n("Rebel Barrier", qty=2),
    n("Speak With The Jedi Council"),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Draw Their Fire"),
    n("Anakin Skywalker"),
    n("Let's Ride"),
    n("Houjix"),
    n("Another Chance"),
    n("Corran Horn"),
    n("Don't Tread On Me", True),
    n("Admiral Ackbar", True),
    n("Naboo: Battle Plains"),
    n("Naboo"),
    n("Clash Of Sabers"),
    n("Tarfful, Wookiee Insurgent"),
    n("Escape Pod", True),
    n("Mechanical Failure"),
    n("Luke Skywalker, Jedi Knight"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Seeking An Audience", True),
    n("I Feel The Conflict"),
    n("Imperial Atrocity", True),
    n("Cloud City: Platform 327 (Docking Bay)"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Yavin 4: Massassi War Room", True),
    n("Luke's Lightsaber"),
    n("Home One"),
    n("Speak With The Jedi Council"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("He Can Go About His Business", True),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("The Professor", True),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control"),
    n("Sonic Bombardment", True),
    n("Sonic Bombardment", qty=2),
    n("Dark Maneuvers", qty=2),
    n("Armored Attack Tank", qty=4),
    n("Under The Black"),
    n("AAT Laser Cannon", qty=3),
    n("We're In Attack Position Now"),
    n("Force Push", True),
    n("Protocol Failure"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Imperial Command", True),
    n("Imperial Command"),
    n("Darth Maul With Lightsaber", qty=3),
    n("4-LOM With Concussion Rifle", True),
    n("Bespin: Cloud City"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: Security Tower", True),
    n("Cloud City: Downtown Plaza"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Tank Commander", qty=2),
    n("Infantry Battle Droid"),
    n("Surface Defense"),
    n("Defensive Fire", True),
    n("Defensive Fire"),
    n("Imperial Artillery"),
    n("We're All Fine Here Now, Thank You", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("Mist Hunter"),
    n("Cold Feet", True),
    n("Maul's Sith Infiltrator"),
    n("Count Dooku"),
    n("Lightsaber Deficiency"),
    n("Stop Motion", True),
    n("I Have You Now"),
    n("A Stunning Move / A Valuable Hostage"),
    n("Jango Fett, The Assassin"),
    n("Open Fire!"),
    n("OOM-9", True),
    n("AT-AT Deployment Platform"),
    n("Blaster Rack"),
    n("Something Special Planned For Them", True),
    n("Now This Is Podracing"),
    n("Restricted Access"),
    n("The Phantom Menace"),
    n("You Cannot Hide Forever"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Weapon Of A Sith", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever", True),
    n("Fanfare", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("There Is No Try"),
    n("Vader's Cape", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Firepower", True),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
