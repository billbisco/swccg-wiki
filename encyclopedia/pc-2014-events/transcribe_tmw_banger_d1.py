#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Amar Banger (abanger).

Source: 2014-TMW-Day-1.pdf pages 19–20 (2013 form).
"""
from __future__ import annotations

PLAYER = "Amar Banger"
USERNAME = "abanger"
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 20
DS_PAGE = 19
LS_SCAN = "2014 Texas Mini Worlds Day 1 p20 Amar Banger LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p19 Amar Banger DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields)."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Amar Banger. Username abanger. LIGHT checked. Deck Name Sonn (V) Fixer. Event TMW 2014. "
    "AFA dested Anger, Fear, Aggression. "
    "Dagobah Yoda Hut dested Dagobah: Yoda's Hut. "
    "DODN & WA dested Do, Or Do Not & Wise Advice. "
    "BP & DTF dested Battle Plan & Draw Their Fire. "
    "IITFYS dested It Is The Future You See / A Tremor In The Force. "
    "YWGTDS dested You Will Go To The Dagobah System. "
    "OOC & TT dested Out Of Commission & Transmission Terminated. "
    "AWRI & DS dested All Wings Report In & Darklighter Spin. "
    "LTWW dested Let The Wookiee Win. "
    "Antilles Combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Gunship dested Republic Gunship. "
    "Leadership dested Rebel Leadership. "
    "Slight Weap Mal dested Slight Weapons Malfunction. "
    "INMF dested It's Not My Fault!. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "WYTTPOU dested What're You Tryin' To Push On Us?. "
    "Naked 3PO dested Threepio With His Parts Showing. "
    "H1:WR dested Home One: War Room. "
    "Your Ship dested Your Ship?. "
    "Unique overcounts sheet-accurate (You Will Go To The Dagobah System x3, "
    "Let The Wookiee Win x3, Rebel Leadership x3, Dual Laser Cannon x2, "
    "Escape Pod x2, Wesa Gotta Grand Army x3, Crash Site Memorial x2, "
    "Heading For The Medical Frigate x3, AT-RT x3). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Amar Banger. Username abanger. DARK checked. Deck Name Battle Droids. Event TMW 2014. "
    "K&D dested Knowledge And Defense. "
    "Separatist Uprising dested Separatist Uprising / At War With Itself. "
    "Ni Chuba dested Ni Chuba Na?. "
    "D*:WR dested Death Star: War Room. "
    "CC: Sec Tower dested Cloud City: Security Tower. "
    "BF: Bridge dested Blockade Flagship: Bridge. "
    "OWO w/ Backup dested OWO-1 With Backup. "
    "B2 Super Droid dested B2 Super Battle Droid. "
    "Slave I, SoF dested Slave I, Symbol Of Fear. "
    "SRF & WYB dested Short Range Fighters & Watch Your Back!. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Oh Switch Off dested Oh, Switch Off. "
    "YCHF dested You Cannot Hide Forever. "
    "DTHACC dested Do They Have A Code Clearance?. "
    "TINT dested There Is No Try. "
    "CHYBC dested Come Here You Big Coward. "
    "Unique overcounts sheet-accurate (Battle Droid Blaster Rifle x10, "
    "B2 Super Battle Droid x3, 3B3-888 x2, OWO-1 With Backup x2, "
    "We Must Accelerate Our Plans x3, Sonic Bombardment x3, Force Push x2, "
    "ComScan Detection x2, Imperial Artillery x2, Oh, Switch Off x2, "
    "Wounded Warrior x2). "
    "(V) from the checkbox; dittos inherit the first named line except where the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See / A Tremor In The Force"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Dagobah: Yoda's Hut"),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Dual Laser Cannon", True),
    n("Rebel Gunrunner"),
    n("It Is The Future You See / A Tremor In The Force", True),
    n("Snowspeeder Garrison"),
    n("Imperial Atrocity", True),
    n("Wesa Gotta Grand Army"),
    n("Desperate Tactics"),
    n("You Will Go To The Dagobah System", True, qty=3),
    n("Out Of Commission & Transmission Terminated"),
    n("All Wings Report In & Darklighter Spin"),
    n("Crash Site Memorial", qty=2),
    n("Precise Hit", True),
    n("Heading For The Medical Frigate", True, qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Republic Gunship", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Escape Pod", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Slight Weapons Malfunction"),
    n("Desperate Tactics"),
    n("It's Not My Fault!", True),
    n("Projection Of A Skywalker"),
    n("Luke Skywalker, Jedi Knight"),
    n("Flash Of Insight", True),
    n("AT-RT", qty=3),
    n("Luke Skywalker, Rebel Scout", True),
    n("Corran Horn", True),
    n("Admiral Ackbar", True),
    n("Houjix"),
    n("Lady Luck"),
    n("Home One"),
    n("Rebel Artillery"),
    n("Threepio With His Parts Showing"),
    n("What're You Tryin' To Push On Us?"),
    n("Naboo: Battle Plains"),
    n("Dash In Rogue 10"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Endor: Back Door"),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Fixer"),
    n("Harc Seff", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Grimtaash"),
    n("The Professor"),
    n("Chasm"),
    n("Affect Mind"),
    n("Aim High"),
    n("Another Pathetic Lifeform"),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Planetary Defenses", True),
    n("Ultimatum"),
    n("Weapons Display"),
    n("Yavin Sentry"),
    n("Your Insight Serves You Well", True),
    n("Your Ship?"),
]
LS_ADD = []


DS_START = "Separatist Uprising / At War With Itself"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Separatist Uprising / At War With Itself"),
    n("Geonosis: Separatist Council Room"),
    n("War Has Begun"),
    n("Everything Is Going As Planned"),
    n("Droid Racks"),
    n("An Entire Legion Of My Best Troops"),
    n("Ni Chuba Na?", True),
    n("Death Star: War Room", True),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Bridge"),
    n("Geonosis"),
    n("Geonosis: Rocky Plains"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("3B3-888", qty=2),
    n("B2 Super Battle Droid", qty=3),
    n("OWO-1 With Backup", qty=2),
    n("OOM-9", True),
    n("Infantry Battle Droid"),
    n("SSA-1015"),
    n("3B3-1204"),
    n("Slave I, Symbol Of Fear"),
    n("Battle Droid Blaster Rifle", qty=10),
    n("Blast Door Controls"),
    n("Note Tentacle", True),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("Force Push", True, qty=2),
    n("ComScan Detection", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lightsaber Deficiency", True),
    n("Imperial Artillery", qty=2),
    n("Oh, Switch Off", qty=2),
    n("Take Them Away"),
    n("Wounded Warrior", qty=2),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Firepower"),
    n("Do They Have A Code Clearance?", True),
    n("Death Star Sentry"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("Abyss", True),
    n("After Her!"),
    n("There Is No Try"),
    n("Fanfare", True),
    n("Imperial Detention"),
]
DS_ADD = []
