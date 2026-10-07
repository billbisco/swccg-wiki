#!/usr/bin/env python3
"""2013 World Championship Day 2: Ryan Washeleski Agents + Hidden Base X-wings."""
from __future__ import annotations

PLAYER = "Ryan Washeleski"
USERNAME = "Nicodarius"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 112
DS_PAGE = 111
LS_SCAN = "2013 Worlds Day 2 p112 Ryan Washeleski LS.png"
DS_SCAN = "2013 Worlds Day 2 p111 Ryan Washeleski DS.png"
PUBLIC_NOTE = "Username Nicodarius."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields). Name Ryan Washeleski. "
    "Username Nicodarius. Email on sheet. LIGHT. Deck title HB-wings!. "
    "Hidden Base / Flip dested Hidden Base / Systems Will Slip Through Your Fingers. "
    "Alor Shaddaa dested Nar Shaddaa. "
    "Slayn + Korpil facilities dested Slayn & Korpil Facilities. "
    "Heading for the Med. Frigate dested Heading For The Medical Frigate. "
    "B-wing Bomber dested B-wing Bomber. "
    "Hit & Run dested Hit And Run. "
    "Jabba's Prize from shields is an extra Character. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields). Name Ryan Washeleski. "
    "Username Nicodarius. Email on sheet. DARK. Deck title A&M = win?. "
    "A&M / Flip dested Agents Of Black Sun / Vengeance Of The Dark Prince. "
    "Cor: Private Platform dested Coruscant: Private Platform. "
    "Cor: Palpatine's Quarters dested Coruscant: Palpatine's Quarters. "
    "Ni Chuba Na?? dested Ni Chuba Na??. "
    "Imp. Justice dested Imperial Justice. "
    "Grievous, Hunter of Jedi dested Grievous, Hunter Of Jedi. "
    "The Mandalorian, father of Fett dested Jango Fett, The Assassin. "
    "Zuckuss in Mist Hunter dested Zuckuss In Mist Hunter. "
    "B. Flagship sites dested Blockade Flagship: Docking Bay / Hallway / Bridge. "
    "Oh, Switch off dested Oh, Switch Off. "
    "Sniper + Dark Strike dested Sniper & Dark Strike. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Masterful Move combo dested Masterful Move & Endor Occupation. "
    "Sith Fury combo dested Sith Fury & End This Destructive Conflict. "
    "Line 13 replacement Something Special Planned For Them. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Rendezvous Point"),
    n("Superficial Damage", True),
    n("Republic Logistics"),
    n("Heading For The Medical Frigate"),
    n("Hidden Base / Systems Will Slip Through Your Fingers"),
    n("Dressel"),
    n("Nar Shaddaa"),
    n("Roche"),
    n("Naboo", True),
    n("Kessel"),
    n("Rogue Squadron Tactics"),
    n("Slayn & Korpil Facilities"),
    n("Weapons Display"),
    n("Imperial Atrocity", True),
    n("A Jedi's Plans"),
    n("Power Harpoon"),
    n("Concussion Missiles", qty=3),
    n("SW-4 Ion Cannon", qty=3),
    n("B-wing Bomber", qty=8),
    n("Republic Gunship Wing", qty=5),
    n("Aim High", True),
    n("Tycho Celchu", True),
    n("Ten Numb", True),
    n("Concentrate All Fire", qty=2),
    n("Steady Aim", qty=2),
    n("Hit And Run", qty=3),
    n("All Wings Report In", qty=2),
    n("Hyper Escape", qty=3),
    n("Power Pivot", qty=2),
    n("It's Not My Fault", True, qty=2),
    n("Corellian Slip", True),
    n("Houjix", True),
    n("Direct Assault"),
    n("Rapid Fire"),
    n("Rebel Artillery"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Affect Mind", True),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred", True),
    n("Weapons Display", True),
    n("Aim High"),
    n("Ultimatum", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not", True),
    n("Battle Plan", True),
]
LS_ADD = [
    n("Jabba's Prize"),
]


DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Prepared Defenses", True),
    n("Coruscant: Private Platform"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Imperial Justice", True),
    n("The Phantom Menace", qty=2),
    n("Blaster Rack", True),
    n("Something Special Planned For Them", True),
    n("Protocol Failure"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Galen Marek, Starkiller", qty=2),
    n("IG-100 Magna Guard", qty=2),
    n("Battle Droid Squad", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Velken Tezeri", True),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Zuckuss In Mist Hunter"),
    n("Nal Hutta"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Bridge"),
    n("Oh, Switch Off"),
    n("Sniper & Dark Strike"),
    n("Close Call", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Operational As Planned", True),
    n("Masterful Move & Endor Occupation"),
    n("Lightsaber Deficiency", True),
    n("Sith Fury & End This Destructive Conflict"),
    n("Sonic Bombardment", True, qty=2),
    n("Force Field", True, qty=2),
    n("Aurra Sing's Blaster Rifle"),
    n("Trophy Of A Kill", qty=2),
    n("Dark Jedi Lightsaber", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("Lateral Damage"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Imperial Detention"),
    n("Come Here You Big Coward"),
    n("Weapon Of A Sith"),
    n("Fanfare", True),
    n("Firepower", True),
    n("Abyss", True),
    n("Allegations Of Corruption", True),
    n("Battle Order", True),
    n("Secret Plans", True),
    n("Resistance", True),
]
DS_ADD = []
