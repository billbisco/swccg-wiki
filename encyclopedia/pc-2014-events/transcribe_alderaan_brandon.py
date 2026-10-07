#!/usr/bin/env python3
"""2014 Alderaan Regionals Xerox: Brandon.

Source: 2014-Alderaan-Regionals.pdf pages 19–20 (2010 form).
Name Brandon.h dested Brandon. Username blank.
"""
from __future__ import annotations

PLAYER = "Brandon"
USERNAME = ""
STAGE = ""
PDF = "2014 Alderaan Regionals.pdf"
LS_PAGE = 19
DS_PAGE = 20
LS_SCAN = "2014 Alderaan Regionals p19 Brandon LS.png"
DS_SCAN = "2014 Alderaan Regionals p20 Brandon DS.png"
NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Brandon.h dested Brandon. Username blank. "
    "Deck names Thornton step / Thornton slavers. "
    "LS WYS True dested Watch Your Step / This Place Can Be A Little Rough. "
    "DS Wookiee Slaving Op empty dested Wookiee Slaving Operation / Indentured To The Empire without True. "
    "Millennium Falcon True dested Han, Chewie, And The Falcon. "
    "Capt Han dested Captain Han Solo. "
    "CS City dested Spaceport City. "
    "CS DB dested Spaceport Docking Bay. "
    "CS Scoundrels Guild dested Spaceport Scoundrels Guild. "
    "CS Street dested Spaceport Street. "
    "HFTMF dested Heading For The Medical Frigate. "
    "CEC dested Corellian Engineering Corporation. "
    "Insurrection Combo dested Insurrection & Aim High. "
    "Seeking dested Seeking An Audience. "
    "Lando, UH dested Lando Calrissian, Unlikely Hero. "
    "Landoza True dested Lando Calrissian. "
    "Atrocity dested Imperial Atrocity. "
    "LTWW dested Let The Wookiee Win. "
    "Barrier dested Rebel Barrier. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader. "
    "Retort dested Corellian Retort. "
    "Tantive dested Tantive IV. "
    "Leia RP dested Leia, Rebel Princess. "
    "Ant Man Combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Ant Man dested Antilles Maneuver. "
    "Evac Control dested Evacuation Control. "
    "Chewie True dested Chewie, Enraged. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "'Lock' Nawara dested Romas 'Lock' Navander. "
    "H1:DB dested Home One: Docking Bay. "
    "Desp Reach dested Desperate Reach. "
    "NQA dested No Questions Asked. "
    "Ghts dested Grimtaash. "
    "Obi-Wan in Red 5 dested Artoo-Detoo In Red 5. "
    "Melas Brood dested Melas. "
    "Dash dested Dash Rendar. "
    "Yoda, GW dested Yoda, Great Warrior. "
    "AWRI & DS dested All Wings Report In & Darklighter Spin. "
    "Brackman as written. "
    "Palejo dested Palejo Reshad. "
    "Houjix Combo dested Houjix & Out Of Nowhere. "
    "AFA dested Anger, Fear, Aggression. "
    "STAN dested Staging Areas. "
    "A Tragedy dested A Tragedy Has Occurred. "
    "Kash Headquarters dested Kashyyyk: Slaving Camp Headquarters. "
    "Den of Thieves Combo dested Den Of Thieves & Special Delivery. "
    "Wookiee Subj dested Wookiee Subjugation. "
    "Merc Slavers dested Mercenary Slavers. "
    "SSPFT dested Something Special Planned For Them. "
    "Elis Hinthra dested Elis In Hinthra. "
    "Probot dested Probe Droid. "
    "Sail Barge: Pass Deck dested Jabba's Sail Barge: Passenger Deck. "
    "IG88 Renegade Droid dested IG-88, Renegade Droid. "
    "Mara w/ saber dested Mara Jade With Lightsaber. "
    "Slave I SoF dested Slave I, Symbol Of Fear. "
    "Control Combo dested Control & Set For Stun. "
    "SRF / WYB dested Short Range Fighters & Watch Your Back!. "
    "Merc Pilot dested Mercenary Pilot. "
    "Imp Barrier dested Imperial Barrier. "
    "A Dark Time dested A Dark Time For The Rebellion. "
    "Kash: Skyhook Plc dested Kashyyyk: Skyhook Platform. "
    "ORS dested Ominous Rumors. "
    "Grimtaash dested Ghhhk. "
    "Ephant mn dested Ephant Mon. "
    "Kash: Slaving Camp dested Kashyyyk: Wookiee Slaving Camp. "
    "Shutdown Combo as written. "
    "Line 39 crossed then K+D dested Knowledge And Defense. "
    "4-LOM w/ gun dested 4-LOM With Concussion Rifle. "
    "Jango Assassin dested Jango Fett, The Assassin. "
    "MM Combo dested Masterful Move & Endor Occupation. "
    "Imbalance Combo dested Imbalance & Kintan Strider. "
    "CC Sec Tower dested Cloud City: Security Tower. "
    "Imp Prop dested Imperial Propaganda. "
    "Boba Prep Hunter dested Boba Fett, Prepared Hunter. "
    "EPP Dengar dested Dengar With Blaster Carbine. "
    "wooo dested Wookiee Roar. "
    "YISYW dested Your Insight Serves You Well. "
    "DODN dested Do, Or Do Not. "
    "Optimism dested Let's Keep A Little Optimism Here. "
    "Professor dested The Professor. "
    "BP dested Battle Plan. "
    "SP dested Secret Plans. "
    "Allegations dested Allegations Of Corruption. "
    "Coward dested Come Here You Big Coward. "
    "YCHF dested You Cannot Hide Forever. "
    "TINT dested There Is No Try. "
    "Opp Enf dested Oppressive Enforcement. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "B Order dested Battle Order. "
    "Useless Gesture dested A Useless Gesture. "
    "DS Sentry dested Death Star Sentry. "
    "NO_DEST as written: Brackman; Shutdown Combo; Wookiee Roar True (Dark). "
    "(V) from checkbox. Unique overcounts sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True), n("Han, Chewie, And The Falcon", True),
    n("Captain Han Solo"), n("Spaceport City"),
    n("Heading For The Medical Frigate"), n("Wokling", True),
    n("Corellian Engineering Corporation", True), n("Insurrection & Aim High"),
    n("Seeking An Audience", True), n("Lando Calrissian, Unlikely Hero"),
    n("Imperial Atrocity", True, qty=2), n("Let The Wookiee Win", True, qty=2),
    n("Spaceport Docking Bay"), n("Rebel Barrier", qty=2),
    n("Leia's Blaster Rifle"), n("Corellian Slip", True),
    n("Wedge Antilles, Red Squadron Leader", qty=2), n("Corellian Retort", True, qty=2),
    n("Tantive IV", True), n("Leia, Rebel Princess", qty=2),
    n("Antilles Maneuver & Rebel Reinforcements"), n("Punch It!"),
    n("Evacuation Control", True), n("Chewie, Enraged", True),
    n("Luke Skywalker, Jedi Knight", qty=2), n("Antilles Maneuver", True, qty=2),
    n("Romas 'Lock' Navander"), n("Spaceport Scoundrels Guild"),
    n("Home One: Docking Bay"), n("Lando Calrissian", True),
    n("Desperate Reach", True), n("No Questions Asked", True, qty=3), n("Grimtaash"),
    n("Artoo-Detoo In Red 5"), n("Mirax Terrik"), n("General Crix Madine"),
    n("Corran Horn"), n("Spaceport Street"), n("Melas"), n("Dash Rendar", True),
    n("Yoda, Great Warrior"), n("All Wings Report In & Darklighter Spin"),
    n("Brackman"), n("Palejo Reshad"), n("Jaina Solo"), n("Lady Luck"),
    n("Menace Fades"), n("Houjix & Out Of Nowhere"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Chasm", True), n("Weapons Display", True), n("Wise Advice"),
    n("Yavin Sentry", True), n("Your Insight Serves You Well", True),
    n("Do, Or Do Not"), n("Planetary Defenses", True),
    n("Let's Keep A Little Optimism Here", True), n("The Professor", True),
    n("Aim High"), n("Battle Plan"), n("Don't Do That Again", True),
]
LS_ADD = [
    n("Ultimatum"), n("Staging Areas"), n("A Tragedy Has Occurred"),
]
DS_START = "Wookiee Slaving Operation / Indentured To The Empire"
DS_CARDS = [
    n("Wookiee Slaving Operation / Indentured To The Empire"),
    n("Kashyyyk"), n("Kashyyyk: Slaving Camp Headquarters"),
    n("Den Of Thieves & Special Delivery"), n("Wookiee Subjugation"),
    n("Mercenary Slavers"), n("Jabba's Haven"), n("Power Of The Hutt"),
    n("Something Special Planned For Them", True), n("Elis In Hinthra"),
    n("Probe Droid"), n("Jabba The Hutt", True, qty=2), n("Prince Xizor"),
    n("Jabba's Sail Barge: Passenger Deck"), n("Cold Feet", True),
    n("IG-88, Renegade Droid"), n("Mara Jade With Lightsaber"),
    n("Slave I, Symbol Of Fear"), n("Control & Set For Stun"),
    n("Garindan", True), n("Ponda Baba", True),
    n("Short Range Fighters & Watch Your Back!"), n("Nal Hutta"),
    n("Mercenary Pilot", True), n("Imperial Barrier"), n("Bossk", True),
    n("A Dark Time For The Rebellion", True), n("Hutt Bounty", True),
    n("Monnok"), n("Kashyyyk: Skyhook Platform"), n("Sneak Attack", True, qty=2),
    n("Ominous Rumors", qty=4), n("Ghhhk"), n("Scum And Villainy", qty=2),
    n("Ephant Mon"), n("Kashyyyk: Wookiee Slaving Camp"), n("Shutdown Combo"),
    n("Knowledge And Defense", True), n("OOM-9", True),
    n("4-LOM With Concussion Rifle"), n("Jango Fett, The Assassin"),
    n("Masterful Move & Endor Occupation"), n("Jabba's Space Cruiser", True),
    n("Imbalance & Kintan Strider"), n("Sonic Bombardment", True, qty=3),
    n("Jabba's Sail Barge", True), n("Cloud City: Security Tower", True),
    n("Imperial Propaganda", True), n("Boba Fett, Prepared Hunter"),
    n("Dengar With Blaster Carbine", True), n("Wookiee Roar", True),
    n("Cease Fire!"),
]
DS_SHIELDS = [
    n("Secret Plans"), n("Allegations Of Corruption"),
    n("Come Here You Big Coward"), n("Resistance"),
    n("You Cannot Hide Forever"), n("There Is No Try"),
    n("Oppressive Enforcement"), n("Imperial Detention", True),
    n("Do They Have A Code Clearance?", True), n("Fanfare", True),
    n("Firepower", True), n("Battle Order"),
]
DS_ADD = [
    n("A Useless Gesture", True), n("Abyss", True), n("Death Star Sentry", True),
]
