#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Chris Westergard Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Chris Westergard"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 105
DS_PAGE = 106
LS_SCAN = "2013 Match Play Championship p105 Chris Westergard LS.png"
DS_SCAN = "2013 Match Play Championship p106 Chris Westergard DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Chris Westergard. Light. Starting Watch Your Step. "
    "Watch Your Step dested Watch Your Step / This Place Can Be A Little Rough. "
    "Tatooine: Dock Bay 94 dested Tatooine: Docking Bay 94. "
    "Tatooine: with the rest of the line blank dested Tatooine. "
    "Insurrection / Aim High dested Insurrection & Aim High. "
    "Tatooine: Mos Espa D.B. dested Tatooine: Mos Espa Docking Bay. "
    "BoShek Brash Smuggler dested BoShek, Brash Smuggler. "
    "Han Solo, Courageous Smuggler as written. "
    "Sergeant Doallyn dested Sergeant Doallyn. "
    "BoShek's Modified Light Freighter dested YT-1300 Transport. "
    "Pulsar Skate as written. All Wings / DS dested All Wings Report In & Darklighter Spin. "
    "Control & T.V. dested Control & Tunnel Vision. It's A Hit dested It's A Hit!. "
    "Moving to Attack Position dested Moving To Attack Position. "
    "Nar Shaddaa Wind Chimes / Out of Somewhere dested Nar Shaddaa Wind Chimes & Out Of Somewhere. "
    "Strike Force dested Strikeforce. Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Heading For the Medical Frigate dested Heading For The Medical Frigate. "
    "Only Jedi Carry This Weapon dested Only Jedi Carry That Weapon. "
    "Let's Keep a Little Optimism dested Let's Keep A Little Optimism Here. "
    "Simple Tricks & Nonsense dested Simple Tricks And Nonsense. "
    "A Tragedy Has Occurred as written. "
    "Form left column reprints 37–38 on lines 39–40 are filled as Patrol Craft / A Few Maneuvers / All Wings. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Chris Westergard. Dark. Starting Wookiee Slaving. "
    "Wookiee Slaving dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Kashyyyk ditto Slaving Camp dested Kashyyyk: Wookiee Slaving Camp. "
    "Den of Thieves dested Den Of Thieves. Jabba's Palace dested Tatooine: Jabba's Palace. "
    "Jabba's Sail Barge Pass Deck dested Jabba's Sail Barge: Passenger Deck. "
    "Kashyyyk Slaving Camp dested Kashyyyk: Slaving Camp Headquarters. "
    "4-Lom w Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "Boba Fett Prepared Hunter dested Boba Fett, Prepared Hunter. "
    "Bossk w/ Mortar Gun dested Bossk With Mortar Gun. Dr. E dested Dr. Evazan. "
    "FG-88, Renegade Droid dested IG-88, Renegade Droid. "
    "Mara Jade w/ Lightsaber dested Mara Jade With Lightsaber. "
    "The Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "U-3PO dested U-3PO (Yoo-Threepio). Dengar in PO dested Dengar In Punishing One. "
    "Ellis is Hunter dested Mist Hunter. Slave I Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Zuckuss in MH dested Zuckuss In Mist Hunter. Scum & Villainy dested Scum And Villainy. "
    "Nothing Can Get Through Our Shield as written. "
    "Ghhhk & Those Rebels Won't Escape Us as written. "
    "Cease Fire dested Cease Fire!. Knowledge & Defense dested Knowledge And Defense. "
    "Party crossed; Allegations dested Allegations Of Corruption. "
    "Come Here You Big Coward as written. Oppressive Enf. dested Oppressive Enforcement. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine"),
    n("Insurrection & Aim High"),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("Corellia"),
    n("Kessel"),
    n("Tatooine: Mos Espa Docking Bay"),
    n("Spaceport Docking Bay"),
    n("BoShek, Brash Smuggler", True),
    n("Dash Rendar"),
    n("Han Solo, Courageous Smuggler", True),
    n("Luke Skywalker", True),
    n("Melas", True),
    n("Melas"),
    n("Mirax Terrik"),
    n("Palace Raider", qty=6),
    n("Phylo Gandish"),
    n("Sergeant Doallyn", True),
    n("Talon Karrde"),
    n("Wedge Antilles", True),
    n("YT-1300 Transport", True),
    n("Artoo-Detoo In Red 5"),
    n("Millennium Falcon"),
    n("Outrider"),
    n("Pulsar Skate"),
    n("Patrol Craft", qty=5),
    n("A Few Maneuvers"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("Fallen Portal", qty=2),
    n("It Could Be Worse"),
    n("It's A Hit!"),
    n("Moving To Attack Position"),
    n("Nar Shaddaa Wind Chimes & Out Of Somewhere"),
    n("Rebel Barrier"),
    n("Menace Fades"),
    n("Strikeforce", True),
    n("Scrambled Transmission", True),
    n("Tatooine Celebration", qty=2),
    n("I'll Take The Leader", qty=2),
    n("X-wing Laser Cannon"),
    n("Anger, Fear, Aggression"),
    n("Heading For The Medical Frigate"),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Your Insight Serves You Well"),
    n("Yavin Sentry"),
    n("Let's Keep A Little Optimism Here"),
    n("Wise Advice"),
    n("Don't Do That Again"),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("The Professor"),
]
LS_ADD = []

DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Den Of Thieves"),
    n("Mercenary Slavers"),
    n("Tatooine: Jabba's Palace"),
    n("Power Of The Hutt"),
    n("Nal Hutta"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Kashyyyk: Skyhook Platform"),
    n("4-LOM With Concussion Rifle"),
    n("Boba Fett, Prepared Hunter"),
    n("Bossk With Mortar Gun"),
    n("Bib Fortuna"),
    n("Dr. Evazan"),
    n("Ephant Mon"),
    n("Gela Yeens"),
    n("Guri"),
    n("Garindan"),
    n("IG-88, Renegade Droid"),
    n("Jabba The Hutt"),
    n("Mara Jade With Lightsaber"),
    n("Mercenary Pilot", qty=2),
    n("Outer Rim Scout"),
    n("Prince Xizor"),
    n("Jango Fett, The Assassin"),
    n("U-3PO (Yoo-Threepio)"),
    n("Vigo", qty=2),
    n("Velken Tezeri"),
    n("Dengar In Punishing One"),
    n("Mist Hunter"),
    n("Jabba's Space Cruiser"),
    n("Jabba's Sail Barge"),
    n("Slave I, Symbol Of Fear"),
    n("Stinger"),
    n("Racing Skiff", qty=2),
    n("Zuckuss In Mist Hunter"),
    n("Disarmed"),
    n("Hutt Bounty"),
    n("Ket Maliss"),
    n("Molator"),
    n("Protocol Failure"),
    n("Scum And Villainy", qty=2),
    n("Nothing Can Get Through Our Shield"),
    n("Abyssin Ornament"),
    n("Cease Fire!"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lightsaber Deficiency"),
    n("Operational As Planned"),
    n("Sonic Bombardment", qty=3),
    n("Those Rebels Won't Escape Us"),
    n("Wookiee Subjugation"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("A Useless Gesture"),
    n("There Is No Try"),
    n("Oppressive Enforcement"),
    n("Fanfare"),
    n("Firepower"),
    n("Do They Have A Code Clearance?"),
    n("You Cannot Hide Forever"),
    n("Resistance"),
    n("Battle Order"),
    n("Secret Plans"),
]
DS_ADD = []
