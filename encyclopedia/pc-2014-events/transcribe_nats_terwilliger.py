#!/usr/bin/env python3
"""2014 US Nationals Day 2 Xerox: Chris Terwilliger.

Source: Nationals-2014-day-2.pdf pages 7–8 (2010 form).
Name Chris Twigg. Username Vader322. Dest Chris Terwilliger.
p08 DS Same as Day One with In/Out: dest Day 1 DS minus OUT plus IN.
"""
from __future__ import annotations

PLAYER = "Chris Terwilliger"
USERNAME = "Vader322"
STAGE = "Day 2"
PDF = "2014 US Nationals Day 2.pdf"
LS_PAGE = 7
DS_PAGE = 8
LS_SCAN = "2014 US Nationals Day 2 p07 Chris Terwilliger LS.png"
DS_SCAN = "2014 US Nationals Day 2 p08 Chris Terwilliger DS.png"
NOTE = "Handwritten 2010 Xerox. Name Chris Twigg; username Vader322 dested Chris Terwilliger."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Twigg. Username Vader322. Deck name Y4. PA Day 2. "
    "Communing dested Communing. Master Kenobi dested Master Kenobi. "
    "Maneuvering Flaps & Quick Draw dested Maneuvering Flaps & Quick Draw. "
    "Yub Yub, Commander dested Yub Yub, Commander. Let's Go Boys dested Let's Go Boys. "
    "Tatooine: Obi-Wan's Hut dested Tatooine: Obi-Wan's Hut. "
    "EPP Han dested Han With Heavy Blaster Pistol. Chewie Enraged dested Chewie, Enraged. "
    "Tatooine (Ep I) dested Tatooine (Episode I). AFA dested Anger, Fear, Aggression. "
    "Unique overcounts sheet-accurate (Yub Yub, Commander x2, Let's Go Boys x2, "
    "Let The Wookiee Win x2, Escape Pod x2, Rebel Leadership x3). (V) from checkbox. "
    "NO_DEST (2014 index): Maneuvering Flaps & Quick Draw (V); Let's Go Boys (V); Tatooine (Episode I)."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Deck name HDv. Same as Day One with 2 OUT (Cease Fire, "
    "Alert My Star Destroyer!) and 2 IN (Control & Set For Stun, Mara w/ Stick). "
    "Dest Day 1 DS minus those OUT plus Control & Set For Stun and Mara Jade With Lightsaber. "
    "Day 1 already had Control & Set For Stun; Day 2 has x2 sheet-accurate. "
    "Mara w/ Stick dested Mara Jade With Lightsaber. (V) from Day 1 checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing", True),
    n("Master Kenobi", True),
    n("Maneuvering Flaps & Quick Draw", True),
    n("Wokling", True),
    n("Rebel Gunrunner", True),
    n("Mechanical Failure"),
    n("Yub Yub, Commander", True, qty=2),
    n("Threepio With His Parts Showing"),
    n("Let's Go Boys", True),
    n("Dash Rendar", True),
    n("Tatooine: Mos Espa"),
    n("Coruscant: Docking Bay", True),
    n("Seeking An Audience", True),
    n("Desperate Tactics", qty=2),
    n("Use The Force", True),
    n("Let's Go Boys", True),
    n("Projection Of A Skywalker"),
    n("Home One: War Room"),
    n("Let The Wookiee Win", True, qty=2),
    n("Launching The Assault"),
    n("Escape Pod", True, qty=2),
    n("Senator Leia Organa", True),
    n("Shmi Skywalker"),
    n("Imperial Atrocity", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Tatooine: City Outskirts"),
    n("Alderaan Consular Ship", True),
    n("Home One"),
    n("Echo Base Garrison"),
    n("Rogue 1"),
    n("Rogue 2"),
    n("Rogue 3"),
    n("Rogue 4"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Derek 'Hobbie' Klivian"),
    n("Admiral Ackbar", True),
    n("Dual Laser Cannon", True),
    n("Flash Of Insight", True),
    n("Rebel Leadership", True, qty=3),
    n("Zer Senesca"),
    n("Melas"),
    n("Padme Naberrie", True),
    n("Jedi Levitation", True),
    n("Scrambled Transmission", True),
    n("Yoda, Great Warrior", True),
    n("Corran Horn"),
    n("Han With Heavy Blaster Pistol", True),
    n("Chewie, Enraged", True),
    n("Commander Luke Skywalker", True),
    n("Houjix"),
    n("Tatooine (Episode I)"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Do, Or Do Not"),
    n("Chasm"),
    n("Weapons Display"),
    n("Don't Do That Again"),
    n("Aim High"),
    n("There Is Another"),
    n("Affect Mind"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("The Professor"),
    n("Let's Keep A Little Optimism Here"),
    n("Wise Advice"),
]
LS_ADD = [
    n("Ultimatum"),
    n("Your Insight Serves You Well"),
    n("Battle Plan"),
]


# Day 2 Dark = Day 1 Dark minus Cease Fire, Alert My Star Destroyer!
# plus Control & Set For Stun, Mara Jade With Lightsaber.
DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Hoth: Main Power Generators", True),
    n("Hoth: Wampa Cave"),
    n("Hoth: Ice Plains"),
    n("Hoth: Defensive Perimeter"),
    n("Hoth"),
    n("AT-AT Cannon", True),
    n("Target The Main Generator"),
    n("We're In Attack Position Now", qty=2),
    n("Hoth Blockade", True),
    n("No Escape"),
    n("Image Of The Dark Lord", True),
    n("Control & Set For Stun", qty=2),
    n("Ni Chuba Na??", True),
    n("You May Start Your Landing", True),
    n("Do They Have A Code Clearance?"),
    n("Endor Shield", True),
    n("Imperial Command", qty=3),
    n("Trample"),
    n("Force Push", True, qty=2),
    n("Imperial Decree", True),
    n("Imperial Decree"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Stop Motion", True),
    n("Sniper & Dark Strike"),
    n("Walker Garrison"),
    n("Prepared Defenses", True),
    n("Crash Landing"),
    n("U-3PO (Yoo-Threepio)"),
    n("Admiral Ozzel"),
    n("Commander Igar", True),
    n("Juno Eclipse, Black Leader", True),
    n("Darth Vader", True),
    n("Grand Moff Tarkin", True),
    n("Admiral Piett"),
    n("AT-AT Commander", True),
    n("Veers", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Grand Admiral Thrawn"),
    n("Garindan", True),
    n("Jango Fett, The Assassin", True),
    n("Cold Feet", True),
    n("Blizzard 4", qty=2),
    n("Blizzard 1", True),
    n("Tempest 1"),
    n("Blizzard 2", True),
    n("Marquand In Blizzard 6"),
    n("Victory", True, qty=2),
    n("Conquest", True),
    n("Flagship Executor"),
    n("Knowledge And Defense", True),
    n("Mara Jade With Lightsaber", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Leave Them To Me"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever"),
    n("Wipe Them Out, All Of Them"),
    n("Death Star Sentry", True),
    n("Fanfare"),
    n("Secret Plans"),
]
DS_ADD = [
    n("Abyss", True),
    n("Firepower", True),
    n("Allegations Of Corruption"),
]
