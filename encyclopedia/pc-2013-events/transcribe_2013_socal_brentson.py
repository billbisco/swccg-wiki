#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Steve Brentson handwritten 2013 Print Form LS+DS.

Name field Brentson. Username blank. Dest Steve Brentson (file_player).
"""
from __future__ import annotations

PLAYER = "Steve Brentson"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 9
DS_PAGE = 10
LS_SCAN = "2013 SoCal Grand Prix Day 1 p09 Steve Brentson LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p10 Steve Brentson DS.png"
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests 1-6 checked, "
    "Hidden Fortress empty). Name Brentson dested Steve Brentson. "
    "Username blank. Deck Name MWYHL. Event Name So Co 2013. LIGHT. "
    "Do not dest as a new person. "
    "MWYHL dested Mind What You Have Learned / Save You It Can True. "
    "Story Is Vader dested Strong Is Vader. "
    "It Is The Future You See dested It Is The Future You See. "
    "Do or Do Not / Wise Advice dested Do, Or Do Not & Wise Advice. "
    "Battle Plan / DTF dested Battle Plan & Draw Their Fire. "
    "Saitorr Kal Fas dested Sai'torr Kal Fas. "
    "Dagobah dittos dested Dagobah: Yoda's Hut, Dagobah: Training Area, "
    "Dagobah: Swamp (Swamp Shelter). "
    "Star Imposter crossed, Jedi Presence dested Jedi Presence. "
    "Hear Me Baby, Hold Together dested Hear Me Baby, Hold Together. "
    "Republic Gunship dested Republic Cruiser (Aasen analog). "
    "LTWW dested Let The Wookiee Win. "
    "Luke SITF dested Luke Skywalker, Strong In The Force. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Mace Windu dittos dested Mace Windu; Master of The Order dested "
    "Mace Windu, Master Of The Order. "
    "Luke Skywalker JK crossed, Anch. Fail dested Anchoring Failure as written. "
    "HCF dested Han, Chewie, And The Falcon. "
    "AFA dested Anger, Fear, Aggression. "
    "Shield 1 Planetary Defense dested Planetary Defenses. "
    "The High dested The High Ground as written. "
    "Don't Do That Again crossed on shield 15, and Jedi Council dested "
    "Speak With The Jedi Council. "
    "Jedi Tests 1-6 dested the six Jedi Tests. "
    "Unique overcounts sheet-accurate: Let The Wookiee Win x4, "
    "Luke Skywalker, Strong In The Force x3, Escape Pod x3, "
    "Mace Windu x2, Rebel Leadership x2, Aim High shields x2, "
    "Anchoring Failure x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name Brentson dested Steve Brentson. "
    "Username blank. Deck Name Slaves. Event Name SoCal 2013. "
    "LIGHT/DARK boxes empty; dest Dark from Wookiee Slaving Operation. "
    "Do not dest as a new person. "
    "Wookiee Slaving Operation dested Wookiee Slaving Operation / "
    "Indentured To The Empire True. "
    "Den of Thieves / Spec Del dested Den Of Thieves & Special Delivery. "
    "Breached Def / Molator dested Breached Defenses & Molator. "
    "Kashyyyk dittos dested Kashyyyk: Slaving Camp Headquarters, "
    "Kashyyyk: Wookiee Slaving Camp, Kashyyyk: Skyhook Platform. "
    "Jabba's Sail Barge PD dested Jabba's Sail Barge: Passenger Deck. "
    "ORS dested Outer Rim Scout. "
    "Lightsaber Def dested Lightsaber Deficiency (Aasen analog). "
    "Walker Tezzin dested Velken Tezeri. "
    "Probot dested Probot as written. "
    "Zuckuss in MH dested Zuckuss In Mist Hunter. "
    "Reegat dested Reegesk. "
    "Greedle The Hutt dested Gardulla The Hutt. "
    "Bossk With Mortar Gn dested Bossk With Mortar Gun. "
    "Slave I Symbol dested Slave I, Symbol Of Fear. "
    "Dengar I Kaila dested Dengar In Punishing One. "
    "Ghhhk / Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Ket Maliss / Shadow Killer dested Ket Maliss, Shadow Killer. "
    "Dengar w/ shot dested Dengar With Blaster Carbine. "
    "Wookiee Subjugation dested Wookiee Subjugation. "
    "Dr E dested Dr. Evazan. "
    "Boba Fett PH dested Boba Fett, Prepared Hunter. "
    "Jango Fett The Ass dested Jango Fett, The Assassin. "
    "LSD dested Lateral Damage. "
    "KAD dested Knowledge And Defense. "
    "Will Let Fate Death dested We'll Let Fate-a Decide, Huh?. "
    "Weapon of a Sith dested Weapon Of A Sith. "
    "Unique overcounts sheet-accurate: Outer Rim Scout x5, "
    "Imperial Barrier x3, Sonic Bombardment x3, Ponda Baba x2, "
    "Firepower shields x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("Strong Is Vader", True),
    n("It Is The Future You See", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Quick Draw", True),
    n("Projection Of A Skywalker"),
    n("Sai'torr Kal Fas", True),
    n("The Way Of Things"),
    n("Dagobah"),
    n("Dagobah: Yoda's Hut"),
    n("Dagobah: Training Area"),
    n("Dagobah: Swamp"),
    n("Jedi Presence", True),
    n("Hear Me Baby, Hold Together", True),
    n("Weapon Levitation"),
    n("Republic Cruiser", True),
    n("Naboo: Battle Plains"),
    n("Houjix"),
    n("Grimtaash"),
    n("Jedi Lightsaber", True),
    n("Obi-Wan Kenobi, Jedi Knight"),
    n("Clash Of Sabers", qty=2),
    n("Wesa Gotta Grand Army", qty=2),
    n("Let The Wookiee Win", True, qty=4),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Lady Luck", True),
    n("Escape Pod", True, qty=3),
    n("Corran Horn"),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order", True),
    n("A Jedi's Resilience", qty=2),
    n("Rebel Leadership", True, qty=2),
    n("Luke's Lightsaber"),
    n("Luke Skywalker, Jedi Knight"),
    n("Anchoring Failure", qty=2),
    n("Luke's Backpack"),
    n("Yoda", True),
    n("Reflection", True),
    n("Daughter Of Skywalker", True),
    n("Han, Chewie, And The Falcon", True),
    n("Qui-Gon's Lightsaber"),
    n("Republic Gunship Wing"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Planetary Defenses", True),
    n("He Can Go About His Business", True),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("Aim High", True),
    n("Ultimatum", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense", True),
    n("The Professor", True),
    n("Aim High", True),
    n("The High Ground", True),
    n("A Tragedy Has Occurred"),
    n("Speak With The Jedi Council"),
]
LS_ADD = [
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("It Is The Future You See"),
    n("A Jedi's Focus"),
    n("A Jedi's Resilience"),
]


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire", True),
    n("Mercenary Slavers", True),
    n("Power Of The Hutt"),
    n("Jabba's Haven", True),
    n("Den Of Thieves & Special Delivery", True),
    n("Breached Defenses & Molator", True),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters", True),
    n("Kashyyyk: Wookiee Slaving Camp", True),
    n("Kashyyyk: Skyhook Platform", True),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Nal Hutta"),
    n("Ponda Baba", True, qty=2),
    n("Imperial Barrier", qty=3),
    n("Outer Rim Scout", qty=5),
    n("Lightsaber Deficiency", True),
    n("Lightsaber Deficiency", qty=2),
    n("Sonic Bombardment", True, qty=3),
    n("Cold Feet", True),
    n("Jabba's Space Cruiser", True),
    n("Velken Tezeri"),
    n("Probot", True),
    n("Zuckuss In Mist Hunter"),
    n("Reegesk", True),
    n("Mercenary Pilot", True),
    n("Abyssin Ornament"),
    n("Hutt Bounty", True),
    n("Jabba The Hutt", True),
    n("4-LOM With Concussion Rifle"),
    n("Gardulla The Hutt", True),
    n("Bossk With Mortar Gun", True),
    n("Scum And Villainy"),
    n("Slave I, Symbol Of Fear", True),
    n("Dengar In Punishing One", True),
    n("Garindan", True),
    n("Ephant Mon"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Ket Maliss, Shadow Killer", True),
    n("Dengar With Blaster Carbine", True),
    n("P-59"),
    n("Lady Valarian", True),
    n("Wookiee Subjugation", True),
    n("Dr. Evazan"),
    n("IG-88 With Riot Gun"),
    n("Boba Fett, Prepared Hunter", True),
    n("Prince Xizor"),
    n("Jango Fett, The Assassin", True),
    n("Jabba's Sail Barge"),
    n("Lateral Damage"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Imperial Detention", True),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Firepower", True),
    n("Abyss", True),
    n("Secret Plans", True),
    n("Firepower", True),
    n("Weapon Of A Sith"),
]
DS_ADD = []
