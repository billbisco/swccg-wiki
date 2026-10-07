#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Leo Molitor.

Source: 2012NationalsDay1.pdf pages 40–41 (handwritten Dark / typed Light 2010 Xerox, 12 shields).
p40 Dark / p41 Light Name Leo Molitor dested Leo Molitor as written.
Username blank. Analog leftover generate empty dest as written.
Pack player-stubs/Leo_Molitor.wiki.
"""
from __future__ import annotations

PLAYER = "Leo Molitor"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 41
DS_PAGE = 40
LS_SCAN = "2012 US Nationals Day 1 Leo Molitor LS.png"
DS_SCAN = "2012 US Nationals Day 1 Leo Molitor DS.png"
LS_DECK_NAME = "Smugglers Blues"
DS_DECK_NAME = "Combat"
NOTE = "Handwritten Dark / typed Light 2010 Xerox. Name Leo Molitor dested Leo Molitor as written. Username blank."
LS_NOTE = (
    "Typed 2010 Xerox. Name Leo Molitor dested Leo Molitor as written. "
    "Username blank. LIGHT checked. Deck Name Smugglers Blues. Event Date 6/9/12 Event Name Nationals. "
    "Analog leftover generate empty dest as written. "
    "Watch Your Step/This Place Can Be A Little Rough empty dested Watch Your Step / This Place Can Be A Little Rough analog leftover Anderson. "
    "Anger, Fear, Agression dested Anger, Fear, Aggression True analog leftover Casey IN THE 60. "
    "Honor of the Jedi dested Honor Of The Jedi analog leftover Foth. "
    "Sai'torr Kal Fas dested analog leftover Lingrell True. "
    "Boshek dested BoShek True analog leftover. "
    "A Jedi's Concentration crossed dest Luke Skywalker, Strong In The Force True analog leftover TMW Hilbun. "
    "Captive Pursuit crossed dest Luke Skywalker, Rebel Hero True analog leftover Gemme x2. "
    "Medium Bulk Freighter crossed dest BoShek's Modified Freighter True analog leftover Jessica. "
    "luke with Lightsaber dested Luke With Lightsaber analog leftover Cullen. "
    "Millenium Falcon dested Millennium Falcon analog leftover. "
    "Chewie with Blaster rifle dested Chewie With Blaster Rifle analog leftover. "
    "Raltiir Freighter Captain dested Ralltiir Freighter Captain analog leftover. "
    "Han's Back dested as written leftover_xerox analog leftover Martin. "
    "Luke's Back dested leftover_xerox analog leftover Grant. Unique 60. Shields 3 slots 4–12 blank skip."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Leo Molitor dested Leo Molitor as written. "
    "Username blank. DARK checked. Deck Name Combat. Event Date 6/9/12 Event Name Nationals. "
    "Analog leftover generate empty dest as written. "
    "Let them make the first move dested Let Them Make The First Move analog leftover. "
    "Imperial Arrest Order & Secret Plans dested analog leftover Gogolen. "
    "Ni Chuba Na?? dested analog leftover Anderson True. "
    "Prepared Defenses dested analog leftover IN THE 60. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Jessica True. "
    "Vader dested Darth Vader True analog leftover x2. "
    "Kritk Keed Kak dested Kitik Keed'kak True analog leftover Devin. "
    "Darth Sir Lord Sidious crossed dest Lord Sidious True analog leftover Darth Sidious. "
    "Galen, Secret Apprentice dested as written leftover_xerox True analog leftover Casey. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi True analog leftover Casey. "
    "Dark Jedi Lightsaber True and empty kept separate analog leftover McCune. "
    "IG88 in IG 2000 dested IG-88 In IG-2000 analog leftover Kurten. "
    "O switch off dested Oh, Switch Off analog leftover Erwin. "
    "elis helrot dested Elis Helrot analog leftover Bordier. "
    "It's worse dested leftover_xerox analog leftover Fernando x2. "
    "K&D dested Knowledge And Defense analog leftover Cooleo IN THE 60. Unique 59 line 17 crossed skip. Shields 2 slots 3–12 blank skip."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine"),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("Honor Of The Jedi"),
    n("Squadron Assignments"),
    n("Sai'torr Kal Fas", True),
    n("Order To Engage"),
    n("Pulsar Skate"),
    n("Han's Heavy Blaster Pistol"),
    n("Melas", True),
    n("BoShek", True),
    n("Corellian Retort", True, qty=2),
    n("Luke Skywalker, Strong In The Force", True),
    n("Luke Skywalker, Rebel Hero", True, qty=2),
    n("Mantellian Savrip"),
    n("Out Of Nowhere"),
    n("Bacta Tank"),
    n("BoShek's Modified Freighter", True),
    n("Old Ben", qty=2),
    n("Kessel"),
    n("Corellian", qty=2),
    n("Blaster Proficiency"),
    n("Slight Weapons Malfunction"),
    n("Yotts Orren"),
    n("Medium Bulk Freighter", qty=2),
    n("Mirax Terrik"),
    n("Dash Rendar"),
    n("Outrider"),
    n("Red 10"),
    n("Legendary Starfighter"),
    n("Theron Nett"),
    n("Luke With Lightsaber"),
    n("Millennium Falcon"),
    n("Alter"),
    n("Choke"),
    n("Palace Raider"),
    n("Captain Han Solo"),
    n("LE-B0209 (Leebo)"),
    n("Local Defense"),
    n("Rug Hug"),
    n("Han's Back"),
    n("Kessel Run"),
    n("Patrol Craft", qty=2),
    n("Goo Nee Tay"),
    n("Han Solo"),
    n("Luke's Back"),
    n("Mercenary Armor"),
    n("Chewie With Blaster Rifle"),
    n("Ralltiir Freighter Captain"),
    n("Chewbacca"),
    n("The Signal"),
]
LS_SHIELDS = [
    n("Battle Plan", True),
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
]
LS_ADD = []

DS_START = "Let Them Make The First Move"
DS_CARDS = [
    n("Let Them Make The First Move"),
    n("Naboo: Theed Palace Generator Core"),
    n("Naboo: Theed Palace Generator"),
    n("Deep Hatred"),
    n("Imperial Arrest Order & Secret Plans"),
    n("Ni Chuba Na??", True),
    n("Blaster Rack", True),
    n("Prepared Defenses"),
    n("Coruscant: Chancellor's Office", True),
    n("Naboo: Theed Palace Docking Bay"),
    n("Juno Eclipse, Black Leader", True),
    n("Darth Vader, Betrayer Of Jedi", True),
    n("Darth Vader", True, qty=2),
    n("Kitik Keed'kak", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Darth Sidious", True),
    n("Galen, Secret Apprentice", True),
    n("Chokk"),
    n("Shada", True),
    n("Darth Maul"),
    n("Prince Xizor"),
    n("Royal Guard"),
    n("Boba Fett, Relentless Bounty Hunter", True),
    n("Grievous, Hunter Of Jedi", True),
    n("Maul's Electrobinoculars"),
    n("Force Pike"),
    n("Darth Vader's Lightsaber"),
    n("Naboo Blaster Rifle"),
    n("Dark Jedi Lightsaber", True),
    n("Dark Jedi Lightsaber"),
    n("Darth Maul's Double Lightsaber"),
    n("Galen's Lightsaber", True),
    n("Imperial-Class Star Destroyer", True),
    n("Black 2", True),
    n("Sentinel-Class Landing Craft"),
    n("Victory", True),
    n("Virago"),
    n("IG-88 In IG-2000"),
    n("Reactor Terminal"),
    n("Energy Wall"),
    n("Qui-Gon's End"),
    n("The Phantom Menace"),
    n("Establish Control"),
    n("Limited Resources", qty=2),
    n("Imperial Supply"),
    n("Oh, Switch Off"),
    n("Scanning Crew"),
    n("Dark Strike"),
    n("Dark Maneuvers"),
    n("Elis Helrot"),
    n("Sense"),
    n("Torture"),
    n("Twi'lek Advisor"),
    n("Evacuate"),
    n("It's Worse", qty=2),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Abyss", True),
    n("Battle Order", True),
]
DS_ADD = []
