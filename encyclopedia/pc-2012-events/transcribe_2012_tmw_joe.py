#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Charley Joe.

Source: 2012TMWDay1.pdf pages 30–31 (2009 Print Form). Name Charley Joe dested
Charley Joe analog leftover encyclopedia / generate_*.py / player-stubs EMPTY.
Username Wburg dested USERNAME="Wburg". Email CJSandburg@... dested identity
evidence only. Do not dest as Charley Hickey (2024 ROCS is a different person).
Do not dest as a new last-name Sandburg. Pack player-stubs/Charley_Joe.wiki.
p30 Dark Court. p31 Light Profit. Dest independently of Amar Banger Court/Profit
THIS event.
"""
from __future__ import annotations

PLAYER = "Charley Joe"
USERNAME = "Wburg"
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 31
DS_PAGE = 30
LS_SCAN = "2012 Texas Mini Worlds Day 1 Charley Joe LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Charley Joe DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "2009 Print Form p30 Dark / p31 Light. "
    "Name Charley Joe dested Charley Joe analog leftover empty. "
    "Username Wburg. Email CJSandburg@... dested identity evidence only. "
    "Do not dest as Charley Hickey. Do not dest as a new last-name Sandburg. "
    "Pack player-stubs/Charley_Joe.wiki."
)
LS_NOTE = (
    "2009 Print Form p31 Light Deck Name Profit. LIGHT checked. Event Date 04/28/12. "
    "Name Chodyer Joe dested Charley Joe analog leftover p30 filled Name. Username dashed dested Wburg. "
    "Profit / or Be Destroyed dested You Can Either Profit By This analog leftover Banger dual-title. "
    "Han dested Han analog leftover Banger. "
    "HFTMF dested Heading For The Medical Frigate analog leftover. "
    "Padme dested Padme Naberrie analog leftover 2014 MPC. "
    "Kashyyyk Insurgent Leader dested analog leftover Veasey. "
    "Luke SITF dested Luke Skywalker, Strong In The Force analog leftover. "
    "Chewie Enraged dested Chewie, Enraged analog leftover Hendon. "
    "Chewbacca Bowcaster dested Chewbacca's Bowcaster analog leftover. "
    "Leia, Rebel Princess dested analog leftover 2013 TMW Skilton. "
    "Luke, JK dested Luke Skywalker, Jedi Knight analog leftover Skilton. "
    "Jet Utility Belt dested Tatooine Utility Belt analog leftover Pietruszewski. "
    "Lando in Ace dested Lando In Millennium Falcon analog leftover Ojala. "
    "Tat: Lars Moisture Farm dested Tatooine: Lars' Moisture Farm analog leftover Jellison. "
    "Commando Training / K'lor'slug dested Commando Training & K'lor'slug analog leftover. "
    "Jedi Lev dested Jedi Levitation analog leftover. "
    "crossed dest replacement Lando w/ Vibro dested Lando With Vibro-Ax analog leftover. "
    "Naked Threepio dested Threepio With His Parts Showing analog leftover Banger. "
    "Han's Heavy Blaster dested Han's Heavy Blaster Pistol analog leftover. "
    "Naboo Landing dested Naboo: Theed Palace Docking Bay analog leftover Stirling. "
    "Obi-Wan Saber dested Obi-Wan's Lightsaber analog leftover Banger. "
    "Anger Fear Aggression dested Anger, Fear, Aggression analog leftover Anderson IN THE 60. "
    "Left extra 37–40 dest all written lines unique 60. Right printed 41–60. "
    "Unique 60. Shields 11 shield 12 blank skip."
)
DS_NOTE = (
    "2009 Print Form p30 Dark Deck Name Court. DARK checked. Event Date 04/28/12 Event Houston. "
    "Name Charley Joe dested Charley Joe analog leftover empty. Username Wburg. "
    "Court of the Vile Gangster dested Court Of The Vile Gangster analog leftover Banger dual-title. "
    "Mara Jade w/ Lightsaber dested Mara Jade With Lightsaber analog leftover. "
    "Poteet dested Pote Snitkin analog leftover Pietruszewski. "
    "Shoova dested Snoova analog leftover Pietruszewski. "
    "Bare Mallar dested Barne Malar analog leftover Pietruszewski. "
    "Fett in Slave I dested Boba Fett In Slave I analog leftover MPC Anderson. "
    "ZIMH dested Zuckuss In Mist Hunter analog leftover MPC Anderson. "
    "Gela Veosa dested Gela Yeosa analog leftover Grouty. "
    "Thok + Thug dested Thok & Thug analog leftover Pietruszewski. "
    "Abyssin Ornament + Wound dested Abyssin Ornament & Wounded Wookiee analog leftover Huderich. "
    "4-LOM w/ Concussion Rifle dested 4-LOM With Concussion Rifle analog leftover Erwin. "
    "Dengar w/ Blaster Carbine dested Dengar With Blaster Carbine analog leftover. "
    "Ghhhk & Those Rebels Won't Escape Us dested analog leftover srodoski. "
    "Ni Chuba Na?? dested analog leftover. "
    "MM&EO dested Masterful Move & Endor Occupation analog leftover. "
    "Knowledge And Defense True dested analog leftover Anderson IN THE 60. "
    "Fire Power dested Firepower analog leftover Gardner. "
    "Left extra 37–40 dest all written lines unique 60. Right printed 41–60. "
    "Unique 60. Shields 10 shields 11–12 blank skip."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This"
LS_CARDS = [
    n("You Can Either Profit By This"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han", True),
    n("Heading For The Medical Frigate"),
    n("Quick Draw", True),
    n("I Must Be Allowed To Speak", True),
    n("Seeking An Audience", True),
    n("Skiff", qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Padme Naberrie", True, qty=2),
    n("Kashyyyk Insurgent Leader", True),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Porkins Scanner"),
    n("Luke's Lightsaber"),
    n("Master Luke", True),
    n("Palowick Barter"),
    n("Sergeant Doallyn", True),
    n("Assassin Guns", True, qty=2),
    n("Someone Who Loves You", qty=2),
    n("Chewie, Enraged", True),
    n("Chewbacca's Bowcaster"),
    n("Leia, Rebel Princess", qty=2),
    n("Anakin's Lightsaber", True),
    n("Harvest", True, qty=2),
    n("On The Edge"),
    n("Let The Wookiee Win", True, qty=2),
    n("Sai'torr Kal Fas", True),
    n("Tatooine Utility Belt", True, qty=2),
    n("Away Put Your Weapon", True),
    n("Lando In Millennium Falcon"),
    n("Luke Skywalker, Jedi Knight", True),
    n("Jedi Lightsaber", True),
    n("Lightsaber Pike"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Anger, Fear, Aggression", True),
    n("Commando Training & K'lor'slug", True),
    n("Civil Disorder", True),
    n("Raddle's Blaster"),
    n("Jedi Levitation", True),
    n("Lando With Vibro-Ax", True),
    n("Don't Tread On Me", True),
    n("Jedi Prisoner"),
    n("Restraining Belt"),
    n("Han's Heavy Blaster Pistol", True),
    n("Threepio With His Parts Showing"),
    n("Ounee Ta"),
    n("Vibro-Ax"),
    n("Naboo: Theed Palace Docking Bay"),
    n("Obi-Wan's Lightsaber"),
]
LS_SHIELDS = [
    n("Let's Keep It Between Us", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again"),
    n("Do Or Do Not"),
    n("Ounee Ta", True),
    n("Your Insight Serves You Well"),
]
LS_ADD = []

DS_START = "Court Of The Vile Gangster"
DS_CARDS = [
    n("Court Of The Vile Gangster"),
    n("Mara Jade With Lightsaber"),
    n("Bossk In Hound's Tooth", True),
    n("Cease Fire!", qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Protocol Failure", True),
    n("T'Quille", True),
    n("4-LOM With Concussion Rifle"),
    n("Dengar With Blaster Carbine", True),
    n("Pote Snitkin", True),
    n("Ephant Mon"),
    n("P-59"),
    n("Cold Feet", True),
    n("Ponda Baba", True),
    n("Look Sir, Droids"),
    n("Grotto Werribee", True),
    n("Boelo"),
    n("Snoova"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Elis Helrot", qty=2),
    n("Jabba's Space Cruiser", True),
    n("Barne Malar", True),
    n("Boba Fett In Slave I", True, qty=2),
    n("Vibro-Ax", qty=2),
    n("R2-A5", True),
    n("Operational As Planned", True),
    n("First Strike"),
    n("Nal Hutta"),
    n("Dengar In Punishing One"),
    n("Death Star II: Docking Bay"),
    n("Executor: Docking Bay"),
    n("Stunning Leader"),
    n("Zuckuss In Mist Hunter"),
    n("Ni Chuba Na??", True),
    n("Jodo Kast", True),
    n("Lightsaber Proficiency", True, qty=2),
    n("Prince Xizor"),
    n("Jabba's Sail Barge", True),
    n("Thok & Thug", True),
    n("Masterful Move & Endor Occupation"),
    n("Aurra Sing"),
    n("Gela Yeosa", True),
    n("Jabba The Hutt", True),
    n("Abyssin Ornament & Wounded Wookiee", True),
    n("Hutt Bounty", True),
    n("Sarlacc"),
    n("Jabba's Palace: Audience Chamber"),
    n("Scum And Villainy"),
    n("Tatooine: Great Pit Of Carkoon"),
    n("Jabba's Palace: Dungeon"),
    n("Power Of The Hutt"),
    n("Desilijic Tattoo", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward", True),
    n("Allegations Of Corruption", True),
    n("Oppressive Enforcement", True),
    n("Imperial Detention", True),
    n("Firepower", True),
    n("Abyss", True),
    n("Resistance", True),
]
DS_ADD = []
