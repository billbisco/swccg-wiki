#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 typed GEMP: Nate Lowderback.

Source: MPC-2014-Day-1-Main-Event.pdf pages 77–79 (typed GEMP).
Username dorshe1.
"""
from __future__ import annotations

PLAYER = "Nate Lowderback"
USERNAME = "dorshe1"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 79
DS_PAGE = 77
LS_SCAN = "2014 Match Play Championship Day 1 Nate Louderback LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Nate Louderback DS.png"
LS_DECK_NAME = "Nate.Communing"
DS_DECK_NAME = "Nate.HDv"
NOTE = "Typed GEMP list. Dark page 2 of 2 p78 is starting cards."
LS_NOTE = (
    "Typed GEMP. Username dorshe1. Communing. Only Jedi Carry That Weapon crossed, "
    "Let's Keep A Little Optimism Here (V) dested Let's Keep A Little Optimism Here "
    "(V). Unique * is uniqueness, not (V). (V) from written (V). Unique overcounts "
    "sheet-accurate (Chewbacca, Protector (V) x2, Chewie, Enraged (V) x2, Luke With "
    "Lightsaber x2, Artoo-Detoo In Red 5 x2, Escape Pod (V) x3, Houjix x2, Run Luke, "
    "Run! (V) x2, Rebel Leadership (V) x3, Let The Wookiee Win (V) x2, Use The Force "
    "x2). Anger, Fear, Aggression (V) dested in the 60 as starting Effect."
)
DS_NOTE = (
    "Typed GEMP. Username dorshe1. Hunt Down And Destroy The Jedi / Their Fire Has "
    "Gone Out Of The Universe (V) on p78 with A Sith's Plans, Ni Chuba Na?? (V), "
    "Endor Shield (V), Gift Of The Master. Fanfare (Tatooine) (V) dested Fanfare (V). "
    "Juno Eclipse, Black Leader (AI) dested Juno Eclipse, Black Leader. Galen's "
    "Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. Unique "
    "overcounts sheet-accurate (We Must Accelerate Our Plans x3, One Beautiful Thing "
    "x2, Emperor Palpatine x2, Galen Marek, Starkiller x3, Darth Vader, Dark Lord Of "
    "The Sith x2). (V) from written (V)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("K'lor'slug", True),
    n("Launching The Assault"),
    n("Tatooine"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Cantina"),
    n("Home One: War Room"),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Yoda, Great Warrior"),
    n("Han With Heavy Blaster Pistol"),
    n("Leia, Rebel Princess"),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Chewbacca, Protector", True, qty=2),
    n("Chewie, Enraged", True, qty=2),
    n("Luke With Lightsaber", qty=2),
    n("Luke Skywalker", True),
    n("Home One"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Rebel Gunrunner"),
    n("Chewbacca's Bowcaster"),
    n("Lando Calrissian, Scoundrel", True),
    n("Padme Naberrie", True),
    n("Escape Pod", True, qty=3),
    n("Houjix", qty=2),
    n("Projection Of A Skywalker"),
    n("Run Luke, Run!", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Let The Wookiee Win", True, qty=2),
    n("Use The Force", qty=2),
    n("Inconsequential Barriers"),
    n("Control & Tunnel Vision"),
    n("Strikeforce", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Hear Me Baby, Hold Together", True),
    n("Imperial Atrocity", True),
    n("Lucky Shot", True),
    n("Found Someone You Have & Higher Ground"),
    n("Flash Of Insight", True),
    n("Jedi Levitation", True),
    n("Either Way, You Win", True),
    n("Draw Their Fire"),
    n("Nick Of Time", True),
    n("Wokling", True),
    n("Tatooine: Slave Quarters"),
    n("Master Kenobi"),
    n("Communing"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Traffic Control", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("Chasm", True),
    n("Battle Plan"),
    n("Another Pathetic Lifeform"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Control & Set For Stun"),
    n("A Dark Time For The Rebellion", True),
    n("Naboo: Theed Palace Generator"),
    n("Knowledge And Defense", True),
    n("4-LOM With Concussion Rifle", True),
    n("Emperor's Power", True),
    n("Garindan", True),
    n("Where Are You Taking This... Thing?"),
    n("Prepared Defenses", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Lightsaber Deficiency", True),
    n("One Beautiful Thing", qty=2),
    n("Weapon Levitation & The Empire's Back"),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk"),
    n("Sniper & Dark Strike"),
    n("Force Field", True),
    n("Force Lightning"),
    n("Cold Feet", True),
    n("Force Push", True),
    n("Protocol Failure"),
    n("Revenge Of The Sith"),
    n("Blaster Rack", True),
    n("No Escape"),
    n("Imperial Justice", True),
    n("A Sith's Weapon"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Rogue Shadow"),
    n("Victory"),
    n("Endor"),
    n("Blockade Flagship: Bridge"),
    n("Emperor Palpatine", qty=2),
    n("P-59"),
    n("Galen Marek, Starkiller", qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Mara Jade With Lightsaber"),
    n("Grand Moff Tarkin", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Juno Eclipse, Black Leader"),
    n("Grand Admiral Thrawn"),
    n("Boba Fett, Bounty Hunter"),
    n("Dengar With Blaster Carbine", True),
    n("Blizzard 4"),
    n("General Nevar"),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Ni Chuba Na??", True),
    n("Endor Shield", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Gift Of The Master"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("Firepower", True),
    n("Fanfare", True),
    n("Oppressive Enforcement"),
    n("Death Star Sentry", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance?"),
]
DS_ADD = []
