#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Brian Fred handwritten 2013 Print Form LS+DS.

Name field B Fred. Username blank. Dest Brian Fred (file_player BFred).
"""
from __future__ import annotations

PLAYER = "Brian Fred"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 11
DS_PAGE = 12
LS_SCAN = "2013 SoCal Grand Prix Day 1 p11 Brian Fred LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p12 Brian Fred DS.png"
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests 1-6 checked, "
    "Hidden Fortress empty). Name B Fred dested Brian Fred. Username blank. "
    "Deck Name Reid does not approve 1. LIGHT/DARK empty; dest Light from "
    "AFA (V) plus MWYHL/SYIC (V). Do not dest as a new person. "
    "Do not rewrite 2013 Worlds Fred leftover. "
    "AFA dested Anger, Fear, Aggression. "
    "MWYHL/SYIC dested Mind What You Have Learned / Save You It Can True. "
    "Weapon lev dested Weapon Levitation. "
    "Strike force dested Strikeforce. "
    "It could be worse dested It Could Be Worse. "
    "A Jedi res dested A Jedi's Resilience. "
    "Mech failure dested Mechanical Failure. "
    "Do or Do not / Wise dested Do, Or Do Not & Wise Advice. "
    "Luke SITF dested Luke Skywalker, Strong In The Force. "
    "Mace Windu Master dested Mace Windu, Master Of The Order. "
    "Master Qui gon dested Master Qui-Gon. "
    "Lando Cal Unlikely dested Lando Calrissian, Unlikely Hero. "
    "wesa dested Wesa Gotta Grand Army. "
    "Battle plan / DTF dested Battle Plan & Draw Their Fire. "
    "HCF dested Han, Chewie, And The Falcon. "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "Strong is Vader dested Strong Is Vader. "
    "Shield 1 Omin to dested Omin To as written. "
    "Your Ship dested Your Ship?. "
    "Effect might dested Effect Might as written. "
    "Jedi Tests 1-6 dested the six Jedi Tests. "
    "Unique overcounts sheet-accurate: Let The Wookiee Win x4, "
    "Luke Skywalker, Strong In The Force x3, Escape Pod x3, "
    "Master Qui-Gon x2, Republic Gunship Wing x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Jedi Tests empty). "
    "Name B Fred dested Brian Fred. Username blank. "
    "Deck Name Reid does not approve 2. LIGHT/DARK empty; dest Dark from K+D (V). "
    "Hidden Fortress Jedi Test 1-6 crossed, skipped. "
    "Do not dest as a new person. Do not rewrite 2013 Worlds Fred leftover. "
    "K+D dested Knowledge And Defense. "
    "CLT/MFD dested Colo Claw Fish & My Favorite Decoration as written. "
    "thrawn dested Grand Admiral Thrawn. "
    "imp holotable dested Imperial Holotable. "
    "Dr E Ponda B dested Dr. Evazan & Ponda Baba. "
    "Flagship bridge dested Blockade Flagship: Bridge. "
    "SRF/WYB dested Short Range Fighters & Watch Your Back!. "
    "Stunning leader dested Stunning Leader. "
    "Lightsaber Def dested Lightsaber Deficiency (Worlds Fred analog). "
    "Sneak A+K dested Sneak Attack (Worlds Fred analog). "
    "Dark time for rebel dested A Dark Time For The Rebellion. "
    "any medicus necessary dested Any Methods Necessary. "
    "Control / SFT for Stun dested Control & Set For Stun (Banger analog). "
    "Darth Vader epp dested Darth Vader With Lightsaber. "
    "Darth Maul epp dested Darth Maul With Lightsaber. "
    "Mauls Sith Infiltr dested Maul's Sith Infiltrator. "
    "Prisoner dested Prisoner as written. "
    "JP Owner dested Jabba's Palace as written. "
    "JP Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "CC Carbonite Chamber dested Cloud City: Carbonite Chamber. "
    "4lom epp dested 4-LOM With Concussion Rifle. "
    "The Emperor dested Emperor Palpatine. "
    "IG-88 Nerve inhibitor dested IG-88 Nerve Inhibitor as written. "
    "Boba Fett prep hunter dested Boba Fett, Prepared Hunter. "
    "Slave I Symbol dested Slave I, Symbol Of Fear. "
    "Carbon Chamber Console dested Carbonite Chamber Console. "
    "CC Security tower dested Cloud City: Security Tower. "
    "proto failure dested Protocol Failure. "
    "Vitturi dested Vitturi as written. "
    "Mara Jade epp dested Mara Jade With Lightsaber. "
    "Jango Fett the assassin dested Jango Fett, The Assassin. "
    "Grand Moff tarkin dested Grand Moff Tarkin. "
    "Hunted crossed, The Emp's Reach TPM dested Maarek Stele, The Emperor's Reach. "
    "Leave Them To Me dested Leave Them To Me. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "Unique overcounts sheet-accurate: Stunning Leader x2, Sense x2, "
    "Defensive Fire x2, Force Lightning x2, Emperor Palpatine x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Mind What You Have Learned / Save You It Can", True),
    n("Weapon Levitation"),
    n("Hear Me Baby, Hold Together", True),
    n("Strikeforce", True),
    n("It Is The Future You See", True),
    n("It Could Be Worse"),
    n("A Jedi's Resilience", qty=2),
    n("Houjix", qty=2),
    n("Clash Of Sabers", qty=2),
    n("Mechanical Failure", qty=2),
    n("Do, Or Do Not & Wise Advice"),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Projection Of A Skywalker"),
    n("The Way Of Things"),
    n("Luke's Backpack"),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Luke Skywalker, Strong In The Force", qty=3),
    n("Mace Windu, Master Of The Order"),
    n("Mace Windu", True, qty=2),
    n("Let The Wookiee Win", True, qty=4),
    n("Daughter Of Skywalker", True),
    n("Yoda", True),
    n("Corran Horn"),
    n("Master Qui-Gon", True, qty=2),
    n("Lando Calrissian, Unlikely Hero"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Battle Plan & Draw Their Fire"),
    n("Han, Chewie, And The Falcon", True),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Lady Luck"),
    n("Luke Skywalker, Jedi Knight"),
    n("Escape Pod", True, qty=3),
    n("Strong Is Vader"),
    n("Jedi Lightsaber", True),
    n("Qui-Gon's Lightsaber"),
    n("Luke's Lightsaber"),
    n("Dagobah: Swamp"),
    n("Dagobah: Jungle"),
    n("Dagobah: Yoda's Hut"),
    n("Dagobah"),
    n("Naboo: Battle Plains"),
    n("Republic Gunship Wing", qty=2),
]
LS_SHIELDS = [
    n("Omin To", True),
    n("Your Ship?"),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Your Insight Serves You Well", True),
    n("Aim High"),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("He Can Go About His Business", True),
    n("Effect Might", True),
    n("Weapons Display", True),
    n("Chasm", True),
]
LS_ADD = [
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("It Is The Future You See"),
    n("A Jedi's Focus"),
    n("A Jedi's Resilience"),
]


DS_START = "Knowledge And Defense"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("Colo Claw Fish & My Favorite Decoration"),
    n("Grand Admiral Thrawn"),
    n("Imperial Holotable"),
    n("Dr. Evazan & Ponda Baba"),
    n("Blockade Flagship: Bridge"),
    n("Imperial Barrier"),
    n("Monnok"),
    n("Short Range Fighters & Watch Your Back!"),
    n("Stunning Leader", qty=2),
    n("Imperial Command"),
    n("Sense", qty=2),
    n("Lightsaber Deficiency", True),
    n("Sneak Attack", True),
    n("Cold Feet", True),
    n("A Dark Time For The Rebellion", True),
    n("Defensive Fire", True, qty=2),
    n("Masterful Move"),
    n("We Must Accelerate Our Plans"),
    n("Elis Helrot"),
    n("The Circle Is Now Complete"),
    n("Imperial Artillery"),
    n("Any Methods Necessary"),
    n("Blow Parried"),
    n("Control & Set For Stun"),
    n("Force Lightning", qty=2),
    n("Jabba's Prize"),
    n("Darth Vader With Lightsaber"),
    n("Darth Maul"),
    n("Darth Maul With Lightsaber"),
    n("Maul's Sith Infiltrator"),
    n("No Escape"),
    n("Prisoner"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Kashyyyk"),
    n("Jabba's Palace"),
    n("Jabba's Palace: Audience Chamber"),
    n("Cloud City: Carbonite Chamber"),
    n("Black Sun Fleet"),
    n("4-LOM With Concussion Rifle", True),
    n("IG-88", True),
    n("Boba Fett", True),
    n("Emperor Palpatine", True, qty=2),
    n("IG-88 Nerve Inhibitor", True),
    n("Boba Fett, Prepared Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Carbonite Chamber Console", True),
    n("Despair", True),
    n("Cloud City: Security Tower", True),
    n("Protocol Failure"),
    n("Vitturi"),
    n("Mara Jade With Lightsaber", True),
    n("Jango Fett, The Assassin"),
    n("Grand Moff Tarkin", True),
    n("Maarek Stele, The Emperor's Reach"),
]
DS_SHIELDS = [
    n("Leave Them To Me", True),
    n("Do They Have A Code Clearance?", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Firepower", True),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Battle Order"),
    n("Secret Plans"),
    n("Fanfare", True),
    n("Imperial Detention"),
    n("A Useless Gesture", True),
    n("You Cannot Hide Forever", True),
    n("We'll Let Fate-a Decide, Huh?", True),
]
DS_ADD = []
