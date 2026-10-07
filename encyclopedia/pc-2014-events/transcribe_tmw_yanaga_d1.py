#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Ganden Yanaga (Cam Solusar).

Source: 2014-TMW-Day-1.pdf pages 15–16 (2013 form).
"""
from __future__ import annotations

PLAYER = "Ganden Yanaga"
USERNAME = "Cam Solusar"
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 15
DS_PAGE = 16
LS_SCAN = "2014 Texas Mini Worlds Day 1 p15 Ganden Yanaga LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p16 Ganden Yanaga DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields)."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Camden Yanaga dested Ganden Yanaga. Username Cam Solusar. LIGHT checked. "
    "Deck Name Berkeley Step Y, Grimtaash Style. Event Texas Mini Worlds. "
    "Watch Your Step / This Place (V) dested Watch Your Step / This Place Can Be A Little Rough. "
    "C7 Spaceport City dested Corellia: Spaceport City. "
    "C7 Spaceport Street dested Corellia: Spaceport Street. "
    "C7 Spaceport DB dested Corellia: Spaceport Docking Bay. "
    "C7 Spaceport Scoundrels dested Corellia: Spaceport Scoundrels. "
    "H1:DB dested Home One: Docking Bay. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "LTWW dested Let The Wookiee Win. "
    "Antilles Man dested Antilles Maneuver. "
    "Antilles Maneuver & Reb Reinf dested Antilles Maneuver & Rebel Reinforcements. "
    "CEC dested Corellian Engineering Corporation. "
    "NQA dested No Questions Asked. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader. "
    "Chewie dested Chewie, Enraged. "
    "AWRI & DS dested All Wings Report In & Darklighter Spin. "
    "Mace MOTO dested Mace Windu, Master Of The Order. "
    "Palejo dested Palejo Reshad. "
    "Landica dested Landing Claw. "
    "Corellian Retort line 58 crossed, Corellian Slip dested Corellian Slip. "
    "Your Insight dested Your Insight Serves You Well. "
    "Lets Keep dested Let's Keep A Little Optimism Here. "
    "Your Ship dested Your Ship?. "
    "Unique overcounts sheet-accurate (No Questions Asked x3, Imperial Atrocity x2, "
    "All Wings Report In & Darklighter Spin x2, Luke Skywalker, Jedi Knight x2). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Camden Yanaga dested Ganden Yanaga. Username Cam Solusar. DARK checked. "
    "Deck Name Berkeley Walkers Flower-Power style. Event Texas Mini Worlds. "
    "IO/IC (V) dested Imperial Occupation / Imperial Control. "
    "Hoth: MPGs dested Hoth: Main Power Generators. "
    "YMSYL dested You May Start Your Landing. "
    "Maarek Stele dested Maarek Stele, The Emperor's Reach. "
    "WIAPN dested We're In Attack Position Now. "
    "Control & SFS dested Control & Set For Stun. "
    "Marquand in Blizz 6 dested Marquand In Blizzard 6. "
    "DVDLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "U3PO dested U-3PO (Yoc-Threepio). "
    "GMT dested Grand Moff Tarkin. "
    "Veers dested General Veers. "
    "K&D dested Knowledge And Defense. "
    "Victory dested Victory as written. "
    "HHCBY dested as written. "
    "DTHACC dested as written. "
    "CHYBC dested Come Here You Big Coward. "
    "YCHF dested You Cannot Hide Forever. "
    "TINT dested There Is No Try. "
    "Unique overcounts sheet-accurate (Imperial Command x3, Garindan x2, Force Push x2, "
    "A Dark Time For The Rebellion x2, Imperial Decree x2, Cease Fire! x2, "
    "We're In Attack Position Now x2, Blizzard 4 x2). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Corellia: Spaceport City"),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Corellia: Spaceport Street"),
    n("Corellia: Spaceport Docking Bay"),
    n("Corellia: Spaceport Scoundrels"),
    n("Home One: Docking Bay"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Antilles Maneuver", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Corellian Retort", True, qty=2),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("No Questions Asked", True, qty=3),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Obi-Wan In Radiant VII"),
    n("Tantive IV", True),
    n("Padmé Naberrie", True),
    n("Mirax Terrik"),
    n("Jaina Solo"),
    n("Chewie, Enraged", True),
    n("Rebel Barrier", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Escape Pod", True),
    n("Houjix"),
    n("Yoda, Great Warrior"),
    n("Crix Madine"),
    n("Seeking An Audience", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Imperial Atrocity", True),
    n("Mace Windu, Master Of The Order"),
    n("Palejo Reshad"),
    n("You've Got A Lot Of Guts"),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Punch It!"),
    n("Imperial Atrocity", True),
    n("Landing Claw", True),
    n("Evacuation Control", True),
    n("Sergeant Brickman"),
    n("Dash Rendar", True),
    n("Romas 'Lock' Navander"),
    n("Corellian Slip", True),
    n("Grimtaash"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again"),
    n("Chasm"),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Weapons Display"),
    n("Yavin Sentry"),
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("Your Insight Serves You Well"),
    n("Let's Keep A Little Optimism Here"),
    n("Planetary Defenses"),
    n("Do, Or Do Not"),
    n("Jabba's Prize"),
    n("Your Ship?"),
]
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Imperial Decree"),
    n("Imperial Decree", True),
    n("Hoth"),
    n("Hoth: Main Power Generators", True),
    n("Hoth: 5th Marker", True),
    n("Prepared Defenses", True),
    n("Ni Chuba Na?", True),
    n("You May Start Your Landing", True),
    n("Endor Shield", True),
    n("Force Push", True),
    n("Trample"),
    n("Garindan", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("General Nevar"),
    n("A Dark Time For The Rebellion", True),
    n("Hoth Blockade"),
    n("Blizzard 4"),
    n("Target The Main Generator"),
    n("DTHACC"),
    n("AT-AT Cannon", True),
    n("We're In Attack Position Now", True),
    n("Control & Set For Stun"),
    n("Jango Fett, The Assassin"),
    n("Marquand In Blizzard 6"),
    n("Safe Passage"),
    n("Blizzard 4"),
    n("Blizzard 2", True),
    n("Imperial Command"),
    n("Wipe Them Out, All Of Them", True),
    n("Commander Igar", True),
    n("We're In Attack Position Now"),
    n("Flagship Executor"),
    n("Hoth: 6th Marker"),
    n("Admiral Piett"),
    n("Garindan", True),
    n("No Escape"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Force Push", True),
    n("Tempest 1"),
    n("Victory", qty=2),
    n("Hoth: 3rd Marker"),
    n("HHCBY"),
    n("Conquest", True),
    n("Imperial Command"),
    n("Walker Garrison"),
    n("Cease Fire!", qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Image Of The Dark Lord", True),
    n("Grand Admiral Thrawn"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("U-3PO (Yoc-Threepio)"),
    n("Grand Moff Tarkin", True),
    n("General Veers", True),
    n("Imperial Command", True),
    n("Blizzard 1"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Leave Them To Me"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Abyss"),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture"),
    n("Come Here You Big Coward"),
    n("Firepower"),
    n("Resistance"),
    n("Imperial Detention"),
    n("Oppressive Enforcement"),
]
DS_ADD = []
