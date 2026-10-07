#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Chris Gogolen.

Source: 2012mpcday1.pdf pages 75–76 (2010 form, 12 shields).
Name Chris Gogolen dested Chris Gogolen (generate_2013_mpc analog).
p75 Light Anger, Fear, Aggression. p76 Dark Endor Operations.
Do not dest as a new person. Pack player-stubs/Chris_Gogolen.wiki.
Do not rewrite 2013 leftovers (2013 PLAYER="Gogolen").
"""
from __future__ import annotations

PLAYER = "Chris Gogolen"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 75
DS_PAGE = 76
LS_SCAN = "2012 Match Play Championship Day 1 Chris Gogolen LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Chris Gogolen DS.png"
LS_DECK_NAME = "I'm out of interesting ideas"
DS_DECK_NAME = "Not quite Albany Ops"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Gogolen dested Chris Gogolen. "
    "Username blank. LIGHT checked. Event Date 02/11/12 Event Name MPC Main Event. "
    "Deck Name I'm out of interesting ideas. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Line 1 cropped off y0=h*0.188; dest unique 59 from lines 2–60. "
    "Anger fear agression dested Anger, Fear, Aggression True. "
    "Cmd Wedge dested Commander Wedge Antilles True. "
    "Obi wan's apparition dested Obi-Wan's Apparition True. "
    "Manuevering Flaps/Nick of Time dested Maneuvering Flaps / Nick Of Time. "
    "its not my fault dested It's Not My Fault! True x2. "
    "Cmd Luke dested Commander Luke Skywalker True x2. "
    "obi's hut dested Tatooine: Obi-Wan's Hut True. "
    "wesa got grand army dested Wesa Gotta Grand Army. "
    "zev sanesca dested Zev Senesca. "
    "hobbie dested Derek 'Hobbie' Klivian True. "
    "padme dested Padmé Naberrie True. "
    "home 1 dested Home One. "
    "lando, scoundrel dested Lando Calrissian, Scoundrel True. "
    "han chewie & falcon dested Han, Chewie, And The Falcon True x2. "
    "leia with blaster dested Leia With Blaster Rifle. "
    "control/tunnel vision dested Control & Tunnel Vision. "
    "Unique 59 (line 1 cropped). Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Chris Gogolen dested Chris Gogolen. "
    "Username blank. DARK checked. Event Date 02/11/12 Event Name 2012 MPC Main Event. "
    "Deck Name Not quite Albany Ops. "
    "Do not dest as a new person. Do not rewrite 2013 leftovers. "
    "Line 1 cropped off y0=h*0.188; dested Endor Operations / Imperial Outpost from analog "
    "(Deck Name Albany Ops + Endor bunker/landing platform/Endor/Prepared Defenses). "
    "Knowledge & Defense dested Knowledge And Defense True. "
    "imp arrest order/secret plans dested Imperial Arrest Order & Secret Plans. "
    "short range/wyb dested Short Range Fighters & Watch Your Back! x2. "
    "vader's shuttle dested Vader's Personal Shuttle True. "
    "bliz scout 1 dested Blizzard Scout 1 True. "
    "imp propaganda dested Imperial Propaganda True. "
    "at-st cannon dested AT-ST Cannon (True lookup stole AT-AT Cannon). "
    "at-st dual cannon dested AT-ST Dual Cannon True. "
    "major turr phenir dested Major Turr Phennir. "
    "baron fel dested Baron Soontir Fel. "
    "lt arnet dested Lieutenant Arnet. "
    "lt watts dested Lieutenant Watts. "
    "sfs 93 laser cannon dested SFS L-s9.3 Laser Cannons. "
    "adm ozzel dested Admiral Ozzel. "
    "something special dested Something Special Planned For Them True. "
    "you cannot hide dested You Cannot Hide Forever True. "
    "oppressive dested Oppressive Enforcement. "
    "i find your lack of faith dested I Find Your Lack Of Faith Disturbing True. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Communing"),
    n("Master Kenobi"),
    n("Colo Claw Fish"),
    n("Maneuvering Flaps / Nick Of Time"),
    n("Commander Wedge Antilles", True),
    n("Rebel Artillery"),
    n("Obi-Wan's Apparition", True),
    n("Attack Pattern Delta", True),
    n("Kashyyyk: Wookiee Haven"),
    n("It's Not My Fault!", True, qty=2),
    n("Rogue 1"),
    n("Commander Luke Skywalker", True, qty=2),
    n("Corran Horn"),
    n("Dual Laser Cannon", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Punch It!"),
    n("Wesa Gotta Grand Army"),
    n("Yoda, Great Warrior"),
    n("Imperial Atrocity", True, qty=2),
    n("Kashyyyk: Forest Depths"),
    n("Rogue 2"),
    n("Corporal Beezer", True),
    n("Kashyyyk: Sacred Forest"),
    n("Sense", qty=2),
    n("Mechanical Failure"),
    n("Rogue 4"),
    n("Rogue 3"),
    n("Zev Senesca"),
    n("Inconsequential Barriers"),
    n("Control & Tunnel Vision"),
    n("Let The Wookiee Win", True, qty=2),
    n("Hindsight", True),
    n("Precise Hit", True),
    n("Derek 'Hobbie' Klivian", True),
    n("Tunnel Vision"),
    n("Echo Base Garrison"),
    n("Wyron Serper", True),
    n("Padmé Naberrie", True),
    n("Home One"),
    n("Menace Fades"),
    n("Rebel Leadership", True, qty=2),
    n("Rebel Gunrunner"),
    n("Lando Calrissian, Scoundrel", True),
    n("Home One: War Room"),
    n("Rebel Barrier", qty=2),
    n("Han, Chewie, And The Falcon", True, qty=2),
    n("Admiral Ackbar", True),
    n("Use The Force", qty=2),
    n("Leia With Blaster Rifle"),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Don't Do That Again", True),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Knowledge And Defense", True),
    n("Endor: Bunker"),
    n("Endor: Landing Platform"),
    n("Endor"),
    n("Prepared Defenses"),
    n("Imperial Arrest Order & Secret Plans"),
    n("Inconsequential Losses", True),
    n("Establish Control", True),
    n("Sneak Attack", True, qty=2),
    n("Cold Feet", True),
    n("Defensive Fire", True, qty=2),
    n("Imperial Artillery"),
    n("Limited Resources"),
    n("AT-ST Cannon"),
    n("Fighters Coming In", qty=2),
    n("Tempest Scout 2"),
    n("Corporal Drelosyn"),
    n("Saber 2"),
    n("Establish Secret Base", True),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Tempest Scout 3"),
    n("Vader's Personal Shuttle", True),
    n("Endor Shield", True),
    n("Sergeant Irol", True),
    n("Blizzard Scout 1", True),
    n("Imperial Propaganda", True),
    n("Saber 1"),
    n("Sergeant Barich"),
    n("Major Marquand"),
    n("Imperial Barrier"),
    n("AT-ST Dual Cannon", True),
    n("DS-61-2"),
    n("Major Turr Phennir"),
    n("Endor: Back Door"),
    n("Sullust"),
    n("Trample"),
    n("Baron Soontir Fel"),
    n("Punishing One", True),
    n("Tempest Scout 1"),
    n("Black 2", True),
    n("Tempest Scout 6"),
    n("Combat Response", True),
    n("Lieutenant Arnet"),
    n("Wounded Warrior"),
    n("Tempest Scout 5"),
    n("Darth Vader", True),
    n("Aratech Corporation", True),
    n("Fondor"),
    n("Lieutenant Watts"),
    n("SFS L-s9.3 Laser Cannons"),
    n("Admiral Ozzel"),
    n("Ominous Rumors"),
    n("Dengar", True),
    n("Something Special Planned For Them", True),
    n("General Nevar", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = []
