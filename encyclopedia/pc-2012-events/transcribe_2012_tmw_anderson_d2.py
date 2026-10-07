#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 2 leftover Xerox: John Anderson.

Source: 2012TMWDay2.pdf pages 13–14 (handwritten 2010 Xerox, left 1-40 /
right 41-60 / 12 shields). Name John Anderson dested John Anderson analog
leftover Day 1 CANON / player-stubs/John_Anderson.wiki. Username puck71
dested Puck71 analog leftover Day 1. p13 Dark Endor Operations. p14 Light
Yavin 4: Massassi Throne Room. Do not dest as a new person.
Do not dest Day 1 TMW / 2012 Nats / 2012 MPC / 2013 TMW Anderson 60s again.
"""
from __future__ import annotations

PLAYER = "John Anderson"
USERNAME = "Puck71"
STAGE = "Day 2"
PDF = "2012 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 14
DS_PAGE = 13
LS_SCAN = "2012 Texas Mini Worlds Day 2 John Anderson LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 2 John Anderson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p13 handwritten 2010 Xerox Dark. p14 handwritten 2010 Xerox Light. "
    "Name John Anderson dested John Anderson analog leftover Day 1 CANON. "
    "Username puck71 dested Puck71 analog leftover Day 1. Event TMW Day 2 Date 4/29/12. "
    "Do not dest as a new person. Do not dest Day 1 TMW / 2012 Nats / 2012 MPC / 2013 TMW Anderson 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p14 Light Deck Name blank. LIGHT checked. "
    "Event TMW Day 2 Date 4/29/12. Name John Anderson dested John Anderson analog leftover Day 1. "
    "Username puck71 dested Puck71. "
    "Y4 Throne Room dested Yavin 4: Massassi Throne Room analog leftover Day 1. "
    "HFTMF dested Heading For The Medical Frigate analog leftover Day 1. "
    "Speak w/ Jedi Council dested Speak With The Jedi Council analog leftover Day 1 qty=2. "
    "LSJK dested Luke Skywalker, Jedi Knight analog leftover Day 1. "
    "SATM + BP dested Sorry About The Mess & Blaster Proficiency analog leftover Day 1. "
    "HCF dested Han, Chewie, And The Falcon analog leftover Day 1 qty=2. "
    "Leia RP dested Leia, Rebel Princess analog leftover Day 1. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Day 1 qty=2. "
    "Ackbar dested Admiral Ackbar analog leftover Day 1 True. "
    "Coruscant: JCC dested Coruscant: Jedi Council Chamber analog leftover Day 1 True. "
    "Smoke Screen qty=4 unique overcount sheet-accurate analog leftover Day 1. "
    "LTWW dested Let The Wookiee Win analog leftover Day 1 True. "
    "Qui-Gon w/ Saber dested Qui-Gon Jinn With Lightsaber analog leftover Day 1 qty=2. "
    "Line 32 crossed dest Clash Of Sabers analog leftover Day 1; line 45 Clash dest qty=2. "
    "Luke SITF dested Luke Skywalker, Strong In The Force analog leftover Day 1 qty=2. "
    "Armed + Dangerous + Krayt Dragon Howl dested Armed And Dangerous & Krayt Dragon Howl analog leftover Day 1. "
    "Threepio dested Threepio With His Parts Showing analog leftover Day 1 True. "
    "Line 40 dested Were You Looking For Me? analog leftover Day 1. "
    "Wesa Gotta Grand Army dested analog leftover Day 1 qty=2. "
    "Luke's Bionic Hand dested analog leftover Day 1. "
    "Hoth War Room dested Hoth: Echo War Room analog leftover Day 1. "
    "Sai'torr dested Sai'torr Kal Fas analog leftover Day 1 True. "
    "Obi w/ Saber dested Obi-Wan With Lightsaber analog leftover Day 1. "
    "Line 53 crossed dest Launching The Assault analog leftover Hendon. "
    "AFA dested Anger, Fear, Aggression analog leftover Day 1 True IN THE 60. "
    "Shield Insight dested Your Insight Serves You Well analog leftover Day 1 True. "
    "Shield DDTA dested Don't Do That Again analog leftover Day 1 True. "
    "Shield Simple Trix dested Simple Tricks And Nonsense analog leftover Day 1. "
    "Shield Tragedy dested A Tragedy Has Occurred analog leftover Day 1. "
    "Shield Yavin Sentry dested Massassi Base Sentry analog leftover True. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p13 Dark Deck Name blank. DARK checked. "
    "Event TMW Day 2 Date 4/29/12. Name John Anderson dested John Anderson analog leftover Day 1. "
    "Username puck71 dested Puck71. "
    "Eops dested Endor Operations / Imperial Outpost analog leftover Gogolen. "
    "Endor: Landing Platform dested analog leftover Swedal. "
    "Endor: Bunker dested analog leftover Swedal. "
    "Oper. As Planned dested Operational As Planned analog leftover Consoli. "
    "DS II dested Death Star II analog leftover Swedal. "
    "IAO + SP dested Imperial Arrest Order & Secret Plans analog leftover Bordier. "
    "Jerjerrod dested Moff Jerjerrod analog leftover Swedal. "
    "DS2: Coolant Shaft dested Death Star II: Coolant Shaft analog leftover Swedal. "
    "Dark Time dested A Dark Time For The Rebellion analog leftover Day 1 True qty=2. "
    "G.A. Thrawn dested Grand Admiral Thrawn analog leftover Shaw. "
    "Emperor's Reach dested Maarek Stele, The Emperor's Reach analog leftover Barnes Day 2. "
    "DS2: Docking Bay dested Death Star II: Docking Bay analog leftover Swedal. "
    "The Emperor's Back dested Weapon Levitation & The Empire's Back analog leftover Alperstein True. "
    "Imp Command dested Imperial Command analog leftover Richards Day 2 qty=2. "
    "WTAPN dested We're In Attack Position Now analog leftover Gardner qty=3. "
    "Control + SFS dested Control & Set For Stun analog leftover Richards Day 2 qty=3. "
    "DS2: Capacitors dested Death Star II: Capacitors analog leftover Swedal. "
    "Taim dested Taim & Bak Magnetic Rail Gun analog leftover. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Shaw. "
    "TTO dested That's Too Old analog leftover. "
    "Prepared dested Prepared Defenses analog leftover Day 1 True. "
    "Code Clearance dested Do They Have A Code Clearance? analog leftover Barnes Day 2. "
    "Capt. Gilad Pellaeon dested Captain Gilad Pellaeon analog leftover Barnes Day 2. "
    "WMAOP dested We Must Accelerate Our Plans analog leftover qty=2. "
    "DS2: Reactor Core dested Death Star II: Reactor Core analog leftover Swedal. "
    "Line 56 crossed dest Control analog leftover Day 1. "
    "Omni Box + It's Worse dested Ommni Box & It's Worse analog leftover Brodsky. "
    "K+D dested Knowledge And Defense analog leftover Day 1 True IN THE 60. "
    "Shield Allegations dested Allegations Of Corruption analog leftover Day 1. "
    "Shield Useless Gesture dested A Useless Gesture analog leftover Day 1 True. "
    "Shield Coward dested Come Here You Big Coward analog leftover Day 1. "
    "Shield YCHF dested You Cannot Hide Forever analog leftover Day 1 True. "
    "Shield Imperial Detention dested analog leftover Lingrell Day 2. "
    "Shield Death Star Sentry dested analog leftover Herold Day 2 True. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Wokling", True),
    n("Speak With The Jedi Council", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Rebel Leadership", True, qty=3),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Sense", qty=2),
    n("Obi-Wan's Journal"),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Admiral Ackbar", True),
    n("Kiffex"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Smoke Screen", qty=4),
    n("Let The Wookiee Win", True),
    n("Scrambled Transmission", True),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Home One"),
    n("Clash Of Sabers", qty=2),
    n("Jedi Lightsaber", True),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Mace Windu", True, qty=2),
    n("Threepio With His Parts Showing", True),
    n("Were You Looking For Me?"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Luke's Bionic Hand"),
    n("Hoth: Echo War Room"),
    n("Sai'torr Kal Fas", True),
    n("Tantive IV", True),
    n("Home One: War Room"),
    n("Luke's Lightsaber"),
    n("Obi-Wan With Lightsaber"),
    n("Seeking An Audience", True),
    n("Launching The Assault"),
    n("Draw Their Fire"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Blaster Deflection", qty=2),
    n("Corran Horn"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Battle Plan", True),
    n("Ultimatum", True),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Only Jedi Carry That Weapon"),
    n("Massassi Base Sentry", True),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Landing Platform"),
    n("Endor: Bunker"),
    n("Operational As Planned"),
    n("Death Star II"),
    n("Imperial Arrest Order & Secret Plans"),
    n("Moff Jerjerrod"),
    n("Darth Vader", True),
    n("Death Star II: Coolant Shaft"),
    n("Naboo"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Chimaera"),
    n("No Escape"),
    n("Grand Admiral Thrawn"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Death Star II: Docking Bay"),
    n("Weapon Levitation & The Empire's Back", True),
    n("Cold Feet", True),
    n("Imperial Command", qty=2),
    n("Why Didn't You Tell Me?", True),
    n("We're In Attack Position Now", qty=3),
    n("Control & Set For Stun", qty=3),
    n("Death Star II: Capacitors"),
    n("Taim & Bak Magnetic Rail Gun"),
    n("Blizzard 1", True),
    n("Imperial Barrier"),
    n("Superlaser Mark II"),
    n("Juno Eclipse, Black Leader"),
    n("Tyrant"),
    n("That's Too Old"),
    n("Blizzard 2", True),
    n("Prepared Defenses", True),
    n("Do They Have A Code Clearance?"),
    n("Igar", True),
    n("General Veers", True),
    n("Captain Gilad Pellaeon"),
    n("Conquest", True),
    n("We Must Accelerate Our Plans", qty=2),
    n("We Shall Double Our Efforts"),
    n("Twi'lek Advisor"),
    n("Admiral Motti", True),
    n("Endor Shield", True),
    n("Death Star II: Reactor Core"),
    n("Accuser", True),
    n("Victory"),
    n("Grand Moff Tarkin", True),
    n("General Nevar"),
    n("Control"),
    n("Ommni Box & It's Worse"),
    n("Spaceport Docking Bay"),
    n("Force Push", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Abyss", True),
    n("Resistance", True),
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("Oppressive Enforcement", True),
    n("There Is No Try"),
    n("Imperial Detention"),
    n("Death Star Sentry", True),
]
DS_ADD = []
