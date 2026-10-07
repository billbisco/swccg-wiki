#!/usr/bin/env python3
"""2014 Match Play Championship Consolation Xerox: Tim Simon Light.

Source: MPC-2014-Day-2-Consolation-Event.pdf page 3 (2013 form, 15 shields).
Name Tim Simon. Username Aglets. Email timsim.
Light full 60 RTP 2.0. Dark Same as empty skip.
"""
from __future__ import annotations

PLAYER = "Tim Simon"
USERNAME = "Aglets"
STAGE = "Consolation"
PDF = "2014 Match Play Championship Consolation.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2014 Match Play Championship Consolation Tim Simon LS.png"
DS_SCAN = ""
LS_DECK_NAME = "RTP 2.0"
DS_DECK_NAME = ""
NOTE = "Handwritten 2013 Xerox. Light only; Dark Same as empty skip."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Tim Simon. Username Aglets. Email timsim. "
    "LIGHT checked. Deck RTP 2.0. IITFYS dested It Is The Future You See (V). "
    "Luke SITF dested Luke Skywalker, Strong In The Force. "
    "Qui-Gon's Lightsaber (Tat) dested Qui-Gon Jinn's Lightsaber. "
    "Sorry About The Mess and BP dested Sorry About The Mess & Blaster Proficiency. "
    "Armed And Dangerous and Krayt Dragon Howl dested Armed And Dangerous & Krayt Dragon Howl. "
    "Hear Me Baby Hold Together dested Hear Me Baby, Hold Together (V). "
    "Han Chewie And The Falcon dested Han, Chewie, And The Falcon (V). "
    "Unique overcounts sheet-accurate (Mace Windu (V) x3, Master Qui-Gon (V) x2, "
    "Luke Skywalker, Strong In The Force x2, Luke Skywalker, Jedi Knight x2, "
    "Let The Wookiee Win (V) x3, Wesa Gotta Grand Army x3, Rebel Leadership (V) x3, "
    "Escape Pod (V) x2, Armed And Dangerous & Krayt Dragon Howl x2, "
    "Speak With The Jedi Council x2). (V) from checkbox."
)
DS_NOTE = "Same as empty skip."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See"
LS_CARDS = [
    n("Home One: War Room"),
    n("Anger, Fear, Aggression", True),
    n("It Is The Future You See", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Quick Draw", True),
    n("Mace Windu", True, qty=3),
    n("Master Qui-Gon", True, qty=2),
    n("Luke Skywalker, Strong In The Force", qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Weapon Levitation"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Let The Wookiee Win", True, qty=3),
    n("Seeking An Audience", True),
    n("Wesa Gotta Grand Army", qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Clash Of Sabers"),
    n("Luke's Lightsaber"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Jedi Lightsaber", True),
    n("Qui-Gon Jinn's Lightsaber"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("A Jedi's Resilience"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Jaina Solo"),
    n("Coruscant: Jedi Council Chamber", True),
    n("What're You Tryin' To Push On Us"),
    n("Blaster Deflection"),
    n("Obi-Wan In Radiant VII"),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Imperial Atrocity", True),
    n("Lady Luck"),
    n("Artoo-Detoo In Red 5"),
    n("Leia, Rebel Princess"),
    n("Armed And Dangerous & Krayt Dragon Howl", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Home One"),
    n("Admiral Ackbar", True),
    n("Yavin 4: Massassi War Room", True),
    n("Corran Horn"),
    n("Speak With The Jedi Council", qty=2),
    n("Sai'torr Kal Fas", True),
    n("Han, Chewie, And The Falcon", True),
    n("Jedi Levitation", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Planetary Defenses", True),
    n("Ultimatum", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Aim High"),
    n("Chasm"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Only Jedi Carry That Weapon"),
    n("Affect Mind", True),
    n("Don't Do That Again", True),
    n("Your Ship"),
]
LS_ADD = []


DS_START = ""
DS_CARDS = []
DS_SHIELDS = []
DS_ADD = []
