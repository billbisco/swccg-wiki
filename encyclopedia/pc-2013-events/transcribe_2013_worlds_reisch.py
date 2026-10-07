#!/usr/bin/env python3
"""2013 World Championship Day 2: Nick Reisch typed QMC + Hunt Down (V)."""
from __future__ import annotations

PLAYER = "Nick Reisch"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 78
DS_PAGE = 79
LS_SCAN = "2013 Worlds Day 2 p78 Nick Reisch LS.png"
DS_SCAN = "2013 Worlds Day 2 p79 Nick Reisch DS.png"
LS_NOTE = (
    "Typed GEMP-style list (p78) with handwritten shield substitutions. "
    "Header Nick Reisch LS / Worlds. Username blank. Dest Nick Reisch. "
    "Do not dest as a new person. Do not rewrite the 2013 MPC or TMW Reisch leftovers. "
    "Quiet Mining Colony/Independent Operation dested "
    "Quiet Mining Colony / Independent Operation. "
    "Could City: North Corridor dested Cloud City: North Corridor. "
    "Punch It dested Punch It!. "
    "Blast the Door Kid dested Blast The Door, Kid!. "
    "Han Chewie and THe Falcon dested Han, Chewie, And The Falcon. "
    "Lando's luxury Yacht dested Lady Luck. "
    "Luke With lightsaber dested Luke's Lightsaber. "
    "Obi-Wan with Lightsaber dested Obi-Wan's Lightsaber. "
    "Qui-Gon Jinn w/ Lightsaber dested Qui-Gon Jinn's Lightsaber. "
    "Leia Rebel Princess dested Leia, Rebel Princess. "
    "Artoo Brave little Droid dested Artoo, Brave Little Droid. "
    "Anger, Fear, Agression dested Anger, Fear, Aggression. "
    "Let's Keep a little optimism here (v) crossed, Wise Advice written in. "
    "Jabba's Prize crossed, There Is Another written in. "
    "Weapon's Display dested Weapons Display. "
    "Yavin 4 Sentry dested Yavin Sentry. "
    "Chasm in shields dested Chasm (V). "
    "(V) from the typed title."
)
DS_NOTE = (
    "Typed GEMP-style list (p79) with handwritten substitutions. "
    "Header Nick Reisch DS / Worlds. Username blank. Dest Nick Reisch. "
    "Do not dest as a new person. Do not rewrite the 2013 MPC or TMW Reisch leftovers. "
    "Hunt Down (v) dested Hunt Down And Destroy The Jedi (V) / "
    "Their Fire Has Gone Out Of The Universe (V). "
    "Coruscant (SE) dested Coruscant. "
    "NI Chuba Na dested Ni Chuba Na??. "
    "Blockade Flagship Bridge dested Blockade Flagship: Bridge. "
    "CC: Security Tower dested Cloud City: Security Tower. "
    "Naboo: Theed Palace Generator Core dested Naboo: Theed Palace Generator Core. "
    "Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Vader, Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Mara Jade(v) dested Mara Jade, The Emperor's Hand. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Ice-Heart dested I Have You Now. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Aura Sing's Blaster Rifle dested Aurra Sing's Blaster Rifle. "
    "Fourth Trophy Of A Kill crossed called, omitted. "
    "Galen's Fighter dested Rogue Shadow. "
    "Blow Parried crossed; handwritten Weapon Lev + Surprise Strike dested "
    "Weapon Levitation and Surprise Strike as written (two-card IN for 60). "
    "Do They Have a Code Clearance? crossed, Death Star Sentry (V) written in. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "(V) from the typed title."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Wokling", True),
    n("Beldon's Eye"),
    n("Keeping The Empire Out Forever"),
    n("Heading For The Medical Frigate", True),
    n("Cloud City: Chasm Walkway"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: North Corridor"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Rebel Barrier"),
    n("Path Of Least Resistance", qty=2),
    n("Punch It!", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("Into The Ventilation Shaft, Lefty", qty=3),
    n("Houjix"),
    n("Fall Of The Legend", qty=3),
    n("Escape Pod", True),
    n("Choke", qty=2),
    n("Blast The Door, Kid!"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Weather Vane", True),
    n("Imperial Atrocity", True),
    n("Spiral", qty=2),
    n("Han, Chewie, And The Falcon"),
    n("Lady Luck"),
    n("Overseer"),
    n("Outrider"),
    n("Luke's Lightsaber", qty=2),
    n("Obi-Wan's Lightsaber", qty=2),
    n("Pucumir Thryss", qty=2),
    n("Qui-Gon Jinn's Lightsaber", qty=2),
    n("Cloud City Celebration", qty=2),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Kebyc", True),
    n("Harc Seff", True),
    n("Lobot", True),
    n("Dash Rendar", True, qty=2),
    n("Artoo, Brave Little Droid"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("There Is Another"),
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
    n("Chasm"),
    n("Affect Mind", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Drop!", True),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower"),
    n("Hoth: Wampa Cave"),
    n("Death Star: War Room", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Galen Marek, Starkiller", qty=3),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Mara Jade, The Emperor's Hand"),
    n("Juno Eclipse, Black Leader"),
    n("Grand Moff Tarkin", True),
    n("I Have You Now"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Levitation Attack", qty=3),
    n("Weapon Levitation & The Empire's Back", qty=3),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Aurra Sing's Blaster Rifle"),
    n("Trophy Of A Kill", qty=3),
    n("Restraining Bolt"),
    n("Sonic Bombardment", True, qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("ComScan Detection", True),
    n("Rogue Shadow"),
    n("Slave I, Symbol Of Fear"),
    n("Weapon Levitation"),
    n("Surprise Strike"),
    n("Force Field", True, qty=2),
    n("One Beautiful Thing", qty=2),
    n("Sith Fury & End This Destructive Conflict"),
    n("Ability, Ability, Ability", True),
    n("You Are Beaten"),
    n("Control", qty=2),
    n("Blaster Rack", True),
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
    n("Death Star Sentry", True),
    n("Imperial Detention", True),
]
DS_ADD = []
