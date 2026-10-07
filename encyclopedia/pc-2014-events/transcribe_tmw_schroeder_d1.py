#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Olaf Schroeder (Name Schultz pair).

Source: 2014-TMW-Day-1.pdf pages 1–2 (2013 form).
Name Schultz dested Olaf Schroeder (informed 99.9%; hub lists Olaf Schroeder;
2013 TMW Schultz skip was stale because that sheet was Schroeder).
"""
from __future__ import annotations

PLAYER = "Olaf Schroeder"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2014 Texas Mini Worlds Day 1 p01 Olaf Schroeder LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p02 Olaf Schroeder DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields). Name Schultz dested Olaf Schroeder."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Schultz dested Olaf Schroeder. Username blank. LIGHT/DARK both empty; cards are Light. "
    "Deck Name Tom Haiel. "
    "TIGIH dested There Is Good In Him / I Can Save Him. "
    "Luke Rebel Scout dested Luke Skywalker, Rebel Scout. "
    "Luke's Saber dested Luke's Lightsaber. "
    "Chirpa's Hut dested Endor: Chief Chirpa's Hut. "
    "Endor DB dested Endor: Landing Platform (Docking Bay). "
    "AFA dested Anger, Fear, Aggression. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Mace dested Mace Windu. "
    "Mace Moto dested Mace Windu, Master Of The Order. "
    "Master QG dested Master Qui-Gon. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "Obi w Stick dested Obi-Wan With Lightsaber. "
    "Anakin dested Anakin Skywalker, Padawan Learner. "
    "Padme dested Padmé Naberrie. "
    "Lando UH dested Lando Calrissian, Unlikely Hero. "
    "Jarful dested as written. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader. "
    "Leia RP dested Leia, Rebel Princess. "
    "Ackbar dested Admiral Ackbar. "
    "HCF dested Han, Chewie, And The Falcon. "
    "Jedi Saber dested Jedi Lightsaber. "
    "Qui Gons Saber 5 dested Qui-Gon Jinn's Lightsaber. "
    "Dressid dested Dressel. "
    "JCC dested Coruscant: Jedi Council Chamber. "
    "Bhl dested as written. "
    "H1WR dested Home One: War Room. "
    "Sai'torr dested Sai'torr Kal Fas. "
    "Seeking dested Seeking An Audience. "
    "Atrocity dested Imperial Atrocity. "
    "C + TV dested Control & Tunnel Vision. "
    "Blaster Reflect dested Blaster Deflection. "
    "Speak w/ Council dested Speak With The Jedi Council. "
    "Found YH + HG + ASB + RockPath dested Found Someone You Have & Higher Ground. "
    "SLW x2 dested Slight Weapons Malfunction (x2 on the name line dested qty=1 so main=60). "
    "Wesa dested Wesa Gotta Grand Army. "
    "Yub Yub who the hell made this dested Yub Yub, Commander. "
    "Seriously, Lanes Even dested as written. "
    "R Leadership dested Rebel Leadership. "
    "LTWW dested Let The Wookiee Win. "
    "Your Ship dested Your Ship?. "
    "Tragedy Has Occurred dested A Tragedy Has Occurred. "
    "DDTA dested Don't Do That Again. "
    "Simple Tricks + Nonsense dested Simple Tricks And Nonsense. "
    "Oetamin dested The Professor. "
    "DODN dested Do, Or Do Not. "
    "Superficial dested Superficial Injuries. "
    "LTWW shield dested Let The Wookiee Win. "
    "Lets Keep dested Let's Keep A Little Optimism Here. "
    "Tactics + Weapons Display dested Weapons Display. "
    "Unique overcounts sheet-accurate (Master Qui-Gon x2, Smoke Screen x3, "
    "Wesa Gotta Grand Army x2, Rebel Leadership x3, "
    "Let The Wookiee Win x3). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Schultz dested Olaf Schroeder. Username blank. DARK checked. "
    "Deck Name Texas Hates Me. "
    "Kessel dested Kessel. "
    "Kessel Admin's Office dested Kessel: Spice Mines - Administrator's Office. "
    "Extraction Facility dested Kessel: Spice Mines - Extraction Facility. "
    "Prison dested Kessel: Spice Mines - Prison. "
    "CC Security Tower dested Cloud City: Security Tower. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "AI, Guri Ma dested as written. "
    "Gift of the Master dested Gift Of The Master. "
    "Cadet Needles dested Captain Needa. "
    "Dro + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Jango Assassin dested Jango Fett, The Assassin. "
    "Boba PH dested Boba Fett, Prepared Hunter. "
    "DROIDOTS dested Destroyer Droid. "
    "DV Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Dooku dested Count Dooku. "
    "Galen dested Galen Marek, Starkiller. "
    "Darth Maul w Saber dested Darth Maul With Lightsaber. "
    "Sidious Saber dested Sidious Lightsaber. "
    "NO_DEST remaining: Jarful, Bhl, Seriously Lanes Even, Superficial Injuries, "
    "AI Guri Ma, Unhappy Look, YCCHC, Frozen Captive. "
    "Dooku's Saber dested Dooku's Lightsaber. "
    "Galen saber dested Galen's Lightsaber, Vader's Gift. "
    "Kessel asteroid system dested Kessel Surveillance System. "
    "Blizz 4 dested Blizzard 4. "
    "Maul's Interceptor dested Maul's Sith Infiltrator. "
    "Slave I, SoF dested Slave I, Symbol Of Fear. "
    "Prepared Defense dested Prepared Defenses. "
    "Bitter Rack dested Blaster Rack. "
    "Sense Combo dested Sense. "
    "Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Short Range Combo dested Short Range Fighters & Watch Your Back!. "
    "Sith Fury Combo dested Sith Fury & End This Destructive Conflict. "
    "Alter dested Alter (Coruscant). "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "YCCHC dested as written. "
    "Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Find Your Lack of Faith Disturbing dested I Find Your Lack Of Faith Disturbing. "
    "TINT dested There Is No Try. "
    "Weapon of a Sith dested Weapon Of A Sith. "
    "Always dested Always Thinking With Your Stomach. "
    "Unhappy Look dested as written. "
    "Unique overcounts sheet-accurate (Emperor Palpatine x3, Count Dooku x2, "
    "Darth Sidious x2, Galen Marek, Starkiller x2, Darth Maul With Lightsaber x2, "
    "Sonic Bombardment x3, Short Range Fighters & Watch Your Back! x3). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("I Feel The Conflict"),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Rogue Squadron Tactics"),
    n("Mace Windu", True),
    n("Mace Windu, Master Of The Order"),
    n("Master Qui-Gon", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Obi-Wan With Lightsaber"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Yoda"),
    n("Padmé Naberrie", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Rebel Barrier", True),
    n("Jarful"),
    n("Corran Horn"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Leia, Rebel Princess"),
    n("Admiral Ackbar", True),
    n("Han, Chewie, And The Falcon"),
    n("Home One"),
    n("Lady Luck"),
    n("Jedi Lightsaber", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Dressel"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Bhl"),
    n("Home One: War Room"),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Imperial Atrocity", True),
    n("Houjix"),
    n("Dark Approach", True),
    n("Smoke Screen", qty=3),
    n("Escape Pod", True),
    n("Control & Tunnel Vision"),
    n("Blaster Deflection"),
    n("Speak With The Jedi Council"),
    n("Found Someone You Have & Higher Ground"),
    n("Slight Weapons Malfunction", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("Yub Yub, Commander"),
    n("Seriously, Lanes Even"),
    n("Rebel Leadership", True, qty=3),
    n("Let The Wookiee Win", True, qty=3),
]
LS_SHIELDS = [
    n("Your Ship?"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan", True),
    n("The Professor"),
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("Do, Or Do Not"),
    n("Superficial Injuries"),
    n("Let The Wookiee Win"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
]
LS_ADD = []


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Kessel: Spice Mines - Prison"),
    n("Cloud City: Security Tower"),
    n("Spice Mine Operations"),
    n("Knowledge And Defense", True),
    n("AI, Guri Ma", True),
    n("I'll Take Them Myself"),
    n("Gift Of The Master"),
    n("Captain Needa"),
    n("Dr. Evazan & Ponda Baba"),
    n("Ghhhk", True),
    n("Death Star"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Arica"),
    n("Destroyer Droid"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Emperor Palpatine", qty=3),
    n("Count Dooku", qty=2),
    n("Darth Sidious", qty=2),
    n("Galen Marek, Starkiller", qty=2),
    n("Darth Maul With Lightsaber", qty=2),
    n("Sidious Lightsaber"),
    n("Dooku's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Kessel Surveillance System"),
    n("Blizzard 4"),
    n("Maul's Sith Infiltrator"),
    n("Slave I, Symbol Of Fear"),
    n("Black Sun Fleet"),
    n("Imperial Justice", True),
    n("Prepared Defenses"),
    n("Blaster Rack", True),
    n("Sense"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sonic Bombardment", True, qty=3),
    n("Why Didn't You Tell Me?", True),
    n("Unhappy Look"),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Cold Feet", True),
    n("Force Push", True),
    n("Lightsaber Deficiency", True),
    n("Force Lightning"),
    n("Dark Maneuvers"),
    n("Force Field"),
    n("Sense"),
    n("Alter (Coruscant)", True),
    n("Sith Fury & End This Destructive Conflict"),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("YCCHC", True),
    n("Secret Plans"),
    n("Firepower", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("I Find Your Lack Of Faith Disturbing"),
    n("There Is No Try"),
    n("Allegations Of Corruption"),
    n("Crossfire"),
    n("Weapon Of A Sith"),
    n("Frozen Captive", True),
    n("Always Thinking With Your Stomach", True),
]
DS_ADD = []
