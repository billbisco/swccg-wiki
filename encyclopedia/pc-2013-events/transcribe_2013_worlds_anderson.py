#!/usr/bin/env python3
"""2013 World Championship Day 2 typed Print Form: John Anderson LS+DS."""
from __future__ import annotations

PLAYER = "John Anderson"
USERNAME = "puck71"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 5
DS_PAGE = 6
LS_SCAN = "2013 Worlds Day 2 p05 John Anderson LS.png"
DS_SCAN = "2013 Worlds Day 2 p06 John Anderson DS.png"
NOTE = "Typed 2013 Xerox Print Form. Username puck71."


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies"),
    n("Nar Shaddaa"),
    n("Nar Shaddaa: Undercity"),
    n("Scoundrel's Luck"),
    n("Scoundrel's Charm"),
    n("Scoundrel's Bravado"),
    n("Scoundrel's Ingenuity"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Luke, Trust Me"),
    n("Squadron Assignments"),
    n("Hear Me Baby, Hold Together", True),
    n("Houjix"),
    n("Redeemed Apprentice"),
    n("Corellian Retort", True),
    n("Rebel Artillery"),
    n("Control & Tunnel Vision", qty=2),
    n("Moving To Attack Position", qty=2),
    n("Booster Terrik"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Escape Pod", True, qty=2),
    n("We Wish To Board At Once", qty=2),
    n("Scrambled Transmission", True),
    n("Flash Of Insight", True),
    n("Imperial Atrocity", True),
    n("Projection Of A Skywalker"),
    n("I Can't Believe He's Gone", True),
    n("Menace Fades"),
    n("Landing Claw"),
    n("Kessel Run", True),
    n("Han's Toolkit"),
    n("Kyle Katarn's Blaster Rifle"),
    n("Spaceport Scoundrels Guild"),
    n("Nar Shaddaa: Scoundrel's Rest"),
    n("Kessel"),
    n("Obi-Wan In Radiant VII"),
    n("Outrider"),
    n("Red Squadron 7", True),
    n("Pulsar Skate"),
    n("Millennium Falcon"),
    n("Kyle Katarn", qty=4),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Dash Rendar"),
    n("Corran Horn", qty=2),
    n("Captain Han Solo"),
    n("Boushh"),
    n("LE-BO2D9 (Leebo)", True),
    n("Tycho Celchu", True),
    n("Mirax Terrik"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("Only Jedi Carry That Weapon"),
    n("Do, Or Do Not"),
    n("There Is Another"),
    n("Wise Advice"),
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense"),
    n("Weapons Display", True),
    n("Aim High"),
    n("Chasm", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
]
LS_ADD = []


DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("Coruscant"),
    n("Coruscant: Sub City Lair"),
    n("On The Hunt"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Guild Of Assassins"),
    n("Jabba's Haven"),
    n("Force Field", True),
    n("Ket Maliss, Shadow Killer"),
    n("Levitation Attack", True),
    n("Trophy Of A Kill", qty=3),
    n("Stop Motion", True),
    n("Aurra Sing", True, qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Abyssin Ornament", True, qty=3),
    n("Image Of The Dark Lord", True),
    n("Masterful Move", qty=2),
    n("Blaster Rack", True),
    n("Imperial Propaganda", True),
    n("Disarmed", qty=2),
    n("Guri"),
    n("Jango Fett, The Assassin"),
    n("Greedo With Blaster Pistol"),
    n("Keder The Black"),
    n("Imbalance & Kintan Strider", qty=2),
    n("Galen Marek, Starkiller", qty=2),
    n("Nevar Yalnal"),
    n("A Sith's Weapon"),
    n("Cold Feet", True),
    n("Ghhhk"),
    n("Boba Fett, Prepared Hunter"),
    n("Nal Hutta"),
    n("Arica", True, qty=3),
    n("Mandalorian Armor"),
    n("Sith Fury & End This Destructive Conflict"),
    n("Slave One, Symbol Of Fear"),
    n("Weapon Levitation & The Empire's Back"),
    n("J'Quille", True),
    n("Dark Jedi Lightsaber", True),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Casino"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Death Mark & Hutt Bounty"),
    n("Mara Jade's Lightsaber", True),
    n("Bane Malar", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("Come Here You Big Coward"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Fanfare", True),
    n("Secret Plans"),
    n("Battle Order"),
    n("We'll Let Fate-a Decide, Huh?", True),
]
DS_ADD = []
