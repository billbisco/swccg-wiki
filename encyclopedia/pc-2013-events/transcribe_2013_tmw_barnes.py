#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1 typed slang printout: James Barnes LS+DS."""
from __future__ import annotations

PLAYER = "James Barnes"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 22
DS_PAGE = 23
LS_SCAN = "2013 Texas Mini Worlds Day 1 p22 James Barnes LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p23 James Barnes DS.png"
LS_NOTE = "Typed slang printout (not a handwritten Xerox form)."
DS_NOTE = "Typed slang printout (not a handwritten Xerox form). Kashyyyk is handwritten at the bottom of the sheet."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "The Hyperdrive Generator's Gone / We'll Need A New One"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("The Hyperdrive Generator's Gone / We'll Need A New One"),
    n("Tatooine: Watto's Junkyard"),
    n("Tatooine: City Outskirts"),
    n("Credits Will Do Fine"),
    n("Heading For The Medical Frigate", True),
    n("A Remote Planet", True),
    n("Quick Draw", True),
    n("Rycar Ryjerd", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Obi-Wan Kenobi, Padawan Learner", True, qty=2),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Maris Brood, Fallen Jedi", qty=2),
    n("Senator Padme Amidala"),
    n("Senator Jar Jar Binks"),
    n("Obi-Wan's Lightsaber"),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Guardian's Lightsaber"),
    n("Elegant Lightsaber"),
    n("Obi-Wan's Journal"),
    n("Imperial Atrocity", True),
    n("Eject! Eject!"),
    n("Disarmed", qty=2),
    n("Seeking An Audience", True),
    n("Lightsaber Proficiency"),
    n("Meditation"),
    n("I Hope She's All Right"),
    n("Sai'torr Kal Fas", True),
    n("Advantage"),
    n("A Jedi's Resilience", qty=2),
    n("Into The Garbage Chute, Flyboy!", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Escape Pod", True, qty=2),
    n("Out Of Commission & Transmission Terminated"),
    n("Impressive, Most Impressive", True),
    n("Hear Me Baby, Hold Together", True),
    n("Might Of The Republic"),
    n("Blaster Deflection", qty=2),
    n("Rebel Barrier", qty=2),
    n("Sorry About The Mess", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Clash Of Sabers", qty=2),
    n("Houjix"),
    n("Alter", True),
    n("Found Someone You Have & Higher Ground"),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("Ultimatum"),
    n("Affect Mind", True),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor", True),
    n("Do, Or Do Not"),
    n("Weapons Display"),
    n("Only Jedi Carry That Weapon"),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Imperial City"),
    n("Sith's Plans"),
    n("According To My Design"),
    n("Emperor Palpatine"),
    n("Gift Of The Master"),
    n("Ni Chuba Na?", True),
    n("Drop!", True),
    n("Coruscant: Casino"),
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
    n("Slave I, Symbol Of Fear"),
    n("Rogue Shadow"),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Aurra Sing's Blaster Rifle", qty=3),
    n("Trophy Of A Kill", qty=3),
    n("Restraining Bolt"),
    n("Emperor's Power", True),
    n("Ability, Ability, Ability", True),
    n("Blaster Rack", True),
    n("Special Delivery", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Sonic Bombardment", True, qty=3),
    n("Weapon Levitation & The Empire's Back", qty=4),
    n("Force Field", True, qty=2),
    n("One Beautiful Thing", qty=2),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Force Lightning"),
    n("Kashyyyk"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("Resistance"),
    n("Do They Have A Code Clearance?"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Death Star Sentry", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Weapon Of A Sith"),
    n("Abyss", True),
]
DS_ADD = []
