#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 1 Xerox: Chris Schoenthal (imrhil327).

Source: 2014-TMW-Day-1.pdf pages 13–14 (2010 form). Day 2 p17–p18 No Changes — skip card text.
"""
from __future__ import annotations

PLAYER = "Chris Schoenthal"
USERNAME = "imrhil327"
STAGE = "Day 1"
PDF = "2014 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 13
DS_PAGE = 14
LS_SCAN = "2014 Texas Mini Worlds Day 1 p13 Chris Schoenthal LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 1 p14 Chris Schoenthal DS.png"
NOTE = "Handwritten 2010 Xerox Print Form (12 shields + Additional). No Changes on Day 2."
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Chris Schoenthal. Username imrhil327. LIGHT checked. Event TMW 5/3/14. "
    "No Changes on Day 2 — Day 2 p17–p18 skip card text. "
    "Communing empty dested Communing / Stave Off Disaster. "
    "Master Kenobi dested Master Kenobi. "
    "Tatooine Slave Qtrs dested Tatooine: Slave Quarters. "
    "Saitorr Kal Fas dested Sai'torr Kal Fas. "
    "Tatooine (EpI) dested Tatooine. "
    "JP Audience Chamber dested Jabba's Palace: Audience Chamber. "
    "Chewie Enraged dested Chewie, Enraged. "
    "Leia Rebel Princess dested Leia, Rebel Princess. "
    "Yub Yub Commander dested Yub Yub, Commander. "
    "Anakin Skywalker PL dested Anakin Skywalker, Padawan Learner. "
    "Run Luke Run dested Run Luke, Run!. "
    "Let The Wookiee Win dested Let The Wookiee Win. "
    "Chewie Protector dested Chewbacca, Protector. "
    "Lando Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Jaina Solo dested Jaina Solo. "
    "Han Solo w/ Heavy Pistol dested Han With Heavy Blaster Pistol. "
    "AWRI & Darklighter Spin dested All Wings Report In & Darklighter Spin. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "Luke Skywalker SITF dested Luke Skywalker, Strong In The Force. "
    "Tatooine OCS (V) dested Tatooine: Obi-Wan's Hut. "
    "K'lor'slug dested K'lor'slug. "
    "Wedge Rogue Sqd Ldr dested Wedge Antilles, Red Squadron Leader. "
    "Your Ship dested Your Ship?. "
    "Unique overcounts sheet-accurate (Chewie, Enraged x2, Escape Pod x3, "
    "Yub Yub, Commander x2, Run Luke, Run! x2, Padmé Naberrie x2, "
    "Luke Skywalker, Strong In The Force x3, Wesa Gotta Grand Army x2, "
    "Artoo-Detoo In Red 5 x2). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional). "
    "Name Chris Schoenthal. Username imrhil327. DARK checked. Event TMW 5/3/14. "
    "No Changes on Day 2. "
    "A Stunning Move / TBSD ASM empty dested A Stunning Move / A Valuable Hostage. "
    "Coruscant: Palpatine's Qtrs dested Coruscant: Palpatine's Quarters. "
    "We Lost R2 dested We Lost R2. "
    "Galen M. Starkiller dested Galen Marek, Starkiller. "
    "Count Dooku dested Count Dooku. "
    "Grievous Hunter of Jedi dested Grievous, Hunter Of Jedi. "
    "Dengar / Blaster Carbine dested Dengar With Blaster Carbine. "
    "IG-100 Magna Guard dested IG-100 MagnaGuard. "
    "Masterful Move dested Masterful Move & Endor Occupation. "
    "Jango Fett The Assassin dested Jango Fett, The Assassin. "
    "Maul's Sith Infiltrator dested Maul's Sith Infiltrator. "
    "A Sith's Weapon dested Weapon Of A Sith. "
    "Galen's Saber Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Sniper & Dark Strike dested Sniper & Dark Strike. "
    "Slave I, Symbol of Fear dested Slave I, Symbol Of Fear. "
    "P-59 dested P-59. "
    "You Are Beaten dested You Are Beaten. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "I Find Your Lack of Faith dested I Find Your Lack Of Faith Disturbing. "
    "Unique overcounts sheet-accurate (Galen Marek, Starkiller x2, Count Dooku x2, "
    "Grievous, Hunter Of Jedi x2, Trophy Of A Kill x2, Force Field x3, "
    "Darth Maul, Young Apprentice x2, Sonic Bombardment x2, Force Lightning x2). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing / Stave Off Disaster"
LS_CARDS = [
    n("Communing / Stave Off Disaster"),
    n("Master Kenobi", True),
    n("Wokling", True),
    n("Quick Draw", True),
    n("Tatooine: Slave Quarters"),
    n("Sai'torr Kal Fas", True),
    n("Tatooine"),
    n("Jabba's Palace: Audience Chamber"),
    n("Chewie, Enraged", True),
    n("Luke's Lightsaber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Leia, Rebel Princess"),
    n("Wesa Gotta Grand Army"),
    n("Houjix"),
    n("Yub Yub, Commander"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Run Luke, Run!", True),
    n("Escape Pod", True),
    n("Let The Wookiee Win", True),
    n("Seeking An Audience", True),
    n("Chewbacca, Protector"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Weapon Levitation"),
    n("Jaina Solo"),
    n("Escape Pod", True),
    n("Jedi Levitation", True),
    n("Yub Yub, Commander"),
    n("Chewie, Enraged", True),
    n("Padmé Naberrie", True),
    n("Han With Heavy Blaster Pistol"),
    n("All Wings Report In & Darklighter Spin"),
    n("Artoo-Detoo In Red 5"),
    n("Run Luke, Run!", True),
    n("Anakin Skywalker, Padawan Learner"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Luke Skywalker, Strong In The Force"),
    n("Let The Wookiee Win", True),
    n("Padmé Naberrie", True),
    n("Luke Skywalker, Strong In The Force"),
    n("Wesa Gotta Grand Army"),
    n("Escape Pod", True),
    n("A Gift"),
    n("Threepio With His Parts Showing"),
    n("Shmi Skywalker"),
    n("Chewbacca's Bowcaster"),
    n("Rebel Gunrunner"),
    n("Imperial Atrocity", True),
    n("K'lor'slug", True),
    n("Anakin's Lightsaber"),
    n("Dash Rendar", True),
    n("Anakin Skywalker, Padawan Learner"),
    n("Use The Force"),
    n("Corran Horn"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Lady Luck"),
    n("Grimtaash"),
    n("Artoo-Detoo In Red 5"),
    n("Luke Skywalker, Strong In The Force"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Ultimatum"),
    n("Simple Tricks And Nonsense"),
    n("Your Ship?"),
    n("Your Insight Serves You Well", True),
    n("Weapons Display", True),
    n("Wise Advice"),
    n("Chasm", True),
    n("The Professor", True),
    n("Do, Or Do Not"),
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
    n("Aim High"),
]
LS_ADD = [
    n("Don't Do That Again", True),
    n("Battle Plan"),
    n("A Tragedy Has Occurred", True),
]


DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("A Stunning Move / A Valuable Hostage"),
    n("Prepared Defenses", True),
    n("Insidious Prisoner"),
    n("Coruscant: Palpatine's Quarters"),
    n("Coruscant: Private Platform (Docking Bay)"),
    n("Ni Chuba Na?", True),
    n("Gift Of The Master"),
    n("We Lost R2", True),
    n("Cloud City: Security Tower", True),
    n("Galen Marek, Starkiller"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Count Dooku"),
    n("Dooku's Lightsaber"),
    n("Grievous, Hunter Of Jedi"),
    n("Dark Jedi Lightsaber", True),
    n("Trophy Of A Kill"),
    n("No Escape"),
    n("Blaster Rack", True),
    n("Ghhhk"),
    n("Dengar With Blaster Carbine", True),
    n("Boba Fett, Prepared Hunter"),
    n("IG-100 MagnaGuard"),
    n("Masterful Move & Endor Occupation"),
    n("Jango Fett, The Assassin"),
    n("The Phantom Menace"),
    n("Force Field"),
    n("Maul's Sith Infiltrator"),
    n("Imperial Justice", True),
    n("Battle Droid Squad"),
    n("Garindan", True),
    n("Disarmed"),
    n("Weapon Of A Sith"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Battle Droid Squad"),
    n("Sense"),
    n("Sonic Bombardment", True),
    n("Force Push", True),
    n("Galen Marek, Starkiller"),
    n("Sniper & Dark Strike"),
    n("Force Lightning"),
    n("Darth Maul, Young Apprentice"),
    n("Sonic Bombardment", True),
    n("Imperial Barrier"),
    n("Sith Fury", True),
    n("Disarmed"),
    n("Maul's Double-Bladed Lightsaber"),
    n("Darth Maul, Young Apprentice"),
    n("Trophy Of A Kill"),
    n("Grievous, Hunter Of Jedi"),
    n("Slave I, Symbol Of Fear"),
    n("Blockade Flagship: Hallway"),
    n("Count Dooku"),
    n("P-59"),
    n("Force Field", True),
    n("Sonic Bombardment", True),
    n("You Are Beaten"),
    n("Weapon Levitation"),
    n("Force Lightning"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Death Star Sentry"),
    n("Secret Plans"),
    n("Firepower", True),
    n("Battle Order"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("There Is No Try"),
    n("You Cannot Hide Forever", True),
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Weapon Of A Sith"),
]
DS_ADD = [
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Come Here You Big Coward"),
]
