#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Hayes Hunter.

Source: 2012NationalsDay1.pdf pages 84–85 (handwritten notebook dump).
p84 Dark Kessel / p85 Light FPP. Name-box black square “…unter” dested Hayes Hunter
analog leftover 2012 MPC transcribe_2012_mpc_hunter.py / player-stubs/Hayes_Hunter.wiki /
generate_2012_nats CANON / file_player Hunter→Hayes Hunter.
Username blank analog leftover 2012 MPC. Pack player-stubs/Hayes_Hunter.wiki.
Do not dest as Eric Hunter. Do not dest as Brian Hunter. Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Hayes Hunter"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 85
DS_PAGE = 84
LS_SCAN = "2012 US Nationals Day 1 Hayes Hunter LS.png"
DS_SCAN = "2012 US Nationals Day 1 Hayes Hunter DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten notebook dump. Name-box black square …unter dested Hayes Hunter analog leftover "
    "2012 MPC / player-stubs/Hayes_Hunter.wiki. Username blank. Do not dest as Eric Hunter. "
    "Do not dest as Brian Hunter. Do not dest as a new person."
)
LS_NOTE = (
    "Handwritten notebook. Name-box …unter dested Hayes Hunter analog leftover 2012 MPC identified stub. "
    "Username blank. Light. Do not dest as Eric Hunter. Do not dest as Brian Hunter. "
    "FPP obi dested Fear, Piety, And Passion LS_START + Master Kenobi analog leftover Stenerson. "
    "Anigon dested Qui-Gon Jinn With Lightsaber analog leftover Tenneson EPP Qui Gon. "
    "Angry Lando dested Lando Calrissian, Scoundrel analog leftover Stenerson. "
    "Jedi LS dested Jedi Lightsaber x2. Luke's LS dested Luke's Lightsaber. "
    "Leia's gun dested Leia's Blaster Rifle analog leftover. "
    "H1 dested Home One. HCF dested Han, Chewie, And The Falcon analog leftover McCune. "
    "R2 in R5 dested Artoo-Detoo In Red 5 analog leftover Bordier. "
    "Atrocity dested Imperial Atrocity analog leftover McCune IN THE 60. "
    "Throne Room dested Yavin 4: Massassi Throne Room analog leftover Anderson. "
    "HFTMF dested Heading For The Medical Frigate analog leftover tom_h. "
    "QD dested dest-as-written slang. "
    "Ins+AH dested I Hope She's Alright analog leftover Stenerson. "
    "H1:DB dested Home One: Docking Bay. H1 war room dested Home One: War Room analog leftover Anderson. "
    "Hoth war room dested Hoth: Echo Command Center (War Room) analog leftover Booker. "
    "ECC dested Echo Base Operations analog leftover Haglund. "
    "Night club dested Coruscant: Night Club analog leftover Bollentino. "
    "Mace dested Mace Windu, Master Of The Order analog leftover Reisch x2. "
    "3PO dested Threepio With His Parts Showing analog leftover Olson. "
    "Yoda Mofo dested Yoda, Great Warrior analog leftover Stenerson x2. "
    "Padme dested Padmé Naberrie analog leftover Schoenthal. "
    "Ackbar (v) dested Admiral Ackbar True analog leftover Stenerson. "
    "Luke sith dested Luke Skywalker, Rebel Hero analog leftover Stenerson x2. "
    "Jedi luke dested Luke Skywalker, Jedi Knight analog leftover Jake Nelson. "
    "Leia RP dested Leia, Rebel Princess analog leftover Anderson. "
    "Leia dested Princess Leia analog leftover Olson. "
    "AFA dested Anger, Fear, Aggression analog leftover McCune IN THE 60. "
    "Sai'tor dested Sai'torr Kal Fas analog leftover Olson Virtual Block. "
    "Scrambled dested Scrambled Transmission analog leftover Shaw. "
    "Seeking dested Seeking An Audience analog leftover 2012 MPC Hunter. "
    "Evac. Cont dested Evacuation Control analog leftover Alex W. "
    "Hear me baby dested Hear Me Baby, Hold Together analog leftover. "
    "Jedi plan dested Jedi Presence analog leftover TMW Shannon. "
    "Sense combo dested Sense & Uncertain Is The Future analog leftover. "
    "desperate reach dested The Bith Shuffle & Desperate Reach analog leftover Nelson. "
    "Blaster def dested Blaster Deflection analog leftover Anis x2. "
    "mess combo dested Sorry About The Mess & Blaster Proficiency analog leftover x2. "
    "speak dested I Must Be Allowed To Speak analog leftover Olson x2. "
    "AJR dested All Wings Report In & Darklighter Spin analog leftover Haglund x2. "
    "LTWW dested Let The Wookiee Win analog leftover Brady x2. "
    "RL dested Rebel Leadership analog leftover Stenerson x2. "
    "KL XC dested X-wing Laser Cannon analog leftover Casey. "
    "Shield Grabber dested A Tragedy Has Occurred analog leftover. "
    "Shield only Jedi dested Only Jedi Carry That Weapon analog leftover Burgt/Bordier. "
    "Shield chasm (v) dested Chasm True analog leftover McCune. "
    "No (V) boxes on most lines. Unique 63 sheet-accurate analog leftover Haglund. Shields 11."
)
DS_NOTE = (
    "Handwritten notebook. Name-box …unter dested Hayes Hunter analog leftover 2012 MPC identified stub. "
    "Username blank. Dark Kessel. Do not dest as Eric Hunter. Do not dest as Brian Hunter. "
    "Kessel dested Kessel / Spice Mines Of Kessel analog leftover Finley. "
    "spice mine: Admin office dested Kessel: Spice Mines - Administrator's Office analog leftover Finley. "
    "CR(v) dested Combat Readiness True analog leftover Herold. "
    "Chu (v) dested dest-as-written slang True. "
    "I'll take them myself dested I'll Take Them Myself analog leftover Finley. "
    "# Gift (v) dested Gift Of The Master analog leftover Alperstein. "
    "Bridge dested dest-as-written slang. "
    "spice mine prison dested Kessel: Spice Mines - Prison analog leftover Finley. "
    "extraction dested Kessel: Spice Mines - Extraction Facility analog leftover Finley. "
    "Spice mine ops dested Spice Mine Operations analog leftover Finley. "
    "surve.. system dested Kessel Surveillance System analog leftover Finley. "
    "Avica dested Arica analog leftover. "
    "Dvd lots dested Darth Vader, Dark Lord Of The Sith analog leftover Alperstein x2. "
    "Darth maul dested Darth Maul With Lightsaber analog leftover Finley. "
    "Emp maul dested Darth Maul, Young Apprentice analog leftover Anderson x2. "
    "Gemme dested Grotto Werribee analog leftover Stenerson/Pinto. "
    "Spice mine admin dested Spice Mine Administrator analog leftover Finley x2. "
    "Galen dested Galen, Secret Apprentice analog leftover Anderson x2. "
    "Darth Sid dested Darth Sidious analog leftover Finley x2. "
    "Emp 4-lom (v) dested 4-LOM With Concussion Rifle True analog leftover Stenerson. "
    "p-59 dested P-59 analog leftover Frafjord. "
    "Sidious' saber dested Sidious' Lightsaber dest-as-written slang. "
    "Galen's saber dested Galen's Lightsaber, Vader's Gift analog leftover 2014 Worlds. "
    "Vader's saber dested Vader's Lightsaber analog leftover. "
    "Victory (v) dested Victory True analog leftover McCune. "
    "Conquest (v) dested Conquest True analog leftover. "
    "Maul's ship dested Maul's Sith Infiltrator analog leftover Anderson x2. "
    "Slave 1 (v) dested Slave I True analog leftover. "
    "Boba, preped dested Boba Fett, Renowned Bounty Hunter analog leftover Ojala. "
    "Father of Fett dested Jango Fett, The Assassin analog leftover Shannon. "
    "Phantom menace dested The Phantom Menace analog leftover Sokol x2. "
    "Sniper combo dested Sniper & Dark Strike analog leftover Stenerson. "
    "Elis dested Elis Helrot analog leftover. "
    "Close call (v) dested Close Call True analog leftover Stenerson. "
    "accelerate dested We Must Accelerate Our Plans analog leftover Alperstein x2. "
    "MM+EO dested Masterful Move & Endor Occupation analog leftover Veasey. "
    "protocol failure dested Protocol Failure analog leftover Anis. "
    "Imba dested Imbalance analog leftover. "
    "Blast door C dested Blast Door Controls analog leftover. "
    "YAB dested You Are Beaten analog leftover Stenerson. "
    "I. Justice dested Imperial Justice analog leftover. "
    "SSPFT dested Something Special Planned For Them analog leftover Fernando. "
    "K+D dested Knowledge And Defense analog leftover McCune IN THE 60. "
    "Shield Weapon of a sith dested Weapon Of A Sith analog leftover. "
    "Shield Grabber dested Oppressive Enforcement analog leftover Finley. "
    "Shield Coward dested Come Here You Big Coward analog leftover. "
    "Shield YCNHF dested You Cannot Hide Forever analog leftover. "
    "Shield Cod. clear dested Do They Have A Code Clearance? analog leftover. "
    "Shield AUG dested A Useless Gesture analog leftover. "
    "Shield Fire power dested Firepower analog leftover Finley. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Fear, Piety, And Passion"
LS_CARDS = [
    n("Fear, Piety, And Passion"),
    n("Master Kenobi"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Lando Calrissian, Scoundrel"),
    n("Jedi Lightsaber", qty=2),
    n("Luke's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Spiral"),
    n("Home One"),
    n("Han, Chewie, And The Falcon"),
    n("Artoo-Detoo In Red 5"),
    n("Imperial Atrocity"),
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("QD"),
    n("I Hope She's Alright"),
    n("Wokling"),
    n("Home One: Docking Bay"),
    n("Home One: War Room"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Echo Base Operations"),
    n("Kessel"),
    n("Coruscant: Night Club"),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Threepio With His Parts Showing"),
    n("Yoda, Great Warrior", qty=2),
    n("Padmé Naberrie"),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Luke Skywalker, Rebel Hero", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Leia, Rebel Princess"),
    n("Princess Leia"),
    n("Anger, Fear, Aggression"),
    n("Affect Mind"),
    n("Sai'torr Kal Fas"),
    n("Hindsight"),
    n("Scrambled Transmission"),
    n("Seeking An Audience"),
    n("Strike Force"),
    n("Evacuation Control"),
    n("Houjix"),
    n("Hear Me Baby, Hold Together"),
    n("Jedi Presence"),
    n("Sense & Uncertain Is The Future"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Blaster Deflection", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("I Must Be Allowed To Speak", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Let The Wookiee Win", qty=2),
    n("Rebel Leadership", qty=2),
    n("X-wing Laser Cannon"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Only Jedi Carry That Weapon"),
    n("Ultimatum"),
    n("Chasm", True),
    n("Another Pathetic Lifeform"),
    n("Your Insight Serves You Well"),
    n("Let's Keep A Little Optimism Here"),
    n("Don't Do That Again"),
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "Kessel / Spice Mines Of Kessel"
DS_CARDS = [
    n("Kessel / Spice Mines Of Kessel"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Combat Readiness", True),
    n("Chu", True),
    n("I'll Take Them Myself"),
    n("Gift Of The Master"),
    n("Bridge"),
    n("Kessel: Spice Mines - Prison"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Spice Mine Operations"),
    n("Kessel Surveillance System"),
    n("Arica"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Maul With Lightsaber"),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Grotto Werribee"),
    n("Spice Mine Administrator", qty=2),
    n("Galen, Secret Apprentice", qty=2),
    n("Garindan"),
    n("Darth Sidious", qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Grand Admiral Thrawn"),
    n("P-59"),
    n("Sidious' Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Victory", True),
    n("Conquest", True),
    n("Maul's Sith Infiltrator", qty=2),
    n("Slave I", True),
    n("Boba Fett, Renowned Bounty Hunter"),
    n("Jango Fett, The Assassin"),
    n("Cold Feet"),
    n("The Phantom Menace", qty=2),
    n("Sniper & Dark Strike"),
    n("Elis Helrot"),
    n("Close Call", True),
    n("Monnok"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Force Field", qty=2),
    n("Ghhhk"),
    n("Protocol Failure"),
    n("Imbalance"),
    n("Blast Door Controls"),
    n("Force Push"),
    n("You Are Beaten"),
    n("Imperial Justice"),
    n("Blaster Rack"),
    n("Something Special Planned For Them"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Secret Plans"),
    n("Battle Order"),
    n("Abyss"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Fanfare"),
    n("You Cannot Hide Forever"),
    n("Do They Have A Code Clearance?"),
    n("A Useless Gesture"),
    n("Firepower"),
]
DS_ADD = []
