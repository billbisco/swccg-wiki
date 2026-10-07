#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Alex Klimenko.

Source: Yavin42012.pdf pages 18–22 typed dumps.
p18–p19 Light Dantooine Base II / p20–p22 Dark Imperial Occupation/Imperial Control.
Name Alex Klimenko handwritten dested Alex Klimenko analog leftover
generate/transcribe/file_player empty dest as written.
Username blank. Pack player-stubs/Alex_Klimenko.wiki.
Do not dest as Alex Klimo. Do not dest as a new last-name Klimenko.
"""
from __future__ import annotations

PLAYER = "Alex Klimenko"
USERNAME = ""
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 18
DS_PAGE = 20
LS_SCAN = "2012 Yavin 4 Regionals Alex Klimenko LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Alex Klimenko DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p18–p19 Light typed dump / p20–p22 Dark typed dump. "
    "Name Alex Klimenko handwritten dested Alex Klimenko analog leftover "
    "generate/transcribe/file_player empty dest as written. "
    "Username blank. Facing pair analog leftover Skilton. "
    "Do not dest as Alex Klimo. Do not dest as a new last-name Klimenko. "
    "Pack player-stubs/Alex_Klimenko.wiki."
)
LS_NOTE = (
    "Typed dump p18–p19 Light Dantooine Base II. Name Alex Klimenko dest as written. "
    "Username blank. Deck Name Dantooine Base II dested off article. "
    "Dantooine Base Operations/More Dangerous Than You Realize dested "
    "Dantooine Base Operations / More Dangerous Than You Realize analog leftover Micah Wall. "
    "Dantooine: Base – Operations Center (v) dested True analog leftover Micah Wall. "
    "Faithful Serivce dested Faithful Service analog leftover dest as written slang. "
    "A280 Sharpshooter Rifle (v) qty=2. Naboo Blaster Rifle qty=2. "
    "X-Wing Assault Squadron qty=3. Y-Wing Assault Squadron qty=4. "
    "Eject! Eject! & Imperial Atrocity (v) dested analog leftover dest as written combo. "
    "It Could Be Worse qty=3. Rebel Ambush qty=2. Organized Attack qty=2. "
    "Dantooine Base – Docking Bay dested Dantooine: Base - Docking Bay analog leftover typical. "
    "Forest dested dest as written. Jungle dested dest as written. "
    "Kiffex dested analog leftover TYPE_OVERRIDE Location. "
    "Handwritten shields p19 dest empty analog leftover dest as written. "
    "Do or Do Not dested Do, Or Do Not analog leftover Skilton. "
    "Ounee Ta dested analog leftover Rossi. Unique 60 shields 11."
)
DS_NOTE = (
    "Typed dump p20–p22 Dark Imperial Occupation/Imperial Control. "
    "Name Alex Klimenko dest as written. Username blank. "
    "Imperial Occupation/Imperial Control (v) dested Imperial Occupation / Imperial Control True analog leftover Anderson. "
    "Hoth: 1st marker – Main Power Generator dested Hoth: Main Power Generators analog leftover Rambo. "
    "Hoth: 5th marker – Ice Plains dested Hoth: Ice Plains True analog leftover Anderson. "
    "Knowledge And Defense (v) dested True analog leftover Anderson IN THE 60. "
    "Veers dested General Veers analog leftover Westergard. "
    "Tempest 1 dested Tempest Scout 1 analog leftover Mike. "
    "Marquand in Blizzard 6 dested Marquand In Blizzard 6 analog leftover Peterson. "
    "Laser Cannon Battery qty=2. AT-AT Cannon (v) qty=2. Target The Main Generator qty=2. "
    "Imperial Artillery qty=3. "
    "Hoth: 3rd Marker – Defensive Perimeter dested Hoth: Defensive Perimeter analog leftover Anderson. "
    "Hoth: 4th Marker – North Ridge dested Hoth: North Ridge analog leftover dest as written. "
    "Hoth: 6th Marker – Mountains dested Hoth: Mountains analog leftover Anderson. "
    "Handwritten shields p22 dest empty analog leftover dest as written. "
    "Fire Power dested Firepower analog leftover TMW Joe. "
    "Leave Them To Me dested analog leftover Brist. Unique 60 shields 10."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Dantooine Base Operations / More Dangerous Than You Realize"
LS_CARDS = [
    n("Dantooine Base Operations / More Dangerous Than You Realize"),
    n("Dantooine"),
    n("Dantooine: Base - Operations Center", True),
    n("Don't Underestimate Our Chances", True),
    n("Dantooine Engineering Corps", True),
    n("Strike Planning"),
    n("Faithful Service", True),
    n("Anger, Fear, Aggression", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Lando Calrissian, Scoundrel"),
    n("General Solo"),
    n("General Crix Madine"),
    n("Red Leader", True),
    n("Colonel Cracken"),
    n("Lieutenant Page"),
    n("Lieutenant Greeve"),
    n("Orrimaarko"),
    n("Sergeant Brooks Carlson"),
    n("Corporal Kensaric"),
    n("Corporal Midge"),
    n("Corporal Janse"),
    n("A280 Sharpshooter Rifle", True, qty=2),
    n("Naboo Blaster Rifle", qty=2),
    n("Liberty"),
    n("Spiral"),
    n("Bright Hope", True),
    n("X-Wing Assault Squadron", qty=3),
    n("Y-Wing Assault Squadron", qty=4),
    n("Eject! Eject! & Imperial Atrocity", True),
    n("Houjix"),
    n("First Aid"),
    n("Slight Weapons Malfunction"),
    n("Blaster Proficiency"),
    n("Rebel Barrier"),
    n("Rebel Leadership"),
    n("It Could Be Worse", qty=3),
    n("Out Of Nowhere"),
    n("Changing The Odds", True),
    n("Rebel Ambush", qty=2),
    n("Organized Attack", qty=2),
    n("Insertion Planning"),
    n("Escape Pod", True),
    n("Rebel Artillery"),
    n("Dantooine: Base - Docking Bay", True),
    n("Forest"),
    n("Jungle"),
    n("Coruscant"),
    n("Kiffex"),
    n("Kessel"),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Don't Do That Again"),
    n("The Professor"),
    n("Do, Or Do Not"),
    n("Wise Advice"),
    n("Your Insight Serves You Well"),
    n("Ounee Ta"),
    n("Weapons Display"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Main Power Generators"),
    n("Hoth: Ice Plains", True),
    n("Imperial Decree"),
    n("Prepared Defenses"),
    n("Prepare For A Surface Attack"),
    n("You May Start Your Landing"),
    n("Endor Shield", True),
    n("Knowledge And Defense", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Arica", True),
    n("Boba Fett, Bounty Hunter", True),
    n("Grand Admiral Thrawn"),
    n("Admiral Chiraneau"),
    n("General Veers", True),
    n("General Nevar", True),
    n("Commander Igar"),
    n("Lieutenant Watts"),
    n("Dr. Evazan & Ponda Baba"),
    n("P-59"),
    n("U-3PO"),
    n("Blizzard Scout 1", True),
    n("Blizzard 1"),
    n("Blizzard 2"),
    n("Blizzard 4", True),
    n("Marquand In Blizzard 6", True),
    n("Tempest Scout 1"),
    n("Chimaera"),
    n("Judicator"),
    n("Dominator"),
    n("Dreadnaught"),
    n("Colonel Jendon In Onyx 1", True),
    n("Onyx 2", True),
    n("Bossk In Hound's Tooth"),
    n("Laser Cannon Battery", qty=2),
    n("AT-AT Cannon", True, qty=2),
    n("Electro-Rangefinder"),
    n("Target The Main Generator", qty=2),
    n("Hoth Blockade", True),
    n("Image Of The Dark Lord", True),
    n("Imperial Propaganda", True),
    n("He Is Not Ready & Imperial Propaganda", True),
    n("Ghhhk"),
    n("Imperial Barrier"),
    n("Imperial Command"),
    n("Walker Garrison"),
    n("Surface Defense"),
    n("Masterful Move"),
    n("Outflank", True),
    n("Wounded Warrior"),
    n("Imperial Artillery", qty=3),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: North Ridge"),
    n("Hoth: Mountains"),
]
DS_SHIELDS = [
    n("Leave Them To Me"),
    n("Abyss"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Firepower"),
    n("There Is No Try"),
    n("Imperial Detention"),
    n("Fanfare"),
]
DS_ADD = []
