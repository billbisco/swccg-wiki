#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1 typed slang printout: Nick Reisch LS+DS."""
from __future__ import annotations

PLAYER = "Nick Reisch"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 2
DS_PAGE = 1
LS_SCAN = "2013 Texas Mini Worlds Day 1 p02 Nick Reisch LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p01 Nick Reisch DS.png"
NOTE = "Typed slang printout (not a handwritten Xerox form). Dark Restraining Bolt struck; handwritten No Escape."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: City Outskirts"),
    n("Credits Will Do Fine"),
    n("Rycar Ryjerd", True),
    n("A Remote Planet", True),
    n("Quick Draw", True),
    n("Heading For The Medical Frigate", True),
    n("Into The Garbage Chute, Flyboy!", True, qty=2),
    n("A Jedi's Resilience", qty=2),
    n("Let The Wookiee Win", True),
    n("Blaster Deflection", True, qty=2),
    n("Rebel Barrier"),
    n("Clash Of Sabers"),
    n("Alter", True),
    n("Found Someone You Have & Higher Ground"),
    n("Might Of The Republic"),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Naboo: Boss Nass' Chambers"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Sorry About The Mess", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Guardian's Lightsaber"),
    n("Obi-Wan's Journal"),
    n("Obi-Wan's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("I Hope She's All Right"),
    n("Lightsaber Proficiency"),
    n("Meditation"),
    n("Disarmed", qty=2),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Senator Jar Jar Binks"),
    n("Maris Brood, Fallen Jedi", qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Senator Padme Amidala"),
    n("Escape Pod", True, qty=2),
    n("Clash Of Sabers"),
    n("Houjix"),
    n("Dark Approach", True),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("Imperial Atrocity", True),
    n("Advantage"),
    n("Rebel Barrier"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("Battle Plan"),
    n("Do, Or Do Not"),
    n("He Can Go About His Business", True),
    n("Chasm", True),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Imperial City"),
    n("Sith's Plans"),
    n("According To My Design"),
    n("Emperor Palpatine"),
    n("Gift Of The Master"),
    n("Ni Chuba Na", True),
    n("Drop!", True),
    n("Kashyyyk"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Galen Marek, Starkiller", qty=3),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Mara Jade, The Emperor's Hand"),
    n("Juno Eclipse, Black Leader"),
    n("Grand Moff Tarkin", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Slave One, Symbol Of Fear"),
    n("Rogue Shadow"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Aurra Sing's Blaster Rifle", qty=3),
    n("Trophy Of A Kill", qty=3),
    n("Special Delivery", True),
    n("Emperor's Power", True),
    n("Ability, Ability, Ability", True),
    n("Blaster Rack", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("Weapon Levitation & The Empire's Back", qty=3),
    n("Force Field", True, qty=2),
    n("One Beautiful Thing", qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Force Lightning"),
    n("Sith Fury & End This Destructive Conflict"),
    n("Coruscant: Casino"),
    n("No Escape"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("There Is No Try"),
    n("Abyss", True),
    n("Battle Order"),
    n("Weapon Of A Sith"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Do They Have A Code Clearance?"),
    n("Imperial Detention", True),
]
DS_ADD = []
