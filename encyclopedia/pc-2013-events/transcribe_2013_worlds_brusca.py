#!/usr/bin/env python3
"""2013 World Championship Day 2: Victor G. Brusca Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Victor G. Brusca"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 21
DS_PAGE = 22
LS_SCAN = "2013 Worlds Day 2 p21 Victor G. Brusca LS.png"
DS_SCAN = "2013 Worlds Day 2 p22 Victor G. Brusca DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Victor G. Brusca. Username blank. "
    "LIGHT. Communing. Lines 59–60 empty on the sheet (58 in the 60). "
    "We're Jamming dested as written. "
    "Maris Brood, Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Wedge Antilles, Red Squadron dested Wedge Antilles, Red Squadron Leader. "
    "A vengeance in the Force dested Presence Of The Force. "
    "Rug Hug dested Rug Hug. "
    "Han With Heavy Blaster dested Han With Heavy Blaster Pistol. "
    "Threepio With Parts Showing dested Threepio With His Parts Showing. "
    "Chewbacca's Bowcaster dested Chewbacca's Bowcaster. "
    "Run Luke, Run dested Run Luke, Run!. "
    "Don't Forget The Droids dested Don't Forget The Droids. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Victor G. Brusca. Username blank. "
    "DARK. Hunt Down And Destroy The Jedi. "
    "Weapon Levitation & The Empire's B dested Weapon Levitation & The Empire's Back. "
    "Boba Fett, Bounty Hunter dested Boba Fett, Bounty Hunter. "
    "Sith Fury & End This Destructive dested Sith Fury & End This Destructive Conflict. "
    "Blackside Flagship Bridge dested Blockade Flagship: Bridge. "
    "Cyborg Commander, Hunter of Jedi dested as written. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Naboo: Theed Palace Generator dested Naboo: Theed Palace Generator. "
    "They're Still Coming Through dested They're Still Coming Through!. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Communing", True),
    n("Tatooine: Slave Quarters"),
    n("Master Kenobi", True),
    n("Wokling", True),
    n("We're Jamming"),
    n("Anger, Fear, Aggression", True),
    n("Bright Hope", True),
    n("Tantive IV", True),
    n("Chewbacca, Protector"),
    n("Chewbacca, Protector", True),
    n("Home One"),
    n("Spiral"),
    n("Luke With Lightsaber", qty=3),
    n("Maris Brood, Fallen Jedi", True),
    n("Yoda, Great Warrior", True),
    n("Leia, Rebel Princess"),
    n("Han With Heavy Blaster Pistol"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Dash Rendar", True),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Padme Naberrie"),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Chewbacca's Bowcaster", True),
    n("Rebel Gunrunner"),
    n("Draw Their Fire"),
    n("Menace Fades"),
    n("Launching The Assault"),
    n("Tatooine Celebration", True),
    n("Seeking An Audience"),
    n("Presence Of The Force"),
    n("Imperial Atrocity", True),
    n("Run Luke, Run!", True, qty=3),
    n("Houjix"),
    n("Don't Forget The Droids", True),
    n("Hear Me Baby, Hold Together", True),
    n("Desperate Reach", True),
    n("Rug Hug"),
    n("Let The Wookiee Win"),
    n("Let The Wookiee Win", True),
    n("Use The Force", True, qty=2),
    n("Captive Pursuit", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Tatooine"),
    n("Tatooine: Obi-Wan's Hut"),
    n("Tatooine: Cantina"),
    n("Tatooine: Mos Eisley"),
    n("Home One: War Room"),
    n("Chewbacca, Protector"),
]
LS_SHIELDS = [
    n("Chasm"),
    n("A Tragedy Has Occurred"),
    n("Wise Advice"),
    n("Ultimatum"),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("Don't Do That Again"),
    n("Traffic Control"),
    n("Yavin Sentry"),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display"),
    n("Let's Keep A Little Optimism Here"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("A Sith's Plans", True),
    n("Coruscant: Imperial City"),
    n("Prepared Defenses", True),
    n("Gift Of The Master", True),
    n("Ni Chuba Na??"),
    n("Endor Shield", True),
    n("Knowledge And Defense", True),
    n("Sniper & Dark Strike"),
    n("Weapon Levitation & The Empire's Back", True),
    n("Force Lightning"),
    n("Hoth: Defensive Perimeter"),
    n("Boba Fett, Bounty Hunter"),
    n("Grand Moff Tarkin", True),
    n("Masterful Move & Endor Occupation", True),
    n("Cold Feet", True),
    n("Sith Fury & End This Destructive Conflict", True),
    n("No Escape"),
    n("Ghhhk"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Vader's Lightsaber"),
    n("Blast Door Controls"),
    n("Blizzard 4"),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Rogue Shadow", True),
    n("They're Still Coming Through!"),
    n("Galen Marek, Starkiller"),
    n("Emperor's Power", True),
    n("Force Field", True),
    n("General Nevar"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Naboo: Theed Palace Generator"),
    n("Endor"),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Bridge"),
    n("Imperial Justice", True),
    n("Blaster Rack", True),
    n("Cyborg Commander, Hunter Of Jedi", True, qty=2),
    n("Dengar With Blaster Carbine", True),
    n("Victory", True),
    n("Grand Admiral Thrawn"),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("We Must Accelerate Our Plans"),
    n("Galen Marek, Starkiller"),
    n("Juno Eclipse, Black Leader", True),
    n("Emperor Palpatine"),
    n("Jango Fett, The Assassin"),
    n("Dark Jedi Lightsaber", True),
    n("We Must Accelerate Our Plans"),
    n("Emperor Palpatine", True),
    n("Alter", True),
    n("Revenge Of The Sith", True),
    n("Force Push", True),
    n("Galen Marek, Starkiller", True),
    n("Garindan"),
    n("Close Call"),
    n("Sonic Bombardment", qty=2),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Imperial Detention", True),
    n("Do They Have A Code Clearance?"),
    n("Come Here You Big Coward", True),
    n("Battle Order"),
    n("A Useless Gesture"),
    n("Allegations Of Corruption"),
]
DS_ADD = [
    n("Abyss", True),
]
