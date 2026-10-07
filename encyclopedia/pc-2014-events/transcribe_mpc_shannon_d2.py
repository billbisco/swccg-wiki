#!/usr/bin/env python3
"""2014 Match Play Championship Day 2 Xerox: Kevin Shannon.

Source: MPC-2014-Day-2-Main-Event.pdf pages 5–6.
Name Shannon dested Kevin Shannon. Username blank.
Same as Yesterday with In/Out from Day 1 both sides (notes pages, no 60 form).
"""
from __future__ import annotations

PLAYER = "Kevin Shannon"
USERNAME = ""
STAGE = "Day 2"
PDF = "2014 Match Play Championship Day 2.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2014 Match Play Championship Day 2 Kevin Shannon LS.png"
DS_SCAN = "2014 Match Play Championship Day 2 Kevin Shannon DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Same as Yesterday with In/Out notes. Dest Day 1 60 minus OUT plus IN."
PUBLIC_NOTE = (
    "Same as Day 1 with In/Out substitutions listed on the scan."
)
LS_NOTE = (
    "Same as Yesterday notes page. Name Shannon dested Kevin Shannon. "
    "OUT Path Of Least Resistance (one copy, Day 1 qty 2). "
    "IN I'll Take The Leader. Dest Day 1 Light minus that OUT plus that IN."
)
DS_NOTE = (
    "Same as Yesterday notes page. Name Shannon dested Kevin Shannon. "
    "OUT Sonic Bombardment (V) one copy (Day 1 qty 3), Tarkin's Orders, "
    "He Hasn't Come Back Yet, Stop Motion (V). "
    "IN Twi'lek Advisor (V), Ki-Adi-Mundi, Lightsaber Proficiency (V) second copy, "
    "Where Are You Taking This... Thing?. "
    "Ki-Adi-Mundi's Shadow Killer dested Ki-Adi-Mundi. "
    "We're ARE You taking them dested Where Are You Taking This... Thing?. "
    "Dest Day 1 Dark minus those OUT plus those IN. (V) from Day 1 checkbox / notes V."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate", True),
    n("All My Urchins & Cloud City Celebration"),
    n("Beldon's Eye", True),
    n("Keeping The Empire Out Forever"),
    n("Cloud City: North Corridor"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Cloud City: West Gallery"),
    n("Cloud City: Platform 327 (Docking Bay)"),
    n("Kebyc", True),
    n("Chewbacca, Walking Carpet"),
    n("Leslomy Tacema", True),
    n("Tanus Spijek", True),
    n("Melas", True),
    n("Sergeant Edian", True),
    n("Jar Jar Binks"),
    n("Leia, Rebel Princess"),
    n("Harc Seff", True),
    n("Han Solo, Innocent Scoundrel"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Mirax Terrik"),
    n("Leesub Sirln", True),
    n("Trooper Utris M'Toc", True),
    n("Luke With Lightsaber"),
    n("Nien Nunb, Sullustan Smuggler"),
    n("Aayla Secura"),
    n("Foul Moudama"),
    n("Caldera Righim", True),
    n("Dash Rendar", True),
    n("Oola"),
    n("It Could Be Worse"),
    n("Lady Luck"),
    n("Booster In Pulsar Skate"),
    n("Overseer"),
    n("Outrider"),
    n("Path Of Least Resistance"),
    n("Dark Approach", True),
    n("Choke", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("It's A Trap"),
    n("Escape Pod", True),
    n("Let The Wookiee Win", True, qty=2),
    n("It's A Hit"),
    n("Blast The Door, Kid!"),
    n("Alter"),
    n("Houjix"),
    n("Grimtaash"),
    n("Rebel Barrier", qty=2),
    n("Imperial Atrocity", True, qty=2),
    n("Hiding In The Garbage", True),
    n("Ellor's Madak", True),
    n("Menace Fades"),
    n("Anger, Fear, Aggression", True),
    n("I'll Take The Leader"),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Ultimatum"),
    n("Jabba's Prize", True),
    n("Chasm", True),
    n("Don't Do That Again", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Do, Or Do Not"),
    n("Simple Tricks And Nonsense"),
]
LS_ADD = [
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Wise Advice"),
]


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Den Of Thieves & Special Delivery"),
    n("Wookiee Subjugation"),
    n("Mercenary Slavers"),
    n("Power Of The Hutt"),
    n("Jabba's Haven"),
    n("Kashyyyk: Skyhook Platform"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Nal Hutta"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Velken Tezeri", True),
    n("OOM-9", True),
    n("Jango Fett, The Assassin"),
    n("Mercenary Pilot", True),
    n("Outer Rim Scout", qty=4),
    n("Dengar With Blaster Carbine", True),
    n("Ponda Baba", True),
    n("Bossk", True),
    n("Probot"),
    n("Ephant Mon"),
    n("IG-88, Renegade Droid"),
    n("Prince Xizor"),
    n("Boba Fett, Prepared Hunter"),
    n("P-59"),
    n("Jabba The Hutt", True),
    n("4-LOM With Concussion Rifle"),
    n("Mara Jade With Lightsaber"),
    n("Garindan", True),
    n("Maul's Sith Infiltrator"),
    n("Jabba's Space Cruiser", True),
    n("Slave I, Symbol Of Fear"),
    n("Jabba's Sail Barge", True),
    n("Lightsaber Proficiency", True, qty=2),
    n("Short Range Fighters & Watch Your Back!"),
    n("Defensive Fire & Hutt Smooch"),
    n("Sonic Bombardment", True, qty=2),
    n("Imbalance & Kintan Strider"),
    n("Sneak Attack", True, qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Limited Resources"),
    n("Cold Feet", True),
    n("Defensive Fire & Hutt Smooch"),
    n("Scum And Villainy", qty=2),
    n("Something Special Planned For Them", True),
    n("Hutt Bounty", True),
    n("Protocol Failure"),
    n("Ability, Ability, Ability", True),
    n("Knowledge And Defense", True),
    n("Twi'lek Advisor", True),
    n("Ki-Adi-Mundi"),
    n("Where Are You Taking This... Thing?"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Firepower", True),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance", True),
    n("Fanfare", True),
    n("There Is No Try"),
    n("Abyss", True),
    n("Imperial Detention", True),
    n("Oppressive Enforcement"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
