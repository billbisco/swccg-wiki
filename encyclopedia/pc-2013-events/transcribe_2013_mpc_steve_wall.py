#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Steve Wall Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Steve Wall"
USERNAME = "w@nd3r-b0b"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 112
DS_PAGE = 111
LS_SCAN = "2013 Match Play Championship p112 Steve Wall LS.png"
DS_SCAN = "2013 Match Play Championship p111 Steve Wall DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Steve Wall. Username w@nd3r-b0b. Light. Deck title WYS. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough (Decipher; (V) unchecked). "
    "Ralltiir Freighter Captain dittos x9. Chewie w/ Blaster Rifle dested Chewie With Blaster Rifle. "
    "Lando w/ Blaster Pistol dested Lando With Blaster Pistol. LE-BO2D9 dested LE-BO2D9 (Leebo). "
    "BoShek Brash Smuggler dested BoShek, Brash Smuggler. Han w/ Heavy Blaster dested Han With Heavy Blaster Pistol. "
    "Han Solo, CS dested Han Solo, Courageous Smuggler. LS, STTF dested Son Of Skywalker. "
    "Rycar Ryjerd (V). Smuggler's Blues (V). Projection of Skywalker dested Projection Of A Skywalker. "
    "Bargaining Table as written. An Unusual Amount dested An Unusual Amount Of Fear. "
    "Nar Shaddaa Wind dested Nar Shaddaa Wind Chimes. The Bith dested The Bith Shuffle. "
    "Punch It dested Punch It!. YT-1300 Transport (V). Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "BoShek's Ship dested BoShek's Modified Light Freighter. Fifle dested Spiral. "
    "Tat Docking Bay dested Tatooine: Docking Bay 94. Tat Cantina dested Tatooine: Cantina. "
    "Tat dested Tatooine. Your Ship dested Yavin Sentry. No Questions dested No Questions Asked. "
    "Battle Plan (V). Wise Advice (V). Ultimatum (V). Do or Do Not dested Do, Or Do Not (V). "
    "Your Insight dested Your Insight Serves You Well (V). "
    "Form left column reprints 37–38 on lines 39–40 are The Bith Shuffle ditto and Punch It!. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Steve Wall. Username w@nd3r-b0b. Dark. Deck title Hunt Down. "
    "Hunt Down and... (V) dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe (V). "
    "Alter + Collateral Damage dested Alter & Collateral Damage. "
    "Sense + Uncertain is the Future dested Sense & Uncertain Is The Future. "
    "Galen's light saber dested Galen's Lightsaber. "
    "Cyborg Commander's Lightsaber dested Grievous' Lightsabers. "
    "Vader's Lightsaber as written. Blaster Rack (V). "
    "Breached Defenses + Molator dested Breached Defenses & Molator. "
    "A Sith's Plans as written. Mara Jade w/ Lightsaber dested Mara Jade With Lightsaber. "
    "Aerra Sing dested Aurra Sing. Dr. E + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "U3PO dested U-3PO (Yoo-Threepio). Shade dested Shada. "
    "Darth Vader, BOTJ dested Darth Vader, Betrayer Of The Jedi. "
    "Darth Vader, MMTM dested Darth Vader, More Machine Than Man. "
    "Darth Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Cyborg Commander, HoJ dested Grievous, Hunter Of Jedi. "
    "Black Leader dested Juno Eclipse, Black Leader. Galen, SA dested Galen Marek, Starkiller. "
    "Zuckass in Mist dested Zuckuss In Mist Hunter. Galen's Fighter dested Rogue Shadow. "
    "If The Trace Was dested If The Trace Was Correct (V). "
    "Defensive Shields marked n/a. "
    "Form left column reprints 37–38 on lines 39–40 are Darth Vader, Betrayer Of The Jedi and More Machine Than Man. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Ralltiir Freighter Captain", qty=9),
    n("Chewie With Blaster Rifle", qty=2),
    n("Lando With Blaster Pistol", qty=2),
    n("LE-BO2D9 (Leebo)", qty=2),
    n("BoShek, Brash Smuggler"),
    n("Han With Heavy Blaster Pistol"),
    n("Han Solo, Courageous Smuggler"),
    n("Son Of Skywalker"),
    n("Dash Rendar"),
    n("Mirax Terrik"),
    n("Rycar Ryjerd", True),
    n("Kessel Run", qty=4),
    n("Legendary Starfighter"),
    n("Squadron Assignments"),
    n("Smuggler's Blues", True),
    n("Projection Of A Skywalker"),
    n("Bargaining Table"),
    n("An Unusual Amount Of Fear"),
    n("Hyper Escape", qty=2),
    n("Nar Shaddaa Wind Chimes", qty=3),
    n("The Bith Shuffle", qty=2),
    n("Punch It!", qty=2),
    n("Cantina Brawl"),
    n("The Signal"),
    n("Houjix"),
    n("Millennium Falcon", qty=2),
    n("YT-1300 Transport", True, qty=2),
    n("Artoo-Detoo In Red 5"),
    n("Outrider"),
    n("BoShek's Modified Light Freighter"),
    n("Pulsar Skate"),
    n("Spiral"),
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Ralltiir", qty=2),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine: Cantina"),
    n("Tatooine"),
    n("Kessel"),
]
LS_SHIELDS = [
    n("Yavin Sentry"),
    n("No Questions Asked"),
    n("Battle Plan", True),
    n("Wise Advice", True),
    n("Ultimatum", True),
    n("Do, Or Do Not", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Force Lightning"),
    n("One Bright Spot", qty=3),
    n("One Beautiful Thing", qty=3),
    n("Alter & Collateral Damage"),
    n("Sense & Uncertain Is The Future"),
    n("Elis Helrot", qty=2),
    n("I Have You Now", qty=2),
    n("Imperial Barrier"),
    n("Scanning Crew", qty=2),
    n("Lightsaber Parry", qty=2),
    n("Galen's Lightsaber"),
    n("Grievous' Lightsabers"),
    n("Trophy Of A Kill", qty=2),
    n("Vader's Lightsaber"),
    n("Presence Of The Force"),
    n("Imperial Propaganda"),
    n("Blaster Rack", True),
    n("Guild Of Assassins"),
    n("Breached Defenses & Molator"),
    n("A Sith's Plans"),
    n("Ghhhk"),
    n("Prepared Defenses"),
    n("Mara Jade With Lightsaber"),
    n("Aurra Sing"),
    n("Dr. Evazan & Ponda Baba"),
    n("U-3PO (Yoo-Threepio)"),
    n("Prince Xizor"),
    n("Guri"),
    n("Shada"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Vader, More Machine Than Man"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Juno Eclipse, Black Leader", qty=2),
    n("Galen Marek, Starkiller", qty=2),
    n("The Force Unleashed"),
    n("Coruscant: Imperial City"),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Kiffex"),
    n("Tatooine: Cantina"),
    n("Endor: Back Door"),
    n("Zuckuss In Mist Hunter"),
    n("Executor"),
    n("Virago"),
    n("Rogue Shadow"),
    n("Stalker"),
    n("If The Trace Was Correct", True),
]
DS_SHIELDS = []
DS_ADD = []
