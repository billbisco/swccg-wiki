#!/usr/bin/env python3
"""2013 World Championship Day 2: VeeZ Xerox Communing + typed Agents (John Veasey)."""
from __future__ import annotations

PLAYER = "John Veasey"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 100
DS_PAGE = 99
LS_SCAN = "2013 Worlds Day 2 p100 VeeZ LS.png"
DS_SCAN = "2013 Worlds Day 2 p99 VeeZ DS.png"
PUBLIC_NOTE = "Name box on the Day 2 sheet is VeeZ."
LS_NOTE = (
    "Handwritten 2013 Xerox Print Form (15 shields, Hidden Fortress, Jedi Tests). "
    "Name VeeZ. Username blank. Email blank. LIGHT. Deck title Something D. Recent. "
    "Dest as John Veasey (2013 MPC Username veez). "
    "Do not dest as Veez as a new person. Do not rewrite the 2013 MPC Veasey leftover. "
    "Tatooine Slave Quarters dested Tatooine: Slave Quarters. "
    "Maneuvering Flaps and Nick of Time dested Maneuvering Flaps & Nick Of Time. "
    "Tatooine (EP1) dested Tatooine. "
    "Tatooine City Outskirts dested Tatooine: City Outskirts. "
    "Tatooine Obi-Wan Hut dested Tatooine: Obi-Wan's Hut. "
    "Tatooine Jundland Wastes dested Tatooine: Jundland Wastes. "
    "Home 1 War Room dested Home One: War Room. "
    "Han Chewie and the Falcon dested Han, Chewie, And The Falcon. "
    "Lando Collision Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Yoda Great Warrior dested Yoda, Great Warrior. "
    "Dual Laser Cannon dested Dual Laser Cannon. "
    "Echo Base Garrison dested Echo Base Garrison. "
    "Strikeforce dested Strikeforce. "
    "Let's Go Left dested Let's Go Left. "
    "It's Not My Fault dested It's Not My Fault!. "
    "Hear Me Baby Hold Together dested Hear Me Baby, Hold Together. "
    "Antilles Maneuver and Rebel Reinforcements dested "
    "Antilles Maneuver & Rebel Reinforcements. "
    "Yub Yub Commander dested Yub Yub, Commander. "
    "Leia Rebel Princess dested Leia, Rebel Princess. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Yavin Sentry dested Yavin Sentry. "
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
    n("Tatooine: City Outskirts"),
    n("Tatooine"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Jundland Wastes"),
    n("Home One: War Room"),
    n("Han, Chewie, And The Falcon", True),
    n("Home One"),
    n("Lady Luck"),
    n("Rogue 1", qty=2),
    n("Rogue 2"),
    n("Rogue 3"),
    n("Rogue 4"),
    n("Commander Luke Skywalker", True, qty=2),
    n("Commander Wedge Antilles", True),
    n("Zev Senesca"),
    n("Derek 'Hobbie' Klivian"),
    n("Admiral Ackbar", True),
    n("Captain Verrack", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Corran Horn"),
    n("Yoda, Great Warrior"),
    n("Padme Naberrie", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Dual Laser Cannon", True),
    n("Rebel Gunrunner"),
    n("Seeking An Audience", True),
    n("Echo Base Garrison"),
    n("Scrambled Transmission", True),
    n("Flash Of Insight", True, qty=3),
    n("Evacuation Control", True),
    n("Imperial Atrocity", True),
    n("Strikeforce", True),
    n("Menace Fades"),
    n("Let's Go Left", True),
    n("Houjix"),
    n("We're Doomed"),
    n("It's Not My Fault!", True, qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Yub Yub, Commander"),
    n("Escape Pod", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Leia, Rebel Princess"),
    n("Corporal Beezer", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Affect Mind", True),
    n("A Tragedy Has Occurred", True),
    n("Battle Plan"),
    n("Don't Do That Again"),
    n("Do, Or Do Not"),
    n("He Can Go About His Business", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well"),
]
LS_ADD = []

DS_NOTE = (
    "Typed GEMP-style list (p99) with handwritten substitutions. Signed VeeZ / "
    "Strap on Surprise / 8/10/13 / Worlds 2013. Username blank. Dest John Veasey. "
    "Do not dest as Veez as a new person. Do not rewrite the 2013 MPC Veasey leftover. "
    "Do not rewrite the Day 2 Light Communing leftover. "
    "Defensive Shields bracket: Imperial Detention (1 starting) crossed out, "
    "Death Star Sentry (V) written in (Virtual Shield dest). "
    "You Cannot Hide Forever (Death Star II) (V) dested You Cannot Hide Forever (V). "
    "Fanfare (Tatooine) (V) dested Fanfare (V). "
    "Ability, Ability, Ability crossed out, dested Begin Landing Your Troops & The Dark Path. "
    "IG-100 MagnaGuard crossed out, dested Bodyguard Droid as written. "
    "Agents of Black Sun/Vengeance of the Dark Prince dested "
    "Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "(V) from the typed title; unique overcounts kept sheet-accurate."
)
DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("No Escape"),
    n("Imperial Propaganda", True),
    n("You Swindled Me!", True),
    n("Begin Landing Your Troops & The Dark Path"),
    n("Elis Helrot", qty=2),
    n("First Strike"),
    n("Ghhhk"),
    n("Masterful Move & Endor Occupation"),
    n("Control & Set For Stun"),
    n("Stunning Leader", True, qty=3),
    n("We Must Accelerate Our Plans", qty=3),
    n("Jabba's Haven"),
    n("Dark Reconnaissance"),
    n("A Sith's Plans"),
    n("Restraining Bolt"),
    n("Trophy Of A Kill", qty=3),
    n("OOM-9", True),
    n("Bodyguard Droid"),
    n("4-LOM With Concussion Rifle"),
    n("Probot"),
    n("Guri", True, qty=2),
    n("Kitik Keed'kak", True),
    n("Rachalt Hyst"),
    n("Greeata"),
    n("Sy Snootles", True),
    n("Rystall"),
    n("Lady Valarian", qty=2),
    n("Gardulla The Hutt", True, qty=2),
    n("Aurra Sing"),
    n("Prophetess", True, qty=2),
    n("Arica", qty=2),
    n("Zuckuss In Mist Hunter"),
    n("Coruscant: Sub City Lair"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Chancellor's Office"),
    n("Coruscant: Casino"),
    n("Blockade Flagship: Bridge"),
    n("Breached Defenses & Molator"),
    n("I've Lost Artoo!", True),
    n("Ket Maliss", True),
    n("Prepared Defenses", True),
    n("No Bargain", True),
    n("Shada", qty=2),
    n("Coruscant: Imperial City"),
    n("Coruscant"),
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Abyss", True),
]
DS_ADD = []
