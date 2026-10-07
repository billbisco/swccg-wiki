#!/usr/bin/env python3
"""2014 US Nationals Day 2 Xerox: Matt Sokol.

Source: Nationals-2014-day-2.pdf pages 3–4 (2010 form).
Name Sokol. Username blank. Facing p04 Name blank dests Matt Sokol.
"""
from __future__ import annotations

PLAYER = "Matt Sokol"
USERNAME = ""
STAGE = "Day 2"
PDF = "2014 US Nationals Day 2.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2014 US Nationals Day 2 p03 Matt Sokol LS.png"
DS_SCAN = "2014 US Nationals Day 2 p04 Matt Sokol DS.png"
NOTE = "Handwritten 2010 Xerox. Name Sokol dested Matt Sokol."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Sokol. Username blank. Deck name Light. "
    "QMC dested Quiet Mining Colony / Independent Operation. "
    "Path Revealed dested Path Of Least Resistance & Revealed. "
    "AFA dested Anger, Fear, Aggression. Houjix & Out of Nowhere dested Houjix & Out Of Nowhere. "
    "LTWW dested Let The Wookiee Win. HFTMF dested Heading For The Medical Frigate. "
    "All My Urchins & CC Celebration dested All My Urchins & Cloud City Celebration. "
    "Lando Calrissian, UH dested Lando Calrissian, Unlikely Hero. "
    "Saw Saw Banks dested Senator Jar Jar Binks. Harc Seff dested Harc Seff. "
    "CC sites dested Cloud City: Upper Plaza Corridor / West Gallery / North Corridor / "
    "Incinerator / Guest Quarters. 15 Shields written with dittos, no individual shields. "
    "Unique overcounts sheet-accurate (Rebel Barrier x3, Path Of Least Resistance x2, "
    "Let The Wookiee Win x2, Choke x2, Lando Calrissian, Unlikely Hero x2). (V) from checkbox. "
    "NO_DEST (2014 index): Gola."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name blank facing Sokol Light. Dest Matt Sokol. "
    "IO/IC dested Imperial Occupation / Imperial Control. "
    "Hoth Ice Plains dested Hoth: Ice Plains. AT-ATs dested AT-AT (V). "
    "Hoth: Mountains dested Hoth: Mountains. Hoth: 3rd marker dested Hoth: Defensive Perimeter. "
    "TTMG dested Target The Main Generator. MM & EO dested Masterful Move & Endor Occupation. "
    "ADTFTB dested A Dark Time For The Rebellion. WIAPN dested We're In Attack Position Now. "
    "YMSYL dested You May Start Your Landing. Ni Chuba Na dested Ni Chuba Na??. "
    "DTHACC dested Do They Have A Code Clearance?. Endor Shield dested Endor Shield. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "Mara with Stick dested Mara Jade With Lightsaber. Doctor E & PB dested Dr. Evazan & Ponda Baba. "
    "GMT dested Grand Moff Tarkin. DV DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Keder dested Keder The Black. Maul with Saber dested Darth Maul With Lightsaber. "
    "TOADL dested Wipe Them Out, All Of Them. Hoth Blockade dested Hoth Blockade. "
    "Victory dested Victory. 15 Shields written, no individual shields. "
    "Unique overcounts sheet-accurate (Conquest x2, Victory x2, Blizzard 4 x2, Trample x2, "
    "Stop Motion x2, A Dark Time For The Rebellion x2, Imperial Command x3, "
    "Imperial Decree x2, We're In Attack Position Now x2). (V) from checkbox. "
    "NO_DEST (2014 index): AT-AT (V)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Landing Claw"),
    n("Path Of Least Resistance & Revealed"),
    n("Path Of Least Resistance", qty=2),
    n("Anger, Fear, Aggression", True),
    n("Rebel Barrier", qty=3),
    n("Houjix & Out Of Nowhere"),
    n("Desperate Reach", True),
    n("Choke", qty=2),
    n("Dark Approach", True),
    n("Alternatives To Fighting"),
    n("Let The Wookiee Win", True, qty=2),
    n("Heading For The Medical Frigate", True),
    n("Ellorrs Madak", True),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Menace Fades"),
    n("All My Urchins & Cloud City Celebration"),
    n("Keeping The Empire Out Forever"),
    n("Beldon's Eye", True),
    n("Aayla Secura", True),
    n("Tawss Khaa"),
    n("Sergeant Edian", True),
    n("Leesub Sirln", True),
    n("Yoxgit"),
    n("Leia, Rebel Princess"),
    n("Caldera Righim"),
    n("Lobot", True),
    n("Chewbacca, Walking Carpet"),
    n("Leslomy Tacema", True),
    n("Tanus Spijek", True),
    n("Luke With Lightsaber"),
    n("Dash Rendar", True),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Kal'Falnl C'ndros"),
    n("Mirax Terrik"),
    n("Melas", True),
    n("Gola"),
    n("Han Solo, Innocent Scoundrel"),
    n("Kebyc", True),
    n("Foul Moudama"),
    n("Senator Jar Jar Binks"),
    n("Harc Seff", True),
    n("Trooper Utris M'toc", True),
    n("Overseer"),
    n("Lady Luck"),
    n("Booster In Pulsar Skate"),
    n("Errant Venture"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: West Gallery"),
    n("Cloud City: North Corridor"),
    n("Cloud City: Incinerator"),
    n("Cloud City: Guest Quarters"),
    n("Bespin"),
]
LS_SHIELDS = []
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth: Ice Plains", True),
    n("AT-AT", True),
    n("Hoth"),
    n("Hoth: Mountains"),
    n("Hoth: Defensive Perimeter"),
    n("Target The Main Generator"),
    n("AT-AT Cannon", True),
    n("Conquest", True, qty=2),
    n("Victory", qty=2),
    n("Flagship Executor"),
    n("Blizzard 1", True),
    n("Marquand In Blizzard 6"),
    n("Tempest 1"),
    n("Blizzard 2", True),
    n("Blizzard 4", qty=2),
    n("Prepared Defenses", True),
    n("Cold Feet", True),
    n("Trample", qty=2),
    n("Stop Motion", True, qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Walker Garrison"),
    n("Masterful Move & Endor Occupation"),
    n("Force Push", True),
    n("Imperial Command", qty=3),
    n("Alert My Star Destroyer!"),
    n("Hoth Blockade"),
    n("Wipe Them Out, All Of Them", True),
    n("Imperial Decree", True),
    n("Do They Have A Code Clearance?", True),
    n("No Escape"),
    n("Endor Shield", True),
    n("You May Start Your Landing"),
    n("Ni Chuba Na??"),
    n("Imperial Decree"),
    n("We're In Attack Position Now", qty=2),
    n("Garindan", True),
    n("U-3PO (Yoo-Threepio)"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Boba Fett"),
    n("Mara Jade With Lightsaber"),
    n("Dr. Evazan & Ponda Baba"),
    n("Admiral Piett"),
    n("Veers", True),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Keder The Black"),
    n("Darth Maul With Lightsaber"),
    n("ISB Sector Commander"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = []
DS_ADD = []
