#!/usr/bin/env python3
"""2013 World Championship Day 2: Ryan Jellison Xerox Senate Jank + LAAT Jank."""
from __future__ import annotations

PLAYER = "Ryan Jellison"
USERNAME = "sac89837"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 49
DS_PAGE = 48
LS_SCAN = "2013 Worlds Day 2 p49 Ryan Jellison LS.png"
DS_SCAN = "2013 Worlds Day 2 p48 Ryan Jellison DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Ryan Jellison. "
    "Username Sre 89857 dested sac89837 (Alderaan Username). "
    "Event Worlds Day 2, dated 08/10/13. Deck title LAAT Jank. LIGHT. "
    "Local Uprising dested Local Uprising / Liberation. "
    "Hoth MPG dested Hoth: Main Power Generators (1st Marker). "
    "Hoth North Ridge dested Hoth: North Ridge (4th Marker). "
    "Hoth Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth Echo Command Center dested Hoth: Echo Command Center (War Room). "
    "Republic Gunship dested Republic Gunship Wing. "
    "Senator Bail Organa dested Bail Organa. "
    "Flare, Chewie and Fate dested Han, Chewie, And The Falcon. "
    "I Know Someone dested Someone Who Loves You. "
    "Why You Looking For Me dested Were You Looking For Me?. "
    "Increasing The Odds / Burning Sky dested Changing The Odds. "
    "It Could Be Worse / It's Not My Fault dested It's Not My Fault!. "
    "A Fine Mind dested Affect Mind. "
    "Don't Do That Again struck through, omitted. "
    "Additional Aim High / Yavin Sentry / A Tragedy / Chasm moved to Light shields. "
    "Form left column reprints 37-38 on lines 39-40 are Fixer. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Ryan Jellison. "
    "Username Sre 89837 dested sac89837 (Alderaan Username). "
    "Event Worlds Day 2, dated 08/10/13. Deck title Senate Jank. DARK. "
    "My Lord That's One Hell Of An Entrance dested My Lord, Is That Legal? / I Will Make It Legal. "
    "Accepting Trade Federation dested Accepting Trade Federation Control. "
    "Astromech Shortage dested Astromech Shortage. "
    "Senate Hovercam dested Senate Hovercam. "
    "Short Range Fighters / Watch Your Back dested Short Range Fighters & Watch Your Back!. "
    "Bossk in Hound's Tooth dested Bossk In Hound's Tooth. "
    "Slave I, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "The Emperor's Reach dested The Emperor's Reach. "
    "Stinge dested Stinger. "
    "On Free Taa dested Orn Free Taa. "
    "Briska Yeesrim dested Baskol Yeesrim. "
    "Yeb Yeb Adem'thin dested Yeb Yeb Adem'thorn. "
    "We'll Let Fate Decide Huh dested We'll Let Fate-a Decide, Huh?. "
    "Imperial Detention dested Imperial Detention. "
    "Additional Allegations / There Is No Try / Abyss moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40 are Guri / I Had No Choice. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Local Uprising / Liberation"
LS_CARDS = [
    n("Local Uprising / Liberation", True),
    n("Hoth"),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth: North Ridge (4th Marker)"),
    n("Hoth: Echo Corridor"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Echo Med Lab", True),
    n("Hoth: Echo Command Center (War Room)"),
    n("Hoth: Echo Docking Bay"),
    n("Heading For The Medical Frigate"),
    n("Maneuvering Flaps"),
    n("Superficial Damage", True),
    n("Nick Of Time", True),
    n("Wokling", True),
    n("A New Secret Base", qty=2),
    n("Crash Site Memorial", qty=2),
    n("Evacuation Control", True, qty=2),
    n("Draw Their Fire"),
    n("Flash Of Insight"),
    n("Scrambled Transmission", True),
    n("Men To Load, You Still Have A Choice", True),
    n("Dash In Rogue 10"),
    n("Snowspeeder Garrison"),
    n("Republic Gunship Wing", qty=4),
    n("Dual Laser Cannon", True),
    n("Power Harpoon", qty=2),
    n("Cannon Fodder"),
    n("Luke Skywalker", True),
    n("Bail Organa"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Deception"),
    n("Fixer", qty=2),
    n("Alderaan Consular Ship", qty=2),
    n("Spiral"),
    n("Lady Luck"),
    n("Wedge In Red Squadron 1"),
    n("Han, Chewie, And The Falcon"),
    n("Let The Wookiee Win", True, qty=3),
    n("Escape Pod", True, qty=2),
    n("Lucky Shot"),
    n("Someone Who Loves You"),
    n("Were You Looking For Me?"),
    n("Houjix"),
    n("All Wings Report In & Darklighter Spin"),
    n("Desperate Reach"),
    n("Changing The Odds"),
    n("It's Not My Fault!", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Affect Mind"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Ship?"),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Battle Plan"),
    n("Aim High"),
    n("Yavin Sentry", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
]
LS_ADD = []


DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Surface Defense", True),
    n("Naboo"),
    n("Tatooine: Desert Landing Site"),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Bridge"),
    n("This Is Outrageous!"),
    n("Our Blockade Is Perfectly Legal"),
    n("Motion Supported"),
    n("Accepting Trade Federation Control"),
    n("Strategic Reserves", True),
    n("Astromech Shortage", True),
    n("Blast Door Controls"),
    n("Senate Hovercam", qty=2),
    n("Squabbling Delegates", qty=3),
    n("Sonic Bombardment", True, qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Those Rebels Won't Escape Us", True),
    n("Sense"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Victory"),
    n("Elis Helrot"),
    n("Bossk In Hound's Tooth", True),
    n("Emperor's Personal Shuttle"),
    n("Slave I, Symbol Of Fear"),
    n("Guri", qty=3),
    n("Darth Maul With Lightsaber"),
    n("The Emperor", True, qty=2),
    n("The Emperor's Reach"),
    n("Stinger"),
    n("I Had No Choice"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Coruscant Guard", True, qty=2),
    n("Coruscant Guard"),
    n("Lott Dod", qty=3),
    n("Aks Moe", qty=2),
    n("Orn Free Taa", qty=2),
    n("Baskol Yeesrim"),
    n("Yeb Yeb Adem'thorn"),
    n("Toonbuck Toora", qty=2),
    n("Passel Argente"),
    n("Tikkes"),
    n("Edcel Bar Gane"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Imperial Detention"),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Fanfare", True),
    n("Resistance"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Abyss"),
]
DS_ADD = []
