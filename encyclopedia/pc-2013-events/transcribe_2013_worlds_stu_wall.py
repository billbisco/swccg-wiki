#!/usr/bin/env python3
"""2013 World Championship Day 2: Stu Wall Xerox WYS + Wookiee Slaving."""
from __future__ import annotations

PLAYER = "Stu Wall"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 105
DS_PAGE = 106
LS_SCAN = "2013 Worlds Day 2 p105 Stu Wall LS.png"
DS_SCAN = "2013 Worlds Day 2 p106 Stu Wall DS.png"
PUBLIC_NOTE = "Name as written on the Day 2 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Stu Wall. Username blank. Email blank. LIGHT. "
    "Deck title Watch Out. Event Worlds, dated 08/10/13. "
    "Dest as Stu Wall as written. Do not dest as Steve Wall. "
    "WYS v dested Watch Your Step / This Place Can Be A Little Rough. "
    "Wokling dested Wokling. "
    "Insurrection + Aim High dested Insurrection & Aim High. "
    "Corellian Engineering dested Corellian Engineering Corporation. "
    "No Questions Asked dested No Questions Asked. "
    "Punch It dested Punch It!. "
    "AFA dested Anger, Fear, Aggression. "
    "AWR + DS dested All Wings Report In & Darklighter Spin. "
    "Houjix + OON dested Houjix & Out Of Nowhere. "
    "Padme N. dested Padme Naberrie. "
    "Antilles Maneuver + RR dested Antilles Maneuver & Rebel Reinforcements. "
    "C. Bruckman dested Sergeant Bruckman. "
    "Boshek's Ship dested BoShek's Modified Light Freighter. "
    "Spaceport SG dested Spaceport Speeders. "
    "Wedge A RSL dested Wedge Antilles, Red Squadron Leader. "
    "Leia RP dested Leia, Rebel Princess. "
    "Mace W MOTO dested Mace Windu, Master Of The Order. "
    "Yoda, GW dested Yoda, Great Warrior. "
    "Palejo Reshad dested Palejo Reshad. "
    "General Bob Hudson dested as written. "
    "Imperial Arrest dested Imperial Atrocity. "
    "LS, SK dested Luke Skywalker, Jedi Knight. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Corellian Retro dested Corellian Retort. "
    "AtD + RDH dested Artoo-Detoo In Red 5. "
    "Dash R dested Dash Rendar. "
    "General Crix M. dested General Crix Madine. "
    "LTWW dested Let The Wookiee Win. "
    "Rebel Leader dested Rebel Leadership. "
    "M. Falcon dested Millennium Falcon. "
    "CC UH dested Cloud City: Upper Plaza Corridor. "
    "Lando's Ship dested Lady Luck. "
    "Jabba Baze dested Jabba's Prize. "
    "HCGAHB dested He Can Go About His Business. "
    "YISYW dested Your Insight Serves You Well. "
    "You've Dest dested You've Got A Lot Of Guts Coming Here. "
    "Form left column reprints 37-38 on lines 39-40 are Imperial Atrocity and "
    "Luke Skywalker, Jedi Knight. "
    "Additional Chasm / A Close Call / You've Got A Lot Of Guts Coming Here "
    "moved to Light shields or extra. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Stu Wall. Username blank. Email blank. DARK. "
    "Deck title Slavers. Event Worlds. "
    "Dest as Stu Wall as written. Do not dest as Steve Wall. "
    "Wookiee Slaving Op dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Kashyyyk HQ dested Kashyyyk: Slaving Camp Headquarters. "
    "Kashyyyk Skyhook dested Kashyyyk: Skyhook Platform. "
    "Slave Camp dested Kashyyyk: Wookiee Slaving Camp. "
    "Jabba's Space Shir dested Jabba's Space Cruiser. "
    "DoT + SD dested Den Of Thieves & Special Delivery. "
    "BD + M dested Breached Defenses & Molator. "
    "Jabba's Sail Deck dested Jabba's Sail Barge: Passenger Deck. "
    "TM, FoF dested Jango Fett, The Assassin. "
    "Kel Malice dested Ket Maliss, Shadow Killer. "
    "Reesesk dested Reegesk. "
    "Ability 3x dested Ability, Ability, Ability. "
    "Scum dested Scum And Villainy. "
    "Lady V dested Lady Valarian. "
    "Bossk w/ Gun dested Bossk With Mortar Gun. "
    "Garrison dested Garindan. "
    "BF, PH dested Boba Fett, Prepared Hunter. "
    "Slave I SoF dested Slave I, Symbol Of Fear. "
    "4-LOM w/ Gun dested 4-LOM With Concussion Rifle. "
    "M Pilot dested Mercenary Pilot. "
    "Lightsaber D dested Lightsaber Deficiency. "
    "Elephant Men dested Ephant Mon. "
    "Zuckuss + Ship dested Zuckuss In Mist Hunter. "
    "Ghhhk + TRWEU dested Ghhhk & Those Rebels Won't Escape Us. "
    "R + D dested Knowledge And Defense. "
    "TINT dested There Is No Try. "
    "CHYBC dested Come Here You Big Coward. "
    "Allegiance dested Allegations Of Corruption. "
    "AUG dested A Useless Gesture. "
    "I FYLOFD dested I Find Your Lack Of Faith Disturbing. "
    "DSS dested Death Star Sentry. "
    "Form left column reprints 37-38 on lines 39-40 are Sonic Bombardment dittos. "
    "Additional Abyss / Death Star Sentry / LTTM moved to Dark shields. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Spaceport Street"),
    n("Home One: Docking Bay"),
    n("Wokling", True),
    n("Insurrection & Aim High"),
    n("Corellian Engineering Corporation", True),
    n("No Questions Asked", True, qty=2),
    n("Punch It!"),
    n("Rebel Barrier", qty=2),
    n("Anger, Fear, Aggression", True),
    n("All Wings Report In & Darklighter Spin", True),
    n("Corellian Slip", True),
    n("Houjix & Out Of Nowhere"),
    n("Padme Naberrie", True),
    n("Antilles Maneuver & Rebel Reinforcements", True, qty=3),
    n("Sergeant Bruckman"),
    n("BoShek's Modified Light Freighter", True),
    n("Grimtaash", qty=2),
    n("Spaceport Speeders"),
    n("Corran Horn"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Leia, Rebel Princess"),
    n("BoShek", True),
    n("Mace Windu, Master Of The Order"),
    n("Elegant Lightsaber", qty=2),
    n("Yoda, Great Warrior"),
    n("Corellia", True),
    n("Spaceport City"),
    n("Spaceport Docking Bay"),
    n("Palejo Reshad"),
    n("General Bob Hudson"),
    n("Escape Pod", True),
    n("Imperial Atrocity", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("Heading For The Medical Frigate"),
    n("Maris Brood, Fallen Jedi"),
    n("Mirax Terrik"),
    n("Corellian Retort", True),
    n("Artoo-Detoo In Red 5"),
    n("Luke's Bionic Hand", True),
    n("Under Attack"),
    n("Corellian Slip", True),
    n("Dash Rendar", True),
    n("General Crix Madine"),
    n("Let The Wookiee Win", True),
    n("Booster Terrik"),
    n("Rebel Leadership", True),
    n("General Solo", True),
    n("Chewie", True),
    n("Millennium Falcon", True),
    n("Cloud City: Upper Plaza Corridor"),
    n("Lady Luck"),
]
LS_SHIELDS = [
    n("Weapons Display"),
    n("Battle Plan"),
    n("Ounee Ta"),
    n("Your Insight Serves You Well", qty=2),
    n("OICTW"),
    n("Another Pathetic Lifeform"),
    n("He Can Go About His Business"),
    n("Wise Advice"),
    n("Aim High"),
    n("Do, Or Do Not"),
    n("Chasm"),
]
LS_ADD = [
    n("Jabba's Prize"),
    n("A Close Call"),
    n("You've Got A Lot Of Guts Coming Here"),
]

DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Kashyyyk: Skyhook Platform"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Kashyyyk"),
    n("Jabba's Space Cruiser"),
    n("Den Of Thieves & Special Delivery"),
    n("Mercenary Slavers"),
    n("Power Of The Hutt"),
    n("Jabba's Haven"),
    n("Breached Defenses & Molator"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Probot"),
    n("Wookiee Subjugation"),
    n("Jango Fett, The Assassin"),
    n("Ket Maliss, Shadow Killer", True),
    n("Reegesk", True),
    n("Turbulence"),
    n("Ability, Ability, Ability"),
    n("Limited Resources"),
    n("Scum And Villainy"),
    n("Nal Hutta"),
    n("Lady Valarian"),
    n("Bossk With Mortar Gun", qty=2),
    n("Dr. Evazan"),
    n("Ponda Baba", True),
    n("Garindan", True),
    n("Hutt Bounty", True),
    n("Jabba's Sail Barge"),
    n("Boba Fett, Prepared Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("4-LOM With Concussion Rifle"),
    n("Mercenary Pilot", True),
    n("Abyssin Ornament", True, qty=2),
    n("Sonic Bombardment", True, qty=4),
    n("Lightsaber Deficiency", True, qty=3),
    n("Imperial Barrier"),
    n("Imperial Barrier", True, qty=2),
    n("Jabba The Hutt", True),
    n("Ephant Mon"),
    n("Zuckuss In Mist Hunter"),
    n("Outer Rim Scout", qty=5),
    n("Velken Tezeri", True),
    n("Prince Xizor"),
    n("Dengar With Blaster Carbine"),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("A Useless Gesture"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("After Her"),
    n("Imperial Detention"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("You Cannot Hide Forever"),
    n("You Want This Don't You"),
    n("Abyss"),
    n("Death Star Sentry"),
]
DS_ADD = [
    n("Leave Them To Me"),
]
