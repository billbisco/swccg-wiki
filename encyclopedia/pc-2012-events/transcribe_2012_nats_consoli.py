#!/usr/bin/env python3
"""2012 US Nationals Day 1 leftover Xerox: Angelo Consoli.

Source: 2012NationalsDay1.pdf pages 11–12 typed GEMP dumps.
Name Angelo Consoli dested Angelo Consoli analog leftover 2013 Worlds CANON.
Username blank.
p11 Light Clash of Sabers / We'll Handle This.
p12 Dark A Stunning Move.
Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Angelo Consoli"
USERNAME = ""
STAGE = "Day 1"
PDF = "2012 US Nationals Day 1.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2012 US Nationals Day 1 Angelo Consoli LS.png"
DS_SCAN = "2012 US Nationals Day 1 Angelo Consoli DS.png"
LS_DECK_NAME = "Clash of Sabers"
DS_DECK_NAME = ""
NOTE = "p11 typed GEMP dump Light We'll Handle This. p12 typed GEMP dump Dark A Stunning Move. Username blank."
LS_NOTE = (
    "Typed GEMP dump. Name Angelo Consoli dested Angelo Consoli analog leftover 2013 Worlds CANON. "
    "Username blank. Event US-Nationals 2012. LS. Deck Name Clash of Sabers. "
    "Do not dest as a new person. "
    "We'll Handle This/Duel Of The Fates (V) dested We'll Handle This / Duel Of The Fates True analog leftover Fred. "
    "Virtual-only objective dest without extra (V). "
    "Booster In Pulsar Skate first line crossed skip (Clash of Sabers is the deck name). "
    "Rebel Barrier crossed dested Evacuation Control True analog leftover. "
    "Weapon Levitation crossed dested Booster In Pulsar Skate True analog leftover Veasey. "
    "Coruscant: Senate Landing Platform crossed dested Coruscant: Lower Levels analog leftover Terwilliger. "
    "Sorry About The Mess Combo dested Sorry About The Mess & Blaster Proficiency analog leftover Ziagos. "
    "Alter (Coruscant) dested Alter (Coruscant) True analog leftover Wehner. "
    "Sense (Prem.) dested Sense analog leftover. "
    "A Jedi's Resilience dested analog leftover Anderson. "
    "Speak With The Jedi Council dested analog leftover. "
    "Mace Windu, Master of the Order dested analog leftover. "
    "Obi-Wan Kenobi, Jedi Knight dested analog leftover. "
    "Yoda, Senior Council Member dested analog leftover Fred. "
    "Republic Logistics / Quick Draw True / Wokling True / Heading For The Medical Frigate / "
    "Coruscant: Jedi Council Chamber True dested IN THE 60 analog leftover. "
    "Shield Chasm crossed skipped. Unique 58 sheet-accurate. Shields 13 sheet-accurate."
)
DS_NOTE = (
    "Typed GEMP dump. Name Angelo Consoli dested Angelo Consoli analog leftover 2013 Worlds CANON. "
    "Username blank. Event US-Nationals 2012. DS. "
    "Do not dest as a new person. "
    "A Stunning Move/A Valuable Hostage dested A Stunning Move / A Valuable Hostage empty dual analog leftover. "
    "Virtual-only objective dest without extra (V). "
    "Coruscant: Private Platform (Docking Bay) dested analog leftover IN THE 60. "
    "Coruscant: Palpatine's Quarters dested analog leftover IN THE 60. "
    "Knowledge And Defense True dested IN THE 60 analog leftover. "
    "Oh, Switch Off dested analog leftover Gamble. "
    "Masterful Move & Endor Occupation dested analog leftover Marlow. "
    "Elis Helrot dested analog leftover. "
    "Weapon Levitation & The Empire's Back dested analog leftover. "
    "Imbalance & Kintan Strider dested analog leftover. "
    "Ghhhk & Those Rebels Won't Escape Us dested analog leftover Fred. "
    "Sniper & Dark Strike dested analog leftover. "
    "Cyborg Commander, Hunter Of Jedi dested Grievous, Hunter Of Jedi analog leftover. "
    "Cyborg Commander's Lightsabers dested Grievous' Lightsabers analog leftover. "
    "Galen, Secret Apprentice dested as written analog leftover. "
    "Galen's Lightsaber, Vader's Gift dested analog leftover Ziagos. "
    "IG Bodyguard droid dested IG-100 MagnaGuard analog leftover. "
    "Dr. Evazan & Ponda Baba dested analog leftover. "
    "Ni Chuba Na?? dested analog leftover Marlow. "
    "Jabba's Haven dested analog leftover Millet. "
    "Find Your Lack Of Faith Disturbing dested I Find Your Lack Of Faith Disturbing True analog leftover Ziagos. "
    "AP-59 dested as written leftover_xerox. "
    "Imperial Justice dested as written leftover_xerox True. "
    "Gift Of The Master / Prepared Defenses True / Insidious Prisoner dested IN THE 60 analog leftover. "
    "Shield Force Lightning True crossed skipped. Unique 60. Shields 12."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "We'll Handle This / Duel Of The Fates"
LS_CARDS = [
    n("Jedi Pilot"),
    n("Imperial Atrocity", True),
    n("Hindsight", True),
    n("Civil Disorder", True),
    n("Disarmed"),
    n("Menace Fades"),
    n("Sai'torr Kal Fas", True),
    n("A Jedi's Plans"),
    n("Impressive, Most Impressive", True),
    n("Are You Brain Dead?!"),
    n("It's Not My Fault!", True),
    n("Control & Tunnel Vision"),
    n("Dodge"),
    n("Evacuation Control", True),
    n("Jedi Levitation", True),
    n("Under Attack"),
    n("Booster In Pulsar Skate", True),
    n("Nabrun Leids"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Alter (Coruscant)", True),
    n("Sense"),
    n("Dark Approach", True),
    n("Let The Wookiee Win", True, qty=2),
    n("Blaster Deflection", qty=2),
    n("A Jedi's Resilience", qty=2),
    n("It's A Trap!"),
    n("Speak With The Jedi Council", qty=2),
    n("Jedi Lightsaber", True, qty=2),
    n("Obi-Wan's Lightsaber"),
    n("Ki-Adi-Mundi", True),
    n("Mace Windu, Master Of The Order", qty=2),
    n("Obi-Wan Kenobi, Jedi Knight", True, qty=2),
    n("Qui-Gon Jinn With Lightsaber", qty=2),
    n("Jedi Advisor", qty=2),
    n("Depa Billaba"),
    n("Plo Koon"),
    n("Fallen Jedi"),
    n("Yoda, Senior Council Member", True),
    n("Mirax Terrik"),
    n("Booster's Star Destroyer"),
    n("Coruscant: Night Club"),
    n("Coruscant: Jedi Archives"),
    n("Coruscant: Lower Levels"),
    n("Republic Logistics"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Heading For The Medical Frigate"),
    n("Coruscant: Jedi Council Chamber", True),
    n("We'll Handle This / Duel Of The Fates", True),
]
LS_SHIELDS = [
    n("The Professor", True),
    n("Yavin Sentry", True),
    n("Ultimatum"),
    n("Do, Or Do Not"),
    n("Another Pathetic Lifeform", True),
    n("Only Jedi Carry That Weapon"),
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Anger, Fear, Aggression", True),
]
LS_ADD = []

DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Coruscant: Palpatine's Quarters"),
    n("Knowledge And Defense", True),
    n("Oh, Switch Off"),
    n("Lightsaber Deficiency", True),
    n("Masterful Move & Endor Occupation"),
    n("Cold Feet", True),
    n("Operational As Planned", True),
    n("Force Push", True),
    n("Elis Helrot"),
    n("Force Field", True, qty=2),
    n("Weapon Levitation & The Empire's Back"),
    n("Imperial Barrier"),
    n("Imbalance & Kintan Strider"),
    n("A Dark Time For The Rebellion", True),
    n("They're Still Coming Through!"),
    n("You Are Beaten"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Control"),
    n("Sniper & Dark Strike"),
    n("The Phantom Menace"),
    n("Protocol Failure"),
    n("Blaster Rack", True),
    n("No Escape"),
    n("First Strike"),
    n("Disarmed"),
    n("Nal Hutta"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Blockade Flagship"),
    n("Victory"),
    n("Zuckuss In Mist Hunter"),
    n("Boba Fett In Slave I", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Grievous' Lightsabers"),
    n("Grievous, Hunter Of Jedi", qty=2),
    n("Battle Droid Squad", qty=2),
    n("Darth Maul, Young Apprentice", qty=2),
    n("Darth Maul"),
    n("Galen, Secret Apprentice", qty=2),
    n("AP-59"),
    n("Dr. Evazan & Ponda Baba"),
    n("OOM-9", True),
    n("IG-100 MagnaGuard"),
    n("Garindan", True),
    n("4-LOM With Concussion Rifle", True),
    n("Jabba's Haven"),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Prepared Defenses", True),
    n("Insidious Prisoner"),
    n("Imperial Justice", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
    n("Secret Plans"),
    n("Resistance"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Firepower", True),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("A Useless Gesture", True),
]
DS_ADD = []
