#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Mauer Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Mauer"
LS_USERNAME = "Mauer"
DS_USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 101
DS_PAGE = 102
LS_SCAN = "2013 Match Play Championship p101 Mauer LS.png"
DS_SCAN = "2013 Match Play Championship p102 Mauer DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username Mauer (Name blank). Light unchecked. "
    "Deck title Senate. Starting Tatooine: Slave Quarters + Communing. "
    "Slave Quarters dested Tatooine: Slave Quarters. Inc Barriers dested Inconsequential Barriers. "
    "Jedi Lev dested Jedi Levitation. A SR dested A Jedi's Resilience. "
    "Run Luke dested Run Luke, Run!. Antilles Maneuvers / RR dested Antilles Maneuver & Rebel Reinforcements. "
    "Line 17 Don't Get Cocky / Lucky Shot struck dested Don't Get Cocky & Lucky Shot. "
    "OOC / TT dested Out Of Commission & Transmission Terminated. LTWW dested Let The Wookiee Win. "
    "A SN as written. Cantina dested Tatooine: Cantina. Obi hut dested Tatooine: Obi-Wan's Hut. "
    "H 1 WR dested Home One: War Room. EPP Han dested Han With Heavy Blaster Pistol. "
    "Yoda, Greatest Master dested Yoda, Great Warrior. Leia RP dested Leia, Rebel Princess. "
    "Chewie's Bowcaster dested Chewbacca's Bowcaster. Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "A CS dested Alderaan Consular Ship. Chewie Protector dested Chewbacca, Protector. "
    "Chewie Enraged dested Chewie, Enraged. "
    "Form left column reprints 37–38 on lines 39–40 are Admiral Ackbar and Corran Horn. "
    "T WHPS dested Threepio With His Parts Showing. SMN dested Shmi Skywalker. "
    "EPP Luke dested Luke With Lightsaber. Atrocity dested Imperial Atrocity. "
    "C training / Slug dested Commando Training & K'lor'slug. Gun runner dested Rebel Gunrunner. "
    "Draw Fire dested Draw Their Fire. Seeking dested Seeking An Audience. Core dested Corellia. "
    "Projection dested Projection Of A Skywalker. "
    "Line 55 Don't Get Cocky / Lucky Shot struck dested Don't Get Cocky & Lucky Shot. "
    "Senate Appropriation as written. AFA dested Anger, Fear, Aggression. "
    "YISYW dested Your Insight Serves You Well. DDTA dested Don't Do That Again. "
    "Simple Tricks dested Simple Tricks And Nonsense. Planetary Defense dested Planetary Defenses. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Mauer (Username blank). Dark unchecked. "
    "Deck title Invasion dested Invasion (not Invasion / In Complete Control). "
    "Starting A Stunning Move (not A Stunning Move / A Valuable Hostage). "
    "A SM dested A Stunning Move. Fallen Lord dested Coruscant: Palpatine's Quarters. "
    "Private Platform dested Coruscant: Private Platform (Docking Bay). "
    "Prison dested Insidious Prisoner. Prep D dested Prepared Defenses. "
    "Ni Chuba Na dested Ni Chuba Na??. Jabba Haven dested Jabba's Haven. "
    "Gift of Master dested Gift Of The Master. Jabba's Hut dested Tatooine: Jabba's Palace. "
    "BF Hallway / Bridge / DB dested Blockade Flagship sites. "
    "CC Prison dested Cloud City: Security Tower. "
    "Jabba's Palace Audience dested Jabba's Palace: Audience Chamber. "
    "JP Dungeon dested Jabba's Palace: Dungeon. Cyborg Lightsaber dested Grievous' Lightsabers. "
    "WMAOP dested We Must Accelerate Our Plans. Sniper / DS dested Sniper & Dark Strike. "
    "Control / SFS dested Control & Set For Stun. They Still Coming Through dested They're Still Coming Through!. "
    "Weapon Lev dested Weapon Levitation. Sonic dested Sonic Bombardment. "
    "Ability x3 dested Ability, Ability, Ability. TPM dested The Phantom Menace. "
    "Galen dested Galen Marek, Starkiller. "
    "Form left column reprints 37–38 on lines 39–40 are Battle Droid Squad. "
    "Line 41 prior title struck dested Elis Helrot. IG Bodyguard Droid dested IG-100 MagnaGuard. "
    "Dengar w/ Blaster dested Dengar With Blaster Carbine. Mando Fett dested Jango Fett, The Assassin. "
    "Dr E & PB dested Dr. Evazan & Ponda Baba. Boba Fett PH dested Boba Fett, Prepared Hunter. "
    "DM YA dested Darth Maul, Young Apprentice. Cyborg Commander dested General Grievous. "
    "4-LOM w/ Rifle dested 4-LOM With Concussion Rifle. Slave I Symbol dested Slave I, Symbol Of Fear. "
    "K+D dested Knowledge And Defense. "
    "We'll Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "A Useless Gesture dested A Useless Gesture. YCHF dested You Cannot Hide Forever. "
    "DS Sentry dested Death Star Sentry. Do They Clearance dested Do They Have A Code Clearance?. "
    "Line 12 Secret Plans struck dested I Find Your Lack Of Faith Disturbing. "
    "Garrison as written. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Houjix", qty=2),
    n("Escape Pod", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Use The Force", True, qty=2),
    n("Inconsequential Barriers"),
    n("Jedi Levitation", True),
    n("A Jedi's Resilience"),
    n("Run Luke, Run!", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Don't Get Cocky & Lucky Shot", True, qty=2),
    n("Grimtaash"),
    n("Out Of Commission & Transmission Terminated"),
    n("Let The Wookiee Win", True, qty=2),
    n("A SN"),
    n("Tatooine: Cantina"),
    n("Tatooine"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Home One: War Room"),
    n("Wedge Antilles", True),
    n("Han With Heavy Blaster Pistol"),
    n("Yoda, Great Warrior"),
    n("Leia, Rebel Princess"),
    n("Chewbacca's Bowcaster"),
    n("Home One"),
    n("Tantive IV", True),
    n("Artoo-Detoo In Red 5"),
    n("Alderaan Consular Ship"),
    n("Chewbacca, Protector"),
    n("Chewie, Enraged", True, qty=2),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Threepio With His Parts Showing"),
    n("Shmi Skywalker"),
    n("Luke With Lightsaber", qty=3),
    n("Imperial Atrocity", True, qty=2),
    n("Commando Training & K'lor'slug"),
    n("Wokling", True),
    n("Rebel Gunrunner"),
    n("Draw Their Fire"),
    n("Seeking An Audience", True),
    n("Corellia"),
    n("Projection Of A Skywalker"),
    n("Master Kenobi"),
    n("Communing"),
    n("Scrambled Transmission", True),
    n("Senate Appropriation"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("He Can Go About His Business"),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Planetary Defenses"),
]
LS_ADD = []

DS_START = "A Stunning Move"
DS_CARDS = [
    n("A Stunning Move"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Tatooine: Jabba's Palace"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Docking Bay"),
    n("Cloud City: Security Tower"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Dungeon"),
    n("Grievous' Lightsabers"),
    n("We Must Accelerate Our Plans"),
    n("Sniper & Dark Strike"),
    n("Control & Set For Stun"),
    n("Ghhhk"),
    n("Sith Fury", True, qty=2),
    n("Force Field", True, qty=2),
    n("Stunning Leader"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("They're Still Coming Through!"),
    n("Weapon Levitation"),
    n("Sonic Bombardment", True, qty=2),
    n("Blaster Rack", True),
    n("Ability, Ability, Ability", True),
    n("No Escape"),
    n("The Phantom Menace", qty=2),
    n("Galen Marek, Starkiller", qty=2),
    n("Battle Droid Squad", qty=2),
    n("Elis Helrot"),
    n("IG-100 MagnaGuard"),
    n("Dengar With Blaster Carbine", True),
    n("Jango Fett, The Assassin"),
    n("Dr. Evazan & Ponda Baba"),
    n("Boba Fett, Prepared Hunter"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("General Grievous", qty=2),
    n("P-59"),
    n("4-LOM With Concussion Rifle", True),
    n("Probe Droid", True),
    n("Guri", True),
    n("Garrison", True),
    n("Victory"),
    n("Blockade Support Ship"),
    n("Slave I, Symbol Of Fear"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Death Star Sentry", True),
    n("Battle Order"),
    n("Fanfare"),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?"),
    n("Secret Plans"),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
