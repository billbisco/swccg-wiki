#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 typed GEMP: Patrick Johnson.

Source: MPC-2014-Day-1-Main-Event.pdf pages 61–62 (typed GEMP).
Username PMJ on Light, PMT on Dark.
"""
from __future__ import annotations

PLAYER = "Patrick Johnson"
USERNAME = "PMJ"
LS_USERNAME = "PMJ"
DS_USERNAME = "PMT"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 61
DS_PAGE = 62
LS_SCAN = "2014 Match Play Championship Day 1 Patrick Johnson LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Patrick Johnson DS.png"
NOTE = "Typed GEMP list."
LS_NOTE = (
    "Typed GEMP. Username PMJ. We Have A Plan / They Will Be Lost And Confused. "
    "Republic Gunship Wing crossed, I've Decided To Go Back (V) dested I've Decided "
    "To Go Back (V). Unique * is uniqueness, not (V). (V) from written (V). "
    "Much to Learn, You Still Have dested Much To Learn You Still Have. "
    "Dorme' dested Dorme. Unique overcounts sheet-accurate (Queen Amidala x3, "
    "Panaka, Protector Of The Queen x3, A Jedi's Resilience x2, Imperial Atrocity "
    "(V) x2, Control & Tunnel Vision x2, Smoke Screen x2, Obi-Wan Kenobi, Jedi "
    "Knight (V) x2, Mace Windu, Master Of The Order x2, Anakin Skywalker, Padawan "
    "Learner x2)."
)
DS_NOTE = (
    "Typed GEMP. Username PMT. Carbon Chamber Testing / My Favorite Decoration. "
    "Jabba's Prize/Jabba's Prize dested Jabba's Prize. ***Rodian (V) dested Rodian "
    "(V) unique overcount. Slave I, Symbol Of Fear dested Slave I, Symbol Of Fear. "
    "Fanfare (Tatooine) (V) dested Fanfare (V). P-59 dested P-59. Unique overcounts "
    "sheet-accurate (Maul's Sith Infiltrator x2, Darth Maul x2, Stunning Leader x2, "
    "None Shall Pass (V) x2, P-59 x2, ComScan Detection (V) x2, We Must Accelerate "
    "Our Plans x2, Imperial Barrier x2). (V) from written (V)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We Have A Plan / They Will Be Lost And Confused"
LS_CARDS = [
    n("We Have A Plan / They Will Be Lost And Confused"),
    n("Naboo: Theed Palace Courtyard"),
    n("Naboo: Theed Palace Hallway"),
    n("Naboo: Theed Palace Throne Room"),
    n("Wokling", True),
    n("Civil Disorder", True),
    n("Quick Draw", True),
    n("Heading For The Medical Frigate"),
    n("Anger, Fear, Aggression", True),
    n("Found Someone You Have & Higher Ground"),
    n("Blaster Deflection"),
    n("A Jedi's Resilience", qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("Much To Learn You Still Have"),
    n("Control & Tunnel Vision", qty=2),
    n("We'll Take The Long Way"),
    n("Ki-Adi-Mundi", True),
    n("Queen Amidala", qty=3),
    n("Wesa Gotta Grand Army", qty=2),
    n("Ascension Guns", True),
    n("Speak With The Jedi Council"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Lady Luck"),
    n("Bravo Fighter", True),
    n("Obi-Wan's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Smoke Screen", qty=2),
    n("Panaka, Protector Of The Queen", qty=3),
    n("Obi-Wan Kenobi, Jedi Knight", True, qty=2),
    n("Lando Calrissian, Unlikely Hero"),
    n("Clash Of Sabers"),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Jerus Jannick"),
    n("Guardian's Lightsaber"),
    n("I've Decided To Go Back", True),
    n("Anakin Skywalker, Padawan Learner", qty=2),
    n("Dorme"),
    n("Captain Rex, 501st Legion"),
    n("Strikeforce", True),
    n("Dodge"),
    n("Seeking An Audience", True),
    n("Sai'torr Kal Fas", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sense"),
    n("Yoda, Master Of The Force"),
    n("Either Way, You Win", True),
]
LS_SHIELDS = [
    n("He Can Go About His Business", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Only Jedi Carry That Weapon"),
    n("Planetary Defenses", True),
    n("Simple Tricks And Nonsense"),
    n("The Professor", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Do, Or Do Not"),
    n("A Tragedy Has Occurred"),
    n("Affect Mind", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Chasm", True),
]
LS_ADD = []


DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: Security Tower", True),
    n("Carbonite Chamber Console", True),
    n("Jabba's Prize"),
    n("Any Methods Necessary"),
    n("Jabba's Palace: Dungeon"),
    n("Despair", True),
    n("Boba Fett, Relentless Bounty Hunter"),
    n("Boba Fett's Blaster Rifle", True),
    n("Slave I, Symbol Of Fear"),
    n("Where Are You Taking This... Thing?"),
    n("Imperial Propaganda", True),
    n("Mara Jade With Lightsaber"),
    n("Ket Maliss, Shadow Killer"),
    n("Jabba's Haven"),
    n("Tatooine"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Darth Maul", qty=2),
    n("Imperial Artillery"),
    n("Jango Fett, The Assassin"),
    n("Scum And Villainy"),
    n("Rodian", True),
    n("Elis Helrot"),
    n("Stunning Leader", qty=2),
    n("Hutt Bounty", True),
    n("Masterful Move & Endor Occupation"),
    n("Cold Feet", True),
    n("Bane Malar", True),
    n("Something Special Planned For Them", True),
    n("Twi'lek Advisor", True),
    n("None Shall Pass", True, qty=2),
    n("Probot"),
    n("P-59", qty=2),
    n("Dengar With Blaster Carbine", True),
    n("Defensive Fire", True),
    n("Kitik Keed'kak", True),
    n("4-LOM With Concussion Rifle", True),
    n("A Dark Time For The Rebellion", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Hidden Weapons"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Imperial Barrier", qty=2),
    n("Jabba The Hutt", True),
    n("Death Star: War Room", True),
    n("ComScan Detection", True, qty=2),
    n("Blockade Flagship: Bridge"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Tatooine: Docking Bay 94"),
    n("Jabba's Palace: Audience Chamber"),
    n("IG-88", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?"),
    n("There Is No Try"),
    n("Weapon Of A Sith"),
    n("Secret Plans"),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
    n("Abyss", True),
]
DS_ADD = []
