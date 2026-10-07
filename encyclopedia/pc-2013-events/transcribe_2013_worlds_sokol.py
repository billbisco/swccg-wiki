#!/usr/bin/env python3
"""2013 World Championship Day 2: Matt Sokol Xerox Walker Garrison + Profit."""
from __future__ import annotations

PLAYER = "Matt Sokol"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 92
DS_PAGE = 91
LS_SCAN = "2013 Worlds Day 2 p92 Matt Sokol LS.png"
DS_SCAN = "2013 Worlds Day 2 p91 Matt Sokol DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Sokol / Matt Sokol. Username blank. LIGHT/DARK boxes empty; Profit is Light. "
    "Dest as Matt Sokol. Do not rewrite later Matt Sokol leftovers. "
    "Profit dested You Can Either Profit By This... / Or Be Destroyed. "
    "Han dested Han Solo. JP Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "LTWW dested Let The Wookiee Win. GHTM & BP dested as written. "
    "Don't Forget The Droids dested Don't Forget The Droids. "
    "You Will Take Me To Jabbanow dested You Will Take Me To Jabba Now. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Sai'torr Kal Fas dested Sai'torr Kal Fas. "
    "Mace Windu MOTO dested Mace Windu, Master Of The Order. "
    "Gayandrum's Lightsaber dested Qui-Gon Jinn's Lightsaber. "
    "Aayla Secure dested Aayla Secura. "
    "Lando with Vibro-Ax dested Lando With Vibro-Ax. "
    "IL-19 dested IL-19. "
    "Struck line 49 omitted; Artoo In Red 5 dested Artoo-Detoo In Red 5. "
    "Threepio WTHPS dested Threepio With His Parts Showing. "
    "Luke SITF dested Luke Skywalker, Strong In The Force. "
    "Obi-wan Kenobi dested Obi-Wan Kenobi. AFA dested Anger, Fear, Aggression. "
    "Jabba's Prize written on shield 6 dested as Character in the 60. "
    "Additional Do, Or Do Not / He Can Go About His Business / Simple Tricks moved to Light shields. "
    "Form left column reprints 37-38 on lines 39-40 are Tatooine Utility Belt and Luke's Lightsaber. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Matt Sokol. Username blank. DARK checked. "
    "Dest as Matt Sokol. "
    "To ISC dested Walker Garrison (Hoth walker package). "
    "Hoth: Ice Plains dested Hoth: Ice Plains (5th Marker). "
    "Hoth: Mountains dested Hoth: Mountains (6th Marker). "
    "Hoth: Main Power Generators dested Hoth: Main Power Generators (1st Marker). "
    "Hoth: Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "WIAPN dested We're In Attack Position Now. "
    "Jango Fett, The Assassin dested Jango Fett, The Assassin. "
    "U-3PO dested U-3PO (Yoo-Threepio). Veers dested Veers. "
    "Admiral Mott dested Admiral Motti. "
    "Cyclone Walker dested Cyclone Walker. "
    "ADTFTRL dested A Dark Time For The Rebellion. "
    "YMSTL dested You May Start Your Landing. "
    "MM & Endor Occupation dested Masterful Move & Endor Occupation. "
    "Control & Set For Stun dested Control & Set For Stun. "
    "Scribbled line 59 dested You'll Be Dead!. "
    "Reprint 37 Do They Have A Code Clearance dested in the 60. "
    "Reprint 38 Alert My Star Destroyer dested Alert My Star Destroyer!. "
    "Additional Come Here You Big Coward / Battle Order / Death Star Sentry moved to Dark shields. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Han Solo", True),
    n("Sense", qty=2),
    n("Home One: War Room"),
    n("Rebel Leadership", True, qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Coruscant: Jedi Council Chamber"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Naboo: Boss Nass' Chambers"),
    n("Tatooine: Lars' Moisture Farm"),
    n("Blaster Deflection"),
    n("Let The Wookiee Win", True),
    n("GHTM & BP"),
    n("Run Luke, Run!"),
    n("Don't Forget The Droids", True, qty=2),
    n("Nabrun Leids", qty=2),
    n("Clash Of Sabers", qty=2),
    n("You Will Take Me To Jabba Now", True),
    n("Heading For The Medical Frigate"),
    n("Imperial Atrocity", True, qty=2),
    n("A Gift"),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Lightsaber Proficiency"),
    n("Rycar Ryjerd", True),
    n("Quick Draw", True),
    n("I Must Be Allowed To Speak", True),
    n("Luke's Bionic Hand"),
    n("Tatooine Utility Belt", True),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Obi-Wan's Journal"),
    n("Aayla Secura"),
    n("Mace Windu, Master Of The Order"),
    n("Corran Horn"),
    n("Lando With Vibro-Ax"),
    n("IL-19"),
    n("Artoo-Detoo In Red 5", True),
    n("Threepio With His Parts Showing"),
    n("Leia, Rebel Princess"),
    n("Padme Naberrie"),
    n("Chewbacca, Protector"),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Obi-Wan Kenobi", True, qty=3),
    n("Anger, Fear, Aggression", True),
    n("Jabba's Prize"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Let's Keep A Little Optimism Here", True),
    n("Aim High"),
    n("The Professor", True),
    n("Affect Mind", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Traffic Control", True),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Do, Or Do Not", True),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []


DS_START = "Walker Garrison"
DS_CARDS = [
    n("Walker Garrison", True),
    n("Imperial Decree"),
    n("AT-AT Cannon", True),
    n("U-3PO (Yoo-Threepio)"),
    n("Target The Main Generator"),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("AT-AT Deployment Platform", qty=2),
    n("Hoth"),
    n("We're In Attack Position Now", qty=2),
    n("Admiral Piett"),
    n("Jango Fett, The Assassin"),
    n("Garindan", True),
    n("Veers", True),
    n("Admiral Motti", True),
    n("General Nevar"),
    n("Darth Vader", True),
    n("Commander Igar"),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("Blizzard 1"),
    n("Tempest 1"),
    n("Cyclone Walker", qty=3),
    n("Blizzard 2", True),
    n("Blizzard 4", qty=2),
    n("Victory", qty=2),
    n("Flagship Executor"),
    n("Conquest", True, qty=2),
    n("A Dark Time For The Rebellion", True),
    n("Alert My Star Destroyer!"),
    n("Do They Have A Code Clearance?", True),
    n("Image Of The Dark Lord"),
    n("Cold Feet", True),
    n("Trample"),
    n("Hoth Blockade"),
    n("Fleet Security Protocols"),
    n("You May Start Your Landing", True),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("Imperial Command", qty=3),
    n("Close Call", True, qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Prepared Defenses", True),
    n("No Escape"),
    n("Control & Set For Stun"),
    n("Crash Landing"),
    n("You'll Be Dead!"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Resistance", True),
    n("There Is No Try"),
    n("After Her!", True),
    n("Firepower", True),
    n("Reactor Terminal", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Secret Plans"),
    n("Leave Them To Me", True),
    n("Allegations Of Corruption", True),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Death Star Sentry", True),
]
DS_ADD = []
