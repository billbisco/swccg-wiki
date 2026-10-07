#!/usr/bin/env python3
"""2013 World Championship Day 2: Cole Lepine Xerox WYS + Wookiee Slaving."""
from __future__ import annotations

PLAYER = "Cole Lepine"
USERNAME = "clepines"
LS_USERNAME = "clepines"
DS_USERNAME = "clepine"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 56
DS_PAGE = 57
LS_SCAN = "2013 Worlds Day 2 p56 Cole Lepine LS.png"
DS_SCAN = "2013 Worlds Day 2 p57 Cole Lepine DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Clepines. Username clepines. "
    "Email cole.lepine. Event Worlds '13, dated 08/10/13. Deck title WYSv. "
    "LIGHT and DARK boxes empty; dested Light. "
    "Do not rewrite the 2013 MPC Cole Lepine leftover. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough. "
    "Capn Han dested Captain Han Solo. SP STREET dested Spaceport Street. "
    "HFTMF dested Heading For The Medical Frigate. "
    "CEC dested Corellian Engineering Corporation. "
    "I & AH dested Insurrection & Aim High. "
    "R. Leadership dested Rebel Leadership. "
    "Anthman Combo dested Antilles Maneuver & Rebel Reinforcements. "
    "S. Bruckman dested Sergeant Bruckman. Seeking AA dested Seeking An Audience. "
    "Obi-Wan K. dested Obi-Wan Kenobi. Tantive IV struck; Spiral dested Spiral. "
    "Boshek dested BoShek. LSJK dested Luke Skywalker, Jedi Knight. "
    "G. Crix Madine dested General Crix Madine. "
    "Mace Windu, Moto dested Mace Windu, Master Of The Order. "
    "Dash R. dested Dash Rendar. Fallen Jedi dested Fallen Jedi. "
    "Lando's Yacht dested Lando's Luxury Yacht. "
    "Lando C, UH dested Lando Calrissian, Unlikely Hero. "
    "Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. "
    "NQA dested No Questions Asked. H2: DB dested Home One: Docking Bay. "
    "SP: DB dested Spaceport Docking Bay. SP: City dested Spaceport City. "
    "SP: Set dested Spaceport Scoundrels Guild. Y, GW dested Yoda, Great Warrior. "
    "LTWW dested Let The Wookiee Win. I. Atrocity dested Imperial Atrocity. "
    "L, RP dested Leia, Rebel Princess. HMB, HT dested Han's Toolkit. "
    "Han's HT Dark Approach struck omitted. "
    "Beghr Mel. Era Fallen dested BoShek's Modified Light Freighter. "
    "Relian N. dested Relian. Ant man dested Antilles Maneuver. "
    "ICBZ struck; Fall Back! dested Fall Back!. "
    "Flash of Insight struck; At E. Unleash dested The Force Unleashed. "
    "AFA dested Anger, Fear, Aggression. "
    "Shields Prof dested The Professor. Sentry dested Yavin Sentry. "
    "STAN dested Simple Tricks And Nonsense. DODN dested Do, Or Do Not. "
    "YISYW dested Your Insight Serves You Well. W. Display dested Weapons Display. "
    "OOTA dested Ounee Ta. Additional LKALOH dested Let's Keep A Little Optimism Here. "
    "J. Prize dested Jabba's Prize kept as extra Character. "
    "Form left column reprints 37-38 on lines 39-40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Clepines. Username clepine. "
    "Email cole.lepine. Event Worlds!, dated 08/10/13. Deck title Slavers. DARK. "
    "Do not rewrite the 2013 MPC Cole Lepine leftover. "
    "Wookiee Slaving op dested Wookiee Slaving Operation / Indentured To The Empire. "
    "K: Headquarters dested Kashyyyk: Slaving Camp Headquarters. "
    "Den o Thieves & Sp. D. dested Den Of Thieves & Special Delivery. "
    "Breached Hatch Occupiers & Mol dested Breached Defenses & Molator. "
    "J. Haven dested Jabba's Haven. "
    "M. Slavers Hut Bounty dested Mercenary Slavers and Hutt Bounty. "
    "Why Couldn't You Have Told Me dested Why Didn't You Tell Me?. "
    "ORS dested Outer Rim Scout. IG-88 w/ A. Gun dested IG-88 With Riot Gun. "
    "Q. Maul w/ Lightsaber dested Darth Maul With Lightsaber. "
    "B. Fett, Prep Hunter dested Boba Fett, Prepared Hunter. "
    "Leegesk dested Gela Yeens. M. Jade w/ Lightsaber dested Mara Jade With Lightsaber. "
    "P. Baba dested Ponda Baba. Hutt Bounty struck; Wait!? dested It Can Wait. "
    "TSCT dested They're Still Coming Through!. I. Barrier dested Imperial Barrier. "
    "SPF & WYB dested Short Range Fighters & Watch Your Back!. "
    "S. Bombardment dested Sonic Bombardment. Control struck; Sense dested Sense. "
    "Op as Planned dested Operational As Planned. A Dark Time struck; Alter dested Alter. "
    "Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Look Sir, Droids dested Look Sir, Droids. I. Justice dested Imperial Justice. "
    "BOControls dested Blast Door Controls. Slave 1, SoF dested Slave I, Symbol Of Fear. "
    "Velkin Tereri dested Velken Tezeri. "
    "Jango, FoF (The Mandlm) dested The Mandalorian. "
    "4-LOM w/ Gun dested 4-LOM With Concussion Rifle. "
    "K: Forest Maze dested Kashyyyk: Forest Maze. "
    "K: Skyhook Platform dested Kashyyyk: Skyhook Platform. "
    "K: Wookiee Slaving Camp struck; K: Security Tower dested Kashyyyk: Security Tower. "
    "K+D dested Knowledge And Defense. "
    "We'll Let Fate-a Decide Huh struck omitted. "
    "DSS Oppressive Enf dested Death Star Sentry and Oppressive Enforcement. "
    "AUG dested A Useless Gesture. YCHF dested You Cannot Hide Forever. "
    "IFYLOFD dested I Find Your Lack Of Faith Disturbing. "
    "CHYBC dested Come Here You Big Coward. BO dested Battle Order. "
    "TINT dested There Is No Try. S.Plans dested Secret Plans. "
    "DTHACC dested Do They Have A Code Clearance?. "
    "Additional Firepower / AoC / Abyss moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Millennium Falcon", True),
    n("Captain Han Solo"),
    n("Spaceport Street"),
    n("Heading For The Medical Frigate"),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("Wokling", True),
    n("Rebel Leadership", True),
    n("Houjix"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Sergeant Bruckman"),
    n("Seeking An Audience", True),
    n("Punch It!"),
    n("All Wings Report In & Darklighter Spin"),
    n("Obi-Wan Kenobi", True),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Spiral"),
    n("BoShek", True),
    n("Sense"),
    n("Luke Skywalker, Jedi Knight"),
    n("General Crix Madine"),
    n("Mace Windu, Master Of The Order"),
    n("Dash Rendar", True),
    n("Fallen Jedi", True),
    n("Lando's Luxury Yacht"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Palejo Reshad"),
    n("Corran Horn"),
    n("Escape Pod", True),
    n("Chewie", True),
    n("No Questions Asked", True),
    n("Menace Fades"),
    n("Home One: Docking Bay"),
    n("Spaceport Docking Bay"),
    n("Spaceport City"),
    n("Spaceport Scoundrels Guild"),
    n("Mirax Terrik"),
    n("Yoda, Great Warrior"),
    n("Let The Wookiee Win", True),
    n("Imperial Atrocity", True),
    n("Corellian Retort", True),
    n("Luke Skywalker, Jedi Knight"),
    n("No Questions Asked", True),
    n("Rebel Leadership", True),
    n("Rebel Barrier"),
    n("Let The Wookiee Win", True),
    n("Leia, Rebel Princess"),
    n("Han's Toolkit", True),
    n("BoShek's Modified Light Freighter", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Relian", True),
    n("Fallen Portal"),
    n("Antilles Maneuver", True),
    n("Rebel Barrier"),
    n("Fall Back!"),
    n("The Force Unleashed", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Aim High"),
    n("Simple Tricks And Nonsense", True),
    n("Affect Mind", True),
    n("Do, Or Do Not"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Ounee Ta", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
]
LS_ADD = [
    n("Jabba's Prize"),
]


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Wookiee Subjugation"),
    n("Den Of Thieves & Special Delivery"),
    n("Breached Defenses & Molator"),
    n("Jabba's Haven"),
    n("Mercenary Slavers"),
    n("Hutt Bounty", True),
    n("Why Didn't You Tell Me?", True),
    n("Nal Hutta"),
    n("Outer Rim Scout", qty=2),
    n("OOM-9", True),
    n("IG-88 With Riot Gun"),
    n("Darth Maul With Lightsaber"),
    n("Boba Fett, Prepared Hunter"),
    n("Gela Yeens", True),
    n("Mara Jade With Lightsaber"),
    n("Ephant Mon"),
    n("Ponda Baba", True),
    n("Maul's Sith Infiltrator"),
    n("Jabba's Space Cruiser", True),
    n("Disarmed"),
    n("Scum And Villainy"),
    n("It Can Wait"),
    n("They're Still Coming Through!"),
    n("Imperial Barrier"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sonic Bombardment", True, qty=2),
    n("Blow Parried"),
    n("Sense"),
    n("Operational As Planned", True),
    n("Lightsaber Deficiency", True),
    n("Alter", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sonic Bombardment", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Imperial Barrier"),
    n("Look Sir, Droids"),
    n("No Escape"),
    n("Imperial Justice", True),
    n("Blast Door Controls"),
    n("Disarmed"),
    n("Slave I, Symbol Of Fear"),
    n("Velken Tezeri", True),
    n("Jabba The Hutt", True),
    n("Bossk With Mortar Gun", True),
    n("Dengar With Blaster Carbine", True),
    n("Garindan", True),
    n("The Mandalorian", True),
    n("P-59"),
    n("4-LOM With Concussion Rifle"),
    n("Prince Xizor"),
    n("Outer Rim Scout", qty=2),
    n("Kashyyyk: Forest Maze"),
    n("Kashyyyk: Skyhook Platform"),
    n("Kashyyyk: Security Tower"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Resistance"),
    n("Death Star Sentry", True),
    n("Oppressive Enforcement"),
    n("After Her!", True),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Allegations Of Corruption", True),
    n("Abyss", True),
]
DS_ADD = []
