#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Matt Thornton Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Matt Thornton"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 39
DS_PAGE = 40
LS_SCAN = "2013 SoCal Grand Prix Day 1 p39 Matt Thornton LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p40 Matt Thornton DS.png"
LS_NOTE = (
    "Handwritten Print Form. Deck Name Sep V. Event SOGP. Line 1 written SoGa (V) is "
    "Watch Your Step (V) / This Place Can Be A Little Rough (Corellia / Dash / Lady Luck / "
    "Punch It! / Corellian Slip). HFTMF → Heading For The Medical Frigate. "
    "EK Am Hub → Hoth: Echo Docking Bay. Wedge, RSL → Wedge Antilles, Red Squadron Leader. "
    "LS, JK → Luke Skywalker, Jedi Knight. Leia, RP → Leia, Rebel Princess. "
    "CDC → Chewbacca. NQA → No Questions Asked. Antilles Man → Antilles Maneuver. "
    "Antilles Man Combo → Antilles Maneuver & Rebel Reinforcements. "
    "AWRI & DS → All Wings Report In & Darklighter Spin. LTWW → Let The Wookiee Win. "
    "The Lock → Landing Claw. Retreat → Run Luke, Run!. Yoda, GW → Yoda, Great Warrior. "
    "Leia's Gun → Leia With Blaster Rifle. Houjix Combo → Houjix. Palejo → Palejo Reshad. "
    "Strike Force → Strikeforce. SP DB → Tatooine: Spaceport Docking Bay. "
    "HL DB → Home One: Docking Bay. GP Street → Coruscant: Golden Plaza. "
    "AFA → Anger, Fear, Aggression. DDTAT → Don't Do That Again. "
    "STAN → Simple Tricks And Nonsense. (V) from the checkbox."
)
DS_NOTE = (
    "Handwritten Print Form. Deck Name Senate. Senate Obj → My Lord, Is That Legal / "
    "I Will Make It Legal. Senate → Coruscant: Galactic Senate. "
    "Maul's site → Naboo: Theed Palace Generator. Combat response → Combat Response. "
    "SRF & WYB → Short Range Fighters & Watch Your Back!. Emp Maul → Darth Maul. "
    "Squabbling Del → Squabbling Delegates. Sonic Bomb → Sonic Bombardment. "
    "WMAOP → We Must Accelerate Our Plans. Jango, FOE → Jango Fett, The Assassin. "
    "THWN → They Will Be No Match For You. Emp Mara → Mara Jade With Lightsaber. "
    "After Mas → Mas Amedda. Pawn's Gem as written. Maul Strikes as written. "
    "Slave I, SOF → Slave I, Symbol Of Fear. Mag Kinter → MagnaGuard. "
    "Boba, Prepared Hunter → Boba Fett, Prepared Hunter. Punishing One as written. "
    "Beskar → Mandalorian Armor. KAD → Knowledge And Defense. "
    "Lack of Faith → I Find Your Lack Of Faith Disturbing. "
    "Coward → Come Here You Big Coward. BO → Battle Order. (V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Heading For The Medical Frigate"),
    n("Hoth: Echo Docking Bay"),
    n("Seeking An Audience"),
    n("Wokling", True),
    n("Evacuation Control"),
    n("Booster In Pulsar Skate"),
    n("Wedge Antilles, Red Squadron Leader", qty=2),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Leia, Rebel Princess"),
    n("Chewbacca", True),
    n("Padme Naberrie"),
    n("Antilles Maneuver", True, qty=2),
    n("Lando Calrissian, Scoundrel"),
    n("Independence"),
    n("No Questions Asked", True, qty=3),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Let The Wookiee Win", True, qty=2),
    n("Corran Horn"),
    n("Chewie, Enraged", True),
    n("Landing Claw"),
    n("Sense"),
    n("Run Luke, Run!", True, qty=2),
    n("Yoda, Great Warrior"),
    n("Padme Naberrie", True),
    n("Anakin Skywalker"),
    n("Rebel Barrier"),
    n("Leia With Blaster Rifle"),
    n("Houjix & Out Of Nowhere"),
    n("Grimtaash"),
    n("Palejo Reshad"),
    n("Corellia", True),
    n("Strikeforce", True),
    n("Houjix", True),
    n("The Bith Shuffle"),
    n("Corellia", True),
    n("Scoundrel's Luck"),
    n("Tatooine: Spaceport Docking Bay"),
    n("Home One: Docking Bay"),
    n("Coruscant: Golden Plaza"),
    n("Coruscant"),
    n("Endor", True),
    n("Dash Rendar", True),
    n("Punch It!"),
    n("Corellian Slip", True),
    n("Mace Windu, Master Of The Order"),
    n("Desperate Reach"),
    n("Fly Casual"),
    n("Lady Luck"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Jabba's Prize"),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("Ultimatum"),
    n("The Professor"),
    n("Yavin Sentry"),
    n("Your Insight Serves You Well", True),
    n("Simple Tricks And Nonsense"),
    n("Wise Advice"),
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
]
LS_ADD = []


DS_START = "My Lord, Is That Legal / I Will Make It Legal"
DS_CARDS = [
    n("My Lord, Is That Legal / I Will Make It Legal"),
    n("Coruscant: Galactic Senate"),
    n("Surface Defense", True),
    n("Nute Gunray"),
    n("Naboo: Theed Palace Generator"),
    n("Combat Response", qty=2),
    n("Short Range Fighters & Watch Your Back!", qty=3),
    n("Darth Maul", qty=3),
    n("Squabbling Delegates", qty=3),
    n("Lott Dod", qty=3),
    n("Sonic Bombardment", True, qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Fear", qty=2),
    n("Jango Fett, The Assassin", qty=2),
    n("Senate Hovercam", qty=2),
    n("Accepting Trade Federation Control"),
    n("Motion Supported"),
    n("Our Blockade Is Perfectly Legal"),
    n("This Is Outrageous"),
    n("Blockade Flagship: Bridge"),
    n("Cloud City: Security Tower"),
    n("They Will Be No Match For You"),
    n("Orn Free Taa", qty=2),
    n("Eeth Koth"),
    n("Emperor Palpatine"),
    n("Mandalorian Armor"),
    n("Limited Resources"),
    n("Mara Jade With Lightsaber"),
    n("Yeb Yeb Adem'thorn"),
    n("Mas Amedda"),
    n("Passel Argente"),
    n("Aks Moe"),
    n("Edcel Bar Gane"),
    n("Maul Strikes"),
    n("Tikkes"),
    n("Slave I, Symbol Of Fear"),
    n("IG-100 MagnaGuard"),
    n("Bossk"),
    n("Hound's Tooth"),
    n("Boba Fett, Prepared Hunter"),
    n("Dengar"),
    n("Punishing One"),
    n("Boushh"),
    n("Saber 1"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("A Useless Gesture"),
    n("Do They Have A Code Clearance?"),
    n("Oppressive Enforcement"),
    n("Firepower", True),
    n("Fanfare"),
    n("Battle Order"),
    n("Abyss", True),
    n("Resistance"),
    n("Allegations Of Corruption"),
    n("Come Here You Big Coward"),
    n("You Cannot Hide Forever"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Secret Plans"),
]
DS_ADD = []
