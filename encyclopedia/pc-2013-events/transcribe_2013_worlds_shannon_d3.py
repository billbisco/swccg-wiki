#!/usr/bin/env python3
"""2013 World Championship Day 3: Kevin Shannon Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Kevin Shannon"
USERNAME = ""
STAGE = "Day 3"
PDF = "2013 Worlds Day 3.pdf"
LS_PAGE = 12
DS_PAGE = 11
LS_SCAN = "2013 Worlds Day 3 p12 Kevin Shannon LS.png"
DS_SCAN = "2013 Worlds Day 3 p11 Kevin Shannon DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name James Shenanigans. Username blank. "
    "LIGHT/DARK boxes empty. Dest Kevin Shannon. "
    "Tatooine: Slave Quarters dested Tatooine: Slave Quarters. "
    "Maneuvering Flaps + Nick of Time dested Maneuvering Flaps & Nick Of Time. "
    "EBO Echo Base Garrison dested Echo Base Garrison. "
    "Commander Wedge Antilles dested Commander Wedge Antilles. "
    "Obi's Hut dested Tatooine: Obi-Wan's Hut. "
    "Don't Underestimate Our Chances dested Don't Underestimate Our Chances. "
    "Lev Zensun dested Lev Zensun as written. "
    "Jabba's Palace: Entrance dested Jabba's Palace: Entrance Cavern. "
    "Doyle dested Dodge. "
    "Wedge Antilles, Red Sq Led dested Wedge Antilles, Red Squadron Leader. "
    "Threepio Naked dested Threepio With His Parts Showing. "
    "Chewbacca Protector dested Chewbacca, Protector. "
    "Dual Laser Cannon dested Dual Laser Cannon. "
    "Someone Who Loves You dested Someone Who Loves You. "
    "Lando Calrissian Scoundrel dested Lando Calrissian, Scoundrel. "
    "R2 in Red 5 dested Artoo-Detoo In Red 5. "
    "Your Ship dested Your Ship?. "
    "Form left column lines 39–40 are sheet lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Kevin Shannon. Username blank. "
    "LIGHT/DARK boxes empty. Dest Kevin Shannon. "
    "SYCFA dested Set Your Course For Alderaan / The Ultimate Power In The Universe. "
    "Death Star: DB dested Death Star: Docking Bay 327. "
    "K. Flex dested Kiffex. "
    "4-LOM w/ gun dested 4-LOM With Concussion Rifle. "
    "Lightsaber Def dested Lightsaber Deficiency. "
    "Judicator dested Judicator. "
    "CPI dested Commence Primary Ignition. "
    "Control & Set for Stun dested Control & Set For Stun. "
    "Force Field dested Force Field. "
    "Why Didn't You Tell Me dested Why Didn't You Tell Me?. "
    "You Swindled Me dested You Swindled Me!. "
    "Nevar Yalnal dested Nevar Yalnal. "
    "Tarkin Doctrine dested Tarkin Doctrine. "
    "We'll Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Form left column lines 39–40 are sheet lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Maneuvering Flaps & Nick Of Time"),
    n("Wokling", True),
    n("Echo Base Garrison"),
    n("General Solo", True, qty=2),
    n("Commander Wedge Antilles", True),
    n("Rebel Leadership", True, qty=3),
    n("Menace Fades"),
    n("Rogue 3"),
    n("Admiral Ackbar", True),
    n("Seeking An Audience", True),
    n("Shmi Skywalker"),
    n("Commander Luke Skywalker", True),
    n("Commander Luke Skywalker"),
    n("Lando's Luxury Yacht", True),
    n("Rogue 2"),
    n("Padme Naberrie", True),
    n("Imperial Atrocity", True),
    n("Crash Site Memorial"),
    n("Projection Of A Skywalker"),
    n("Don't Underestimate Our Chances"),
    n("Home One: War Room"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("It's Not My Fault", True, qty=2),
    n("Lev Zensun"),
    n("Jabba's Palace: Entrance Cavern"),
    n("Let The Wookiee Win", True, qty=2),
    n("Dodge"),
    n("Escape Pod", True, qty=2),
    n("Rebel Commander"),
    n("Republic Gunship", qty=2),
    n("Corran Horn", qty=2),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Threepio With His Parts Showing"),
    n("Yoda, Great Warrior", True),
    n("Power Harpoon"),
    n("Tatooine"),
    n("Chewbacca, Protector", True),
    n("Dual Laser Cannon", True),
    n("Home One"),
    n("Rogue 4"),
    n("Houjix"),
    n("Someone Who Loves You", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Alderaan Consular Ship", True),
    n("Artoo-Detoo In Red 5"),
    n("Rogue 1"),
    n("Tatooine: Jundland Wastes"),
    n("Echo Base Operations"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("The Professor", True),
    n("Do, Or Do Not"),
    n("Weapons Display", True),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Your Insight Serves You Well"),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Your Ship?"),
]
LS_ADD = [
    n("A Tragedy Has Occurred"),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
]


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Kuat Drive Yards", True),
    n("Imperial Stockpile"),
    n("A Million Voices Crying Out"),
    n("Prepared Defenses", True),
    n("Laser Cannon Battery"),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Kiffex"),
    n("Death Star: Central Core", True),
    n("Corulag"),
    n("Superlaser"),
    n("Rendili"),
    n("Death Star: War Room", True),
    n("U-3PO (Yoo-Threepio)"),
    n("Lord Sidious"),
    n("Darth Sidious", qty=2),
    n("Arica"),
    n("Garindan", True),
    n("4-LOM With Concussion Rifle", True),
    n("Lightsaber Deficiency", True, qty=2),
    n("Gravity Shadow"),
    n("Judicator", qty=2),
    n("Victory"),
    n("Accuser"),
    n("Thunderflare"),
    n("Tyrant"),
    n("Conquest", True),
    n("Stalker", True),
    n("Devastator", True),
    n("Commence Primary Ignition", True),
    n("Control & Set For Stun", qty=2),
    n("Force Field", True),
    n("Why Didn't You Tell Me?", True),
    n("Close Call", True),
    n("Ghhhk"),
    n("Cold Feet", True),
    n("Force Push", True),
    n("Imperial Barrier"),
    n("Masterful Move"),
    n("TIE Sentry Ships", True),
    n("Intensify The Forward Batteries", qty=2),
    n("Relentless Pursuit", qty=2),
    n("Flawless Marksmanship", qty=3),
    n("Imperial Propaganda", True),
    n("Lateral Damage"),
    n("Tarkin Doctrine"),
    n("You Swindled Me!", True),
    n("Nevar Yalnal"),
    n("Protocol Failure"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("Battle Order"),
    n("Resistance"),
    n("There Is No Try"),
    n("A Useless Gesture", True),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
]
DS_ADD = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("We'll Let Fate-a Decide, Huh?", True),
]
