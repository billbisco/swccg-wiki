#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Kevin Shannon.

Source: 2014-TMW-Day-1.pdf pages 17–18 (2013 form).
Name Shannon dested Kevin Shannon (informed 99.9%).
"""
from __future__ import annotations

PLAYER = "Kevin Shannon"
USERNAME = ""
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 17
DS_PAGE = 18
LS_SCAN = "2014 Texas Mini Worlds Day 1 p17 Kevin Shannon LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p18 Kevin Shannon DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields)."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Shannon dested Kevin Shannon. Username blank. LIGHT/DARK both empty; cards are Light. "
    "Plead My Case To Senate dested Plead My Case To The Senate / Sanity And Compassion. "
    "Do not dest as a new person. "
    "Heading For Frigate dested Heading For The Medical Frigate. "
    "Yoda, Great Warrior dested Yoda, Great Warrior. "
    "Luke Skywalker, Rebel Scout dested Luke Skywalker, Rebel Scout. "
    "Wedge Antilles, Red Squadron Leader dested Wedge Antilles, Red Squadron Leader. "
    "Lando Calrissian, Scoundrel dested Lando Calrissian, Scoundrel. "
    "Chewbacca Protector dested Chewbacca, Protector. "
    "A280 Sharpshooter Rifle dested A280 Sharpshooter Rifle. "
    "Yoda's Stew & You Do Have Your Moments dested Yoda Stew & You Do Have Your Moments. "
    "Much To Learn You Still Have dested Much To Learn You Still Have. "
    "So This Is How Liberty Dies dested So This Is How Liberty Dies. "
    "Unique overcounts sheet-accurate (Might Of The Republic x3, Rebel Leadership x2, "
    "Luke Skywalker, Rebel Scout x2, Obi-Wan With Lightsaber x2, Lando Calrissian, Scoundrel x2, "
    "Bail Organa x2, Bail Organa, Father Of Rebellion x2, Jedi Presence x2). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Shannon dested Kevin Shannon. Username blank. LIGHT/DARK both empty; cards are Dark. "
    "Wookiee Slaving Ops dested Wookiee Slaving Operation / Indentured To The Empire. "
    "Nal Hutta dested Nal Hutta. "
    "P-59 dested P-59. "
    "Mandalorian, Father of Fett dested Jango Fett, The Assassin. "
    "Boba Fett, Prep'd Hunter dested Boba Fett, Prepared Hunter. "
    "Slave I, Symbol Of Fear dested Slave I, Symbol Of Fear. "
    "Maul's Sith Infiltrator dested Maul's Sith Infiltrator. "
    "Masterful Move dested Masterful Move. "
    "Masterful Move & Endor Occ dested Masterful Move & Endor Occupation. "
    "Defensive Fire & Hutt Smooch dested Defensive Fire & Hutt Smooch. "
    "Short Range Fighters & Watch Your Back dested Short Range Fighters & Watch Your Back!. "
    "Scum & Villainy dested Scum And Villainy. "
    "Ability Ability Ability dested Ability, Ability, Ability. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "CHYBC dested Come Here You Big Coward. "
    "We'll Let Fate-a Decide HUH dested We'll Let Fate-a Decide, Huh?. "
    "YCHF dested You Cannot Hide Forever. "
    "DTHLOED dested Do They Have A Code Clearance?. "
    "Unique overcounts sheet-accurate (Outer Rim Scout x4, Jabba The Hutt x2, "
    "Dengar With Blaster Carbine x2, Sonic Bombardment x2, Scum And Villainy x2, "
    "Cease Fire x2). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Plead My Case To The Senate / Sanity And Compassion"
LS_CARDS = [
    n("Plead My Case To The Senate / Sanity And Compassion"),
    n("Coruscant: Galactic Senate"),
    n("Coruscant: Jedi Council Chamber"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Strike Planning"),
    n("Rogue Squadron Tactics"),
    n("Endor: Back Door"),
    n("Home One: War Room"),
    n("Endor: Forest Depths"),
    n("Dressel"),
    n("Bail Organa", qty=2),
    n("Bail Organa, Father Of Rebellion", qty=2),
    n("Senator Mon Mothma"),
    n("Senator Padme Amidala"),
    n("Senator Leia Organa"),
    n("Yoda, Great Warrior", qty=2),
    n("Luke Skywalker, Rebel Scout", True, qty=2),
    n("Obi-Wan With Lightsaber", qty=2),
    n("Admiral Ackbar", True),
    n("Commander Narra"),
    n("Owen Lars & Beru Lars"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Lando Calrissian, Scoundrel", qty=2),
    n("Jaina Solo"),
    n("General Solo", True),
    n("Corran Horn"),
    n("General Airen Cracken"),
    n("Chewbacca, Protector"),
    n("Home One"),
    n("Alderaan Consular Ship"),
    n("Jedi Presence", qty=2),
    n("Escape Pod", True),
    n("Might Of The Republic", qty=3),
    n("Rebel Leadership", True, qty=2),
    n("A280 Sharpshooter Rifle", True),
    n("Sense", qty=2),
    n("Houjix"),
    n("Yoda Stew & You Do Have Your Moments"),
    n("Grimtaash"),
    n("Let The Wookiee Win", True),
    n("Imperial Atrocity", True),
    n("Field Dressing"),
    n("Much To Learn You Still Have"),
    n("Seeking An Audience", True),
    n("Menace Fades"),
    n("So This Is How Liberty Dies"),
    n("Senate Hovercam"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Yavin Sentry"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Jabba's Prize"),
    n("Wise Advice"),
    n("Planetary Defenses", True),
]
LS_ADD = []


DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"),
    n("Kashyyyk: Slaving Camp Headquarters"),
    n("Mercenary Slavers"),
    n("Power Of The Hutt"),
    n("Den Of Thieves & Special Delivery"),
    n("Jabba's Haven"),
    n("Nal Hutta"),
    n("Jabba's Sail Barge: Passenger Deck"),
    n("Kashyyyk: Wookiee Slaving Camp"),
    n("Velken Tezeri", True),
    n("IG-88, Renegade Droid"),
    n("Jabba The Hutt", True, qty=2),
    n("P-59"),
    n("Garindan", True),
    n("OOM-9"),
    n("Probot"),
    n("Outer Rim Scout", qty=4),
    n("Bossk", True),
    n("Ponda Baba", True),
    n("4-LOM With Concussion Rifle"),
    n("Ephant Mon"),
    n("Dengar With Blaster Carbine", True, qty=2),
    n("Mercenary Pilot", True),
    n("Mara Jade With Lightsaber"),
    n("Jango Fett, The Assassin"),
    n("Prince Xizor"),
    n("Boba Fett, Prepared Hunter"),
    n("Jabba's Sail Barge", True),
    n("Jabba's Space Cruiser", True),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Cease Fire", qty=2),
    n("Monnok"),
    n("Ghhhk"),
    n("Masterful Move"),
    n("Masterful Move & Endor Occupation"),
    n("Defensive Fire & Hutt Smooch"),
    n("Sneak Attack", True, qty=2),
    n("Sonic Bombardment", True, qty=2),
    n("Cold Feet", True),
    n("Wookiee Subjugation"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Imperial Propaganda", True),
    n("Scum And Villainy", qty=2),
    n("Hutt Bounty", True),
    n("Something Special Planned For Them", True),
    n("Where Are You Taking This... Thing?"),
    n("Ability, Ability, Ability", True),
    n("Kashyyyk: Skyhook Platform"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Death Star Sentry", True),
    n("A Useless Gesture", True),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Abyss", True),
    n("Secret Plans"),
    n("Firepower", True),
    n("Fanfare"),
    n("There Is No Try"),
    n("Do They Have A Code Clearance?", True),
    n("Come Here You Big Coward"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("DTHLOED"),
]
DS_ADD = []
