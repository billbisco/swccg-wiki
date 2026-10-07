#!/usr/bin/env python3
"""2012 Match Play Championship Day 1 Xerox: SAN.

Source: 2012mpcday1.pdf pages 145–146 (2010 form, 12 shields).
Name SAN dested SAN analog 2013 leftover PLAYER="SAN".
Username blank. Do not copy 2014 leftover Username Pancakes.
p145 Light Communing. p146 Dark My Lord, Is That Legal?.
Pack player-stubs/SAN.wiki (is_bio False).
Do not dest as a new person. Do not invent a first name.
Do not rewrite 2013 leftover Watch Your Step / Wookiee Slaving Operation.
Do not rewrite 2014 leftover There Is Good In Him / Carbon Chamber Testing.
"""
from __future__ import annotations

PLAYER = "SAN"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Match Play Championship Day 1.pdf"
LS_PAGE = 145
DS_PAGE = 146
LS_SCAN = "2012 Match Play Championship Day 1 SAN LS.png"
DS_SCAN = "2012 Match Play Championship Day 1 SAN DS.png"
LS_DECK_NAME = "It looks alot like engine oil & tastes like being poor & small"
DS_DECK_NAME = "DEEP RED BELLS"
NOTE = "Handwritten 2010 Xerox form."
PUBLIC_NOTE = "Name as written on the Day 1 sheet."
LS_NOTE = (
    "Handwritten 2010 Xerox. Name SAN dested SAN analog 2013 leftover. "
    "Username blank. Do not copy 2014 leftover Username Pancakes. "
    "LIGHT/DARK empty dest Light from the 60s. "
    "Do not dest as a new person. Do not invent a first name. "
    "Do not rewrite 2013 leftover Watch Your Step. "
    "Communing dested Communing analog leftover. "
    "Master Jedi dested Master Kenobi analog leftover. "
    "Slave Quarters dested Tatooine: Slave Quarters analog leftover. "
    "Commando Training & K'lor Slug dested Commando Training & K'lor'slug analog leftover. "
    "Houjix & OON dested Houjix & Out Of Nowhere analog leftover. "
    "Padme True dested Padmé Naberrie True analog leftover. "
    "Chewie Enraged True dested Chewie, Enraged True analog leftover. "
    "Jedi Lev True dested Jedi Levitation True analog leftover. "
    "Weapon Lev dested Weapon Levitation analog leftover. "
    "Chewie Protector dested Chewbacca, Protector analog leftover. "
    "Instant Hindsight True dested Hindsight True analog leftover. "
    "Wyron Serper True dested Wyron Serper True analog leftover. "
    "Artoo in R5 dested Artoo-Detoo In Red 5 analog leftover. "
    "Its Not my Fault True dested It's Not My Fault! True analog leftover. "
    "Loader Ship, Rebel True and empty kept separate analog Foth. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency analog leftover. "
    "Tatooine EPI dested Tatooine (Coruscant) analog leftover. "
    "Lando Scoundrel True dested Lando Calrissian, Scoundrel True analog leftover. "
    "NAMED 3PO dested C-3PO (See-Threepio) analog leftover. "
    "Luke Rebel Hero dested Luke Skywalker, Rebel Hero analog leftover. "
    "Blind Jedi dested as written analog leftover. "
    "Obi-Wan's Hut True dested Tatooine: Obi-Wan's Hut True analog leftover. "
    "Fallen Jedi dested as written analog leftover. "
    "Wedge RSL dested Wedge Antilles, Red Squadron Leader analog leftover. "
    "H1: War Room dested Home One: War Room analog leftover. "
    "Han w/ gun dested Han With Heavy Blaster Pistol analog leftover. "
    "AFA True dested Anger, Fear, Aggression True analog leftover IN THE 60. Unique 60. Shields 12."
)
DS_NOTE = (
    "Handwritten 2010 Xerox. Name SAN dested analog 2013 leftover. "
    "Username blank. DARK checked dest Dark from the 60s. "
    "Do not dest as a new person. Do not invent a first name. "
    "Do not rewrite 2013 leftover Wookiee Slaving Operation. "
    "My Lord is That Legal dested My Lord, Is That Legal? / I Will Make It Legal analog leftover. "
    "Senate dested Coruscant: Galactic Senate analog leftover. "
    "NABOO dested Naboo analog leftover. "
    "Ni Chuba Na True dested Ni Chuba Na?? True analog leftover. "
    "Lot Dodd dested Lott Dod analog leftover. "
    "Squabble dested Squabbling Delegates analog leftover. "
    "Baskol dested Baskol Yeesrim analog leftover. "
    "Toonbuck dested Toonbuck Toora analog leftover. "
    "SRF & WYB dested Short Range Fighters & Watch Your Back analog leftover. "
    "Dark Maneuvers & Tallon Roll dested Dark Maneuvers & Tallon Roll analog leftover. "
    "Hovercam dested Senate Hovercam analog leftover. "
    "Obsidian 10 True dested Obsidian 10 True analog leftover. "
    "Passel dested Passel Argente analog leftover. "
    "OS-72-1 in Obs 1 dested OS-72-1 In Obsidian 1 analog leftover. "
    "OS-72-2 in Obs 2 dested OS-72-2 In Obsidian 2 analog leftover. "
    "Zuckuss Shuttle ZIMH crossed skipped. "
    "OS 72 10 dested OS-72-10 analog leftover. "
    "This is Outrageous dested This Is Outrageous! analog leftover. "
    "Edcel Bar Gain dested Edcel Bar Gane analog leftover. "
    "Yeb Yeb dested Yeb Yeb Adem'thorn analog leftover. "
    "A Dark Time For The Rebellion True crossed skipped. "
    "Our Blackmail is Legal dested Our Blockade Is Perfectly Legal analog leftover. "
    "Motion Supported dested Motion Supported analog leftover. "
    "MM & EO dested Masterful Move & Endor Occupation analog leftover. "
    "On Fire Tag dested Orn Free Taa analog leftover. "
    "This MORE dested Aks Moe analog leftover. "
    "Baron Fel dested Baron Soontir Fel analog leftover. "
    "K&D True dested Knowledge And Defense True analog leftover IN THE 60. "
    "Dengar in P1 margin Additional empty skipped. Unique 58. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Commando Training & K'lor'slug"),
    n("We're Leaving"),
    n("Home One"),
    n("Flash Of Insight"),
    n("Houjix & Out Of Nowhere"),
    n("Padmé Naberrie", True),
    n("Chewie, Enraged", True),
    n("Seeking An Audience", True),
    n("Jedi Levitation", True),
    n("Desperate Reach", True),
    n("Weapon Levitation"),
    n("Chewbacca, Protector", qty=2),
    n("Use The Force", qty=2),
    n("Hindsight", True),
    n("Run Luke, Run!", True, qty=2),
    n("Wyron Serper", True),
    n("Alderaan Consular Ship", qty=2),
    n("Artoo-Detoo In Red 5"),
    n("Lucky Shot", True),
    n("It's Not My Fault!", True),
    n("Inconsequential Barriers", qty=2),
    n("Loader Ship, Rebel", True),
    n("Loader Ship, Rebel"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Security Breach"),
    n("Senator Leia Organa", True),
    n("Admiral Ackbar", True),
    n("Tatooine (Coruscant)"),
    n("Lando Calrissian, Scoundrel", True),
    n("Draw Their Fire"),
    n("Casting"),
    n("It Could Be Worse"),
    n("C-3PO (See-Threepio)"),
    n("Luke Skywalker, Rebel Hero", qty=3),
    n("Chewbacca's Bowcaster"),
    n("Blind Jedi"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tantive IV", True),
    n("Corran Horn"),
    n("Fallen Jedi"),
    n("Rebel Gunner"),
    n("Shmi Skywalker"),
    n("Yoda, Great Warrior"),
    n("Luke's Blaster Pistol", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Menace Fades"),
    n("Home One: War Room"),
    n("Imperial Atrocity", True),
    n("Han With Heavy Blaster Pistol"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Ultimatum"),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Don't Do That Again", True),
    n("Battle Plan", True),
    n("Your Insight Serves You Well", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Ounee Ta"),
]
LS_ADD = []

DS_START = "My Lord, Is That Legal? / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal? / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Naboo"),
    n("Prepared Defenses"),
    n("Combat Response"),
    n("I'm Sorry", True),
    n("Ni Chuba Na??", True),
    n("Lott Dod", qty=3),
    n("Squabbling Delegates", qty=4),
    n("Tikkes", qty=2),
    n("Baskol Yeesrim", qty=2),
    n("Toonbuck Toora", qty=2),
    n("Short Range Fighters & Watch Your Back", qty=2),
    n("Dark Maneuvers & Tallon Roll", qty=2),
    n("Control", qty=2),
    n("All Power To Weapons", qty=2),
    n("Senate Hovercam", qty=2),
    n("Floating Refinery", True, qty=2),
    n("Obsidian 10", True),
    n("Passel Argente"),
    n("OS-72-1 In Obsidian 1"),
    n("OS-72-2 In Obsidian 2"),
    n("Pride Of The Empire"),
    n("DS-61-2"),
    n("Saber 1"),
    n("Black 2"),
    n("OS-72-10"),
    n("Clouds"),
    n("Accepting Trade Federation Control"),
    n("This Is Outrageous!"),
    n("Edcel Bar Gane"),
    n("Darth Vader", True),
    n("Yeb Yeb Adem'thorn"),
    n("Our Blockade Is Perfectly Legal"),
    n("Storm Clouds"),
    n("Motion Supported"),
    n("Masterful Move & Endor Occupation"),
    n("Coruscant Guard"),
    n("Orn Free Taa"),
    n("Aks Moe"),
    n("Black 3", True),
    n("DS-61-3"),
    n("Baron Soontir Fel"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("A Useless Gesture", True),
    n("Fanfare", True),
    n("Battle Order"),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Do They Have A Code Clearance?", True),
    n("Allegations Of Corruption"),
    n("Resistance"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Abyss", True),
]
DS_ADD = []
