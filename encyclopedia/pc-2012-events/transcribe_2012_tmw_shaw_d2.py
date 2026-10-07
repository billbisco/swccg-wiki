#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 2 leftover Xerox: Greg Shaw.

Source: 2012TMWDay2.pdf pages 9–10 (handwritten 2010 Xerox, left 1-40 /
right 41-60 / 12 shields). Name Gregory Shaw dested Greg Shaw analog leftover
Day 1 CANON / player-stubs/Greg_Shaw.wiki. Username blank.
p09 Light Yavin 4: Massassi Throne Room. p10 Dark Same as Yesterday with
In/Out from Day 1 Hunt Down And Destroy The Jedi.
Do not dest as a new person.
Do not dest Day 1 TMW / 2012 MPC Shaw 60s again.
"""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2012 Texas Mini Worlds Day 2 Greg Shaw LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 2 Greg Shaw DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p09 handwritten 2010 Xerox Light Deck Name APPLE SAETOIZ skip. "
    "p10 handwritten 2010 Xerox Dark empty Same as Yesterday with In/Out. "
    "Name Gregory Shaw dested Greg Shaw analog leftover Day 1 CANON. "
    "Username blank. Event TMW DAY 2. Date blank. "
    "Do not dest as a new person. Do not dest Day 1 TMW / 2012 MPC Shaw 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p09 Light Deck Name APPLE SAETOIZ skip. LIGHT checked. "
    "Event TMW DAY 2 Date blank. Name Gregory Shaw dested Greg Shaw analog leftover Day 1. "
    "Username blank. "
    "Yavin IV Massassi Throne Room dested Yavin 4: Massassi Throne Room analog leftover Anderson. "
    "Home One War Room dested Home One: War Room analog leftover Banger. "
    "Naboo Boss Nass Chambers dested Naboo: Boss Nass' Chambers analog leftover Nass Chamber. "
    "Naboo Battle Plains dested Naboo: Battle Plains analog leftover. "
    "JCC dested Coruscant: Jedi Council Chamber analog leftover True. "
    "Luke Skywalker Jedi Knight dested Luke Skywalker, Jedi Knight analog leftover Cullen. "
    "Luke Skywalker, Strong Force dested Luke Skywalker, Strong In The Force analog leftover qty=2. "
    "Qui Gon With Saber dested Qui-Gon Jinn With Lightsaber analog leftover Barnes qty=2. "
    "Obi With Saber dested Obi-Wan Kenobi With Lightsaber analog leftover Barnes. "
    "Threepio With Parts dested Threepio With His Parts Showing analog leftover Banger. "
    "Leia Rebel Princess dested Leia, Rebel Princess analog leftover Shaw. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel analog leftover Shaw. "
    "Restraining Bolt dested analog leftover MPC Herold. "
    "Han Chewie And The Falcon dested Han, Chewie, And The Falcon analog leftover Barnes. "
    "Artoo In Red 5 dested Artoo-Detoo In Red 5 analog leftover Hendon qty=2. "
    "Luke's Blaster Hand dested Luke's Blaster Pistol analog leftover Baroni. "
    "Obi Wan's Journal dested Obi-Wan's Journal analog leftover Anderson. "
    "Were You Looking For Me dested Were You Looking For Me? analog leftover. "
    "Out Of Commission & Trans Term dested Out Of Commission & Transmission Terminated analog leftover Richards Day 2. "
    "Sorry About The Mess & Blaster dested Sorry About The Mess & Blaster Proficiency analog leftover Barnes. "
    "Wesa Gotta Grand Army dested analog leftover qty=2. "
    "Rebel Leadership dested analog leftover True qty=3. "
    "Draw Their Fire dested analog leftover Banger. "
    "Hyper Escape dested analog leftover True. "
    "Anger, Fear, Aggression dested analog leftover Anderson True IN THE 60. "
    "Shield A Tragedy dested A Tragedy Has Occurred analog leftover. "
    "Shield Lets Keep Optimism dested Let's Keep A Little Optimism Here analog leftover True. "
    "Shield Your Insight dested Your Insight Serves You Well analog leftover True. "
    "Shield Wise Advice dested analog leftover. "
    "Shield Yavin Sentry dested Massassi Base Sentry analog leftover Anderson. "
    "Shield He Can Go About His Biz dested He Can Go About His Business analog leftover. "
    "Shield Only Jedi Carry dested Only Jedi Carry That Weapon analog leftover; crossed Your Insight duplicate dest skip. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p10 Dark Deck Name blank. DARK checked. "
    "Event TMW DAY 2 Date blank. Name Gregory Shaw dested Greg Shaw analog leftover Day 1. "
    "Username blank. Empty 60 Same as Yesterday with In/Out dested Day 1 Hunt Down And Destroy The Jedi analog leftover Consoli. "
    "OUT Imperial Reinforcements True analog leftover Day 1 Shaw. "
    "IN First Strike empty analog leftover Consoli. "
    "Shields dest Day 1 Shaw DS_SHIELDS (Day 2 shield boxes blank). "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Kiffex"),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Mace Windu", True, qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Obi-Wan Kenobi With Lightsaber"),
    n("Admiral Ackbar", True),
    n("Threepio With His Parts Showing"),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel"),
    n("Restraining Bolt"),
    n("Corran Horn"),
    n("Han, Chewie, And The Falcon"),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Luke's Blaster Pistol"),
    n("Obi-Wan's Journal"),
    n("Seeking An Audience", True),
    n("Blaster Deflection", qty=2),
    n("Were You Looking For Me?"),
    n("Hear Me Baby, Hold Together", True),
    n("Sense"),
    n("Out Of Commission & Transmission Terminated"),
    n("The Force Is Strong With This One"),
    n("A Jedi's Resilience", qty=2),
    n("Under Attack"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Let The Wookiee Win", True, qty=2),
    n("Speak With The Jedi Council"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Escape Pod", True),
    n("Grimtaash"),
    n("Rebel Leadership", True, qty=3),
    n("Heading For The Medical Frigate"),
    n("Scrambled Transmission", True),
    n("Imperial Atrocity", True),
    n("Hindsight", True),
    n("Draw Their Fire"),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Hyper Escape", True),
    n("Wokling", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Wise Advice"),
    n("Massassi Base Sentry"),
    n("He Can Go About His Business"),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi", True),
    n("Coruscant (Dark)"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Knowledge And Defense", True),
    n("Blaster Rack", True),
    n("Darth Vader, Betrayer Of Jedi", qty=3),
    n("The Emperor", True),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Galen, Secret Apprentice", qty=3),
    n("Juno Eclipse, Black Leader"),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("General Nevar"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Blizzard 4"),
    n("Grievous' Lightsabers"),
    n("Darth Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Rogue Shadow"),
    n("Victory"),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Endor"),
    n("4-LOM With Rifle", True),
    n("Wipe Them Out, All Of Them", True),
    n("Search And Destroy"),
    n("Mara Jade With Lightsaber"),
    n("Boba Fett, Renowned Bounty Hunter"),
    n("We Must Accelerate Our Plans", qty=3),
    n("No Escape"),
    n("Revenge Of The Sith"),
    n("Tarkin's Bounty", True),
    n("First Strike"),
    n("Sith Fury", True),
    n("Masterful Move"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lightsaber Deficiency", True),
    n("Protocol Failure"),
    n("According To My Design"),
    n("Disarmed", qty=2),
    n("Imperial Barrier", qty=2),
    n("Force Push", True),
    n("Force Field", True),
    n("One Beautiful Thing"),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Abyss"),
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Oppressive Enforcement"),
    n("Fanfare", True),
]
DS_ADD = []
