#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Sam Marlow Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Sam Marlow"
USERNAME = "Hari Seldon"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 62
DS_PAGE = 61
LS_SCAN = "2013 Match Play Championship p62 Sam Marlow LS.png"
DS_SCAN = "2013 Match Play Championship p61 Sam Marlow DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username Hari Seldon. Event MPC, 26 January 2013. "
    "Deck title 2/2. Light. Starting location Coruscant: Night Club with Do, Or Do Not & Wise Advice. "
    "Mane Wind dested Maneuvering Flaps. Luke Skywalker SITF dested Son Of Skywalker. "
    "Krayt Dragon Howl & Armed And Dangerous dested Armed And Dangerous & Krayt Dragon Howl. "
    "Wesa Gotta Grand Army dested Wesa Gotta Grand Army. "
    "Artoo-Detoo In Red 5 dested Artoo-Detoo In Red 5. "
    "Simple Tricks & Nonsense dested Simple Tricks And Nonsense. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username Hari Seldon. Event MPC, 26 January 2013. "
    "Deck title HD We Must Accelerate Our Handwriting. Dark. "
    "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Boba Fett, Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Fist Strike dested First Strike. I'll Choke dested Physical Choke. "
    "Dr. Evazan & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Masterful Move & Endor Occupation dested Masterful Move & Endor Occupation. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Coruscant: Night Club"
LS_CARDS = [
    n("Coruscant: Night Club"),
    n("Do Or Do Not & Wise Advice"),
    n("Are You Brain Dead?"),
    n("Naboo: Boss Nass' Chambers"),
    n("Yoda, Master Of The Force"),
    n("Jedi Lightsaber", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Maneuvering Flaps", True),
    n("Jedi Lightsaber", True),
    n("Hear Me Baby, Hold Together", True),
    n("Speak With The Jedi Council"),
    n("Han, Chewie, And The Falcon"),
    n("Son Of Skywalker"),
    n("Speak With The Jedi Council"),
    n("Armed And Dangerous & Krayt Dragon Howl", True),
    n("Imperial Atrocity", True),
    n("Speak With The Jedi Council"),
    n("Leia, Rebel Princess"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Leia, Rebel Princess"),
    n("Yoda, Master Of The Force"),
    n("Are You Brain Dead?"),
    n("Blaster Deflection"),
    n("Master Qui-Gon", True, qty=2),
    n("Qui-Gon's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Let The Wookiee Win", True),
    n("Wesa Gotta Grand Army"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Son Of Skywalker"),
    n("Let The Wookiee Win", True),
    n("Speak With The Jedi Council"),
    n("Imperial Atrocity", True),
    n("Let The Wookiee Win", True),
    n("Wesa Gotta Grand Army", qty=2),
    n("Leia's Blaster Rifle"),
    n("Son Of Skywalker"),
    n("The Force Is Strong With This One"),
    n("Control & Tunnel Vision"),
    n("Yoda, Master Of The Force"),
    n("Speak With The Jedi Council"),
    n("Son Of Skywalker"),
    n("Artoo-Detoo In Red 5"),
    n("Corran Horn"),
    n("A Jedi's Resilience"),
    n("Are You Brain Dead?"),
    n("A Jedi's Resilience"),
    n("Threepio With His Parts Showing"),
    n("Maneuvering Flaps", True),
    n("The Force Is Strong With This One"),
    n("Artoo-Detoo In Red 5"),
    n("Quick Draw", True),
    n("Battle Plan & Draw Their Fire"),
    n("The Force Is Strong With This One"),
    n("Sai'torr Kal Fas", True),
    n("Blaster Deflection"),
    n("It Is The Future You See"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Chasm", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Meditation Chamber"),
    n("Executor: Holotheatre"),
    n("Visage Of The Emperor"),
    n("Blizzard 4"),
    n("Maul Strikes"),
    n("The Phantom Menace"),
    n("Blizzard 4"),
    n("Elis Helrot"),
    n("Galen Marek, Starkiller"),
    n("Darth Maul With Lightsaber"),
    n("Force Field", True),
    n("Force Lightning"),
    n("Endor: Back Door"),
    n("No Escape"),
    n("Jango Fett, The Assassin"),
    n("Emperor Palpatine"),
    n("Emperor's Power", True),
    n("Sith Fury", True, qty=2),
    n("A Sith's Weapon"),
    n("Darth Maul With Lightsaber"),
    n("Emperor Palpatine"),
    n("Vader's Lightsaber"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Galen Marek, Starkiller"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Slave I, Symbol Of Fear"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Masterful Move & Endor Occupation"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Dr. Evazan & Ponda Baba"),
    n("Mara Jade With Lightsaber"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Maul With Lightsaber"),
    n("Emperor Palpatine"),
    n("Boba Fett, Prepared Hunter"),
    n("Garindan", True),
    n("Visage Of The Emperor"),
    n("Blockade Flagship: Bridge"),
    n("Visage Of The Emperor"),
    n("I Have You Now"),
    n("Conduct Your Search"),
    n("Prepared Defenses", True),
    n("Sonic Bombardment", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Galen Marek, Starkiller"),
    n("First Strike"),
    n("Blaster Rack", True),
    n("Cloud City: Security Tower", True),
    n("Force Field", True),
    n("Physical Choke", True),
    n("Gift Of The Master"),
    n("Force Push", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("Reactor Terminal", True),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Battle Order"),
    n("Fanfare", True),
]
DS_ADD = []
