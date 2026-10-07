#!/usr/bin/env python3
"""2014 Alderaan Regionals Xerox: Adam K (Plagueis).

Source: 2014-Alderaan-Regionals.pdf pages 11–12 (typed 2013 Print Form).
Name Adam K dested as written. Username Plagueis. Do not invent a last name.
"""
from __future__ import annotations

PLAYER = "Adam K"
USERNAME = "Plagueis"
STAGE = ""
PDF = "2014 Alderaan Regionals.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2014 Alderaan Regionals p11 Adam K LS.png"
DS_SCAN = "2014 Alderaan Regionals p12 Adam K DS.png"
NOTE = (
    "Typed 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Adam K dested as written. Username Plagueis. Email [redacted]. "
    "Do not dest as Adam Kwart. LS Hidden Base (Deck Name Hidden Base Rogues) / "
    "DS Imperial Occupation (Deck Name Walkers). "
    "Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Coran Horn dested Corran Horn. "
    "Obi Wan with Saber dested Obi-Wan With Lightsaber. "
    "Han Chewie & Falcon dested Han, Chewie, And The Falcon. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "DarkLighter Spin dested Darklighter Spin. "
    "Rouge Squadron Tactics dested Rogue Squadron Tactics. "
    "Anger,Fear, Agression dested Anger, Fear, Aggression. "
    "A Tragedy Has Occured dested A Tragedy Has Occurred. "
    "Weapon Display dested Weapons Display. "
    "Wise Advise dested Wise Advice. "
    "Do or Do Not dested Do, Or Do Not. "
    "Ep I Tatooine dested Tatooine. "
    "Darth Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Mara Jade with Saber dested Mara Jade With Lightsaber. "
    "Darth Maul with Saber dested Darth Maul With Lightsaber. "
    "Dr. E & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Ni Chuba Na?? dested Ni Chuba Na?. "
    "Hoth Blocado dested as written (NO_DEST). "
    "BoShek's Modified Freighter dested as written (NO_DEST). "
    "Omni Box & It's Worse dested Ommni Box & It's Worse. "
    "Opressive Enforcement dested Oppressive Enforcement. "
    "Allagations of Corruption dested Allegations Of Corruption. "
    "Imperial Occupation/Imperial Control (V) dested Imperial Occupation / Imperial Control True. "
    "(V) from the checkbox. Unique overcounts sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Biggs, Rogue Legend", True),
    n("Luke Skywalker", True),
    n("Jek Porkins", True),
    n("Tycho Celchu", True),
    n("Ten Numb", True),
    n("Corran Horn"),
    n("Jaina Solo", True),
    n("BoShek, Brash Smuggler", True),
    n("Boushh"),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Han, Chewie, And The Falcon", True),
    n("BoShek's Modified Freighter", True),
    n("Red Squadron 1"),
    n("Red 3", True),
    n("Artoo-Detoo In Red 5"),
    n("Red 6", True),
    n("Red Squadron 7", True),
    n("Rogue Squadron X-Wing", True, qty=2),
    n("X-Wing", qty=6),
    n("Heading For The Medical Frigate"),
    n("Houjix & Out Of Nowhere"),
    n("Darklighter Spin", True),
    n("It's A Hit!", True),
    n("It Could Be Worse"),
    n("Rebel Barrier"),
    n("All Wings Report In", qty=2),
    n("Antilles Maneuver", True),
    n("Hyper Escape"),
    n("Out Of Nowhere"),
    n("Organized Attack"),
    n("Starship Levitation", True),
    n("What About That Blue One?", True),
    n("Rogue Squadron Tactics", True),
    n("Squadron Assignments"),
    n("Legendary Starfighter"),
    n("S-Foils"),
    n("The Planet That It's Farthest From", True),
    n("Projection Of A Skywalker", qty=2),
    n("Imperial Atrocity", True),
    n("X-Wing Laser Cannon"),
    n("I'll Take The Leader"),
    n("Forest"),
    n("Dressel", True),
    n("Kiffex"),
    n("Tatooine"),
    n("Endor"),
    n("Kessel"),
    n("Rendezvous Point"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Ultimatum", True),
    n("He Can Go About His Business"),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Traffic Control", True),
    n("Don't Do That Again"),
    n("Do, Or Do Not"),
]
LS_ADD = []


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Emperor Palpatine"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Grand Moff Tarkin", True, qty=2),
    n("Grand Admiral Thrawn"),
    n("Veers", True),
    n("General Nevar"),
    n("ISB Sector Commander", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Mara Jade With Lightsaber", True),
    n("Boba Fett, Bounty Hunter"),
    n("Jango Fett, The Assassin", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Garindan", True),
    n("Darth Maul With Lightsaber"),
    n("U-3PO"),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4", qty=2),
    n("Marquand In Blizzard 6", True),
    n("Tempest 1"),
    n("Flagship Executor"),
    n("Devastator", True),
    n("Dominator", True),
    n("Victory", True),
    n("Prepared Defenses"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Imperial Command", True),
    n("Imperial Command", qty=2),
    n("Trample", qty=2),
    n("Cold Feet", True),
    n("Force Push", True, qty=2),
    n("Ommni Box & It's Worse"),
    n("Stop Motion", True),
    n("Imperial Decree"),
    n("Ni Chuba Na?", True),
    n("You May Start Your Landing", True),
    n("Endor Shield", True),
    n("Hoth Blocado", True),
    n("Alert My Star Destroyer!"),
    n("No Escape"),
    n("Wipe Them Out, All Of Them", True),
    n("Image Of The Dark Lord", True),
    n("Imperial Propaganda"),
    n("AT-AT Cannon", True),
    n("Target The Main Generator"),
    n("We're In Attack Position Now", qty=2),
    n("Hoth"),
    n("Hoth: Main Power Generators", True),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Mountains"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Crossfire"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Imperial Detention", True),
    n("Oppressive Enforcement", True),
    n("Resistance"),
    n("Weapon Of A Sith"),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Do They Have A Code Clearance?"),
    n("Allegations Of Corruption"),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("Battle Order"),
    n("Secret Plans"),
]
DS_ADD = []
