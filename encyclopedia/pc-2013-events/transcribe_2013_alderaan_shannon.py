#!/usr/bin/env python3
"""2013 Alderaan Regionals: Kevin Shannon handwritten 2010 Xerox LS+DS.

Name field Shannon. Username blank. Dest Kevin Shannon.
Do not dest as a new person. Do not rewrite Worlds / SoCal Shannon leftovers.
"""
from __future__ import annotations

PLAYER = "Kevin Shannon"
USERNAME = ""
STAGE = ""
PDF = "2013 Alderaan Regionals.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2013 Alderaan Regionals p08 Kevin Shannon LS.png"
DS_SCAN = "2013 Alderaan Regionals p07 Kevin Shannon DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional empty). Name Shannon dested "
    "Kevin Shannon. Username blank. Deck Name I made this in my car on the way here. "
    "LIGHT/DARK empty; dest Light from QMC. QMC empty dested Quiet Mining Colony / "
    "Independent Operation without True. Heading dested Heading For The Medical Frigate True. "
    "Guest Quarters dested Cloud City: Guest Quarters. Urchins Combo dested Urchins. "
    "Yeppin dested Yeppin as written. Calder dested Calder as written. Tawus dested Tawss Khaa. "
    "Ayla dittos dested Aayla Secura. Sgt Edian dested Sergeant Edian. DTF dested Draw Their Fire. "
    "Lando Hero dittos dested Lando Calrissian, Unlikely Hero. Harc dested Harc Seff. "
    "Boosters Star Destroyer dested Boosters Star Destroyer as written. "
    "Ellorrs dested Ellorrs Madak. Leesub dested Leesub Sirln. "
    "Booster in Pulsar dested Booster In Pulsar Skate. Houjix Combo dittos dested "
    "Houjix & Out Of Nowhere. Overseer dested Overseer as written. Carding Claw dested "
    "Carding Claw as written. Wuttik dested Wuttik as written. Han Innocent dittos dested "
    "Han Solo, Innocent Scoundrel. GNASHAM dested GNASHAM as written. Imp Atrocity dested "
    "Imperial Atrocity. Path dested Path as written. West Gallery dested Cloud City: West Gallery. "
    "Uslony dested Uslony as written. Luxury Yacht dested Lady Luck. Path Combo dested "
    "Path Combo as written. Inc. Barriers dested Inc. Barriers as written. "
    "North Corridor dested North Corridor as written. BoShek dested BoShek, Brash Smuggler. "
    "All Wings Combo dested All Wings Report In & Darklighter Spin. Upper P.C. dested "
    "Cloud City: Upper Plaza Corridor. LTWW dested Let The Wookiee Win. EPP Luke dested "
    "Luke Skywalker With Lightsaber. YGALOCCA dested YGALOCCA as written. Combat dested "
    "Combat as written. Leia RP dested Leia, Rebel Princess. Free Ride Combo dested "
    "Free Ride & You'll Be Dead. Seeking dested Seeking An Audience True. AFA dested "
    "Anger, Fear, Aggression True. Shields empty. Additional empty. Unique overcounts "
    "sheet-accurate (Aayla Secura x2, Lando Unlikely Hero x2, Houjix combo x2, Han Innocent x2, "
    "Tawss Khaa x2). (V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional empty). Name Shannon dested "
    "Kevin Shannon. Username blank. Deck Name Some deck I found from last year. "
    "LIGHT/DARK empty; dest Dark from CCT. CCT empty dested Carbon Chamber Testing / "
    "My Kind Of Scum without True. Jabba Prize dested Jabba's Prize. Carbonite Chamber dested "
    "Cloud City: Carbonite Chamber. Security Tower dested Cloud City: Security Tower True. "
    "JP Dungeon dested Jabba's Palace: Dungeon. Carbon Console dested Carbonite Chamber Console True. "
    "4LOM w Gun dested 4-LOM With Concussion Rifle True. Boba Prepared Hunter dested "
    "Boba Fett, Prepared Hunter. EPP Maul dested Darth Maul With Lightsaber. Emperor dested "
    "Emperor Palpatine True. Darth Vader True dested Darth Vader, Dark Lord Of The Sith True. "
    "Victory dested Victory as written. Slave I SOF dested Slave I, Symbol Of Fear. "
    "Mandalorian Father dested Jango Fett, The Assassin. WMAOP dested We Must Accelerate Our Plans. "
    "Proto Failure dested Protocol Failure. Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "TPM dested TPM as written. BDS dested BDS as written. IG Neural Input dested "
    "IG Neural Input as written. EPP Vader dested Darth Vader With Lightsaber. EPP Mara dested "
    "Mara Jade With Lightsaber. Ghhhk Combo dested Ghhhk & Those Rebels Won't Escape Us. "
    "Any Lastwords dested Any Last Words as written. Sniper Combo dested Sniper & Dark Strike. "
    "Close Call dested Close Call True. Jabba Haven dested Jabba's Haven. Special Delivery dested "
    "Special Delivery True. THYN dested THYN as written. Maul Ship dested Sith Infiltrator True. "
    "GMT dested Grand Moff Tarkin True. Fine Artillery dested Fire Artillery as written. "
    "Def Fire dested Defensive Fire True. Tark Bounty dested Tarkin's Bounty True. "
    "Lightsaber Def dested Lightsaber Deficiency True. Flagship Bridge dested "
    "Blockade Flagship: Bridge. K+D dested Knowledge And Defense True. Shields empty. "
    "Additional empty. Unique overcounts sheet-accurate (Emperor Palpatine x2, EPP Maul x3, "
    "Stunning Leader x2, Disarmed x2, Sense x2, WMAOP x2, BDS x2). (V) from the checkbox; "
    "dittos inherit the first named line except where the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Heading For The Medical Frigate", True),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Urchins"),
    n("Lando Calrissian", True),
    n("Yeppin"),
    n("Calder"),
    n("Tawss Khaa", True),
    n("No Questions Asked"),
    n("Aayla Secura"),
    n("Aayla Secura"),
    n("Sergeant Edian", True),
    n("Draw Their Fire"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Harc Seff", True),
    n("Dash Rendar", True),
    n("Deneb Both"),
    n("Boosters Star Destroyer"),
    n("Ellorrs Madak", True),
    n("Leesub Sirln", True),
    n("Booster In Pulsar Skate"),
    n("Houjix & Out Of Nowhere"),
    n("Houjix & Out Of Nowhere"),
    n("Overseer"),
    n("Carding Claw"),
    n("Lobot", True),
    n("Melas", True),
    n("Blast Door Key"),
    n("Alter", True),
    n("Wuttik", True),
    n("Yoxgit", True),
    n("Han Solo, Innocent Scoundrel"),
    n("Han Solo, Innocent Scoundrel"),
    n("GNASHAM"),
    n("Imperial Atrocity", True),
    n("Path"),
    n("Cloud City: West Gallery"),
    n("Dark Approach", True),
    n("Uslony", True),
    n("Lady Luck"),
    n("Path Combo"),
    n("Inc. Barriers"),
    n("North Corridor"),
    n("Mirax Terrik"),
    n("BoShek, Brash Smuggler", True),
    n("Rebel Barrier"),
    n("All Wings Report In & Darklighter Spin"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Let The Wookiee Win"),
    n("Luke Skywalker With Lightsaber"),
    n("Tawss Khaa"),
    n("YGALOCCA"),
    n("Combat"),
    n("Leia, Rebel Princess"),
    n("Chewie"),
    n("Free Ride & You'll Be Dead"),
    n("Seeking An Audience", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = []
LS_ADD = []


DS_START = "Carbon Chamber Testing / My Kind Of Scum"
DS_CARDS = [
    n("Carbon Chamber Testing / My Kind Of Scum"),
    n("Jabba's Prize"),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: Security Tower", True),
    n("Jabba's Palace: Dungeon"),
    n("Despair", True),
    n("Carbonite Chamber Console", True),
    n("4-LOM With Concussion Rifle", True),
    n("Boba Fett, Prepared Hunter"),
    n("Darth Maul With Lightsaber"),
    n("Emperor Palpatine", True),
    n("Darth Vader, Dark Lord Of The Sith", True),
    n("Victory"),
    n("Slave I, Symbol Of Fear"),
    n("Jango Fett, The Assassin"),
    n("Nal Hutta"),
    n("We Must Accelerate Our Plans"),
    n("Dr. Evazan"),
    n("Disarmed"),
    n("Protocol Failure"),
    n("Jabba's Palace: Audience Chamber"),
    n("Alter", True),
    n("Force Field"),
    n("Stunning Leader"),
    n("TPM"),
    n("BDS"),
    n("IG Neural Input", True),
    n("Ree-Yees", True),
    n("First Strike"),
    n("IG-88", True),
    n("Mara Jade", True),
    n("Darth Vader With Lightsaber"),
    n("Mara Jade With Lightsaber"),
    n("Darth Maul With Lightsaber"),
    n("Emperor Palpatine", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Stunning Leader"),
    n("Any Last Words"),
    n("Sniper & Dark Strike"),
    n("No Escape"),
    n("Close Call", True),
    n("Jabba's Haven"),
    n("Special Delivery", True),
    n("BDS"),
    n("Darth Maul With Lightsaber"),
    n("Sense"),
    n("THYN"),
    n("Sith Infiltrator", True),
    n("Grand Moff Tarkin", True),
    n("Blow Parried"),
    n("Disarmed"),
    n("Fire Artillery"),
    n("Garindan", True),
    n("Defensive Fire", True),
    n("Tarkin's Bounty", True),
    n("Sense"),
    n("We Must Accelerate Our Plans"),
    n("Lightsaber Deficiency", True),
    n("Blockade Flagship: Bridge"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = []
DS_ADD = []
