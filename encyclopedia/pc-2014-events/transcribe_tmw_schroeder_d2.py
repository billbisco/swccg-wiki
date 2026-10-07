#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 2 Xerox: Olaf Schroeder (Name Schultz).

Source: 2014-TMW-Day-2.pdf pages 9–10 (2013 form).
Name Schultz dested Olaf Schroeder (informed 99.9%).
"""
from __future__ import annotations

PLAYER = "Olaf Schroeder"
USERNAME = ""
STAGE = "Day 2"
PDF = "2014 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2014 Texas Mini Worlds Day 2 p09 Olaf Schroeder LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 2 p10 Olaf Schroeder DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields). Name Schultz dested Olaf Schroeder."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Schultz dested Olaf Schroeder. Username blank. LIGHT/DARK both empty; cards are Light. "
    "Deck Name Shouldn't have Played this Ever. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough. "
    "SP City dested Corellia: Spaceport City. "
    "H1 WR dested Home One: War Room. "
    "JCC dested Coruscant: Jedi Council Chamber. "
    "Back Door dested Endor: Back Door. "
    "AFA dested Anger, Fear, Aggression. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "Obi w Saber dested Obi-Wan With Lightsaber. "
    "Chewie dested Chewie, Enraged. "
    "Mace Moto dested Mace Windu, Master Of The Order. "
    "Mace dested Mace Windu. "
    "Padme dested Padmé Naberrie. "
    "Lando UH dested Lando Calrissian, Unlikely Hero. "
    "Jarful dested as written. "
    "Falcon dested Millennium Falcon. "
    "H1 dested Home One. "
    "Jedi Saber dested Jedi Lightsaber. "
    "Luke's Saber dested Luke's Lightsaber. "
    "Luke's Hand dested Luke's Bionic Hand. "
    "Obi's Journal dested Obi-Wan's Journal. "
    "Han's Toolkit dested Han's Toolkit. "
    "R Leadership dested Rebel Leadership. "
    "SATM+BP dested Sorry About The Mess & Blaster Proficiency. "
    "Speak with JC dested Speak With The Jedi Council. "
    "Ant Man + RR dested Antilles Maneuver & Rebel Reinforcements. "
    "IFTMF dested Heading For The Medical Frigate. "
    "LTWW dested Let The Wookiee Win. "
    "Your Ship dested Your Ship?. "
    "Only Jedi CTW dested Only Jedi Carry That Weapon. "
    "Optimism dested Let's Keep A Little Optimism Here. "
    "YISYW dested Your Insight Serves You Well. "
    "Unique overcounts sheet-accurate (Luke Skywalker, Jedi Knight x4, "
    "Obi-Wan With Lightsaber x2, Rebel Leadership x3, Punch It! x2, "
    "Let The Wookiee Win x5). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Schultz dested Olaf Schroeder. Username blank. DARK checked. "
    "Deck Name Never played This before. "
    "HD dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Ni Chuba Na dested Ni Chuba Na?. "
    "NO_DEST remaining: Jarful, Juno Eclipse. "
    "Gift of the Master dested Gift Of The Master. "
    "Blaster Rack dested Blaster Rack. "
    "Visage dested Visage Of The Emperor. "
    "Sun Eclipse dested Juno Eclipse as written. "
    "Maul w/ stick dested Darth Maul With Lightsaber. "
    "Lord Sidious dested Darth Sidious. "
    "DVD lots dested Darth Vader, Dark Lord Of The Sith. "
    "DV Betrayer dested Darth Vader, Betrayer Of The Jedi. "
    "Mara w Saber dested Mara Jade With Lightsaber. "
    "Jango Assassin dested Jango Fett, The Assassin. "
    "Boba Fett PH dested Boba Fett, Prepared Hunter. "
    "Dr E + PB dested Dr. Evazan & Ponda Baba. "
    "Dengar w gun dested Dengar With Blaster Carbine. "
    "Meditation Chamber dested Executor: Meditation Chamber. "
    "Holotheatre dested Executor: Holotheatre. "
    "Back Door dested Endor: Back Door. "
    "Flagship Bridge dested Blockade Flagship: Bridge. "
    "CC Prison dested Cloud City: Security Tower. "
    "Slave I SOF dested Slave I, Symbol Of Fear. "
    "Victory dested Victory as written. "
    "Blizz 4 dested Blizzard 4. "
    "MM + EO dested Masterful Move & Endor Occupation. "
    "Omni Box + It's Worse dested Omni Box & It's Worse. "
    "Short Range Combo dested Short Range Fighters & Watch Your Back!. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "I Have You Now dested I Have You Now. "
    "CHYBC dested Come Here You Big Coward. "
    "YCHF dested You Cannot Hide Forever. "
    "Lack of Faith dested I Find Your Lack Of Faith Disturbing. "
    "TINT dested There Is No Try. "
    "Useless Gesture dested A Useless Gesture. "
    "Let Fate Decide dested We'll Let Fate-a Decide, Huh?. "
    "Unique overcounts sheet-accurate (Visage Of The Emperor x2, "
    "Darth Maul With Lightsaber x2, Count Dooku x2, Emperor Palpatine x2, "
    "Darth Vader, Dark Lord Of The Sith x2, Blizzard 4 x2, Sonic Bombardment x3, "
    "Why Didn't You Tell Me? x2, Masterful Move & Endor Occupation x2, "
    "We Must Accelerate Our Plans x3). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Corellia: Spaceport City"),
    n("Home One: War Room"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Endor: Back Door"),
    n("Anger, Fear, Aggression", True),
    n("Wokling", True),
    n("Rycar Ryjerd", True),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Imperial Atrocity", True),
    n("General Solo", True),
    n("Chewie, Enraged", True),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Corran Horn"),
    n("Admiral Ackbar", True),
    n("Leia, Rebel Princess"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Mace Windu, Master Of The Order"),
    n("Mace Windu", True),
    n("Anakin Skywalker, Padawan Learner"),
    n("Padmé Naberrie", True),
    n("Jaina Solo"),
    n("Dash Rendar", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Jarful"),
    n("Millennium Falcon", True),
    n("Lady Luck"),
    n("Home One"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber", True),
    n("Luke's Bionic Hand", True),
    n("Obi-Wan's Journal"),
    n("Han's Toolkit", True),
    n("Rebel Leadership", True, qty=3),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Smoke Screen"),
    n("Sense"),
    n("Speak With The Jedi Council"),
    n("Escape Pod", True),
    n("Houjix"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Punch It!", qty=2),
    n("Alter"),
    n("Heading For The Medical Frigate"),
    n("Let The Wookiee Win", True, qty=5),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Jabba's Prize", True),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Only Jedi Carry That Weapon"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Ship?"),
    n("Aim High"),
    n("Wise Advice"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Knowledge And Defense", True),
    n("Ni Chuba Na?", True),
    n("Conduct Your Search"),
    n("Gift Of The Master"),
    n("Blaster Rack", True),
    n("Visage Of The Emperor", qty=2),
    n("Presence Of The Force"),
    n("Image Of The Dark Lord", True),
    n("Juno Eclipse"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Sidious"),
    n("Count Dooku", qty=2),
    n("Emperor Palpatine", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Grand Moff Tarkin", True),
    n("Mara Jade With Lightsaber"),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Dr. Evazan & Ponda Baba"),
    n("Dengar With Blaster Carbine", True),
    n("Garindan", True),
    n("P-59"),
    n("Executor: Meditation Chamber"),
    n("Executor: Holotheatre"),
    n("Endor: Back Door"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower", True),
    n("Vader's Lightsaber"),
    n("Dooku's Lightsaber"),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Blizzard 4", qty=2),
    n("Ghhhk"),
    n("Monnok"),
    n("Sniper & Dark Strike"),
    n("Prepared Defenses", True),
    n("Force Field", True),
    n("Sonic Bombardment", True, qty=3),
    n("Why Didn't You Tell Me?", True, qty=2),
    n("Masterful Move & Endor Occupation", qty=2),
    n("Omni Box & It's Worse"),
    n("Force Lightning"),
    n("Force Push", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("We Must Accelerate Our Plans", qty=3),
    n("I Have You Now"),
]
DS_SHIELDS = [
    n("Come Here You Big Coward", True),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("Battle Order"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("There Is No Try"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Oppressive Enforcement", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Abyss", True),
    n("Weapon Of A Sith"),
    n("Secret Plans"),
]
DS_ADD = []
