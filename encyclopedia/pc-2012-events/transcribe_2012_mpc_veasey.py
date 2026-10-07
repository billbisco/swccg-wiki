#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: John Veasey.

Source: 2012mpcday1.pdf pages 139–140 (2010 form, 12 shields).
Name Veez dested John Veasey (2013 Worlds analog PLAYER="John Veasey" name box VeeZ).
Username blank (do not copy 2013 Username veez or 2014 Username VeeZ).
p139 Light Watch Your Step. p140 Dark Kessel.
LIGHT/DARK boxes empty dest sides from the 60s.
Pack player-stubs/John_Veasey.wiki (is_bio False).
Do not dest as Veez as a new person.
Do not dest as Thomas Graham.
Do not rewrite 2013 leftover Communing / Agents (Worlds) or Communing / A Stunning Move (MPC).
"""
from __future__ import annotations

PLAYER = "John Veasey"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 139
DS_PAGE = 140
LS_SCAN = "2012 Match Play Championship Day 1 John Veasey LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 John Veasey DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = "Handwritten 2010 Xerox form."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Veez dested John Veasey. "
    "Username blank. LIGHT/DARK empty dest Light from the 60s. "
    "Do not dest as Veez as a new person. "
    "Do not copy 2013 Username veez or 2014 Username VeeZ. "
    "Do not rewrite 2013 leftover Communing. "
    "Watch Yer Step / Patriot dested Watch Your Step / This Place Can Be A Little Rough empty analog leftover. "
    "Anger Fear Aggression True dested Anger, Fear, Aggression True in the 60 analog Casey. "
    "Tat Cantina dested Tatooine: Cantina analog leftover. "
    "Tat DB 94 dested Tatooine: Docking Bay 94 analog leftover. "
    "HFTMF dested Heading For The Medical Frigate analog leftover. "
    "I ought be allowed to grind True dested I Should Be Allowed To Grind True analog leftover. "
    "Hear me baby Hold together dested Hear Me Baby, Hold Together analog leftover. "
    "LTWW dested Let The Wookiee Win analog leftover. "
    "Control and Tunnel Vision dested Control & Tunnel Vision analog leftover. "
    "All Wings Report and Rebel Spin dested All Wings Report In & Darklighter Spin analog leftover. "
    "Line 27 blank skipped unique 59 analog Schoenthal blank line. "
    "I'll Take the Leader dested I'll Take The Leader analog leftover. "
    "Projection Skywalker dested Projection Of A Skywalker analog leftover. "
    "Chewbacca Protector dested Chewbacca, Protector analog leftover. "
    "Sergeant Beylsn True dested Sergeant Bruckman True analog leftover. "
    "Han Solo Courageous Smuggler dested Han Solo, Courageous Smuggler analog leftover. "
    "BoShek Brash Smuggler dested BoShek, Brash Smuggler analog leftover. "
    "Chewie's ATST True dested Chewie's AT-ST True analog leftover. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5 analog leftover. "
    "P. Skate has List Frame dested Booster In Pulsar Skate analog leftover. "
    "Tatooine Lars Moisture Farm True dested Tatooine: Lars' Moisture Farm True analog leftover. "
    "Luke Skywalker True AND empty kept separate analog Foth. Unique 59. Shields 12. "
    "Chasm True dested Chasm True analog leftover."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Veez dested John Veasey. "
    "Username blank. LIGHT/DARK empty dest Dark from the 60s. "
    "Do not dest as Veez as a new person. "
    "Do not copy 2013 Username veez or 2014 Username VeeZ. "
    "Do not rewrite 2013 leftover Agents / A Stunning Move. "
    "Knowledge And Defense True dested in the 60 analog Murray. Start is Kessel empty. "
    "Combat Readiness True dested analog leftover. "
    "Kessel - Administrator's Office dested Kessel: Spice Mines - Administrator's Office analog leftover. "
    "I'll Take them Myself dested I'll Take Them Myself analog leftover. "
    "Kuat Drive Yards True dested analog leftover. "
    "4LOM With Concussion Rifle True dested 4-LOM With Concussion Rifle True analog leftover. "
    "Black Leader dested Juno Eclipse, Black Leader analog Eier. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach analog Eier. "
    "General Veers True dested Veers True analog Brian leftover. "
    "Tempest 1 dested analog Brian leftover. "
    "Blackhole Support Ship dested Executor analog leftover. "
    "Denger in Punishing One dested Dengar In Punishing One analog leftover. "
    "Boba Fett in Slave One True dested Boba Fett In Slave I True analog leftover. "
    "Thunder Flare dested Thunderflare analog leftover. "
    "Victory dested without extra (V). "
    "Kessel Docking Bay dested Kessel: Spice Mines - Docking Bay analog leftover. "
    "Kessel Extraction Facility dested Kessel: Spice Mines - Extraction Facility analog leftover. "
    "Control and Set For Stun dested Control & Set For Stun analog leftover. "
    "Masterful Move and Endor Occupation dested Masterful Move & Endor Occupation analog leftover. "
    "Close Call True AND empty kept separate analog Foth. "
    "He is Not Ready and Imperial Propaganda dested He Is Not Ready & Imperial Propaganda analog leftover. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance? analog leftover. "
    "Kessel Surveillance System dested analog leftover. Unique 60. Shields 11 shield 12 blank skipped. "
    "Endor Shield True in the 60 AND empty in shields kept separate analog Foth. "
    "Resistance dested without extra (V) analog Mack."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine"),
    n("Heading For The Medical Frigate"),
    n("Squadron Assignments"),
    n("Wokling", True),
    n("I Should Be Allowed To Grind", True),
    n("Grimtaash"),
    n("Too Close For Comfort"),
    n("Hear Me Baby, Hold Together"),
    n("Hyper Escape"),
    n("Lost In The Wilderness"),
    n("Weapon Levitation"),
    n("Let The Wookiee Win"),
    n("On The Edge"),
    n("Corellian Retort", True),
    n("Houjix"),
    n("Escape Pod", True),
    n("Dodge"),
    n("Fallen Portal"),
    n("Control & Tunnel Vision", qty=2),
    n("Moving To Attack Position"),
    n("All Wings Report In & Darklighter Spin"),
    n("Uncontrollable Fury"),
    n("Seeking An Audience", True),
    n("I'll Take The Leader"),
    n("Projection Of A Skywalker"),
    n("Scrambled Transmission", True),
    n("Menace Fades"),
    n("Phylo Gandish"),
    n("Talon Karrde", qty=2),
    n("Luke Skywalker", True),
    n("Luke Skywalker"),
    n("Chewbacca, Protector"),
    n("Rycar Ryjerd", True),
    n("Sergeant Bruckman", True),
    n("Lando With Blaster Pistol"),
    n("Melas", True),
    n("Mirax Terrik"),
    n("Dash Rendar"),
    n("Wedge Antilles", True),
    n("Theron Nett"),
    n("Han Solo, Courageous Smuggler"),
    n("BoShek, Brash Smuggler"),
    n("Chewie's AT-ST", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Red 10"),
    n("Pulsar Skate"),
    n("Outrider"),
    n("Millennium Falcon"),
    n("Booster In Pulsar Skate"),
    n("Corellia", True),
    n("Kessel"),
    n("Tatooine: Lars' Moisture Farm", True),
]
LS_SHIELDS = [
    n("He Can Go About His Business", True),
    n("Chasm", True),
    n("Aim High"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum", True),
    n("Battle Plan"),
    n("Let's Keep A Little Optimism Here", True),
    n("The Professor"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
]
LS_ADD = []

DS_START = "Kessel"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("I'll Take Them Myself"),
    n("Endor Shield", True),
    n("Kuat Drive Yards", True),
    n("4-LOM With Concussion Rifle", True),
    n("U-3PO"),
    n("Juno Eclipse, Black Leader"),
    n("Admiral Motti", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Spice Mine Administrator", qty=2),
    n("Mara Jade With Lightsaber"),
    n("Darth Maul With Lightsaber"),
    n("Darth Vader With Lightsaber"),
    n("Grand Moff Tarkin", True),
    n("Veers", True),
    n("Grand Admiral Thrawn"),
    n("Blizzard 2", True),
    n("Blizzard 1", True, qty=2),
    n("Tempest 1"),
    n("Executor"),
    n("Dengar In Punishing One"),
    n("Boba Fett In Slave I", True),
    n("Conquest", True),
    n("Tyrant"),
    n("Thunderflare"),
    n("Victory", qty=2),
    n("Kashyyyk"),
    n("Endor"),
    n("Kessel: Spice Mines - Docking Bay"),
    n("Kessel: Spice Mines - Extraction Facility"),
    n("Control & Set For Stun"),
    n("Operational As Planned", True),
    n("Trample"),
    n("Imperial Barrier"),
    n("Imperial Command", qty=2),
    n("Close Call", True),
    n("Close Call"),
    n("Masterful Move & Endor Occupation"),
    n("Ghhhk"),
    n("Cold Feet", True),
    n("You Are Beaten"),
    n("Alter"),
    n("Sense"),
    n("Battle Deployment"),
    n("Tarkin's Bounty", True),
    n("Something Special Planned For Them", True),
    n("I Have You Now", True),
    n("Do They Have A Code Clearance?"),
    n("He Is Not Ready & Imperial Propaganda"),
    n("Protocol Failure"),
    n("Lost In Space"),
    n("Spice Mine Operations"),
    n("Kessel Surveillance System"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Secret Plans"),
    n("Resistance"),
    n("Abyss", True),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Battle Order"),
    n("Endor Shield"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = []
