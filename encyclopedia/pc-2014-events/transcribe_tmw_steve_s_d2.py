#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 2 Xerox: Steve S.

Source: 2014-TMW-Day-2.pdf pages 5–6 (2013 form).
Name Steve S dested as written (username blank; handwriting differs from Day 1 Skilton).
"""
from __future__ import annotations

PLAYER = "Steve S"
USERNAME = ""
STAGE = "Day 2"
PDF = "2014 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2014 Texas Mini Worlds Day 2 p06 Steve S LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 2 p05 Steve S DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields). Name dested as written."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Steve S dested as written. Username blank. LIGHT checked. "
    "Deck Name JJD + DJK's Deck. "
    "Do not dest as Steve Skilton (Day 1 Skilton handwriting and this sheet differ; username blank). "
    "RAW dested Republic At War / A Precarious Predicament. "
    "Geo: Comm Ctr dested Geonosis: Forward Command Center. "
    "Begun Clone War Has dested Begun, The Clone War Has. "
    "Rogue Squad Tact dested Rogue Squadron Tactics. "
    "Crash Site Mem dested Crash Site Memorial. "
    "Assault On Muun dested Assault On Muunilinst. "
    "Muun: DB dested Muunilinst: Harnaidan? Muun: DB dested as written then Muunilinst sites. "
    "Muun: Landing Site dested Muunilinst: Republic Landing Site. "
    "Muun: Harnaidan Plains dested Muunilinst: Harnaidan Plains. "
    "Muun: City of Harnaidan dested Muunilinst: City Of Harnaidan. "
    "Dual Laser Cann dested Dual Laser Cannon. "
    "Lucky Shot Non-(V) dested Lucky Shot. "
    "Phyfo dested as written. "
    "Barrier dested Rebel Barrier. "
    "AT-RT dested AT-RT. "
    "Plo Koon dested Plo Koon. "
    "Acclamator dested Acclamator-Class Assault Ship. "
    "All Wings + DS dested All Wings Report In & Darklighter Spin. "
    "SATM dested Sorry About The Mess. "
    "SATM Combo dested Sorry About The Mess & Blaster Proficiency. "
    "Not My Fault dested It's Not My Fault!. "
    "Lando UH dested Lando Calrissian, Unlikely Hero. "
    "Obi-JK dested Obi-Wan Kenobi, Jedi Knight. "
    "Away Put Weapon dested Away With His Weapon?. "
    "Anakin Skywalk, PL dested Anakin Skywalker, Padawan Learner. "
    "Seeking dested Seeking An Audience. "
    "Atrocity dested Imperial Atrocity. "
    "Projection dested Projection Of A Skywalker. "
    "Dressel dested Dressel. "
    "Anakin Solo dested Anakin Solo. "
    "Jaina Solo dested Jaina Solo. "
    "Dash Rendar dested Dash Rendar. "
    "HFTMF dested Heading For The Medical Frigate. "
    "AFA dested Anger, Fear, Aggression. "
    "Keep Optimism dested Let's Keep A Little Optimism Here. "
    "Insight dested Your Insight Serves You Well. "
    "DDTA dested Don't Do That Again. "
    "Line 31 Plo Koon (V) replacement for a crossed card. "
    "Unique overcounts sheet-accurate (Dual Laser Cannon x4, AT-RT x9, "
    "Acclamator-Class Assault Ship x2, All Wings Report In & Darklighter Spin x2, "
    "Sorry About The Mess lines, Away Put Weapon x2). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Steve S dested as written. Username blank. DARK checked. "
    "Deck Name I Made This One. "
    "HD dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "DVD lots dested Darth Vader, Dark Lord Of The Sith. "
    "Myn dested Myn Kyneugh. "
    "NO_DEST remaining: Phyfo, Away With His Weapon?, Muunilinst: DB, Republic At War. "
    "EPP Maul dested Darth Maul With Lightsaber. "
    "Visage dested Visage Of The Emperor. "
    "Vader Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Sniper & Dark Strike dested Sniper & Dark Strike. "
    "Comscan Detect dested ComScan Detection. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "SFS + WYB dested Short Range Fighters & Watch Your Back!. "
    "Exec: Med Chamber dested Executor: Meditation Chamber. "
    "DS: WR dested Death Star: War Room. "
    "CC: Security Tower dested Cloud City: Security Tower. "
    "Exec: Holotheatre dested Executor: Holotheatre. "
    "BF: Bridge dested Blockade Flagship: Bridge. "
    "Blizz 4 dested Blizzard 4. "
    "Dooku's Saber dested Dooku's Lightsaber. "
    "Vader's Saber dested Vader's Lightsaber. "
    "ROTS dested Revenge Of The Sith. "
    "EPP Dengar dested Dengar With Blaster Carbine. "
    "Dr E + Ponda dested Dr. Evazan & Ponda Baba. "
    "Boba PH dested Boba Fett, Prepared Hunter. "
    "Boba, BH dested Boba Fett. "
    "Jango Assassin dested Jango Fett, The Assassin. "
    "Ni Chuba Na dested Ni Chuba Na. "
    "EPP Mara dested Mara Jade With Lightsaber. "
    "GOTM dested Gift Of The Master. "
    "K&D dested Knowledge And Defense. "
    "Weapon of a Sith dested Weapon Of A Sith. "
    "Coward dested Come Here You Big Coward. "
    "We'll Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "Lack of Faith dested I Find Your Lack Of Faith Disturbing. "
    "Cannot Hide Forever dested You Cannot Hide Forever. "
    "Useless Gesture dested A Useless Gesture. "
    "Unique overcounts sheet-accurate (Bossk x2, Emperor Palpatine x2, "
    "Darth Vader, Dark Lord Of The Sith x2, Darth Maul With Lightsaber x2, "
    "Visage Of The Emperor x2, Sonic Bombardment x3, We Must Accelerate Our Plans x2, "
    "Force Lightning x2, Short Range Fighters & Watch Your Back! x2, Blizzard 4 x2, "
    "Garindan x2, Masterful Move x2). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Republic At War / A Precarious Predicament"
LS_CARDS = [
    n("Republic At War / A Precarious Predicament"),
    n("Geonosis: Forward Command Center"),
    n("Nick Of Time", True),
    n("Begun, The Clone War Has"),
    n("Wokling", True),
    n("Rogue Squadron Tactics"),
    n("Crash Site Memorial"),
    n("Assault On Muunilinst"),
    n("Muunilinst: DB"),
    n("Muunilinst: Republic Landing Site"),
    n("Muunilinst: Harnaidan Plains"),
    n("Muunilinst: City Of Harnaidan"),
    n("Desperate Tactics"),
    n("Rebel Barrier"),
    n("Dual Laser Cannon", True, qty=2),
    n("Dual Laser Cannon", qty=2),
    n("Lucky Shot", qty=2),
    n("Phyfo", True),
    n("AT-RT", True, qty=2),
    n("AT-RT", qty=7),
    n("Plo Koon", True),
    n("Rebel Barrier"),
    n("Weapon Levitation"),
    n("Acclamator-Class Assault Ship", qty=2),
    n("Escape Pod", True),
    n("It's Not My Fault!"),
    n("All Wings Report In & Darklighter Spin"),
    n("Sorry About The Mess"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("All Wings Report In & Darklighter Spin"),
    n("Rebel Artillery"),
    n("It's Not My Fault!", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Lady Luck"),
    n("Away With His Weapon?", True),
    n("Anakin Skywalker, Padawan Learner"),
    n("Seeking An Audience", True),
    n("Imperial Atrocity"),
    n("Dark Approach"),
    n("Away With His Weapon?", True),
    n("Houjix"),
    n("Projection Of A Skywalker"),
    n("Dressel"),
    n("Anakin Solo"),
    n("Jaina Solo"),
    n("Dash Rendar", True),
    n("Heading For The Medical Frigate"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Yavin Sentry"),
    n("Affect Mind"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well"),
    n("Don't Do That Again", True),
    n("Chasm"),
    n("Battle Plan"),
    n("Wise Advice"),
    n("Do, Or Do Not"),
    n("Weapons Display"),
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Bossk", qty=2),
    n("Emperor Palpatine", qty=2),
    n("P-59"),
    n("Grand Moff Tarkin", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Myn Kyneugh", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Visage Of The Emperor", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Conduct Your Search"),
    n("Force Push", True),
    n("Ghhhk"),
    n("Sniper & Dark Strike"),
    n("Masterful Move"),
    n("ComScan Detection", True),
    n("Sonic Bombardment", True, qty=3),
    n("We Must Accelerate Our Plans", qty=2),
    n("Why Didn't You Tell Me?", True),
    n("Monnok"),
    n("Force Lightning", qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Prepared Defenses"),
    n("Executor: Meditation Chamber"),
    n("Death Star: War Room"),
    n("Endor: Back Door"),
    n("Cloud City: Security Tower"),
    n("Executor: Holotheatre"),
    n("Blockade Flagship: Bridge"),
    n("Blizzard 4", qty=2),
    n("Dooku's Lightsaber"),
    n("Vader's Lightsaber"),
    n("Revenge Of The Sith"),
    n("Dengar With Blaster Carbine", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Boba Fett, Prepared Hunter"),
    n("Boba Fett"),
    n("Jango Fett, The Assassin"),
    n("Garindan", qty=2),
    n("Ni Chuba Na?", True),
    n("Mara Jade With Lightsaber"),
    n("No Escape"),
    n("Darth Sidious"),
    n("Gift Of The Master"),
    n("Blaster Rack"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Masterful Move"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Slave I, Symbol Of Fear"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Firepower"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?"),
    n("Death Star Sentry"),
    n("After Her!"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Battle Order"),
    n("Abyss"),
    n("A Useless Gesture", True),
]
DS_ADD = []
