#!/usr/bin/env python3
"""2013 World Championship Day 2: Steve Skilton Xerox Wookiee Slaving + Profit."""
from __future__ import annotations

PLAYER = "Steve Skilton"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 88
DS_PAGE = 87
LS_SCAN = "2013 Worlds Day 2 p88 Steve Skilton LS.png"
DS_SCAN = "2013 Worlds Day 2 p87 Steve Skilton DS.png"
PUBLIC_NOTE = "Name box on the Day 2 sheet is the Username stevetotheizzo."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name box stevetotheizzo. Username blank. LIGHT. "
    "Deck title DC told me to play Profit. Dest as Steve Skilton. "
    "Do not rewrite the 2013 MPC or SoCal Steve Skilton leftovers. "
    "Profit dested You Can Either Profit By This... / Or Be Destroyed. "
    "Luke SITF dested Son Of Skywalker. cal III Lando dested Lando Calrissian, Scoundrel. "
    "show show dested Stop! Stop!. Swing + a miss dested Swing-And-A-Miss. "
    "Still coming thru dested They're Still Coming Through!. "
    "Obi-wan L dested Obi-Wan Kenobi. "
    "Additional Insight / Optimism / Simple Tricks moved to Light shields. "
    "Form left column reprints 37-38 on lines 39-40 are Double Agent and Stop! Stop!. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name box stevetotheizzo. Username blank. DARK. "
    "Deck title Tom Haid's Little Slaver Friends. Dest as Steve Skilton. Do not dest as Tom Haid. "
    "Slaver objective on line 58 dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Nal Hutta dested Nal Hutta. Ability x3 dested Ability, Ability, Ability. "
    "Jangolorian FoF dested Jango Fett, The Assassin. "
    "Dengar w Gun dested Dengar With Blaster Carbine. "
    "Bossk w Gun dested Bossk With Mortar Gun. "
    "Reegesk dested Reegesk. "
    "Line 28 Blown Barrier struck; Look sir Droids dested Look Sir, Droids. "
    "Additional Abyss / Allegations Of Corruption / Fanfare moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40 are Dr. Evazan and Bossk With Mortar Gun. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Han Solo", True),
    n("Boushh"),
    n("Threepio With His Parts Showing"),
    n("Chewbacca, Protector"),
    n("Padme Naberrie", True),
    n("Dash Rendar", True),
    n("Corran Horn"),
    n("Lando Calrissian, Scoundrel"),
    n("Admiral Ackbar", True),
    n("Yoda, Great Warrior", qty=2),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Son Of Skywalker", qty=3),
    n("Home One"),
    n("Tatooine Utility Belt", True),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Home One: War Room"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Disarmed"),
    n("A Gift"),
    n("Sai'torr Kal Fas"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Sense", qty=2),
    n("Blaster Deflection"),
    n("Jedi Levitation", True, qty=2),
    n("Double Agent"),
    n("Stop! Stop!"),
    n("Speak With The Jedi Council"),
    n("NOOOOOOOOOOOO!", True),
    n("Clash Of Sabers", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=2),
    n("Let The Wookiee Win", True, qty=4),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Lucky Shot"),
    n("Swing-And-A-Miss"),
    n("Heading For The Medical Frigate"),
    n("They're Still Coming Through!"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("He Can Go About His Business"),
    n("Ultimatum"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Aim High"),
    n("Don't Do That Again", True),
    n("Yavin Sentry"),
    n("The Professor"),
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("Weapons Display"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here"),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Mercenary Slavers"),
    n("Breached Defenses & Molator"),
    n("Nal Hutta"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Kashyyyk: Skyhook Platform"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Protocol Failure"),
    n("Power Of The Hutt"),
    n("Hutt Bounty"),
    n("Ability, Ability, Ability"),
    n("Jabba's Haven"),
    n("Scum And Villainy"),
    n("Den Of Thieves & Special Delivery"),
    n("Lightsaber Deficiency", True, qty=3),
    n("Imperial Barrier", qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("Abyssin Ornament", qty=2),
    n("Force Push", True),
    n("Look Sir, Droids"),
    n("Wookiee Subjugation", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Outer Rim Scout", qty=5),
    n("Reegesk"),
    n("Lady Valarian"),
    n("Boba Fett, Prepared Hunter"),
    n("Dr. Evazan"),
    n("Bossk With Mortar Gun", True),
    n("Dengar With Blaster Carbine", True),
    n("Velken Tezeri", True),
    n("Prince Xizor"),
    n("Mercenary Pilot"),
    n("Garindan", True),
    n("Ponda Baba", True),
    n("4-LOM With Concussion Rifle"),
    n("Probot"),
    n("Jango Fett, The Assassin"),
    n("Ket Maliss, Shadow Killer"),
    n("P-59"),
    n("Ephant Mon"),
    n("Jabba The Hutt", True),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Jabba's Space Cruiser", True),
    n("Jabba's Sail Barge", True),
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Laser Cannon Battery"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?"),
    n("Oppressive Enforcement"),
    n("Secret Plans"),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("A Useless Gesture", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Firepower"),
    n("Do They Have A Code Clearance?"),
    n("Abyss"),
    n("Allegations Of Corruption"),
    n("Fanfare"),
]
DS_ADD = []
