#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Andrew Bollentino Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Andrew Bollentino"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 14
DS_PAGE = 13
LS_SCAN = "2013 Match Play Championship p14 Andrew Bollentino LS.png"
DS_SCAN = "2013 Match Play Championship p13 Andrew Bollentino DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Deck title I Suck At This Game. Light. "
    "Plead My Case → Plead My Case To The Senate. JCC → Coruscant: Jedi Council Chamber. "
    "HFTMF → Heading For The Medical Frigate. AFA → Anger, Fear, Aggression. "
    "YSLVG dested Yoda, Senior Council Member. Saitorr → Sai'torr Kal Fas. "
    "So This Is How LD → So This Is How Liberty Dies. TW+PS dested Thrown Back. "
    "Senator Padme Amidala as written. Bail Organa / FoR → Bail Organa, Father Of Rebellion. "
    "Qui-Gon Jinn Master → Qui-Gon Jinn, Jedi Master. Coruscant (Ep1) dested Coruscant. "
    "Wedge in RS1 → Wedge In Red Squadron 1. SATM/BP → Sorry About The Mess & Blaster Proficiency. "
    "ASR dested All Wings Report In. HL dested Houjix. Might of the Rep → Might Of The Republic. "
    "Yoda MOTF → Yoda, Master Of The Force. Control/TV → Control & Tunnel Vision. "
    "Alderaan Cons. Ship dested Radiant VII. AJR → A Jedi's Resilience. "
    "Sense/Recoil → Sense & Recoil In Fear. HC+F → Han, Chewie, And The Falcon. "
    "LS JK / LS RS → Luke Skywalker, Jedi Knight / Rebel Scout. LTWW → Let The Wookiee Win. "
    "Take Them With Us dested Taking Them With Us. "
    "DDTA → Don't Do That Again. BP → Battle Plan. LKSALOH → Let's Keep A Little Optimism Here. "
    "OJCTW dested Wise Advice. Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Deck title I Suck. Event MPC 13. Dark. "
    "Contract Killers / FITG → Contract Killers / Feared Throughout The Galaxy. "
    "Prep Def → Prepared Defenses. Cor. Sub City Lair dested Coruscant: Private Platform (Docking Bay). "
    "Coruscant (SE) dested Coruscant. K+D → Knowledge And Defense. "
    "It's a Millenium Shadow dested Shadows Of The Empire. Death Mark + HD → Death Mark & Hutt Bounty. "
    "Coruscant Office dested Coruscant: Palpatine's Quarters. Coruscant Casino as written. "
    "Maul's DB LS → Maul's Double-Bladed Lightsaber. Bori → Danz Borin. "
    "Darth Maul YA → Darth Maul, Young Apprentice. CC Security Tower → Cloud City: Security Tower. "
    "Galen, SA → Galen Marek, Starkiller. Mara LS dested Mara Jade With Lightsaber. "
    "ZIMH → Zuckuss In Mist Hunter. Boba Fett PH → Boba Fett, Prepared Hunter. "
    "Slave I, SoF → Slave I, Symbol Of Fear. Abyssin Orn → Abyssin Ornament. "
    "Bard Malor → Bane Malar. U390 → U-3PO (Yoo-Threepio). Sonic Bomb → Sonic Bombardment. "
    "Danni Team → Dannik Jerriko. Area → Arica. Imp Prop → Imperial Propaganda. "
    "DJ LS → Dark Jedi Lightsaber. Tiny Bounty dested Bounty. Aurra's BR → Aurra Sing's Blaster Rifle. "
    "Mando, FoF → Jango Fett, The Assassin. OINPO → Oh, Switch Off. Sniper/DS → Sniper & Dark Strike. "
    "Galen's LS, VG → Galen's Lightsaber, Vader's Gift. Imp Bounty dested Tarkin's Bounty. "
    "Aurra Sing, DA / Aurra Deadly Ass → Aurra Sing, Deadly Assassin. "
    "Jabba, Killer dested Jabba Desilijic Tiure. YCHF → You Cannot Hide Forever. "
    "Imp Def → Imperial Decree. DTHACC → Do They Have A Code Clearance?. "
    "WTOAOT → Wipe Them Out, All Of Them. Alleg of Corrupt → Allegations Of Corruption. "
    "Coward → Come Here You Big Coward. Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Jedi Council Chamber"),
    n("Coruscant: Galactic Senate"),
    n("Heading For The Medical Frigate", True),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Strike Planning"),
    n("Anger, Fear, Aggression", True),
    n("Corran Horn"),
    n("Yoda, Senior Council Member", True),
    n("Sai'torr Kal Fas", True),
    n("Coruscant: Galactic Senate"),
    n("So This Is How Liberty Dies", True),
    n("Coruscant: Night Club", True),
    n("Imperial Atrocity", True),
    n("Thrown Back"),
    n("Jedi Lightsaber", True),
    n("Mace Windu", True),
    n("Senator Leia Organa"),
    n("Senator Padme Amidala", True),
    n("Bail Organa", True),
    n("Supreme Chancellor Valorum", True),
    n("Qui-Gon Jinn, Jedi Master", True),
    n("Coruscant"),
    n("Jedi Presence"),
    n("Lightsaber Proficiency"),
    n("Weapon Levitation"),
    n("Blaster Deflection"),
    n("Escape Pod", True),
    n("Wedge In Red Squadron 1", True),
    n("Spiral"),
    n("Obi-Wan With Lightsaber", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("All Wings Report In"),
    n("Imperial Atrocity", True),
    n("Houjix"),
    n("Might Of The Republic"),
    n("Yoda, Master Of The Force"),
    n("Menace Fades"),
    n("Mas Amedda"),
    n("Control & Tunnel Vision"),
    n("Radiant VII"),
    n("Luke Skywalker, Jedi Knight"),
    n("A Jedi's Resilience"),
    n("Jedi Levitation"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sense & Recoil In Fear"),
    n("Obi-Wan Kenobi", True),
    n("Blaster Deflection"),
    n("Mace Windu", True),
    n("Han, Chewie, And The Falcon", True),
    n("It's A Trap!"),
    n("Luke's Lightsaber"),
    n("Let The Wookiee Win", True),
    n("Bail Organa, Father Of Rebellion", True),
    n("Taking Them With Us"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Bail Organa, Father Of Rebellion", True),
    n("Might Of The Republic"),
    n("Jedi Lightsaber", True),
]
LS_SHIELDS = [
    n("Don't Do That Again"),
    n("Battle Plan"),
    n("Wise Advice"),
    n("Your Insight Serves You Well"),
    n("Weapons Display"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here"),
    n("Another Pathetic Lifeform"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("The Professor"),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = []

DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy", True),
    n("Prepared Defenses", True),
    n("Coruscant: Private Platform (Docking Bay)", True),
    n("Coruscant"),
    n("On The Hunt", True),
    n("Gift Of The Master", True),
    n("Jabba's Haven", True),
    n("I've Lost Artoo!", True),
    n("Knowledge And Defense", True),
    n("Shadows Of The Empire", True),
    n("Blaster Rack"),
    n("Death Mark & Hutt Bounty", True),
    n("Coruscant: Palpatine's Quarters", True),
    n("Coruscant: Casino", True),
    n("Maul's Double-Bladed Lightsaber"),
    n("Danz Borin", True),
    n("Darth Maul, Young Apprentice"),
    n("Cloud City: Security Tower", True),
    n("Nal Hutta"),
    n("Galen Marek, Starkiller", True),
    n("Trophy Of A Kill", True),
    n("Aurra Sing", True),
    n("Mara Jade With Lightsaber", True),
    n("Trophy Of A Kill", True),
    n("Force Push", True),
    n("Zuckuss In Mist Hunter"),
    n("Boba Fett, Prepared Hunter", True),
    n("Slave I, Symbol Of Fear", True),
    n("Abyssin Ornament"),
    n("Bane Malar", True),
    n("Force Field", True),
    n("Disarmed"),
    n("U-3PO (Yoo-Threepio)"),
    n("Sonic Bombardment", True),
    n("Dannik Jerriko"),
    n("Arica", True),
    n("Sonic Bombardment", True),
    n("Force Field", True),
    n("Imperial Propaganda", True),
    n("Dark Jedi Lightsaber", True),
    n("Bounty"),
    n("Aurra Sing's Blaster Rifle"),
    n("Jango Fett, The Assassin", True),
    n("Oh, Switch Off"),
    n("Abyssin Ornament", True),
    n("Sniper & Dark Strike"),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Weapon Levitation"),
    n("IG-88", True),
    n("Tarkin's Bounty"),
    n("Sniper & Dark Strike"),
    n("Sonic Bombardment", True),
    n("Disarmed"),
    n("Aurra Sing, Deadly Assassin", True),
    n("Darth Maul, Young Apprentice"),
    n("Elis Helrot"),
    n("Galen Marek, Starkiller", True),
    n("Abyssin Ornament", True),
    n("Aurra Sing, Deadly Assassin", True),
    n("Jabba Desilijic Tiure", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever"),
    n("Imperial Decree"),
    n("Do They Have A Code Clearance?"),
    n("Wipe Them Out, All Of Them"),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("Weapon Of A Sith"),
    n("Battle Order"),
    n("Abyss"),
    n("Firepower"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
]
DS_ADD = []
