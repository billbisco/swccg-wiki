#!/usr/bin/env python3
"""2014 Alderaan Regionals Xerox: Gabe (Babomb dude).

Source: 2014-Alderaan-Regionals.pdf pages 15–16 (2010 form).
Name Gabe dested existing first-name-only SoCal Gabe stub. Username Babomb dude.
"""
from __future__ import annotations

PLAYER = "Gabe"
USERNAME = "Babomb dude"
STAGE = ""
PDF = "2014 Alderaan Regionals.pdf"
LS_PAGE = 15
DS_PAGE = 16
LS_SCAN = "2014 Alderaan Regionals p15 Gabe LS.png"
DS_SCAN = "2014 Alderaan Regionals p16 Gabe DS.png"
NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Gabe dested existing SoCal stub. Username Babomb dude. "
    "LS Watch Your Step (Deck Name Fort Knox) / DS Agents Of Black Sun (Deck Name AOBS). "
    "WYS empty dested Watch Your Step / This Place Can Be A Little Rough without True. "
    "AOBS empty dested Agents Of Black Sun / Vengeance Of The Dark Prince without True. "
    "AFA dested Anger, Fear, Aggression. "
    "HFTMF dested Heading For The Medical Frigate. "
    "LS, JK dested Luke Skywalker, Jedi Knight. "
    "Lando UH dested Lando Calrissian, Unlikely Hero. "
    "SATM + BP dested Sorry About The Mess & Blaster Proficiency. "
    "Control + Tunnel Vision dested Control & Tunnel Vision. "
    "Control + SFS dested Control & Set For Stun. "
    "Cantina dested Tatooine: Cantina. "
    "Docking Bay 94 dested Tatooine: Docking Bay 94. "
    "Tatooine (Pre) dested Tatooine. "
    "Tat: Mos Eisley (Pre) dested Tatooine: Mos Eisley. "
    "3PO parts out dested Threepio With His Parts Showing. "
    "BoShek BS dested BoShek, Brash Smuggler. "
    "Lady luck dested Lady Luck. "
    "Chewie bowcaster dested Chewbacca's Bowcaster. "
    "Obi Journal dested Obi-Wan's Journal. "
    "Luke's Saber dested Luke's Lightsaber. "
    "Sai'torr dested Sai'torr Kal Fas. "
    "DoDN dested Do, Or Do Not. "
    "YISYW dested Your Insight Serves You Well. "
    "K+D dested Knowledge And Defense. "
    "Twilek Advisor dested Twi'lek Advisor. "
    "Scum + Villainy dested Scum And Villainy. "
    "IG-88 w/ Riot Gun dested IG-88 With Riot Gun. "
    "Boba Fett PH dested Boba Fett, Prepared Hunter. "
    "Boba Fett BH dested Boba Fett, Bounty Hunter. "
    "Datoo Kart dested as written (NO_DEST). "
    "Greedo With Blaster Rifle dested Greedo with Blaster Pistol. "
    "Elis Hinthra dested Elis In Hinthra. "
    "Dengar w/ Blaster dested Dengar With Blaster Carbine. "
    "4-LOM w/ Gun dested 4-LOM With Concussion Rifle. "
    "Slave I SOF dested Slave I, Symbol Of Fear. "
    "Mando Armor dested Mandalorian Armor. "
    "Look Sir, Droid dested Look Sir, Droids. "
    "Oh Switch Off dested Oh, Switch Off. "
    "Ghhhk & TRUEU dested Ghhhk & Those Rebels Won't Escape Us. "
    "Flagship Bridge dested Blockade Flagship: Bridge. "
    "Cor's Docking Bay dested Coruscant: Docking Bay. "
    "Security Tower dested Cloud City: Security Tower. "
    "CHYBC dested Come Here You Big Coward. "
    "TINT dested There Is No Try. "
    "YCHF dested You Cannot Hide Forever. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "We'll let Fate-a dested We'll Let Fate-a Decide, Huh?. "
    "Shield 7 The Professor crossed, skipped. "
    "(V) from the checkbox. Unique overcounts sheet-accurate."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine"),
    n("Anger, Fear, Aggression", True),
    n("Heading For The Medical Frigate"),
    n("Rycar Ryjerd", True),
    n("Insurrection"),
    n("Quick Draw", True),
    n("Luke Skywalker, Jedi Knight", qty=5),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Chewie, Enraged", True, qty=2),
    n("Han Solo, Innocent Scoundrel", qty=2),
    n("Melas", True),
    n("Wedge Antilles", True),
    n("Mirax Terrik"),
    n("Talon Karrde"),
    n("BoShek, Brash Smuggler"),
    n("Kyle Katarn"),
    n("Threepio With His Parts Showing"),
    n("Sergeant Doallyn", True),
    n("Lady Luck", qty=2),
    n("Booster In Pulsar Skate"),
    n("Luke's Lightsaber"),
    n("Black Market Blaster"),
    n("Chewbacca's Bowcaster"),
    n("Obi-Wan's Journal"),
    n("Luke's Bionic Hand"),
    n("Smuggler's Blues", True),
    n("Sai'torr Kal Fas", True),
    n("Lightsaber Proficiency"),
    n("Temporary Foothold"),
    n("I'll Take The Leader"),
    n("Punch It!"),
    n("On The Edge"),
    n("Blaster Deflection", qty=2),
    n("Escape Pod", True),
    n("Were You Looking For Me"),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("It Could Be Worse"),
    n("Houjix"),
    n("All Wings Report In & Darklighter Spin"),
    n("Rebel Barrier"),
    n("Control & Tunnel Vision"),
    n("Imperial Atrocity", True),
    n("Tatooine: Mos Eisley"),
    n("Corellia", True),
    n("Spaceport Docking Bay"),
    n("Home One: Docking Bay"),
]
LS_SHIELDS = [
    n("Jabba's Prize"),
    n("Affect Mind"),
    n("Yavin Sentry"),
    n("Do, Or Do Not"),
    n("Planetary Defenses", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Battle Plan"),
    n("Aim High"),
]
LS_ADD = [
    n("Don't Do That Again"),
    n("A Tragedy Has Occurred"),
    n("Weapons Display"),
    n("Chasm"),
]


DS_START = "Agents Of Black Sun / Vengeance Of The Dark Prince"
DS_CARDS = [
    n("Agents Of Black Sun / Vengeance Of The Dark Prince"),
    n("Coruscant: Imperial City"),
    n("Prince Xizor", True),
    n("Coruscant"),
    n("Knowledge And Defense"),
    n("Twi'lek Advisor", True),
    n("Information Exchange", True),
    n("Scum And Villainy"),
    n("Jabba's Haven"),
    n("Bossk", True),
    n("IG-88 With Riot Gun"),
    n("Greedo", True),
    n("Vigo"),
    n("Vigo", True),
    n("Boba Fett, Prepared Hunter"),
    n("Greedo with Blaster Pistol"),
    n("Ponda Baba", True),
    n("Dr. Evazan"),
    n("Datoo Kart", True),
    n("Datoo Kart"),
    n("Boba Fett, Bounty Hunter"),
    n("Jabba The Hutt", True),
    n("Guri"),
    n("OOM-9", True),
    n("Velken Tezeri", True),
    n("Dengar With Blaster Carbine", True),
    n("4-LOM With Concussion Rifle", True),
    n("Slave I, Symbol Of Fear", True),
    n("Zuckuss"),
    n("Elis In Hinthra"),
    n("Den Of Thieves", True),
    n("Ket Maliss", True),
    n("Disarmed", qty=2),
    n("Protocol Failure"),
    n("Mandalorian Armor", True),
    n("Feltipern Trevagg", True),
    n("Look Sir, Droids"),
    n("Sonic Bombardment", True, qty=2),
    n("Control & Set For Stun"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Imperial Barrier"),
    n("They're Still Coming Through"),
    n("Imbalance & Kintan Strider"),
    n("Hidden Weapons", qty=2),
    n("Oh, Switch Off"),
    n("Lightsaber Deficiency", True),
    n("Unexpected Interruption"),
    n("Cease Fire!"),
    n("Blow Parried"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Lana Dobreed & Sacrifice"),
    n("Spaceport Docking Bay"),
    n("Nal Hutta"),
    n("Blockade Flagship: Bridge"),
    n("Coruscant: Docking Bay"),
    n("Cloud City: Security Tower", True),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever"),
    n("Fanfare", True),
    n("Death Star Sentry"),
    n("Come Here You Big Coward"),
    n("There Is No Try"),
    n("I Find Your Lack Of Faith Disturbing"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture"),
    n("Battle Order"),
    n("Secret Plans"),
    n("Resistance"),
]
DS_ADD = [
    n("Firepower"),
    n("Allegations Of Corruption"),
    n("Abyss"),
]
