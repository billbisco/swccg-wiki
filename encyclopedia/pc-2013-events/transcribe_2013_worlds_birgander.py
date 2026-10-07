#!/usr/bin/env python3
"""2013 World Championship Day 2: Pär Birgander Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Pär Birgander"
USERNAME = "pbira"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 18
DS_PAGE = 17
LS_SCAN = "2013 Worlds Day 2 p18 Pär Birgander LS.png"
DS_SCAN = "2013 Worlds Day 2 p17 Pär Birgander DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Pär Birgander. Username pbira. "
    "Event Worlds Day 2. Date 08/10/13. LIGHT. "
    "Tatooine: Slave Quarters dested Tatooine: Slave Quarters. "
    "Communing dested Communing. Master Kenobi dested Master Kenobi. "
    "Chewbacca, Protector dested Chewbacca, Protector. "
    "Chewbacca's Bowcaster dested Chewbacca's Bowcaster. "
    "Tatooine (Coruscant) dested as written. "
    "Yoda, Great Warrior dested Yoda, Great Warrior. "
    "Inconsequential Barriers dested Inconsequential Barriers. "
    "Chewie Enraged dested Chewie, Enraged. "
    "Jabba's Palace: Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Commando Training & K'lor'slug dested Commando Training & K'lor'slug. "
    "The Bith Shuffle & Desperate Reach dested The Bith Shuffle & Desperate Reach. "
    "Artoo-Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Tatooine: Obi-Wan's Hut dested Tatooine: Obi-Wan's Hut. "
    "Out of Commission & Transmission Terminated dested "
    "Out Of Commission & Transmission Terminated. "
    "Rebel Gunrunner dested Rebel Gunrunner. "
    "Run Luke, Run dested Run Luke, Run!. "
    "Let The Wookiee Win dested Let The Wookiee Win. "
    "Wookiee Strangle dested Wookiee Strangle. "
    "AFA dested Anger, Fear, Aggression. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Pär Birgander. Username pbira. "
    "Deck title All They Know Is Killing And White Uniforms. DARK. Event Worlds day 2. "
    "Imperial Entanglements / No One To Stop Us dested "
    "Imperial Entanglements / No One To Stop Us This Time. "
    "Tatooine (Premiere) dested Tatooine. "
    "Tatooine: Imperial Occupied Camp dested Tatooine: Imperial Vanguard Camp. "
    "Blaster Rifle dested Blaster Rifle. "
    "Imperial Academy Training dested Imperial Academy Training. "
    "ISB Sector Commander dested ISB Sector Commander. "
    "Ghhhk & Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. "
    "A Dark Time For The Rebellion dested A Dark Time For The Rebellion. "
    "Knowledge And Defense dested Knowledge And Defense. "
    "We'll Let Fate Decide dested We'll Let Fate-A Decide, Huh?. "
    "I Find Your Lack Of Faith Disturbing dested I Find Your Lack Of Faith Disturbing. "
    "Line 54 struck dested Control. "
    "You Cannot Hide Forever dested You Cannot Hide Forever. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Wokling", True),
    n("Home One"),
    n("Admiral Ackbar", True),
    n("Draw Their Fire"),
    n("Chewbacca, Protector", qty=2),
    n("Escape Pod", True, qty=3),
    n("Houjix", qty=2),
    n("Civil Disorder", True),
    n("Chewbacca's Bowcaster"),
    n("Corran Horn"),
    n("Tatooine (Coruscant)"),
    n("Yoda, Great Warrior"),
    n("Launching The Assault"),
    n("Inconsequential Barriers"),
    n("A Gift"),
    n("Shmi Skywalker"),
    n("Chewie, Enraged", True, qty=2),
    n("Leia, Rebel Princess"),
    n("Jabba's Palace: Audience Chamber"),
    n("Commando Training & K'lor'slug"),
    n("Jedi Levitation", True),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("The Bith Shuffle & Desperate Reach"),
    n("Artoo-Detoo In Red 5"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Threepio With His Parts Showing"),
    n("Luke With Lightsaber", qty=2),
    n("Strikeforce", True),
    n("Imperial Atrocity", True),
    n("Use The Force"),
    n("Rebel Gunrunner"),
    n("Out Of Commission & Transmission Terminated"),
    n("Republic Gunship"),
    n("Lando Calrissian, Scoundrel", True),
    n("Home One: War Room"),
    n("Out Of Commission"),
    n("Rebel Leadership", True, qty=3),
    n("Run Luke, Run!", True, qty=3),
    n("Let The Wookiee Win", True, qty=3),
    n("Hear Me Baby, Hold Together", True),
    n("Use The Force"),
    n("Wookiee Strangle"),
    n("Boushh"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense", True),
    n("Your Insight Serves You Well", True),
    n("Jabba's Prize", True),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
]
LS_ADD = [
    n("Do, Or Do Not"),
    n("Wise Advice"),
    n("The Professor"),
]


DS_START = "Imperial Entanglements / No One To Stop Us This Time"
DS_CARDS = [
    n("Imperial Entanglements / No One To Stop Us This Time", True),
    n("Tatooine"),
    n("Devastator"),
    n("Tatooine: Imperial Vanguard Camp", True),
    n("Prepared Defenses"),
    n("Blaster Rifle", True),
    n("Imperial Stockpile"),
    n("Endor Shield", True),
    n("Imperial Academy Training", True),
    n("Imperial Stormtrooper", True, qty=6),
    n("Elite Squadron Stormtrooper", True, qty=4),
    n("Close Call", True, qty=2),
    n("Imperial Command", qty=3),
    n("Intensify The Forward Batteries", qty=3),
    n("Operational As Planned", True),
    n("Outflank", True, qty=2),
    n("Tatooine Occupation", qty=2),
    n("Imperial Domination", True, qty=2),
    n("Laser Cannon Battery"),
    n("Protocol Failure"),
    n("Deflector Shield Generators", True),
    n("Grand Admiral Thrawn"),
    n("ISB Sector Commander", True),
    n("Admiral Piett"),
    n("Admiral Motti", True),
    n("Commander Daine Jir"),
    n("Trooper Assault", qty=2),
    n("Coordinated Attack", True, qty=2),
    n("Grand Moff Tarkin", True),
    n("Blast Points"),
    n("Lightsaber Deficiency", True),
    n("Strategic Reserves", True),
    n("Tatooine: Mos Eisley"),
    n("Tatooine: Mos Espa"),
    n("Tatooine: Watto's Junkyard"),
    n("Control", True),
    n("Wounded Warrior", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("A Dark Time For The Rebellion"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Fanfare", True),
    n("Allegations Of Corruption", True),
    n("There Is No Try", True),
    n("Secret Plans"),
    n("Come Here You Big Coward", True),
    n("Firepower", True),
    n("Battle Order"),
    n("Imperial Detention", True),
    n("Resistance"),
    n("We'll Let Fate-A Decide, Huh?"),
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
DS_ADD = [
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Abyss", True),
]
