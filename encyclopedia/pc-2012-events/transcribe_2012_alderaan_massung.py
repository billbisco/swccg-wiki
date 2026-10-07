#!/usr/bin/env python3
"""2012 Alderaan Regionals leftover Xerox: Anthony Massung.

Source: 2012AlderaanRegionals.pdf pages 3–4 (handwritten 2010 Xerox).
Name Anthony Massung dested Anthony Massung analog leftover 2013 Alderaan /
2014 Alderaan / 2013 SoCal / player-stubs/Anthony_Massung.wiki. Username blank.
p03 Light Watch Your Step. p04 Dark A Stunning Move. Date 7/7/12.
Do not dest as a new person. Do not dest 2013 Alderaan / 2014 Alderaan /
2013 SoCal Massung 60s again.
"""
from __future__ import annotations

PLAYER = "Anthony Massung"
USERNAME = ""
STAGE = ""
PDF = "2012 Alderaan Regionals.pdf"
LS_PAGE = 3
DS_PAGE = 4
LS_SCAN = "2012 Alderaan Regionals Anthony Massung LS.png"
DS_SCAN = "2012 Alderaan Regionals Anthony Massung DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Handwritten 2010 Xerox p03 Light / p04 Dark. "
    "Name Anthony Massung dested Anthony Massung analog leftover 2013 Alderaan / "
    "2014 Alderaan / 2013 SoCal. Username blank. Event Regionals Alderaan 7/7/12. "
    "Do not dest as a new person. Do not dest 2013 Alderaan / 2014 Alderaan / "
    "2013 SoCal Massung 60s again."
)
LS_NOTE = (
    "Handwritten 2010 Xerox p03 Light. Name Anthony Massung dested Anthony Massung. "
    "Username blank. LIGHT checked. Deck Name WYS dested off the article. "
    "Watch Your Step empty dested Watch Your Step. "
    "HFTMF dested Heading For The Medical Frigate analog leftover. "
    "DB 94 dested Tatooine: Docking Bay 94. "
    "Tatooine (Coruscant) dested Tatooine (Coruscant) analog leftover. "
    "Lars Moisture Farm dested Tatooine: Lars Moisture Farm. "
    "Chewie, Protector dested Chewie, Protector analog leftover Lingrell. "
    "Lando w Pistol dested Lando With Blaster Pistol. "
    "Bosheks Ship dested BoShek's Modified Freighter analog leftover MPC Atkin. "
    "Falcon dested Millennium Falcon. "
    "Mirax dested Mirax Terrik. "
    "Dash dested Dash Rendar. "
    "Its a Hit dested It's A Hit!. "
    "Its a trap dested It's A Trap!. "
    "Antilles Maneuver combo dested Antilles Maneuver & Rebel Reinforcements analog leftover. "
    "Darklighter Spin combo dested All Wings Report In & Darklighter Spin analog leftover 2013 Atkin. "
    "Control combo dested Control & Tunnel Vision analog leftover MPC Atkin. "
    "Moving to Attack Pdsitio dested Moving To Attack Position. "
    "Wookie Strangle dested Wookiee Strangle. "
    "AFA dested Anger, Fear, Aggression True. "
    "Simple Tricks dested Simple Tricks And Nonsense analog leftover Lush. "
    "Optimism dested Let's Keep A Little Optimism Here analog leftover Atkin. "
    "Chasm dested Chasm analog leftover 2013 Atkin. "
    "Insight serves dested Your Insight Serves You Well True. "
    "Proffessor dested The Professor analog leftover Lush. "
    "Shield 12 empty skip. Unique 60 shields 11 sheet-accurate."
)
DS_NOTE = (
    "Handwritten 2010 Xerox p04 Dark. Name Anthony Massung dested Anthony Massung. "
    "Username blank. DARK checked. Deck Name ASM dested off the article. "
    "ASM empty dested A Stunning Move virtual-only. "
    "Knowledge + Defense dested Knowledge And Defense True IN THE 60 analog leftover Lush. "
    "Private Platform dested Cloud City: Private Platform. "
    "Palpy's Quartels dested Coruscant: Palpatine's Quarters. "
    "Security Tower dested Cloud City: Security Tower True. "
    "Blockade DB dested Blockade Flagship: Docking Bay. "
    "Flagship Bridge dested Blockade Flagship: Bridge analog leftover Lush. "
    "Cyborg Commander's Saber dested Cyborg Commander's Lightsabers analog leftover Atkin. "
    "Maul's Double saber dested Maul's Double-Bladed Lightsaber analog leftover Lush. "
    "ZIMH dested Zuckuss In Mist Hunter. "
    "Slave 1, SOF dested Slave I, Symbol Of Fear analog leftover Atkin. "
    "Mandalorian, FOF dested Jango Fett, The Assassin analog leftover Atkin. "
    "Boba Fett, PH dested Boba Fett, Prepared Hunter analog leftover Atkin. "
    "Grevious dested Grievous, Hunter Of Jedi analog leftover Banger/Atkin. "
    "Darth Maul YA dested Darth Maul, Young Apprentice analog leftover Lush. "
    "They're Still Coming Thru dested They're Still Coming Through!. "
    "Imbalance Combo dested Imbalance & Kintan Strider analog leftover combo. "
    "Oh Switch Off dested Oh, Switch Off analog leftover. "
    "Ghhhk combo dested Ghhhk & Those Rebels Won't Escape Us analog leftover 2013 Massung. "
    "Short Range Fighters combo dested Short Range Fighters & Watch Your Back! analog leftover combo. "
    "Epic Duel crossed dest Wipe Them Out, All Of Them True analog leftover. "
    "Phantom Menace dested The Phantom Menace analog leftover 2013 Massung. "
    "Allegations Of Corruption dested Allegations Of Corruption analog leftover Atkin/Lush. "
    "Abyss dested Abyss analog leftover 2013 Massung. "
    "We'll Let Fate-a Decide dested We'll Let Fate-a Decide, Huh? True analog leftover 2013 Massung. "
    "Do They Have Code Clearance dested Do They Have A Code Clearance?. "
    "CHYBC dested Come Here You Big Coward analog leftover Atkin. "
    "YCHF dested You Cannot Hide Forever True analog leftover Atkin. "
    "Useless Gesture dested A Useless Gesture analog leftover Atkin. "
    "I Find Your Lack Faith dested I Find Your Lack Of Faith Disturbing analog leftover Atkin. "
    "Unique 60 shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step"
LS_CARDS = [
    n("Watch Your Step"),
    n("Cantina"),
    n("Tatooine: Docking Bay 94"),
    n("Tatooine (Coruscant)"),
    n("Heading For The Medical Frigate", True),
    n("Wokling", True),
    n("I Must Be Allowed To Speak", True),
    n("Get To Your Ships!"),
    n("Corellia", True),
    n("Kessel"),
    n("Tatooine: Lars Moisture Farm", True),
    n("Luke Skywalker", True, qty=2),
    n("Han, Courageous Smuggler", qty=2),
    n("Chewie, Protector"),
    n("Chewbacca", True),
    n("Dash Rendar", qty=2),
    n("Talon Karrde", qty=2),
    n("Melas", True, qty=2),
    n("Lando With Blaster Pistol"),
    n("Rycar Ryjerd", True),
    n("Sergeant Doallyn", True),
    n("BoShek, Brash Smuggler"),
    n("Mirax Terrik"),
    n("Wedge Antilles", True),
    n("Millennium Falcon"),
    n("BoShek's Modified Freighter"),
    n("Pulsar Skate"),
    n("Outrider", qty=2),
    n("Artoo-Detoo In Red 5", qty=2),
    n("It Could Be Worse"),
    n("Inconsequential Barriers"),
    n("Escape Pod", True, qty=2),
    n("It's A Hit!"),
    n("It's A Trap!"),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("All Wings Report In & Darklighter Spin"),
    n("Houjix"),
    n("Control & Tunnel Vision", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Choke"),
    n("Moving To Attack Position", qty=2),
    n("Sabotage", True),
    n("Wookiee Strangle", True),
    n("Imperial Atrocity", True, qty=2),
    n("K'lor'slug", True),
    n("Civil Disorder", True),
    n("Menace Fades"),
    n("Seeking An Audience", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Weapons Display"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("Let's Keep A Little Optimism Here"),
    n("Chasm"),
    n("Don't Do That Again"),
    n("Your Insight Serves You Well", True),
    n("The Professor"),
]
LS_ADD = []

DS_START = "A Stunning Move"
DS_CARDS = [
    n("A Stunning Move"),
    n("Knowledge And Defense", True),
    n("Cloud City: Private Platform"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na", True),
    n("Jabba's Haven"),
    n("Gift Of The Master"),
    n("Nal Hutta"),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Cyborg Commander's Lightsabers"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Zuckuss In Mist Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Victory", True),
    n("4-LOM With Concussion Rifle", True),
    n("Probe Droid"),
    n("P-59"),
    n("IG-Bodyguard Droid", qty=3),
    n("Battle Droid Squadron", qty=2),
    n("Garindan", True),
    n("Boba Fett, Prepared Hunter"),
    n("Jango Fett, The Assassin"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Galen, Secret Apprentice", qty=2),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Darth Maul"),
    n("Elis Helrot"),
    n("They're Still Coming Through!"),
    n("Imbalance & Kintan Strider"),
    n("Lightsaber Deficiency", True),
    n("Operational As Planned", True),
    n("Oh, Switch Off"),
    n("Sonic Bombardment", True, qty=2),
    n("Close Call", True),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Sith Fury", True),
    n("Short Range Fighters & Watch Your Back!"),
    n("Abyssin Ornament", True),
    n("Force Field", True, qty=2),
    n("Wipe Them Out, All Of Them", True),
    n("You Are Beaten"),
    n("Protocol Failure", True),
    n("Blaster Rack", True),
    n("Imperial Justice", True),
    n("No Escape"),
    n("Special Delivery", True),
    n("The Phantom Menace"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Secret Plans"),
    n("Weapon Of A Sith"),
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Abyss"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("Do They Have A Code Clearance?"),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture"),
    n("I Find Your Lack Of Faith Disturbing"),
]
DS_ADD = []
