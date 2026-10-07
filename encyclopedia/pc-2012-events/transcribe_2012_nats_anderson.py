#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: John Anderson.

Source: 2012NationalsDay1.pdf pages 1–2 (2010 Xerox, 12 shields).
Name John Anderson dested John Anderson. Username Puck71.
p01 Dark A Stunning Move. p02 Light Yavin 4: Massassi Throne Room.
Do not dest as a new person. Do not rewrite 2012 MPC leftover Communing / A Stunning Move
or 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "John Anderson"
USERNAME = "Puck71"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 2
DS_PAGE = 1
LS_SCAN = "2012 US Nationals Day 1 John Anderson LS.png"
DS_SCAN = "2012 US Nationals Day 1 John Anderson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
DS_NOTE = (
    "Handwritten 2010 Xerox. Name John Anderson dested John Anderson. Username Puck71. "
    "DARK checked. Event Date 6/9/12 Event Name Nats 2012. "
    "A Stunning Move empty dested A Stunning Move / A Valuable Hostage. "
    "Cor: Private Platform dested Coruscant: Private Platform. "
    "Cor: Palp's Quarters dested Coruscant: Palpatine's Quarters. "
    "Ni Chuba Na dested Ni Chuba Na?? True. "
    "Phantom Menace dested The Phantom Menace. "
    "Galen dested Galen, Secret Apprentice as written. "
    "Cyborg's Saber dested Grievous' Lightsabers. "
    "MM + EO dested Masterful Move & Endor Occupation. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi. "
    "IG Body Guard Droid dested IG-100 MagnaGuard. "
    "Short Range Fighters + Watch Yer Back dested Short Range Fighters & Watch Your Back!. "
    "Boba Fett Prepared Hunter dested Boba Fett, Bounty Hunter. "
    "Probot dested Probot. "
    "You Cannot Hide Forever dested You Cannot Hide Forever in the 60. "
    "Maul's Double Bladed Saber dested Maul's Double-Bladed Lightsaber. "
    "Dr. E + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Maul Young Apprentice dested Darth Maul, Young Apprentice. "
    "Galen's Saber Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Dark Time dested A Dark Time For The Rebellion True. "
    "Sniper + DS dested Sniper & Dark Strike. "
    "Mandalorian Father of Fett dested Jango Fett, The Assassin. "
    "B.F. Hallway dested Blockade Flagship: Hallway. "
    "Slave I Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Why Didn't You Tell Me? dested Why Didn't You Tell Me? True. "
    "Knowledge + Defense dested Knowledge And Defense True in the 60. "
    "Shield Coward dested Come Here You Big Coward. "
    "Code Clearance dested Do They Have A Code Clearance? True. "
    "Unique overcounts sheet-accurate (Galen, Secret Apprentice x3, Darth Maul x2, "
    "Masterful Move & Endor Occupation x2, Grievous, Hunter Of Jedi x2, Control x2, "
    "IG-100 MagnaGuard x2, Darth Maul, Young Apprentice x2, A Dark Time For The Rebellion True x2, "
    "Battle Droid Squad x2, Force Field True x2). (V) from checkbox."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name John Anderson dested John Anderson. Username Puck71. "
    "LIGHT checked. Event Date 6/9/12 Event Name Nats 2012. "
    "Y4: Throne Room dested Yavin 4: Massassi Throne Room (starting location, no Objective). "
    "HFTMF dested Heading For The Medical Frigate. "
    "Adm Ackbar dested Admiral Ackbar True. "
    "Speak w/ Jedi Council dested Speak With The Jedi Council. "
    "Coruscant: JCC dested Coruscant: Jedi Council Chamber True. "
    "Obi Wan's Journal dested Obi-Wan's Journal. "
    "Luke's Saber dested Luke's Lightsaber. "
    "Jedi Saber dested Jedi Lightsaber True. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel. "
    "Leia RP dested Leia, Rebel Princess. "
    "Qui-Gon w/ Saber dested Qui-Gon Jinn With Lightsaber. "
    "Yoda MOTF dested Yoda, Master Of The Force. "
    "Obi w/ Saber dested Obi-Wan With Lightsaber. "
    "Naboo: TP Generator Core dested Naboo: Theed Palace Generator Core. "
    "Sai'torr dested Sai'torr Kal Fas True. "
    "IL-10 dested I'll Take The Odds. "
    "Wesa Gots a Grand Army dested Wesa Gots A Grand Army. "
    "Han Chewie Falcon dested Han, Chewie, And The Falcon. "
    "SATM + BP dested Sorry About The Mess & Blaster Proficiency. "
    "Luke SITF dested Luke Skywalker, Strong In The Force. "
    "Luke Jedi Knight dested Luke Skywalker, Jedi Knight. "
    "Resilience dested A Jedi's Resilience. "
    "Armed + Dangerous + Krayt Dragon Howl dested Armed And Dangerous & Krayt Dragon Howl. "
    "AFA dested Anger, Fear, Aggression True IN THE 60. "
    "Shield Ultimatum dested Ultimatum True. "
    "Shield Only Jedi Carry That Weapon dested Only Jedi Carry That Weapon. "
    "Shield Chasm dested Chasm True. "
    "Shield Yavin Sentry dested Yavin Sentry True. "
    "Unique overcounts sheet-accurate (Speak With The Jedi Council x2, "
    "Qui-Gon Jinn With Lightsaber x2, Smoke Screen x3, Clash Of Sabers x2, "
    "Rebel Leadership True x3, Mace Windu True x2, Wesa Gots A Grand Army x2, "
    "Luke Skywalker, Strong In The Force x2, Lando Calrissian, Scoundrel x2, "
    "Blaster Deflection x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Yavin 4: Massassi Throne Room"
LS_CARDS = [
    n("Yavin 4: Massassi Throne Room"),
    n("Heading For The Medical Frigate"),
    n("Wokling"),
    n("Quick Draw", True),
    n("Rycar Ryjerd"),
    n("Hindsight", True),
    n("Kiffex"),
    n("Home One"),
    n("Admiral Ackbar", True),
    n("Speak With The Jedi Council", qty=2),
    n("Coruscant: Jedi Council Chamber", True),
    n("Tantive IV", True),
    n("Obi-Wan's Journal"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Menace Fades"),
    n("Luke's Bionic Hand"),
    n("Lando Calrissian, Scoundrel"),
    n("Leia, Rebel Princess"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Yoda, Master Of The Force"),
    n("Smoke Screen", qty=3),
    n("Obi-Wan With Lightsaber"),
    n("Clash Of Sabers", qty=2),
    n("Draw Their Fire"),
    n("Naboo: Theed Palace Generator Core"),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Rebel Leadership", True, qty=3),
    n("Mace Windu", True, qty=2),
    n("Let The Wookiee Win", True),
    n("I'll Take The Odds"),
    n("Wesa Gots A Grand Army", qty=2),
    n("Naboo: Boss Nass' Chambers"),
    n("Han, Chewie, And The Falcon"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Corran Horn"),
    n("Alter", True),
    n("Blaster Deflection", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Home One: War Room"),
    n("Sense"),
    n("A Jedi's Resilience"),
    n("A Jedi's Plans"),
    n("Scrambled Transmission", True),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Battle Plan", True),
    n("Ultimatum", True),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Only Jedi Carry That Weapon"),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here"),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Private Platform"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Ni Chuba Na??", True),
    n("A Sith's Weapon"),
    n("The Phantom Menace"),
    n("Darth Maul", qty=2),
    n("Blockade Flagship: Bridge"),
    n("Ghhhk"),
    n("Galen, Secret Apprentice", qty=3),
    n("Blaster Rack", True),
    n("Grievous' Lightsabers"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Maul's Sith Infiltrator"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Search And Destroy"),
    n("Blockade Flagship: Docking Bay"),
    n("Control", qty=2),
    n("IG-100 MagnaGuard", qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Boba Fett, Bounty Hunter"),
    n("Probot"),
    n("Sonic Bombardment", True),
    n("Trophy Of A Kill"),
    n("You Cannot Hide Forever"),
    n("No Escape"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Nal Hutta"),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Darth Maul, Young Apprentice", qty=2),
    n("You Are Beaten"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Sniper & Dark Strike"),
    n("Abyssin Ornament", True),
    n("Battle Droid Squad", qty=2),
    n("Force Field", True, qty=2),
    n("Jango Fett, The Assassin"),
    n("Blockade Flagship: Hallway"),
    n("Slave I, Symbol Of Fear"),
    n("OOM-9", True),
    n("Why Didn't You Tell Me?", True),
    n("Sense"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Secret Plans"),
    n("Firepower", True),
    n("You Cannot Hide Forever"),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Leave Them To Me"),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = []
