#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Unknown Player.

Source: 2012mpcday1.pdf pages 155–156 (2010 form, 12 shields).
Name blank / Username blank both sides. Facing pair sandwich
light_frank remainder p154 then last pages of the PDF.
Dest Unknown Player (canonical; not Blank Player). Index Unknown players.
p155 Light Communing. p156 Dark Imperial Occupation / Imperial Control True.
LIGHT/DARK empty dest sides from the 60s analog leftover Kinsey/Pistone.
Pack player-stubs/Unknown_Player.wiki.
Do not dest as a new named person. Do not dest as light_frank.
"""
from __future__ import annotations

PLAYER = "Unknown Player"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 155
DS_PAGE = 156
LS_SCAN = "2012 Match Play Championship Day 1 Unknown Player LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Unknown Player DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form. Name blank. Username blank."
PUBLIC_NOTE = "Name blank on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name blank Username blank both. "
    "Facing pair sandwich light_frank remainder p154 then last pages. "
    "Dest Unknown Player. Index Unknown players. "
    "LIGHT/DARK empty dest Light from the 60s analog leftover Kinsey. "
    "Do not dest as a new named person. Do not dest as light_frank. "
    "Communing dested Communing analog leftover SAN IN THE 60 AND START. "
    "Instant Hindsight True dested Hindsight True analog leftover SAN. "
    "Houjix / OON dested Houjix & Out Of Nowhere analog leftover SAN. "
    "Grim Skywalker dested as written. "
    "Fallen Jedi dested Fallen Jedi analog leftover SAN. "
    "Chewie Enraged True dested Chewie, Enraged True analog leftover SAN. "
    "Luke Rebel Hero dested Luke Skywalker, Rebel Hero analog leftover SAN x3. "
    "Run Luke Run True dested Run Luke, Run! True analog leftover SAN x2. "
    "Rebel Leader Ship True dested Loader Ship, Rebel True analog leftover SAN x2. "
    "Wyron Serper True dested Wyron Serper True analog leftover SAN. "
    "Its Not my Fault True dested It's Not My Fault! True analog leftover SAN x2. "
    "Obi's Hut True dested Tatooine: Obi-Wan's Hut True analog leftover SAN. "
    "Threepio w/ parts dested Threepio With His Parts Showing analog leftover Foth. "
    "Suhaya True dested Suhaya True analog leftover Foth. "
    "Cantina dested Tatooine: Cantina analog leftover Shaw. "
    "Home 1 War Room dested Home One: War Room analog leftover SAN. "
    "Security Breach dested Security Breach analog leftover SAN. "
    "Pine Deli dested as written. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader analog leftover SAN. "
    "Sorry About the Mess / BP dested Sorry About The Mess & Blaster Proficiency analog leftover SAN. "
    "Yoda GW dested Yoda, Great Warrior analog leftover SAN. "
    "Luke's Blaster True dested Luke's Blaster Pistol True analog leftover SAN. "
    "Alderaan Consular Ship dested Alderaan Consular Ship analog leftover SAN x2. "
    "Use The Force True AND empty kept separate analog leftover Shaw. "
    "Mag. Flaps dested Maneuvering Flaps analog leftover Anderson. "
    "Padme True dested Padmé Naberrie True analog leftover SAN. "
    "Mace in Slave Quarters dested Tatooine: Slave Quarters analog leftover SAN. "
    "Chewie's Bowcaster dested Chewbacca's Bowcaster analog leftover SAN. "
    "Master Kenobi dested Master Kenobi analog leftover SAN. "
    "Wise Counsel dested as written. "
    "Commando Training & Klor dested Commando Training & K'lor'slug analog leftover SAN. "
    "Captain Verrack True dested Captain Verrack True analog leftover Shaw. "
    "AFA True dested Anger, Fear, Aggression True analog leftover SAN IN THE 60. "
    "Shield 12 cropped dested Do, Or Do Not analog leftover Murray. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name blank Username blank. "
    "LIGHT/DARK empty dest Dark from the 60s analog leftover Pistone. "
    "Do not dest as a new named person. Do not dest as light_frank. "
    "Imperial Occupation / IC True dested Imperial Occupation / Imperial Control True analog leftover Wirfs IN THE 60 AND START. "
    "We're in attack position dested We're In Attack Position Now analog leftover walker x2. "
    "Do they have a code dested Do They Have A Code Clearance analog leftover Eier IN THE 60. "
    "Executor Shuttle True dested TIE Shuttle True analog leftover. "
    "Ni Chuba Na True dested Ni Chuba Na?? True analog leftover Marlow. "
    "Hoth MPG dested Hoth: Main Power Generators analog leftover Wirfs. "
    "Hoth Blockade dested Hoth Blockade analog leftover Wirfs. "
    "Hoth Mountains dested Hoth: Mountains (6th Marker) analog leftover walker. "
    "Tempest 1 dested Tempest 1 analog leftover Brian leftover. "
    "Veers True dested Veers True analog leftover Brian leftover. "
    "Thrawn dested Grand Admiral Thrawn analog leftover Wirfs. "
    "While are you telling this True dested Why Didn't You Tell Me? True analog leftover Lepine. "
    "Boba Fett BH True dested Boba Fett, Bounty Hunter True analog leftover Booker. "
    "Grindan True dested Garindan True analog leftover Wirfs x2. "
    "Conqueror True dested Conquest True analog leftover Wirfs. "
    "Mercenary in Bounty dested Boba Fett In Slave I analog leftover Booker. "
    "A Dark Time True dested A Dark Time For The Rebellion True analog leftover SAN x2. "
    "Prepared Defenses True dested Prepared Defenses True analog leftover IN THE 60. "
    "Omni Box & It's Worse dested Ommni Box & It's Worse analog leftover Hollingworth. "
    "Trample dested Trample analog leftover Eier x2. "
    "Fett dested Boba Fett analog leftover. "
    "Hoth Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker) analog leftover Eier. "
    "Imperial Command dested Imperial Command analog leftover Eier x3. "
    "Hoth Ice Plains True dested Hoth: Ice Plains True analog leftover. "
    "Target The Main dested Target The Main Generator analog leftover Lepine. "
    "Secret Moff & Fusion True dested as written. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach analog leftover Eier. "
    "Black Leader dested Juno Eclipse, Black Leader analog leftover Eier. "
    "U-3PO dested U-3PO analog leftover Wirfs. "
    "Executor dested Executor analog leftover Veasey x2 sheet-accurate. "
    "K&D dested Knowledge And Defense analog leftover Murray IN THE 60. "
    "Coward dested Come Here You Big Coward analog leftover Lepine. "
    "A Useless Gesture dested A Useless Gesture analog leftover Eier. "
    "Shield 12 cropped dested skip analog leftover crossed no replacement. "
    "Additional Leave Them To Me True dested Leave Them To Me True analog leftover. Unique 60. Shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Hindsight", True),
    n("Houjix & Out Of Nowhere"),
    n("Use The Force", True),
    n("Grim Skywalker"),
    n("Fallen Jedi"),
    n("Chewie, Enraged", True),
    n("Luke Skywalker, Rebel Hero", qty=3),
    n("Run Luke, Run!", True, qty=2),
    n("Home One"),
    n("Tantive IV", True),
    n("Tatooine (Coruscant)"),
    n("Weapon Levitation"),
    n("Chewbacca, Protector", True, qty=2),
    n("Loader Ship, Rebel", True, qty=2),
    n("Desperate Reach", True),
    n("Seeking An Audience", True),
    n("Wyron Serper", True),
    n("It's Not My Fault!", True, qty=2),
    n("Lando Calrissian, Scoundrel", True),
    n("Coruscant: Plaza"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Threepio With His Parts Showing"),
    n("Suhaya", True),
    n("Tatooine: Cantina"),
    n("Home One: War Room"),
    n("Security Breach"),
    n("Pine Deli"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Draw Their Fire"),
    n("Han With Heavy Blaster Pistol"),
    n("Artoo-Detoo In Red 5"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Yoda, Great Warrior"),
    n("Flash Of Insight", True),
    n("Luke's Blaster Pistol", True),
    n("Senator Leia Organa", True),
    n("It Could Be Worse"),
    n("Alderaan Consular Ship", qty=2),
    n("Admiral Ackbar", True),
    n("Use The Force"),
    n("Maneuvering Flaps"),
    n("Padmé Naberrie", True),
    n("Jedi Levitation", True),
    n("Pride Of The Jedi"),
    n("Tatooine: Slave Quarters"),
    n("Chewbacca's Bowcaster"),
    n("Rebel Leadership"),
    n("Master Kenobi"),
    n("Communing"),
    n("Wise Counsel"),
    n("Commando Training & K'lor'slug"),
    n("Captain Verrack", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Aim High", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("Ultimatum", True),
    n("A Tragedy Has Occurred", True),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Do, Or Do Not"),
]
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("No Escape"),
    n("We're In Attack Position Now", qty=2),
    n("Do They Have A Code Clearance"),
    n("Imperial Decree"),
    n("TIE Shuttle", True),
    n("Ni Chuba Na??", True),
    n("You May Start Your Landing"),
    n("Hoth: Main Power Generators"),
    n("Hoth Blockade"),
    n("General Veers"),
    n("Admiral Piett"),
    n("Hoth: Mountains (6th Marker)"),
    n("AT-AT Cannon", True),
    n("Tempest 1"),
    n("Veers", True),
    n("Grand Admiral Thrawn"),
    n("Why Didn't You Tell Me?", True),
    n("Image Of The Dark Lord", True),
    n("Boba Fett, Bounty Hunter", True),
    n("Darth Vader", True, qty=2),
    n("Garindan", True, qty=2),
    n("Bossk", True),
    n("Walker Garrison"),
    n("Probe Droid", True),
    n("Conquest", True),
    n("Boba Fett In Slave I"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Prepared Defenses", True),
    n("Ommni Box & It's Worse"),
    n("Blizzard 2", True),
    n("Trample", qty=2),
    n("Boba Fett"),
    n("Masterful Move"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Imperial Command", qty=3),
    n("Hoth: Ice Plains", True),
    n("Admiral Motti", True),
    n("Blizzard 1", True),
    n("Executor", qty=2),
    n("Control"),
    n("Target The Main Generator"),
    n("Cold Feet", True),
    n("Secret Moff & Fusion", True),
    n("Commander Igar", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Blizzard 4"),
    n("Protocol Failure"),
    n("Juno Eclipse, Black Leader"),
    n("U-3PO"),
    n("Crash Landing"),
    n("Imperial Occupation / Imperial Control", True),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Abyss"),
    n("Secret Plans", True),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Battle Order", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Firepower"),
    n("A Useless Gesture"),
]
DS_ADD = [
    n("Leave Them To Me", True),
]
