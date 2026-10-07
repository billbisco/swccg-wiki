#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Steve Baroni.

Source: MPC-2014-Day-1-Main-Event.pdf pages 17–18 (2013 form, 15 shields).
Username blank. Deck names Mike Desai / Communing Justin.
"""
from __future__ import annotations

PLAYER = "Steve Baroni"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 18
DS_PAGE = 17
LS_SCAN = "2014 Match Play Championship Day 1 Steve Baroni LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Steve Baroni DS.png"
LS_DECK_NAME = "Communing Justin"
DS_DECK_NAME = "Mike Desai"
NOTE = "Handwritten 2013 Xerox form."
LS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. LIGHT/DARK empty. Deck Communing Justin "
    "dested Communing (LS_START). Slave Quarters dested Tatooine: Slave Quarters. "
    "DO or DO Not WA dested Do, Or Do Not & Wise Advice. BP DTF dested Battle Plan & "
    "Draw Their Fire. IITFYS dested It Is The Future You See. Lando's Yacht dested Lady "
    "Luck. HCF dested Han, Chewie, And The Falcon. Artoo in Red 5 dested Artoo-Detoo In "
    "Red 5. Unique overcounts sheet-accurate (Artoo-Detoo In Red 5 x2, Master Qui-Gon "
    "(V) x2, Mace Windu (V) x2, Luke Skywalker, Strong In The Force (V) x2, Let The "
    "Wookiee Win (V) x3, Wesa Gotta Grand Army x3, Rebel Leadership (V) x3, Clash Of "
    "Sabers x2, Escape Pod (V) x3, Houjix x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Username blank. Deck Mike Desai. HD (V) dested Hunt Down "
    "And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V). Gift of "
    "Mgr dested Gift Of The Master. Galen Saber Vader dested Galen's Lightsaber, Vader's "
    "Gift. They're Still Coming dested They're Still Coming Through!. K+D dested "
    "Knowledge And Defense. P-59 dested P-59. Hidden Fortress Abyss (V) "
    "and There Is No Try dested extra shields. Unique overcounts sheet-accurate "
    "(Blizzard 4 x3, Emperor Palpatine x2, Galen Marek, Starkiller x3, We Must "
    "Accelerate Our Plans x3, Force Field (V) x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Communing"),
    n("Tatooine: Slave Quarters"),
    n("Quick Draw", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Sai'torr Kal Fas", True),
    n("It Is The Future You See", True),
    n("Naboo: Battle Plains"),
    n("Home One: War Room"),
    n("Naboo: Boss Nass' Chambers"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Qui-Gon's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Dagobah: Yoda's Hut"),
    n("Lady Luck", True),
    n("Han, Chewie, And The Falcon", True),
    n("Master Qui-Gon", True, qty=2),
    n("Mace Windu", True, qty=2),
    n("Yoda, Great Warrior", True),
    n("Obi-Wan Kenobi", True),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Luke Skywalker, Jedi Knight"),
    n("Admiral Ackbar", True),
    n("Corran Horn"),
    n("Jaina Solo", True),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Let The Wookiee Win", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Rebel Leadership", True, qty=3),
    n("Speak With The Jedi Council"),
    n("Imperial Atrocity", True),
    n("Strikeforce", True),
    n("Hear Me Baby, Hold Together", True),
    n("Blaster Deflection"),
    n("Rebel Barrier"),
    n("Mechanical Failure"),
    n("Weapon Levitation"),
    n("A Jedi's Resilience"),
    n("Seeking An Audience", True),
    n("Clash Of Sabers", qty=2),
    n("Escape Pod", True, qty=3),
    n("Houjix", qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("He Can Go About His Business"),
    n("Aim High"),
    n("Your Ship?"),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("The Professor"),
    n("Yavin Sentry"),
    n("Your Insight Serves You Well"),
    n("Planetary Defenses"),
    n("Weapons Display"),
    n("Let's Keep A Little Optimism Here"),
    n("Affect Mind"),
    n("Chasm", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Blaster Rack", True),
    n("Prepared Defenses", True),
    n("Coruscant: Imperial City"),
    n("Endor Shield", True),
    n("Ni Chuba Na??", True),
    n("A Sith's Plans", True),
    n("Gift Of The Master", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Vader's Lightsaber"),
    n("Blockade Flagship: Bridge"),
    n("Endor"),
    n("Endor: Back Door"),
    n("Blizzard 4", qty=3),
    n("Victory", True),
    n("Rogue Shadow", True),
    n("General Nevar", True),
    n("Grand Admiral Thrawn"),
    n("Dr. Evazan & Ponda Baba"),
    n("Dengar With Blaster Carbine", True),
    n("Juno Eclipse, Black Leader", True),
    n("Mara Jade With Lightsaber"),
    n("P-59"),
    n("Boba Fett, Bounty Hunter"),
    n("Juno Eclipse, Black Leader", True),
    n("Grand Moff Tarkin", True),
    n("Emperor Palpatine", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Lord Vader"),
    n("Galen Marek, Starkiller", True, qty=3),
    n("We Must Accelerate Our Plans", qty=4),
    n("Force Field", True, qty=2),
    n("They're Still Coming Through!"),
    n("Wipe Them Out, All Of Them", True),
    n("A Sith's Weapon", True),
    n("Lightsaber Deficiency", True),
    n("Force Push", True),
    n("The Circle Is Now Complete"),
    n("Protocol Failure", True),
    n("No Escape"),
    n("Ghhhk"),
    n("One Beautiful Thing", True),
    n("Revenge Of The Sith"),
    n("Something Special Planned For Them", True),
    n("Cold Feet", True),
    n("Force Lightning"),
    n("Sniper & Dark Strike"),
    n("Imperial Barrier"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Fanfare", True),
    n("Death Star Sentry", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance?", True),
    n("Weapon Of A Sith"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("You Cannot Hide Forever"),
    n("Come Here You Big Coward"),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Secret Plans"),
    n("Abyss", True),
    n("There Is No Try"),
]
DS_ADD = []
