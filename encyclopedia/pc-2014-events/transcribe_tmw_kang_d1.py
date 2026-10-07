#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: 康威廉.

Source: 2014-TMW-Day-1.pdf pages 23–24 (2010 form).
Name 康威廉 dested as written (Pinyin William Kang; no wiki stub).
"""
from __future__ import annotations

PLAYER = "康威廉"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 23
DS_PAGE = 24
LS_SCAN = "2014 Texas Mini Worlds Day 1 p23 康威廉 LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p24 康威廉 DS.png"
NOTE = "Handwritten 2010 Xerox Print Form (12 shields + Additional). Name dested as written."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name 康威廉 dested as written. Username blank. LIGHT/DARK both empty; cards are Light. "
    "Event TMW. Deck Name Chinese characters dested as written. "
    "TIGIH dested There Is Good In Him / I Can Save Him. "
    "AFA dested Anger, Fear, Aggression. "
    "DTOM dested Don't Tread On Me. "
    "E: DB dested Endor: Landing Platform (Docking Bay). "
    "E: CCH dested Endor: Chief Chirpa's Hut. "
    "Luke RS dested Luke Skywalker, Rebel Scout. "
    "Luke's Saber dested Luke's Lightsaber. "
    "IFTC dested I Feel The Conflict. "
    "Projection dested Projection Of A Skywalker. "
    "Leia RP dested Leia, Rebel Princess. "
    "Jedi LS dested Jedi Lightsaber. "
    "Corran dested Corran Horn. "
    "LTWW dested Let The Wookiee Win. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader. "
    "Leadership dested Rebel Leadership. "
    "Esc Pod dested Escape Pod. "
    "WGGA dested Wesa Gotta Grand Army. "
    "Y4: MWR dested Yavin 4: Massassi War Room. "
    "HCF dested Han, Chewie, And The Falcon. "
    "Anakin PL dested Anakin Skywalker, Padawan Learner. "
    "Jedi Lev dested Jedi Levitation. "
    "Weapon Lev dested Weapon Levitation. "
    "Anakin's Saber dested Anakin's Lightsaber. "
    "Jaima Solo dested Jaina Solo. "
    "DTF dested Draw Their Fire. "
    "N: BNC dested Naboo: Boss Nass' Chambers. "
    "Atrocity dested Imperial Atrocity. "
    "Lando UH dested Lando Calrissian, Unlikely Hero. "
    "EPP Obi dested Obi-Wan With Lightsaber. "
    "Padme dested Padmé Naberrie. "
    "Cor: JCC dested Coruscant: Jedi Council Chamber. "
    "SATM + BP dested Sorry About The Mess & Blaster Proficiency. "
    "A Jedi Resil dested A Jedi's Resilience. "
    "Speak w/ JC dested Speak With The Jedi Council. "
    "EPP Qui dested Qui-Gon Jinn With Lightsaber. "
    "Lando Scound dested Lando Calrissian, Scoundrel. "
    "Nabrun dested Nabrun Leids. "
    "N: BP dested Naboo: Battle Plains. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "Seeking dested Seeking An Audience. "
    "Clash dested Clash Of Sabers. "
    "Tragedy dested A Tragedy Has Occurred. "
    "Only Jedi dested Only Jedi Carry That Weapon. "
    "DDTA dested Don't Do That Again. "
    "Y Sentry dested Yavin Sentry. "
    "Simple Tricks dested Simple Tricks And Nonsense. "
    "Professor dested The Professor. "
    "B Plan dested Battle Plan. "
    "DODN dested Do, Or Do Not. "
    "YISYN dested Your Insight Serves You Well. "
    "LKAOH dested Let's Keep A Little Optimism Here. "
    "Unique overcounts sheet-accurate (Wesa Gotta Grand Army x3, Escape Pod x2, "
    "Han, Chewie, And The Falcon x2, Let The Wookiee Win x2, Imperial Atrocity x2, "
    "Anakin Skywalker, Padawan Learner x2, Mace Windu x3, Qui-Gon Jinn With Lightsaber x2, "
    "Rebel Leadership x2, Jaina Solo x2, A Jedi's Resilience x2). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name 康威廉 dested as written. Username blank. DARK checked. Event TMW. "
    "Deck Name Chinese characters dested as written. "
    "Kessel dested Kessel. "
    "Kessel: SM AO dested Kessel: Spice Mines - Administrator's Office. "
    "Ni Chu dested Ni Chuba Na?. "
    "NO_DEST remaining: Imperial Holotable, Propaganda (lookup miss on (V) path), "
    "S + DS dested Superlaser Mark II. "
    "GOTM dested Gift Of The Master. "
    "ITTM dested I'll Take Them Myself. "
    "Know And Defend dested Knowledge And Defense. "
    "CC: Sec Tower dested Cloud City: Security Tower. "
    "Kessel: SM EF dested Kessel: Spice Mines - Extraction Facility. "
    "Kessel: SM P dested Kessel: Spice Mines - Prison. "
    "Imp Holotable dested Imperial Holotable. "
    "Mun Kyneugh dested Mun Kyneugh. "
    "Dengar w/ Gun dested Dengar With Blaster Carbine. "
    "Keder dested Keder The Black. "
    "Mara w/ Saber dested Mara Jade With Lightsaber. "
    "GM Tarkin dested Grand Moff Tarkin. "
    "Django Fett The Assassin dested Jango Fett, The Assassin. "
    "Boba Fett, Prep Hunter dested Boba Fett, Prepared Hunter. "
    "Galen dested Galen Marek, Starkiller. "
    "Dooku dested Count Dooku. "
    "Dudlots dested Destroyer Droid. "
    "Janus dested Janus Greejatus. "
    "Emp Palp dested Emperor Palpatine. "
    "Blizz 4 dested Blizzard 4. "
    "Slave I SOF dested Slave I, Symbol Of Fear. "
    "Vader Saber dested Vader's Lightsaber. "
    "Galen Saber, VG dested Galen's Lightsaber, Vader's Gift. "
    "Dooku Saber dested Dooku's Lightsaber. "
    "Kessel Surv System (NASA) dested Kessel Surveillance System. "
    "B Rack dested Blaster Rack. "
    "Emp Power dested Emperor's Power. "
    "Image dested Image Of The Dark Lord. "
    "ROTS dested Revenge Of The Sith. "
    "S + DS dested Superlaser Mark II. "
    "YAB dested You Are Beaten. "
    "ADTFTR dested A Dark Time For The Rebellion. "
    "F Lightning dested Force Lightning. "
    "F Push dested Force Push. "
    "F Field dested Force Field. "
    "M Move dested Masterful Move. "
    "M Move + EO dested Masterful Move & Endor Occupation. "
    "Sonic Bomb dested Sonic Bombardment. "
    "Weap Lev dested Weapon Levitation. "
    "DS Sentry dested Death Star Sentry. "
    "YCHF dested You Cannot Hide Forever. "
    "Weap Of Sith dested Weapon Of A Sith. "
    "Allegations dested Allegations Of Corruption. "
    "CHYBC dested Come Here You Big Coward. "
    "Useless dested A Useless Gesture. "
    "B Order dested Battle Order. "
    "DTHACC dested Do They Have A Code Clearance?. "
    "Detention dested Imperial Detention. "
    "Opp Enforce dested Oppressive Enforcement. "
    "Resist dested Resistance. "
    "Sec Plans dested Secret Plans. "
    "Unique overcounts sheet-accurate (Galen Marek, Starkiller x2, Count Dooku x2, "
    "Destroyer Droid x3, Emperor Palpatine x3, Force Lightning x2, Masterful Move x2, "
    "Sonic Bombardment x3). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Anger, Fear, Aggression", True),
    n("Don't Tread On Me", True),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Chief Chirpa's Hut"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("I Feel The Conflict"),
    n("Projection Of A Skywalker"),
    n("Leia, Rebel Princess"),
    n("Jedi Lightsaber", True),
    n("Corran Horn"),
    n("Let The Wookiee Win", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Rebel Leadership", True),
    n("Lady Luck"),
    n("Escape Pod", True),
    n("Wesa Gotta Grand Army"),
    n("Yavin 4: Massassi War Room", True),
    n("Wesa Gotta Grand Army"),
    n("Han, Chewie, And The Falcon"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Jedi Levitation", True),
    n("Weapon Levitation"),
    n("Han, Chewie, And The Falcon"),
    n("Mace Windu", True),
    n("Wesa Gotta Grand Army"),
    n("Anakin's Lightsaber"),
    n("Let The Wookiee Win", True),
    n("Jaina Solo"),
    n("Draw Their Fire"),
    n("Naboo: Boss Nass' Chambers"),
    n("Imperial Atrocity", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Obi-Wan With Lightsaber"),
    n("Padmé Naberrie", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Escape Pod", True),
    n("Obi-Wan Kenobi", True),
    n("Quick Draw", True),
    n("Imperial Atrocity", True),
    n("Houjix"),
    n("Jaina Solo"),
    n("A Jedi's Resilience"),
    n("Speak With The Jedi Council"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Lando Calrissian, Scoundrel"),
    n("Mace Windu", True),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Nabrun Leids"),
    n("Rebel Leadership", True),
    n("Naboo: Battle Plains"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Under Attack"),
    n("Mace Windu", True),
    n("Luke Skywalker, Jedi Knight"),
    n("A Jedi's Resilience"),
    n("Seeking An Audience", True),
    n("Clash Of Sabers"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Only Jedi Carry That Weapon"),
    n("Chasm"),
    n("Aim High"),
    n("Don't Do That Again"),
    n("Yavin Sentry"),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Battle Plan"),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("Ultimatum"),
]
LS_ADD = [
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here"),
    n("Affect Mind", True),
]


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Ni Chuba Na?", True),
    n("Gift Of The Master"),
    n("I'll Take Them Myself"),
    n("Knowledge And Defense", True),
    n("Cloud City: Security Tower", True),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Kessel: Spice Mines - Prison"),
    n("Imperial Holotable"),
    n("Spice Mine Operations"),
    n("Mun Kyneugh", True),
    n("Garindan", True),
    n("Dengar With Blaster Carbine", True),
    n("Keder The Black"),
    n("Mara Jade With Lightsaber"),
    n("Grand Moff Tarkin", True),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Galen Marek, Starkiller", qty=2),
    n("Count Dooku", qty=2),
    n("Destroyer Droid", qty=3),
    n("Janus Greejatus"),
    n("Emperor Palpatine", qty=3),
    n("Blizzard 4"),
    n("Slave I, Symbol Of Fear"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Dooku's Lightsaber"),
    n("Kessel Surveillance System"),
    n("Blaster Rack", True),
    n("Emperor's Power", True),
    n("Image Of The Dark Lord", True),
    n("Revenge Of The Sith"),
    n("Propaganda", True),
    n("Alter (Coruscant)", True),
    n("Superlaser Mark II"),
    n("You Are Beaten"),
    n("A Dark Time For The Rebellion", True),
    n("Force Lightning", qty=2),
    n("Force Push", True),
    n("Force Field", True),
    n("Sith Fury", True),
    n("Monnok"),
    n("Ghhhk"),
    n("Masterful Move", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Sonic Bombardment", True, qty=3),
    n("Weapon Levitation"),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Abyss"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower"),
    n("Fanfare", True),
    n("Imperial Detention"),
]
DS_ADD = [
    n("Oppressive Enforcement"),
    n("Resistance", True),
    n("Secret Plans"),
]
