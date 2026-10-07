#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Steve Skilton Xerox LS+DS.

Name field Steve S. Username stevetotheizzo is Steve Skilton
(2014 Philadelphia Premiere Event 3rd Place DS Steve Skilton (stevetotheizz0)).
"""
from __future__ import annotations

PLAYER = "Steve Skilton"
USERNAME = "stevetotheizzo"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 87
DS_PAGE = 88
LS_SCAN = "2013 Match Play Championship p87 Steve S. LS.png"
DS_SCAN = "2013 Match Play Championship p88 Steve S. DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Steve S. Name field also Stevetotheizzo. "
    "E-mail Don't Email Me. Deck title Combat. Light. "
    "We'll Handle This dested We'll Handle This / Duel Of The Fates. "
    "Yoda, Master of the Force dested Yoda, Master Of The Force. "
    "Mace, Master of the Order dested Mace Windu, Master Of The Order. "
    "Mace, Not Master of the Order dested Mace Windu. "
    "Qui-Gon, JM dested Master Qui-Gon. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "Screaming Lando dested Lando Calrissian, Scoundrel. "
    "Luke's Bio Hand dested Luke's Bionic Hand. "
    "Sai-tor dested Sai'torr Kal Fas. "
    "Projection of a Skywalker dested Projection Of A Skywalker. "
    "Dis-f'n-Armed! dested Disarmed. "
    "Atrocity dested Imperial Atrocity. "
    "AFA dested Anger, Fear, Aggression. "
    "Boonta Eve Podrace as written. "
    "Control / TV dested Control & Tunnel Vision. "
    "Blast the Door kid! dested Blast The Door, Kid!. "
    "Bith Shuffle Combo dested The Bith Shuffle & Desperate Reach. "
    "Clinging to the edge dested Clinging To The Edge. "
    "Sense + Recoil dested Sense & Recoil In Fear. "
    "Blaster Defl dested Blaster Deflection. "
    "Armed + Dang Combo dested Armed And Dangerous & Krayt Dragon Howl. "
    "LTWW dested Let The Wookiee Win. "
    "Naboo: Theed Pal Gen dested Naboo: Theed Palace Generator. "
    "Naboo: Theed Pal Gen Core dested Naboo: Theed Palace Generator Core. "
    "Tatooine: Pod Arena dested Tatooine: Podrace Arena. "
    "Yavin 4: Mass War Room dested Yavin 4: Massassi War Room. "
    "Home 1: WR dested Home One: War Room. "
    "HCF dested Han, Chewie, And The Falcon. "
    "Luke's Saber dested Luke's Lightsaber. "
    "Jedi Saber dested Jedi Lightsaber. "
    "Qui-Gon's Ref III Saber dested Qui-Gon's Lightsaber. "
    "Obi-Wan's Non-Ref III Saber dested Obi-Wan's Lightsaber. "
    "DDTA dested Don't Do That Again. "
    "The Prof dested The Professor. "
    "Simple Tricks dested Simple Tricks And Nonsense. "
    "Only Jedi Carry Stuff dested Only Jedi Carry That Weapon. "
    "Your Insight dested Your Insight Serves You Well. "
    "Optimism dested Let's Keep A Little Optimism Here. "
    "Weapons Disp dested Weapons Display. "
    "A Tragedy dested A Tragedy Has Occurred. "
    "Form left column reprints 37–38 on lines 39–40 are Escape Pod and Clinging To The Edge. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Steve S. Name field also Stevetotheizzo. "
    "Deck title Assassins. Dark. "
    "Contract Killers dested Contract Killers / Feared Throughout The Galaxy. "
    "K+D dested Knowledge And Defense. "
    "A Sith's Weapon as written. "
    "I've lost Artoo dested I've Lost Artoo!. "
    "Prepared Def dested Prepared Defenses. "
    "Sonic Bomb dested Sonic Bombardment. "
    "Abyssin Orn dested Abyssin Ornament. "
    "Imp Barrier dested Imperial Barrier. "
    "Masterful Move Combo dested Masterful Move & Endor Occupation. "
    "Force Field v dested Force Field. "
    "One Beautiful Thing as written. "
    "YAB dested You Are Beaten. "
    "Sniper Combo dested Sniper & Dark Strike. "
    "Lightsaber Def dested Lightsaber Deficiency. "
    "Imbalance Combo dested Imbalance & Kintan Strider. "
    "Line 25 You … Control fully crossed; omitted. "
    "Death Mark Combo dested Death Mark & Hutt Bounty. "
    "Prot Failure dested Protocol Failure. "
    "Blast Rack dested Blaster Rack. "
    "Guild of Assassins dested Guild Of Assassins. "
    "On The Hunt as written. "
    "Jabba's Haven as written. "
    "Gift of the Master dested Gift Of The Master. "
    "Keder the Black dested Keder The Black. "
    "Boba Fett PH dested Boba Fett, Prepared Hunter. "
    "Mando, FoF dested Jango Fett, The Assassin. "
    "Ket Maliss, Shadow Killer as written. "
    "Bane Malar dested Bane Malar. "
    "Rodian as written. "
    "Aurra dested Aurra Sing. "
    "Galen dested Galen Marek, Starkiller. "
    "Cor: Sub-City Lair dested Coruscant: Sub City Lair. "
    "Cor: Palp's Quarters dested Coruscant: Palpatine's Quarters. "
    "Cor: Casino dested Coruscant: Casino. "
    "Slave I, Symbol dested Slave I, Symbol Of Fear. "
    "Zuckuss in MH dested Zuckuss In Mist Hunter. "
    "Dark Jedi Saber dested Dark Jedi Lightsaber. "
    "Trophy of a Kill dested Trophy Of A Kill. "
    "MJ's Saber dested Mara Jade's Lightsaber. "
    "Galen's Gift Saber dested Galen's Lightsaber, Vader's Gift. "
    "Weapon of a Sith dested Weapon Of A Sith. "
    "Coward dested Come Here You Big Coward. "
    "I find your lack dested I Find Your Lack Of Faith Disturbing. "
    "You Cannot Hide dested You Cannot Hide Forever. "
    "Form left column reprints 37–38 on lines 39–40 are Bane Malar and Rodian. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("We'll Handle This / Duel Of The Fates"),
    n("Yoda, Master Of The Force", qty=2),
    n("Mace Windu, Master Of The Order"),
    n("Mace Windu", True),
    n("Master Qui-Gon", qty=3),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Luke Skywalker, Jedi Knight", qty=3),
    n("Lando Calrissian, Scoundrel"),
    n("Luke's Bionic Hand", qty=2),
    n("Sai'torr Kal Fas", True),
    n("Projection Of A Skywalker", qty=2),
    n("Disarmed", qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("Anger, Fear, Aggression", True),
    n("Boonta Eve Podrace"),
    n("I Did It!"),
    n("Inner Strength"),
    n("Life Debt"),
    n("Dodge", qty=2),
    n("Control & Tunnel Vision"),
    n("Blast The Door, Kid!"),
    n("Rebel Barrier"),
    n("Podrace Prep"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Rebel Leadership", True, qty=3),
    n("Escape Pod", True),
    n("Clinging To The Edge", True),
    n("Sense & Recoil In Fear", qty=2),
    n("Blaster Deflection", qty=2),
    n("Armed And Dangerous & Krayt Dragon Howl", True, qty=2),
    n("Let The Wookiee Win", True),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Theed Palace Generator Core"),
    n("Tatooine: Podrace Arena"),
    n("Yavin 4: Massassi War Room", True),
    n("Home One: War Room"),
    n("Anakin's Podracer"),
    n("Han, Chewie, And The Falcon", qty=2),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True, qty=2),
    n("Qui-Gon's Lightsaber"),
    n("Obi-Wan's Lightsaber"),
]
LS_SHIELDS = [
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Simple Tricks And Nonsense", True),
    n("Only Jedi Carry That Weapon"),
    n("Aim High"),
    n("Yavin Sentry", True),
    n("Your Insight Serves You Well", True),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred"),
]
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("Knowledge And Defense", True),
    n("A Sith's Weapon"),
    n("I've Lost Artoo!", True),
    n("Prepared Defenses"),
    n("Sonic Bombardment", True, qty=3),
    n("Abyssin Ornament", True, qty=3),
    n("Stunning Leader"),
    n("Imperial Barrier"),
    n("Masterful Move & Endor Occupation"),
    n("Force Field", True),
    n("One Beautiful Thing"),
    n("Cold Feet", True),
    n("You Are Beaten"),
    n("Sniper & Dark Strike"),
    n("Lightsaber Deficiency", True),
    n("Ghhhk"),
    n("Operational As Planned", True),
    n("Nevar Yalnal"),
    n("Imbalance & Kintan Strider"),
    n("Death Mark & Hutt Bounty"),
    n("Disarmed"),
    n("Protocol Failure"),
    n("Blaster Rack", True),
    n("Guild Of Assassins"),
    n("On The Hunt"),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Guri"),
    n("Keder The Black"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Ket Maliss, Shadow Killer"),
    n("Bane Malar", True),
    n("Rodian", True),
    n("Aurra Sing", True, qty=2),
    n("Galen Marek, Starkiller", qty=3),
    n("Arica", True, qty=2),
    n("Coruscant"),
    n("Nal Hutta"),
    n("Coruscant: Sub City Lair"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Casino"),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Dark Jedi Lightsaber", True),
    n("Trophy Of A Kill", qty=3),
    n("Mara Jade's Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift"),
]
DS_SHIELDS = [
    n("Weapon Of A Sith"),
    n("Battle Order"),
    n("Fanfare", True),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("There Is No Try"),
    n("A Useless Gesture"),
    n("You Cannot Hide Forever", True),
    n("Firepower"),
]
DS_ADD = []
