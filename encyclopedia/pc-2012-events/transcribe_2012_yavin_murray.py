#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Tim Murray.

Source: Yavin42012.pdf pages 35–36.
p35 Dark typed 2010 Xerox / p36 Light typed 2010 Xerox.
Name Tim Murray dested Tim Murray analog leftover generate_2012_nats.py /
generate_2012_mpc.py CANON Timbod2003 / player-stubs/Tim_Murray.wiki.
Username timbod2003 dested USERNAME as written this sheet.
Pack player-stubs/Tim_Murray.wiki.
Do not dest as a new person.
Do not dest 2012 MPC Day 1 Tim Murray 60s again.
"""
from __future__ import annotations

PLAYER = "Tim Murray"
USERNAME = "timbod2003"
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 36
DS_PAGE = 35
LS_SCAN = "2012 Yavin 4 Regionals Tim Murray LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Tim Murray DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p35 Dark typed 2010 Xerox / p36 Light typed 2010 Xerox. "
    "Name Tim Murray dested Tim Murray analog leftover generate_2012_nats.py / "
    "generate_2012_mpc.py CANON Timbod2003 / player-stubs/Tim_Murray.wiki. "
    "Username timbod2003 dested USERNAME as written this sheet. "
    "Event Date 06/30/2012 Event Name Yavin IV 2012 dest Yavin 4 facing pair analog leftover Orthner. "
    "Deck Name Lightsaber Combat / Expendable Ewok's dested off article. "
    "Do not dest as a new person. Pack player-stubs/Tim_Murray.wiki. "
    "Do not dest 2012 MPC Day 1 Tim Murray 60s again."
)
LS_NOTE = (
    "Typed 2010 Xerox p36 Light. Name Tim Murray Username timbod2003. "
    "Event Date 06/30/2012 Event Name Yavin IV 2012 dest Yavin 4 facing pair. LIGHT checked. "
    "Rebel Strike Team/Garrison Destroyed dested Rebel Strike Team / Garrison Destroyed True analog leftover dual-title mpc murray. "
    "START dested from line 9 objective analog leftover dual-title. "
    "Ewok Spear dested analog leftover dest as written line 1. "
    "The Shield is Down dested The Shield Is Down True analog leftover dest as written slang. "
    "Ewok Sentry empty qty=2 consecutive lines 10/11 analog leftover consecutive. "
    "Ewok Tribesman empty qty=2 consecutive lines 12/13 analog leftover consecutive. "
    "Throw Me Another Charge empty qty=2 consecutive lines 14/15 analog leftover consecutive. "
    "Hingsight dested Hindsight True analog leftover dest as written slang. "
    "Endor: Dense Forrest dested Endor: Dense Forest analog leftover dest as written slang. "
    "Sound The Attack empty qty=2 consecutive lines 39/40 analog leftover consecutive. "
    "Explosive Charge empty qty=2 consecutive lines 41/42 analog leftover consecutive. "
    "Wesa Ready To Do Our-sa Part dested Wesa Ready To Do Our-Sa Part True analog leftover mpc murray. "
    "Wookie Guide dested Wookiee Guide analog leftover dest as written slang. "
    "Luke with Lightsaber dested Luke Skywalker With Lightsaber analog leftover dest as written slang TYPE_OVERRIDE. "
    "Shields 1–11 filled shield 12 empty skip analog leftover Dwyer. Unique 60 shields 11."
)
DS_NOTE = (
    "Typed 2010 Xerox p35 Dark. Name Tim Murray Username timbod2003. "
    "Event Date 06/30/2012 Event Name Yavin IV 2012 dest Yavin 4 facing pair. DARK checked. "
    "Let Them Make The First Move/At Last we will ... dested Let Them Make The First Move / At Last We Will Have Revenge analog leftover dual-title. "
    "START dested from line 1 analog leftover dual-title. "
    "Imperial Propoganda dested Imperial Propaganda True qty=2 consecutive lines 8/9 analog leftover dest as written slang. "
    "The Phantom Menace empty qty=2 consecutive lines 11/12 analog leftover consecutive. "
    "Force Field True qty=2 consecutive lines 13/14 analog leftover consecutive. "
    "Weapon of An Ungrateful Son dested Weapon Of An Ungrateful Son empty qty=2 consecutive lines 15/16 analog leftover dest as written slang. "
    "Operational As Planned True qty=2 consecutive lines 17/18 analog leftover consecutive. "
    "Lord Maul empty qty=3 consecutive lines 19/20/21 analog leftover consecutive dest qty at first. "
    "Dr. Evazam & Ponda Baba dested Dr. Evazan & Ponda Baba analog leftover dest as written combo slang. "
    "Darth Vader, Betrayer Of The Jedi empty qty=2 consecutive lines 24/25 analog leftover dest as written. "
    "The Empire's Back True qty=2 consecutive lines 35/36 analog leftover dest as written slang. "
    "Bob Fett in Slave I dested Boba Fett In Slave I True analog leftover dest as written slang. "
    "Ghhhk & Those Rebels Won't Escape Us dested analog leftover dest as written combo slang. "
    "Knowledge And Defense True dested analog leftover Anderson IN THE 60. "
    "Shields 1–11 filled shield 12 empty skip analog leftover Dwyer. Unique 60 shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Rebel Strike Team / Garrison Destroyed"
LS_CARDS = [
    n("Ewok Spear"),
    n("Rebel Gunrunner"),
    n("Strike Planning"),
    n("The Shield Is Down", True),
    n("Ewok Celebration"),
    n("Endor"),
    n("Heading For The Medical Frigate"),
    n("Endor: Back Door"),
    n("Rebel Strike Team / Garrison Destroyed", True),
    n("Ewok Sentry", qty=2),
    n("Ewok Tribesman", qty=2),
    n("Throw Me Another Charge", qty=2),
    n("Goo Nee Tay"),
    n("Deactivate The Shield Generator"),
    n("Hindsight", True),
    n("Endor: Bunker"),
    n("I Hope She's All Right", True),
    n("Endor: Dense Forest"),
    n("Lumat"),
    n("Endor: Ewok Village", True),
    n("Kazak"),
    n("Wicket", True),
    n("Wuta"),
    n("General Solo", True),
    n("Daughter Of Skywalker"),
    n("Chewbacca Of Kashyyyk"),
    n("General Crix Madine"),
    n("Graak"),
    n("I'm With You Too", True),
    n("Luke Skywalker, Rebel Scout", True),
    n("Liberty"),
    n("Redeemed Apprentice"),
    n("Home One"),
    n("Imperial Atrocity"),
    n("Slight Weapons Malfunction"),
    n("Sound The Attack", qty=2),
    n("Explosive Charge", qty=2),
    n("Romba"),
    n("Ewok Catapult"),
    n("Ewok Spearman"),
    n("Insertion Planning"),
    n("I Know"),
    n("Rebel Barrier"),
    n("Yub Yub!"),
    n("Let The Wookiee Win", True),
    n("Honor Of The Jedi"),
    n("Houjix"),
    n("Chief Chirpa", True),
    n("Wesa Ready To Do Our-Sa Part", True),
    n("Wookiee Guide"),
    n("Luke Skywalker With Lightsaber"),
    n("Tantive IV", True),
    n("Bright Hope", True),
    n("Ewok Rescue"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Aim High"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Do, Or Do Not", True),
    n("Affect Mind", True),
    n("Traffic Control", True),
    n("Wise Advice"),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("The Professor"),
]
LS_ADD = []

DS_START = "Let Them Make The First Move / At Last We Will Have Revenge"
DS_CARDS = [
    n("Let Them Make The First Move / At Last We Will Have Revenge"),
    n("Deep Hatred"),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Theed Palace Generator Core"),
    n("Trained In The Jedi Arts"),
    n("Blaster Rack", True),
    n("Jabba's Haven"),
    n("Imperial Propaganda", True, qty=2),
    n("Masterful Move"),
    n("The Phantom Menace", qty=2),
    n("Force Field", True, qty=2),
    n("Weapon Of An Ungrateful Son", qty=2),
    n("Operational As Planned", True, qty=2),
    n("Lord Maul", qty=3),
    n("Dr. Evazan & Ponda Baba"),
    n("Mara Jade, The Emperor's Hand"),
    n("Darth Vader, Betrayer Of Jedi", qty=2),
    n("P-59"),
    n("Emperor Palpatine"),
    n("Darth Sidious"),
    n("4-LOM With Concussion Rifle", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Image Of The Dark Lord", True),
    n("Young Fool"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Bossk In Hound's Tooth", True),
    n("The Empire's Back", True, qty=2),
    n("Maul Strikes"),
    n("Release Your Anger", True),
    n("Trophy Of A Kill"),
    n("Aurra Sing's Blaster Rifle"),
    n("Boba Fett In Slave I", True),
    n("Dengar In Punishing One"),
    n("Podracer Collision"),
    n("Imperial Barrier"),
    n("We Must Accelerate Our Plans"),
    n("Sense"),
    n("Vader's Lightsaber"),
    n("A Dark Time For The Rebellion", True),
    n("The Ebb Of Battle"),
    n("Weapon Levitation"),
    n("Force Push", True),
    n("Aurra Sing, Deadly Assassin"),
    n("Furry Furry"),
    n("Force Lightning"),
    n("Mara Jade's Lightsaber", True),
    n("Sidious' Lightsaber"),
    n("Nal Hutta"),
    n("Zuckuss In Mist Hunter"),
    n("According To My Design"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever"),
    n("Allegations Of Corruption"),
    n("Resistance", True),
    n("Weapon Of A Sith"),
    n("Oppressive Enforcement"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
]
DS_ADD = []
