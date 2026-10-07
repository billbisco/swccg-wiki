#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Tom handwritten Print Form LS+DS.

Name field Tom. Username blank. Dest Tom as written (first name only).
"""
from __future__ import annotations

PLAYER = "Tom"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 21
DS_PAGE = 22
LS_SCAN = "2013 SoCal Grand Prix Day 1 p21 Tom LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p22 Tom DS.png"
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name Tom dested as written. Username blank. "
    "Deck Name Same deck as last 5 years. LIGHT/DARK empty; dest Light from WYS. "
    "WYS checkbox empty dested Watch Your Step / This Place Can Be A Little Rough "
    "without True. CEC dested It Could Be Worse. "
    "Insurrection & Aim High dested Insurrection & Aim High. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Falcon dested Han, Chewie, And The Falcon. "
    "Spaceport Scoundrel Guild dested Scoundrel's Guild as written. "
    "Leia's Blaster Rifle dested Leia With Blaster Rifle. "
    "Tunnel Vision dested Tunnel Vision as written. "
    "Antilles Maneuver line 20 True / line 21 empty kept split. "
    "Antilles combo dested Antilles Maneuver & Rebel Reinforcements. "
    "AWRIGDS dested All Wings Report In & Darklighter Spin. "
    "LTWW line 25 True / line 26 empty kept split. "
    "Report dested Report as written. "
    "NQA line 32 True / lines 33-34 empty kept split. "
    "Mace MOTO dested Mace Windu, Master Of The Order. "
    "Luke EP dested Luke Skywalker With Lightsaber as written. "
    "Yoda Great Warrior dested Yoda, Great Warrior. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "Palejie Reshad dested Taletjie Reshad as written. "
    "BoShek dested BoShek, Brash Smuggler. "
    "Seeking An Audience dested Seeking An Audience. "
    "Houjix Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Strike Force dested Strikeforce. "
    "Unique overcounts sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name Tom dested as written. Username blank. LIGHT/DARK empty; dest Dark from AOBS. "
    "AOBS checkbox empty dested Agents Of Black Sun / Vengeance Of The Dark Prince "
    "without True. Dengar crossed, Velken dested Velken Tezeri. "
    "Look Sir Droids dested Look Sir, Droids. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Oh Switch Off dested Oh, Switch Off. "
    "Flagship Bridge dested Blockade Flagship: Bridge. "
    "Slave I Symbol dested Slave I, Symbol Of Fear. "
    "IG-88 with Riot Gun dested IG-88 With Riot Gun. "
    "Kel Hutta dested Nal Hutta. "
    "Control / SFS dested Control & Set For Stun. "
    "Imbalance & Krayt dested Armed And Dangerous & Krayt Dragon Howl. "
    "Unique overcounts sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("It Could Be Worse", True),
    n("Insurrection & Aim High"),
    n("Wokling", True),
    n("Heading For The Medical Frigate"),
    n("Chewie"),
    n("Captain Han Solo"),
    n("Han, Chewie, And The Falcon", True),
    n("Spaceport City"),
    n("Corellia", True),
    n("Scoundrel's Guild"),
    n("Home One: Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Docking Bay"),
    n("Rebel Barrier"),
    n("Corellian Slip", True),
    n("Leia With Blaster Rifle"),
    n("Tunnel Vision", True),
    n("Imperial Atrocity", True),
    n("Antilles Maneuver", True),
    n("Antilles Maneuver"),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win"),
    n("All Wings Report In & Darklighter Spin"),
    n("Report", True),
    n("Report"),
    n("Punch It"),
    n("Tantive IV", True),
    n("No Questions Asked", True),
    n("No Questions Asked", qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Luke Skywalker With Lightsaber"),
    n("Padme Naberrie"),
    n("Yoda, Great Warrior"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Corran Horn"),
    n("Taletjie Reshad"),
    n("BoShek, Brash Smuggler"),
    n("Crix Madine"),
    n("Brokuman"),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Lando Calrissian", True),
    n("Seeking An Audience", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Dash Rendar", True),
    n("Desperate Reach"),
    n("Houjix & Out Of Nowhere"),
    n("Mirax Terrik"),
    n("Leia With Blaster Rifle"),
    n("Rebel Barrier"),
    n("Luke Skywalker With Lightsaber"),
    n("Anger, Fear, Aggression", True),
    n("Strikeforce", True),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Chasm", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not"),
    n("He Can Go About His Business"),
    n("Jabba's Prize"),
    n("Let's Keep A Little Optimism Here", True),
    n("Planetary Defenses", True),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
]
LS_ADD = []


DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Xizor", True),
    n("Coruscant"),
    n("Imperial City"),
    n("Twi'lek Advisor"),
    n("Jabba's Palace: Audience Chamber"),
    n("Scum And Villainy"),
    n("Den Of Thieves"),
    n("Boba Fett, Bounty Hunter"),
    n("Velken Tezeri", True),
    n("Imperial Barrier"),
    n("Zinnht"),
    n("Vigo"),
    n("Sonic Bombardment"),
    n("Lightsaber Deficiency", True),
    n("Mandalorian Armor", True),
    n("Look Sir, Droids"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sonic Bombardment"),
    n("I'm Being Ambushed & Sacrifice"),
    n("Hidden Weapons"),
    n("Scrambled Transmission"),
    n("Ket Maliss", True),
    n("They're Still Coming Through!"),
    n("4-LOM With Concussion Rifle"),
    n("Coruscant: Docking Bay"),
    n("Dengar", True),
    n("Blow Parried"),
    n("Despair"),
    n("Ghhhk"),
    n("Leave Them!"),
    n("Oh, Switch Off"),
    n("Elis Helrot"),
    n("What?"),
    n("Hidden Weapons"),
    n("Despair"),
    n("Spaceport Docking Bay"),
    n("Dr. Evazan"),
    n("Blockade Flagship: Bridge"),
    n("Jabba's Haven", True),
    n("Slave I, Symbol Of Fear"),
    n("Datoo Kart"),
    n("IG-88 With Riot Gun"),
    n("Nal Hutta"),
    n("Boba Fett, Prepared Hunter"),
    n("Lando With Blaster Rifle"),
    n("Ree-Yees", True),
    n("Protocol Failure"),
    n("Vigo"),
    n("Fett's Stun Rifle", True),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Control & Set For Stun"),
    n("Ponda Baba", True),
    n("Datoo Kart"),
    n("Bossk", True),
    n("Cloud City: Security Tower", True),
    n("Dengar With Blaster Carbine"),
    n("Wuntoo"),
    n("Knowledge And Defense", True),
    n("Ghhhk", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Imperial Detention"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Firepower", True),
    n("Secret Plans"),
]
DS_ADD = [
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Abyss"),
]
