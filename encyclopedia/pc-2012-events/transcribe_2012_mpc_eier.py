#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: Brad Eier.

Source: 2012mpcday1.pdf pages 21–22 (handwritten notebook 60s).
Name Brad Eier dested Brad Eier. Username blank.
p21 Dark IO/IC (V). p22 Light Communing.
"""
from __future__ import annotations

PLAYER = "Brad Eier"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 22
DS_PAGE = 21
LS_SCAN = "2012 Match Play Championship Day 1 Brad Eier LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 Brad Eier DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten notebook 60 bound into 2012mpcday1.pdf."
LS_NOTE = (
    "Handwritten notebook. Name Brad Eier dested Brad Eier. Username blank. "
    "Brad Eier Light side. Event MPC Day 1. "
    "Tatooine: Slave Quarters (SL) dested Tatooine: Slave Quarters. "
    "Tatooine city outskirts dested Tatooine: City Outskirts. "
    "Tatooine obiwans hut dested Tatooine: Obi-Wan's Hut. "
    "Tatooine jundland wastes dested Tatooine: Jundland Wastes. "
    "Tatooine (ep1) dested Tatooine (Coruscant). "
    "Home one war room dested Home One: War Room. "
    "COMMUNING dested Communing. "
    "Commander Luke Skywalker dested Commander Luke Skywalker. "
    "Wedge Antilles, red squadron leader dested Wedge Antilles, Red Squadron Leader. "
    "Commander Wedge Antilles dested Commander Wedge Antilles. "
    "Yoda great warrior dested Yoda, Great Warrior. "
    "Master Kenobi dested Master Kenobi. Captain Verrack dested Captain Verrack. "
    "Major Hassh'n dested Major Hassh'n. Admiral Ackbar dested Admiral Ackbar. "
    "Dash Rendar dested Dash Rendar. Zev Senesca dested Zev Senesca. "
    "Padme Naberrie dested Padmé Naberrie. Leia rebel princess dested Leia, Rebel Princess. "
    "Corran Horn dested Corran Horn. Shmi Skywalker dested Shmi Skywalker. "
    "Threepio w/his parts showing dested Threepio With His Parts Showing. "
    "Derek Hobbie Klivian dested Derek \"Hobbie\" Klivian. "
    "Lando Calrissian, scoundrel dested Lando Calrissian, Scoundrel. "
    "Home One dested Home One. Spiral dested Spiral. Tantive IV dested Tantive IV. "
    "Han Chewie & the Falcon dested Han, Chewie, And The Falcon. "
    "Bright Hope dested Bright Hope. Rogue 1 dested Rogue 1. "
    "Rogue 2 dested Rogue 2. Rogue 3 dested Rogue 3. Rogue 4 dested Rogue 4. "
    "Lets go left dested Let's Go Left. Flash of insight dested Flash Of Insight. "
    "Imperial atrocity dested Imperial Atrocity. "
    "Launching the assault dested Launching The Assault. "
    "Menace fades dested Menace Fades. Echo base garrison dested Echo Base Garrison. "
    "Scrambled transmission dested Scrambled Transmission. "
    "Tatooine celebration dested Tatooine Celebration. Wokling dested Wokling. "
    "Maneuvering flaps & nick of time dested Maneuvering Flaps & Nick Of Time. "
    "Rebel gunrunner dested Rebel Gunrunner. "
    "Dual laser cannon dested Dual Laser Cannon. Escape Pod dested Escape Pod. "
    "Houjix dested Houjix. "
    "Over for rest of List is the right column on the same page. No shield block. "
    "Unique overcounts sheet-accurate (Commander Luke Skywalker x2, Rogue 1 x2, "
    "Let's Go Left x3, Flash Of Insight x3). "
    "(V) as written on the notebook."
)
DS_NOTE = (
    "Handwritten notebook. Name Brad Eier dested Brad Eier. Username blank. "
    "Brad Eier dark. Event MPC Day 1. "
    "Imperial occupation / Imp. control dested Imperial Occupation / Imperial Control. "
    "You may start your landing dested You May Start Your Landing. "
    "Endor shield dested Endor Shield. Imperial decree dested Imperial Decree. "
    "Ni Chuba Na? dested Ni Chuba Na??. Hol-ice plains dested Hoth: Ice Plains. "
    "Hoth mainpower generator (Light) dested Hoth: Main Power Generators. "
    "Hoth dested Hoth. Hoth defensive perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth mountains dested Hoth: Mountains (6th Marker). "
    "A dark time for the rebellion dested A Dark Time For The Rebellion. "
    "Imperial command dested Imperial Command. Control dested Control. "
    "Operational as planned dested Operational As Planned. "
    "Prepared defenses circled non-V dested Prepared Defenses empty. "
    "THE EMPIRE'S BACK dested Weapon Levitation & The Empire's Back. "
    "Cold feet dested Cold Feet. Walker garrison dested Walker Garrison. "
    "Force push dested Force Push. Trample dested Trample. No escape dested No Escape. "
    "Image of the dark lord dested Image Of The Dark Lord. "
    "Imperial propaganda dested Imperial Propaganda. "
    "Something special planned for them dested Something Special Planned For Them. "
    "Do they have a code clearance dested Do They Have A Code Clearance? in the main 60. "
    "Hoth blockade dested Hoth Blockade. "
    "We're in attack position now dested We're In Attack Position Now. "
    "AT-AT cannon dested AT-AT Cannon. Target the main generator dested Target The Main Generator. "
    "Emperor Palpatine dested Emperor Palpatine. Darth vader dested Darth Vader, Dark Lord Of The Sith. "
    "Darth maul w/lightsaber dested Darth Maul With Lightsaber. "
    "Black leader circled non-V dested Juno Eclipse, Black Leader empty. "
    "Commander Igar dested Commander Igar. Grand admiral Thrawn dested Grand Admiral Thrawn. "
    "Admiral Piett dested Admiral Piett. Veers dested Veers. "
    "Admiral Motti dested Admiral Motti. General Nevar dested General Nevar. "
    "Grand moff Tarkin dested Grand Moff Tarkin. "
    "The emperor's reach dested Maarek Stele, The Emperor's Reach. "
    "Admiral Pellaeon dested Admiral Pellaeon. Garindan dested Garindan. "
    "Blizzard 1 dested Blizzard 1. Blizzard 2 dested Blizzard 2. "
    "Blizzard 4 circled non-V dested Blizzard 4 empty. "
    "Marquand in Blizzard 6 dested Marquand In Blizzard 6. Tempest 1 dested Tempest 1. "
    "Justifier dested Justifier. "
    "Emperor's personal shuttle circled non-V dested Emperor's Personal Shuttle empty. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "Battle order dested Battle Order. There is NO try dested There Is No Try. "
    "You cannot hide forever dested You Cannot Hide Forever. "
    "A useless gesture dested A Useless Gesture. "
    "Come here you big coward dested Come Here You Big Coward. "
    "Secret plans dested Secret Plans. Fanfare dested Fanfare. Abyss dested Abyss. "
    "Allegations of corruption dested Allegations Of Corruption. "
    "Resistance dested Resistance. Oppressive enforcement dested Oppressive Enforcement. "
    "Firepower dested Firepower. "
    "Unique overcounts sheet-accurate (A Dark Time For The Rebellion x2, Imperial Command x3, "
    "Control x2, We're In Attack Position Now x2, Emperor Palpatine x2, Garindan x2, "
    "Justifier x2, Emperor's Personal Shuttle x2). "
    "(V) as written on the notebook."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Jundland Wastes"),
    n("Tatooine (Coruscant)"),
    n("Home One: War Room"),
    n("Communing"),
    n("Commander Luke Skywalker", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Commander Wedge Antilles", True),
    n("Yoda, Great Warrior"),
    n("Master Kenobi"),
    n("Captain Verrack", True),
    n("Major Hassh'n"),
    n("Admiral Ackbar", True),
    n("Dash Rendar", True),
    n("Zev Senesca"),
    n("Padmé Naberrie", True),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Derek \"Hobbie\" Klivian"),
    n("Lando Calrissian, Scoundrel", True),
    n("Home One"),
    n("Spiral"),
    n("Tantive IV", True),
    n("Han, Chewie, And The Falcon", True),
    n("Bright Hope", True),
    n("Rogue 1", qty=2),
    n("Rogue 2"),
    n("Rogue 3"),
    n("Rogue 4"),
    n("Let's Go Left", True, qty=3),
    n("Flash Of Insight", True, qty=3),
    n("Imperial Atrocity", True),
    n("Launching The Assault"),
    n("Menace Fades"),
    n("Echo Base Garrison"),
    n("Scrambled Transmission", True),
    n("Tatooine Celebration"),
    n("Wokling", True),
    n("Maneuvering Flaps & Nick Of Time"),
    n("Rebel Gunrunner"),
    n("Dual Laser Cannon", True),
    n("Escape Pod", True),
    n("Houjix"),
]
LS_SHIELDS = []
LS_ADD = []

DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("You May Start Your Landing"),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("Ni Chuba Na??", True),
    n("Hoth: Ice Plains", True),
    n("Hoth: Main Power Generators"),
    n("Hoth"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Mountains (6th Marker)"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Imperial Command", qty=3),
    n("Control", qty=2),
    n("Operational As Planned", True),
    n("Prepared Defenses"),
    n("Weapon Levitation & The Empire's Back", True),
    n("Cold Feet", True),
    n("Walker Garrison"),
    n("Force Push", True),
    n("Trample"),
    n("No Escape"),
    n("Image Of The Dark Lord", True),
    n("Imperial Propaganda", True),
    n("Something Special Planned For Them", True),
    n("Do They Have A Code Clearance?"),
    n("Hoth Blockade"),
    n("We're In Attack Position Now", qty=2),
    n("AT-AT Cannon", True),
    n("Target The Main Generator"),
    n("Emperor Palpatine", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", True),
    n("Darth Maul With Lightsaber"),
    n("Juno Eclipse, Black Leader"),
    n("Commander Igar", True),
    n("Grand Admiral Thrawn"),
    n("Admiral Piett"),
    n("Veers", True),
    n("Admiral Motti", True),
    n("General Nevar"),
    n("Grand Moff Tarkin", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Admiral Pellaeon"),
    n("Garindan", True, qty=2),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Marquand In Blizzard 6"),
    n("Tempest 1"),
    n("Justifier", qty=2),
    n("Emperor's Personal Shuttle", qty=2),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Firepower", True),
]
DS_ADD = []
