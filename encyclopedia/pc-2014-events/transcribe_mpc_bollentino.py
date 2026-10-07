#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Xerox: Andrew Bollentino.

Source: MPC-2014-Day-1-Main-Event.pdf pages 19–20 (2013 form, 15 shields).
Username Lord Bane. Sheet Andrew Bolletino / Biletino.
"""
from __future__ import annotations

PLAYER = "Andrew Bollentino"
USERNAME = "Lord Bane"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 20
DS_PAGE = 19
LS_SCAN = "2014 Match Play Championship Day 1 Andrew Bollentino LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Andrew Bollentino DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = "MILF HUNTER"
NOTE = "Handwritten 2013 Xerox form. Sheet Bolletino/Biletino dested Andrew Bollentino."
LS_NOTE = (
    "Handwritten 2013 Xerox. Name Biletino dested Andrew Bollentino. LIGHT/DARK empty. "
    "Communing (V) dested Communing (virtual-only v=False). Commando Trans combo dested "
    "Commando Training & K'lor'slug. IGABFAT dested I've Got A Bad Feeling About This. "
    "Yoda stew combo dested You Will Go To The Dagobah System. SATM combo dested Sorry "
    "About The Mess & Blaster Proficiency. Antilles Man. combo dested Antilles Maneuver "
    "& Rebel Reinforcements. C-TV dested Control & Tunnel Vision. MTFYSYH dested Much To "
    "Learn, You Still Have. Threepio WHPS dested Threepio With His Parts Showing. Unique "
    "overcounts sheet-accurate (Rebel Leadership (V) x5, Chewie, Enraged (V) x3, Luke "
    "Skywalker (V) x3, Luke's T-16 Skyhopper x2, Let The Wookiee Win (V) x2, Precise Hit "
    "(V) x2, You Will Go To The Dagobah System x2, Old Ben x2, Wookiee Roar (V) x2, "
    "Republic Cruiser (V) x2). (V) from checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Xerox. Name Andrew Bolletino dested Andrew Bollentino. Username "
    "Lord Bane. DARK checked. Deck MILF HUNTER. HD (V) dested Hunt Down And Destroy The "
    "Jedi (V) / Their Fire Has Gone Out Of The Universe (V). GOTM dested Gift Of The "
    "Master. Black leader dested Juno Eclipse, Black Leader. Mara w/ stick dested Mara "
    "Jade With Lightsaber. Aurra DA dested Aurra Sing, Deadly Assassin. Mand FOF dested "
    "Jango Fett, The Assassin. Grievous dested Grievous, Hunter Of Jedi. Galen dested "
    "Galen Marek, Starkiller. Galen's Fighter dested Rogue Shadow. C & SFS dested Control "
    "& Set For Stun. OBT dested One Beautiful Thing. P-59 dested P-59. Unique overcounts "
    "sheet-accurate (Grievous, Hunter Of Jedi x2, Galen Marek, Starkiller x2, Emperor "
    "Palpatine x2, Darth Vader, Dark Lord Of The Sith x2, Sniper & Dark Strike x2, Sonic "
    "Bombardment (V) x2, Imperial Barrier (V) x2). (V) from checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Communing"),
    n("Master Kenobi"),
    n("Tatooine: Slave Quarters"),
    n("Wokling", True),
    n("Commando Training & K'lor'slug", True),
    n("Imperial Atrocity", True),
    n("Menace Fades"),
    n("Rebel Leadership", True, qty=5),
    n("Han With Heavy Blaster Pistol"),
    n("I've Got A Bad Feeling About This"),
    n("You Will Go To The Dagobah System", qty=2),
    n("Precise Hit", True, qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Luke's T-16 Skyhopper", qty=2),
    n("Luke Skywalker", True, qty=3),
    n("It's A Trap!"),
    n("Leia, Rebel Princess"),
    n("Shmi Skywalker"),
    n("Chewie, Enraged", True, qty=3),
    n("Yoda, Great Warrior"),
    n("Home One: War Room"),
    n("Tatooine: Beggar's Canyon"),
    n("Tatooine"),
    n("Launching The Assault"),
    n("Chewbacca's Bowcaster"),
    n("Rebel Gunrunner", True),
    n("Admiral Ackbar", True),
    n("Home One"),
    n("Houjix"),
    n("Lando Calrissian, Scoundrel", True),
    n("Tatooine: Obi-Wan's Hut", True),
    n("IL-19"),
    n("Out Of Commission & Transmission Terminated"),
    n("Much To Learn, You Still Have"),
    n("Threepio With His Parts Showing"),
    n("Control & Tunnel Vision"),
    n("Old Ben", qty=2),
    n("Nabrun Leids"),
    n("Wookiee Roar", True, qty=2),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Escape Pod", True),
    n("The Bith Shuffle & Desperate Reach"),
    n("Republic Cruiser", True, qty=2),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Battle Plan", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("The Professor", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Affect Mind", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master", True),
    n("Endor Shield", True),
    n("A Sith's Plans", True),
    n("Coruscant: Imperial City"),
    n("Coruscant"),
    n("U-3PO"),
    n("Juno Eclipse, Black Leader", True),
    n("Mara Jade With Lightsaber", True),
    n("Aurra Sing, Deadly Assassin", True),
    n("Jango Fett, The Assassin", True),
    n("Boba Fett, Bounty Hunter", True),
    n("4-LOM With Concussion Rifle", True),
    n("P-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("Grievous, Hunter Of Jedi", True, qty=2),
    n("Galen Marek, Starkiller", True, qty=2),
    n("Emperor Palpatine", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Cloud City: Security Tower", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Endor"),
    n("Blizzard 4"),
    n("Victory", True),
    n("Rogue Shadow", True),
    n("Revenge Of The Sith", True),
    n("Malakili"),
    n("Blaster Rack", True),
    n("Durge", True),
    n("Grievous' Lightsabers", True),
    n("Tarkin's Bounty", True),
    n("Tarkin's Bounty"),
    n("Vader's Lightsaber"),
    n("Dooku's Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Control & Set For Stun"),
    n("Ghhhk"),
    n("Sniper & Dark Strike", qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Imperial Barrier", True, qty=2),
    n("One Beautiful Thing", True),
    n("Evader"),
    n("Force Field", True),
    n("Weapon Levitation & The Empire's Back", True),
    n("Force Lightning"),
    n("Force Push", True),
    n("Masterful Move"),
    n("Image Of The Dark Lord", True),
    n("Imperial Propaganda", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Resistance", True),
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward", True),
    n("Imperial Detention", True),
    n("Weapon Of A Sith"),
    n("Secret Plans", True),
    n("Allegations Of Corruption"),
    n("Battle Order", True),
    n("Abyss", True),
]
DS_ADD = []
