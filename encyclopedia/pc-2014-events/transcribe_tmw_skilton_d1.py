#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Steve Skilton.

Source: 2014-TMW-Day-1.pdf pages 3–4 (2013 form).
"""
from __future__ import annotations

PLAYER = "Steve Skilton"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 4
DS_PAGE = 3
LS_SCAN = "2014 Texas Mini Worlds Day 1 p04 Steve Skilton LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p03 Steve Skilton DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields)."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Skilton dested Steve Skilton. Username blank. LIGHT checked. "
    "Deck Name Steal this Book. "
    "TIGIH dested There Is Good In Him / I Can Save Him. "
    "Do not dest as a new person. Do not rewrite 2013 MPC Steve S. / Worlds / SoCal / TMW Skilton leftovers. "
    "EPP Han dested Han With Heavy Blaster Pistol. "
    "Ref iii Lando dested Lando Calrissian, Scoundrel. "
    "Ref iii Chewie dested Chewbacca, Protector. "
    "EPP Obi dested Obi-Wan With Lightsaber. "
    "EPP Qui Gon dested Qui-Gon Jinn With Lightsaber. "
    "Ref iii Leia dested Leia, Rebel Princess. "
    "Mace MOTO dested Mace Windu, Master Of The Order. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "LTWW dested Let The Wookiee Win. "
    "Wesa Gotta dested Wesa Gotta Grand Army. "
    "Speak w/ Jedi dested Speak With The Jedi Council. "
    "RL dested Rebel Leadership. "
    "AJR dested A Jedi's Resilience. "
    "SATM+BP dested Sorry About The Mess & Blaster Proficiency. "
    "JCC dested Coruscant: Jedi Council Chamber. "
    "Y4 Mass WR dested Yavin 4: Massassi War Room. "
    "Chirpa's Hut dested Endor: Chief Chirpa's Hut. "
    "Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "H1 WR dested Home One: War Room. "
    "Jarful dested as written. "
    "Natsun dested Natsun. "
    "Mech Failure dested Mechanical Failure. "
    "Unique overcounts sheet-accurate (Let The Wookiee Win x3, Wesa Gotta Grand Army x3, "
    "Han With Heavy Blaster Pistol x2, Lando Calrissian, Scoundrel x2, Chewbacca, Protector x2, "
    "Obi-Wan With Lightsaber x2, Qui-Gon Jinn With Lightsaber x2, Rebel Leadership x2, "
    "A Jedi's Resilience x2, Dark Approach x2). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Skilton dested Steve Skilton. Username blank. LIGHT/DARK both empty; cards are Dark. "
    "Deck Name Slavers (crossed prior name). "
    "Slaving Ops dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Den of Thieves Combo dested Den Of Thieves & Special Delivery. "
    "ORS dested Outer Rim Scout. "
    "EPP 4-LOM dested 4-LOM With Concussion Rifle. "
    "SRF & WYB dested Short Range Fighters & Watch Your Back!. "
    "Look Sir Droids dested Look Sir, Droids. "
    "Ket Maliss dested Ket Maliss. "
    "EPP Dengar dested Dengar With Blaster Carbine. "
    "EPP Mato dested Mara Jade With Lightsaber. "
    "Jango Assassin dested Jango Fett, The Assassin. "
    "Reegest dested Reegesh. "
    "Boba PH dested Boba Fett, Prepared Hunter. "
    "Slave I, SoF dested Slave I, Symbol Of Fear. "
    "Ghhk Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "K&D dested Knowledge And Defense. "
    "Evader + Monnok dested as written. "
    "Shield 7 Let Fate Decide After Her! crossed with no replacement, skipped. "
    "Unique overcounts sheet-accurate (Outer Rim Scout x4, Sonic Bombardment x3, "
    "4-LOM With Concussion Rifle x2, Short Range Fighters & Watch Your Back! x2, "
    "Sneak Attack x2, Jabba The Hutt x2, Imperial Barrier x2, Scum And Villainy x2). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("I Feel The Conflict"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Luke's Lightsaber"),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Chewbacca, Protector", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Leia, Rebel Princess"),
    n("Mace Windu, Master Of The Order"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Luke Skywalker, Jedi Knight"),
    n("Blaster Deflection", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Speak With The Jedi Council", qty=2),
    n("Rebel Leadership", True),
    n("Rebel Barrier", qty=2),
    n("A Jedi's Resilience"),
    n("Sense", qty=2),
    n("A Jedi's Resilience"),
    n("Dark Approach", True, qty=2),
    n("Clash Of Sabers"),
    n("Natsun"),
    n("Grimtaash"),
    n("Houjix"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Don't Tread On Me", True),
    n("Escape Pod", True),
    n("Mechanical Failure"),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Naboo: Battle Plains"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Yavin 4: Massassi War Room", True),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Home One"),
    n("Home One: War Room"),
    n("Rebel Leadership", True),
    n("Jarful"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("The Professor"),
    n("Weapons Display"),
    n("Yavin Sentry"),
    n("Do, Or Do Not"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Chasm"),
    n("Aim High"),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Jabba's Haven"),
    n("Den Of Thieves & Special Delivery"),
    n("Power Of The Hutt"),
    n("Mercenary Slavers"),
    n("Outer Rim Scout", qty=4),
    n("4-LOM With Concussion Rifle", qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Sneak Attack", True, qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Imperial Barrier", qty=2),
    n("Scum And Villainy", qty=2),
    n("Jabba The Hutt", True, qty=2),
    n("Lightsaber Deficiency", True),
    n("Alter"),
    n("Prince Xizor"),
    n("Kashyyyk: Skyhook Platform"),
    n("Nal Hutta"),
    n("Look Sir, Droids"),
    n("Crush The Rebellion"),
    n("Wookiee Subjugation"),
    n("Evader & Monnok"),
    n("Mercenary Pilot", True),
    n("Jabba's Sail Barge", True),
    n("Ket Maliss", True),
    n("Dengar With Blaster Carbine", True),
    n("Mara Jade With Lightsaber"),
    n("Garindan"),
    n("Jango Fett, The Assassin"),
    n("Reegesh"),
    n("Boba Fett, Prepared Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Abyssin Ornament"),
    n("Hutt Bounty", True),
    n("Probot"),
    n("Maul's Sith Infiltrator"),
    n("Jabba's Space Cruiser", True),
    n("Ephant Mon"),
    n("Protocol Failure"),
    n("P-59"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Velken Tezeri", True),
    n("Ponda Baba", True),
    n("Bossk", True),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Firepower"),
    n("Fanfare", True),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?"),
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Death Star Sentry"),
    n("Oppressive Enforcement"),
    n("Do They Have A Code Clearance?"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
