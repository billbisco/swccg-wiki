#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: WIRFS Xerox LS+DS."""
from __future__ import annotations

PLAYER = "WIRFS"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 116
DS_PAGE = 115
LS_SCAN = "2013 Match Play Championship p116 WIRFS LS.png"
DS_SCAN = "2013 Match Play Championship p115 WIRFS DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. WIRFS. Light. Deck title Training. "
    "MWYHL / Save it you can (V) dested Mind What You Have Learned / Save You It Can (V). "
    "Sorry About the mess combo dested Sorry About The Mess & Blaster Proficiency. "
    "Do or Do Not & Wise Advice dested Do, Or Do Not & Wise Advice. "
    "Battle Plan & DTF dested Battle Plan & Draw Their Fire. "
    "It is the Future you see (V) dested It Is The Future You See (Epic Event). "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. Qui Gon's Lightsaber dested Qui-Gon Jinn's Lightsaber. "
    "Master Qui-Gon (V). Wesa Gotta Grand Army as written. Clash of Sabers dested Clash Of Sabers. "
    "Mace Windu, Master of the Order dested Mace Windu, Master Of The Order. "
    "Obi-wan Kenobi, Jedi Knight dested Obi-Wan Kenobi, Jedi Knight (V). "
    "AJR dested A Jedi's Resilience. Noooooooo! dested NOOOOOOOOOOOO! (V). "
    "Luke Skywalker STTF dested Son Of Skywalker. Let the Wookiee Win dested Let The Wookiee Win (V). "
    "HC & F dested Han, Chewie, And The Falcon (V). OOC & TT dested Out Of Commission & Transmission Terminated. "
    "The Force is Strong in This One dested The Force Is Strong With This One. "
    "Houjix & Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Daughter of Skywalker dested Daughter Of Skywalker (V). "
    "Dagobah: Yoda's Hut as written. Seeking an Audience dested Seeking An Audience (V). "
    "Imperial Atrocity dested Imperial Atrocity (V). Sai Torr Kal Fas dested Sai'torr Kal Fas (V). "
    "The Way of Things dested The Way Of Things. Naboo Battle Plains dested Naboo: Battle Plains. "
    "Naboo: Boss Nass Chambers dested Naboo: Boss Nass' Chambers. "
    "Dagobah Jungle dested Dagobah: Jungle. Dagobah: Swamp as written. "
    "Artoo Detoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Knowledge crossed; Anger Fear Aggression dested Anger, Fear, Aggression (V). "
    "Chdsm dested Chasm (V). Simple Tricks & Nonsense dested Simple Tricks And Nonsense. "
    "Lets Keep A Little Optimism Here dested Let's Keep A Little Optimism Here (V). "
    "Your Ensight Serves You Well dested Your Insight Serves You Well (V). "
    "Crossed line then Aim High dested Aim High (V). Jabba's Prize as written. "
    "Jedi Tests in Additional: Great Warrior, A Jedi's Strength, Domain Of Evil, Size Matters Not, "
    "It Is The Future You See, You Must Confront Vader. "
    "Form left column lines 39–40 numbered as 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. WIRFS. Dark. Deck title Blow it up Go Boom. "
    "Set Your Course / The Ultimate Power dested Set Your Course For Alderaan / The Ultimate Power In The Universe. "
    "Death Star: Central Core as written. Prepared Defenses (V). CPI dested Commence Primary Ignition (V). "
    "U-3PO dested U-3PO (Yoo-Threepio). Intensify the Forward Batteries dested Intensify The Forward Batteries. "
    "Tarkin's Bounty (V). Cold Feet (V). Tarkin's Doctrine dested Tarkin Doctrine (V). "
    "MM & EO dested Masterful Move & Endor Occupation. Force Push (V). "
    "Darth Maul w/ Lightsaber dested Darth Maul With Lightsaber. Imperial Propaganda (V). "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "A Dark Time For The Rebellion (V). Control & Tunnel Vision dested Control & Set For Stun. "
    "Why Didn't You Tell Me? (V). He is not Ready & Imp Prop dested He Is Not Ready (V). "
    "Lightsaber Deficiency (V). Protocol Failure (V). Close Call (V). Force Field (V). "
    "Grievous dested Grievous, Hunter Of Jedi (V). 4-Lom w/ Gun dested 4-LOM With Concussion Rifle (V). "
    "Death Star: Docking Bay dested Death Star: Docking Bay 327. "
    "A Million Voices Crying Out as written. Kuat Drive Yards (V). "
    "Cesor Cannon Battery dested Laser Cannon Battery. Knowledge + Defence dested Knowledge And Defense (V). "
    "Allegations of Corruption dested Allegations Of Corruption. Abyss (V). "
    "You Cannot Hide Forever (V). Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "I Find Your Lack Of Faith Disturbing (V). A Useless Gesture (V). Firepower (V). "
    "There is no Try dested There Is No Try. Fanfare as written. Secret Plans as written. "
    "Form left column lines 39–40 numbered as 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Strong Is Vader"),
    n("Quick Draw", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Desperate Reach", True),
    n("Under Attack"),
    n("Jedi Levitation", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("It Is The Future You See", True),
    n("Dagobah"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Qui-Gon Jinn's Lightsaber", qty=2),
    n("Master Qui-Gon", True, qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Luke's Lightsaber"),
    n("Clash Of Sabers"),
    n("Mace Windu, Master Of The Order"),
    n("Obi-Wan Kenobi, Jedi Knight", True, qty=2),
    n("A Jedi's Resilience"),
    n("NOOOOOOOOOOOO!", True),
    n("Luke's Bionic Hand"),
    n("Corran Horn", True),
    n("Mace Windu", True),
    n("Son Of Skywalker", qty=2),
    n("Let The Wookiee Win", True),
    n("Blaster Deflection", qty=2),
    n("Han, Chewie, And The Falcon", True, qty=2),
    n("Disarmed"),
    n("Luke's Bionic Hand", True),
    n("Jedi Lightsaber", True),
    n("Lucky Shot", True),
    n("The Force Is Strong With This One"),
    n("Houjix & Out Of Nowhere"),
    n("Kiffex"),
    n("Out Of Commission & Transmission Terminated", qty=2),
    n("Yoda's Hope"),
    n("Daughter Of Skywalker", True),
    n("Reflection", True),
    n("Yoda", True),
    n("Son Of Skywalker", True),
    n("Dagobah: Yoda's Hut"),
    n("Seeking An Audience", True),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("The Way Of Things"),
    n("Naboo: Battle Plains"),
    n("Naboo: Boss Nass' Chambers"),
    n("Dagobah: Jungle"),
    n("Dagobah: Swamp"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon"),
    n("Chasm", True),
    n("Ultimatum"),
    n("A Tragedy Has Occurred"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Aim High", True),
    n("Jabba's Prize"),
]
LS_ADD = [
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
]

DS_START = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
DS_CARDS = [
    n("Set Your Course For Alderaan / The Ultimate Power In The Universe"),
    n("Death Star: War Room"),
    n("Death Star: Central Core"),
    n("Prepared Defenses", True),
    n("Commence Primary Ignition", True),
    n("Superlaser"),
    n("U-3PO (Yoo-Threepio)"),
    n("Intensify The Forward Batteries", qty=2),
    n("Corulag"),
    n("Kiffex"),
    n("Tarkin's Bounty", True),
    n("Cold Feet", True),
    n("Tarkin Doctrine", True),
    n("Rendili"),
    n("Masterful Move & Endor Occupation"),
    n("The Phantom Menace"),
    n("Force Push", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Imperial Propaganda", True),
    n("Arica"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("A Dark Time For The Rebellion", True),
    n("Control & Set For Stun"),
    n("Why Didn't You Tell Me?", True),
    n("He Is Not Ready", True),
    n("Lightsaber Deficiency", True),
    n("Protocol Failure", True),
    n("Operational As Planned"),
    n("Restraining Bolt"),
    n("Close Call", True),
    n("Force Field", True),
    n("Darth Sidious", qty=3),
    n("Grievous, Hunter Of Jedi", True),
    n("4-LOM With Concussion Rifle", True),
    n("Lateral Damage"),
    n("Overwhelmed"),
    n("Relentless Pursuit", qty=2),
    n("Flawless Marksmanship"),
    n("Avenger"),
    n("Judicator", qty=2),
    n("Thunderflare"),
    n("Victory"),
    n("Accuser"),
    n("Devastator", True),
    n("Stalker", True),
    n("Conquest", True),
    n("Death Star: Docking Bay 327"),
    n("Alderaan"),
    n("Death Star"),
    n("Imperial Stockpile"),
    n("A Million Voices Crying Out"),
    n("Kuat Drive Yards", True),
    n("Laser Cannon Battery"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Firepower", True),
    n("Resistance"),
    n("Battle Order"),
    n("There Is No Try"),
    n("Fanfare"),
    n("Secret Plans"),
]
DS_ADD = []
