#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Greg Shaw (stealtheblind).

Source: 2014-TMW-Day-1.pdf pages 5–6 (2013 form).
"""
from __future__ import annotations

PLAYER = "Greg Shaw"
USERNAME = "stealtheblind"
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2014 Texas Mini Worlds Day 1 p06 Greg Shaw LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p05 Greg Shaw DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields)."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Gregory Shaw dested Greg Shaw. Username stealtheblind. LIGHT checked. "
    "Deck Name blank. It Is The Future You See (V) dested It Is The Future You See / A Tremor In The Force. "
    "Dash in Rogue 10 dested Dash In Rogue 10. "
    "Hear Me, Baby, Hold Together crossed, Either Way You Win dested Either Way, You Win. "
    "It's Not My Fault! line 37 crossed, Crash Site Memorial dested Crash Site Memorial. "
    "Let The Wookiee Win line 52 crossed, Control & Tunnel Vision dested Control & Tunnel Vision. "
    "Antilles Maneuver & Rebel Reinforcements crossed, Rebel Artillery dested Rebel Artillery. "
    "Your Ship dested Your Ship?. "
    "Unique overcounts sheet-accurate (Rebel Leadership x3, You Will Go To The Dagobah System x3, "
    "Crash Site Memorial x2). "
    "(V) from the checkbox; dittos inherit the first named line except where the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Gregory Shaw dested Greg Shaw. Username stealtheblind. DARK checked. "
    "Separatist Uprising empty dested Separatist Uprising / At War With Itself. "
    "Ni Chuba Na? crossed, Battle Order & First Strike dested Battle Order & First Strike. "
    "Protocol Failure crossed, Note Tentacle dested Note Tentacle. "
    "ComScan Detection line 40 crossed, Note Gunnery dested Note Gunnery. "
    "Force Push line 48 crossed, Wounded Warrior dested Wounded Warrior. "
    "Wounded Warrior line 50 crossed, Rally The Cause dested Rally The Cause. "
    "Short Range Fighters & Watch Your Back! line 54 crossed, Ghhhk dested Ghhhk. "
    "Battle Order shield crossed, We'll Let Fate-a Decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "Jango Fett, the Assassin dested Jango Fett, The Assassin. "
    "Oh, Switch Off dested Oh, Switch Off. "
    "Unique overcounts sheet-accurate (We Must Accelerate Our Plans x3). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("Dagobah: Yoda's Hut"),
    n("It Is The Future You See / A Tremor In The Force", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Rebel Gunrunner"),
    n("Dual Laser Cannon", True),
    n("Endor: Back Door"),
    n("Home One: War Room"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Harc Seff", True),
    n("Fixer"),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Threepio With His Parts Showing"),
    n("Corran Horn"),
    n("AT-RT", qty=3),
    n("Dash In Rogue 10"),
    n("Republic Gunship Wing", qty=2),
    n("Snowspeeder Garrison"),
    n("Home One"),
    n("Lady Luck"),
    n("Crash Site Memorial"),
    n("Imperial Atrocity", True),
    n("What're You Tryin' To Push On Us?"),
    n("Flash Of Insight", True),
    n("Projection Of A Skywalker"),
    n("Seeking An Audience", True),
    n("Either Way, You Win", True),
    n("It's Not My Fault!", True, qty=2),
    n("Crash Site Memorial", True),
    n("You Will Go To The Dagobah System", True, qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Let The Wookiee Win", True, qty=2),
    n("Control & Tunnel Vision", True),
    n("Desperate Tactics", qty=2),
    n("Slight Weapons Malfunction"),
    n("Rebel Artillery"),
    n("All Wings Report In & Darklighter Spin"),
    n("Precise Hit", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Affect Mind"),
    n("Aim High"),
    n("Another Pathetic Lifeform"),
    n("Chasm", True),
    n("Don't Do That Again"),
    n("Let's Keep A Little Optimism Here", True),
    n("Planetary Defenses", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Your Ship?"),
]
LS_ADD = []


DS_START = "Separatist Uprising / At War With Itself"
DS_CARDS = [
    n("Separatist Uprising / At War With Itself"),
    n("Geonosis: Separatist Council Room"),
    n("War Has Begun"),
    n("Everything Is Going As Planned"),
    n("An Entire Legion Of My Best Troops"),
    n("Battle Order & First Strike", True),
    n("Droid Racks"),
    n("Cloud City: Security Tower", True),
    n("Death Star: War Room", True),
    n("Blockade Flagship: Bridge"),
    n("Geonosis"),
    n("Geonosis: Rocky Plains"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("3B3-888", qty=2),
    n("OWO-1 With Backup", qty=2),
    n("B2 Super Battle Droid", qty=3),
    n("3B3-1204"),
    n("Infantry Battle Droid"),
    n("OOM-9", True),
    n("SSA-1015"),
    n("Battle Droid Blaster Rifle", qty=10),
    n("Slave I, Symbol Of Fear"),
    n("Blast Door Controls"),
    n("Note Tentacle", True),
    n("ComScan Detection", True),
    n("Note Gunnery", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("Force Push", True),
    n("Wounded Warrior", qty=2),
    n("Rally The Cause"),
    n("Oh, Switch Off", qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Ghhhk"),
    n("Take Them Away"),
    n("Lightsaber Deficiency", True),
    n("Imperial Artillery", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("After Her!", True),
    n("Allegations Of Corruption"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Imperial Detention"),
    n("There Is No Try"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
