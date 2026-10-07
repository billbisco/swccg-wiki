#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Philippe Dubreuil.

Source: 2012mpcday1.pdf pages 65–66 (2010 form, 12 shields).
Name Philippe Dubreuil dested Philippe Dubreuil (2014 Worlds analog).
Username N/A blank. Do not dest as Pierre Dubreuil. Do not dest as a new person.
p65 Light Hidden Base. p66 Dark Endor Operations.
Pack player-stubs/Philippe_Dubreuil.wiki.
"""
from __future__ import annotations

PLAYER = "Philippe Dubreuil"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 65
DS_PAGE = 66
LS_SCAN = "2012 Match Play Championship Day 1 Philippe Dubreuil LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Philippe Dubreuil DS.png"
LS_DECK_NAME = "Same Light Side Deck"
DS_DECK_NAME = "Dark Side Deck"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Philippe Dubreuil dested Philippe Dubreuil. "
    "Username N/A blank. LIGHT checked. Deck Name Same Light Side Deck. Event MPC Date 02/11/12. "
    "Hidden Base dested Hidden Base / Systems Will Slip Through Your Fingers True. "
    "Luke S, Rebel Scout dested Luke Skywalker, Rebel Scout True x2. "
    "Luke S, Jedi Knight dested Luke Skywalker, Jedi Knight. "
    "Hear me Baby, HT dested Hear Me Baby, Hold Together True. "
    "What're you trying dested What Are You Trying To Push On Us?. "
    "We Wish TBAC dested We Wish To Board At Once. "
    "OCC/TT dested Out Of Commission & Transmission Terminated. "
    "Gold Leader in GL dested Gold Leader In Gold 1 True. "
    "HCATF dested Han, Chewie, And The Falcon True. "
    "Gold Squadron 1 dested Gold Squadron 1 x3. "
    "Wedge in RS1 dested Wedge In Red Squadron 1 True. "
    "Blaster Def dested Blaster Deflection. "
    "A Jedi's Resilience dested A Jedi's Resilience x2. "
    "Control / Tunnel V dested Control & Tunnel Vision. "
    "Alderaan Cons Ship dested Radiant VII True. "
    "Captain Venick dested Captain Verrack True. "
    "Qui Gon EPP dested Qui-Gon Jinn With Lightsaber. "
    "Obi-Wan EPP dested Obi-Wan With Lightsaber. "
    "Leia RP dested Leia, Rebel Princess. "
    "Restore Freedom to TG dested Restore Freedom To The Galaxy True. "
    "Massassi Base S dested Massassi Base Sentry True. "
    "Like Trust Me dested Trust Me True. "
    "Haven dested Haven. The Camp dested The Camp. Liberty dested Liberty. "
    "Unique 60. Shields 11 written. Additional empty. (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Philippe Dubreuil dested Philippe Dubreuil. "
    "Username N/A blank. DARK checked. Deck Name Dark Side Deck. Event MPC Date 02/11/12. "
    "Endor Ops dested Endor Operations / Imperial Outpost empty. "
    "Endor Bunker dested Endor: Bunker. "
    "Endor : Landing Platform dested Endor: Landing Platform. "
    "Alert My Star Dest True and empty kept separate. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach True. "
    "Imperial Barrier x2 then Imperial Command x4. "
    "Boba Fett, BH dested Boba Fett, Bounty Hunter. "
    "Dengar in PC dested Dengar In Punishing One. "
    "Darth Maul EPP dested Darth Maul With Lightsaber x2. "
    "Vader EPP dested Darth Vader With Lightsaber x2. "
    "Kir Kanos with FP dested Kir Kanos With Force Pike True. "
    "Dr Evazan and Ponda dested Dr. Evazan & Ponda Baba. "
    "Zuckuss in HH dested Zuckuss In Mist Hunter. "
    "4 Lom EPP dested 4-LOM With Concussion Rifle. "
    "Ice Heart dested Ysanne Isard True. "
    "The Calamari dested Mon Calamari. "
    "A Dark Time empty and True kept separate. "
    "Ulyn Kyneegh dested Myn Kyneugh True. "
    "Alert My Star Dest dested Alert My Star Destroyer!. "
    "Unique 60. Shields 11 written. Additional empty. (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers", True),
    n("Jedi Lightsaber", True),
    n("Luke Skywalker, Rebel Scout", True, qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Admiral Ackbar", True),
    n("Hear Me Baby, Hold Together", True),
    n("Liberty"),
    n("What Are You Trying To Push On Us?"),
    n("Rebel Barrier", qty=2),
    n("Houjix"),
    n("Alter", True),
    n("We Wish To Board At Once"),
    n("Out Of Commission & Transmission Terminated"),
    n("Scrambled Transmission", True),
    n("Tantive IV", True),
    n("Bright Hope", True),
    n("Gold Leader In Gold 1", True),
    n("Han, Chewie, And The Falcon", True),
    n("Spiral"),
    n("Gold Squadron 1", qty=3),
    n("Wedge In Red Squadron 1", True),
    n("Home One"),
    n("Escape Pod", True),
    n("Blaster Deflection"),
    n("A Jedi's Resilience", qty=2),
    n("Sense", qty=2),
    n("Menace Fades"),
    n("Control & Tunnel Vision"),
    n("Radiant VII", True),
    n("Captain Verrack", True),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Lando Calrissian, Scoundrel"),
    n("Obi-Wan With Lightsaber"),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Luke's Lightsaber"),
    n("Flash Of Insight", True, qty=2),
    n("Rescue", True),
    n("Yavin 4: War Room"),
    n("Dressel", True),
    n("Sai'torr Kal Fas", True),
    n("Wokling", True),
    n("Restore Freedom To The Galaxy", True),
    n("Massassi Base Sentry", True),
    n("Haven"),
    n("Launching The Assault"),
    n("Quick Draw", True),
    n("Trust Me", True),
    n("The Camp", True),
    n("Yavin 4: Jedi Academy", True),
    n("Careful Planning", True),
    n("Yavin 4", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Crossing", True),
    n("Affect Mind", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Wise Advice"),
    n("Battle Plan"),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor: Bunker"),
    n("Endor"),
    n("Endor: Landing Platform"),
    n("Establish Secret Base", True),
    n("Ominous Rumors"),
    n("Alert My Star Destroyer!", True),
    n("Establish Control", True),
    n("Endor Shield", True),
    n("Flagship Executor"),
    n("Alert My Star Destroyer!"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Imperial Barrier", qty=2),
    n("Imperial Command", qty=4),
    n("Cold Feet", True),
    n("Boba Fett, Bounty Hunter"),
    n("Dengar In Punishing One"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader With Lightsaber", qty=2),
    n("Force Lightning"),
    n("General Nevar", True),
    n("Janus Greejatus"),
    n("Emperor Palpatine"),
    n("Limited Resources"),
    n("Admiral Piett"),
    n("Lateral Damage"),
    n("Alter", True),
    n("Masterful Move"),
    n("Arica", True),
    n("Kir Kanos With Force Pike", True),
    n("J'Quille", True),
    n("Blizzard 4"),
    n("Dr. Evazan & Ponda Baba"),
    n("Ghhhk"),
    n("Zuckuss In Mist Hunter"),
    n("Darth Vader", True),
    n("4-LOM With Concussion Rifle"),
    n("Myn Kyneugh", True),
    n("Ysanne Isard", True),
    n("Stormtrooper Garrison"),
    n("Sense", qty=2),
    n("Control"),
    n("A Dark Time For The Rebellion"),
    n("According To My Design", True),
    n("Executor"),
    n("Mon Calamari"),
    n("A Dark Time For The Rebellion", True),
    n("Chimaera"),
    n("Gravity Shadow"),
    n("Broken Concentration", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance?"),
    n("Battle Order"),
    n("Imperial Detention", True),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("A Useless Gesture"),
    n("Fanfare", True),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = []
