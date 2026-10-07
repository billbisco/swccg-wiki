#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Nicholas Amato.

Source: MPC-2014-Day-1-Main-Event.pdf pages 3–4 (2010 form, 12 shields).
Light username VadersLackey; Dark username nicholas.amato.
Light deck name: or this might win a game. Dark: Great Ball of Fire!
"""
from __future__ import annotations

PLAYER = "Nicholas Amato"
USERNAME = "nicholas.amato"
LS_USERNAME = "VadersLackey"
DS_USERNAME = "nicholas.amato"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2014 Match Play Championship Day 1 Nicholas Amato LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Nicholas Amato DS.png"
LS_DECK_NAME = "or this might win a game"
DS_DECK_NAME = "Great Ball of Fire!"
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Username VadersLackey. Deck name or this might "
    "win a game. LIGHT checked. Communing starting Objective. EPP Han dested "
    "Han With Heavy Blaster Pistol. Line 2 OOC crossed with no replacement, skipped. "
    "OOC dested Out Of Commission. OOC + TT dested Out Of Commission & Transmission "
    "Terminated. Line 14 Combo ditto dested Imperial Atrocity True. Rebel Gunner dested "
    "Rebel Gunrunner. Line 32 crossed with no replacement, skipped (main=58). "
    "Yoda, Great Warrior dested Yoda, Great Warrior. Commando training + K'lor'slug "
    "dested Commando Training & K'lor'slug. SATM + Blaster Prof dested Sorry About "
    "The Mess & Blaster Proficiency. Unique undercount sheet-accurate (main=58). "
    "(V) from checkbox."
)
DS_NOTE = (
    "Typed 2010 Xerox with handwritten replacements. Username nicholas.amato. "
    "Deck name Great Ball of Fire! DARK checked. SYCFA dested Set Your Course For "
    "Alderaan / The Ultimate Power In The Universe. Super Laser dested Superlaser. "
    "Death Star: Central Core dested Death Star: Central Core True. "
    "U-3PO dested U-3PO (Yoo-Threepio). Cease Fire line 20 crossed, Force Field dested "
    "Force Field. Why Didn't You Tell Me line 27 crossed, Force Field True dested "
    "Force Field True. Why Didn't You Tell Me line 28 crossed, Protocol Failure True. "
    "Cease Fire line 29 crossed, You Swindled Me True dested You Swindled Me!. "
    "A Dark Time for the Rebellion line 34 crossed, You Swindled Me True dested "
    "You Swindled Me!. Furry Fury dested Furry Fury. Visage dested Visage Of The Emperor. "
    "He is Not Ready & Imperial Propaganda dested He Is Not Ready. "
    "Imperial Barrier line 55 crossed, Astromech Shortage True dested Astromech Shortage. "
    "Victory dested Victory. Hyper Route Navigation Chart dested Hyperroute Navigation "
    "Chart. Unique overcounts sheet-accurate (Imperial Barrier x2, You Swindled Me! x2, "
    "Force Field x2, Overwhelmed x2, TIE Sentry Ships True x2, Relentless Pursuit x2, "
    "Intensify The Forward Batteries x2, Control & Set For Stun x2, Lord Sidious x2, "
    "Judicator x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Han With Heavy Blaster Pistol"),
    n("Let The Wookiee Win", True, qty=2),
    n("Use The Force", qty=2),
    n("Communing"),
    n("Master Kenobi"),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke's Lightsaber"),
    n("Luke With Lightsaber", qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("Anger, Fear, Aggression"),
    n("Lando Calrissian, Scoundrel", True, qty=2),
    n("Scrambled Transmission", True),
    n("Chewie, Enraged", True, qty=2),
    n("Chewbacca, Protector", True),
    n("Chewbacca, Protector"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Rebel Gunrunner"),
    n("Chewbacca's Bowcaster"),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("Out Of Commission", qty=2),
    n("Tatooine: City Outskirts"),
    n("Padme Naberrie", True),
    n("Flash Of Insight", True),
    n("Yoda, Great Warrior"),
    n("Commando Training & K'lor'slug"),
    n("Houjix"),
    n("Senator Leia Organa"),
    n("Escape Pod"),
    n("Run Luke, Run!", True, qty=2),
    n("Alderaan Consular Ship"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Mos Eisley"),
    n("I Feel The Conflict"),
    n("What're You Tryin' To Push On Us?", qty=3),
    n("Leia, Rebel Princess"),
    n("The Signal", qty=2),
    n("Seeking An Audience", True),
    n("Changing The Odds", qty=2),
    n("Away Put Your Weapon"),
    n("Stone Pile", qty=2),
    n("Draw Their Fire"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Dagobah: Yoda's Hut"),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Chasm"),
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Aim High"),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("The Professor"),
]
LS_ADD = []


DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Knowledge And Defense", True),
    n("Prepared Defenses"),
    n("Imperial Stockpile"),
    n("A Million Voices Crying Out"),
    n("Kuat Drive Yards", True),
    n("Death Star"),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Kiffex"),
    n("Rendili"),
    n("Nal Hutta"),
    n("Death Star: Central Core", True),
    n("Death Star: War Room", True),
    n("Superlaser"),
    n("Commence Primary Ignition", True),
    n("Lord Sidious", True),
    n("Lord Sidious"),
    n("U-3PO (Yoo-Threepio)"),
    n("Force Field"),
    n("Intensify The Forward Batteries", qty=2),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Furry Fury", qty=2),
    n("Force Field", True),
    n("Protocol Failure", True),
    n("You Swindled Me!", True, qty=2),
    n("Relentless Pursuit", qty=2),
    n("TIE Sentry Ships", True, qty=2),
    n("A Dark Time For The Rebellion"),
    n("Overwhelmed", qty=2),
    n("Operational As Planned", True),
    n("Lightsaber Deficiency", True),
    n("Image Of The Dark Lord", True),
    n("Imperial Decree", True),
    n("Lateral Damage"),
    n("He Is Not Ready"),
    n("A Bright Center To The Universe"),
    n("Tarkin Doctrine"),
    n("Devastator", True),
    n("Conquest", True),
    n("Victory"),
    n("Tyrant"),
    n("Visage Of The Emperor"),
    n("Judicator", qty=2),
    n("Accuser"),
    n("Thunderflare"),
    n("Astromech Shortage", True),
    n("Imperial Barrier", qty=2),
    n("Control & Set For Stun", qty=2),
    n("Laser Cannon Battery"),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Battle Order"),
    n("Fanfare"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Wipe Them Out, All Of Them", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Firepower", True),
]
DS_ADD = [
    n("Hyperroute Navigation Chart"),
]
