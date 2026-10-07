#!/usr/bin/env python3
"""2012 Texas Mini Worlds Day 1 leftover Xerox: Evan Kirkpatrick.

Source: 2012TMWDay1.pdf pages 19–20 (typed slang printout, not a handwritten
Xerox form). Name Evan Kirkpatrick dested Evan Kirkpatrick analog leftover
2013 TMW / 2015 San Diego GP / player-stubs/Evan_Kirkpatrick.wiki. Username
blank (typed dump has no Username field). p19 Light. p20 Dark. Do not dest
as a new person. Do not dest 2013 TMW Kirkpatrick 60s again.
"""
from __future__ import annotations

PLAYER = "Evan Kirkpatrick"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 19
DS_PAGE = 20
LS_SCAN = "2012 Texas Mini Worlds Day 1 Evan Kirkpatrick LS.png"
DS_SCAN = "2012 Texas Mini Worlds Day 1 Evan Kirkpatrick DS.png"
LS_DECK_NAME = ""
DS_DECK_NAME = ""
NOTE = (
    "Typed slang printout (not a handwritten Xerox form). "
    "Name Evan Kirkpatrick dested Evan Kirkpatrick analog leftover player-stubs/Evan_Kirkpatrick.wiki. "
    "Username blank. Do not dest as a new person. Do not dest 2013 TMW Kirkpatrick 60s again."
)
LS_NOTE = (
    "Typed slang printout. Name Evan Kirkpatrick dested Evan Kirkpatrick. Username blank. "
    "Anger, Fear, Aggression True dested analog leftover 2013 Kirkpatrick start. "
    "Tatooine: Slave Quarters dested analog leftover Hendon. "
    "Communing dested analog leftover Hendon IN THE 60. "
    "Master Kenobi dested analog leftover Hendon. "
    "Quick Draw True dested analog leftover Lush. "
    "Commando Training & K'lor Slug dested Commando Training & K'lor'slug analog leftover Hendon. "
    "Tatooine: Obi-wan's Hut True dested Tatooine: Obi-Wan's Hut analog leftover Hendon True. "
    "Home: One War Room dested Home One: War Room analog leftover Hendon. "
    "Hoth: Echo War Room dested analog leftover Lush. "
    "Tatooine (EP1) dested Tatooine analog leftover Hendon. "
    "Luke Skywalker, Strong in the Force x4 dested Luke Skywalker, Strong In The Force analog leftover qty=4. "
    "Chewbacca Enraged True dested Chewie, Enraged analog leftover Hendon True qty=3. "
    "Han with Heavy Blaster Pistol dested Han With Heavy Blaster Pistol analog leftover Hendon qty=2. "
    "Fallen Jedi dested Maris Brood, Fallen Jedi analog leftover Fred. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5 analog leftover Hendon qty=2. "
    "Strikeforce True dested Strike Force analog leftover Hendon True. "
    "Sai Tor True dested Sai'torr Kal Fas analog leftover Lush True. "
    "Seeking an Audience True dested Seeking An Audience analog leftover True. "
    "Run Luke Run True dested Run Luke, Run! analog leftover Hendon True qty=2. "
    "Desperate Reach True dested analog leftover Foth True. "
    "Houjix & Out of Nowhere dested Houjix & Out Of Nowhere analog leftover qty=2. "
    "Hear Me Baby Hold Together True dested Hear Me Baby, Hold Together analog leftover Hendon True. "
    "Sorry About the Mess & Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency analog leftover Lush. "
    "Shield Simple Tricks and Nonsense dested Simple Tricks And Nonsense analog leftover Hendon. "
    "Shield Yavin Sentry True dested Yavin Sentry analog leftover Lush True. "
    "Unique 60. Shields 12."
)
DS_NOTE = (
    "Typed slang printout. Name Evan Kirkpatrick dested Evan Kirkpatrick. Username blank. "
    "Knowledge & Defense True dested Knowledge And Defense analog leftover Anderson True IN THE 60. "
    "A Stunning Move dested A Stunning Move analog leftover Anderson virtual-only. "
    "Ni Chuba Na? True dested Ni Chuba Na?? analog leftover Hendon True. "
    "Gift of the Master dested Gift Of The Master analog leftover Hendon. "
    "3720 to 1 True dested 3,720 To 1 analog leftover Massung True. "
    "Cyborg Commander, Hunter of Jedi dested Grievous, Hunter Of Jedi analog leftover Hendon qty=2. "
    "IG-Bodyguard Droid dested analog leftover Angelo qty=3. "
    "4LOM with Concussion Rifle True dested 4-LOM With Concussion Rifle analog leftover Hendon True. "
    "Dr. Evazan & Ponda Boba dested Dr. Evazan & Ponda Baba analog leftover Lush. "
    "Elis in Hinthra dested Elis In Hinthra analog leftover Gabe. "
    "Maul's Double Bladed Lightsaber dested Maul's Double-Bladed Lightsaber analog leftover Lush. "
    "Galen's Lightsaber, Vader's Gift dested analog leftover Hendon. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover Hendon. "
    "Wipe Them Out, All of Them True dested Wipe Them Out, All Of Them analog leftover Hendon True. "
    "Your Powers Are Weak Old Man True dested Your Powers Are Weak, Old Man analog leftover Anis True. "
    "Imbalance & Kintan Strider dested analog leftover Reisch. "
    "Sniper & Dark Strike dested analog leftover Reisch. "
    "Shield Weapon of a Sith dested Weapon Of A Sith analog leftover Lush. "
    "Shield Do They Have a Code Clearance True dested Do They Have A Code Clearance? analog leftover Chu True. "
    "Shield We'll Let-a Fate Decide, HUH? dested We'll Let Fate-a Decide, Huh? analog leftover Lush. "
    "Unique 57 sheet-accurate. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Anger, Fear, Aggression"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Tatooine: Slave Quarters"),
    n("Communing"),
    n("Master Kenobi"),
    n("Quick Draw", True),
    n("Commando Training & K'lor'slug"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Home One: War Room"),
    n("Hoth: Echo War Room"),
    n("Tatooine: Cantina"),
    n("Tatooine"),
    n("Luke Skywalker, Strong In The Force", qty=4),
    n("Yoda, Great Warrior", qty=2),
    n("Chewie, Enraged", True, qty=3),
    n("Han With Heavy Blaster Pistol", qty=2),
    n("Leia, Rebel Princess"),
    n("Maris Brood, Fallen Jedi"),
    n("Admiral Ackbar", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Corran Horn"),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Luke's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Chewbacca's Bowcaster"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Home One"),
    n("Bright Hope"),
    n("Spiral"),
    n("Imperial Atrocity", True),
    n("Hindsight", True),
    n("Strike Force", True),
    n("Sai'torr Kal Fas", True),
    n("Seeking An Audience", True),
    n("Rebel Gunrunner"),
    n("Launching The Assault"),
    n("Run Luke, Run!", True, qty=2),
    n("Blaster Deflection", qty=2),
    n("Rebel Leadership", True, qty=3),
    n("Antilles Maneuver & Rebel Reinforcements"),
    n("Desperate Reach", True),
    n("Houjix & Out Of Nowhere", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Use The Force"),
    n("Hear Me Baby, Hold Together", True),
    n("Sorry About The Mess & Blaster Proficiency"),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Battle Plan"),
    n("Aim High"),
    n("The Professor"),
    n("Do, Or Do Not"),
    n("Only Jedi Carry That Weapon"),
    n("Don't Do That Again", True),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Simple Tricks And Nonsense"),
    n("Ultimatum"),
    n("Yavin Sentry", True),
]
LS_ADD = []

DS_START = "A Stunning Move"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("A Stunning Move"),
    n("Coruscant: Private Platform"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Prepared Defenses", True),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("3,720 To 1", True),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Galen, Secret Apprentice", qty=3),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Battle Droid Squad", qty=3),
    n("IG-Bodyguard Droid", qty=3),
    n("P-59"),
    n("P-60"),
    n("4-LOM With Concussion Rifle", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Victory"),
    n("Elis In Hinthra"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Grievous' Lightsabers"),
    n("Restraining Bolt"),
    n("The Phantom Menace", qty=2),
    n("Wipe Them Out, All Of Them", True),
    n("Something Special Planned For Them", True),
    n("Blaster Rack", True),
    n("No Escape"),
    n("Ability, Ability, Ability", True),
    n("Forced Servitude"),
    n("Oh, Switch Off", qty=2),
    n("Force Field", True, qty=2),
    n("Self-Destruct Mechanism"),
    n("Your Powers Are Weak, Old Man", True),
    n("Masterful Move"),
    n("Ghhhk"),
    n("Stop Motion", True),
    n("Cold Feet", True),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Control & Set For Stun"),
    n("Operational As Planned", True),
    n("Imbalance & Kintan Strider"),
    n("Sniper & Dark Strike"),
]
DS_SHIELDS = [
    n("Battle Order"),
    n("Weapon Of A Sith"),
    n("Secret Plans"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Resistance"),
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try"),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?"),
]
DS_ADD = []
