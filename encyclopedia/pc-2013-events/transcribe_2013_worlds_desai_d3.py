#!/usr/bin/env python3
"""2013 World Championship Day 3: Justin Desai Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Justin Desai"
USERNAME = ""
STAGE = "Day 3"
PDF = "2013 Worlds Day 3.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2013 Worlds Day 3 p08 Justin Desai LS.png"
DS_SCAN = "2013 Worlds Day 3 p07 Justin Desai DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Deck Name Desai. LIGHT checked. "
    "Event Day 3. Name/Username/Email blank. Dest Justin Desai. "
    "Tatooine: Slave Quarters dested Tatooine: Slave Quarters. "
    "It is the Future dested It Is The Future You See. "
    "Coruscant: JCC dested Coruscant: Jedi Council Chamber. "
    "Leia RP dested Leia, Rebel Princess. "
    "Speak with the Jedi dested Speak With The Jedi Council. "
    "Jedi saber dested Jedi Lightsaber. "
    "Sense / AC dested Sense. "
    "Mace Windu, MOTW dested Mace Windu, Master Of The Order. "
    "Luke Skywalker JK dested Luke Skywalker, Jedi Knight. "
    "Luke SITF dested Luke Skywalker, Strong In The Force. "
    "Qui-Gon's saber (5) dested Qui-Gon's Lightsaber; (5) is destiny. "
    "Jedi Leadership dested Rebel Leadership. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "HCE dested Heading For The Medical Frigate. "
    "Wesa dested Wesa Gotta Grand Army. "
    "Battle Plan / DTF dested Battle Plan & Draw Their Fire. "
    "Do or Do Not / WA dested Do, Or Do Not & Wise Advice. "
    "Weequay dested Weequay as written. "
    "Weapon Lev dested Weapon Levitation. "
    "Lando Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Projection of a Skywalker dested Projection Of A Skywalker. "
    "AFA dested Anger, Fear, Aggression. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Deck Name Desai. DARK checked. "
    "Event Day 3. Name/Username/Email blank. Dest Justin Desai. "
    "Imperial Occupation/IC dested Imperial Occupation / Imperial Control. "
    "Hoth Ice Plains dested Hoth: Ice Plains (5th Marker). "
    "Hoth MPG dested Hoth: Main Power Generators (1st Marker). "
    "YMSYL dested You May Start Your Landing. "
    "Ni Chuba dested Ni Chuba Na??. "
    "Alert dested Alert My Star Destroyer!. "
    "Image of the DL dested Image Of The Dark Lord. "
    "A dark time dested A Dark Time For The Rebellion. "
    "Hoth blizzard dested Hoth: Echo Command Center (War Room). "
    "Hoth defensive perim dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth mountains dested Hoth: Mountains (6th Marker). "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "Struck then Emp Maul dested Darth Maul With Lightsaber. "
    "Veers dested General Veers. "
    "Guardian dested Garindan. "
    "Dugout dested Admiral Chiraneau. "
    "Marquand in Bliz 6 dested Marquand In Blizzard 6. "
    "We're in attk pos dested We're In Attack Position Now. "
    "Vader dested Darth Vader With Lightsaber. "
    "IED dested Imperial Artillery. "
    "CHYBC dested Come Here You Big Coward. "
    "YCHFF dested You Cannot Hide Forever. "
    "We'll let fate dested We'll Let Fate-a Decide, Huh?. "
    "Useless Gesture dested A Useless Gesture. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("It Is The Future You See", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Seeking An Audience", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Imperial Atrocity", True, qty=2),
    n("Speak With The Jedi Council", qty=2),
    n("Jedi Lightsaber", True),
    n("A Jedi's Resilience", qty=2),
    n("Clash Of Sabers"),
    n("Sense"),
    n("Mace Windu", True, qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Mace Windu, Master Of The Order", True),
    n("Master Qui-Gon", True, qty=2),
    n("Sai'torr Kal Fas", True),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Yoda, Great Warrior", True),
    n("Naboo: Battle Plains"),
    n("Qui-Gon's Lightsaber"),
    n("Home One: War Room"),
    n("Rebel Leadership", True, qty=4),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Heading For The Medical Frigate", True),
    n("Home One"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Escape Pod", True, qty=2),
    n("Blaster Deflection"),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Quick Draw", True),
    n("Weequay"),
    n("Weapon Levitation"),
    n("Rebel Ambush"),
    n("Strikeforce", True),
    n("Luke's Lightsaber"),
    n("Let The Wookiee Win", True, qty=2),
    n("Let The Wookiee Win"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Houjix"),
    n("Lucky Shot", True),
    n("Projection Of A Skywalker"),
    n("Anger, Fear, Aggression", True),
    n("Admiral Ackbar", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well"),
    n("Don't Do That Again"),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here"),
    n("Affect Mind"),
    n("Chasm", True),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense"),
    n("Only Jedi Carry That Weapon"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = [
    n("Don't Do That Again", True),
    n("Ultimatum", True),
    n("Aim High"),
]


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control"),
    n("Prepared Defenses", True),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth"),
    n("You May Start Your Landing", True),
    n("Imperial Decree"),
    n("Endor Shield", True),
    n("Ni Chuba Na??", True),
    n("Blizzard 4", qty=2),
    n("Blizzard 1", True),
    n("Alert My Star Destroyer!"),
    n("Image Of The Dark Lord", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Cold Feet", True),
    n("Hoth: Echo Command Center (War Room)", True),
    n("Imperial Propaganda", True),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Mountains (6th Marker)"),
    n("Juno Eclipse, Black Leader", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Darth Maul With Lightsaber"),
    n("Grand Admiral Thrawn"),
    n("ISB Sector Commander", True),
    n("Grand Moff Tarkin", True, qty=2),
    n("Jango Fett, The Assassin"),
    n("Dr. Evazan & Ponda Baba"),
    n("Emperor Palpatine"),
    n("General Veers", True, qty=2),
    n("Garindan", True),
    n("Force Push", True, qty=2),
    n("Admiral Chiraneau"),
    n("U-3PO (Yoo-Threepio)"),
    n("Target The Main Generator"),
    n("Blizzard 2", True),
    n("Marquand In Blizzard 6", True),
    n("Tempest 1"),
    n("AT-AT Cannon", True),
    n("Trample", qty=2),
    n("Stop Motion", True, qty=2),
    n("No Escape"),
    n("We're In Attack Position Now", qty=2),
    n("Imperial Command", qty=3),
    n("Conquest", True),
    n("Flagship Executor", qty=2),
    n("Darth Vader With Lightsaber", True),
    n("Do They Have A Code Clearance?"),
    n("Victory", True),
    n("Imperial Artillery", True),
]
DS_SHIELDS = [
    n("Firepower"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Secret Plans", True),
    n("Abyss", True),
    n("There Is No Try"),
    n("After Her!", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Oppressive Enforcement", True),
    n("We'll Let Fate-a Decide, Huh?", True),
]
DS_ADD = [
    n("A Useless Gesture"),
    n("Do They Have A Code Clearance?"),
    n("Battle Order"),
]
