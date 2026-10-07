#!/usr/bin/env python3
"""2013 World Championship Day 2: Schwartz Xerox Wookiee Slaving + Profit."""
from __future__ import annotations

PLAYER = "Schwartz"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 84
DS_PAGE = 83
LS_SCAN = "2013 Worlds Day 2 p84 Schwartz LS.png"
DS_SCAN = "2013 Worlds Day 2 p83 Schwartz DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Schwartz. Username blank. LIGHT. "
    "Deck title why can't I play a Dark Dark Deck?. "
    "Do not dest as Matt Schmaltz; Username is blank. "
    "Be Destroyed / Profit dested You Can Either Profit By This... / Or Be Destroyed. "
    "Have Me dested Home One. Luke Skywalker SitForce dested Son Of Skywalker. "
    "3PO with Parts Showing dested Threepio With His Parts Showing. "
    "Lando Scoundrel dested Lando Calrissian, Scoundrel. "
    "Ackbar dested Admiral Ackbar. Stop! Stop! dested as written. "
    "Swing + A Miss dested Swing-And-A-Miss. "
    "Additional Wise Advice / Let's Keep A Little Optimism Here / "
    "He Can Go About His Business moved to Light shields. "
    "Form left column reprints 37-38 on lines 39-40 are Let The Wookiee Win x2. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Schwartz. Username blank. DARK. "
    "Deck title I NAME TOM HAID. The 60 is Schwartz's Wookiee Slaving list. "
    "Do not dest as Tom Haid. Do not dest as Matt Schmaltz. "
    "Wookiee Slaving Ops dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Nat Hutta dested Nal Hutta. Ability x3 dested Ability, Ability, Ability. "
    "Jango Father of Fett dested Jango Fett, The Assassin. "
    "Bossk w Mortar Gun dested Bossk With Mortar Gun. "
    "Dengar w Blaster Carbine dested Dengar With Blaster Carbine. "
    "Reegesk dested Reegesk. Look Sir Droids dested Look Sir, Droids. "
    "Additional Allegations Of Corruption / Do They Have A Code Clearance? / "
    "Abyss moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40 are Ephant Mon and Reegesk. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "You Can Either Profit By This... / Or Be Destroyed"
LS_CARDS = [
    n("You Can Either Profit By This... / Or Be Destroyed"),
    n("Tatooine: Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Tatooine Utility Belt", True),
    n("Jedi Lightsaber", True),
    n("Obi-Wan's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Han Solo", True),
    n("Corran Horn"),
    n("Yoda, Great Warrior", qty=2),
    n("Chewbacca, Protector"),
    n("Padme Naberrie", True),
    n("Threepio With His Parts Showing"),
    n("Lando Calrissian, Scoundrel"),
    n("Admiral Ackbar", True),
    n("Dash Rendar", True),
    n("Obi-Wan Kenobi", qty=2),
    n("Son Of Skywalker", qty=3),
    n("Boushh"),
    n("Home One"),
    n("Seeking An Audience", True),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Disarmed"),
    n("A Gift"),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("Let The Wookiee Win", True, qty=4),
    n("Rebel Leadership", True, qty=3),
    n("Wesa Gotta Grand Army", qty=2),
    n("Jedi Levitation", True, qty=2),
    n("Sense", qty=2),
    n("Clash Of Sabers", qty=2),
    n("Blaster Deflection"),
    n("NOOOOOOOOOOOO!", True),
    n("Double Agent"),
    n("Stop! Stop!", True),
    n("Speak With The Jedi Council"),
    n("Lucky Shot", True),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Swing-And-A-Miss"),
    n("Inconsequential Barriers"),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Only Jedi Carry That Weapon"),
    n("Battle Plan"),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
    n("He Can Go About His Business", True),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Laser Cannon Battery"),
    n("Jabba's Space Cruiser", True),
    n("Jabba's Sail Barge", True),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Nal Hutta"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Kashyyyk: Skyhook Platform"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Kashyyyk"),
    n("Ability, Ability, Ability"),
    n("Protocol Failure"),
    n("Hutt Bounty", True),
    n("Scum And Villainy"),
    n("Mercenary Slavers"),
    n("Breached Defenses & Molator"),
    n("Jabba's Haven"),
    n("Den Of Thieves & Special Delivery"),
    n("Power Of The Hutt"),
    n("Knowledge And Defense", True),
    n("Outer Rim Scout", qty=5),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Garindan", True),
    n("Bossk With Mortar Gun", True),
    n("Ponda Baba", True),
    n("4-LOM With Concussion Rifle"),
    n("Dr. Evazan"),
    n("Velken Tezeri", True),
    n("Prince Xizor"),
    n("Ket Maliss, Shadow Killer"),
    n("Jabba The Hutt", True),
    n("Ephant Mon"),
    n("Reegesk", True),
    n("Probot"),
    n("Lady Valarian"),
    n("Dengar With Blaster Carbine"),
    n("Mercenary Pilot"),
    n("Lightsaber Deficiency", True, qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("Abyssin Ornament", qty=2),
    n("Imperial Barrier", qty=3),
    n("Wookiee Subjugation"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Force Push"),
    n("P-59"),
    n("Look Sir, Droids"),
]
DS_SHIELDS = [
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever"),
    n("Secret Plans"),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Firepower"),
    n("Oppressive Enforcement"),
    n("Fanfare"),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?"),
    n("Abyss"),
]
DS_ADD = []
