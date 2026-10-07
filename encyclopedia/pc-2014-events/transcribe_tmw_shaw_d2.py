#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 2 Xerox: Greg Shaw.

Source: 2014-TMW-Day-2.pdf pages 1–2 (2013 form).
"""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = ""
STAGE = "Day 2"
PDF = "2014 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2014 Texas Mini Worlds Day 2 p01 Greg Shaw LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 2 p02 Greg Shaw DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields)."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests 1–6 checked). "
    "Name Gregory Shaw dested Greg Shaw. Username blank. LIGHT checked. Event TMW 2014 Day 2. "
    "Mind What You Have Learned dested Mind What You Have Learned / Save You It Can. "
    "Strong Is Vader dested as written. "
    "Battle Plan & Don't Tread On Me dested as written. "
    "Do Or Do Not & Wise Advice dested Do, Or Do Not & Wise Advice. "
    "Daughter of Skywalker dested Daughter Of Skywalker. "
    "General Crix Madine dested General Crix Madine. "
    "NO_DEST remaining: Strong Is Vader, Battle Plan & Don't Tread On Me, "
    "Do Or Do Not & Wise Advice, Juno Eclipse Blockade. "
    "Lando Calrissian, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Artoo Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Han, Chewie, and the Falcon dested Han, Chewie, And The Falcon. "
    "Obi-Wan in Radiant VII dested Obi-Wan In Radiant VII. "
    "Red Squadron 1 dested Red Squadron 1. "
    "AWRI & DS dested All Wings Report In & Darklighter Spin. "
    "Antilles Maneuver & Rebel Reinf dested Antilles Maneuver & Rebel Reinforcements. "
    "LTWW dested Let The Wookiee Win. "
    "Your Ship dested Your Ship?. "
    "Jedi Tests 1–6 dested Great Warrior, A Jedi's Strength, Domain Of Evil, "
    "Size Matters Not, It Is The Future You See, You Must Confront Vader. "
    "Unique overcounts sheet-accurate (Lando Calrissian, Unlikely Hero x2, "
    "Luke Skywalker x2, Artoo-Detoo In Red 5 x3, Imperial Atrocity x3, "
    "Projection Of A Skywalker x2, All Wings Report In & Darklighter Spin x2, "
    "Escape Pod x3, It Could Be Worse x2, Let The Wookiee Win x3, Rebel Leadership x4). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Gregory Shaw dested Greg Shaw. Username blank. DARK checked. "
    "Imperial Occupation dested Imperial Occupation / Imperial Control. "
    "Hoth: Ice Plains dested Hoth: Ice Plains. "
    "Ni Chuba Na? dested Ni Chuba Na. "
    "YMSYL dested You May Start Your Landing. "
    "Marquand in Bliz 6 dested Marquand In Blizzard 6. "
    "Veers dested General Veers. "
    "Juno Eclipse, Blockade dested as written. "
    "DVDLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Darth Maul With Saber dested Darth Maul With Lightsaber. "
    "Mara With Saber dested Mara Jade With Lightsaber. "
    "Maarek Stele dested Maarek Stele, The Emperor's Reach. "
    "U-3PO dested U-3PO (Yoc-Threepio). "
    "Wipe Them Out dested Wipe Them Out, All Of Them. "
    "Alert My Star Destroyer dested Alert My Star Destroyer!. "
    "Victory dested Victory as written. "
    "Omni Box + It's Worse crossed, Cease Fire dested Cease Fire!. "
    "ADTFTR dested A Dark Time For The Rebellion. "
    "WIAPN dested We're In Attack Position Now. "
    "CHYBC dested Come Here You Big Coward. "
    "YCHF dested You Cannot Hide Forever. "
    "TINT dested There Is No Try. "
    "Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Useless Gesture dested A Useless Gesture. "
    "DTHACC dested Do They Have A Code Clearance?. "
    "Unique overcounts sheet-accurate (Blizzard 4 x2, Grand Moff Tarkin x2, "
    "Imperial Decree x2, Victory x2, Cease Fire! x2, A Dark Time For The Rebellion x2, "
    "Force Push x2, Imperial Command x3, We're In Attack Position Now x2). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Strong Is Vader"),
    n("Dagobah"),
    n("It Is The Future You See"),
    n("Battle Plan & Don't Tread On Me"),
    n("Do, Or Do Not & Wise Advice"),
    n("Squadron Assignments"),
    n("Dagobah: Yoda's Hut"),
    n("Dagobah: Jungle"),
    n("Dagobah: Swamp"),
    n("Home One: War Room"),
    n("Naboo"),
    n("Admiral Ackbar", True),
    n("Daughter Of Skywalker", True),
    n("General Crix Madine"),
    n("Han Solo"),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Luke Skywalker", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Yoda", True),
    n("Artoo-Detoo In Red 5", qty=3),
    n("Han, Chewie, And The Falcon", True),
    n("Obi-Wan In Radiant VII"),
    n("Home One"),
    n("Lady Luck"),
    n("Red Squadron 1"),
    n("Tantive IV", True),
    n("Luke's Backpack"),
    n("Imperial Atrocity", True, qty=3),
    n("Launching The Assault"),
    n("Legendary Starfighter"),
    n("Much To Learn You Still Have"),
    n("Projection Of A Skywalker", qty=2),
    n("Reflection", True),
    n("Seeking An Audience", True),
    n("The Way Of Things"),
    n("A Few Maneuvers"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Escape Pod", True, qty=3),
    n("It Could Be Worse", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Rebel Leadership", True, qty=4),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Ultimatum", True),
    n("Affect Mind"),
    n("Let's Keep A Little Optimism Here", True),
    n("Planetary Defenses"),
    n("Yavin Sentry"),
    n("Your Ship?"),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("Don't Do That Again"),
    n("Another Pathetic Lifeform"),
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
    n("Aim High"),
]
LS_ADD = [
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
]


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Main Power Generators"),
    n("Hoth: Ice Plains", True),
    n("Imperial Decree"),
    n("Ni Chuba Na?", True),
    n("Endor Shield", True),
    n("You May Start Your Landing", True),
    n("Prepared Defenses", True),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Mountains", True),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Marquand In Blizzard 6"),
    n("Tempest 1"),
    n("Blizzard 4", qty=2),
    n("General Veers", True),
    n("General Nevar"),
    n("Emperor Palpatine"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True, qty=2),
    n("Juno Eclipse, Blockade"),
    n("ISB Sector Commander"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Maul With Lightsaber"),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("U-3PO (Yoc-Threepio)"),
    n("Jango Fett, The Assassin"),
    n("Hoth Blockade"),
    n("Image Of The Dark Lord", True),
    n("Wipe Them Out, All Of Them", True),
    n("No Escape"),
    n("Alert My Star Destroyer!"),
    n("Imperial Decree", True),
    n("Flagship Executor"),
    n("Victory", qty=2),
    n("Conquest", True),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Cease Fire!"),
    n("Cease Fire!"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Trample"),
    n("Force Push", True, qty=2),
    n("Imperial Command", qty=3),
    n("We're In Attack Position Now", qty=2),
    n("Target The Main Generator"),
    n("AT-AT Cannon", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Secret Plans"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Do They Have A Code Clearance?", True),
    n("Abyss"),
    n("After Her!", True),
    n("Resistance"),
    n("Firepower", True),
]
DS_ADD = []
