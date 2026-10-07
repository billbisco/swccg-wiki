#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Barry Alperstein Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Barry Alperstein"
USERNAME = "MrFromMars"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 1
DS_PAGE = 2
LS_SCAN = "2013 Match Play Championship p01 Barry Alperstein LS.png"
DS_SCAN = "2013 Match Play Championship p02 Barry Alperstein DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username MrFromMars. Event MPC '13. "
    "Title above the form: I Hope Shannon Doesn't Steal My Starting Cards. "
    "AFA → Anger, Fear, Aggression. QMC → Quiet Mining Colony. "
    "HFTMF → Heading For The Medical Frigate. Lokling → Wokling. "
    "KTEO → Keeping The Empire Out Forever. Luke, RH → Luke Skywalker, Rebel Hero. "
    "Luke, QH dested Luke Skywalker, Jedi Knight. Path → Path Of Least Resistance. "
    "Chewbacca, WC dested Chewbacca Of Kashyyyk. Rebel Agent dested Rebel Scout. "
    "Blast The Door Kid → Blast The Door, Kid!. Artoo, BAD dested Artoo-Detoo In Red 5. "
    "Obi in Radiant → Radiant VII. Lando, UH → Lando Calrissian, Unlikely Hero. "
    "Han w/ Gun → Han With Heavy Blaster Pistol. Leia, RP → Leia, Rebel Princess. "
    "SATM + BP → Sorry About The Mess & Blaster Proficiency. "
    "Houjix + OON → Houjix & Out Of Nowhere. Lando's Yacht → Lady Luck. "
    "Insight → Your Insight Serves You Well. DoDN / DDTA → Don't Do That Again. "
    "Form left column reprints 37–38 on lines 39–40. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Username MrFromMars. Title above the form: "
    "I'm Starting Quarters. K+D → Knowledge And Defense. ASM → A Stunning Move. "
    "MM + EO → Masterful Move & Endor Occupation. Sniper + DS → Sniper & Dark Strike. "
    "DrE + PB → Dr. Evazan & Ponda Baba. Mando, FoF → Jango Fett, The Assassin. "
    "Cyborg Commander → General Grievous. Galen, SA → Galen Marek, Starkiller. "
    "Maul, YA → Darth Maul, Young Apprentice. Slave I, SoF → Slave I, Symbol Of Fear. "
    "Galen's LS, VG → Galen's Lightsaber, Vader's Gift. "
    "4-LOM w/ Rifle → 4-LOM With Concussion Rifle. TPM → The Phantom Menace. "
    "YCHF → You Cannot Hide Forever. Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Anger, Fear, Aggression", True),
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Keeping The Empire Out Forever"),
    n("Beldon's Eye", True),
    n("Kebyc", True),
    n("Narrow Escape"),
    n("Luke Skywalker, Rebel Hero"),
    n("Path Of Least Resistance", qty=3),
    n("Padme Naberrie", True),
    n("Alternatives To Fighting"),
    n("No Questions Asked"),
    n("Pucumir Thryss"),
    n("Corran Horn"),
    n("Cloud City Celebration", qty=2),
    n("Dash Rendar", True),
    n("It's A Trap!"),
    n("Yoda, Great Warrior"),
    n("Cloud City: West Gallery"),
    n("Imperial Atrocity", True, qty=3),
    n("Houjix & Out Of Nowhere"),
    n("Melas", True),
    n("Mirax Terrik"),
    n("Rebel Scout"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Luke Skywalker, Jedi Knight"),
    n("Redeemed Apprentice"),
    n("Booster In Pulsar Skate"),
    n("Chewbacca Of Kashyyyk"),
    n("Blast The Door, Kid!"),
    n("Rebel Artillery", qty=2),
    n("Spiral", qty=2),
    n("Cloud City: North Corridor"),
    n("Artoo-Detoo In Red 5"),
    n("Overseer"),
    n("Luke's Blaster Pistol", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Rebel Barrier", qty=2),
    n("Harc Seff", True),
    n("Cloud City: Upper Plaza Corridor"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Black Market Blaster"),
    n("Han With Heavy Blaster Pistol"),
    n("Leia, Rebel Princess"),
    n("Radiant VII"),
    n("Menace Fades"),
    n("Cloud City: Lower Corridor"),
    n("Lady Luck"),
    n("Seeking An Audience"),
]
LS_SHIELDS = [
    n("Your Insight Serves You Well", True),
    n("The Professor"),
    n("Ultimatum"),
    n("Aim High"),
    n("Don't Do That Again"),
    n("Wise Advice"),
    n("Weapons Display"),
    n("Yavin Sentry"),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
]
LS_ADD = []


DS_START = "A Stunning Move / A Valuable Hostage"
DS_CARDS = [
    n("Knowledge And Defense", True),
    n("A Stunning Move / A Valuable Hostage"),
    n("Coruscant: Private Platform"),
    n("Coruscant: Palpatine's Quarters"),
    n("Insidious Prisoner"),
    n("Prepared Defenses"),
    n("Gift Of The Master"),
    n("Jabba's Haven", True),
    n("Ni Chuba Na?", True),
    n("Force Field", True, qty=2),
    n("Stop Motion", True, qty=2),
    n("Sonic Bombardment", True),
    n("Masterful Move & Endor Occupation"),
    n("You Are Beaten"),
    n("Oh, Switch Off"),
    n("Sniper & Dark Strike"),
    n("Sith Fury", True),
    n("Cold Feet", True),
    n("Slave I, Symbol Of Fear"),
    n("Victory"),
    n("Zuckuss In Mist Hunter"),
    n("Blockade Flagship: Hallway"),
    n("Blockade Flagship: Docking Bay"),
    n("Blockade Flagship: Bridge"),
    n("Nal Hutta"),
    n("Trophy Of A Kill", qty=2),
    n("Dark Jedi Lightsaber", True),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Maul's Double-Bladed Lightsaber"),
    n("IG-100 MagnaGuard", qty=2),
    n("Galen Marek, Starkiller", qty=3),
    n("Darth Maul, Young Apprentice", qty=3),
    n("Dr. Evazan & Ponda Baba"),
    n("Boba Fett, Prepared Hunter"),
    n("Dengar With Blaster Carbine", True),
    n("Jango Fett, The Assassin"),
    n("General Grievous", qty=2),
    n("P-59"),
    n("4-LOM With Concussion Rifle", True),
    n("Battle Droid Squad", qty=2),
    n("The Phantom Menace", qty=2),
    n("Something Special Planned For Them", True),
    n("Tarkin's Bounty", True),
    n("Blaster Rack", True),
    n("Imperial Justice", True),
    n("Imperial Propaganda", True),
    n("Where Are You Taking This Thing?", True),
    n("No Escape"),
    n("A Sith's Weapon"),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever"),
    n("Weapon Of A Sith"),
    n("Abyss"),
    n("Firepower"),
    n("Resistance"),
    n("There Is No Try"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Battle Order"),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("Secret Plans"),
]
DS_ADD = []
