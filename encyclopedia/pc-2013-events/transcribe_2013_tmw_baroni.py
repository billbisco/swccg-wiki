#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Steve Baroni Xerox Hunt Down / TIGIH."""
from __future__ import annotations

PLAYER = "Steve Baroni"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 15
DS_PAGE = 14
LS_SCAN = "2013 Texas Mini Worlds Day 1 p15 Steve Baroni LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p14 Steve Baroni DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Baroni dested Steve Baroni. "
    "Username blank. Deck Name Are You?. LIGHT/DARK boxes empty. "
    "Do not rewrite the 2013 MPC or Worlds Steve Baroni leftovers. "
    "TIGIH dested There Is Good In Him / I Can Save Him. "
    "JCC dested Coruscant: Jedi Council Chamber. "
    "Luke Rebel Scout dested Luke Skywalker, Rebel Scout. "
    "Scrambled Transmission crossed, Iico Rammur dested Iico Rammur as written. "
    "HCF dested Han, Chewie, And The Falcon. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel. "
    "Luke SK dested Luke Skywalker, Jedi Knight. "
    "Yoda MOF dested Yoda, Master Of The Force. "
    "Qui Gons Lightsaber dested Qui-Gon Jinn's Lightsaber. "
    "EPP Obi dested Obi-Wan With Lightsaber. "
    "Mace Master of Order dested Mace Windu, Master Of The Order. "
    "Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Naboo BP dested Naboo: Battle Plains. "
    "Sai'torr dested Sai'torr Kal Fas. "
    "Atrocity dested Imperial Atrocity. "
    "Speak dested Speak With The Jedi Council. "
    "LTWW dested Let The Wookiee Win. "
    "AJR dested A Jedi's Resilience. "
    "SATM BP dested Sorry About The Mess & Blaster Proficiency. "
    "Hidden dested Heading For The Medical Frigate. "
    "DTF dested Draw Their Fire. "
    "Leia RP dested Leia, Rebel Princess. "
    "AFA dested Anger, Fear, Aggression. "
    "Insight dested Your Insight Serves You Well. "
    "Keep a little optimism dested Let's Keep A Little Optimism Here. "
    "He Can Go About Business (V) struck dested He Can Go About His Business. "
    "Tragedy Has Occurred dested A Tragedy Has Occurred. "
    "Your Insight crossed on Additional, Only Jedi Carry dested Only Jedi Carry That Weapon. "
    "Form left column reprints 37-38 on lines 39-40 are Wesa Gotta Grand Army "
    "and Speak With The Jedi Council. "
    "Unique overcounts sheet-accurate: Sense x3, Master Qui-Gon x2, "
    "Han, Chewie, And The Falcon x2, Lando Calrissian, Scoundrel x2, "
    "Mace Windu x2, Wesa Gotta Grand Army x3, Let The Wookiee Win x3, "
    "A Jedi's Resilience x2, Escape Pod x2, Rebel Leadership x3. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Baroni dested Steve Baroni. "
    "Username blank. Deck Name MIKE likes. LIGHT/DARK boxes empty. "
    "Do not rewrite the 2013 MPC or Worlds Steve Baroni leftovers. "
    "HD dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Super DS dested Superlaser Mark II. "
    "Ability 3 dested Ability, Ability, Ability. "
    "Cold Pact dested Cold Feet. "
    "MM EO dested Masterful Move & Endor Occupation. "
    "Force Pork dested Force Push. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "Galens Saber dested Galen's Lightsaber, Vader's Gift. "
    "3rd Marker dested Hoth: Defensive Perimeter (3rd Marker). "
    "Coruscant SE dested Coruscant. Imp City dested Coruscant: Imperial City. "
    "Galen's Fighter dested Rogue Shadow. "
    "GMT dested Grand Moff Tarkin. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Dr E Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Dengar W Blaster dested Dengar With Blaster Carbine. "
    "Mara W Light dested Mara Jade With Lightsaber. "
    "Boba Fett BH dested Boba Fett, Bounty Hunter. "
    "DuDlots dested Droideka. "
    "Darth Vader Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Galen dested Galen, Secret Apprentice as written. "
    "Prep Defenses dested Prepared Defenses. "
    "They're Still dested They're Still Coming Through!. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "Gift of Master dested Gift Of The Master. "
    "K&D dested Knowledge And Defense. "
    "Weapon Lev / Emp Back dested Weapon Levitation & The Empire's Back. "
    "Imperial Barriers dested Imperial Barrier. "
    "POTF dested Presence Of The Force. "
    "Compassion & Concession dested Compassion & Concession as written. "
    "YCHFF dested You Cannot Hide Forever. "
    "Coward dested Come Here You Big Coward. "
    "Useless Gesture dested A Useless Gesture. "
    "Allegations dested Allegations Of Corruption. "
    "Weapon of Sith dested Weapon Of A Sith. "
    "We'll Let Fate dested We'll Let Fate-A Decide, Huh?. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "Leave them to me dested Leave Them To Me. "
    "I Find Your Lack dested I Find Your Lack Of Faith Disturbing. "
    "Form left column reprints 37-38 on lines 39-40 are Mara Jade With Lightsaber "
    "and Boba Fett, Bounty Hunter. "
    "Unique overcounts sheet-accurate: Force Field x2, We Must Accelerate Our Plans x3, "
    "Blizzard 4 x2, Boba Fett, Bounty Hunter x2, Emperor Palpatine x3, "
    "Droideka x2, Galen, Secret Apprentice x3. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Seeking An Audience", True),
    n("Sense", qty=3),
    n("I Feel The Conflict"),
    n("Impressive, Most Impressive", True),
    n("Endor: Chief Chirpa's Hut"),
    n("Master Qui-Gon", True, qty=2),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Luke Skywalker, Rebel Scout", True),
    n("Iico Rammur", True),
    n("Home One"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Yoda, Master Of The Force"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Obi-Wan With Lightsaber"),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Wokling", True),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Imperial Atrocity", True),
    n("Wesa Gotta Grand Army", qty=3),
    n("Speak With The Jedi Council"),
    n("Let The Wookiee Win", qty=3),
    n("A Jedi's Resilience", qty=2),
    n("Blaster Deflection"),
    n("Houjix"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Heading For The Medical Frigate"),
    n("Weapon Levitation"),
    n("Draw Their Fire"),
    n("Escape Pod", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Home One: War Room"),
    n("Leia, Rebel Princess"),
    n("Projection Of A Skywalker"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business"),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
]
LS_ADD = [
    n("Yavin Sentry", True),
    n("Affect Mind", True),
    n("Only Jedi Carry That Weapon"),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Superlaser Mark II"),
    n("Ability, Ability, Ability"),
    n("Cold Feet", True),
    n("No Escape"),
    n("Force Lightning"),
    n("Revenge Of The Sith", True),
    n("One Beautiful Thing", True),
    n("Lightsaber Deficiency", True),
    n("Protocol Failure", True),
    n("Ghhhk"),
    n("Masterful Move & Endor Occupation"),
    n("Force Field", True, qty=2),
    n("Force Push", True),
    n("Emperor's Power", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Blockade Flagship: Bridge"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Endor"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("Rogue Shadow", True),
    n("Victory", True),
    n("Blizzard 4", qty=2),
    n("Grand Moff Tarkin", True),
    n("Juno Eclipse, Black Leader", True),
    n("Grand Admiral Thrawn"),
    n("General Nevar", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("P-59"),
    n("Dengar With Blaster Carbine", True),
    n("Mara Jade With Lightsaber", True),
    n("Boba Fett, Bounty Hunter", qty=2),
    n("Emperor Palpatine", qty=3),
    n("Droideka", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Galen, Secret Apprentice", True, qty=3),
    n("Prepared Defenses", True),
    n("They're Still Coming Through!", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master", True),
    n("Endor Shield"),
    n("A Sith's Plans", True),
    n("Knowledge And Defense"),
    n("Weapon Levitation & The Empire's Back", True),
    n("Imperial Barrier", True),
    n("Presence Of The Force"),
]
DS_SHIELDS = [
    n("Compassion & Concession", True),
    n("Secret Plans", True),
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("Come Here You Big Coward", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption", True),
    n("There Is No Try"),
    n("Weapon Of A Sith", True),
    n("We'll Let Fate-A Decide, Huh?", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = [
    n("Leave Them To Me", True),
    n("Firepower", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
