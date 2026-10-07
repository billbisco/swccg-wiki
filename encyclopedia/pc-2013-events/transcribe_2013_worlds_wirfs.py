#!/usr/bin/env python3
"""2013 World Championship Day 2: Chris Wirfs Hunt Down + Communing."""
from __future__ import annotations

PLAYER = "Chris Wirfs"
USERNAME = "itcouldbewirfs"
LS_USERNAME = ""
DS_USERNAME = "itcouldbewirfs"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 118
DS_PAGE = 117
LS_SCAN = "2013 Worlds Day 2 p118 Chris Wirfs LS.png"
DS_SCAN = "2013 Worlds Day 2 p117 Chris Wirfs DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (uniqueness dots, 12 shields). "
    "Name WIRFS dested Chris Wirfs. Username blank this side. Email blank. LIGHT. "
    "Deck title Save the Wookies!. Event Worlds 2013. "
    "Do not rewrite 2013 MPC leftover WIRFS. "
    "Line 1 overlay There Is Good In Him dested There Is Good In Him / I Can Save Him. "
    "Communing dested Communing. "
    "Nick of Time dested Nick Of Time. "
    "Hoth Echo Command Center dested Hoth: Echo Command Center (War Room). "
    "Tatooine EP1 dested Tatooine: Slave Quarters. "
    "Rebel Trooper dested Rebel Trooper. "
    "General Corlsk Rieekan dested General Carlist Rieekan. "
    "General Crix Madine dested General Crix Madine. "
    "Run Luke Run dested Run Luke, Run!. "
    "Capt Yutani w/ Blaster Cannon dested Captain Yutani With Blaster Cannon. "
    "It's not My Fault dested It's Not My Fault!. "
    "It Behooves in Rad 5 dested Red 5. "
    "All wings Report in / DS dested All Wings Report In & Darklighter Spin. "
    "Lando's Luxury Yacht dested Lady Luck. "
    "Tatooine: Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Tatto's Pit Additional dested Tatooine: Podrace Arena. "
    "Yoda Great Warrior / Escape Pod / Mantellian Savrip / Luke With Lightsaber / "
    "Rebel Leadership / Run Luke, Run! unique overcounts kept sheet-accurate. "
    "Chewbacca Of Kashyyyk (V) on line 14 and without (V) on line 53 kept sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (uniqueness dots, 12 shields). "
    "Name WIRFS dested Chris Wirfs. Username itcouldbewirfs. Email blank. DARK. "
    "Deck title VADER'S CREW. Event Worlds 2013. "
    "Hunt Down (V) dested Hunt Down And Destroy The Jedi (V) / "
    "Their Fire Has Gone Out Of The Universe (V). "
    "Endor Shield dested Endor Shield. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "The Mandalorian, Father dested Jango Fett, The Assassin. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Galen's Fighter dested Rogue Shadow. "
    "Darth Vader, Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Sense & Uncertainty is the Future dested Sense & Uncertain Is The Future. "
    "K & D dested Knowledge And Defense. "
    "We'll Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Ice Heart dested I Have You Now. "
    "Shield 7 Firepower. Additional Battle Order / Secret Plans / Weapon Of A Sith "
    "stay Additional (main already 60). "
    "Galen Marek / Darth Vader, Betrayer / One Beautiful Thing / Emperor Palpatine / "
    "Force Field / We Must Accelerate Our Plans unique overcounts kept sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Communing"),
    n("Master Kenobi"),
    n("Seeking An Audience", True),
    n("Strike Planning"),
    n("Nick Of Time", True),
    n("Home One: War Room"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Slave Quarters"),
    n("Chewbacca's Bowcaster"),
    n("Rebel Trooper"),
    n("Chewbacca Of Kashyyyk", True),
    n("General Carlist Rieekan", True),
    n("Shmi Skywalker"),
    n("General Crix Madine"),
    n("Luke With Lightsaber", qty=2),
    n("Mantellian Savrip", qty=2),
    n("Civil Disorder", True),
    n("Admiral Ackbar", True),
    n("Run Luke, Run!", True, qty=3),
    n("Threepio With His Parts Showing"),
    n("Wedge Antilles", True),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel", True),
    n("A Gift"),
    n("Han With Heavy Blaster Pistol"),
    n("Menace Fades"),
    n("Use The Force"),
    n("Captain Yutani With Blaster Cannon"),
    n("It's Not My Fault", True),
    n("Houjix"),
    n("Escape Pod", True, qty=3),
    n("Lucky Shot", True),
    n("Rebel Leadership", True, qty=2),
    n("Red 5"),
    n("Yoda, Great Warrior", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Hear Me Baby, Hold Together", True),
    n("Imperial Atrocity", True),
    n("Lieutenant Blount", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("K'lor'slug", True),
    n("Home One"),
    n("Lady Luck"),
    n("Chewbacca Of Kashyyyk"),
    n("Colonel Cracken"),
    n("General Solo", True),
    n("Double Agent"),
    n("Jabba's Palace: Audience Chamber"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not"),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here"),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Battle Plan"),
    n("The Professor", True),
]
LS_ADD = [
    n("Tatooine: Podrace Arena"),
    n("Wise Advice"),
    n("Weapons Display"),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Endor Shield", True),
    n("Ni Chuba Na??", True),
    n("A Sith's Weapon", True),
    n("Gift Of The Master"),
    n("Blaster Rack", True),
    n("Imperial Justice", True),
    n("Prepared Defenses", True),
    n("Grand Admiral Thrawn"),
    n("Force Lightning"),
    n("Jango Fett, The Assassin"),
    n("Mara Jade's Lightsaber", True),
    n("Juno Eclipse, Black Leader"),
    n("Rogue Shadow"),
    n("Emperor Palpatine", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", qty=2),
    n("Sense"),
    n("One Beautiful Thing", qty=2),
    n("Lightsaber Deficiency", True),
    n("Vader's Lightsaber"),
    n("Endor"),
    n("General Nevar"),
    n("Galen Marek, Starkiller", qty=3),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Masterful Move & Endor Occupation"),
    n("Dengar With Blaster Carbine"),
    n("Naboo: Theed Palace Generator"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Alter", True),
    n("Force Push", True),
    n("Victory", True),
    n("Weapon Levitation & The Empire's Back"),
    n("Revenge Of The Sith"),
    n("Grand Moff Tarkin", True),
    n("Blockade Flagship: Bridge"),
    n("I Have You Now"),
    n("Force Field", True, qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Blizzard 4"),
    n("Enter The Bureaucrat"),
    n("Cold Feet", True),
    n("Garindan", True),
    n("Cloud City: Downtown Plaza"),
    n("Boba Fett, Bounty Hunter"),
    n("Ghhhk"),
    n("Protocol Failure"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sense & Uncertain Is The Future"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("Death Star Sentry", True),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?"),
    n("Resistance"),
    n("A Useless Gesture"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
]
DS_ADD = [
    n("Battle Order"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
]
