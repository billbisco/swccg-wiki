#!/usr/bin/env python3
"""2013 Alderaan Regionals: Chris Menzel typed spreadsheet LS+DS."""
from __future__ import annotations

PLAYER = "Chris Menzel"
USERNAME = ""
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 13
DS_PAGE = 14
LS_SCAN = "2013 Alderaan Regionals p13 Chris Menzel LS.png"
DS_SCAN = "2013 Alderaan Regionals p14 Chris Menzel DS.png"
LS_NOTE = (
    "Typed spreadsheet printout (not a handwritten Xerox form). Header California / "
    "LS Strange Menzel Senate Deck 2013, dated 13.07.2013. Yoda, Master Of The Force "
    "struck (qty 0). Civil Disorder (V) typed qty 0, rewritten by hand as 1. "
    "Simple Tricks And Knowledge (V) → Simple Tricks And Nonsense (V). "
    "Senator header says 17; listed copies total 16."
)
DS_NOTE = (
    "Typed spreadsheet printout (not a handwritten Xerox form). Header California 2013 / "
    "Hunt Down and Destroy the Sunshine, dated 13.07.2013 V 6.03. "
    "The Mandalorian, Fetter Father (V) → Jango Fett (V). "
    "Darth Maul on a Stick → Darth Maul With Lightsaber. "
    "4-LOM with Tracking Rifle (V) → 4-LOM With Concussion Rifle (V). "
    "After Her (V) handwritten on shields."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("Strike Planning"),
    n("Wokling", True),
    n("Seeking An Audience", True),
    n("Anger, Fear, Aggression", True),
    n("Senator Palpatine", qty=2),
    n("Supreme Chancellor Valorum", True, qty=2),
    n("Tendau Bendon"),
    n("Horox Ryyder"),
    n("Liana Merian"),
    n("Yarua"),
    n("Senator Mon Mothma", True),
    n("Princess Leia", True, qty=2),
    n("Mas Amedda"),
    n("General Carlist Rieekan", True),
    n("Queen Amidala, Ruler Of Naboo", qty=3),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Corran Horn"),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Han, Chewie, And The Falcon"),
    n("Han, Chewie, And The Falcon", True),
    n("Artoo-Detoo In Red 5"),
    n("Home One"),
    n("Lady Luck", True),  # sheet Lando's Luxury Yacht (V)
    n("Hoth: Echo Command Center (War Room)"),
    n("Hoth"),
    n("Cloud City: Guest Quarters"),
    n("Ascertaining The Truth"),
    n("I Will Not Defer"),
    n("The Gravest Of Circumstances"),
    n("Plea To The Court"),
    n("Senate Hovercam"),
    n("Imperial Atrocity", True),
    n("Haven"),
    n("Civil Disorder", True),
    n("Might Of The Republic", qty=3),
    n("I've Got A Bad Feeling About This"),
    n("Tunnel Vision", qty=2),
    n("Sense", qty=2),
    n("I've Decided To Go Back", qty=2),
    n("A Jedi's Resilience", qty=2),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Another Pathetic Lifeform", True),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Aim High"),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Chasm", True),
    n("Only Jedi Carry That Weapon"),
    n("Wise Advice"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Holotheatre"),
    n("Executor: Meditation Chamber"),
    n("Visage Of The Emperor"),
    n("Surface Defense", True),
    n("Knowledge And Defense", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader With Lightsaber", qty=3),
    n("Mara Jade With Lightsaber", True, qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Battle Droid Squad", True, qty=2),
    n("P-59", qty=2),
    n("Boba Fett, Prepared Hunter", True),
    n("Jango Fett", True, qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Garindan", True),
    n("Slave I, Symbol Of Fear"),
    n("Victory", True),
    n("Restraining Bolt"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Cloud City: Security Tower", True),
    n("Imperial Holotable"),
    n("Visage Of The Emperor", qty=2),
    n("The Phantom Menace"),
    n("Revenge Of The Sith", True),
    n("Imperial Justice", True),
    n("No Escape"),
    n("Program Trap"),
    n("Something Special Planned For Them", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Why Didn't You Tell Me?", True, qty=2),
    n("Force Field", True),
    n("Sonic Bombardment", True, qty=2),
    n("They're Still Coming Through", qty=2),
    n("Imperial Barrier"),
    n("Masterful Move & Endor Occupation"),
    n("Force Push", True),
    n("Sith Fury & End This Destructive Conflict", True, qty=2),
    n("A Dark Time For The Rebellion", True),
    n("You Swindled Me!", True),
    n("Imbalance & Kintan Strider", True),
    n("You Are Beaten"),
    n("Sense"),
    n("Cold Feet", True),
    n("Stop Motion", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("A Useless Gesture"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention", True),
    n("Resistance"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("After Her!", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare"),
]
DS_ADD = []
