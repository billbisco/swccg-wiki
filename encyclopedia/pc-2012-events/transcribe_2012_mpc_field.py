#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Brian Field.

Source: 2012mpcday1.pdf pages 5–6 (2010 form, 12 shields).
p05 Name Justin Brown crossed, dest Field. Worlds Day II crossed, Event MPC.
DARK checked. Username blank. X on Dark line numbers is reuse marking; dest as written.
p06 Name Brian Field. Deck Name Rhodes!?. LIGHT checked. Username blank.
"""
from __future__ import annotations

PLAYER = "Brian Field"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2012 Match Play Championship Day 1 Brian Field LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Brian Field DS.png"
LS_DECK_NAME = "Rhodes!?"
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Brian Field. Username blank. LIGHT checked. "
    "Deck Name Rhodes!?. WYS dested Watch Your Step / This Place Can Be A Little Rough. "
    "Landing plat 1 dested Endor: Landing Platform (Docking Bay). "
    "Mining Plaza dested Cloud City: Downtown Plaza. "
    "Kessel DB 94 dested Tatooine: Docking Bay 94. Spaceport DB dested Spaceport Docking Bay. "
    "Cantina dested Tatooine: Cantina. Booster's Ship dested Errant Venture. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. Gold squadron dested Gold Squadron 1. "
    "Han (confused) dested Han Solo. Chewie dested Chewbacca. "
    "ODC/It dested Odin Ith. Ins/Aim High dested Insurrection & Aim High. "
    "Don't Let dested Don't Get Cocky. AWRI/Darklighter Spin dested "
    "All Wings Report In & Darklighter Spin. Control/Tunnel dested Control & Tunnel Vision. "
    "Scrambled Transmission (V) checkbox crossed; dest Scrambled Transmission. "
    "Unique overcounts sheet-accurate (Gold Squadron 1 x6, Patrol Craft x5, "
    "Don't Get Cocky x2, Melas x2, I'll Take The Leader x2, Odin Ith x2, "
    "All Wings Report In & Darklighter Spin x2, Fallen Portal x2, "
    "Control & Tunnel Vision x2). (V) from checkbox; dittos inherit."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Justin Brown crossed, dest Brian Field. Username blank. "
    "Worlds Day II crossed; Event MPC. DARK checked. Line-number X is reuse marking. "
    "Hunt Down dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Naboo Theed Palace Generator dested Naboo: Theed Palace Generator. "
    "Weapon Lev/the empire's back dested Weapon Levitation & The Empire's Back. "
    "Darth Vader, Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Gift of the Master dested Gift Of The Master. Galen, Secret App dested Galen, Secret Apprentice. "
    "Galen's Lightsaber Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi. I've Lost Artoo dested I've Lost Artoo!. "
    "Contradiction (SE) dested Contradiction. Kir Kanos w/ force pike dested Kir Kanos With Force Pike. "
    "The circle is now complete dested The Circle Is Now Complete. "
    "Masterful/EO dested Masterful Move & Endor Occupation. PILOT dested Imperial Pilot. "
    "4-LOM w/ rifle dested 4-LOM With Concussion Rifle. Mara Jade w/ saber dested Mara Jade With Lightsaber. "
    "Form 59 Coruscant Detention replaced by footer Vader's Obsession. "
    "Footer 38 Masterful/Endor Occ restates form 16. "
    "Unique overcounts sheet-accurate (Force Field x3, We Must Accelerate Our Plans x3, "
    "Emperor Palpatine x3, Galen, Secret Apprentice x3, Grievous x2, "
    "Weapon Levitation & The Empire's Back x2, Trophy Of A Kill x2, Imperial Pilot x2). "
    "(V) from checkbox; dittos inherit."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Kessel"),
    n("Corellia", True),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Cloud City: Downtown Plaza"),
    n("Tatooine: Docking Bay 94"),
    n("Spaceport Docking Bay"),
    n("Tatooine: Cantina"),
    n("Outrider"),
    n("Pulsar Skate"),
    n("Millennium Falcon"),
    n("Artoo-Detoo In Red 5"),
    n("Errant Venture"),
    n("Patrol Craft", qty=5),
    n("Gold Squadron 1", qty=6),
    n("Mirax Terrik"),
    n("Luke Skywalker", True),
    n("Booster Terrik"),
    n("Talon Karrde"),
    n("Wedge Antilles", True),
    n("Chewbacca"),
    n("Lando Calrissian"),
    n("Han Solo"),
    n("Dash Rendar"),
    n("Melas", True, qty=2),
    n("A Few Maneuvers"),
    n("Scrambled Transmission"),
    n("Odin Ith", qty=2),
    n("Squadron Assignments"),
    n("I'll Take The Leader", qty=2),
    n("Heading For The Medical Frigate"),
    n("Anger, Fear, Aggression", True),
    n("Don't Get Cocky", qty=2),
    n("Wokling", True),
    n("Han's Toolkit"),
    n("Insurrection & Aim High"),
    n("It Could Be Worse"),
    n("It's A Trap!"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Fallen Portal", qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("Wise Advice"),
    n("Rebel Barrier"),
    n("Moving To Attack Position"),
]
LS_SHIELDS = [
    n("Another Pathetic Lifeform", True),
    n("The Professor", True, qty=2),
    n("Jabba's Prize"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Blaster Deflection", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Force Lightning"),
    n("Force Field", True, qty=3),
    n("Naboo: Theed Palace Generator"),
    n("Trophy Of A Kill", True, qty=2),
    n("Weapon Levitation & The Empire's Back", True, qty=2),
    n("Blockade Flagship: Bridge"),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("First Strike"),
    n("Blaster Rack", True),
    n("P-59"),
    n("Gift Of The Master", True),
    n("Dark Jedi Lightsaber", True),
    n("Masterful Move & Endor Occupation"),
    n("Galen, Secret Apprentice", True, qty=3),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Vader's Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Emperor Palpatine", qty=3),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("A Sith's Plans", True),
    n("Prepared Defenses"),
    n("Force Push", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Coruscant: Imperial City"),
    n("I've Lost Artoo!", True),
    n("Knowledge And Defense", True),
    n("No Escape"),
    n("Contradiction"),
    n("Ni Chuba Na??", True),
    n("Weapon Of A Sith", True),
    n("Kir Kanos With Force Pike"),
    n("The Circle Is Now Complete"),
    n("Elis Helrot"),
    n("Presence Of The Force", True),
    n("Revenge Of The Sith", True),
    n("Restraining Bolt"),
    n("Death Star: War Room", True),
    n("Imperial Pilot", qty=2),
    n("4-LOM"),
    n("Search And Destroy"),
    n("4-LOM With Concussion Rifle", True),
    n("Blast Door Controls"),
    n("Mara Jade With Lightsaber", True),
    n("A Sith's Weapon", True),
    n("Emperor's Power", True),
    n("Vader's Obsession"),
]
DS_SHIELDS = [
    n("Oppressive Enforcement", True),
    n("Secret Plans", True),
    n("Allegations Of Corruption"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Weapon Of A Sith"),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Fanfare", True),
    n("Battle Order"),
]
DS_ADD = [
    n("Resistance"),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
]
