#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 2: Kevin Shannon Xerox LS+DS.

Light sheet crosses out Phil Aasen and writes Kevin Shannon (joke).
Dark sheet sticky note James Shenanigans is Kevin Shannon.
"""
from __future__ import annotations

PLAYER = "Kevin Shannon"
USERNAME = "Karrdeshark"
STAGE = "Day 2"
PDF = "2013 SoCal Grand Prix Day 2.pdf"
LS_PAGE = 8
DS_PAGE = 9
LS_SCAN = "2013 SoCal Grand Prix Day 2 p08 Kevin Shannon LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 2 p09 Kevin Shannon DS.png"
LS_NOTE = (
    "Handwritten Xerox form. Name Phil Aasen struck, Kevin Shannon written (joke). "
    "Username Karrdeshark and Phil's email remain on the sheet. Deck Name Nobody Plays Combat. "
    "We'll Handle This / DOTF → We'll Handle This / Duel Of The Fates. "
    "TP Gen Core / TP Generator → Naboo: Theed Palace Generator Core / Naboo: Theed Palace Generator. "
    "HFTMF → Heading For The Medical Frigate. BN Chambers → Naboo: Boss Nass' Chambers. "
    "SITF → Luke Skywalker, Strong In The Force. MOTO → Mace Windu, Master Of The Order. "
    "Qui-Gon Jinn, JM → Qui-Gon Jinn, Jedi Master. R2 in Red 5 → Artoo-Detoo In Red 5. "
    "HCF → Han, Chewie, And The Falcon. Flash of Insight struck, Redeemed Apprentice remains. "
    "AWRI & DS → All Wings Report In & Darklighter Spin. AM & Rebel Reinforcements is the "
    "Reflections combo. LTWW → Let The Wookiee Win. T Bith Shuffle & DR → "
    "The Bith Shuffle & Desperate Reach. WGG Army → Wesa Gotta Grand Army. "
    "OCLT Weapon in the shield box → Only Jedi Carry That Weapon. "
    "DDT Again → Don't Do That Again. DODN&T → Do, Or Do Not. "
    "He Can Go About His Business struck, Chasm remains. "
    "LKALO Optimism → Let's Keep A Little Optimism Here. "
    "Planetary Defense → Planetary Defenses. YISY Well → Your Insight Serves You Well. "
    "Your Ship? struck, Weapons Display remains. Hidden Fortress lines are a joke note "
    "(Greg Shaw's IG-88 Day 1 Dark), not dested as Hidden Fortress cards. "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Print Form. Sticky note James Shenanigans is Kevin Shannon. "
    "Event SoCal Grand Prix, 26 October 2013. Carbon Chamber Testing / My Favorite Decoration. "
    "Carkoonite Chamber → Cloud City: Carbonite Chamber. IG-88 on line 9 struck; Elis Helrot remains. "
    "Boba Fett, Prepared Hunter → Boba Fett, Bounty Hunter. Boba Fett (SE) → Boba Fett. "
    "The Emperor → The Emperor. U-3PO → U-3PO (Yoo-Threepio). "
    "Short Range Fighters & WYB → Short Range Fighters & Watch Your Back!. "
    "Sense (Premiere) → Sense. WMAOP → We Must Accelerate Our Plans. "
    "I Find Your Lack of Faith → I Find Your Lack Of Faith Disturbing. "
    "We'll Let Fate Decide → We'll Let Fate-a Decide, Huh?. "
    "DTHACC → Do They Have A Code Clearance?. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("Inner Strength"),
    n("Heading For The Medical Frigate"),
    n("Rycar Ryjerd", True),
    n("Sai'torr Kal Fas", True),
    n("Wokling", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Aayla Secura", True, qty=2),
    n("Corran Horn"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Mace Windu, Master Of The Order", True, qty=2),
    n("Qui-Gon Jinn, Jedi Master", qty=3),
    n("Sergeant Doallyn", True),
    n("Artoo-Detoo In Red 5", qty=3),
    n("Han, Chewie, And The Falcon"),
    n("Guardian's Lightsaber", True),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Qui-Gon's Lightsaber"),
    n("Luke's Bionic Hand", True, qty=2),
    n("Mercenary Armor", True),
    n("Obi-Wan's Journal"),
    n("Redeemed Apprentice", True),
    n("I'm With You Too", True),
    n("Imperial Atrocity", True),
    n("Lightsaber Proficiency"),
    n("Undercover", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Away Put Your Weapon", True),
    n("Blaster Deflection", qty=2),
    n("Clinging To The Edge", True),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Jedi Levitation", True),
    n("Let The Wookiee Win", True, qty=3),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Weapon Levitation"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Chasm", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Planetary Defenses", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: Security Tower", True),
    n("Carbonite Chamber Console", True),
    n("Jabba's Prize"),
    n("Any Methods Necessary"),
    n("IG-88", True),
    n("IG-88's Neural Inhibitor", True),
    n("Elis Helrot"),
    n("Despair", True),
    n("Darth Vader With Lightsaber"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Maul"),
    n("Darth Maul With Lightsaber"),
    n("Boba Fett, Bounty Hunter"),
    n("Boba Fett", True),
    n("Dr. Evazan & Ponda Baba"),
    n("The Emperor", True, qty=2),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Mara Jade With Lightsaber"),
    n("Jango Fett, The Assassin"),
    n("U-3PO"),
    n("4-LOM With Concussion Rifle", True),
    n("Blockade Flagship: Bridge"),
    n("Jabba's Palace: Dungeon"),
    n("Jabba's Palace: Audience Chamber"),
    n("Kashyyyk"),
    n("Dagobah: Cave"),
    n("Victory"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Black Sun Fleet"),
    n("Disarmed", qty=2),
    n("Protocol Failure"),
    n("The Phantom Menace"),
    n("Much Anger In Him"),
    n("No Escape"),
    n("Sneak Attack"),
    n("Defensive Fire", True, qty=2),
    n("Imperial Artillery"),
    n("Imperial Barrier"),
    n("Imperial Command"),
    n("Lightsaber Deficiency", True),
    n("A Dark Time For The Rebellion", True),
    n("Control & Set For Stun"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Stunning Leader", qty=2),
    n("Masterful Move"),
    n("Sense", qty=2),
    n("Cold Feet", True),
    n("Force Lightning", qty=2),
    n("We Must Accelerate Our Plans"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Battle Order"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("Death Star Sentry", True),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
]
DS_ADD = []
