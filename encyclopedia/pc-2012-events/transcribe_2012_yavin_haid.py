#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Tom Haid.

Source: Yavin42012.pdf pages 25–26.
p25 Dark handwritten 2010 Xerox / p26 Light handwritten 2010 Xerox.
Name Tom Llaid dested Tom Haid analog leftover p26 filled Name Tom Haid /
generate_2013_worlds.py CANON / player-stubs/Tom_Haid.wiki /
transcribe_2013_worlds_haid.py USERNAME Xenth.
Username Xanth dested USERNAME as written this sheet analog leftover
2013 Worlds Xenth same identity. Pack player-stubs/Tom_Haid.wiki.
Do not dest as a new person. Do not dest as first-name-only Tom.
Do not dest as Tom H. Do not dest 2013 Worlds Tom Haid 60s again.
"""
from __future__ import annotations

PLAYER = "Tom Haid"
USERNAME = "Xanth"
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 26
DS_PAGE = 25
LS_SCAN = "2012 Yavin 4 Regionals Tom Haid LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Tom Haid DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p25 Dark handwritten 2010 Xerox / p26 Light handwritten 2010 Xerox. "
    "Name Tom Llaid dested Tom Haid analog leftover p26 filled Name Tom Haid / "
    "generate_2013_worlds.py CANON / player-stubs/Tom_Haid.wiki. "
    "Username Xanth dested USERNAME as written this sheet analog leftover "
    "2013 Worlds Xenth same identity. "
    "Event Date 6/30/12 Event Name Yavin IV Regionals dest Yavin 4 facing pair analog leftover Orthner. "
    "Deck Name Walkers / Falcon Punch! dested off article. "
    "Do not dest as a new person. Do not dest as first-name-only Tom. "
    "Do not dest as Tom H. Do not dest 2013 Worlds Tom Haid 60s again. "
    "Pack player-stubs/Tom_Haid.wiki."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p26 Light. Name Tom Haid Username Xanth. "
    "Event Date 6/30/12 Event Name Yavin IV Regionals dest Yavin 4 facing pair. LIGHT checked. "
    "Watch Your Step / This Place Can Be A Little Rough dested analog leftover Atkin True. "
    "Mil. Falcon dested Millennium Falcon analog leftover dest as written slang. "
    "Corellian Eng. Corp dested Corellian Engineering Corporation analog leftover dest as written slang. "
    "Lowrick dested analog leftover dest as written. "
    "Sergeant Brickman dested analog leftover dest as written slang Bruckman. "
    "Gen. Crix Madine dested General Crix Madine analog leftover Klimenko. "
    "BoShek, Boon Smug. dested BoShek, Brash Smuggler analog leftover Massung. "
    "Artoo & 3PO dested analog leftover dest as written combo. "
    "Flish of Insight dested Flash Of Insight analog leftover dest as written slang. "
    "No Questions Asked True line 15 KEEP SEPARATE from empty line 34 analog leftover McCune differing checkboxes. "
    "Punch It! empty lines 35/39 dest qty=2 at first analog leftover non-consecutive. "
    "Rebel Leadership True lines 32/45 dest qty=2 at first analog leftover non-consecutive. "
    "Life Debt empty lines 42/49 dest qty=2 at first analog leftover non-consecutive. "
    "Corellian Retort True lines 44/57 dest qty=2 at first analog leftover non-consecutive. "
    "Wesa Gotta Grand Army empty lines 55/58 dest qty=2 at first analog leftover non-consecutive. "
    "I Wonder Who They Found True qty=2 analog leftover Cooleo consecutive. "
    "Legendery dested Legendary Starfighter analog leftover dest as written slang. "
    "Lando Cal, Scoundrel dested Lando Calrissian, Scoundrel analog leftover Westergard. "
    "Baita Tank dested Bacta Tank analog leftover Scott dest as written slang. "
    "Weapon Display dested Weapons Display analog leftover dest as written slang. "
    "Yavin Sgntry dested Yavin Sentry analog leftover dest as written slang. "
    "Jabba's Palace True dest dest as written extra S1112 clip as shield. "
    "Shields 1–12 filled. Unique 60 shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p25 Dark. Name Tom Llaid dested Tom Haid analog leftover p26 filled Name. "
    "Username Xanth. Event Date 6/30/12 Event Name Yavin IV Regionals dest Yavin 4 facing pair. DARK checked. "
    "Imperial Occupation / ... dested Imperial Occupation / Imperial Control True analog leftover Anderson. "
    "1st Marker (LS) dested Hoth: Main Power Generators analog leftover Rambo. "
    "5th Marker dested Hoth: Ice Plains analog leftover Anderson. "
    "3rd Marker dested Hoth: Defensive Perimeter analog leftover Anderson. "
    "6th Marker dested Hoth: Mountains analog leftover Anderson. "
    "Knowledge & Defense dested Knowledge And Defense True analog leftover Anderson IN THE 60. "
    "Imp. Artillery dested Imperial Artillery analog leftover Brummett qty=2 at first lines 13/34 analog leftover non-consecutive. "
    "Thrawn dested Grand Admiral Thrawn analog leftover typical. "
    "Flagship Executor dested Executor analog leftover dest as written slang. "
    "Tempest 1 dested Tempest Scout 1 analog leftover Mike. "
    "Veers dested General Veers analog leftover Westergard. "
    "Marquand In Blizz 6 dested Marquand In Blizzard 6 analog leftover Peterson. "
    "We're In Attack Pos. Now dested We're In Attack Position Now qty=2 at first lines 31/40 analog leftover non-consecutive. "
    "A Dark Time For The Rebellion True qty=4 analog leftover consecutive ditto unique overcount sheet-accurate. "
    "Imp. Command dested Imperial Command qty=3 analog leftover consecutive. "
    "AT-AT Cannon True lines 30/50 dest qty=2 at first analog leftover non-consecutive. "
    "Victory True lines 16/57 dest qty=2 at first analog leftover non-consecutive. "
    "Ghhhk & Those Rebels Won't... dested Ghhhk & Those Rebels Won't Escape Us analog leftover TMW Joe. "
    "Cold Feet True qty=2 analog leftover consecutive TYPE_OVERRIDE. "
    "Control empty qty=2 analog leftover consecutive dest as written. "
    "Shields 1–12 filled. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("General Solo", True),
    n("Millennium Falcon"),
    n("Corellia", True),
    n("Spaceport City"),
    n("Rycar Ryjerd", True),
    n("Corellian Engineering Corporation", True),
    n("Scomp Link Access", True),
    n("Anger, Fear, Aggression", True),
    n("Menace Fades"),
    n("Strikeforce", True),
    n("Hindsight", True),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("No Questions Asked", True),
    n("Spaceport Scoundrels Guild", True),
    n("Boss Nass Chambers"),
    n("We're Doomed"),
    n("How Did We Get Into This Mess?"),
    n("Lowrick", True),
    n("Sergeant Brickman"),
    n("General Crix Madine"),
    n("Wedge Antilles", True),
    n("Paleso Rashad"),
    n("Mirax Terrik"),
    n("BoShek, Brash Smuggler", True),
    n("Corran Horn"),
    n("2-1B", True),
    n("Han's Toolkit"),
    n("Artoo & 3PO"),
    n("Hopping Mad", True),
    n("Rebel Leadership", True, qty=2),
    n("Flash Of Insight", True),
    n("No Questions Asked"),
    n("Punch It!", qty=2),
    n("Chewie", True),
    n("Let The Wookiee Win", True),
    n("Leia, Rebel Princess"),
    n("I've Got A Bad Feeling About This"),
    n("Legendary Starfighter"),
    n("Life Debt", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Corellian Retort", True, qty=2),
    n("Honor Of The Jedi"),
    n("Bacta Tank"),
    n("Thank The Maker"),
    n("Hear Me Baby, Hold Together", True),
    n("It Could Be Worse"),
    n("Moving To Attack Position"),
    n("That's One", True),
    n("Artoo, I Have A Bad Feeling About This"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Home One: War Room"),
    n("I Wonder Who They Found", True, qty=2),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("Battle Plan", True),
    n("Don't Do That Again"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Weapons Display", True),
    n("Do, Or Do Not"),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("Jabba's Palace", True),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth: Main Power Generators"),
    n("Hoth: Ice Plains", True),
    n("Hoth"),
    n("Knowledge And Defense", True),
    n("Prepared Defenses"),
    n("Imperial Decree"),
    n("Prepare For A Surface Attack"),
    n("You May Start Your Landing"),
    n("Endor Shield", True),
    n("Walker Garrison"),
    n("Trample"),
    n("Imperial Artillery", qty=2),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Mountains"),
    n("Victory", True, qty=2),
    n("Grand Admiral Thrawn"),
    n("Hoth Blockade", True),
    n("Executor"),
    n("Do They Have A Code Clearance?"),
    n("No Escape"),
    n("Something Special Planned For Them", True),
    n("Blizzard 1", True),
    n("Blizzard 4"),
    n("General Nevar", True),
    n("Marquand In Blizzard 6", True),
    n("Admiral Piett"),
    n("Tempest Scout 1"),
    n("General Veers", True),
    n("AT-AT Cannon", True, qty=2),
    n("We're In Attack Position Now", qty=2),
    n("Lightsaber Deficiency", True),
    n("Dominator", True),
    n("A Dark Time For The Rebellion", True, qty=4),
    n("Conquest", True),
    n("Imperial Command", qty=3),
    n("Stop Motion", True),
    n("Alert My Star Destroyer"),
    n("Grand Moff Tarkin", True),
    n("Operational As Planned", True),
    n("Cold Feet", True, qty=2),
    n("Blizzard 2", True),
    n("Commander Igar", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Control", qty=2),
    n("Protocol Failure", True),
    n("Admiral Ozzel"),
    n("ISB Sector Commander", True),
    n("Target The Main Generator"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Reactor Terminal", True),
    n("Oppressive Enforcement"),
    n("Death Star Sentry", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("There Is No Try"),
]
DS_ADD = []
