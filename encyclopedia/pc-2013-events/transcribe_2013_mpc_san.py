#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: SAN Xerox LS+DS."""
from __future__ import annotations

PLAYER = "SAN"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 107
DS_PAGE = 108
LS_SCAN = "2013 Match Play Championship p107 SAN LS.png"
DS_SCAN = "2013 Match Play Championship p108 SAN DS.png"
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. SAN. Light. Deck title DANGER ZONE!. "
    "WYS dested Watch Your Step / This Place Can Be A Little Rough (Decipher; (V) unchecked). "
    "Tatooine (EPI) dested Tatooine. Cantina (DANGER ZONE!) dested Tatooine: Cantina (V). "
    "DB 94 dested Tatooine: Docking Bay 94. Wokling dested Wokling. "
    "Squassin dested Squadron Assignments. QD dested Quick Draw. "
    "HFTMF dested Heading For The Medical Frigate. Corellia dested Corellia. "
    "Mos Eisley dested Tatooine: Mos Eisley. Bacta Tank as written. "
    "Strike Force dested Strikeforce. Menace Fades as written. "
    "Sai'torr KF dested Sai'torr Kal Fas. A Good Blaster at your Side dested A Good Blaster At Your Side. "
    "Disarmed as written. Tat Celebration dested Tatooine Celebration. "
    "Atrocity dested Imperial Atrocity. Rebel Agent dested Leia, Rebel Princess. "
    "Han, Innocent Scoundrel dested Han Solo, Innocent Scoundrel. Melas dested Melas. "
    "Talon Karrde as written. Wedge dested Wedge Antilles. "
    "Chewie, Carpet dested Chewbacca, Walking Carpet. Doallyn dested Sergeant Doallyn. "
    "Han's Heavy Blaster dested Han's Heavy Blaster Pistol. Black Market Blaster as written. "
    "Luke Skywalker dested Luke Skywalker. AIR5 dested Artoo-Detoo In Red 5. "
    "Mirax dested Mirax Terrik. Skute dested Pulsar Skate. "
    "BoShek, BB dested BoShek, Brash Smuggler. BoShek's Freighter dested BoShek's Modified Light Freighter. "
    "Dash Rendar as written. Outrider as written. Lando Hero dested Lando Calrissian, Unlikely Hero. "
    "Luxury Yacht dested Lady Luck. SATM & BP dested Sorry About The Mess & Blaster Proficiency. "
    "Barrier dested Rebel Barrier. AWRI & DS dested All Wings Report In & Darklighter Spin. "
    "C & TV dested Control & Tunnel Vision. A Few Maneuvers as written. "
    "Not My Fault dested It's Not My Fault!. Alternatives to Fighting dested Alternatives To Fighting. "
    "Houjix & OON dested Houjix & Out Of Nowhere. We'll Find Han as written. "
    "ICBW dested It Could Be Worse. NQA dested No Questions Asked (listed in the main 60). "
    "AFA dested Anger, Fear, Aggression. Tragedy dested A Tragedy Has Occurred. "
    "Aim High as written. Chasm as written. B Plan dested Battle Plan. "
    "DDTA dested Don't Do That Again. Ultimatum as written. Weapons Display as written. "
    "Insight dested Your Insight Serves You Well. STAN dested Simple Tricks And Nonsense. "
    "Sentry dested Yavin Sentry. Another dested There Is Another. "
    "Jedi's Prize dested Jabba's Prize. "
    "Form left column reprints 37–38 on lines 39–40 are Dash Rendar and Outrider. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. SAN. Dark. Deck title Who put the bump in the bump-sh-bump. "
    "WOOKIEE SLAVES dested Wookiee Slaving Operation / Indentured To The Empire (Decipher; (V) unchecked). "
    "KASHYYYK dested Kashyyyk. SLAVE CAMP HQ dested Kashyyyk: Slaving Camp Headquarters. "
    "Den o' Thieves & SD dested Den Of Thieves & Special Delivery. "
    "Power o' Hutt dested Power Of The Hutt. Merc SLAVERS dested Mercenary Slavers. "
    "Wookiee Subj. dested Wookiee Subjugation. "
    "SAIL BARGE: PASSENGER DECK dested Jabba's Sail Barge: Passenger Deck. "
    "Wookies Slaving Camp dested Kashyyyk: Wookiee Slaving Camp. "
    "Skyhook Site dested Kashyyyk: Skyhook Platform. Disarmed as written. "
    "AAA dested Ability, Ability, Ability. Protocol Failure as written. "
    "Scum & Villainy dested Scum And Villainy. "
    "Jabba's Sailing Barge dested Jabba's Sail Barge. "
    "Symbol of Fear dested Slave I, Symbol Of Fear. ZIMH dested Zuckuss In Mist Hunter. "
    "Jabba's Space Cruiser dested Jabba's Space Cruiser. "
    "Elis in Hinthra dested Mist Hunter (V). Dengar in P1 dested Dengar In Punishing One. "
    "Boba Fett, PH dested Boba Fett, Prepared Hunter. "
    "Mandalorian, FoF dested Jango Fett, The Assassin. Dr. Evazan as written. "
    "Pote dested Pote Snitkin. Velken dested Velken Tezeri. Prince Xizor dested Prince Xizor. "
    "Bossk w/ Gun dested Bossk With Mortar Gun. Gela Yeens as written. "
    "Ponda Baba O'Riley dested Ponda Baba. Vigo as written. "
    "Bane Spice Addict dested Bane Malar, Spice Addict. "
    "Maul w/ Saber dested Darth Maul With Lightsaber. Jabba the Hutt dested Jabba The Hutt. "
    "Bib Fortuna, EPI dested Bib Fortuna. Ephant Mon as written. "
    "IG-88 Renegade dested IG-88, Renegade Droid. 4LOM w/ Gun dested 4-LOM With Concussion Rifle. "
    "Sonic Bomb dested Sonic Bombardment. LS Deficiency dested Lightsaber Deficiency. "
    "Abyssin Ornament as written. LSD! dested Look Sir, Droids. "
    "ADTPTR dested A Dark Time For The Rebellion. "
    "SRF & WYB dested Short Range Fighters & Watch Your Back. "
    "Blast Door Controls as written. WAYTTT, Huh?!? dested Where Are You Taking This ... Thing?. "
    "Lateral Damage as written. Hutt Bounty dested Hutt Bounty. "
    "Forest Maze dested Kashyyyk: Forest Maze. Jabba's Haven as written. Nal Hutta as written. "
    "Op As Planned dested Operational As Planned. K & D dested Knowledge And Defense. "
    "Allegations dested Allegations Of Corruption. DTHAIC dested Do They Have A Code Clearance?. "
    "B. Order dested Battle Order. Plans dested Secret Plans. Abyss as written. "
    "CHYC dested Come Here You Big Coward. Fanfare as written. OE dested Oppressive Enforcement. "
    "YCHF dested You Cannot Hide Forever. AUG dested A Useless Gesture. "
    "Resistance as written. TINT dested There Is No Try. "
    "Form left column reprints 37–38 on lines 39–40 are Jabba The Hutt and Bib Fortuna. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Docking Bay 94"),
    n("Wokling", True),
    n("Squadron Assignments"),
    n("Quick Draw", True),
    n("Heading For The Medical Frigate"),
    n("Corellia", True),
    n("Tatooine: Mos Eisley"),
    n("Bacta Tank"),
    n("Strikeforce", True),
    n("Menace Fades"),
    n("Sai'torr Kal Fas", True),
    n("A Good Blaster At Your Side"),
    n("Disarmed"),
    n("Tatooine Celebration", qty=2),
    n("Imperial Atrocity", True),
    n("Leia, Rebel Princess", qty=2),
    n("Han Solo, Innocent Scoundrel", qty=2),
    n("Melas", True),
    n("Talon Karrde"),
    n("Wedge Antilles", True),
    n("Chewbacca, Walking Carpet"),
    n("Sergeant Doallyn", True),
    n("Han's Heavy Blaster Pistol", True),
    n("Black Market Blaster"),
    n("Luke Skywalker", True, qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Mirax Terrik"),
    n("Pulsar Skate"),
    n("BoShek, Brash Smuggler"),
    n("BoShek's Modified Light Freighter"),
    n("Dash Rendar"),
    n("Outrider"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lady Luck"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Rebel Barrier", qty=2),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Control & Tunnel Vision", qty=2),
    n("A Few Maneuvers", qty=2),
    n("It's Not My Fault!", True),
    n("Alternatives To Fighting"),
    n("Houjix & Out Of Nowhere"),
    n("We'll Find Han", True),
    n("It Could Be Worse"),
    n("No Questions Asked", qty=2),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Chasm"),
    n("Battle Plan"),
    n("Don't Do That Again"),
    n("Ultimatum"),
    n("Weapons Display"),
    n("Your Insight Serves You Well"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry"),
    n("There Is Another"),
    n("Jabba's Prize"),
]
LS_ADD = []

DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Den Of Thieves & Special Delivery"),
    n("Power Of The Hutt"),
    n("Mercenary Slavers"),
    n("Wookiee Subjugation"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Kashyyyk: Skyhook Platform"),
    n("Disarmed", qty=2),
    n("Ability, Ability, Ability", True),
    n("Protocol Failure"),
    n("Scum And Villainy", qty=2),
    n("Jabba's Sail Barge", True),
    n("Slave I, Symbol Of Fear"),
    n("Zuckuss In Mist Hunter"),
    n("Jabba's Space Cruiser", True),
    n("Mist Hunter", True),
    n("Dengar In Punishing One"),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Dr. Evazan"),
    n("Pote Snitkin"),
    n("Velken Tezeri"),
    n("Prince Xizor", True, qty=2),
    n("Bossk With Mortar Gun", True),
    n("Gela Yeens", True),
    n("Ponda Baba", True),
    n("Vigo", qty=3),
    n("Bane Malar, Spice Addict"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Jabba The Hutt", True),
    n("Bib Fortuna"),
    n("Ephant Mon"),
    n("IG-88, Renegade Droid"),
    n("4-LOM With Concussion Rifle"),
    n("Sonic Bombardment", True, qty=3),
    n("Lightsaber Deficiency", True),
    n("Abyssin Ornament"),
    n("Look Sir, Droids"),
    n("A Dark Time For The Rebellion", True),
    n("Short Range Fighters & Watch Your Back"),
    n("Blast Door Controls"),
    n("Where Are You Taking This ... Thing?"),
    n("Lateral Damage"),
    n("Hutt Bounty", True),
    n("Kashyyyk: Forest Maze"),
    n("Jabba's Haven"),
    n("Nal Hutta"),
    n("Operational As Planned", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Abyss"),
    n("Come Here You Big Coward"),
    n("Fanfare"),
    n("Oppressive Enforcement"),
    n("You Cannot Hide Forever"),
    n("A Useless Gesture"),
    n("Resistance"),
    n("There Is No Try"),
]
DS_ADD = []
