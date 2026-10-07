#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Steve Harpster handwritten 2013 Print Form LS+DS.

Name field HARPSTER. Username blank. Dest Steve Harpster (file_player Harpster).
"""
from __future__ import annotations

PLAYER = "Steve Harpster"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 13
DS_PAGE = 14
LS_SCAN = "2013 SoCal Grand Prix Day 1 p13 Steve Harpster LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p14 Steve Harpster DS.png"
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name HARPSTER dested Steve Harpster. Username blank. "
    "LIGHT/DARK empty; dest Light from AFA (V) plus WYS (V). "
    "Do not dest as a new person. Do not rewrite 2013 MPC HARPSTER leftover. "
    "AFA dested Anger, Fear, Aggression. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough True. "
    "Falcon dested Han, Chewie, And The Falcon. "
    "Dash Radar dested Dash Rendar. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader. "
    "NQA dested No Questions Asked. "
    "Insurrection Combo dested Insurrection & Aim High. "
    "CBC dested It Could Be Worse. "
    "Scoundrel's Guild dested Scoundrel's Guild as written. "
    "Padme dested Padme Naberrie. "
    "Lea EP dested Leia With Blaster Rifle. "
    "All Wings Combo dested All Wings Report In & Darklighter Spin. "
    "Chewie dested Chewie. "
    "Seekers dested Seekers as written. "
    "You've Got A Lot dested You've Got A Lot Of Guts Coming Here. "
    "Field Presence dested Field Presence as written. "
    "Atrocity dested Imperial Atrocity. "
    "EWYW dested EWYW as written. "
    "Control Combo dested Control & Tunnel Vision. "
    "Wookiee Win dested Let The Wookiee Win. "
    "Punch It dested Punch It. "
    "Taletjie Reshad dested Taletjie Reshad as written. "
    "Crix dested Crix Madine as written. "
    "Brocuman dested Brokuman as written. "
    "Another Man dested Antilles Maneuver. "
    "Mace MOTO dested Mace Windu, Master Of The Order. "
    "Fallen Jedi dested Fallen Jedi as written. "
    "Jedi Luke dested Luke Skywalker, Jedi Knight. "
    "It's A Trap dested It's A Trap. "
    "Luxury Yacht dested Lady Luck. "
    "Booster's SD dested Booster's Star Destroyer as written. "
    "Obi in Red 7 dested Obi-Wan In Red 7 as written. "
    "Shield 4 Frozen Carbon dested Frozen Assets. "
    "Unique overcounts sheet-accurate: No Questions Asked x3, "
    "All Wings Report In & Darklighter Spin x2, Let The Wookiee Win x2, "
    "Dash Rendar x2, Wedge Antilles, Red Squadron Leader x2, "
    "Antilles Maneuver x2, Luke Skywalker, Jedi Knight x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name HARPSTER dested Steve Harpster. Username blank. "
    "Event SDGP. LIGHT/DARK empty; dest Dark from ROPS (AFA crossed, K+D (V) "
    "in the 60 as Interrupt). Do not dest as a new person. "
    "Do not rewrite 2013 MPC HARPSTER leftover. "
    "K+D dested Knowledge And Defense. "
    "ROPS dested Ralltiir Operations / In The Hands Of The Empire without True. "
    "Gene Nevar dested General Nevar. "
    "Droids dested Droids as written. "
    "Darth Vader Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Imp Domination dested Imperial Domination. "
    "Commander Traj dested Commander Traj as written. "
    "The Emp's (VAP) dested Maarek Stele, The Emperor's Reach. "
    "Ice Heart dested Ysanne Isard. "
    "He Hasn't Gone Back Yet dested He Hasn't Gone Back Yet as written. "
    "You Sounded Me dested You Sounded Me as written. "
    "GHHHK Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Flagship Executor dested Flagship Executor. "
    "Colonel Dave Jon dested Colonel Davod Jon. "
    "Victory dested Victory-Class Star Destroyer. "
    "CT Ground dested CT Ground as written. "
    "ISB Sector Command dested ISB Sector Command as written. "
    "Katalia dested Katalia as written. "
    "Ralltiir's Financial District dested Ralltiir: Financial District as written. "
    "ditto Prefect's Office dested Spaceport Prefect's Office. "
    "Unique overcounts sheet-accurate: Imperial Command x3, "
    "Imperial Domination x2, Blizzard 4 x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Han, Chewie, And The Falcon", True),
    n("Dash Rendar", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Fallen Portal"),
    n("Rebel Barrier"),
    n("General Solo", True),
    n("Corellia", True),
    n("Spaceport Street"),
    n("No Questions Asked", True),
    n("Insurrection & Aim High"),
    n("It Could Be Worse", True),
    n("Spaceport City"),
    n("Scoundrel's Guild", True),
    n("Bacta Tank"),
    n("Spaceport Docking Bay"),
    n("Home One: Docking Bay"),
    n("Padme Naberrie", True),
    n("Strike Planning"),
    n("Leia With Blaster Rifle"),
    n("No Questions Asked", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("That's One", True),
    n("Chewie", True),
    n("Heading For The Medical Frigate"),
    n("Seekers", True),
    n("You've Got A Lot Of Guts Coming Here"),
    n("Menace Fades"),
    n("Field Presence", True),
    n("Imperial Atrocity", True),
    n("EWYW", True),
    n("Control & Tunnel Vision"),
    n("Let The Wookiee Win", True, qty=2),
    n("Punch It"),
    n("Taletjie Reshad"),
    n("Dash Rendar", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Crix Madine"),
    n("Brokuman"),
    n("Mirax Terrik"),
    n("Corran Horn"),
    n("Corellian Slip", True),
    n("Antilles Maneuver", True, qty=2),
    n("Escape Pod", True),
    n("Houjix"),
    n("Mace Windu, Master Of The Order", True),
    n("Fallen Jedi", True),
    n("Master Qui-Gon", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Lando Calrissian, Unlikely Hero", True),
    n("No Questions Asked", True),
    n("It's A Trap"),
    n("Lady Luck", True),
    n("Booster's Star Destroyer", True),
    n("Obi-Wan In Red 7", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Frozen Assets", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Do, Or Do Not"),
    n("Wise Advice"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("He Can Go About His Business", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Ultimatum", True),
    n("Chasm", True),
]
LS_ADD = []


DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Blizzard 2", True),
    n("Blizzard 1", True),
    n("Tempest 1"),
    n("General Veers", True),
    n("General Nevar", True),
    n("Admiral Piett"),
    n("Sergeant Barich"),
    n("Sergeant Irol", True),
    n("Droids"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Arica"),
    n("Ghhhk", True),
    n("Imperial Domination", True),
    n("Conquest", True),
    n("Imperial Arrest Order"),
    n("Imperial Justice", True),
    n("Commander Traj", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Ysanne Isard", True),
    n("Outflank", True),
    n("Prepared Defenses", True),
    n("Alter", True),
    n("Stop Motion", True),
    n("He Hasn't Gone Back Yet"),
    n("Cold Feet", True),
    n("Protocol Failure", True),
    n("You Sounded Me", True),
    n("Imperial Command", qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lightsaber Deficiency", True),
    n("Garindan", True),
    n("Grand Admiral Thrawn"),
    n("Flagship Executor"),
    n("Admiral Ozzel"),
    n("Colonel Davod Jon"),
    n("Victory-Class Star Destroyer", True),
    n("Insignificant Rebellion", True),
    n("Imperial Domination", True),
    n("Establish Control", True),
    n("We're In Attack Position Now"),
    n("CT Ground", True),
    n("ISB Sector Command", True),
    n("Admiral Chiraneau"),
    n("Close Call", True),
    n("Katalia", True),
    n("Fondor"),
    n("Naboo"),
    n("Ralltiir"),
    n("Ralltiir: Financial District", True),
    n("Spaceport Street"),
    n("Spaceport Prefect's Office"),
    n("Spaceport Docking Bay"),
    n("Spaceport City"),
    n("Executor: Docking Bay"),
    n("Blizzard 4", qty=2),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Fanfare", True),
    n("Battle Order"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("A Useless Gesture"),
    n("Firepower", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Leave Them To Me", True),
]
DS_ADD = []
