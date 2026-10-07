#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Matt Hanson.

Source: 2012BespinRegionals.pdf pages 33–34.
p33 Dark handwritten 2010 Xerox / p34 Light handwritten 2010 Xerox.
Name Matt Hanson dested Matt Hanson analog leftover generate_2012_nats.py CANON /
player-stubs/Matt_Hanson.wiki. Username blank.
Do not dest as Marc Hanson. Do not dest 2012 Nats Day 1 Matt Hanson 60s again.
Pack player-stubs/Matt_Hanson.wiki.
"""
from __future__ import annotations

PLAYER = "Matt Hanson"
USERNAME = ""
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 34
DS_PAGE = 33
LS_SCAN = "2012 Bespin Regionals Matt Hanson LS.png"
DS_SCAN = "2012 Bespin Regionals Matt Hanson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p33 Dark handwritten 2010 Xerox / p34 Light handwritten 2010 Xerox. "
    "Name Matt Hanson dested Matt Hanson analog leftover generate_2012_nats.py CANON / "
    "player-stubs/Matt_Hanson.wiki. Username blank. "
    "LIGHT/DARK empty both dest facing pair analog leftover Cooleo/Nelson. "
    "Event Date blank both dest both as Bespin facing pair analog leftover Cooleo. "
    "Deck Name blank. "
    "Do not dest as Marc Hanson. Do not dest 2012 Nats Day 1 Matt Hanson 60s again. "
    "Pack player-stubs/Matt_Hanson.wiki."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p34 Light. Name Matt Hanson dested Matt Hanson. Username blank. "
    "LIGHT/DARK empty dest Light from the 60 analog leftover Cooleo. Event Date blank. Deck Name blank. "
    "Line 1 MWYHL dested Mind What You Have Learned / Save You It Can analog leftover Dwyer. "
    "HFTFS dested Heading For The Medical Frigate analog leftover HFTMF Sokol. "
    "Sorry is vader dested Strong Is Vader analog leftover Dwyer. "
    "Battle Plan combo dested Battle Plan & Draw Their Fire analog leftover Dwyer. "
    "DODN/W4 dested Do, Or Do Not & Wise Advice analog leftover Dwyer. "
    "Yodas Hut dested Dagobah: Yoda's Hut analog leftover Dwyer. "
    "Dagobah Jungle dested Dagobah: Jungle analog leftover Dwyer. "
    "Bog Clearing dested Dagobah: Bog Clearing analog leftover typical. "
    "Boss Nass Chambers dested Naboo: Boss Nass' Chambers analog leftover nats Hanson. "
    "Battle plains dested Naboo: Battle Plains analog leftover typical. "
    "Sai'torr dested Sai'torr Kal Fas analog leftover nats Hanson. "
    "Projection dested Projection Of A Skywalker analog leftover McCune. "
    "Strikeforce dested Strikeforce analog leftover nats Hanson. "
    "Han Chewie Falcon dested Han, Chewie, And The Falcon analog leftover nats Hanson. "
    "H1 dested Home One analog leftover nats Hanson. "
    "Elegant lightsaber dested Elegant Lightsaber analog leftover nats Hanson. "
    "LSTK / LSJK dested Luke Skywalker, Jedi Knight analog leftover nats Hanson qty=3 unique overcount. "
    "Mace empty line 27 and True line 28 kept separate analog leftover Dwyer. "
    "Fallen Jedi True line 29 and empty line 30 kept separate analog leftover Dwyer. "
    "Obi w/ stick dested Obi-Wan With Lightsaber analog leftover nats Hanson. "
    "Screaming Teroch dest as written analog leftover empty. "
    "DoS dested Daughter Of Skywalker analog leftover typical. "
    "Padme dested Padme Naberrie analog leftover nats Hanson. "
    "Threepio w/ parts dested Threepio With His Parts Showing analog leftover nats Hanson. "
    "SATM combo dested Sorry About The Mess & Blaster Proficiency analog leftover Howland. "
    "Hur me Hold together dested Hear Me Baby, Hold Together analog leftover Howland. "
    "LTWW dested Let The Wookiee Win analog leftover nats Hanson. "
    "OOC combo dested Out Of Commission & Transmission Terminated analog leftover Massung. "
    "WYLCFM dested leftover_xerox as written analog leftover nats Hanson. "
    "Wesa dested Wesa Gotta Grand Army analog leftover nats Hanson. "
    "WCJA dest as written analog leftover nats Hanson WYLCFM. "
    "WCSS dest as written analog leftover nats Hanson WYLCFM. "
    "AJR dested A Jedi's Resilience analog leftover nats Hanson qty=2. "
    "H1 war room dested Home One: War Room analog leftover nats Hanson. "
    "AFA True IN THE 60 analog leftover nats Hanson. Unique 60 shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p33 Dark. Name Matt Hanson dested Matt Hanson. Username blank. "
    "LIGHT/DARK empty dest Dark from the 60 analog leftover Cooleo. Event Date blank. Deck Name blank. "
    "AOBS dested Agents Of Black Sun / Vengeance Of The Dark Prince analog leftover chu_d2. "
    "Coruscant : IC dested Coruscant: Imperial City analog leftover chu_d2. "
    "Ni Chuba dested Ni Chuba Na?? analog leftover nats Hanson. "
    "Ket Maliss dested analog leftover chu_d2. "
    "Establish Control dested analog leftover Bordier. "
    "YtD dested Your Destiny True analog leftover K&D IN THE 60. "
    "Cease Fire qty=2 dested Cease Fire analog leftover lookup. "
    "Dengar w/ gun dested Dengar With Blaster Carbine analog leftover Howland. "
    "Bloe Parricd dested Blow Parried analog leftover Cullen. "
    "4-LOM w/ gun dested 4-LOM With Concussion Rifle analog leftover Howland. "
    "Boba Fett Prepared dested Boba Fett, Prepared Hunter analog leftover qty=2. "
    "Jabba's Palace : AC dested Jabba's Palace: Audience Chamber analog leftover typical. "
    "The Emperor dested The Emperor analog leftover lookup. "
    "Ist Strike dested First Strike analog leftover chu_d2. "
    "CC: Security Tower dested Cloud City: Security Tower analog leftover typical. "
    "According to my design dested According To My Design analog leftover typical. "
    "Dr C / Dr. E dested Dr. Evazan analog leftover Howland qty=2. "
    "reccesk dested Reckless analog leftover dest-as-written. "
    "ZTMLL dest as written analog leftover empty. "
    "Slave 1, Symbol dested Slave I, Symbol Of Fear analog leftover Nelson. "
    "2im H dested Zuckuss In Mist Hunter analog leftover chu_d2. "
    "Coruscant : DB dested Coruscant: Docking Bay analog leftover typical. "
    "Fendor dested Endor analog leftover lookup. "
    "Ability x 3 dested Ability, Ability, Ability analog leftover Nelson. "
    "Elis dested Elis Helrot analog leftover chu_d2 qty=2. "
    "Seek to destroy dested Search And Destroy analog leftover chu_d2. "
    "Branyus dested Brangus Glee analog leftover typical. "
    "Mauler starfighter dested Mauler Mithel analog leftover typical. "
    "Scum to Villainy dested Scum And Villainy analog leftover typical. "
    "Jabba the Hutt dested Jabba The Hutt analog leftover Dwyer. "
    "Ghhk combo dested Ghhhk & Those Rebels Won't Escape Us analog leftover nats Hanson. "
    "Hidden Weapons qty=3 unique overcount. Vigo qty=3 unique overcount. "
    "Prince Xizor True qty=2. Jodo Kast True qty=2. Sonic Bombardment True qty=2. "
    "Unexpected Interruption qty=2. Disarmed qty=2. "
    "Shield 1 Useless gesture dested A Useless Gesture analog leftover extra S clip. "
    "YCHE dested You Cannot Hide Forever analog leftover nats Hanson. "
    "Well let fate dested We'll Let Fate-a Decide, Huh? analog leftover nats Hanson. "
    "Cowards / Coward dested Come Here You Big Coward analog leftover qty=2. "
    "Code Clearance dested Do They Have A Code Clearance? analog leftover nats Hanson. "
    "OPP En dested Oppressive Enforcement analog leftover typical. "
    "BO dested Battle Order analog leftover typical. "
    "Allegations dested Allegations Of Corruption analog leftover Nelson. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can"),
    n("Dagobah"),
    n("Heading For The Medical Frigate"),
    n("Strong Is Vader"),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Quick Draw"),
    n("Dagobah: Yoda's Hut"),
    n("Dagobah: Jungle"),
    n("Dagobah: Bog Clearing"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Sai'torr Kal Fas"),
    n("Seeking An Audience", True),
    n("Yoda's Hope"),
    n("Projection Of A Skywalker"),
    n("Strikeforce", True),
    n("The Way Of Things"),
    n("Han, Chewie, And The Falcon", True),
    n("Home One"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Elegant Lightsaber", True),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Mace Windu"),
    n("Mace Windu", True),
    n("Fallen Jedi", True),
    n("Fallen Jedi"),
    n("Obi-Wan With Lightsaber"),
    n("Screaming Teroch", True),
    n("Daughter Of Skywalker", True),
    n("Yoda", True),
    n("Corran Horn"),
    n("Padme Naberrie", True),
    n("Hindsight", True),
    n("Threepio With His Parts Showing"),
    n("Sorry About The Mess & Blaster Proficiency", True),
    n("Blaster Deflection", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Let The Wookiee Win"),
    n("Out Of Commission & Transmission Terminated"),
    n("We're Doomed"),
    n("WYLCFM"),
    n("Wesa Gotta Grand Army"),
    n("WCJA"),
    n("WCSS"),
    n("A Jedi's Resilience", qty=2),
    n("Home One: War Room"),
    n("Under Attack"),
    n("On The Edge"),
    n("Admiral Ackbar", True),
    n("Reflection", True),
    n("Scrambled Transmission", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("I Possess", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again"),
    n("Simple Tricks And Nonsense", True),
    n("Withdrawal"),
    n("Weapons Display"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Close Call"),
    n("He Can Go About His Business"),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Coruscant: Imperial City"),
    n("Prince Xizor", True, qty=2),
    n("Ni Chuba Na??", True),
    n("Ket Maliss", True),
    n("Establish Control", True),
    n("Your Destiny", True),
    n("Prepared Defenses"),
    n("Cease Fire", qty=2),
    n("Hidden Weapons", qty=3),
    n("Dengar With Blaster Carbine"),
    n("Blow Parried"),
    n("Vigo", qty=3),
    n("4-LOM With Concussion Rifle"),
    n("Boba Fett, Prepared Hunter", True, qty=2),
    n("No Escape"),
    n("Jabba's Palace: Audience Chamber"),
    n("The Emperor", True),
    n("First Strike"),
    n("Cloud City: Security Tower", True),
    n("Jodo Kast", True, qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("According To My Design", True),
    n("Dr. Evazan", qty=2),
    n("Reckless", True),
    n("ZTMLL"),
    n("Slave I, Symbol Of Fear", True),
    n("Zuckuss In Mist Hunter"),
    n("Coruscant: Docking Bay"),
    n("Endor"),
    n("Unexpected Interruption", qty=2),
    n("Cold Feet", True),
    n("Disarmed", qty=2),
    n("Ability, Ability, Ability", True),
    n("Elis Helrot", qty=2),
    n("Voyeur", True),
    n("Bossk", True),
    n("Imperial Barrier"),
    n("Search And Destroy"),
    n("Guri", True),
    n("P-60"),
    n("Brangus Glee", True),
    n("Mauler Mithel"),
    n("P-59"),
    n("Scum And Villainy"),
    n("Jabba The Hutt", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
]
DS_SHIELDS = [
    n("A Useless Gesture"),
    n("You Cannot Hide Forever"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Come Here You Big Coward", qty=2),
    n("Do They Have A Code Clearance?"),
    n("Resistance", True),
    n("Firepower", True),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
