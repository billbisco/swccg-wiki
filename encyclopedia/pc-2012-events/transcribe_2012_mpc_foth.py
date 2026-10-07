#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Caleb Foth.

Source: 2012mpcday1.pdf pages 29–30 (2010 form, 12 shields).
Name Caleb Foth dested Caleb Foth. Username @9N05.
p29 Dark Eric Hunter's Bunch o' Bitches / Agents Of Black Sun.
p30 Light @9N05' Pile Communing / Communing.
"""
from __future__ import annotations

PLAYER = "Caleb Foth"
USERNAME = "@9N05"
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 30
DS_PAGE = 29
LS_SCAN = "2012 Match Play Championship Day 1 Caleb Foth LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Caleb Foth DS.png"
LS_DECK_NAME = "@9N05' Pile Communing"
DS_DECK_NAME = "Eric Hunter's Bunch o' Bitches"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Caleb Foth dested Caleb Foth. "
    "Username @9N05. Event MPC Day 1. Deck Name @9N05' Pile Communing. LIGHT checked. "
    "Communing dested Communing True. "
    "Tatooine: Slave Quarters dested Tatooine: Slave Quarters. "
    "Master Kenobi dested Master Kenobi. "
    "Chewie dested Chewie True. "
    "Threepio with His Parts Showing dested Threepio With His Parts Showing. "
    "Yoda, Great Warrior dested Yoda, Great Warrior. "
    "Strikeforce dested Strikeforce. "
    "Antilles Maneuver & Rebel Reinforcements crossed, Suhaya dest replacement. "
    "Ultimatum crossed, Ounee Ta dest replacement. "
    "Blind Jedi dested as written. "
    "(V) from checkbox; dittos inherit; differing checkboxes kept separate."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Caleb Foth dested Caleb Foth. "
    "Username @9N05. Event Date 02/11/12. Deck Name Eric Hunter's Bunch o' Bitches. "
    "DARK checked. Agents of the Black Sun dested Agents Of Black Sun / Vengeance Of The Dark Prince empty. "
    "Knowledge and Defense dested Knowledge And Defense True. "
    "Coruscant (SE) dested Coruscant. "
    "Tarkin's Bounty crossed, Cease Fire! Non-V dest replacement without (V). "
    "Cease Fire! crossed on form 41, Vader's Obsession dest replacement. "
    "Fondor crossed, Corulag dest replacement. "
    "Abyss crossed, Do They Have A Code Clearance dest replacement. "
    "Fanfare crossed, Imperial Detention dest replacement. "
    "Aurra Sing empty and True kept separate. "
    "(V) from checkbox; dittos inherit; differing checkboxes kept separate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
    n("Communing", True),
    n("Master Kenobi", True),
    n("Strike Planning"),
    n("Blind Jedi", True),
    n("Chewbacca, Protector", qty=2),
    n("Chewie", True),
    n("Corran Horn"),
    n("General Carlist Rieekan", True),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Leia, Rebel Princess"),
    n("Luke Skywalker, Rebel Hero", True, qty=3),
    n("Padme Naberrie", True),
    n("Senator Leia Organa", True),
    n("Senator Mon Mothma", True),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Yoda, Great Warrior", True),
    n("Alderaan Consular Ship", True),
    n("Artoo-Detoo In Red 5"),
    n("Millennium Falcon", True),
    n("Chewbacca's Bowcaster"),
    n("Luke's Blaster Pistol", True),
    n("Commando Training & K'lor'slug", True),
    n("Draw Their Fire"),
    n("Flash Of Insight", True),
    n("Hindsight", True),
    n("Goo Nee Tay"),
    n("Honor Of The Jedi"),
    n("Nick Of Time", True),
    n("Obi-Wan's Apparition", True),
    n("Rebel Gunrunner", True),
    n("Scrambled Transmission", True),
    n("Seeking An Audience", True),
    n("Security Breach", True),
    n("Strikeforce", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Suhaya", True),
    n("Desperate Reach", True),
    n("Hear Me Baby, Hold Together", True),
    n("Houjix & Out Of Nowhere"),
    n("Inconsequential Barriers", qty=2),
    n("It's Not My Fault", True, qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Lucky Shot", True),
    n("Run Luke, Run", True, qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Kashyyyk: Forest Depths", True),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Obi-Wan's Hut", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Ounee Ta"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Knowledge And Defense", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("No Bargain", True),
    n("Shada", True),
    n("Prepared Defenses", True),
    n("4-LOM With Concussion Rifle", qty=2),
    n("IG-88 With Riot Gun", qty=2),
    n("Aurra Sing", qty=2),
    n("Aurra Sing", True),
    n("Gardulla The Hutt", True),
    n("Gragra"),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Prophetess", True),
    n("Sy Snootles", True),
    n("Zuckuss In Mist Hunter", qty=2),
    n("Dark Jedi Lightsaber", True),
    n("Mara Jade's Lightsaber"),
    n("Restraining Bolt"),
    n("Trophy Of A Kill", True, qty=2),
    n("Ability, Ability, Ability"),
    n("Blast Door Controls"),
    n("Broken Concentration"),
    n("Establish Control", True),
    n("First Strike"),
    n("Gift Of The Master", True),
    n("I've Lost Artoo", True),
    n("Jabba's Haven", True),
    n("Ket Maliss", True),
    n("Lateral Damage"),
    n("No Escape"),
    n("Cease Fire!"),
    n("Control & Set For Stun"),
    n("Vader's Obsession"),
    n("Elis Helrot", qty=2),
    n("Force Push", True),
    n("Imperial Barrier", qty=3),
    n("Jabba's Through With You", qty=2),
    n("Stunning Leader", True, qty=2),
    n("We Must Accelerate Our Plans", qty=5),
    n("Coruscant: Private Platform (Docking Bay)", True),
    n("Corulag"),
    n("Spaceport Docking Bay"),
    n("Blockade Flagship: Bridge"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
