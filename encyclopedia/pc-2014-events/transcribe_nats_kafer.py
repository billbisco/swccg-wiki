#!/usr/bin/env python3
"""2014 US Nationals Day 1 notebook lists: Bill Kafer.

Source: Nationals-2014-day-1.pdf pages 11–12 (handwritten notebook, not a 2010 Xerox 60).
Dest as written notebook groups. (V) from a trailing v on the notebook.
"""
from __future__ import annotations

PLAYER = "Bill Kafer"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 US Nationals Day 1.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2014 US Nationals Day 1 p11 Bill Kafer LS.png"
DS_SCAN = "2014 US Nationals Day 1 p12 Bill Kafer DS.png"
NOTE = "Handwritten notebook lists (not a 2010 Xerox 60)."
LS_NOTE = (
    "Notebook heading Bill Kafer - 2014 Nats (LS). Username blank. "
    "TIGIH dested There Is Good In Him / I Can Save Him. "
    "End: CCH dested Endor: Chief Chirpa's Hut. End: DB dested Endor: Landing Platform (Docking Bay). "
    "LSRS dested Luke Skywalker, Rebel Scout. DTDM dested Don't Tread On Me. "
    "AFA dested Anger, Fear, Aggression. Hologameboard dested Dejarik Hologame Board. "
    "C: JCC dested Coruscant: Jedi Council Chamber. N: B Plains dested Naboo: Battle Plains. "
    "N: BNC dested Naboo: Boss Nass' Chambers. Leia RP dested Leia, Rebel Princess. "
    "Anakin dested Anakin Skywalker, Padawan Learner. Mace dested Mace Windu. "
    "Jaina dested Jaina Solo. EPP Qui dested Qui-Gon Jinn With Lightsaber. "
    "EPP Obi dested Obi-Wan With Lightsaber. Padme dested Padme Naberrie. "
    "Lando S dested Lando Calrissian, Scoundrel. Lando UH dested Lando Calrissian, Unlikely Hero. "
    "LSSK dested Luke Skywalker, Jedi Knight. HCF dested Han, Chewie, And The Falcon. "
    "Jedi LS dested Jedi Lightsaber. Ani's LS dested Anakin's Lightsaber. "
    "Projection dested Projection Of A Skywalker. OOV dested Out Of Nowhere. "
    "Atrocity dested Imperial Atrocity. Seeking dested Seeking An Audience. "
    "DTF dested Draw Their Fire. Scramble dested Scrambled Transmission. "
    "Esc Pod dested Escape Pod. WGGA dested Wesa Gotta Grand Army. "
    "LTWW dested Let The Wookiee Win. OOC+TT dested Odin Nesloor & First Aid. "
    "Jedi Lev dested Jedi Levitation. Speak dested Speak With The Jedi Council. "
    "AWR+DS dested All Wings Report In & Darklighter Spin. "
    "SATM+BP dested Sorry About The Mess & Blaster Proficiency. "
    "Clash dested Clash Of Sabers. Resilience dested A Jedi's Resilience. "
    "OJCTW dested Only Jedi Carry That Weapon. DDTA dested Don't Do That Again. "
    "Y Sentry dested Yavin Sentry. Simple Tricks dested Simple Tricks And Nonsense. "
    "Professor dested The Professor. B Plan dested Battle Plan. DoDN dested Do, Or Do Not. "
    "YISYW dested Your Insight Serves You Well. LKALOH dested Let's Keep A Little Optimism Here. "
    "A Mind dested Affect Mind. Planetary Def dested Planetary Defenses. "
    "Unique overcounts sheet-accurate (Anakin Skywalker, Padawan Learner x3, Escape Pod x3, "
    "Wesa Gotta Grand Army x3, Mace Windu x2, Jaina Solo x2, Obi-Wan With Lightsaber x2, "
    "Han, Chewie, And The Falcon x2, Imperial Atrocity x2, Let The Wookiee Win x2, "
    "A Jedi's Resilience x2). (V) from a trailing v."
)
DS_NOTE = (
    "Notebook heading Bill Kafer - 2014 Nats (DS). Username blank. "
    "Hunt Down dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Sith Plans dested A Sith's Plans. Cor: Imp City dested Coruscant: Imperial City. "
    "Prep Def dested Prepared Defenses. GOTM dested Gift Of The Master. "
    "Ni Chu dested Ni Chuba Na??. BF: Bridge dested Blockade Flagship: Bridge. "
    "Imp Holotable dested Imperial Holotable. CC: ST dested Cloud City: Security Tower. "
    "Nab: TPG dested Naboo: Theed Palace Generator. Emp Palp dested Emperor Palpatine. "
    "DV DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Galen SA dested Galen Marek, Starkiller. Grievous dested Grievous, Hunter Of Jedi. "
    "Dengar w/ Gun dested Dengar With Blaster Carbine. Dr E + PB dested Dr. Evazan & Ponda Baba. "
    "Jango, Assassin dested Jango Fett, The Assassin. Keder w/ FP dested Keder The Black. "
    "Dark Jedi LS dested Dark Jedi Lightsaber. Galen Saber VG dested Galen's Lightsaber, Vader's Gift. "
    "Vader's Saber dested Vader's Lightsaber. Trophy of Kill dested Trophy Of A Kill. "
    "Emp New Order dested Empire's New Order. B Rack dested Blaster Rack. "
    "Emp Power dested Emperor's Power. Revenge of Sith dested Revenge Of The Sith. "
    "Imp Prop dested Imperial Propaganda. Image dested Image Of The Dark Lord. "
    "M Move dested Masterful Move. WL+TEB dested Weapon Levitation & The Empire's Back. "
    "ADTFTB dested A Dark Time For The Rebellion. Elis dested Elis Helrot. "
    "WDYTM dested What Do You Think You're Doing?. IHYN dested I Have You Now. "
    "WMAOP dested We Must Accelerate Our Plans. F Field dested Force Field. "
    "F Lightning dested Force Lightning. Sith Fury+ETDC dested Sith Fury & End This Destructive Conflict. "
    "KAD dested Knowledge And Defense. DS Sentry dested Death Star Sentry. "
    "I Find dested I Find Your Lack Of Faith Disturbing. TINT dested There Is No Try. "
    "Detention dested Imperial Detention. Firepower crossed, skipped. "
    "Useless dested A Useless Gesture. DTHACC dested Do They Have A Code Clearance?. "
    "B Order dested Battle Order. CHYBC dested Come Here You Big Coward. "
    "WDGS dested We'll Let Fate-a Decide, Huh?. YCHF dested You Cannot Hide Forever. "
    "Unique overcounts sheet-accurate (Emperor Palpatine x3, Galen Marek, Starkiller x3, "
    "Darth Vader, Dark Lord Of The Sith x2, Grievous, Hunter Of Jedi x2, "
    "Jango Fett, The Assassin x2, Trophy Of A Kill x2, Masterful Move x2, "
    "We Must Accelerate Our Plans x2, Sense x2). (V) from a trailing v. "
    "NO_DEST (2014 index): What Do You Think You're Doing? (V)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("I Feel The Conflict"),
    n("Don't Tread On Me", True),
    n("Anger, Fear, Aggression", True),
    n("Dejarik Hologame Board"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("IL-19"),
    n("Anakin Skywalker, Padawan Learner", qty=3),
    n("Mace Windu", True, qty=2),
    n("Jaina Solo", qty=2),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Padme Naberrie", True),
    n("Lando Calrissian, Scoundrel"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Luke Skywalker, Jedi Knight"),
    n("Lady Luck"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Jedi Lightsaber", True),
    n("Anakin's Lightsaber"),
    n("Projection Of A Skywalker"),
    n("Out Of Nowhere"),
    n("Imperial Atrocity", qty=2),
    n("Seeking An Audience", True),
    n("Draw Their Fire"),
    n("Scrambled Transmission", True),
    n("Escape Pod", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Odin Nesloor & First Aid"),
    n("Jedi Levitation", True),
    n("Houjix"),
    n("Speak With The Jedi Council"),
    n("Nabrun Leids"),
    n("All Wings Report In & Darklighter Spin"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Clash Of Sabers"),
    n("A Jedi's Resilience", qty=2),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Only Jedi Carry That Weapon"),
    n("Chasm", True),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("Planetary Defenses"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("A Sith's Plans"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Prepared Defenses"),
    n("I've Lost Artoo!", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Blockade Flagship: Bridge"),
    n("Imperial Holotable"),
    n("Cloud City: Security Tower", True),
    n("Naboo: Theed Palace Generator"),
    n("Emperor Palpatine", qty=3),
    n("Darth Vader"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Galen Marek, Starkiller", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Jango Fett, The Assassin", qty=2),
    n("Garindan", True),
    n("Keder The Black"),
    n("P-59"),
    n("Dark Jedi Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Trophy Of A Kill", qty=2),
    n("Empire's New Order", True),
    n("No Escape"),
    n("Blaster Rack", True),
    n("Emperor's Power", True),
    n("Revenge Of The Sith"),
    n("Imperial Propaganda", True),
    n("Image Of The Dark Lord", True),
    n("Alter", True),
    n("Masterful Move", qty=2),
    n("Monnok"),
    n("Weapon Levitation & The Empire's Back"),
    n("A Dark Time For The Rebellion", True),
    n("Elis Helrot"),
    n("What Do You Think You're Doing?", True),
    n("I Have You Now"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Sense", True, qty=2),
    n("Force Field", True),
    n("Force Lightning"),
    n("Sith Fury & End This Destructive Conflict"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("Imperial Detention"),
    n("A Useless Gesture", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
