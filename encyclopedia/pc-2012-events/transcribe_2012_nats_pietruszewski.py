#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Jake Pietruszewski.

Source: 2012NationalsDay1.pdf pages 60–61 (handwritten 2010 Xerox, 12 shields).
p60 Light / p61 Dark Name Jake Pietruszewski Username jake.irish dested Jake Pietruszewski analog leftover empty.
Pack player-stubs/Jake_Pietruszewski.wiki.
"""
from __future__ import annotations

PLAYER = "Jake Pietruszewski"
USERNAME = "jake.irish"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 60
DS_PAGE = 61
LS_SCAN = "2012 US Nationals Day 1 Jake Pietruszewski LS.png"
DS_SCAN = "2012 US Nationals Day 1 Jake Pietruszewski DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Jake Pietruszewski dested Jake Pietruszewski analog leftover empty. "
    "Username jake.irish. Event Date 6/10/12 Event Name US Nationals. Do not dest as Jake Nelson."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Jake Pietruszewski dested Jake Pietruszewski analog leftover empty. "
    "Username jake.irish. LIGHT checked. Event Date 6/10/12 Event Name US Nationals. "
    "Deck Name Fairy Princess Profit stays off the article. "
    "LS_START You Can Either Profit / Or Be Destroyed dested You Can Either Profit By This... / Or Be Destroyed analog leftover Olson. "
    "Han dested Han Solo True analog leftover Olson. "
    "AFA dested Anger, Fear, Aggression True analog leftover Cooleo IN THE 60. "
    "Luke, Rebel Hero dested Luke Skywalker, Rebel Hero True analog leftover Molitor. "
    "Luke w/ saber dested Luke With Lightsaber analog leftover Jake Nelson. "
    "Chewie Protector dested Chewbacca, Protector analog leftover Olson. "
    "Yutani w/ blaster cannon dested YT-1300 Transport True leftover_xerox dest-as-written. "
    "Senator Amidala dested Senator Padmé Amidala True analog leftover Mark Peterson. "
    "Owen + Beru Lars dested Owen Lars & Beru Lars analog leftover Ojala. "
    "Obi-Wan Crazy Wizard dested Obi-Wan, Crazy Old Wizard True analog leftover Ojala. "
    "Commando Training combo dested Commando Training & K'lor'slug True analog leftover McCune. "
    "Armed + Krayt dested Armed And Dangerous & Krayt Dragon Howl True analog leftover Nelson. "
    "Odin Nesloor / I Stand dested Odin Nesloor & First Aid True analog leftover McCune. "
    "Shields 7–12 blank skip. Unique 60. Shields 6."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Jake Pietruszewski dested Jake Pietruszewski analog leftover empty. "
    "Username jake.irish. DARK checked. Event Date 6/10/12 Event Name US Nationals. "
    "Deck Name Jabba is a sexy beast stays off the article. "
    "DS_START Court Of The Vile Gangster / I Shall Enjoy Watching You Die analog leftover 2014 Worlds. "
    "Audience Chambers dested Jabba's Palace: Audience Chamber analog leftover Olson. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Mara-Freaking-Jade w/ stick dested Mara Jade With Lightsaber True analog leftover Jan. "
    "IG-88 w/ Riot Gun dested IG-88 With Riot Gun analog leftover Alden. "
    "Trapdoor dested Trap Door leftover_xerox dest-as-written x3 unique overcount. "
    "Dengar IP1 dested Dengar In Punishing One analog leftover Brady. "
    "Gela Yeens dested Gela Yeens True analog leftover Ojala. "
    "Shield Coward dested Come Here You Big Coward True analog leftover. "
    "Shields 7–12 blank skip. Unique 60. Shields 6."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han Solo", True),
    n("Heading For The Medical Frigate"),
    n("Declaration Of Rebellion", True),
    n("Seeking An Audience", True),
    n("Rycar Ryjerd", True),
    n("Anger, Fear, Aggression", True),
    n("Luke Skywalker, Rebel Hero", True),
    n("Luke With Lightsaber"),
    n("Master Luke", True),
    n("Chewbacca, Protector"),
    n("Leia, Optimistic Leader", True, qty=2),
    n("YT-1300 Transport", True),
    n("Padmé Naberrie", True),
    n("Blind Jedi", True, qty=2),
    n("Yoda, Great Warrior", True, qty=2),
    n("Lando With Vibro-Ax"),
    n("Han Solo, Courageous Smuggler", True),
    n("Senator Padmé Amidala", True),
    n("Bail Organa", True),
    n("Owen Lars & Beru Lars"),
    n("Ben Kenobi"),
    n("Obi-Wan Kenobi", True),
    n("Obi-Wan, Crazy Old Wizard", True),
    n("Tatooine Utility Belt", True),
    n("Jedi Lightsaber", True),
    n("Jedi Lightsaber"),
    n("Tatooine: Slave Quarters", True),
    n("Yavin 4: Massassi War Room", True),
    n("Field Dressing", True),
    n("I Hope She's All Right", True),
    n("Draw Their Fire"),
    n("Commando Training & K'lor'slug", True),
    n("Leia Of Alderaan", True),
    n("Our Most Desperate Hour", True),
    n("Luke's Ultimatum", True),
    n("Blaster Proficiency"),
    n("Nabrun Leids", qty=3),
    n("Tunnel Vision", qty=3),
    n("A Jedi's Resilience"),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Odin Nesloor & First Aid", True),
    n("Jedi Presence", qty=3),
    n("Sense", qty=2),
    n("Old Ben", qty=2),
    n("Protector"),
    n("It's Not My Fault"),
]
LS_SHIELDS = [
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Traffic Control", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Court Of The Vile Gangster / I Shall Enjoy Watching You Die"
DS_CARDS = [
    n("Court Of The Vile Gangster / I Shall Enjoy Watching You Die"),
    n("Jabba's Palace: Audience Chamber"),
    n("Jabba's Palace: Dungeon"),
    n("Great Pit Of Carkoon"),
    n("Knowledge And Defense", True),
    n("Prepared Defenses"),
    n("Jabba's Haven", True),
    n("Jabba's Influence", True),
    n("Power Of The Hutt"),
    n("Jabba The Hutt", True),
    n("Mara Jade With Lightsaber", True),
    n("Boba Fett"),
    n("Hidden Weapons"),
    n("IG-88 With Riot Gun"),
    n("M'ilyoon Olith"),
    n("Trap Door", qty=3),
    n("Feltipern Trevagg"),
    n("You Swindled Me!"),
    n("Ephant Mon"),
    n("Rancor Pit"),
    n("Barne Malar"),
    n("IG-88 In IG-2000"),
    n("Rodian", True, qty=2),
    n("Gailid"),
    n("Cloud City Engineer"),
    n("Barge: Passenger Deck"),
    n("Jabba's Space Cruiser", True),
    n("Dengar In Punishing One"),
    n("Bossk In Hound's Tooth"),
    n("Zuckuss In Mist Hunter"),
    n("All Wrapped Up"),
    n("Nal Hutta"),
    n("Hutt Bounty", True),
    n("Hutt Influence", True),
    n("Thok & Thug"),
    n("Scum And Villainy"),
    n("Jabba's Sail Barge"),
    n("Dengar With Blaster Carbine", True),
    n("Jabba's Palace"),
    n("Danz Borin", True),
    n("It's Worse", True),
    n("Chokk"),
    n("Snoova"),
    n("Trinto Duaba"),
    n("Salacious Crumb"),
    n("4-LOM With Rifle", True),
    n("Gela Yeens", True),
    n("Boelo"),
    n("Rancor"),
    n("Boba Fett In Slave I"),
    n("Limited Resources"),
    n("Ponda Baba", True),
    n("Pote Snitkin"),
    n("Boba Fett, Bounty Hunter"),
    n("Double Back"),
    n("Uncertain Is The Future"),
    n("We Have A Prisoner"),
]
DS_SHIELDS = [
    n("There Is No Try", True),
    n("Secret Plans", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Come Here You Big Coward", True),
    n("Imperial Detention", True),
]
DS_ADD = []
