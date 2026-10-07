#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1 typed slang printout: Allen Gamble LS+DS."""
from __future__ import annotations

PLAYER = "Allen Gamble"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 37
DS_PAGE = 36
LS_SCAN = "2013 Texas Mini Worlds Day 1 p37 Allen Gamble LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p36 Allen Gamble DS.png"
LS_NOTE = (
    "Typed slang printout (not a handwritten Xerox form). "
    "Name Allen Gamble LS. Username blank. "
    "Do not dest as a new person. Do not rewrite 2013 TMW Banger leftover. "
    "AFAv dested Anger, Fear, Aggression. "
    "WYSv dested Watch Your Step / This Place Can Be A Little Rough. "
    "Millenium Falcon dested Millennium Falcon. "
    "Insurrection & Aim High dested Insurrection & Aim High. "
    "Spaceport Scoundrel's Guild dested Spaceport Scoundrels Guild. "
    "Mace Windu, Master of the Order dested Mace Windu, Master Of The Order. "
    "Fallen Jedi dested Fallen Jedi as written. "
    "Chewie v dested Chewie, Enraged. "
    "Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Dash Rendar v dested Dash Rendar. "
    "Romas 'Lock' Navander dested Romas 'Lock' Navander. "
    "Obi-wan in Radiant VII dested Obi-Wan In Radiant VII. "
    "Booster in Pulsar Skate dested Booster In Pulsar Skate. "
    "I Hope She's Alright dested I Hope She's Alright as written. "
    "Antilles Maneuver v dested Antilles Maneuver. "
    "Desperate Reach v dested Desperate Reach. "
    "Houjix & Out Of Nowhere dested Houjix & Out Of Nowhere. "
    "Simple Tricks dested Simple Tricks And Nonsense. "
    "YISYW dested Your Insight Serves You Well. "
    "Optimism dested Let's Keep A Little Optimism Here. "
    "Professor dested The Professor. "
    "Your Ship? dested Your Ship?. "
    "Unique overcounts sheet-accurate: No Questions Asked x3, "
    "Luke Skywalker, Jedi Knight x2, Dash Rendar x2, "
    "Wedge Antilles, Red Squadron Leader x2, Let The Wookiee Win x2. "
    "v tags on the printout are Holotable virtual versions."
)
DS_NOTE = (
    "Typed slang printout (not a handwritten Xerox form). "
    "Name Allen Gamble DS. Username blank. "
    "Do not dest as a new person. Do not rewrite 2013 TMW Banger leftover. "
    "K&D v dested Knowledge And Defense. "
    "ASM dested A Stunning Move / A Valuable Hostage. "
    "Coruscant: Private Platform dested Coruscant: Private Platform (Docking Bay). "
    "Ni Chuba Na? v dested Ni Chuba Na??. "
    "Blockade Flaghsip: Hallway dested Blockade Flagship: Hallway. "
    "Galen dested Galen Marek, Starkiller. "
    "Cyborg Commander dested Grievous, Hunter Of Jedi. "
    "IG Bodyguard Droid dested IG-100 MagnaGuard. "
    "4LOM with Concussion Rifle v dested 4-LOM With Concussion Rifle. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Dr. Evazan & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Slave 1, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers. "
    "Ability, Ability, Ability v dested Ability, Ability, Ability. "
    "Imbalance & Kintan Strinder dested Imbalance & Kintan Strider. "
    "Oh Switch Off dested Oh, Switch Off. "
    "Self Destruct Mechanism dested Self-Destruct Mechanism. "
    "Coward dested Come Here You Big Coward. "
    "YCHF v dested You Cannot Hide Forever. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "We'll Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Useless Gesture v dested A Useless Gesture. "
    "Weapon of a Sith dested Weapon Of A Sith. "
    "Unique overcounts sheet-accurate: Darth Maul, Young Apprentice x3, "
    "Galen Marek, Starkiller x3, Sonic Bombardment x3, "
    "Grievous, Hunter Of Jedi x2, Force Field x2. "
    "v tags on the printout are Holotable virtual versions."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Spaceport City"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("Home One: Docking Bay"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Scoundrel's Guild"),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Master Qui-Gon", True),
    n("Fallen Jedi"),
    n("Leia, Rebel Princess"),
    n("Chewie, Enraged", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Corran Horn", qty=2),
    n("Dash Rendar", True, qty=2),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Romas 'Lock' Navander"),
    n("Mirax Terrik"),
    n("Palejo Reshad"),
    n("Sergeant Bruckman"),
    n("Spiral"),
    n("Obi-Wan In Radiant VII"),
    n("Lady Luck"),
    n("Booster In Pulsar Skate"),
    n("No Questions Asked", True, qty=3),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Menace Fades"),
    n("Evacuation Control", True),
    n("Civil Disorder", True),
    n("I Hope She's Alright"),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Antilles Maneuver", True, qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Corellian Retort", True, qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Desperate Reach", True),
    n("We Wish To Board At Once"),
    n("Sense", qty=2),
    n("Houjix & Out Of Nowhere"),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Jabba's Prize", True),
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
    n("Your Ship?"),
]
LS_ADD = []


DS_START = "Knowledge And Defense"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Jabba's Haven"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Cloud City: Security Tower"),
    n("Nal Hutta"),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Galen Marek, Starkiller", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Battle Droid Squad", qty=2),
    n("IG-100 MagnaGuard", qty=2),
    n("P-59"),
    n("4-LOM With Concussion Rifle", True),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Dr. Evazan & Ponda Baba"),
    n("Victory"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Grievous' Lightsabers"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("The Phantom Menace", qty=2),
    n("Imperial Propaganda", True),
    n("A Sith's Weapon"),
    n("No Escape"),
    n("Ability, Ability, Ability", True),
    n("Imperial Justice", True),
    n("Blaster Rack", True),
    n("Something Special Planned For Them", True),
    n("Sonic Bombardment", True, qty=3),
    n("Force Field", True, qty=2),
    n("Sniper & Dark Strike"),
    n("Ghhhk"),
    n("Short Range Fighters & Watch Your Back"),
    n("Cold Feet", True),
    n("Masterful Move"),
    n("Imbalance & Kintan Strider"),
    n("Oh, Switch Off"),
    n("A Dark Time For The Rebellion", True),
    n("Self-Destruct Mechanism"),
    n("Operational As Planned", True),
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
