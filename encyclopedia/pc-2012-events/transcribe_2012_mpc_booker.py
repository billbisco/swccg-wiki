#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: James Booker.

Source: 2012mpcday1.pdf pages 47–48 (handwritten notebook 60s).
Name James Booker dested James Booker (existing 2014 Philadelphia Premiere Event stub).
Username blank (not on notebook).
p47 Light James Booker's LS Deck / Anger, Fear, Aggression.
p48 Dark James Booker's Dark Side List / A Stunning Move.
Do not dest as a new person. Do not dest as James Barnes. Do not rewrite 2013 leftovers.
"""
from __future__ import annotations

PLAYER = "James Booker"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 47
DS_PAGE = 48
LS_SCAN = "2012 Match Play Championship Day 1 James Booker LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 James Booker DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = "Oh, You Can't Read My Decklist?"
NOTE = "Handwritten notebook 60 bound into 2012mpcday1.pdf."
LS_NOTE = (
    "Handwritten notebook. Name James Booker dested James Booker. Username blank. "
    "James Booker's LS Deck. Signature James Booker = Saving Card Slots. "
    "Do not dest as a new person. Do not dest as James Barnes. Do not rewrite 2013 leftovers. "
    "Cor: SCC dested Coruscant: Jedi Council Chamber True. Jedi LS dested Jedi Lightsaber True + empty kept separate. "
    "AJR dested A Jedi's Resilience x2. Atrocity dested Imperial Atrocity True. "
    "Hoth River Room dested Hoth: Echo Command Center (War Room). "
    "A Jedi's Plans dested A Jedi's Plans. Luke, SITF dested Luke Skywalker, Strong In The Force x2. "
    "Hanjix + First Aid dested Odin Nesloor & First Aid. IL-10 dested IL-10. "
    "Leia, RP True + Leia, RP empty kept separate. R2 in R5 dested Artoo-Detoo In Red 5. "
    "Armed and Dangerous + KDH dested Armed And Dangerous & Krayt Dragon Howl. "
    "LS SK dested Luke Skywalker, Jedi Knight. Leia's Blaster dested Leia's Blaster Rifle. "
    "Y4: Mass War Room dested Yavin 4: Massassi War Room. "
    "EPP Obi-Gin / EPP Obi-Wan dested Obi-Wan With Lightsaber x2. "
    "Han, Chewie, Falcon dested Han, Chewie, And The Falcon. "
    "SATM + BP dested Sorry About The Mess & Blaster Proficiency x2. "
    "Yoda, MOTF dested Yoda, Master Of The Force x2. HFTMF dested Heading For The Medical Frigate. "
    "Colo Claw Fish dested Colo Claw Fish. Looking for Me dested Were You Looking For Me? True. "
    "AFA dested Anger, Fear, Aggression True. "
    "Bonus Cards dested shields. The Shield Goes Down dested The Shield Goes Down. "
    "Unique overcounts sheet-accurate (Mace Windu True x2, A Jedi's Resilience x2, "
    "Blaster Deflection x2, Luke Skywalker, Strong In The Force x2, Rebel Leadership True x3, "
    "Yoda, Master Of The Force x2, Let The Wookiee Win True x2, Sense x2, "
    "Obi-Wan With Lightsaber x2, Sorry About The Mess & Blaster Proficiency x2). Unique 60."
)
DS_NOTE = (
    "Handwritten notebook. Name James Booker dested James Booker. Username blank. "
    "James Booker's Dark Side List. Subtitle Oh, You Can't Read My Decklist? COOL STORY, Bro. "
    "Do not dest as a new person. Do not dest as James Barnes. Do not rewrite 2013 leftovers. "
    "ASM dested A Stunning Move / A Valuable Hostage. Instant Dest dested Instantaneous Destruction. "
    "Ni Chuba Na dested Ni Chuba Na?? True. Gift of the Master dested Gift Of The Master. "
    "Jabba's Haven dested Jabba's Haven. Cor: Private Platform dested Coruscant: Private Platform. "
    "Cor: Palp's Quarters dested Coruscant: Palpatine's Quarters. "
    "Galen's LS, VG dested Galen's Lightsaber, Vader's Gift. "
    "Maul's Double-Bladed LS dested Maul's Double-Bladed Lightsaber. "
    "Fett in Hunter dested Boba Fett, Bounty Hunter. BF in SI dested Boba Fett In Slave I. "
    "BF: Hallway / Docking Bay / Bridge dested Blockade Flagship sites. "
    "Naboo: Theed dested Naboo: Theed Palace Generator Core. AAA dested Ability, Ability, Ability True. "
    "Image of a DL dested Image Of The Dark Lord True. Sniper + DS dested Sniper & Dark Strike x2. "
    "Elis dested Elis Helrot. P-59 dested P-59. Dr. E + PB dested Dr. Evazan & Ponda Baba. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi x2. Galen dested Galen Marek, Starkiller x3. "
    "Darth Maul, YA dested Darth Maul, Young Apprentice x3. Maul's Saber dested Maul's Lightsaber. "
    "Weapon Lev dested Weapon Levitation. WMAOP dested We Must Accelerate Our Plans. "
    "MM + EO dested Masterful Move & Endor Occupation. K+D dested Knowledge And Defense. "
    "Ghhhk True + Ghhhk empty kept separate. We'll Let Fate crossed, skipped. "
    "YCHF dested You Cannot Hide Forever True. CHYBC dested Come Here You Big Coward. "
    "All of Cor dested Allegations Of Corruption. Opp Enf dested Oppressive Enforcement. "
    "Unique overcounts sheet-accurate (Control x2, A Dark Time For The Rebellion True x2, "
    "Force Field x2, Sniper & Dark Strike x2, Battle Droid Squad x2, "
    "Grievous, Hunter Of Jedi x2, Galen Marek, Starkiller x3, Darth Maul, Young Apprentice x3). Unique 60."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Coruscant: Jedi Council Chamber", True),
    n("Kiffex"),
    n("Mace Windu", True, qty=2),
    n("Jedi Lightsaber", True),
    n("It Could Be Worse"),
    n("A Jedi's Resilience", qty=2),
    n("Sai'torr Kal Fas"),
    n("Imperial Atrocity", True),
    n("Under Attack"),
    n("Hoth: Echo Command Center (War Room)"),
    n("A Jedi's Plans"),
    n("Lando Calrissian, Scoundrel"),
    n("Blaster Deflection", qty=2),
    n("Luke's Lightsaber"),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Tantive IV", True),
    n("Admiral Ackbar", True),
    n("Rebel Leadership", True, qty=3),
    n("Leia, Rebel Princess", True),
    n("Clash Of Sabers"),
    n("Yoda, Master Of The Force", qty=2),
    n("Odin Nesloor & First Aid"),
    n("IL-10"),
    n("Let The Wookiee Win", True, qty=2),
    n("Corran Horn"),
    n("Seeking An Audience", True),
    n("Desperate Rescue"),
    n("Leia, Rebel Princess"),
    n("Artoo-Detoo In Red 5"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Home One"),
    n("Hear Me Baby, Hold Together", True),
    n("Scrambled Transmission", True),
    n("Padmé Naberrie", True),
    n("Sense", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Leia's Blaster Rifle"),
    n("Yavin 4: Massassi War Room"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Han, Chewie, And The Falcon"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Spiral"),
    n("Home One: War Room"),
    n("Jedi Lightsaber"),
    n("Heading For The Medical Frigate"),
    n("Colo Claw Fish"),
    n("Were You Looking For Me?", True),
    n("Quick Draw", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Battle Plan"),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("The Shield Goes Down"),
    n("Don't Do That Again", True),
    n("Ultimatum", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Instantaneous Destruction"),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Jabba's Haven"),
    n("Coruscant: Private Platform"),
    n("Coruscant: Palpatine's Quarters"),
    n("Prepared Defenses", True),
    n("Dark Jedi Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Blockade Flagship"),
    n("Victory", True),
    n("Zuckuss In Mist Hunter"),
    n("Boba Fett, Bounty Hunter"),
    n("Boba Fett In Slave I"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Bridge"),
    n("Lateral Damage"),
    n("A Sith's Weapon"),
    n("Imperial Propaganda", True),
    n("Ability, Ability, Ability", True),
    n("The Phantom Menace"),
    n("No Escape", True),
    n("Blaster Rack"),
    n("Image Of The Dark Lord", True),
    n("Control", qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Force Field", qty=2),
    n("Sniper & Dark Strike", qty=2),
    n("Elis Helrot"),
    n("Sith Fury", True),
    n("Stop Motion", True),
    n("P-59"),
    n("Ghhhk", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Battle Droid Squad", qty=2),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen Marek, Starkiller", qty=3),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Ghhhk"),
    n("Maul's Lightsaber"),
    n("Weapon Levitation"),
    n("Force Push", True),
    n("We Must Accelerate Our Plans"),
    n("Masterful Move & Endor Occupation"),
    n("Cold Feet", True),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Secret Plans"),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Battle Order"),
    n("Resistance"),
    n("A Useless Gesture", True),
    n("Weapon Of A Sith"),
    n("Oppressive Enforcement"),
]
DS_ADD = []
