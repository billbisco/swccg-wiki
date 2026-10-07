#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Mark Walseth.

Source: 2012NationalsDay1.pdf pages 82–83 (typed 2010 Xerox, 12 shields).
p82 Dark / p83 Light Name Walseth Username blank dested Mark Walseth analog leftover
identified stub player-stubs/Mark_Walseth.wiki / Walseth.wiki redirect / generate_2013_worlds CANON.
Pack player-stubs/Mark_Walseth.wiki. Do not dest as a new person Walseth.
"""
from __future__ import annotations

PLAYER = "Mark Walseth"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 83
DS_PAGE = 82
LS_SCAN = "2012 US Nationals Day 1 Mark Walseth LS.png"
DS_SCAN = "2012 US Nationals Day 1 Mark Walseth DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed 2010 Xerox. Name Walseth dested Mark Walseth analog leftover identified stub. "
    "Username blank. Do not dest as a new person Walseth."
)
LS_NOTE = (
    "Typed 2010 Xerox. Name Walseth dested Mark Walseth analog leftover identified stub. "
    "Username blank. LIGHT checked. Deck Name Yavin 4 Space 2012. Event Name Nationals. Event Date 06/09/12. "
    "Do not dest as a new person Walseth. "
    "Yavin 4 dested analog leftover. "
    "Yavin 4: Massassi Headquarters dested dest-as-written. "
    "Careful Planning True dested Careful Planning (V) analog leftover 2013 Worlds Walseth LS_START. "
    "Get to Your Ships dested Get To Your Ships analog leftover. "
    "Luke, Trust Me dested analog leftover. "
    "Rycar Ryjar dested Rycar Ryjerd analog leftover Reisch. "
    "Yavin 4: War Room dested analog leftover. "
    "Yavin 4: Throne Room dested Yavin 4: Massassi Throne Room analog leftover Anderson. "
    "Yavin 4: Briefing Room dested analog leftover. "
    "R2-D2 in Red 5 dested Artoo-Detoo In Red 5 analog leftover Bordier x4 unique overcount. "
    "Han, Chewie, and the Millennium Falcon dested Han, Chewie, And The Falcon analog leftover McCune. "
    "X-Wing Laser Cannon dested X-wing Laser Cannon analog leftover Casey x3. "
    "All Wings Report In & Darklighter Spin dested analog leftover Haglund x3. "
    "Antilles Maneuver & Rebel Reinforcement dested Antilles Maneuver & Rebel Reinforcements analog leftover Schoenthal. "
    "Projection of a Skywalker dested Projection Of A Skywalker analog leftover McCune. "
    "I'll Take the Leader dested I'll Take The Leader analog leftover Casey. "
    "Restore Freedom To The Galaxy True dested analog leftover virtual-only. "
    "Anger Fear Aggression dested Anger, Fear, Aggression True analog leftover McCune IN THE 60. "
    "A Tragedy Has Occured dested A Tragedy Has Occurred analog leftover. Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed 2010 Xerox. Name Walseth dested Mark Walseth analog leftover identified stub. "
    "Username blank. DARK checked. Deck Name Fully Armed. Event Name Nationals 2012. "
    "Do not dest as a new person Walseth. "
    "SYCFA / TUPITU dested Set Your Course For Alderaan / The Ultimate Power In The Universe analog leftover McCune. "
    "Dreaded Imperial Starfleet dested analog leftover McCune True. "
    "Kuat Drive Yards dested analog leftover McCune True. "
    "Darth Maul with Lightsaber dested Darth Maul With Lightsaber analog leftover x3 unique overcount. "
    "Death Star Gunner True dested analog leftover McCune x3 unique overcount. "
    "Control & Set For Stun dested analog leftover Amato x2. "
    "Lateral Damage dested analog leftover McCune x4 unique overcount. "
    "He Is Not Ready & Imperial Propaganda dested analog leftover McCune True. "
    "Image of the Dark Lord dested Image Of The Dark Lord analog leftover McCune True. "
    "Superlaser dested analog leftover McCune. "
    "Visage dested analog leftover McCune. "
    "A Dark Time For The Rebellion dested analog leftover McCune True x3 unique overcount. "
    "Knowledge And Defense dested analog leftover McCune IN THE 60 True. "
    "Come Here you Big Coward dested Come Here You Big Coward analog leftover. "
    "Do They Have a Code Clearance dested Do They Have A Code Clearance? analog leftover. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Careful Planning"
LS_CARDS = [
    n("Yavin 4"),
    n("Yavin 4: Massassi Headquarters"),
    n("Careful Planning", True),
    n("Get To Your Ships"),
    n("Luke, Trust Me", True),
    n("Rycar Ryjerd", True),
    n("Yavin 4: War Room", True),
    n("Yavin 4: Massassi Throne Room"),
    n("Yavin 4: Briefing Room"),
    n("Ralltiir"),
    n("Kiffex"),
    n("Luke Skywalker", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Elyhek Rue"),
    n("Boshek, Brash Smuggler", True),
    n("Corran Horn"),
    n("Jek Porkins", True),
    n("Mace Windu, Master Of The Order", True),
    n("Artoo-Detoo In Red 5", qty=4),
    n("Red Squadron 1"),
    n("Red Squadron 7"),
    n("Red 6"),
    n("Red 7", True),
    n("Boshek's Modified Freighter", True),
    n("Han, Chewie, And The Falcon"),
    n("X-wing Laser Cannon", qty=3),
    n("Portable Scanner"),
    n("All Wings Report In & Darklighter Spin", qty=3),
    n("Rebel Artillery", qty=3),
    n("Power Pivot", qty=2),
    n("Organized Attack", qty=2),
    n("It Could Be Worse", qty=2),
    n("We're Doomed", qty=2),
    n("Alter", True),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Stay Sharp"),
    n("Projection Of A Skywalker"),
    n("Imperial Atrocity", True, qty=3),
    n("I'm With You Too", True),
    n("Massassi Base Sentry", True),
    n("A Vergence In The Force"),
    n("Scrambled Transmission", True),
    n("I'll Take The Leader"),
    n("Restore Freedom To The Galaxy", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Do, Or Do Not", True),
    n("Ultimatum"),
    n("Aim High"),
    n("Battle Plan"),
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star"),
    n("Death Star: Docking Bay"),
    n("Alderaan"),
    n("Prepared Defenses"),
    n("A Million Voices Crying Out"),
    n("Dreaded Imperial Starfleet", True),
    n("Kuat Drive Yards", True),
    n("Death Star: War Room", True),
    n("Death Star: Central Core", True),
    n("Anoat"),
    n("Malastare"),
    n("Raithal"),
    n("Nal Hutta"),
    n("Rendili"),
    n("Corulag"),
    n("Darth Maul With Lightsaber", qty=3),
    n("Death Star Gunner", True, qty=3),
    n("Tyrant"),
    n("Devastator", True),
    n("Accuser"),
    n("Vengeance"),
    n("Conquest", True),
    n("Victory", True),
    n("Thunderflare"),
    n("Visage"),
    n("Dominator", True),
    n("Stalker"),
    n("Judicator"),
    n("Overwhelmed", qty=4),
    n("A Dark Time For The Rebellion", True, qty=3),
    n("Control & Set For Stun", qty=2),
    n("Limited Resources", qty=2),
    n("Put All Sections On Alert", qty=2),
    n("Lateral Damage", qty=4),
    n("Dark Waters"),
    n("Imperial Propaganda", True, qty=2),
    n("He Is Not Ready & Imperial Propaganda", True),
    n("Image Of The Dark Lord", True),
    n("Tarkin's Bounty", True),
    n("No Escape"),
    n("Superlaser"),
    n("Commence Primary Ignition", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?"),
    n("Oppressive Enforcement"),
    n("A Useless Gesture", True),
    n("Imperial Detention", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Fanfare"),
]
DS_ADD = []
