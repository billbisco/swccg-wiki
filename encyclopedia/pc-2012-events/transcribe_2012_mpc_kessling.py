#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Mike Kessling.

Source: 2012mpcday1.pdf pages 101–102.
p101 typed GEMP dump Light Communing. p102 typed GEMP dump Dark AOBS.
Handwritten MIKE KESSLING / MPC 2012. Username blank.
Dest Mike Kessling (existing bio). Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Mike Kessling"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 101
DS_PAGE = 102
LS_SCAN = "2012 Match Play Championship Day 1 Mike Kessling LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Mike Kessling DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "p101 typed GEMP dump Communing; p102 typed GEMP dump AOBS. Username blank."
LS_NOTE = (
    "Typed GEMP dump. Handwritten MIKE KESSLING dested Mike Kessling. "
    "Username blank. Event MPC 2012. Do not dest as a new person. "
    "Communing empty dested Communing. "
    "Threepio With His Parts Showing (AI) dested x1 unique variant. "
    "Padme Naberrie (V) dested Padme Naberrie True. "
    "Escape Pod True x2 plus Sabotage True handwritten. "
    "Artoo-Detoo In Red 5 crossed skipped. "
    "Nick Of Time True (1 starting) dested in the 60. "
    "Commando Training & K'lor'slug (1 starting) dested in the 60. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed GEMP dump. Handwritten MIKE KESSLING dested Mike Kessling. "
    "Username blank. Event MPC 2012. Do not dest as a new person. "
    "Agents of Black Sun/Vengeance of the Dark Prince empty dested dual. "
    "Aurra Sing x2 plus Aurra Sing True dested both. "
    "Abyss True crossed dested Do They Have A Code Clearance?. "
    "Crossed shield dested Imperial Detention. "
    "Cease Fire! handwritten x2. Vader's Obsession handwritten. "
    "<>Spaceport Docking Bay dested Spaceport Docking Bay. "
    "Plan crossed skipped. Crossed (V) skipped. "
    "Ket Maliss True dested Ket Maliss True. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Yoda, Great Warrior", qty=2),
    n("Threepio With His Parts Showing"),
    n("Shmi Skywalker"),
    n("Senator Mon Mothma"),
    n("Senator Leia Organa"),
    n("Padme Naberrie", True),
    n("Luke Skywalker, Rebel Hero", qty=3),
    n("Leia, Rebel Princess"),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("General Carlist Rieekan", True),
    n("Corran Horn"),
    n("Chewbacca, Protector", qty=3),
    n("Strike Planning"),
    n("Master Kenobi"),
    n("Communing"),
    n("Tatooine: Slave Quarters"),
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: City Outskirts"),
    n("Kashyyyk: Forest Depths"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Run Luke, Run!", True, qty=2),
    n("Lucky Shot", True),
    n("Let The Wookiee Win", True, qty=2),
    n("It's Not My Fault!", True, qty=2),
    n("Inconsequential Barriers", qty=2),
    n("Houjix"),
    n("Hear Me Baby, Hold Together", True),
    n("Grimtaash"),
    n("Escape Pod", True, qty=2),
    n("Sabotage", True),
    n("Strikeforce", True),
    n("Seeking An Audience", True),
    n("Security Breach"),
    n("Scrambled Transmission", True),
    n("Rebel Gunrunner"),
    n("Obi-Wan's Apparition", True),
    n("Nick Of Time", True),
    n("Honor Of The Jedi"),
    n("Hindsight", True),
    n("Goo Nee Tay"),
    n("Flash Of Insight", True),
    n("Draw Their Fire"),
    n("Commando Training & K'lor'slug"),
    n("Luke's Blaster Pistol", True),
    n("Chewbacca's Bowcaster"),
    n("Alderaan Consular Ship", qty=2),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Chasm", True),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Prophetess", True),
    n("Shada"),
    n("Sy Snootles", True),
    n("Aurra Sing", qty=2),
    n("Aurra Sing", True),
    n("Gardulla The Hutt", True),
    n("Gragra"),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("4-LOM With Concussion Rifle", qty=2),
    n("IG-88 With Riot Gun", qty=2),
    n("Trophy Of A Kill", qty=2),
    n("Restraining Bolt"),
    n("Ability, Ability, Ability"),
    n("Establish Control", True),
    n("I've Lost Artoo!", True),
    n("Ket Maliss", True),
    n("No Bargain", True),
    n("Broken Concentration"),
    n("First Strike"),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("No Escape"),
    n("Knowledge And Defense", True),
    n("Lateral Damage"),
    n("Control & Set For Stun"),
    n("Force Push", True),
    n("Stunning Leader", True, qty=2),
    n("We Must Accelerate Our Plans", qty=5),
    n("Jabba's Through With You", qty=2),
    n("Imperial Barrier", qty=3),
    n("Elis Helrot", qty=2),
    n("Cease Fire!", qty=2),
    n("Prepared Defenses", True),
    n("Vader's Obsession"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Spaceport Docking Bay"),
    n("Coruscant: Imperial City"),
    n("Blockade Flagship: Bridge"),
    n("Corulag"),
    n("Coruscant"),
    n("Zuckuss In Mist Hunter", qty=2),
    n("Mara Jade's Lightsaber"),
    n("Dark Jedi Lightsaber", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Firepower", True),
    n("Imperial Detention"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
]
DS_ADD = []
