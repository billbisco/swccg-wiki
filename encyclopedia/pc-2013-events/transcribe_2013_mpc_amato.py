#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Nicholas Amato Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Nicholas Amato"
USERNAME = "VadersLackey"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2013 Match Play Championship p03 Nicholas Amato LS.png"
DS_SCAN = "2013 Match Play Championship p04 Nicholas Amato DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username VadersLackey. Event MPC 2013. "
    "Deck title: or this might win a game. Light. Dated 1/26/13. "
    "EPP Han → Han With Heavy Blaster Pistol. OOC → Out Of Commission. "
    "OOC + TT → Out Of Commission & Transmission Terminated. "
    "Line 2 struck a prior title and replaced with OOC. "
    "Bail Organa, Father of Rebellion as written. "
    "Chewbacca, Protector line 21 (V) box filled. (V) from the checkbox. "
    "Communing start inferred at Tatooine: Obi-Wan's Hut (exactly two Light)."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username VadersLackey. Event MPC 2013. "
    "Deck title: Maybe this will win a game. Dark. Dated 1/26/13. "
    "EPP Maul → Darth Maul With Lightsaber. SYCFA / TUPIU → Set Your Course For Alderaan. "
    "DS: DB 327 → Death Star: Docking Bay 327. Furry Fury → Sith Fury. "
    "Close Cell dested Death Star: Detention Block Corridor. "
    "He is not ready + Imperial Prop dested He Is Not Ready. "
    "Ghhhk & Those Rebels → Ghhhk & Those Rebels Won't Escape Us. "
    "Hyperroute Navigation Chart in Additional Cards. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Han With Heavy Blaster Pistol"),
    n("Out Of Commission"),
    n("Let The Wookiee Win", True, qty=2),
    n("Use The Force", qty=2),
    n("Communing"),
    n("Master Kenobi"),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke's Lightsaber"),
    n("Luke With Lightsaber", qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("Anger, Fear, Aggression", True),
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
    n("Bail Organa, Father Of Rebellion"),
    n("Flash Of Insight", True),
    n("Yoda, Great Warrior"),
    n("Commando Training & K'lor'slug"),
    n("Houjix"),
    n("Senator Leia Organa"),
    n("Escape Pod", True),
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
    n("Prepared Defenses", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Knowledge And Defense", True),
    n("Kuat Drive Yards", True),
    n("Laser Cannon Battery"),
    n("Imperial Stockpile"),
    n("A Million Voices Crying Out"),
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star: Docking Bay 327"),
    n("Death Star"),
    n("Alderaan"),
    n("You Swindled Me!", True, qty=2),
    n("Lord Sidious", qty=2),
    n("Judicator", qty=2),
    n("Force Field", qty=2),
    n("Commence Primary Ignition", True),
    n("U-3PO (Yoo-Threepio)"),
    n("Nal Hutta"),
    n("Relentless Pursuit", qty=2),
    n("TIE Sentry Ships", True, qty=2),
    n("Intensify The Forward Batteries", qty=2),
    n("Visage Of The Emperor"),
    n("Victory"),
    n("Tyrant"),
    n("Thunderflare"),
    n("The Phantom Menace"),
    n("Control & Set For Stun", qty=2),
    n("Rendili"),
    n("He Is Not Ready"),
    n("Operational As Planned", True),
    n("Image Of The Dark Lord", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Devastator", True),
    n("Conquest", True),
    n("Overwhelmed", qty=2),
    n("Superlaser"),
    n("Death Star: War Room", True),
    n("Death Star: Central Core (Reactor Shaft)", True),
    n("A Bright Center To The Universe"),
    n("Death Star: Detention Block Corridor"),
    n("Protocol Failure"),
    n("Lightsaber Deficiency", True),
    n("Tarkin's Bounty", True),
    n("Imperial Decree", True),
    n("Lateral Damage"),
    n("Tarkin Doctrine"),
    n("Sith Fury"),
    n("Kiffex"),
    n("Masterful Move & Endor Occupation"),
    n("Accuser"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("Battle Order"),
    n("Fanfare"),
    n("Firepower"),
    n("Come Here You Big Coward"),
    n("Wipe Them Out, All Of Them", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("We'll Let Fate Decide, Huh?", True),
]
DS_ADD = [
    n("Hyperroute Navigation Chart"),
]
