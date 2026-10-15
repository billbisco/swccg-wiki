#!/usr/bin/env python3
"""2015 European Championship leftover Xerox: Marc Nickels Day 2 (place 7).

Source: SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf p16 Dark / p17 Light (handwritten PC forms).
"""
from __future__ import annotations

PLAYER = "Marc Nickels"
USERNAME = "Darkbow"
STAGE = "Day 2"
PDF = "2015 European Championship Day 2 Place 01-17.pdf"
LS_PAGE = 17
DS_PAGE = 16
LS_SCAN = "2015 European Championship Marc Nickels LS.png"
DS_SCAN = "2015 European Championship Marc Nickels DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Place 7 circled. p16 Dark / p17 Light handwritten PC forms. Event Name 'Europeans'. "
    "DS name box 'Marc Nickels', LS name box 'MARC'. Usernames differ: DS 'Darkbow' (handwriting, could be 'Darkbeo') used; LS 'FATBOY'. "
    "DS 4:0 / LS 2:2. Sheet deck name DS 'Violence!' (not used as DECK_NAME); LS blank."
)
LS_NOTE = (
    "START Watch Your Step / This Place Can Be A Little Rough (sheet 'Watch Your Step/This Place Can..'). "
    "Posted Naboo Boss Nass Chambers dested Naboo: Boss Nass' Chambers. Posted Here Me Baby Hold Together dested Hear Me Baby, Hold Together. "
    "Posted Lukes Lightsabers dested Luke's Lightsaber. Posted Lukes Bionic Hand dested Luke's Bionic Hand. "
    "Posted Obi Wan Kenobi dested Obi-Wan Kenobi (lines 19, 23, both (V)). Posted Melas x2 (V) dested Melas. "
    "Posted Dodge kept. Posted Wesa Got A Grand Army dested Wesa Gotta Grand Army x3. "
    "Posted SATHM + Blasters Proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "Posted Obi Wans Journal dested Obi-Wan's Journal. Posted OOC + Transmission Terminated dested Out Of Commission & Transmission Terminated. "
    "Posted Antilles Maneuver kept. Posted All Wings Report In & DS dested All Wings Report In & Darklighter Spin. "
    "Posted Obi Wans Lightsaber dested Obi-Wan's Lightsaber. Posted A Jedis Concentration dested A Jedi's Concentration. "
    "Posted Millenium Falcon dested Millennium Falcon. Posted Capt Han Solo dested Captain Han Solo. "
    "Posted Pulsar Skate kept. Posted Out Rider dested Outrider. Posted Anger Fear Agression dested Anger, Fear, Aggression. "
    "Luke Skywalker, Jedi Knight x4 and Talon Karrde x2 unique overcounts sheet-accurate. "
    "Shields: Jabbas Prize dested Jabba's Prize; Do or Do Not kept; line 15 'Your Insight Serves You Well' crossed out "
    "(duplicate of 13), replacement The Republic No Longer Functions. No (V) marks on shields. Main 60, shields 15."
)
DS_NOTE = (
    "START Bring Him Before Me / Take Your Father's Place. "
    "Posted Death Star 2 Throne Room dested Death Star II: Throne Room. Posted 4-Lom w/Concussion Rifle dested 4-LOM With Concussion Rifle. "
    "Posted Cloud City Security Tower dested Cloud City: Security Tower. Posted Blockade Flagship Bridge dested Blockade Flagship: Bridge. "
    "Posted Dagobah Cave dested Dagobah: Cave. Posted Sniper + Dark Strike dested Sniper & Dark Strike. "
    "Posted Masterful Move Endor Occupation dested Masterful Move & Endor Occupation. "
    "Posted Ghhhk + Those Rebels Won't Escape Us dested Ghhhk & Those Rebels Won't Escape Us. Posted IG 88 in IG 2000 dested IG-88 In IG-2000. "
    "Posted Darth Maul w/Lightsaber x3 dested Darth Maul With Lightsaber. Posted Darth Vader w/Lightsaber x2 dested Darth Vader With Lightsaber. "
    "Posted Dengar w/ Blaster Carbine dested Dengar With Blaster Carbine. Posted Janus Greejatus kept. "
    "Posted Knowledge + Defence dested Knowledge And Defense. "
    "Unique overcounts sheet-accurate (Mara Jade WL x2, Count Dooku x2, Maul WL x3, Vader WL x2, DVDLOTS x2). "
    "Shields: line 2 'Weapon of' crossed out, replacement A Useless Gesture (V); Imperial Detenti.. dested Imperial Detention. "
    "Main 60, shields 15."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Naboo: Boss Nass' Chambers"),
    n("Like My Father Before Me", True),
    n("Wokling", True),
    n("Squadron Assignments"),
    n("Tatooine"),
    n("Tatooine: Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Luke Skywalker, Jedi Knight", qty=4),
    n("On The Edge"),
    n("Heading For The Medical Frigate"),
    n("Control & Tunnel Vision", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Luke's Lightsaber"),
    n("Dash Rendar"),
    n("Luke's Bionic Hand", True),
    n("Tatooine: Mos Eisley"),
    n("Kessel"),
    n("Obi-Wan Kenobi", True, qty=2),
    n("Talon Karrde", qty=2),
    n("Tatooine Celebration"),
    n("Moving To Attack Position"),
    n("Melas", True, qty=2),
    n("I'll Take The Leader"),
    n("Dodge"),
    n("Force Levitation", True),
    n("Wesa Gotta Grand Army", qty=3),
    n("Free Ride & Endor Celebration"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Escape Pod", True),
    n("Obi-Wan's Journal"),
    n("Out Of Commission & Transmission Terminated"),
    n("Don't Get Cocky"),
    n("Antilles Maneuver", True),
    n("Chewbacca, Protector"),
    n("All Wings Report In & Darklighter Spin"),
    n("Obi-Wan's Lightsaber"),
    n("A Few Maneuvers"),
    n("Civil Disorder", True),
    n("A Jedi's Concentration"),
    n("Yotts Orren"),
    n("Ounee Ta"),
    n("Houjix"),
    n("Millennium Falcon"),
    n("Captain Han Solo"),
    n("Lando Calrissian", True),
    n("Pulsar Skate"),
    n("Wedge Antilles", True),
    n("Mirax Terrik"),
    n("Outrider"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Don't Do That Again"),
    n("Aim High"),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Ultimatum"),
    n("Weapons Display"),
    n("Jabba's Prize"),
    n("Do, Or Do Not"),
    n("He Can Go About His Business"),
    n("Your Insight Serves You Well"),
    n("Affect Mind"),
    n("The Republic No Longer Functions"),
]
LS_ADD = []

DS_START = "Bring Him Before Me / Take Your Father's Place"
DS_CARDS = [
    n("Bring Him Before Me / Take Your Father's Place"),
    n("Death Star II: Throne Room"),
    n("Your Destiny"),
    n("Insignificant Rebellion"),
    n("4-LOM With Concussion Rifle", True),
    n("Cloud City: Security Tower", True),
    n("Any Methods Necessary"),
    n("Blockade Flagship: Bridge"),
    n("Dagobah: Cave"),
    n("We Must Accelerate Our Plans", qty=3),
    n("I Have You Now", qty=2),
    n("Force Lightning", qty=2),
    n("Maul Strikes", qty=2),
    n("Force Field", True, qty=2),
    n("Sniper & Dark Strike"),
    n("The Circle Is Now Complete"),
    n("Masterful Move & Endor Occupation"),
    n("Limited Resources"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Force Push"),
    n("Zuckuss In Mist Hunter"),
    n("IG-88 In IG-2000"),
    n("Maul's Sith Infiltrator", qty=2),
    n("Presence Of The Force", qty=2),
    n("The Phantom Menace", qty=2),
    n("First Strike"),
    n("Crush The Rebellion"),
    n("Expand The Empire"),
    n("No Escape"),
    n("Emperor's Power"),
    n("Grand Moff Tarkin", True),
    n("Mara Jade With Lightsaber", qty=2),
    n("Darth Sidious"),
    n("Count Dooku", qty=2),
    n("Darth Maul With Lightsaber", qty=3),
    n("Darth Vader With Lightsaber", qty=2),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Emperor Palpatine"),
    n("Sith Probe Droid", True),
    n("Probot"),
    n("Jango Fett"),
    n("Boba Fett, Bounty Hunter"),
    n("Dengar With Blaster Carbine", True),
    n("Janus Greejatus"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Secret Plans"),
    n("Fanfare"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?"),
    n("Imperial Detention"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Resistance"),
    n("Allegations Of Corruption"),
    n("You Cannot Hide Forever"),
    n("Vote Of No Confidence"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("Death Star Sentry"),
]
DS_ADD = []
