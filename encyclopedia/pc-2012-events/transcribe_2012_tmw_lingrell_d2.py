#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 2 leftover Xerox: Scott Lingrell.

Source: 2012TMWDay2.pdf pages 3–4 (handwritten 2010 Xerox, right numbered 37–60).
Name Advocate dested Scott Lingrell analog leftover Day 1 CANON /
player-stubs/Scott_Lingrell.wiki GEMP handle advocate. Username blank.
p03 Light Precise Hit Profit. p04 Dark Set Your Labia for Stun.
Do not dest as a new person Advocate. Do not dest as Chris Schoenthal.
Do not dest Day 1 TMW / 2012 MPC Lingrell 60s again.
"""
from __future__ import annotations

PLAYER = "Scott Lingrell"
USERNAME = ""
STAGE = "Day 2"
PDF = "2012 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2012 Texas Mini Worlds Day 2 Scott Lingrell LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 2 Scott Lingrell DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p03 handwritten 2010 Xerox Light Precise Hit Profit. "
    "p04 handwritten 2010 Xerox Dark Set Your Labia for Stun. "
    "Name Advocate dested Scott Lingrell analog leftover Day 1 CANON. "
    "Username blank. Right column numbered 37–60. "
    "Do not dest as a new person Advocate. Do not dest as Chris Schoenthal. "
    "Do not dest Day 1 TMW / 2012 MPC Lingrell 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p03 Light Deck Name Precise Hit Profit. LIGHT checked. "
    "Event Texas. Name Advocate dested Scott Lingrell analog leftover Day 1. Username blank. "
    "You Can Either Profit By This empty dested You Can Either Profit By This analog leftover Banger dual-title virtual-only. "
    "Audience Chamber dested Jabba's Palace: Audience Chamber analog leftover Banger. "
    "Council Chamber dested Coruscant: Jedi Council Chamber analog leftover JCC. "
    "Lars Farm dested Tatooine: Lars' Moisture Farm analog leftover Jellison. "
    "Chew's Bowcaster dested Chewbacca's Bowcaster analog leftover. "
    "Tat Util Belt dested Tatooine Utility Belt analog leftover Pietruszewski. "
    "Luke's Gun dested Luke's Blaster Pistol analog leftover Baroni. "
    "Naked 3PO dested Threepio With His Parts Showing analog leftover Banger. "
    "Yutani w/ Blaster dested Captain Yutani With Blaster Cannon analog leftover Banger. "
    "Leia with blaster dested Leia With Blaster Rifle analog leftover Tom. "
    "Tantel Skreej dested Tamtel Skreej analog leftover. "
    "K'lor slug dested K'lor'slug analog leftover Joe. "
    "Armed & Dangerous / Krayt Howl dested Armed And Dangerous & Krayt Dragon Howl analog leftover Atkin. "
    "A Jedi Concentration dested A Jedi's Concentration analog leftover. "
    "Speak With The Jedi dested Speak With The Jedi Council analog leftover Anis. "
    "A280 Rifle dested A280 Sharpshooter Rifle analog leftover Emil. "
    "Anger, Fear dested Anger, Fear, Aggression analog leftover Anderson IN THE 60. "
    "Shield Tragedy dested A Tragedy Has Occurred analog leftover. "
    "Shield Onasm dested Let's Keep A Little Optimism Here analog leftover Richards Day 2. "
    "Shield DDTA dested Don't Do That Again analog leftover. "
    "Shield That's One Planetary Defense dested That's One analog leftover Mix. "
    "Shield Simple Tricks dested Simple Tricks And Nonsense analog leftover Lingrell qty=2 unique overcount. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p04 Dark Deck Name Set Your Labia for Stun. DARK checked. "
    "Event Texas. Name Advocate dested Scott Lingrell analog leftover Day 1. Username blank. "
    "Line 1 Tatooine (EP1) starting location on printed OBJECTIVE dested Court Of The Vile Gangster analog leftover Banger virtual-only. "
    "Tat:JP dested Tatooine: Jabba's Palace analog leftover Alex W. "
    "Imp Stockpile dested Imperial Stockpile analog leftover Brodsky. "
    "Audience Chamber dested Jabba's Palace: Audience Chamber analog leftover Banger. "
    "Lower Passages dested Jabba's Palace: Lower Passages analog leftover. "
    "U3PO dested U-3PO analog leftover Lush. "
    "Boba Fett, BH dested Boba Fett, Bounty Hunter analog leftover Nats. "
    "4-Lom dested 4-LOM analog leftover. "
    "Fouc dested Guri analog leftover Buck qty=2 unique overcount. "
    "Short Range + Watch Your Back dested Short Range Fighters & Watch Your Back analog leftover Bali. "
    "Ghhhk + TRWEU dested Ghhhk & Those Rebels Won't Escape Us analog leftover. "
    "Imbalance + Kintan Strider dested Imbalance & Kintan Strider analog leftover Kirkpatrick. "
    "Knowledge & Defense dested Knowledge And Defense analog leftover Anderson IN THE 60. "
    "Shield YCHF dested You Cannot Hide Forever analog leftover Lingrell. "
    "Shield Abuse dested Abyss analog leftover. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This"
LS_CARDS = [
    n("You Can Either Profit By This"),
    n("Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han", True),
    n("Heading For The Medical Frigate"),
    n("Seeking An Audience", True),
    n("Quick Draw", True),
    n("I Must Be Allowed To Speak", True),
    n("Tatooine: Lars' Moisture Farm", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("A280 Sharpshooter Rifle", True),
    n("Chewbacca's Bowcaster"),
    n("Tatooine Utility Belt", True),
    n("Luke's Blaster Pistol", True),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Captain Yutani With Blaster Cannon", True),
    n("Orrimaarko", True),
    n("Threepio With His Parts Showing"),
    n("Leia", True),
    n("Leia With Blaster Rifle"),
    n("Chewie, Protector", qty=2),
    n("Padme Naberrie", True),
    n("Tamtel Skreej", True),
    n("Master Luke", qty=4),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("K'lor'slug", True),
    n("Advantage", True),
    n("Hiding In The Garbage", True),
    n("I Hope She's All Right"),
    n("Houjix"),
    n("Skywalkers"),
    n("Run, Luke, Run!"),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Hear Me Baby, Hold Together", True),
    n("Jedi Levitation", True),
    n("We're Doomed"),
    n("Rebel Artillery", qty=2),
    n("Let The Wookiee Win", True),
    n("A Jedi's Concentration", qty=3),
    n("Precise Hit", True, qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Nabrun Leids"),
    n("Visored Vision", True, qty=2),
    n("Slight Weapons Malfunction", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Do Or Do Not"),
    n("Insight", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice", True),
    n("Don't Do That Again", True),
    n("That's One", True),
    n("Simple Tricks And Nonsense", True, qty=2),
]
LS_ADD = []

DS_START = "Court Of The Vile Gangster"
DS_CARDS = [
    n("Court Of The Vile Gangster"),
    n("Combat Readiness", True),
    n("Tatooine: Jabba's Palace"),
    n("Combat Response", True),
    n("Jabba's Haven", True),
    n("Imperial Stockpile", True),
    n("Concussion Missile"),
    n("Kashyyyk"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Lower Passages"),
    n("Nal Hutta"),
    n("Black Sun Fleet", qty=2),
    n("Maul's Sith Infiltrator"),
    n("Hound's Tooth", True),
    n("Slave I", True),
    n("Mist Hunter", True),
    n("Obsidian 10", True),
    n("Black 3", True),
    n("Punishing One", True),
    n("Undercover", True, qty=3),
    n("Imperial Propaganda", True),
    n("Pride Of The Empire"),
    n("Bossk", True),
    n("Guri", True, qty=2),
    n("Brangus Glee", True),
    n("U-3PO"),
    n("Boba Fett, Bounty Hunter", True),
    n("Boba Fett, Bounty Hunter"),
    n("Labria", True),
    n("Zuckuss", True),
    n("OS-72-10"),
    n("OS-61-3"),
    n("Dengar", True),
    n("4-LOM", True),
    n("Darth Maul", qty=2),
    n("Nevar Yalnal", qty=3),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Set For Stun", qty=3),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Coordinated Attack", True),
    n("Force Push", True),
    n("Informant", True),
    n("Why Didn't You Tell Me?", True, qty=2),
    n("Imbalance & Kintan Strider"),
    n("Unsalvageable", True),
    n("Unsalvageable"),
    n("Imbalance & Kintan Strider"),
    n("Arica"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Battle Order"),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Imperial Detention", True),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Do They Have A Code Clearance?"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
]
DS_ADD = []
