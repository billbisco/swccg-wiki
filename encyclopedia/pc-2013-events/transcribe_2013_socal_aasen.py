#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Phil Aasen Xerox LS+DS.

Username Korreshark. Light Chewie's Hut in the margin replaces struck
It Is The Future You See on line 1; line 2 is still IITFYS.
"""
from __future__ import annotations

PLAYER = "Phil Aasen"
USERNAME = "Korreshark"
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2013 SoCal Grand Prix Day 1 p01 Phil Aasen LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p02 Phil Aasen DS.png"
LS_NOTE = (
    "Handwritten Xerox form. Username Korreshark. Deck name Undesaided. "
    "Margin Chewie's Hut replaces struck line 1 It Is The Future You See; "
    "line 2 is still It Is The Future You See (V). BP/DTE → Battle Plan & Draw Their Fire. "
    "DoDN/WA → Do, Or Do Not & Wise Advice. TCC (V) → Coruscant: Jedi Council Chamber (V). "
    "Jedi Luke (LS, TK) → Luke Skywalker, Jedi Knight. SITF → Luke Skywalker, Strong In The Force. "
    "MOTO → Mace Windu, Master Of The Order. R2 in RS → Artoo-Detoo In Red 5. "
    "HCF → Han, Chewie, And The Falcon. SWTJCC → Speak With The Jedi Council. "
    "SATM/BP → Sorry About The Mess & Blaster Proficiency. AFA → Anger, Fear, Aggression. "
    "Republic Gunship (V) → Republic Cruiser. "
    "HF & All Business → He Can Go About His Business. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Xerox form. Username Korreshark. Deck name Let The Wookiee Lose. "
    "Wookiee Slaving ops / Jabba → Wookiee Slaving Operation / Indentured To The Empire. "
    "Slave I SOF → Slave I, Symbol Of Fear. BF Prepared Hunter → Boba Fett, Prepared Hunter. "
    "DIPO → Dengar In Punishing One. ORS → Outer Rim Scout. JS Cruiser → Jabba's Space Cruiser. "
    "K: Slaving HTR → Kashyyyk: Slaving Camp Headquarters. Merc. Slavers as written. "
    "SRF/WPB → Short Range Fighters & Watch Your Back!. SKP/WTK → Imbalance & Kintan Strider. "
    "Den of Thieves / SD → Den Of Thieves & Special Delivery. Jango Fett, TA → Jango Fett, The Assassin. "
    "KAD → Knowledge And Defense. DTF & CC → Do They Have A Code Clearance?. "
    "FYC of Disturbing → I Find Your Lack Of Faith Disturbing. YCHF → You Cannot Hide Forever. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "It Is The Future You See"
LS_CARDS = [
    n("Kashyyyk: Chewie's Hut"),
    n("It Is The Future You See", True),
    n("Battle Plan & Draw Their Fire"),
    n("Do, Or Do Not & Wise Advice"),
    n("Quick Draw", True),
    n("Naboo: Boss Nass' Chambers"),
    n("Naboo: Battle Plains"),
    n("Hoth: Echo Command Center (War Room)"),
    n("Home One: War Room"),
    n("Coruscant: Jedi Council Chamber", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Luke Skywalker, Strong In The Force", True, qty=2),
    n("Mace Windu", True, qty=2),
    n("Mace Windu, Master Of The Order", True),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Admiral Ackbar", True),
    n("Master Qui-Gon", True, qty=2),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Home One"),
    n("Han, Chewie, And The Falcon", True),
    n("Lady Luck", True),
    n("Republic Cruiser", True),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Qui-Gon's Lightsaber"),
    n("Strikeforce", True),
    n("Imperial Atrocity", True),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Mechanical Failure"),
    n("Let The Wookiee Win", True, qty=3),
    n("Wesa Gotta Grand Army", qty=3),
    n("Speak With The Jedi Council", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Escape Pod", True, qty=2),
    n("Houjix"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Clash Of Sabers", qty=2),
    n("Jedi Levitation", True),
    n("Sense"),
    n("Luke's Bionic Hand", True),
    n("A Jedi's Resilience"),
    n("Blaster Deflection"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("There Is Another", True),
    n("Only Jedi Carry That Weapon"),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Ship?"),
    n("He Can Go About His Business", True),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Simple Tricks And Nonsense", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Chasm", True),
    n("Weapons Display", True),
    n("Jabba's Prize", True),
    n("The Professor", True),
    n("Yavin Sentry", True),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire", True),
    n("Jabba's Haven", True),
    n("Power Of The Hutt"),
    n("Slave I, Symbol Of Fear", True),
    n("Outer Rim Scout"),
    n("Abyssin Ornament", True),
    n("Boba Fett, Prepared Hunter", True),
    n("Dengar In Punishing One"),
    n("Nal Hutta"),
    n("Outer Rim Scout", qty=2),
    n("Velken Tezeri", True),
    n("Jabba's Space Cruiser", True),
    n("Kashyyyk"),
    n("Jabba's Sail Barge", True),
    n("Ponda Baba", True),
    n("Probot", True),
    n("P-59"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Skyhook Platform", True),
    n("Kashyyyk: Wookiee Slaving Camp", True),
    n("Scum And Villainy"),
    n("Kashyyyk: Slaving Camp Headquarters", True),
    n("Mercenary Slavers", True),
    n("Guri", True),
    n("Imperial Barrier"),
    n("Zuckuss In Mist Hunter"),
    n("Force Push", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Sith Probe Droid", True),
    n("Lightsaber Deficiency", True),
    n("Lady Valarian", True),
    n("Cold Feet", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Imperial Justice", True),
    n("Imbalance & Kintan Strider"),
    n("Wookiee Subjugation", True),
    n("Mercenary Pilot"),
    n("Imperial Barrier"),
    n("IG-88 With Riot Gun"),
    n("4-LOM With Concussion Rifle"),
    n("Jabba The Hutt", True),
    n("Sonic Bombardment", True, qty=2),
    n("Bane Malar", True),
    n("Ephant Mon"),
    n("Hutt Bounty", True),
    n("Bossk", True),
    n("Limited Resources"),
    n("Imperial Decree", True),
    n("Relentless Pursuit", True),
    n("Garindan", True),
    n("Mara Jade With Lightsaber", True),
    n("J'Quille", True),
    n("Jango Fett, The Assassin", True),
    n("You Swindled Me", True),
    n("Protocol Failure", True),
    n("Cease Fire"),
    n("Den Of Thieves & Special Delivery", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("After Her!", True),
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Resistance"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("A Useless Gesture"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
    n("Secret Plans"),
]
DS_ADD = []
