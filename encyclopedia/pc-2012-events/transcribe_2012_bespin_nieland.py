#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox: Mitch N. dested Mitch Nieland.

Source: 2012BespinRegionals.pdf pages 1–2.
p01 Dark handwritten 2010 Xerox Deck Name ROPS. p02 Light notebook dump QMC.
Name Mitch N. dested Mitch Nieland analog leftover 2012 Nats CANON /
player-stubs/Mitch_Nieland.wiki. Username blank. Date 7/14/12.
Do not dest as Mitch Wieland. Do not dest 2012 Nats / 2014 Worlds Nieland 60s again.
"""
from __future__ import annotations

PLAYER = "Mitch Nieland"
USERNAME = ""
STAGE = ""
PDF = "2012 Bespin Regionals.pdf"
LS_PAGE = 2
DS_PAGE = 1
LS_SCAN = "2012 Bespin Regionals Mitch Nieland LS.png"
DS_SCAN = "2012 Bespin Regionals Mitch Nieland DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p01 Dark handwritten 2010 Xerox / p02 Light notebook dump. "
    "Name Mitch N. dested Mitch Nieland analog leftover 2012 Nats CANON / "
    "player-stubs/Mitch_Nieland.wiki. Username blank. Date 7/14/12 Event 2012 Bespin Regional. "
    "LIGHT/DARK empty dest Dark from Deck Name ROPS / Light from QMC notebook. "
    "Do not dest as Mitch Wieland. Do not dest 2012 Nats / 2014 Worlds Nieland 60s again."
)
LS_NOTE = (
    "Notebook dump p02 Light. Name Mitch N. dested Mitch Nieland. Username blank. "
    "QMC dested Quiet Mining Colony / Independent Operation analog leftover 2012 Nats Nieland. "
    "Cloud City: GQ dested Cloud City: Guest Quarters analog leftover nats nieland. "
    "Heading For Meet Brigade dested Heading For The Medical Frigate analog leftover. "
    "Beldon's Eye (V) dested Beldon's Eye True. Harc Seff (V) dested Harc Seff True. "
    "Off The Edge dested Off The Edge analog leftover nats nieland. "
    "Qui-Gon / Obi / Luke w saber dested Qui-Gon Jinn With Lightsaber / Obi-Wan With Lightsaber / Luke With Lightsaber analog leftover nats nieland. "
    "Lando's not a system dested Lando's Not A System, He's A Man analog leftover. "
    "OOC/TT dested Out Of Commission & Transmission Terminated analog leftover nats nieland combo. "
    "Alternative to Fighting dested Alternatives To Fighting analog leftover nats nieland. "
    "Kal'Falnl dested Kal'Falnl C'ndros analog leftover nats nieland. "
    "Booster in Skate dested Booster In Pulsar Skate analog leftover Kafer. "
    "Tangus Spijek dested Tanus Spijek True analog leftover nats nieland. "
    "Leebo dested LE-BO2D9 (Leebo) True analog leftover. "
    "Doets dested Kebyc analog leftover nats nieland. "
    "HICF dested Han, Chewie, And The Falcon analog leftover nats nieland. "
    "Spiren dested Spiral analog leftover nats nieland. "
    "Shields on other side dested empty skip. Unique 58 sheet-accurate shields 0."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p01 Dark. Name Mitch N. dested Mitch Nieland. Username blank. "
    "LIGHT/DARK empty dest Dark from Deck Name ROPS. "
    "Ralltiir Operations / Skeet dested Ralltiir Operations / In The Hands Of The Empire analog leftover 2012 Nats Shannon. "
    "Ni Chuba Na?? dested Ni Chuba Na? analog leftover. "
    "The Mandalorian, Father Of Fett dested Jango Fett, The Assassin analog leftover Atkin. "
    "Darth Maul with Lightsaber dested Darth Maul With Lightsaber analog leftover. "
    "Darth Vader, Dark Lord Of The sith dested Darth Vader, Dark Lord Of The Sith. "
    "Lt. Commander Arden dested Lieutenant Commander Arden analog leftover. "
    "Imbalance & Kitran Strider dested Imbalance & Kintan Strider analog leftover Massung combo. "
    "Darth Vader, Betrayor of Jedi dested Darth Vader, Betrayer Of Jedi analog leftover. "
    "Colonol David Jon dested Colonel Davod Jon analog leftover Nathan. "
    "Ice Heart dested Ysanne Isard analog leftover 2013 Alderaan Atkin. "
    "Imperial Command empty lines 25 and 41 dest qty=2 at first occurrence. "
    "He Hasnt Come Back yet dested He Hasn't Come Back Yet analog leftover. "
    "Masterful Move & Endor Occupation dested combo analog leftover. "
    "<> Spaceport Street / Docking Bay / Prefect's Office dested without marker. "
    "Slave 1 dested Slave I, Symbol Of Fear analog leftover Atkin. "
    "Knowledge and Defense True IN THE 60. Unique 60 shields 12 sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate"),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("Wokling"),
    n("Off The Edge"),
    n("Imperial Atrocity", qty=2),
    n("Path Of Least Resistance", qty=3),
    n("Cloud City: Carbonite Chamber"),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Overseer"),
    n("Harc Seff", True),
    n("Luke With Lightsaber", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Corran Horn"),
    n("Lando's Not A System, He's A Man"),
    n("Lando Calrissian", True),
    n("Dodge"),
    n("Clash Of Sabers", qty=2),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("Projection Of A Skywalker"),
    n("Kessel"),
    n("Leia, Rebel Princess"),
    n("Alternatives To Fighting", qty=3),
    n("Landing Claw"),
    n("Kal'Falnl C'ndros"),
    n("Tantive IV", True),
    n("BoShek", True),
    n("Rebel Barrier"),
    n("It Could Be Worse"),
    n("Narrow Escape", qty=2),
    n("Booster In Pulsar Skate"),
    n("Houjix & Out Of Nowhere"),
    n("Tanus Spijek", True),
    n("Scramble"),
    n("LE-BO2D9 (Leebo)", True),
    n("Kebyc"),
    n("Lando Calrissian, Scoundrel"),
    n("Han, Chewie, And The Falcon"),
    n("Pucumir Thryss"),
    n("Spiral"),
    n("Cloud City Celebration"),
    n("Cloud City: North Corridor"),
]
LS_SHIELDS = []
LS_ADD = []

DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Ralltiir"),
    n("Prepared Defenses"),
    n("Ni Chuba Na?", True),
    n("Endor Shield", True),
    n("Insignificant Rebellion", True),
    n("Arica"),
    n("Jango Fett, The Assassin"),
    n("Zuckuss In Mist Hunter"),
    n("Ghhhk"),
    n("Emperor's Personal Shuttle"),
    n("Close Call", True),
    n("Darth Maul With Lightsaber"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Grand Moff Tarkin", True),
    n("Search And Destroy"),
    n("Lieutenant Commander Arden"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Outflank", True),
    n("Imbalance & Kintan Strider"),
    n("Blizzard 1", True),
    n("Garindan", True, qty=2),
    n("Imperial Command", qty=2),
    n("Tempest 1"),
    n("Blizzard 4", True),
    n("Imperial Barrier"),
    n("Darth Vader, Betrayer Of Jedi"),
    n("Blizzard 2", True),
    n("General Veers", True),
    n("General Nevar"),
    n("Admiral Ozzel"),
    n("Colonel Davod Jon"),
    n("Boba Fett, Prepared Hunter"),
    n("Grand Admiral Thrawn"),
    n("Ysanne Isard"),
    n("Janus Greejatus"),
    n("Emperor Palpatine"),
    n("Imperial Justice", True),
    n("He Hasn't Come Back Yet"),
    n("Masterful Move & Endor Occupation"),
    n("Sonic Bombardment", True, qty=2),
    n("Victory"),
    n("Endor"),
    n("Cloud City: Security Tower", True),
    n("Spaceport Street"),
    n("Spaceport Docking Bay"),
    n("Spaceport Prefect's Office"),
    n("Ralltiir: Spaceport Financial District"),
    n("Kashyyyk"),
    n("Image Of The Dark Lord", True),
    n("Slave I, Symbol Of Fear"),
    n("Where Are You Taking This Thing?"),
    n("Special Delivery", True),
    n("Something Special Planned For Them", True),
    n("Imperial Propaganda", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Oppressive Enforcement"),
    n("After Her", True),
    n("Secret Plans"),
    n("Firepower", True),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
]
DS_ADD = []
