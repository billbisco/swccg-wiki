#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Zach Stenerson.

Source: 2012NationalsDay1.pdf pages 72–73 (handwritten 2010 Xerox, 12 shields).
p72 Dark / p73 Light Name Zach Stevenson Username Dewaddict6 dested Zach Stenerson
analog leftover player-stubs/Zach_Stenerson.wiki. Pack player-stubs/Zach_Stenerson.wiki.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Zach Stenerson"
USERNAME = "Dewaddict6"
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 73
DS_PAGE = 72
LS_SCAN = "2012 US Nationals Day 1 Zach Stenerson LS.png"
DS_SCAN = "2012 US Nationals Day 1 Zach Stenerson DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox. Name Zach Stevenson dested Zach Stenerson analog leftover "
    "player-stubs/Zach_Stenerson.wiki. Username Dewaddict6. Event Date 6/9/12 Event Name US Nationals. "
    "Do not dest as a new person."
)
LS_NOTE = (
    "Handwritten 2010 Xerox. Name Zach Stevenson dested Zach Stenerson analog leftover player-stubs. "
    "Username Dewaddict6. LIGHT checked. Event Date 6/9/12 Event Name US Nationals. "
    "Deck Name City of Scumptown stays off the article. "
    "LS_START Communing True analog leftover Echeverria. "
    "AFA dested Anger, Fear, Aggression True analog leftover Nelson IN THE 60. "
    "Slave DSG dested Tatooine: Slave Quarters analog leftover Baroni. "
    "Commando Training & Klor dested Commando Training & K'lor'slug True analog leftover Baroni. "
    "Home 1: War Room dested Home One: War Room analog leftover Anderson. "
    "Tat: Obi's Hut dested Tatooine: Obi-Wan's Hut True analog leftover. "
    "Tatooine (EP1) dested Tatooine analog leftover. "
    "Chewie Enraged dested Chewbacca, Enraged True analog leftover x4. "
    "Luke Skywalker, Rebel Hero True analog leftover x3. "
    "Han w/ Blaster dested Han With Heavy Blaster Pistol analog leftover. "
    "Lando, Scoundrel dested Lando Calrissian, Scoundrel True analog leftover Simmering. "
    "Leia, Rebel Princess dested analog leftover Anderson. "
    "Padme Naberrie dested Padmé Naberrie True analog leftover Schoenthal. "
    "Threepio w/ Parts dested Threepio With His Parts Showing analog leftover Olson. "
    "Clone One dested Lone Operative analog leftover. "
    "Wedge in RSQ 1 dested Wedge In Red Squadron 1 True analog leftover Simmering. "
    "Artoo in RS dested Artoo-Detoo In Red 5 analog leftover Bordier. "
    "Protector dested Protector analog leftover Pietruszewski. "
    "Hear Me Baby dested Hear Me Baby, Hold Together True analog leftover. "
    "Bith Shuffle combo dested The Bith Shuffle & Desperate Reach analog leftover Nelson True + empty stay separate. "
    "IL-(6) dested I've Lost Artoo! True analog leftover Echeverria. "
    "Shield 12 Weapons Display dested analog leftover Simmering. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name Zach Stevenson dested Zach Stenerson analog leftover player-stubs. "
    "Username Dewaddict6. DARK checked. Event Date 6/9/12 Event Name US Nationals. "
    "Deck Name Prof. Oak's Spice Girls stays off the article. "
    "DS_START Kessel dested Kessel / Spice Mines Of Kessel analog leftover Finley. "
    "Combat Readiness dested Combat Readiness True analog leftover Finley. "
    "Kessel: Spice Office dested Kessel: Spice Mines - Administrator's Office True analog leftover Finley. "
    "Kessel: Spice Mines-Extraction dested Kessel: Spice Mines - Extraction Facility True analog leftover Finley. "
    "Kessel: Spice Mines Prison dested Kessel: Spice Mines - Prison True analog leftover Finley. "
    "Front Drive Yards dested Kuat Drive Yards True analog leftover Hanson. "
    "Maul w/ Stick dested Darth Maul With Lightsaber analog leftover Finley x2. "
    "Vader w/ Stick dested Darth Vader With Lightsaber analog leftover Finley. "
    "Mara w/ Stick dested Mara Jade With Lightsaber analog leftover Simmering. "
    "Emperor's Reach dested Maarek Stele, The Emperor's Reach True analog leftover MPC Bollentino. "
    "Grotto Warrior dested Grotto Werribee True analog leftover Pinto. "
    "Spice Admin dested Spice Mine Administrator True analog leftover Finley x2. "
    "4-LOM w/ Gun dested 4-LOM With Concussion Rifle True analog leftover Simmering. "
    "Line 33 crossed Blizzard 4 dests the replacement Blizzard 4 True analog leftover. "
    "Publo. Failure dested Public Execution True analog leftover dest-as-written slang. "
    "Spice Mines O' Kessel dested Kessel / Spice Mines Of Kessel True analog leftover Finley unique overcount mixed-V IN THE 60. "
    "Lat Dam dested Lateral Damage analog leftover TMW Banger. "
    "Control & STS dested Control & Set For Stun analog leftover Amato. "
    "Sniper & Dark Strike dested analog leftover Shannon Alderaan. "
    "Surprise dested Surprise analog leftover Peterson. "
    "MM&EO dested Masterful Move & Endor Occupation analog leftover. "
    "Kessel Surveillance dested Kessel Surveillance System True analog leftover Finley. "
    "Spice Mine Ops dested Spice Mine Operations True analog leftover Finley. "
    "K&D dested Knowledge And Defense True analog leftover Cooleo IN THE 60. "
    "Shield Coward dested Come Here You Big Coward analog leftover. "
    "Shield YCNHF dested You Cannot Hide Forever True analog leftover. "
    "Shield TINT dested There Is No Try True analog leftover. "
    "Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Slave Quarters"),
    n("Master Kenobi", True),
    n("Communing", True),
    n("Wokling", True),
    n("Commando Training & K'lor'slug", True),
    n("Home One: War Room"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: Cantina"),
    n("Tatooine"),
    n("Chewbacca, Enraged", True, qty=4),
    n("Luke Skywalker, Rebel Hero", True, qty=3),
    n("Yoda, Great Warrior", True),
    n("Admiral Ackbar", True),
    n("Han With Heavy Blaster Pistol"),
    n("Lando Calrissian, Scoundrel", True),
    n("Leia, Rebel Princess"),
    n("Corran Horn"),
    n("Padmé Naberrie", True),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Lone Operative"),
    n("Spiral"),
    n("Wedge In Red Squadron 1", True),
    n("Artoo-Detoo In Red 5"),
    n("Chewie's Bowcaster"),
    n("Luke's Blaster Pistol", True),
    n("Landing Claw"),
    n("I Hope She's Alright"),
    n("Security Control"),
    n("Honor Of The Jedi"),
    n("Rebel Gunrunner", True),
    n("Launching The Assault"),
    n("Draw Their Fire"),
    n("Strike Force", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Hindsight", True),
    n("Houjix"),
    n("Grimtaash"),
    n("Wookiee Roar", True, qty=2),
    n("Protector"),
    n("Use The Force", True, qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Hear Me Baby, Hold Together", True),
    n("The Bith Shuffle & Desperate Reach", True),
    n("The Bith Shuffle & Desperate Reach"),
    n("Run Luke Run", True, qty=2),
    n("Escape Pod", True, qty=2),
    n("I've Lost Artoo!", True),
]
LS_SHIELDS = [
    n("Chasm"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again"),
    n("The Professor", True),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("Aim High"),
    n("Weapons Display", True),
]
LS_ADD = []

DS_START = "Kessel / Spice Mines Of Kessel"
DS_CARDS = [
    n("Kessel / Spice Mines Of Kessel"),
    n("Combat Readiness", True),
    n("Kessel: Spice Mines - Administrator's Office", True),
    n("Endor Shield", True),
    n("Kuat Drive Yards", True),
    n("I'll Take Them Myself", True),
    n("Kessel: Spice Mines - Extraction Facility", True),
    n("Kessel: Spice Mines - Prison", True),
    n("Endor"),
    n("Kashyyyk"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Darth Vader With Lightsaber"),
    n("Mara Jade With Lightsaber"),
    n("Grand Moff Tarkin", True),
    n("Grand Admiral Thrawn"),
    n("Admiral Ozzel"),
    n("General Veers", True),
    n("Maarek Stele, The Emperor's Reach", True),
    n("Grotto Werribee", True),
    n("Spice Mine Administrator", True, qty=2),
    n("4-LOM With Concussion Rifle", True),
    n("U-3PO"),
    n("Conquest", True),
    n("Thunderflare"),
    n("Accuser"),
    n("Blockade Support Ship", True),
    n("Victory", True, qty=2),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4", True),
    n("Search And Destroy"),
    n("Public Execution", True),
    n("Kessel / Spice Mines Of Kessel", True),
    n("Lateral Damage"),
    n("Security Precautions"),
    n("Image Of The Dark Lord", True),
    n("Control & Set For Stun"),
    n("Ghhhk"),
    n("Monnok"),
    n("Sniper & Dark Strike"),
    n("Close Call", True, qty=3),
    n("Surprise"),
    n("You Are Beaten"),
    n("Imperial Barrier"),
    n("Overload"),
    n("Gravity Shadow"),
    n("A Dark Time For The Rebellion", True),
    n("Imperial Command", qty=2),
    n("Cold Feet", True),
    n("Masterful Move & Endor Occupation"),
    n("Kessel Surveillance System", True),
    n("Spice Mine Operations", True),
    n("Battle Deployment"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Oppressive Enforcement"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("Firepower", True),
    n("Abyss", True),
    n("Fanfare", True),
    n("Battle Order", True),
    n("Resistance", True),
    n("There Is No Try", True),
]
DS_ADD = []
