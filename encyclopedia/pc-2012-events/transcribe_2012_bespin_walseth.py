#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Mark Walseth.

Source: 2012BespinRegionals.pdf pages 37–38.
p37 Light typed 2010 Xerox / p38 Dark typed 2010 Xerox.
Name Walseth dested Mark Walseth analog leftover generate_2012_nats.py CANON /
player-stubs/Mark_Walseth.wiki / Walseth.wiki redirect.
Username blank. Pack player-stubs/Mark_Walseth.wiki.
Do not dest as a new person Walseth. Do not dest 2012 Nats Day 1 Mark Walseth 60s again.
Do not dest 2013 Worlds Day 2 Walseth 60s again.
"""
from __future__ import annotations

PLAYER = "Walseth"
USERNAME = ""
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 37
DS_PAGE = 38
LS_SCAN = "2012 Bespin Regionals Mark Walseth LS.png"
DS_SCAN = "2012 Bespin Regionals Mark Walseth DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p37 Light typed 2010 Xerox / p38 Dark typed 2010 Xerox. "
    "Name Walseth dested Mark Walseth analog leftover generate_2012_nats.py CANON / "
    "player-stubs/Mark_Walseth.wiki / Walseth.wiki redirect. Username blank. "
    "Event Date blank both dest both as Bespin facing pair analog leftover Cooleo. "
    "Deck Name Liberate Mains / Endor Ops dested off article. "
    "Do not dest as a new person Walseth. Do not dest 2012 Nats Day 1 Mark Walseth 60s again. "
    "Do not dest 2013 Worlds Day 2 Walseth 60s again. "
    "Pack player-stubs/Mark_Walseth.wiki."
)
LS_NOTE = (
    "Typed 2010 Xerox p37 Light. Name Walseth dested Mark Walseth. Username blank. "
    "LIGHT checked. Event Date blank. Deck Name Liberate Mains dested off article. "
    "Yavin 4 dested analog leftover nats Walseth. "
    "Yavin 4: Massassi Headquarters dested analog leftover nats Walseth. "
    "Careful Planning True dested Careful Planning (V) analog leftover nats Walseth. "
    "Yavin 4: Throne Room dested Yavin 4: Massassi Throne Room analog leftover nats Walseth. "
    "Master Qui-Gon True lines 13–14 dest qty=2 at first. "
    "Luke Skywalker, Strong In The Force True lines 15–16 dest qty=2 at first. "
    "Lando Calrissian, Scoundrel empty lines 19–20 dest qty=2 at first. "
    "Chewbacca, Protector dested analog leftover TYPE_OVERRIDE chewie, protector. "
    "Han, Chewie, in the Millennium Falcon dested Han, Chewie, And The Falcon analog leftover nats Walseth. "
    "Obi-Wan in Radiant IV dested Obi-Wan In Radiant VII analog leftover 2014 mpc. "
    "Booster's Star Destroyer True lines 28–30 dest qty=3 unique overcount analog leftover TYPE_OVERRIDE. "
    "Vibroaxe crossed dest Chewbacca's Bowcaster analog leftover crossed-with-replacement. "
    "We Wish To Board At Once empty lines 38–41 dest qty=4 at first. "
    "Rycar Ryjar dested Rycar Ryjerd analog leftover nats Walseth. "
    "Merc Sunlet dested Mercenary Sunset analog leftover TYPE_OVERRIDE. "
    "Restore Freedom To The Galaxy True dested analog leftover virtual-only. "
    "Anger Fear Aggression dested Anger, Fear, Aggression True analog leftover nats Walseth IN THE 60. "
    "A Tragedy Has Occured dested A Tragedy Has Occurred analog leftover nats Walseth. "
    "Shield 12 Chasm dested analog leftover extra S clip. Unique 60 shields 12."
)
DS_NOTE = (
    "Typed 2010 Xerox p38 Dark. Name Walseth dested Mark Walseth. Username blank. "
    "DARK checked. Event Date blank. Deck Name Endor Ops dested off article. "
    "EOPS dested Endor Operations / Imperial Outpost analog leftover 2013 Worlds Walseth. "
    "Endor: Landing Platform dested Endor: Landing Platform (Docking Bay) analog leftover 2013 Worlds Walseth. "
    "You Cannot Hide Forever / Mob Points dested You Cannot Hide Forever & Mobilization Points analog leftover 2013 Worlds Walseth. "
    "Crossed line 13 dest Alter True analog leftover crossed-with-replacement. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover 2013 Worlds Walseth. "
    "The Mandalorian, Father Of Fett dested Jango Fett, The Assassin analog leftover 2013 Worlds Walseth. "
    "Galen's Fighter dested Rogue Shadow analog leftover 2013 Worlds Walseth. "
    "Vader's Shuttle dested Vader's Personal Shuttle analog leftover 2013 Worlds Walseth. "
    "Sneak Attack True lines 39–40 dest qty=2 at first. "
    "Crossed line 41 dest Fighters Coming In analog leftover crossed-with-replacement; line 59 same empty dest qty=2 at first analog leftover non-consecutive. "
    "Imperial Command empty lines 42–44 dest qty=3 at first. "
    "Short Range Fighters & Watch Your Back! empty lines 45–47 dest qty=3 analog leftover Bespin Mike. "
    "Imperial Arrest Order crossed dest Offer as written analog leftover empty. "
    "Knowl + def dested Knowledge And Defense True analog leftover nats Hanson IN THE 60. "
    "Do They Have a Code Clearance dested Do They Have A Code Clearance? analog leftover nats Walseth. "
    "Shield 12 We'll Let Fate dested We'll Let Fate-a Decide, Huh? analog leftover extra S clip / 2013 Worlds Walseth. Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Careful Planning"
LS_CARDS = [
    n("Yavin 4"),
    n("Yavin 4: Massassi Headquarters"),
    n("Careful Planning", True),
    n("Strike Planning"),
    n("Luke, Trust Me", True),
    n("Quick Draw", True),
    n("Yavin 4: War Room", True),
    n("Yavin 4: Massassi Throne Room"),
    n("Kashyyyk: Forest Depths", True),
    n("Senator Mon Mothma", True),
    n("General Solo", True),
    n("Mace Windu, Master Of The Order", True),
    n("Master Qui-Gon", True, qty=2),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Princess Leia, Lost Scion", True),
    n("Boushh"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Chewbacca, Protector", True),
    n("Ki-Adi-Mundi", True),
    n("Corran Horn"),
    n("Booster Terrik", True),
    n("Mirax Terrik"),
    n("Han, Chewie, And The Falcon"),
    n("Obi-Wan In Radiant VII", True),
    n("Booster's Star Destroyer", True, qty=3),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Chewbacca's Bowcaster"),
    n("Han's Blaster Pistol", True),
    n("Leia's Blaster Rifle"),
    n("Han's Toolkit"),
    n("We Wish To Board At Once", qty=4),
    n("I Know"),
    n("Don't Get Cocky"),
    n("Life Debt"),
    n("Han's Back", True),
    n("Luke's Back", True),
    n("Leia's Back", True),
    n("A Few Maneuvers"),
    n("Sai'torr Kal Fas", True),
    n("Rycar Ryjerd", True),
    n("Draw Their Fire"),
    n("Mercenary Sunset", True),
    n("Meditation"),
    n("Plastoid Armor", True),
    n("Menace Fades"),
    n("I Can't Believe He's Gone", True),
    n("Hindsight", True),
    n("Massassi Base Sentry", True),
    n("Restore Freedom To The Galaxy", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Do, Or Do Not"),
    n("Let's Keep A Little Optimism Here"),
    n("Planetary Defenses"),
    n("Your Insight Serves You Well"),
    n("The Professor"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Aim High"),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
]
LS_ADD = []

DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Endor"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Lone Pilot", True),
    n("Kuat"),
    n("DS-61-2"),
    n("Black 2", True),
    n("You Cannot Hide Forever & Mobilization Points"),
    n("Wakeelmui"),
    n("Dantooine"),
    n("Endor: Back Door"),
    n("Alter", True),
    n("General Nevar", True),
    n("General Tagge", True),
    n("Admiral Ozzel"),
    n("Juno Eclipse, Black Leader", True),
    n("Darth Vader", True),
    n("Zuckuss", True),
    n("Emperor Palpatine"),
    n("Dengar", True),
    n("Jango Fett, The Assassin", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Lieutenant Watts"),
    n("Major Marquand"),
    n("Sergeant Barich"),
    n("Sergeant Irol", True),
    n("Tempest Scout 1"),
    n("Tempest Scout 2"),
    n("Tempest Scout 3"),
    n("Tempest Scout 5"),
    n("Tempest Scout 6"),
    n("Punishing One", True),
    n("Rogue Shadow", True),
    n("Vader's Personal Shuttle", True),
    n("Mist Hunter", True),
    n("Slave I, Symbol Of Fear", True),
    n("Victory", True),
    n("Sneak Attack", True, qty=2),
    n("Fighters Coming In", qty=2),
    n("Imperial Command", qty=3),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Sith Fury", True),
    n("According To My Design", True),
    n("A Dark Time For The Rebellion", True),
    n("Presence Of The Force"),
    n("Crossfire", True),
    n("Endor Shield", True),
    n("Combat Response", True),
    n("Aratech Corporation", True),
    n("Offer"),
    n("Establish Secret Base", True),
    n("Ominous Rumors"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("A Useless Gesture"),
    n("Do They Have A Code Clearance?"),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Imperial Detention"),
    n("Battle Order"),
    n("Fanfare"),
    n("Come Here You Big Coward"),
    n("Abyss"),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
