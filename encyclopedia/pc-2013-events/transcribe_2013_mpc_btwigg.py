#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: BTwigg Xerox LS+DS."""
from __future__ import annotations

PLAYER = "BTwigg"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 96
DS_PAGE = 95
LS_SCAN = "2013 Match Play Championship p96 BTwigg LS.png"
DS_SCAN = "2013 Match Play Championship p95 BTwigg DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. BTwigg. Username blank. Light. "
    "Deck title I AM THE TAG TEAM CHAMPIONS!. "
    "Anger, Fear, Aggression dested Anger, Fear, Aggression. "
    "X-wing Laser Cannon as written. Organized Attack as written. "
    "Gold Leader in Gold 1 dested Gold Leader In Gold 1. "
    "Ice Storm as written. Projection Of A Skywalker as written. "
    "We're Doomed as written. T-47 Battle Formation as written. Haven as written. "
    "Maneuvering Flaps + Nick Of Time dested Maneuvering Flaps & Nick Of Time "
    "((V) also written in the name; checkbox checked). "
    "Frostbite (V) written in the name; dested Frostbite. "
    "Wrist Comlink as written. Hoth as written. "
    "Hoth 1st Marker dested Hoth: Main Power Generators (1st Marker). "
    "Hoth 2nd Marker dested Hoth: Snow Trench (2nd Marker). "
    "Hoth 3rd Marker dested Hoth: Defensive Perimeter (3rd Marker). "
    "Hoth 4th Marker dested Hoth: North Ridge (4th Marker). "
    "Hoth Docking Bay dested Hoth: Echo Docking Bay. "
    "Jek Porkins as written. Commander Wedge Antilles as written. "
    "Wedge Antilles, Red Squadron Leader dested Wedge Antilles, Red Squadron Leader. "
    "Veteran Rogue (Kin Kian) dested Veteran Rogue. "
    "Zev Senesca as written. Derek Hobbie Klivian dested Derek 'Hobbie' Klivian. "
    "Dash Rendar v dested Dash Rendar. I'm With You Too as written. "
    "Menace Fades as written. Escape Pod as written. "
    "Squadron Assignments as written. Echo Base Garrison as written. "
    "All Wings / Darklighter Spin dested All Wings Report In & Darklighter Spin. "
    "Wokling as written. Rycar Ryjerd as written. "
    "We Wish To Board At Once as written. "
    "Lando Calrissian, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Rogue 1–4 as written. Snowspeeder Garrison (out of play) dested Snowspeeder Garrison. "
    "R2 in Red 5 dested Artoo-Detoo In Red 5. Millennium Falcon as written. "
    "Red 6 as written. Grimtaash dested Grimtaash. "
    "Vergence in the Force dested A Vergence In The Force. "
    "Rebel Barrier as written; line 55 parenthetical (Luke Skywalker). "
    "Commander Luke Skywalker as written. Dual Laser Cannon dested Dual Laser Cannon. "
    "Desperate Tactics as written. "
    "Heading For The Medical Frigate dested Heading For The Medical Frigate. "
    "Local Uprising / Liberation dested Local Uprising / Liberation. "
    "He Can Go About His Business dested He Can Go About His Business. "
    "Do, Or Do Not dested Do, Or Do Not. Affect Mind as written. "
    "Ultimatum as written. Weapons Display as written. "
    "Don't Do That Again dested Don't Do That Again. "
    "A Tragedy Has Occurred dested A Tragedy Has Occurred. "
    "Simple Tricks And Nonsense parenthetical (without (V)); checkbox empty; "
    "dested Simple Tricks And Nonsense. "
    "Battle Plan as written. Aim High as written. Chasm dested Chasm. "
    "Let's Keep A Little Optimism Here dested Let's Keep A Little Optimism Here. "
    "Form left column reprints 37–38 on lines 39–40 are We Wish To Board At Once dittos. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. BTwigg. Username blank. Dark. "
    "Deck title NO… I Am!. "
    "You Swindled Me dested You Swindled Me!. You Are Beaten as written. "
    "Contract Killers / Feared Thru the Galaxy dested "
    "Contract Killers / Feared Throughout The Galaxy. "
    "Trophy Of A Kill dested Trophy Of A Kill; Mara Jade, The Emperor's Hand circled "
    "on lines 4–6 (squeezed on the same slots). "
    "Mara Jade's Lightsaber dested Mara Jade's Lightsaber. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Knowledge + Defense dested Knowledge And Defense. "
    "Prepared Defenses dested Prepared Defenses. "
    "Operational As Planned dested Operational As Planned. "
    "Disarmed as written. Nevar Yalnal dested Nevar Yalnal. "
    "Jabba's Haven (Jabba's Palace (V) in parens) dested Jabba's Haven; checkbox empty. "
    "Abyssin Ornament dested Abyssin Ornament. "
    "Imbalance + Kintan Strider dested Imbalance & Kintan Strider. "
    "One Beautiful Thing as written. On The Hunt as written. "
    "A Sith's Weapon as written; extra writing on the right of line 24. "
    "Masterful Move & Endor Occupation dested Masterful Move & Endor Occupation. "
    "Ghhhk & Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. "
    "Guild Of Assassins dested Guild Of Assassins. "
    "Sonic Bombardment dested Sonic Bombardment. "
    "Death Mark & Hutt Bounty dested Death Mark & Hutt Bounty. "
    "I've Lost Artoo! dested I've Lost Artoo!. Force Field as written. "
    "Gift Of The Master dested Gift Of The Master. Blaster Rack as written. "
    "Force Push as written. Keder The Black dested Keder The Black. Arica as written. "
    "Aurra Sing's Blaster Rifle dested Aurra Sing's Blaster Rifle. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Aurra Sing, Deadly Assassin dested Aurra Sing, Deadly Assassin. "
    "Guri as written. Rodian as written. J'Quille dested J'Quille. "
    "The Mandalorian, Father Of Fett dested Jango Fett, The Assassin. "
    "Ket Maliss, Shadow Killer dested Ket Maliss, Shadow Killer. "
    "Bane Malar dested Bane Malar. "
    "Boba Fett, Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Slave I, Symbol Of Fear dested Slave I, Symbol Of Fear. "
    "Coruscant: Sub City Lair dested Coruscant: Sub City Lair. "
    "ditto Casino dested Coruscant: Casino. "
    "Palpatine Qts dested Coruscant: Palpatine's Quarters. Coruscant as written. "
    "Cloud City: Security Tower dested Cloud City: Security Tower. "
    "Nal Hutta dested Nal Hutta. "
    "I Find Your Lack Of Faith Disturbing dested I Find Your Lack Of Faith Disturbing. "
    "Do They Have A Code Clearance? dested Do They Have A Code Clearance?. "
    "Allegations Of Corruption dested Allegations Of Corruption. "
    "Leave Them To Me dested Leave Them To Me. "
    "Come Here You Big Coward dested Come Here You Big Coward. "
    "Battle Order as written. A Useless Gesture dested A Useless Gesture. "
    "Resistance as written. Secret Plans dested Secret Plans. "
    "Weapon Of A Sith dested Weapon Of A Sith. Abyss dested Abyss. "
    "There Is No Try dested There Is No Try. "
    "Form left column reprints 37–38 on lines 39–40 are Arica dittos. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Local Uprising / Liberation"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("X-wing Laser Cannon"),
    n("Organized Attack"),
    n("Gold Leader In Gold 1", True),
    n("Ice Storm"),
    n("Projection Of A Skywalker", qty=2),
    n("We're Doomed"),
    n("T-47 Battle Formation"),
    n("Haven"),
    n("Maneuvering Flaps & Nick Of Time", True),
    n("Frostbite", True, qty=2),
    n("Wrist Comlink"),
    n("Hoth"),
    n("Hoth: Main Power Generators (1st Marker)", True),
    n("Hoth: Snow Trench (2nd Marker)"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Hoth: North Ridge (4th Marker)"),
    n("Hoth: Echo Docking Bay"),
    n("Jek Porkins", True),
    n("Commander Wedge Antilles", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Veteran Rogue"),
    n("Zev Senesca"),
    n("Derek 'Hobbie' Klivian", True),
    n("Dash Rendar", True),
    n("I'm With You Too", True),
    n("Menace Fades"),
    n("Escape Pod", True, qty=2),
    n("Squadron Assignments"),
    n("Echo Base Garrison"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Wokling", True),
    n("Rycar Ryjerd", True),
    n("Organized Attack"),
    n("We Wish To Board At Once", qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Rogue 1"),
    n("Rogue 2"),
    n("Rogue 3"),
    n("Rogue 4"),
    n("Snowspeeder Garrison"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Millennium Falcon"),
    n("Red 6", qty=2),
    n("Grimtaash"),
    n("A Vergence In The Force"),
    n("Rebel Barrier", qty=2),
    n("Commander Luke Skywalker", True),
    n("Dual Laser Cannon", True),
    n("Desperate Tactics"),
    n("Heading For The Medical Frigate", True),
    n("Local Uprising / Liberation", True),
]
LS_SHIELDS = [
    n("He Can Go About His Business", True),
    n("Do, Or Do Not"),
    n("Affect Mind", True),
    n("Ultimatum"),
    n("Weapons Display", True),
    n("Don't Do That Again", True),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("Aim High"),
    n("Chasm", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("You Swindled Me!", True),
    n("You Are Beaten"),
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("Trophy Of A Kill", qty=3),
    n("Mara Jade's Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Knowledge And Defense", True),
    n("Prepared Defenses", True),
    n("Operational As Planned", True),
    n("Disarmed", qty=2),
    n("Nevar Yalnal", qty=2),
    n("Jabba's Haven"),
    n("Abyssin Ornament", True, qty=3),
    n("Imbalance & Kintan Strider"),
    n("One Beautiful Thing", qty=2),
    n("On The Hunt"),
    n("A Sith's Weapon"),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Guild Of Assassins"),
    n("Sonic Bombardment", True, qty=3),
    n("Death Mark & Hutt Bounty", True),
    n("I've Lost Artoo!", True),
    n("Force Field", True),
    n("Gift Of The Master"),
    n("Blaster Rack", True),
    n("Force Push", True),
    n("Keder The Black"),
    n("Arica", True, qty=3),
    n("Aurra Sing's Blaster Rifle"),
    n("Galen Marek, Starkiller", qty=3),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Guri"),
    n("Rodian", True),
    n("J'Quille", True),
    n("Jango Fett, The Assassin"),
    n("Ket Maliss, Shadow Killer"),
    n("Bane Malar", True),
    n("Boba Fett, Prepared Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Coruscant: Sub City Lair"),
    n("Coruscant: Casino"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant"),
    n("Cloud City: Security Tower", True),
    n("Nal Hutta"),
]
DS_SHIELDS = [
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Do They Have A Code Clearance?", True),
    n("Allegations Of Corruption"),
    n("Leave Them To Me", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("Abyss", True),
    n("There Is No Try"),
]
DS_ADD = []
