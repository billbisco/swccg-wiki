#!/usr/bin/env python3
"""2013 Alderaan Regionals: Tom handwritten 2010 Xerox LS+DS.

Name field Tom. Username blank. Dest Tom as written (same SoCal Tom).
Do not dest as a new person. Do not rewrite 2013 SoCal Tom leftover.
"""
from __future__ import annotations

PLAYER = "Tom"
USERNAME = ""
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2013 Alderaan Regionals p03 Tom LS.png"
DS_SCAN = "2013 Alderaan Regionals p04 Tom DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). Name Tom dested "
    "as written (same SoCal Tom). Username blank. LIGHT/DARK empty; dest Light from WYS. "
    "WYS True dested Watch Your Step / This Place Can Be A Little Rough True. "
    "Falcon dested Han, Chewie, And The Falcon. Captain Han dested Captain Han Solo. "
    "HFTMF dested Heading For The Medical Frigate. CEC dested Corellian Engineering "
    "Corporation True (WYS Corellia package; HT analog). AFA dested Anger, Fear, Aggression. "
    "Barrier dested Rebel Barrier. H1DB dested Home One: Docking Bay. "
    "Romas dested Romas 'Lock' Navander. LTWW dested Let The Wookiee Win. "
    "Leia RP dested Leia, Rebel Princess. Wedge RSL dested Wedge Antilles, Red Squadron Leader. "
    "Antilles combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Runpe dested Rumor. Palejie Reshad dested Taletjie Reshad as written. "
    "Pun ten tor dested Pucumir Thryss. Ambush dested Ambush as written. "
    "AWRI+DS dested All Wings Report In & Darklighter Spin. LSJK dested "
    "Luke Skywalker, Jedi Knight. Yoda Great Warrior dested Yoda, Great Warrior. "
    "Crowd Control dested Crowd Control. Lando Unlikely Hero dested "
    "Lando Calrissian, Unlikely Hero. Sense of Daughter dested Sergeant Bruckman. "
    "Houjix Out of Nowhere dested Houjix & Out Of Nowhere. Laudica dested Laudica. "
    "Mace Windu MOTO dested Mace Windu, Master Of The Order. "
    "Spaceport Scoundrel Guild dested Spaceport Scoundrels Guild. "
    "Padme dested Padme Naberrie. Leia Blaster Rifle dested Leia With Blaster Rifle. "
    "General Bob Hudsol dested Bob Hudsol. Spaceport DB dested Spaceport Docking Bay. "
    "Imp Atrocity dested Imperial Atrocity. Unique overcounts sheet-accurate "
    "(Don't Do That Again shields x2, Corellian Retort x2, NQA x2, Antilles Maneuver x2, "
    "LSJK x2, Wedge RSL x2, Leia RP x2, AFA x2, AWRI+DS x2, Antilles combo x2, LTWW True/empty). "
    "(V) from the checkbox; dittos inherit the first named line except where the "
    "ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). Name Tom dested "
    "as written (same SoCal Tom). Username blank. LIGHT/DARK empty; dest Dark from AOBS. "
    "AOBS empty dested Agents Of Black Sun / Vengeance Of The Dark Prince without True. "
    "Info Exchange dested Information Exchange. Boba BH dested Boba Fett, Bounty Hunter. "
    "Woof dested Wooof. Zinnht dested Zinnht. Lightsaber Deficiency dested Lightsaber Deficiency. "
    "Look Sir Droids dested Look Sir, Droids. Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "I'm Being Ambushed & Sacrifice dested I'm Being Ambushed & Sacrifice. "
    "Unexpected Interruption dested Unexpected Interruption as written. "
    "Ket Maliss dested Ket Maliss. They're Still Coming Through dested They're Still Coming Through!. "
    "4-LOM with rifle dested 4-LOM With Concussion Rifle. Coruscant DB dested Coruscant: Docking Bay. "
    "Oh Switch Off dested Oh, Switch Off. Elis Helrot dested Elis Helrot. "
    "Blockade Bridge dested Blockade Flagship: Bridge. Slave I Symbol dested Slave I, Symbol Of Fear. "
    "Tato Kart dested Datoo Kart. IG-88 with Riot Gun dested IG-88 With Riot Gun. "
    "Kel Hutta dested Nal Hutta. Boba Fett Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Lando with Blaster Rifle dested Lando With Blaster Rifle. Fett's Stun Rifle dested Fett's Stun Rifle. "
    "Imbalance & Krayt dested Armed And Dangerous & Krayt Dragon Howl. "
    "Control & SFS dested Control & Set For Stun. Security Tower dested Cloud City: Security Tower. "
    "Dengar with Blaster Rifle dested Dengar With Blaster Carbine. Wuntoo dested Wuntoo. "
    "Knowledge & Defense dested Knowledge And Defense. Garden dested Ghhhk. "
    "Coward dested Come Here You Big Coward. Code Clearance dested Do They Have A Code Clearance?. "
    "YCHF dested You Cannot Hide Forever. We'll Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Imperial Detention dested Imperial Detention. TINT dested There Is No Try. "
    "Secret Plans dested Secret Plans. Unique overcounts sheet-accurate "
    "(Sonic Bombardment x2, Hidden Weapons x2, Despair x2, Vigo x2, Datoo Kart x2, Ghhhk x2). "
    "(V) from the checkbox; dittos inherit the first named line except where the "
    "ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia"),
    n("Spaceport City"),
    n("Han, Chewie, And The Falcon", True),
    n("Captain Han Solo"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("Anger, Fear, Aggression", True),
    n("Rebel Barrier"),
    n("Home One: Docking Bay"),
    n("Romas 'Lock' Navander"),
    n("Let The Wookiee Win", True),
    n("Leia, Rebel Princess"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Antilles Maneuver", True),
    n("Rumor"),
    n("Luke Skywalker, Jedi Knight"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Taletjie Reshad"),
    n("Corran Horn"),
    n("Pucumir Thryss", True),
    n("Ambush", True),
    n("Corellian Retort", True),
    n("Spaceport Street"),
    n("No Questions Asked", True),
    n("Corellian Retort", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Luke Skywalker, Jedi Knight"),
    n("Yoda, Great Warrior"),
    n("Seeking An Audience", True),
    n("Sabotage", True),
    n("Crowd Control", True),
    n("Let The Wookiee Win"),
    n("Sense"),
    n("General Crix Madine"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Sergeant Bruckman"),
    n("Houjix & Out Of Nowhere"),
    n("Laudica", True),
    n("Mace Windu, Master Of The Order"),
    n("Mirax Terrik"),
    n("Antilles Maneuver", True),
    n("No Questions Asked", True),
    n("Tantive IV", True),
    n("Spaceport Scoundrels Guild", True),
    n("Padme Naberrie", True),
    n("Leia With Blaster Rifle"),
    n("Desperate Reach", True),
    n("Lady Luck"),
    n("Bob Hudsol"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Leia, Rebel Princess"),
    n("Chewie", True),
    n("Spaceport Docking Bay"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("All Wings Report In & Darklighter Spin"),
    n("Imperial Atrocity", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("He Can Go About His Business", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("Planetary Defenses", True),
    n("Ultimatum", True),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("The Professor", True),
    n("Chasm", True),
]
LS_ADD = [
    n("A Tragedy Has Occurred"),
    n("Jabba's Prize"),
    n("Do, Or Do Not"),
]


DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Xizor", True),
    n("Coruscant"),
    n("Imperial City"),
    n("Twi'lek Advisor", True),
    n("Information Exchange", True),
    n("Scum And Villainy"),
    n("Den Of Thieves", True),
    n("Boba Fett, Bounty Hunter"),
    n("Wooof", True),
    n("Imperial Barrier"),
    n("Zinnht"),
    n("Vigo", True),
    n("Sonic Bombardment", True),
    n("Lightsaber Deficiency", True),
    n("Mandalorian Armor", True),
    n("Look Sir, Droids"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sonic Bombardment", True),
    n("I'm Being Ambushed & Sacrifice"),
    n("Hidden Weapons"),
    n("Unexpected Interruption"),
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
    n("Abyss", True),
]
