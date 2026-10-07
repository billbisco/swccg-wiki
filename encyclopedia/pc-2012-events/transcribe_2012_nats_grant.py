#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Grant B.

Source: 2012NationalsDay1.pdf pages 5–6 (typed 2010 Xerox, 12 shields; 11–12 blank skip).
Name Grant B. dested Grant B as written. Username Grant-Irish.
p05 Light Freedom? I Restore Dat. / Restore Freedom To The Galaxy.
p06 Dark Podracing=Lame? No... / Agents Of Black Sun.
Do not dest as Braeden Grant. Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Grant B"
USERNAME = "Grant-Irish"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2012 US Nationals Day 1 Grant B LS.png"
DS_SCAN = "2012 US Nationals Day 1 Grant B DS.png"
LS_DECK_NAME = "Freedom? I Restore Dat."
DS_DECK_NAME = "Podracing=Lame? No..."
NOTE = "Typed 2010 Xerox form."
LS_NOTE = (
    "Typed 2010 Xerox. Name Grant B. dested Grant B as written. Username Grant-Irish. "
    "LIGHT checked. Deck Name Freedom? I Restore Dat. Event Nationals Date 6/9/12. "
    "Do not dest as Braeden Grant. Do not dest as a new person. "
    "Restore Freedom To The Galaxy True dested Restore Freedom To The Galaxy True "
    "(virtual-only objective dest without extra (V)). "
    "Yavin 4 True dested Yavin 4 True (starting location). "
    "Yavin 4: Massassi Headquarters dested Starting. "
    "Lieutenant Tarn Mison dested analog leftover Anderson Tarn Mison. "
    "Derek 'Hobbie' Klivian dested Derek \"Hobbie\" Klivian True analog leftover Anderson. "
    "Red Squadron 1 dested Red Squadron 1 analog leftover Srodoski. "
    "X-Wing Laser Cannon dested X-wing Laser Cannon analog leftover Erwin. "
    "Stay Sharp dested Stay Sharp! analog leftover Brian Day2. "
    "Darklighter Spin / All Wings Report In dested All Wings Report In & Darklighter Spin analog leftover Erwin. "
    "Luke's Back dested Luke's Back True leftover_xerox (not Luke's Backpack). "
    "Antilles Maneuver & Rebel Reinforcements True dested analog leftover. "
    "Massassi Base Sentry dested analog leftover. "
    "Projection of a Skywalker dested Projection Of A Skywalker analog leftover Erwin. "
    "I'm With You Too dested I'm With You Too True analog leftover Kelly. "
    "Eject! Eject! & Imperial Atrocity dested Eject! Eject! Eject! & Imperial Atrocity True analog leftover Jourdan. "
    "Shield Ounee Ta dested analog leftover Foth. "
    "Shields 11–12 blank skip. Unique overcounts sheet-accurate "
    "(Artoo-Detoo In Red 5 x2, X-wing Laser Cannon x4, Power Pivot x2, "
    "It Could Be Worse x2, Organized Attack x2, Rebel Barrier x2, "
    "Projection Of A Skywalker x2, Eject! Eject! Eject! & Imperial Atrocity True x2). "
    "(V) from checkbox."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name Grant B. dested Grant B as written. Username Grant- Irish dested Grant-Irish. "
    "DARK checked. Deck Name Podracing=Lame? No... Event Nationals Date 6/9/12. "
    "Do not dest as Braeden Grant. Do not dest as a new person. "
    "Agents Of Black Sun empty dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Start Your Engines dested Start Your Engines! analog leftover Lingrell. "
    "Tatooine: Podrace Arena dested analog leftover Lingrell. "
    "Boonta Eve Podrace dested analog leftover Lingrell. "
    "Sebulba's Podracer dested analog leftover Lingrell. "
    "Coruscant dested Coruscant (Dark) analog leftover Aue. "
    "Shada dested Shada True analog leftover Lingrell. "
    "Kitik Keed'kak dested Kitik Keed'kak True analog leftover Aue. "
    "Sy Snootles dested analog leftover Foth. "
    "IG-88 With Riot Gun dested analog leftover Foth. "
    "P-60 dested analog leftover Gemme. "
    "Bossk In Hound's Tooth dested analog leftover Aue. "
    "Dengar In Punishing One dested analog leftover Lingrell. "
    "Hoth: Wampa Cave dested Hoth: Wampa Cave (7th Marker) analog leftover Lingrell. "
    "Cloud City: Security Tower dested analog leftover Krueger. "
    "Control & Set For Stun dested analog leftover Amato. "
    "Elis Helrot dested analog leftover. "
    "I'd Just As Soon Kiss A Wookiee dested analog leftover Lingrell. "
    "ComScan Detection dested analog leftover Banger. "
    "I've Lost Artoo dested I've Lost Artoo! True analog leftover Ziagos. "
    "Dark Reconnaissance dested analog leftover Lingrell. "
    "Ni Chuba Na dested Ni Chuba Na?? True analog leftover Aue. "
    "Jabba's Haven dested analog leftover Lingrell. "
    "Shields 11–12 blank skip. Unique overcounts sheet-accurate "
    "(Arica True x2, Aurra Sing x2, Trophy Of A Kill True x3, Control & Set For Stun x2, "
    "Elis Helrot x2, Imperial Barrier x3, Stunning Leader True x3, "
    "A Dark Time For The Rebellion True x4, Operational As Planned True x2, "
    "I'd Just As Soon Kiss A Wookiee x2, Presence Of The Force x2). "
    "(V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Restore Freedom To The Galaxy"
LS_CARDS = [
    n("Restore Freedom To The Galaxy", True),
    n("Yavin 4", True),
    n("Yavin 4: Massassi Headquarters"),
    n("Careful Planning", True),
    n("Squadron Assignments"),
    n("Luke, Trust Me", True),
    n("Rycar Ryjerd", True),
    n("Anger, Fear, Aggression", True),
    n("Luke Skywalker", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Elyhek Rue"),
    n("Lieutenant Naytaan"),
    n("Lieutenant Tarn Mison"),
    n("Jek Porkins", True),
    n("Derek \"Hobbie\" Klivian", True),
    n("Kier Santage"),
    n("Obi-Wan With Lightsaber"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Red Squadron 1"),
    n("Red 7"),
    n("Red 9"),
    n("Red 6"),
    n("Red Squadron 4"),
    n("Red Squadron 7", True),
    n("Ralltiir"),
    n("Kessel"),
    n("Yavin 4: Massassi Throne Room"),
    n("Yavin 4: Massassi War Room"),
    n("Yavin 4: Briefing Room"),
    n("X-wing Laser Cannon", qty=4),
    n("Portable Scanner"),
    n("Rebel Flight Suit"),
    n("Electrobinoculars"),
    n("Power Pivot", qty=2),
    n("Stay Sharp!"),
    n("We're Doomed"),
    n("All Wings Report In & Darklighter Spin"),
    n("Darklighter Spin"),
    n("It Could Be Worse", qty=2),
    n("Organized Attack", qty=2),
    n("Luke's Back", True),
    n("Escape Pod", True),
    n("Rebel Artillery"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Rebel Barrier", qty=2),
    n("Massassi Base Sentry", True),
    n("Legendary Starfighter"),
    n("Projection Of A Skywalker", qty=2),
    n("I'm With You Too", True),
    n("Eject! Eject! Eject! & Imperial Atrocity", True, qty=2),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("Wise Advice"),
    n("Chasm"),
    n("Do, Or Do Not"),
    n("Ounee Ta"),
    n("Weapons Display"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Your Insight Serves You Well"),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("No Bargain", True),
    n("Start Your Engines!"),
    n("Tatooine: Podrace Arena"),
    n("Boonta Eve Podrace"),
    n("Sebulba's Podracer"),
    n("Coruscant (Dark)"),
    n("Coruscant: Imperial City"),
    n("Presence Of The Force", qty=2),
    n("Shada", True),
    n("Knowledge And Defense", True),
    n("Kitik Keed'kak", True),
    n("Sy Snootles", True),
    n("Gardulla The Hutt"),
    n("Arica", True, qty=2),
    n("Prophetess", True),
    n("Rystall", True),
    n("Aurra Sing", qty=2),
    n("IG-88 With Riot Gun"),
    n("P-60"),
    n("4-LOM With Concussion Rifle", True),
    n("Gragra"),
    n("Zuckuss In Mist Hunter"),
    n("Bossk In Hound's Tooth", True),
    n("Dengar In Punishing One"),
    n("Hoth: Wampa Cave (7th Marker)"),
    n("Cloud City: Security Tower", True),
    n("Trophy Of A Kill", True, qty=3),
    n("Control"),
    n("Control & Set For Stun", qty=2),
    n("Elis Helrot", qty=2),
    n("Imperial Barrier", qty=3),
    n("Stunning Leader", True, qty=3),
    n("A Dark Time For The Rebellion", True, qty=4),
    n("Operational As Planned", True, qty=2),
    n("I'd Just As Soon Kiss A Wookiee", qty=2),
    n("Weapon Levitation"),
    n("ComScan Detection", True),
    n("Sonic Bombardment"),
    n("I've Lost Artoo!", True),
    n("Ket Maliss", True),
    n("Dark Reconnaissance", True),
    n("Ni Chuba Na??", True),
    n("Jabba's Haven", True),
]
DS_SHIELDS = [
    n("Death Star Sentry"),
    n("Leave Them To Me"),
    n("Firepower"),
    n("A Useless Gesture"),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("Battle Order"),
    n("Abyss"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
