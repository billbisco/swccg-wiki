#!/usr/bin/env python3
"""2013 World Championship Day 2: Pistone Xerox WYS + Imperial Occupation Walkers."""
from __future__ import annotations

PLAYER = "Pistone"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 74
DS_PAGE = 75
LS_SCAN = "2013 Worlds Day 2 p74 Pistone LS.png"
DS_SCAN = "2013 Worlds Day 2 p75 Pistone DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Pistone. Username blank. LIGHT. "
    "Do not rewrite the 2013 MPC Pistone leftover (WYS / Hunt Down). "
    "WYS / TPCBALT dested Watch Your Step (V) / This Place Can Be A Little Rough (V). "
    "Captain Han dested Captain Han Solo. HFTMF dested Heading For The Medical Frigate. "
    "C> Spaceport City dested Spaceport City. H1: DB dested Home One: Docking Bay. "
    "C>: Spaceport DB dested Spaceport Docking Bay. C> Spaceport Street dested Spaceport Street. "
    "C> Spaceport Scoundrels Guild dested Spaceport Scoundrels Guild. "
    "LSJK dested Luke Skywalker, Jedi Knight. Lando, Unlikely Hero dested "
    "Lando Calrissian, Unlikely Hero. Sgt. Bruckman dested Sergeant Bruckman. "
    "Chewie dested Chewie, Enraged. Antilles Maneuver / Rebel Reinforcements dested "
    "Antilles Maneuver & Rebel Reinforcements. Wedge, RSL dested "
    "Wedge Antilles, Red Squadron Leader. Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "You've Got A Lot Of Guts Coming Here as written. "
    "Additional Chasm / Do, Or Do Not moved to Light shields. "
    "Jabba's Prize kept as extra Character. "
    "Form left column reprints 37-38 on lines 39-40 are Seeking An Audience and Mirax Terrik. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Pistone. Username blank. DARK. "
    "Do not rewrite the 2013 MPC Pistone leftover (Dark is Hunt Down there). "
    "Imperial Occupation / Imp Control dested Imperial Occupation (V) / Imperial Control (V). "
    "Where Are You Taking This ... Thing? dested Where Are You Taking This ... Thing?. "
    "Control & SFS dested Control & Set For Stun. "
    "Black Leader dested Black Leader. "
    "MM & Endor Occupation dested Masterful Move & Endor Occupation. "
    "WIAPN dested We're In Attack Position Now. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "Hoth: MPG (1st Marker) dested Hoth: Main Power Generators (1st Marker). "
    "Hoth: Defensive Perimeter dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth: Ice Plains dested Hoth: Ice Plains (5th Marker). "
    "Hoth: Mountains dested Hoth: Mountains (6th Marker). "
    "U3PO dested U-3PO (Yoo-Threepio). YMSYL dested You May Start Your Landing. "
    "CHYBC dested Come Here You Big Coward. TINT dested There Is No Try. "
    "We'll Let Fate-a Decide Huh? dested We'll Let Fate-a Decide, Huh?. "
    "YCHF dested You Cannot Hide Forever. "
    "Additional YCHF / Oppressive Enforcement / Imperial Detention moved to Dark shields. "
    "Resistance struck then rewritten dested Resistance. "
    "Form left column reprints 37-38 on lines 39-40 are Imperial Command and Flagship Executor. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Captain Han Solo"),
    n("Millennium Falcon", True),
    n("Heading For The Medical Frigate"),
    n("Spaceport City"),
    n("Insurrection & Aim High"),
    n("Wokling", True),
    n("Corellian Engineering Corporation", True),
    n("Home One: Docking Bay"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Scoundrels Guild"),
    n("Imperial Atrocity", True),
    n("Menace Fades"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Lando Calrissian, Unlikely Hero"),
    n("Leia, Rebel Princess", qty=2),
    n("Sergeant Bruckman"),
    n("General Crix Madine"),
    n("Chewie, Enraged", True),
    n("Antilles Maneuver", True),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Corellian Retort", True),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Houjix"),
    n("Grimtaash"),
    n("Escape Pod", True),
    n("You've Got A Lot Of Guts Coming Here"),
    n("Let The Wookiee Win", True, qty=2),
    n("Rebel Barrier", qty=2),
    n("Evacuation Control", True),
    n("Seeking An Audience", True),
    n("Mirax Terrik"),
    n("Dash Rendar", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Palejo Reshad"),
    n("Romas 'Lock' Navander"),
    n("Corran Horn"),
    n("Padme Naberrie", True),
    n("Yoda, Great Warrior", qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Maris Brood, Fallen Jedi"),
    n("Spiral"),
    n("Lady Luck"),
    n("Obi-Wan In Radiant VII"),
    n("No Questions Asked", True, qty=3),
    n("Corellian Slip", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Ultimatum"),
    n("Planetary Defenses", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense", True),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Do, Or Do Not"),
]
LS_ADD = [
    n("Jabba's Prize", True),
]


DS_START = "Imperial Occupation / Imperial Control"
DS_CARDS = [
    n("Imperial Occupation / Imperial Control", True),
    n("Where Are You Taking This ... Thing?"),
    n("Control & Set For Stun"),
    n("No Escape"),
    n("Imperial Command"),
    n("Blizzard 2", True),
    n("Grand Admiral Thrawn"),
    n("Darth Vader", True),
    n("Tempest 1"),
    n("Cyclone Walker", qty=3),
    n("Conquest", True, qty=2),
    n("Grand Moff Tarkin"),
    n("Black Leader"),
    n("Victory", qty=2),
    n("AT-AT Commander"),
    n("Walker Garrison"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Blizzard 4", qty=2),
    n("Veers", True),
    n("Garindan", True),
    n("Jango Fett, The Assassin"),
    n("Trample"),
    n("AT-AT Deployment Platform", qty=2),
    n("Imperial Command"),
    n("Close Call", True),
    n("Cold Feet", True),
    n("Masterful Move & Endor Occupation"),
    n("A Dark Time For The Rebellion", True),
    n("Monnok"),
    n("We're In Attack Position Now", qty=2),
    n("Admiral Piett"),
    n("Imperial Command"),
    n("Flagship Executor"),
    n("Target The Main Generator"),
    n("Prepared Defenses", True),
    n("Commander Igar"),
    n("AT-AT Cannon", True),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("U-3PO (Yoo-Threepio)"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: Ice Plains (5th Marker)", True),
    n("Hoth: Mountains (6th Marker)"),
    n("Image Of The Dark Lord", True),
    n("Hoth Blockade", True),
    n("Hoth"),
    n("Admiral Ozzel", True),
    n("Alert My Star Destroyer!"),
    n("Do They Have A Code Clearance?"),
    n("Fleet Security Protocols"),
    n("Endor Shield", True),
    n("Imperial Decree"),
    n("You May Start Your Landing", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("There Is No Try"),
    n("Firepower", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Death Star Sentry", True),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement"),
    n("Imperial Detention", True),
]
DS_ADD = []
