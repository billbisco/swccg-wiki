#!/usr/bin/env python3
"""2012 Yavin 4 Regionals leftover Xerox: Matt Schmaltz.

Source: Yavin42012.pdf pages 16–17.
p16 Dark handwritten 2010 Xerox / p17 Light handwritten 2010 Xerox.
Name Matt Schmaltz dested Matt Schmaltz analog leftover generate_2013_mpc.py
CANON Schwartz / Username dashmudtz / player-stubs/Matt_Schmaltz.wiki.
Username Dashmudtz dested USERNAME. Email Atlasraf@... dested identity evidence only.
Pack player-stubs/Matt_Schmaltz.wiki.
Do not dest as Schwartz. Do not dest as a new person.
Do not dest 2013 MPC / 2014 MPC / 2014 Philadelphia Matt Schmaltz 60s again.
"""
from __future__ import annotations

PLAYER = "Matt Schmaltz"
USERNAME = "Dashmudtz"
STAGE = ""
PDF = "2012 Yavin 4 Regionals.pdf"
LS_PAGE = 17
DS_PAGE = 16
LS_SCAN = "2012 Yavin 4 Regionals Matt Schmaltz LS.png"
DS_SCAN = "2012 Yavin 4 Regionals Matt Schmaltz DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "p16 Dark handwritten 2010 Xerox / p17 Light handwritten 2010 Xerox. "
    "Name Matt Schmaltz dested Matt Schmaltz analog leftover generate_2013_mpc.py "
    "CANON Schwartz / Username dashmudtz / player-stubs/Matt_Schmaltz.wiki. "
    "Username Dashmudtz dested USERNAME. Email Atlasraf@... dested identity evidence only. "
    "Event Date 06/30/12 Event Name Regionals dest Yavin 4 facing pair analog leftover Orthner. "
    "Do not dest as Schwartz. Do not dest as a new person. "
    "Do not dest 2013 MPC / 2014 MPC / 2014 Philadelphia Matt Schmaltz 60s again. "
    "Pack player-stubs/Matt_Schmaltz.wiki."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p17 Light. Name Matt Schmaltz Username Dashmudtz. "
    "Event Date 06/30/12 Event Name Regionals dest Yavin 4 facing pair. "
    "LIGHT checked. Line 1 Tatooine: Slave Quarters dest START analog leftover Nathan no-objective. "
    "Commando Training & K'lor'slug dested analog leftover TMW Joe. "
    "Tatooine (Cor) dested Tatooine (Coruscant) analog leftover TYPE_OVERRIDE. "
    "Luke Skywalker, Rebel Hero True qty=3 analog leftover consecutive. "
    "Chewbacca, Protector empty qty=2 analog leftover TYPE_OVERRIDE. "
    "Chewie, Enraged True qty=2 analog leftover TMW Joe. "
    "Leia, Rebel Princess dested analog leftover Brady. "
    "Lando Calrissian, Scoundrel dested analog leftover Westergard. "
    "Han with Heavy Blaster Pistol dested Han With Heavy Blaster Pistol analog leftover Orthner. "
    "Blind Jedi dested analog leftover TYPE_OVERRIDE. "
    "Wedge in Red Squadron 1 dested Wedge In Red Squadron 1 analog leftover Stenerson. "
    "Artoo-Detoo in Red 5 dested Artoo-Detoo In Red 5 analog leftover Hendon. "
    "Rebel Gunrunner dested analog leftover TYPE_OVERRIDE. "
    "Security Breach dested analog leftover extra L40 True. "
    "Strikeforce dested analog leftover TYPE_OVERRIDE. "
    "Houjix empty qty=2. Escape Pod True qty=2 analog leftover TYPE_OVERRIDE. "
    "Run Luke, Run! True qty=2 analog leftover TYPE_OVERRIDE. "
    "The Bith Shuffle & Desperate Reach empty qty=2. "
    "Rebel Leadership True qty=2. Use The Force True qty=2. "
    "Shields 1–11 filled shield 12 empty skip analog leftover Dwyer. Unique 60 shields 11."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p16 Dark. Name Matt Schmaltz Username Dashmudtz. "
    "Event Date 06/30/12 Event Name Regionals dest Yavin 4 facing pair. DARK checked. "
    "This Deal Is Getting Worse All The Time dested analog leftover 2014 Philadelphia Schmaltz. "
    "Imperial Arrest Order & Secret Plans dested analog leftover Cooleo. "
    "They Must Never Again Leave This City crossed dest TILT + 06 analog leftover crossed-with-replacement dest as written. "
    "Darth Maul with Lightsaber empty qty=2. Darth Vader with Lightsaber empty qty=2. "
    "Kir Kanos with Force Pike dested Kir Kanos With Force Pike analog leftover typical. "
    "Garindan dested analog leftover TYPE_OVERRIDE garidan. "
    "P-13 & P-14 dested analog leftover TYPE_OVERRIDE. "
    "4-LOM with Concussion Rifle dested 4-LOM With Concussion Rifle analog leftover TMW Joe. "
    "The Emperor dested analog leftover TMW Shaw. "
    "The Emperor's Sword crossed dest Accuser analog leftover crossed-with-replacement. "
    "Battle Deployment dested analog leftover extra L40. "
    "Imperial Propaganda True qty=2. "
    "A Dark Time For The Rebellion True qty=4 unique overcount sheet-accurate. "
    "Operational As Planned True qty=4 unique overcount sheet-accurate. "
    "Ghhhk & Those Rebels Won't Escape Us dested analog leftover TMW Joe qty=2. "
    "Control & Set For Stun dested analog leftover Westergard. "
    "Oppressive Enforcement crossed dest Wipe Them Out, All Of Them analog leftover Massung AOT True. "
    "We'll Let Fate-a Decide, Huh? dested We'll Let Fate Decide, Huh analog leftover TYPE_OVERRIDE. "
    "Shields 1–11 filled shield 12 empty skip analog leftover Dwyer. Unique 60 shields 11."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Tatooine: Slave Quarters"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing", True),
    n("Commando Training & K'lor'slug", True),
    n("Wokling", True),
    n("Master Kenobi", True),
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Tosche Station"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine: City Outskirts"),
    n("Tatooine (Coruscant)"),
    n("Luke Skywalker, Rebel Hero", True, qty=3),
    n("Chewbacca, Protector", qty=2),
    n("Chewie, Enraged", True, qty=2),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Lando Calrissian, Scoundrel", True),
    n("Han With Heavy Blaster Pistol"),
    n("Admiral Ackbar", True),
    n("Blind Jedi", True),
    n("Yoda, Great Warrior", True),
    n("Shmi Skywalker"),
    n("Padme Naberrie", True),
    n("Threepio With His Parts Showing"),
    n("IL-19", True),
    n("Wedge In Red Squadron 1", True),
    n("Spiral"),
    n("Home One"),
    n("Artoo-Detoo In Red 5"),
    n("Chewbacca's Bowcaster"),
    n("Luke's Blaster Pistol", True),
    n("Landing Claw"),
    n("Hindsight", True),
    n("Launching The Assault"),
    n("Rebel Gunrunner", True),
    n("Honor Of The Jedi"),
    n("Security Breach", True),
    n("I Hope She's All Right"),
    n("Draw Their Fire"),
    n("Strikeforce", True),
    n("Grimtaash"),
    n("Houjix", qty=2),
    n("Escape Pod", True, qty=2),
    n("Run Luke, Run!", True, qty=2),
    n("The Bith Shuffle & Desperate Reach", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("Rebel Leadership", True, qty=2),
    n("Use The Force", True, qty=2),
    n("Protector"),
    n("Wookiee Roar", True),
    n("On The Edge"),
]
LS_SHIELDS = [
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Battle Plan"),
    n("Simple Tricks And Nonsense", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Ultimatum"),
    n("Wise Advice"),
    n("Aim High"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "This Deal Is Getting Worse All The Time"
DS_CARDS = [
    n("This Deal Is Getting Worse All The Time"),
    n("Cloud City: Downtown Plaza"),
    n("The Emperor", True),
    n("According To My Design", True),
    n("Imperial Arrest Order & Secret Plans"),
    n("I'm Sorry"),
    n("I'll Take Them Myself", True),
    n("TILT + 06"),
    n("Knowledge And Defense", True),
    n("Cloud City: Dining Room", True),
    n("Cloud City: West Gallery"),
    n("Bespin", True),
    n("Darth Maul With Lightsaber", qty=2),
    n("Admiral Ozzel"),
    n("Grand Admiral Thrawn"),
    n("Ice-Heart", True),
    n("Darth Vader With Lightsaber", qty=2),
    n("Sim Aloo"),
    n("Kir Kanos With Force Pike", True),
    n("Captain Piett", True),
    n("Janus Greejatus"),
    n("ISB Sector Commander", True),
    n("Arica", True),
    n("Trooper Jerrol Blendin"),
    n("Garindan", True),
    n("J'Quille", True),
    n("Shada", True),
    n("Boba Fett, Bounty Hunter", True),
    n("P-13 & P-14", True),
    n("4-LOM With Concussion Rifle"),
    n("Probot", True),
    n("OOM-9", True),
    n("Executor"),
    n("Dengar In Punishing One"),
    n("The Emperor's Shield"),
    n("Accuser"),
    n("Chimaera"),
    n("Battle Deployment"),
    n("Altering The Deal"),
    n("Dark Deal"),
    n("Sundown"),
    n("Expand The Empire"),
    n("Something Special Planned For Them", True),
    n("I Want Every Part Of The Ship Checked", True),
    n("Imperial Propaganda", True, qty=2),
    n("Lateral Damage"),
    n("A Dark Time For The Rebellion", True, qty=4),
    n("Operational As Planned", True, qty=4),
    n("Ghhhk & Those Rebels Won't Escape Us", qty=2),
    n("Control & Set For Stun"),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Wipe Them Out, All Of Them", True),
    n("Battle Order"),
    n("Resistance"),
    n("Do They Have A Code Clearance?", True),
    n("We'll Let Fate Decide, Huh", True),
]
DS_ADD = []
