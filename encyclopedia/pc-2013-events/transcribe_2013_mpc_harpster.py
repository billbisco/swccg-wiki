#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: HARPSTER Xerox LS+DS."""
from __future__ import annotations

PLAYER = "HARPSTER"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 37
DS_PAGE = 38
LS_SCAN = "2013 Match Play Championship p37 HARPSTER LS.png"
DS_SCAN = "2013 Match Play Championship p38 HARPSTER DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. HARPSTER. Light. Event MPC. "
    "Plead My Case To The Senate / Senators In Laager (V). "
    "Obi w/ Stick dested Obi-Wan With Lightsaber. "
    "Luke Sky Rebel Scout dested Luke Skywalker, Rebel Scout. "
    "Yoda Great War dested Yoda, Great Warrior. "
    "Alderaan Con Ship dested Alderaan Consular Ship. "
    "Lando Calrissian Scoundrel dested Lando Calrissian, Scoundrel. "
    "Owen + Beru Lars dested Owen Lars & Beru Lars. "
    "Chewie Protector dested Chewbacca, Protector. "
    "Wedge Antilles RSL dested Wedge Antilles, Red Squadron Leader. "
    "Heading For They Frigate dested Heading For The Medical Frigate. "
    "Battle Plan / Combo dested Battle Plan & Draw Their Fire. "
    "Yoda Stew Combo dested Yoda Stew & You Do Have Your Moments. "
    "Senate Hover Cam dested Senate Hovercam. Much Failure dested Mechanical Failure. "
    "Bail Organa FOR dested Bail Organa, Father Of Rebellion. "
    "Might Of The RIP dested Might Of The Republic. "
    "Senator Padme dested Senator Padme Amidala. "
    "Wesa Got A Grand dested Wesa Gotta Grand Army. "
    "EP1 Coruscant dested Coruscant. Coruscant Nightclub dested Coruscant: Night Club. "
    "Lines 41–42 dittos of Jedi Presence. Line 49 Coruscant Senate struck dested "
    "Yoda Stew & You Do Have Your Moments. "
    "AFA dested Anger, Fear, Aggression. (V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. HARPSTER. Dark. Event MPC. Starting Kessel. "
    "Kessel Spice Mines Admin Office dested Kessel: Spice Mines - Administrator's Office. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "SRF combo dested Short Range Fighters & Watch Your Back. "
    "The Mandalorian Father of Fett dested Jango Fett, The Assassin. "
    "Slave I, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Darth Maul w/ Saber dested Darth Maul With Lightsaber. "
    "Masterful Move & Endor Occupation dested Masterful Move & Endor Occupation. "
    "Spice Mine Admin dested Spice Mine Administrator. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Vader's Lightsaber dested Darth Vader's Lightsaber. "
    "DLOTS dested Droideka. "
    "Darth Vader, Betrayer of Jedi dested Darth Vader, Betrayer Of The Jedi. "
    "Kessel: Spice Mine Prison dested Kessel: Spice Mines - Prison. "
    "Kessel: Spice Mine Docking Bay dested Kessel: Spice Mines - Docking Bay. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "We'll Let Fate Decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "Form left column reprints 37–38 on lines 39–40 are Darth Vader's Lightsaber and Droideka. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Senators In Laager"
LS_CARDS = [
    n("Plead My Case To The Senate / Senators In Laager", True),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Luke Skywalker, Rebel Scout", True, qty=2),
    n("Yoda, Great Warrior", qty=2),
    n("Alderaan Consular Ship", True, qty=2),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Commander Vanden Willard"),
    n("Owen Lars & Beru Lars"),
    n("General Solo", True),
    n("Escape Pod", True),
    n("K'lor'slug", True),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("So This Is How Liberty Dies", True),
    n("Yoda Stew & You Do Have Your Moments", qty=2),
    n("Commander Narra", True),
    n("Corran Horn"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Chewbacca, Protector", True),
    n("Heading For The Medical Frigate"),
    n("Battle Plan & Draw Their Fire"),
    n("Strike Planning"),
    n("Wokling", True),
    n("Senate Hovercam"),
    n("Menace Fades"),
    n("Field Dressing", True),
    n("Mechanical Failure"),
    n("Imperial Atrocity", True),
    n("Bail Organa", True, qty=2),
    n("Bail Organa, Father Of Rebellion", True, qty=2),
    n("Frozen Assets", qty=2),
    n("Jedi Presence", qty=3),
    n("Might Of The Republic", qty=3),
    n("Senator Mon Mothma", True),
    n("Senator Padme Amidala", True),
    n("Senator Leia Organa", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Coruscant"),
    n("Coruscant: Night Club", True),
    n("Sense", qty=2),
    n("Clash Of Sabers"),
    n("Houjix"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Simple Tricks And Nonsense", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("The Professor"),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Broken Concentration", True),
    n("Imperial Justice", True),
    n("Much Anger In Him"),
    n("Protocol Failure"),
    n("Kessel Surveillance System"),
    n("Cloud City: Security Tower", True),
    n("Sonic Bombardment", True, qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Blockade Flagship: Bridge"),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Sense", qty=2),
    n("Force Push", True),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Slave I, Symbol Of Fear", True),
    n("Sidious' Lightsaber"),
    n("Darth Sidious", qty=2),
    n("Force Field", True),
    n("Garindan", True),
    n("The Emperor", True),
    n("Arica"),
    n("Myn Kyneugh", True),
    n("Ghhhk"),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Spice Mine Administrator", True, qty=2),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Galen Marek, Starkiller", qty=2),
    n("Darth Vader's Lightsaber"),
    n("Droideka"),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Aurra Sing's Blaster Rifle"),
    n("Aurra Sing, Deadly Assassin", True, qty=2),
    n("Trophy Of A Kill", True, qty=2),
    n("Kessel: Spice Mines - Prison"),
    n("Kessel: Spice Mines - Docking Bay"),
    n("Spice Mine Operations", True),
    n("A Sith's Weapon", True),
    n("Tarkin's Bounty", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Maul's Sith Infiltrator"),
    n("The Phantom Menace"),
    n("I'll Take Them Myself"),
    n("Gift Of The Master", True),
    n("Blaster Rack", True),
    n("Ni Chuba Na??", True),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Weapon Of A Sith"),
    n("Come Here You Big Coward"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("Fanfare", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("Firepower", True),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
