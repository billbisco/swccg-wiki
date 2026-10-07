#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Amar Banger Xerox AFA / K&D."""
from __future__ import annotations

PLAYER = "Amar Banger"
USERNAME = "abanger"
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 34
DS_PAGE = 35
LS_SCAN = "2013 Texas Mini Worlds Day 1 p34 Amar Banger LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p35 Amar Banger DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name Amar Banger. Username abanger. "
    "Deck Name The 1/1 Deck. Event Name TMW '13. LIGHT checked. "
    "Do not dest as a new person. Do not rewrite 2013 MPC Banger leftover "
    "or 2013 Worlds Banger leftover. "
    "AFA dested Anger, Fear, Aggression. "
    "Vengeance dested as written. "
    "Paw Harp dested Power Harpoon. "
    "Rebel Lead dested Rebel Leadership. "
    "Lando Hero dested Lando Calrissian, Unlikely Hero. "
    "HCF dested Han, Chewie, And The Falcon. "
    "Slight Weap Mal dested Slight Weapons Malfunction. "
    "Wesa dested Wesa Gotta Grand Army. "
    "Dash in Rogue dested Dash In Rogue 10. "
    "Heavy Turbo dested Heavy Turbolaser Battery. "
    "Intruder Mis dested Intruder Missile. "
    "Dual Las Can dested Dual Laser Cannon. "
    "OOC & TT dested Out Of Commission & Transmission Terminated. "
    "Speak w/ JC dested Speak With The Jedi Council. "
    "Tantive dested Tantive IV. "
    "Obi JK dested Obi-Wan Kenobi, Jedi Knight. "
    "Reb Artillery dested Rebel Artillery. "
    "Padme Nab dested Padme Naberrie. "
    "Flash of Fury dested Flash Of Fury as written. "
    "H1 dested Home One. "
    "Shmi dested Shmi Skywalker. "
    "Ackbar dested Admiral Ackbar. "
    "Naked 3PO dested Threepio With His Parts Showing. "
    "Luke's Skyhopper dested Luke's T-16 Skyhopper. "
    "Luke dested Luke Skywalker. "
    "Corran dested Corran Horn. "
    "Blue Squad B-wing dested Blue Squadron B-wing. "
    "Concus Mis dested Concussion Missiles. "
    "JCC dested Coruscant: Jedi Council Chamber. "
    "BNC dested Naboo: Boss Nass' Chambers. "
    "H1: WR dested Home One: War Room. "
    "Slave Quarters dested Tatooine: Slave Quarters. "
    "Hiding in the Garb dested Hiding In The Garbage. "
    "Beggar's Canyon dested Tatooine: Beggar's Canyon. "
    "BP & DTF dested Battle Plan & Draw Their Fire. "
    "DoDN & WA dested Do, Or Do Not & Wise Advice. "
    "Superficial Dam dested Superficial Damage. "
    "IITFYS dested It Is The Future You See. "
    "DDTA dested Don't Do That Again. "
    "Tragedy dested A Tragedy Has Occurred. "
    "Simple Trx dested Simple Tricks And Nonsense. "
    "The Prof dested The Professor. "
    "Your Ship dested Your Ship?. "
    "LKALOH dested Let's Keep A Little Optimism Here. "
    "Weap Disp dested Weapons Display. "
    "XISYW dested Your Insight Serves You Well. "
    "Unique overcounts sheet-accurate: Rebel Leadership x3, "
    "Wesa Gotta Grand Army x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name Amar Banger. Username abanger. "
    "Deck Name ATL Mistryl. Event Name TMW '13. DARK checked. "
    "Do not dest as a new person. Do not rewrite 2013 MPC Banger leftover "
    "or 2013 Worlds Banger leftover. "
    "K&D dested Knowledge And Defense. "
    "IZA dested IZA as written. "
    "Establish Control dested Establish Control. "
    "Prep Def dested Prepared Defenses. "
    "AOBS dested AOBS as written. "
    "Cor: Imp City dested Coruscant: Imperial City. "
    "Cor: Priv Plat dested Coruscant: Private Platform (Docking Bay). "
    "DF: Bridge dested Blockade Flagship: Bridge. "
    "Snoother dested Snoother as written. "
    "Prophetess dested Prophetess. "
    "Mara Hand dested Mara Jade, The Emperor's Hand. "
    "Onith dested Onith as written. "
    "EPP Iggy dested IG-88 With Riot Gun. "
    "Gardulla dested Gardulla The Hutt. "
    "EPP 4-LOM dested 4-LOM With Concussion Rifle. "
    "Rest Bolt dested Rest Bolt as written. "
    "DJ Lightsaber dested Dark Jedi Lightsaber. "
    "Mara Saber dested Mara Jade's Lightsaber. "
    "ZiMH dested Zuckuss In Mist Hunter. "
    "Lat Dam dested Lateral Damage. "
    "1st Strike dested First Strike. "
    "Broken Con dested Broken Concentration. "
    "AAA dested Ability, Ability, Ability. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "Stunning Lead dested Stunning Leader. "
    "Never Yalnal dested Nevar Yalnal. "
    "Jabba's Through dested Jabba's Through as written. "
    "Barrier dested Imperial Barrier. "
    "C&SFS dested Control & Set For Stun. "
    "SP: DB dested Spaceport Docking Bay. "
    "3720 dested 3,720 To 1. "
    "Ket Mal dested Ket Maliss. "
    "Tarkin Bounty dested Tarkin's Bounty. "
    "AUG dested A Useless Gesture. "
    "Allegations dested Allegations Of Corruption. "
    "BO dested Battle Order. "
    "Coward dested Come Here You Big Coward. "
    "D* Sentry dested Death Star Sentry. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "IFYLOFD dested I Find Your Lack Of Faith Disturbing. "
    "Detention dested Imperial Detention. "
    "TINT dested There Is No Try. "
    "Weapon of a Sith dested Weapon Of A Sith. "
    "YCHF dested You Cannot Hide Forever. "
    "Aurra Sing line 21-22 empty checkbox and line 23 (V) kept separate. "
    "Trophy Of A Kill line 25 (V) and line 26 empty kept separate. "
    "Unique overcounts sheet-accurate: We Must Accelerate Our Plans x5, "
    "Aurra Sing x3, Mara Jade, The Emperor's Hand x2, IG-88 With Riot Gun x2, "
    "4-LOM With Concussion Rifle x2, Zuckuss In Mist Hunter x2, "
    "Stunning Leader x2, Elis Helrot x2, Imperial Barrier x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Vengeance"),
    n("Rapid Fire"),
    n("Power Harpoon", qty=3),
    n("Sandspeeder", qty=7),
    n("Rebel Leadership", True, qty=3),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Han, Chewie, And The Falcon", True),
    n("Slight Weapons Malfunction"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Dash In Rogue 10", True),
    n("Heavy Turbolaser Battery"),
    n("Intruder Missile", qty=2),
    n("Dual Laser Cannon", True, qty=3),
    n("Precise Hit", True),
    n("Out Of Commission & Transmission Terminated"),
    n("Speak With The Jedi Council"),
    n("Tantive IV", True),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Rebel Artillery", qty=2),
    n("Padme Naberrie", True),
    n("Princess Leia", True),
    n("Flash Of Fury", True),
    n("Home One"),
    n("Shmi Skywalker"),
    n("Admiral Ackbar", True),
    n("Threepio With His Parts Showing"),
    n("Luke's T-16 Skyhopper"),
    n("Luke Skywalker", True),
    n("Corran Horn"),
    n("Blue Squadron B-wing", qty=3),
    n("Concussion Missiles", qty=2),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Tatooine: Slave Quarters"),
    n("Hiding In The Garbage", True),
    n("Tatooine: Beggar's Canyon"),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Superficial Damage", True),
    n("It Is The Future You See", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Your Ship?"),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = [
    n("Affect Mind"),
]


DS_START = "Knowledge And Defense"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("No Bargain", True),
    n("IZA", True),
    n("Establish Control", True),
    n("Prepared Defenses", True),
    n("AOBS"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Shada", True),
    n("Coruscant: Private Platform (Docking Bay)", True),
    n("Corulag"),
    n("Blockade Flagship: Bridge"),
    n("Snoother", True),
    n("Prophetess", True),
    n("Mara Jade, The Emperor's Hand", qty=2),
    n("Onith"),
    n("IG-88 With Riot Gun", qty=2),
    n("Gardulla The Hutt", True),
    n("Aurra Sing", qty=2),
    n("Aurra Sing", True),
    n("4-LOM With Concussion Rifle", qty=2),
    n("Trophy Of A Kill", True),
    n("Trophy Of A Kill"),
    n("Rest Bolt"),
    n("Dark Jedi Lightsaber", True),
    n("Mara Jade's Lightsaber", True),
    n("Zuckuss In Mist Hunter", qty=2),
    n("No Escape"),
    n("Lateral Damage"),
    n("Jabba's Haven", True),
    n("First Strike"),
    n("Disarmed", qty=2),
    n("Broken Concentration"),
    n("Ability, Ability, Ability"),
    n("We Must Accelerate Our Plans", qty=5),
    n("Vader's Obsession"),
    n("Stunning Leader", True, qty=2),
    n("Nevar Yalnal"),
    n("Jabba's Through", qty=2),
    n("Imperial Barrier", qty=2),
    n("Control & Set For Stun"),
    n("Elis Helrot", qty=2),
    n("Spaceport Docking Bay", True),
    n("3,720 To 1", True),
    n("Ket Maliss", True),
    n("Tarkin's Bounty", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention", True),
    n("Resistance"),
    n("Secret Plans"),
]
DS_ADD = [
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
]
