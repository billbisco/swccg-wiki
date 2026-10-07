#!/usr/bin/env python3
"""2013 World Championship Day 2: Steve Baroni Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Steve Baroni"
USERNAME = ""
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 16
DS_PAGE = 15
LS_SCAN = "2013 Worlds Day 2 p16 Steve Baroni LS.png"
DS_SCAN = "2013 Worlds Day 2 p15 Steve Baroni DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Baroni dested Steve Baroni. "
    "Username blank. Deck title It Won't Fit In The Box. LIGHT. "
    "MWYHL dested Mind What You Have Learned / Save You It Can. "
    "It is Future dested It Is The Future You See (Epic Event in the 60). "
    "Strong Is Vader dested Strong Is Vader. "
    "Do or do not / WA dested Do, Or Do Not & Wise Advice. "
    "BP/DTF dested Battle Plan & Draw Their Fire. "
    "Sai tor Kal Fas dested Sai'torr Kal Fas. "
    "Dagobah Swamp dested Dagobah: Swamp. "
    "Qui-Gon's Saber dested Qui-Gon's Lightsaber. "
    "Luke's Lightsaber (V) struck dested Luke's Lightsaber. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. "
    "A Jedi's Focus dested A Jedi's Focus. "
    "Lando's Yacht dested Lando's Luxury Yacht. "
    "Lando Cal Unlikely dested Lando Calrissian, Unlikely Hero. "
    "Obi-Wan Kenobi JK dested Obi-Wan Kenobi, Jedi Knight. "
    "Luke JK dested Luke Skywalker, Jedi Knight. "
    "Luke SITF dested Luke Skywalker, Strong In The Force. "
    "LePew dested Nabrun Leids. "
    "Mech Failure dested Mechanical Failure. "
    "Wesa Gotta dested Wesa Gotta Grand Army. "
    "Strike Cover dested Strikeforce. "
    "Projection dested Projection Of A Skywalker. "
    "AJR dested A Jedi's Resilience. "
    "Hear Me Baby dested Hear Me Baby, Hold Together. "
    "Houjix * dested Houjix & Out Of Nowhere. "
    "AFA dested Anger, Fear, Aggression. "
    "Additional Jedi Tests x 6 dested the six Jedi Tests. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name field Baroni dested Steve Baroni. "
    "Username blank. Deck title That's Why She Said. DARK. "
    "HD V dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Coruscant SE dested Coruscant. Cor Imp City dested Coruscant: Imperial City. "
    "Gift of Master dested Gift Of The Master. Blaster Racks dested Blaster Rack. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "Blockade Bridge dested Blockade Flagship: Bridge. "
    "Executor Back Door dested Executor: Docking Bay. "
    "Galen Secret Apprentice dested Galen, Secret Apprentice. "
    "Lord Vader dested Darth Vader, Dark Lord Of The Sith. "
    "DuDlots dested Droideka. Cyborg Commander dested as written. "
    "Dr E & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Mara w Saber dested Mara Jade With Lightsaber. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Boba Fett BH dested Boba Fett, Bounty Hunter. "
    "The Circle Is Now Complete dested The Circle Is Now Complete. "
    "Embrace of Dark Lord dested as written. "
    "Revenge of Sith dested Revenge Of The Sith. "
    "Sniper Dark Strike dested Sniper & Dark Strike. "
    "Galen Fighter dested Rogue Shadow. "
    "Galen's Saber Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Vader's Saber dested Vader's Lightsaber. "
    "Dark Jedi Saber dested Dark Jedi Lightsaber. "
    "4LM With Blaster dested 4-LOM With Concussion Rifle. "
    "Weapon Lev dested Weapon Levitation. "
    "We Must Accelerate Plans dested We Must Accelerate Our Plans. "
    "Emperor's Power dested Emperor's Power. "
    "Code Clearance dested Do They Have A Code Clearance?. "
    "Lack of Faith dested I Find Your Lack Of Faith Disturbing. "
    "Let Fate Decide dested We'll Let Fate-A Decide, Huh?. "
    "You Cannot Hide Forever struck dested Oppressive Enforcement. "
    "YCHF dested You Cannot Hide Forever. "
    "Useless Gesture dested A Useless Gesture. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Mind What You Have Learned / Save You It Can"
LS_CARDS = [
    n("Mind What You Have Learned / Save You It Can", True),
    n("It Is The Future You See", True),
    n("Strong Is Vader"),
    n("Dagobah"),
    n("Luke's Backpack"),
    n("The Way Of Things"),
    n("Daughter Of Skywalker", True),
    n("Yoda", True),
    n("Do, Or Do Not & Wise Advice"),
    n("Battle Plan & Draw Their Fire"),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),
    n("Dagobah: Swamp"),
    n("Dagobah: Jungle"),
    n("Dagobah: Yoda's Hut"),
    n("Qui-Gon's Lightsaber"),
    n("Jedi Lightsaber", True),
    n("Luke's Lightsaber"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("A Jedi's Focus", True),
    n("Lando's Luxury Yacht", True),
    n("Lando Calrissian, Unlikely Hero", True),
    n("Republic Gunship", True, qty=2),
    n("Obi-Wan Kenobi, Jedi Knight", True),
    n("Mace Windu", True, qty=3),
    n("Luke Skywalker, Jedi Knight"),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Master Qui-Gon", True, qty=2),
    n("Corran Horn"),
    n("Nabrun Leids", True, qty=4),
    n("Mechanical Failure", qty=2),
    n("Battle Plan"),
    n("Wesa Gotta Grand Army", qty=2),
    n("Strikeforce", True),
    n("Projection Of A Skywalker"),
    n("Escape Pod", True, qty=3),
    n("A Jedi's Resilience", qty=2),
    n("Hear Me Baby, Hold Together", True),
    n("It Could Be Worse"),
    n("Houjix & Out Of Nowhere", qty=2),
    n("Clash Of Sabers", qty=2),
    n("Weapon Levitation"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Only Jedi Carry That Weapon"),
    n("Yavin Sentry", True),
    n("Traffic Control", True),
    n("Your Insight Serves You Well"),
    n("He Can Go About His Business", True),
    n("Affect Mind", True),
    n("The Professor", True),
    n("Weapons Display", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Simple Tricks And Nonsense", True),
    n("Aim High", True),
    n("A Tragedy Has Occurred"),
]
LS_ADD = [
    n("Don't Do That Again"),
    n("Chasm"),
    n("A Jedi's Focus"),
    n("Great Warrior"),
    n("A Jedi's Strength"),
    n("Domain Of Evil"),
    n("Size Matters Not"),
    n("It Is The Future You See"),
    n("You Must Confront Vader"),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("A Sith's Plans", True),
    n("Coruscant: Imperial City"),
    n("Prepared Defenses", True),
    n("Gift Of The Master", True),
    n("Blaster Rack", True),
    n("Endor Shield", True),
    n("Ni Chuba Na??", True),
    n("Executor"),
    n("Blockade Flagship: Bridge"),
    n("Executor: Docking Bay"),
    n("Galen, Secret Apprentice", True, qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Droideka"),
    n("Cyborg Commander", True, qty=2),
    n("Emperor Palpatine", qty=2),
    n("Dr. Evazan & Ponda Baba"),
    n("Mara Jade With Lightsaber"),
    n("Grand Moff Tarkin", True),
    n("Juno Eclipse, Black Leader", True),
    n("Boba Fett, Bounty Hunter"),
    n("P-59"),
    n("The Circle Is Now Complete", qty=2),
    n("Embrace Of The Dark Lord", True),
    n("Masterful Move"),
    n("Revenge Of The Sith", True),
    n("Force Field", True, qty=2),
    n("Force Lightning"),
    n("Force Push", True),
    n("Protocol Failure", True),
    n("Lightsaber Deficiency", True),
    n("Ghhhk"),
    n("We Must Accelerate Our Plans", qty=3),
    n("Emperor's Power", True),
    n("No Escape"),
    n("Cold Feet", True),
    n("A Sith's Weapon", True),
    n("One Beautiful Thing", True),
    n("Sniper & Dark Strike"),
    n("Victory", True),
    n("Rogue Shadow", True),
    n("Galen's Lightsaber, Vader's Gift", True),
    n("Vader's Lightsaber"),
    n("Dark Jedi Lightsaber", True),
    n("Grand Admiral Thrawn"),
    n("General Veers"),
    n("Blizzard 4", qty=2),
    n("Weapon Levitation"),
    n("4-LOM With Concussion Rifle"),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("We'll Let Fate-A Decide, Huh?"),
    n("Death Star Sentry", True),
    n("Oppressive Enforcement"),
    n("Fanfare"),
    n("Firepower"),
    n("Weapon Of A Sith"),
    n("There Is No Try"),
    n("Allegations Of Corruption", True),
    n("Abyss"),
    n("A Useless Gesture", True),
]
DS_ADD = [
    n("Battle Order"),
    n("Secret Plans"),
    n("You Cannot Hide Forever"),
]
