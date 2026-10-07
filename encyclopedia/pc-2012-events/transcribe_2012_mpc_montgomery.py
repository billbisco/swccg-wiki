#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Justin Montgomery.

Source: 2012mpcday1.pdf pages 113–114.
p113 typed GEMP dump Light Wookiees. p114 typed GEMP dump Dark ASM.
Name Justin Montgomery dested Justin Montgomery (analog empty).
Username blank. Pack player-stubs/Justin_Montgomery.wiki.
Do not dest as a new invented person. Dest Name box as written.
Lingrell leftover Deck Name "Justin Montgomery is my Muse" is a different player.
"""
from __future__ import annotations

PLAYER = "Justin Montgomery"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 113
DS_PAGE = 114
LS_SCAN = "2012 Match Play Championship Day 1 Justin Montgomery LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Justin Montgomery DS.png"
LS_DECK_NAME = "Wookiees"
DS_DECK_NAME = "ASM"
NOTE = "p113 typed GEMP dump Wookiees; p114 typed GEMP dump ASM. Username blank."
LS_NOTE = (
    "Typed GEMP dump. Name Justin Montgomery dested Justin Montgomery. "
    "Analog empty dest as written. Username blank. Deck Name Wookiees. "
    "Date 11 February 2012 Event MPC Day 1. "
    "Kashyyyk (v) dested Kashyyyk True starting location analog Lingrell. "
    "Wookiee (v) dested Wookiee True x8. Yarua (v) dested Yarua True x2. "
    "Chewbacca of Kashyyyk dested Chewbacca Of Kashyyyk True x2. "
    "Yoda, GW dested Yoda, Great Warrior x2. "
    "Alderaan Consular Ship dested Alderaan Consular Ship x3. "
    "LTWW dested Let The Wookiee Win True x3. "
    "Wookiee Haven (Forest) dested Kashyyyk: Wookiee Haven. "
    "AFA (v) dested Anger, Fear, Aggression True in the 60 analog Casey. "
    "Weapon Display dested Weapons Display True in shields. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed GEMP dump. Name Justin Montgomery dested Justin Montgomery. "
    "Analog empty dest as written. Username blank. Deck Name ASM. "
    "Date 11 February 2012 Event MPC Day 1. "
    "A Stunning Move/A Valuable Hostage dested dual empty. "
    "Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi x2. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers. "
    "He Is Not Ready & Imperial Prop dested He Is Not Ready & Imperial Propaganda. "
    "Something Special Planned F.T. dested Something Special Planned For Them True. "
    "Ni Chuba Na?? dested Ni Chuba Na?? empty. "
    "You Cannot Hide Forever empty in the 60 and True in shields kept separate. "
    "Secret Plans (v) dested Secret Plans without extra (V). "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Kashyyyk"
LS_CARDS = [
    n("Kashyyyk", True),
    n("Protector", True),
    n("Kashyyyk: Forest Depths"),
    n("Grrrghrrrgh!"),
    n("Learn About The Force, Luke"),
    n("Wookiee", True, qty=8),
    n("Yarua", True, qty=2),
    n("Chewbacca Of Kashyyyk", True, qty=2),
    n("Yoda, Great Warrior", qty=2),
    n("Corran Horn", qty=2),
    n("Luke Skywalker, Rebel Hero", qty=2),
    n("Senator Leia Organa"),
    n("Phylo Gandish", True),
    n("Alderaan Consular Ship", qty=3),
    n("Luke's Blaster Pistol", True),
    n("Wookiee Guide", True, qty=3),
    n("Wookiee Roar", True, qty=3),
    n("Let The Wookiee Win", True, qty=3),
    n("Might Of The Republic", qty=2),
    n("Nar Shaddaa Wind Chimes", qty=2),
    n("It's Not My Fault!", True, qty=2),
    n("Jedi Levitation", True),
    n("Imperial Atrocity", True, qty=3),
    n("Bargaining Table"),
    n("Our Most Desperate Hour", True),
    n("Wokling", True),
    n("Commando Training & K'lor'slug"),
    n("Evacuation Control", True),
    n("Advantage"),
    n("Let's Go Left", True, qty=3),
    n("Kashyyyk: Wookiee Haven"),
    n("Kashyyyk: Sacred Forest"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("The Professor", True),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Insidious Prisoner"),
    n("Coruscant: Private Platform"),
    n("Coruscant: Palpatine's Quarters"),
    n("Prepared Defenses"),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Maul With Lightsaber", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Aurra Sing", qty=2),
    n("Boba Fett, Bounty Hunter", qty=2),
    n("Battle Droid Squad", qty=2),
    n("4-LOM With Concussion Rifle", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("IG-88, Renegade Droid"),
    n("Zuckuss In Mist Hunter", qty=2),
    n("Victory"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Dark Jedi Lightsaber", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Control", qty=2),
    n("Force Field", True, qty=2),
    n("Cold Feet", True),
    n("Stop Motion", True),
    n("Weapon Levitation"),
    n("Sniper & Dark Strike"),
    n("Masterful Move & Endor Occupation"),
    n("Operational As Planned", True),
    n("The Phantom Menace", qty=2),
    n("Trophy Of A Bounty Hunter"),
    n("Desilijic Tattoo", True),
    n("No Escape"),
    n("Blaster Rack", True),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Ni Chuba Na??"),
    n("A Sith's Weapon"),
    n("Something Special Planned For Them", True),
    n("You Cannot Hide Forever"),
    n("Protocol Failure"),
    n("Search And Destroy"),
    n("Nal Hutta"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Hallway"),
]
DS_SHIELDS = [
    n("Knowledge And Defense", True),
    n("Abyss", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Oppressive Enforcement"),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Weapon Of A Sith"),
]
DS_ADD = []
