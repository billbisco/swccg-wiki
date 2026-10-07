#!/usr/bin/env python3
"""2013 World Championship Day 2: Jack Koswicki Xerox Endor Ops + TIGIH."""
from __future__ import annotations

PLAYER = "Jack Koswicki"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 55
DS_PAGE = 54
LS_SCAN = "2013 Worlds Day 2 p55 Jack Koswicki LS.png"
DS_SCAN = "2013 Worlds Day 2 p54 Jack Koswicki DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Jack Koswicki. Username blank. "
    "Event blank. LIGHT. There Is Good In Him. "
    "There is good in him dested There Is Good In Him / I Can Save Him. "
    "Luke Rebel Scout dested Luke Skywalker, Rebel Scout. "
    "Endor landing platform dested Endor: Landing Platform (Docking Bay). "
    "Endor Chief Chirpa's Hut dested Endor: Chief Chirpa's Hut. "
    "Jedi Council Chamber dested Coruscant: Jedi Council Chamber. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel. "
    "Han Innocent Scoundrel dested Han Solo, Innocent Scoundrel. "
    "Obi with saber dested Obi-Wan With Lightsaber. "
    "11-4D as written. "
    "Threepio with parts dested Threepio With His Parts Showing. "
    "Crix Madine dested General Crix Madine. "
    "Ackbar dested Admiral Ackbar. "
    "Chewie Enraged dested Chewie, Enraged. "
    "Yoda Master of the Force dested Yoda, Master Of The Force. "
    "Speak with Council dested Speak With The Jedi Council. "
    "Impressive Most Impressive dested Impressive, Most Impressive. "
    "Nocoo! as written. "
    "Force strong with this one dested The Force Is Strong With This One. "
    "Han's Blaster Pistol dested Han's Heavy Blaster Pistol. "
    "Luke's Hand dested Luke's Bionic Hand. "
    "Naboo Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Form left column reprints 37-38 on lines 39-40 are Nocoo! / Insertion Planning. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Jack Koswicki. Username blank. "
    "Event blank. DARK. Endor Ops. "
    "Endor Ops dested Endor Operations / Imperial Outpost. "
    "Establish Control dested Establish Control (Effect, not the 7-side). "
    "Dreaded Imp Starfleet dested Dreaded Imperial Starfleet. "
    "Imp Arrest Order dested Imperial Arrest Order. "
    "Endor Bunker dested Endor: Bunker. "
    "Endor Landing Platform dested Endor: Landing Platform (Docking Bay). "
    "Emperor's Shield dested The Emperor's Shield. "
    "Avenger dested Avenger. "
    "Ozzel dested Admiral Ozzel. "
    "Thrawn dested Grand Admiral Thrawn. "
    "Father Darth Vader dested Darth Vader. "
    "Latent Damage dested Lateral Damage. "
    "Vader with stick dested Darth Vader With Lightsaber. "
    "Gilad Pellaeon dested Captain Gilad Pellaeon. "
    "Cabbel dested Lieutenant Cabbel. "
    "Tyrant (not virtual) dested Tyrant. "
    "Lennox dested Captain Lennox. "
    "Control + Set For Stun dested Control & Set For Stun. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Forgot Ops as written. "
    "Form left column reprints 37-38 on lines 39-40 are Ominous Rumors / Establish Secret Base. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "There Is Good In Him / I Can Save Him"
LS_CARDS = [
    n("There Is Good In Him / I Can Save Him"),
    n("Heading For The Medical Frigate"),
    n("Strike Planning"),
    n("Squadron Assignments"),
    n("Sai'torr Kal Fas", True),
    n("Luke Skywalker, Rebel Scout", True),
    n("I Feel The Conflict"),
    n("Luke's Lightsaber"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor: Chief Chirpa's Hut"),
    n("Coruscant: Jedi Council Chamber", True),
    n("I'm With You Too", True),
    n("Lando Calrissian, Scoundrel"),
    n("Han Solo, Innocent Scoundrel"),
    n("Obi-Wan With Lightsaber"),
    n("11-4D"),
    n("Maris Brood, Fallen Jedi"),
    n("Corran Horn"),
    n("Dash Rendar", True),
    n("Padme Naberrie", True),
    n("Leia, Rebel Princess"),
    n("Threepio With His Parts Showing"),
    n("General Crix Madine"),
    n("Admiral Ackbar", True),
    n("Elegant Lightsaber"),
    n("Chewie, Enraged"),
    n("Mace Windu", True),
    n("Major Panno"),
    n("Yoda, Master Of The Force"),
    n("Dark Approach", True),
    n("A Jedi's Resilience"),
    n("Let The Wookiee Win", True),
    n("Nabrun Leids"),
    n("Speak With The Jedi Council"),
    n("Wesa Gotta Grand Army"),
    n("Rebel Barrier"),
    n("Blaster Deflection"),
    n("Impressive, Most Impressive", True),
    n("Nocoo!"),
    n("Insertion Planning"),
    n("Anger, Fear, Aggression", True),
    n("Escape Pod", True),
    n("It's A Trap!"),
    n("Houjix"),
    n("The Force Is Strong With This One"),
    n("Insertion Planning"),
    n("Rebel Leadership"),
    n("It Could Be Worse"),
    n("Wesa Gotta Grand Army"),
    n("Han's Heavy Blaster Pistol", True),
    n("Endor"),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One"),
    n("Outrider"),
    n("Lightsaber Proficiency"),
    n("Scrambled Transmission", True),
    n("Jedi Lightsaber", True),
    n("Obi-Wan's Journal"),
    n("Luke's Bionic Hand"),
    n("Smoke Screen"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred", True),
    n("Aim High", True),
    n("Battle Plan", True),
    n("Weapons Display", True),
    n("Do, Or Do Not", True),
    n("Wise Advice", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("The Professor", True),
    n("Ounee Ta", True),
]
LS_ADD = []


DS_START = "Endor Operations / Imperial Outpost"
DS_CARDS = [
    n("Endor Operations / Imperial Outpost"),
    n("Establish Control"),
    n("Prepared Defenses"),
    n("Dreaded Imperial Starfleet", True),
    n("Imperial Arrest Order"),
    n("Endor: Bunker"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Endor"),
    n("Tarkin's Bounty", True),
    n("Endor Shield", True),
    n("Chimaera"),
    n("Grand Admiral Thrawn"),
    n("The Emperor's Shield"),
    n("Blizzard 2"),
    n("Avenger"),
    n("Blockade Flagship"),
    n("Imperial Domination", True),
    n("Admiral Ozzel"),
    n("Arica"),
    n("Blizzard 2", True),
    n("Veers", True),
    n("Relentless Pursuit"),
    n("Conquest", True),
    n("Commander Praji", True),
    n("Devastator", True),
    n("We're In Attack Position Now"),
    n("Judicator"),
    n("We're In Attack Position Now"),
    n("Blizzard 4"),
    n("Darth Vader", True),
    n("Dominator", True),
    n("Officer Evax"),
    n("Executor"),
    n("Accuser", True),
    n("Warrant Officer M'Kae", True),
    n("They've Shut Down The Main Reactor"),
    n("Tyrant"),
    n("Captain Lennox", True),
    n("Ominous Rumors"),
    n("Establish Secret Base", True),
    n("Lateral Damage"),
    n("Imperial Decree"),
    n("Lieutenant Cabbel"),
    n("Major Rhymer"),
    n("Darth Vader With Lightsaber"),
    n("Captain Gilad Pellaeon"),
    n("Kashyyyk"),
    n("Darth Vader With Lightsaber"),
    n("You Cannot Hide Forever"),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("Masterful Move"),
    n("Captain Godherdt"),
    n("DS-61-2"),
    n("We Must Accelerate Our Plans"),
    n("They've Shut Down The Main Reactor"),
    n("Control & Set For Stun"),
    n("Tempest 1"),
    n("Imperial Decree", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption", True),
    n("Secret Plans", True),
    n("Reactor Terminal", True),
    n("A Useless Gesture"),
    n("Firepower", True),
    n("There Is No Try", True),
    n("Death Star Sentry", True),
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("Battle Order", True),
    n("Forgot Ops"),
    n("Forgot Ops"),
]
DS_ADD = []
