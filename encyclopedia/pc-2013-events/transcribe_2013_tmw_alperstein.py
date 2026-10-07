#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Barry Alperstein Xerox Hunt Down / MWYHL."""
from __future__ import annotations

PLAYER = "Barry Alperstein"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 33
DS_PAGE = 32
LS_SCAN = "2013 Texas Mini Worlds Day 1 p33 Barry Alperstein LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p32 Barry Alperstein DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name Barry A + Matt S dested Barry Alperstein (confirmed Day 1 name). "
    "Username blank. Deck Name move Along. LIGHT checked. "
    "Do not dest as a new person. Do not rewrite 2013 MPC Alperstein leftover "
    "or 2013 Worlds Alperstein leftover. "
    "MWYHL dested Mind What You Have Learned / Save You It Can. "
    "Dag dested Dagobah. "
    "BP + DTF dested Battle Plan & Draw Their Fire. "
    "DoDN + WA dested Do, Or Do Not & Wise Advice. "
    "It is the future you see dested It Is The Future You See. "
    "Ackbar dested Admiral Ackbar. "
    "Blaster Deflect dested Blaster Deflection. "
    "Armed & Dangerous Combo dested Armed And Dangerous & Krayt Dragon Howl. "
    "Incon Barriers dested Inconsequential Barriers. "
    "HCF dested Han, Chewie, And The Falcon. "
    "C + TV dested Control & Tunnel Vision. "
    "Dag: Jungle dested Dagobah: Jungle. "
    "Luke, JK dested Luke Skywalker, Jedi Knight. "
    "Jedi Lev dested Jedi Levitation. "
    "Mace dested Mace Windu. "
    "SATM + BP dested Sorry About The Mess & Blaster Proficiency. "
    "Dag: Yoda's Hut dested Dagobah: Yoda's Hut. "
    "H1: WR dested Home One: War Room. "
    "H1 dested Home One. "
    "Imp Atrocity dested Imperial Atrocity. "
    "Clash dested Clash Of Sabers. "
    "OOC + TT dested Out Of Commission & Transmission Terminated. "
    "R2 in R5 dested Artoo-Detoo In Red 5. "
    "Ant man + RR dested Antilles Maneuver & Rebel Reinforcements. "
    "Dag: Bog Clearing dested Dagobah: Bog Clearing. "
    "Elegant LS dested Elegant Lightsaber. "
    "Way of Things dested The Way Of Things. "
    "Mace MOT dested Mace Windu, Master Of The Order. "
    "Fallen Jedi dested Fallen Jedi as written. "
    "Honor dested Honor Of The Jedi. "
    "Naboo TP Generator dested Naboo: Theed Palace Generator. "
    "AFA dested Anger, Fear, Aggression. "
    "Tragedy dested A Tragedy Has Occurred. "
    "He Can Go About His dested He Can Go About His Business. "
    "Simp Tricks dested Simple Tricks And Nonsense. "
    "Optimism dested Let's Keep A Little Optimism Here. "
    "DDTA dested Don't Do That Again. "
    "Only Jedi Carry dested Only Jedi Carry That Weapon. "
    "Insight dested Your Insight Serves You Well. "
    "Weapons Disp dested Weapons Display. "
    "Jabba's Prize dested Jabba's Prize. "
    "Planetary Def dested Planetary Defenses. "
    "Additional 6 Jedi Tests dested the six Jedi Tests. "
    "Unique overcounts sheet-accurate: Luke's Bionic Hand x2, "
    "Elegant Lightsaber x2, Armed And Dangerous & Krayt Dragon Howl x2, "
    "Rebel Leadership x3, Luke Skywalker, Jedi Knight x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name Barry Alperstein. Username blank. "
    "Deck Name Nothing New to see here. Event Name Texas. DARK checked. "
    "Do not dest as a new person. Do not rewrite 2013 MPC Alperstein leftover "
    "or 2013 Worlds Alperstein leftover. "
    "HD dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Sith's plans dested A Sith's Plans. "
    "Imp City dested Coruscant: Imperial City. "
    "Prep Def dested Prepared Defenses. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "Bridge dested Blockade Flagship: Bridge. "
    "3rd Marker dested Hoth: Defensive Perimeter (3rd Marker). "
    "Galen's Fighter dested Rogue Shadow. "
    "Blizz 4 dested Blizzard 4. "
    "Nevar dested General Nevar. "
    "Fett, BH dested Boba Fett, Bounty Hunter. "
    "Emperor Palp dested Emperor Palpatine. "
    "Mara w/ Saber dested Mara Jade With Lightsaber. "
    "Dr E + Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Vader, Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "DV DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "4-LOM w Rifle dested 4-LOM With Concussion Rifle. "
    "Galen dested Galen Marek, Starkiller. "
    "Dengar w Carbine dested Dengar With Blaster Carbine. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Thrawn dested Grand Admiral Thrawn. "
    "Presence dested Presence Of The Force. "
    "Imp Justice dested Imperial Justice. "
    "Galen's Saber dested Galen's Lightsaber, Vader's Gift. "
    "Vader's Saber dested Vader's Lightsaber. "
    "MM + EO dested Masterful Move & Endor Occupation. "
    "Weapon Lev Combo dested Weapon Levitation & The Empire's Back. "
    "Sniper + DS dested Sniper & Dark Strike. "
    "They're Still Coming Thru dested They're Still Coming Through!. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "K&D dested Knowledge And Defense. "
    "We'll Take Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Imp Detention dested Imperial Detention. "
    "AUG dested A Useless Gesture. "
    "TINT dested There Is No Try. "
    "BO dested Battle Order. "
    "SP dested Secret Plans. "
    "CHYBC dested Come Here You Big Coward. "
    "Allegations dested Allegations Of Corruption. "
    "Weapon of A Sith dested Weapon Of A Sith. "
    "Force Field line 55 (V) and line 56 checkbox empty kept as separate copies. "
    "Unique overcounts sheet-accurate: Emperor Palpatine x2, "
    "Darth Vader, Dark Lord Of The Sith x2, Galen Marek, Starkiller x3, "
    "Force Field x2, We Must Accelerate Our Plans x3. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Dagobah"),
    n("Thrown Back", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Strong Is Vader"),
    n("It Is The Future You See"),
    n("Luke's Bionic Hand", qty=2),
    n("Projection Of A Skywalker"),
    n("Admiral Ackbar", True),
    n("Reflection", True),
    n("Quick Draw", True),
    n("Luke's Backpack"),
    n("Escape Pod"),
    n("Blaster Deflection"),
    n("Elegant Lightsaber", qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl", qty=2),
    n("Obi-Wan Kenobi", True),
    n("Inconsequential Barriers"),
    n("Corellian Slip"),
    n("Daughter Of Skywalker", True),
    n("Han, Chewie, And The Falcon", True),
    n("Control & Tunnel Vision"),
    n("Dagobah: Jungle"),
    n("Dodge"),
    n("Rebel Leadership", True, qty=3),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Jedi Levitation", True),
    n("Mace Windu", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("It's A Trap!"),
    n("Yoda's Hope"),
    n("Dagobah: Yoda's Hut"),
    n("Home One: War Room"),
    n("Home One"),
    n("Under Attack"),
    n("Imperial Atrocity"),
    n("Courage Of A Skywalker", True),
    n("Clash Of Sabers"),
    n("It Could Be Worse"),
    n("Bravo Fighter"),
    n("Out Of Commission & Transmission Terminated"),
    n("Houjix"),
    n("Artoo-Detoo In Red 5"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Dagobah: Bog Clearing"),
    n("Seeking An Audience", True),
    n("The Way Of Things"),
    n("Mace Windu, Master Of The Order"),
    n("Fallen Jedi"),
    n("Yoda", True),
    n("Honor Of The Jedi"),
    n("Naboo: Theed Palace Generator"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("He Can Go About His Business", True),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry"),
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Only Jedi Carry That Weapon"),
    n("The Professor"),
    n("Your Insight Serves You Well", True),
    n("Chasm", True),
    n("Weapons Display", True),
]
LS_ADD = [
    n("Jabba's Prize"),
    n("Planetary Defenses"),
    n("Battle Plan"),
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("A Sith's Plans"),
    n("Coruscant: Imperial City"),
    n("Coruscant"),
    n("Prepared Defenses", True),
    n("Endor Shield", True),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Blockade Flagship: Bridge"),
    n("Endor"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Rogue Shadow"),
    n("Victory"),
    n("Blizzard 4"),
    n("General Nevar"),
    n("Boba Fett, Bounty Hunter"),
    n("Emperor Palpatine", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Garindan"),
    n("Dr. Evazan & Ponda Baba"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("Galen Marek, Starkiller", qty=3),
    n("Dengar With Blaster Carbine", True),
    n("Juno Eclipse, Black Leader"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Protocol Failure"),
    n("Presence Of The Force"),
    n("No Escape"),
    n("A Sith's Weapon"),
    n("Blaster Rack", True),
    n("Imperial Justice", True),
    n("Revenge Of The Sith"),
    n("Tarkin's Bounty", True),
    n("Emperor's Power", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Vader's Lightsaber"),
    n("Stop Motion", True),
    n("Force Lightning"),
    n("Cold Feet", True),
    n("Masterful Move & Endor Occupation"),
    n("Force Push", True),
    n("Weapon Levitation & The Empire's Back"),
    n("One Beautiful Thing"),
    n("Ghhhk"),
    n("Sniper & Dark Strike"),
    n("They're Still Coming Through!"),
    n("Lightsaber Deficiency", True),
    n("Force Field", True),
    n("Force Field"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Imperial Detention"),
    n("Death Star Sentry", True),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("There Is No Try"),
    n("Fanfare", True),
    n("Abyss", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Resistance"),
]
DS_ADD = [
    n("Come Here You Big Coward", True),
    n("Allegations Of Corruption"),
    n("Weapon Of A Sith"),
]
