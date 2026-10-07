#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Unknown Player.

Source: 2012NationalsDay1.pdf pages 86–87 (handwritten notebook dump).
p86 Dark Hunt Down / p87 Light YCPBT. Name blank Username blank both.
Facing pair sandwich Hayes Hunter p84–p85 then last pages of Day 1 PDF.
Dest Unknown Player analog leftover 2012 MPC transcribe_2012_mpc_unknown.py.
Pack player-stubs/Unknown_Player.wiki. Index Unknown players.
Do not dest as a new named person. Do not dest as Hayes Hunter.
"""
from __future__ import annotations

PLAYER = "Unknown Player"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 87
DS_PAGE = 86
LS_SCAN = "2012 US Nationals Day 1 Unknown Player LS.png"
DS_SCAN = "2012 US Nationals Day 1 Unknown Player DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten notebook dump. Name blank Username blank both. "
    "I wrote this at Nationals. Dest Unknown Player analog leftover 2012 MPC. "
    "Index Unknown players. Do not dest as a new named person. Do not dest as Hayes Hunter."
)
PUBLIC_NOTE = "Name blank on the Day 1 sheet."
LS_NOTE = (
    "Handwritten notebook. Name blank Username blank. I wrote this at Nationals. "
    "Dest Unknown Player analog leftover 2012 MPC. Index Unknown players. "
    "Starting wrote Agents in the court / No love Lo du empire dested from filled Light 60s: "
    "You Can Either Profit By This... / Or Be Destroyed analog leftover Brady. "
    "Uh-on (v) dested Uh-Oh! True analog leftover. "
    "Hedins For Medical Frigate dested Heading For The Medical Frigate analog leftover tom_h. "
    "Yarna d'al' Gargan (v) dested analog leftover True. "
    "Ellorrs Madak dested analog leftover. "
    "Anger Fear Aggression (v) dested Anger, Fear, Aggression True analog leftover McCune IN THE 60. "
    "Dashed Battle Plan / Wise Advice / Weapons Display / A Tragedy Has Occurred / Yavin Sentry dested shields True. "
    "Tatooine Hutt trade route dested Tatooine: Hutt Trade Route analog leftover. "
    "Jabbas Palace Audience chamber dested Jabba's Palace: Audience Chamber analog leftover. "
    "Senator Padme Amidala (v) dested Senator Padmé Amidala True analog leftover. "
    "Bou gun dested Boushh analog leftover Nelson. "
    "Nbb nulo dested Nibb Nulo analog leftover x2. "
    "Arcona / Kitonak dested analog leftover unique overcount. "
    "Droopy McCool dested analog leftover. "
    "Yoda, great warrior (v) dested Yoda, Great Warrior True analog leftover Stenerson. "
    "Leia Organa dested Princess Leia analog leftover Olson. "
    "Tamtel Skreej (v) dested analog leftover True. "
    "Master luke dested dest-as-written slang. "
    "Obi-wan, crazy wizard (v) dested Obi-Wan Kenobi, Crazy Old Wizard True analog leftover. "
    "luke with lightsaber dested Luke Skywalker With Lightsaber analog leftover. "
    "Joh Yowza dested analog leftover. "
    "wookie dested Chewbacca analog leftover. "
    "Qui-Gon w/ lightsaber dested Qui-Gon Jinn With Lightsaber analog leftover Tenneson. "
    "Jass dested dest-as-written slang. "
    "Ral'Falnl C'ndros dested Kal'Falnl C'ndros analog leftover. "
    "Skiff dested Desert Skiff analog leftover x4. "
    "Projection of a skywalker dested Projection Of A Skywalker analog leftover McCune. "
    "underworld contacts dested analog leftover. "
    "Jabbas palace entrance cavern dested Jabba's Palace: Entrance Cavern analog leftover. "
    "Tatooine Toshe station dested Tatooine: Tosche Station analog leftover. "
    "Tatooine Jundland wastes dested Tatooine: Jundland Wastes analog leftover. "
    "Houjix dested analog leftover x2. "
    "Nebrun Leids dested Nabrun Leids analog leftover x2. "
    "Nar shaddaa wind chimes + out of somewhere dested Nar Shaddaa Wind Chimes & Out Of Somewhere analog leftover Cooleo. "
    "You will take me to Jabba now dested You Will Take Me To Jabba Now analog leftover x3. "
    "Smoke Screen dested analog leftover. Unique sheet-accurate. Shields 5."
)
DS_NOTE = (
    "Handwritten notebook. Name blank Username blank. Hunt down and Eat the Jedi. "
    "Dest Unknown Player analog leftover 2012 MPC. Index Unknown players. "
    "Start Huntdown and destroy the Jedi / the Fire has gone out of the universe dested "
    "Hunt Down And Destroy The Jedi / The Fire Has Gone Out Of The Universe analog leftover Simmering. "
    "A siths plans (v) dested A Sith's Plans True analog leftover Shaw. "
    "Gift of the master (v) dested Gift Of The Master analog leftover Alperstein. "
    "Visage of the emperor dested Visage Of The Emperor analog leftover Hunt Down unique overcount in Effects. "
    "Executor holotheatre dested Executor: Holotheatre analog leftover. "
    "Executor meditation chamber dested Executor: Meditation Chamber analog leftover. "
    "Prepares defences dested Prepared Defenses analog leftover. "
    "The emperor (v) dested Emperor Palpatine True analog leftover. "
    "Darth maul dested Darth Maul With Lightsaber analog leftover Finley x2. "
    "Lord Maul dested dest-as-written slang. "
    "Dr. Evazan + Ponda Baba dested Dr. Evazan & Ponda Baba analog leftover Gemme. "
    "Mara Jade with lightsaber dested Mara Jade With Lightsaber analog leftover Stenerson. "
    "Galen, Secret Apprentice dested analog leftover Anderson x2. "
    "Darth vader with lightsaber dested Darth Vader With Lightsaber analog leftover x3. "
    "Darth vader dark lord of the Sith dested Darth Vader, Dark Lord Of The Sith analog leftover Alperstein. "
    "Cyborg commander, hunter of Jedi (v) dested Grievous, Hunter Of Jedi True analog leftover Morgan. "
    "The empires back dested The Empire's Back analog leftover dest-as-written x3. "
    "Sniper + dark strike dested Sniper & Dark Strike analog leftover Stenerson. "
    "Why didn't you tell me? (V) dested Why Didn't You Tell Me? True analog leftover Schoenthal x2. "
    "Shhhk dested Ghhhk analog leftover Stenerson. "
    "Elis helrot dested Elis Helrot analog leftover. "
    "Sith fury (v) dested Sith Fury True analog leftover x3. "
    "Masterful move dested Masterful Move analog leftover Veasey. "
    "lightsaber deficiency dested Lightsaber Deficiency analog leftover Brady. "
    "stunning leader dested Stunning Leader analog leftover Jespar x2. "
    "set for stun dested Set For Stun analog leftover Amato. "
    "presence of the force dested Presence Of The Force analog leftover Haglund. "
    "blaster rack dested Blaster Rack analog leftover. "
    "Dr Evazans sawed off blaster dested Dr. Evazan's Sawed-Off Blaster analog leftover. "
    "mauls double bladed lightsaber dested Darth Maul's Double-Bladed Lightsaber analog leftover. "
    "sidious lightsaber (v) dested Sidious' Lightsaber True analog leftover. "
    "cyborg commanders lightsabers (v) dested Grievous' Lightsabers True analog leftover Morgan. "
    "mauls sith infiltrator dested Maul's Sith Infiltrator analog leftover Anderson. "
    "Tatooine wattos junkyard dested Tatooine: Watto's Junkyard analog leftover. "
    "Hoth wampa cave dested Hoth: Wampa Cave analog leftover. "
    "Tatooine mos espa dested Tatooine: Mos Espa analog leftover. "
    "mos eisly dested Tatooine: Mos Eisley analog leftover. Unique sheet-accurate. Shields none."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Uh-Oh!", True),
    n("Heading For The Medical Frigate"),
    n("Yarna d'al' Gargan", True),
    n("Ellorrs Madak"),
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Hutt Trade Route"),
    n("Jabba's Palace: Audience Chamber"),
    n("Tessek"),
    n("Senator Padmé Amidala", True),
    n("Boushh"),
    n("Nibb Nulo", qty=2),
    n("Arcona", qty=3),
    n("Kitonak", qty=3),
    n("Droopy McCool"),
    n("Yoda, Great Warrior", True),
    n("Princess Leia"),
    n("Oola"),
    n("Tamtel Skreej", True),
    n("Master Luke"),
    n("Obi-Wan Kenobi, Crazy Old Wizard", True),
    n("Luke Skywalker With Lightsaber"),
    n("Joh Yowza"),
    n("Chewbacca"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Jass"),
    n("Max Rebo"),
    n("Kal'Falnl C'ndros"),
    n("Desert Skiff", qty=4),
    n("Projection Of A Skywalker"),
    n("Underworld Contacts"),
    n("Bargaining Table"),
    n("Bo Shuda"),
    n("Jabba's Palace: Entrance Cavern"),
    n("Tatooine: Tosche Station"),
    n("Tatooine: Jundland Wastes"),
    n("Houjix", qty=2),
    n("Nabrun Leids", qty=2),
    n("Nar Shaddaa Wind Chimes & Out Of Somewhere"),
    n("You Will Take Me To Jabba Now", qty=3),
    n("Smoke Screen"),
]
LS_SHIELDS = [
    n("Battle Plan", True),
    n("Wise Advice", True),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred", True),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / The Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / The Fire Has Gone Out Of The Universe"),
    n("A Sith's Plans", True),
    n("Gift Of The Master"),
    n("Visage Of The Emperor"),
    n("Executor: Holotheatre"),
    n("Executor: Meditation Chamber"),
    n("The Phantom Menace"),
    n("Prepared Defenses"),
    n("Emperor Palpatine", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Lord Maul"),
    n("Dr. Evazan & Ponda Baba"),
    n("Mara Jade With Lightsaber"),
    n("Galen, Secret Apprentice", qty=2),
    n("Darth Vader With Lightsaber", qty=3),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Grievous, Hunter Of Jedi", True),
    n("The Empire's Back", qty=3),
    n("Sniper & Dark Strike"),
    n("Why Didn't You Tell Me?", True, qty=2),
    n("Limited Resources"),
    n("Ghhhk"),
    n("Imperial Barrier", qty=2),
    n("Elis Helrot"),
    n("Force Field"),
    n("Sith Fury", True, qty=3),
    n("Masterful Move"),
    n("Lightsaber Deficiency"),
    n("Stunning Leader", qty=2),
    n("Set For Stun"),
    n("Presence Of The Force"),
    n("Blaster Rack"),
    n("Imperial Justice"),
    n("Search And Destroy"),
    n("Visage Of The Emperor"),
    n("No Escape"),
    n("Dr. Evazan's Sawed-Off Blaster"),
    n("Darth Maul's Double-Bladed Lightsaber"),
    n("Vader's Lightsaber"),
    n("Sidious' Lightsaber", True),
    n("Grievous' Lightsabers", True),
    n("Maul's Sith Infiltrator"),
    n("Tatooine: Watto's Junkyard"),
    n("Hoth: Wampa Cave"),
    n("Tatooine: Mos Espa"),
    n("Tatooine: Mos Eisley"),
]
DS_SHIELDS = []
DS_ADD = []
