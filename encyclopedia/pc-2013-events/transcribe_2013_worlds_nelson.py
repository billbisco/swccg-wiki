#!/usr/bin/env python3
"""2013 World Championship Day 2: Aaron Nelson Xerox WYS + Kessel."""
from __future__ import annotations

PLAYER = "Aaron Nelson"
USERNAME = "Airdog2003"
LS_USERNAME = "Airdog2003"
DS_USERNAME = "Airdog2003"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 66
DS_PAGE = 67
LS_SCAN = "2013 Worlds Day 2 p66 Aaron Nelson LS.png"
DS_SCAN = "2013 Worlds Day 2 p67 Aaron Nelson DS.png"
LS_NOTE = (
    "Handwritten 2009 Xerox Print Form (12 shields). Aaron Nelson. Username Airdog2003. "
    "Deck title Old Faithful Virtual. LIGHT checked. "
    "Do not rewrite the 2013 MPC Aaron Nelson leftover (Username hrdog2003). "
    "Do not dest as Jake Nelson. "
    "Watch Your Step (V) dested Watch Your Step (V) / This Place Can Be A Little Rough (V). "
    "Han Solo (V) dested Han Solo (V). Chewie (V) dested Chewie (V). "
    "Antilles Maneuver Combo dested Antilles Maneuver & Rebel Reinforcements. "
    "Tantive IV written over struck Alderaan Consular Ship dested Tantive IV (V). "
    "Spaceport Scoundrels Guild dested Spaceport Scoundrels Guild. "
    "No Questions Asked dested No Questions Asked (V). "
    "Evac Control dested Evacuation Control (V). "
    "Mace Windu, Moto dested Mace Windu, Master Of The Order. "
    "Boshek struck omitted; Superficial Damage dested Superficial Damage (V). "
    "LSJK dested Luke Skywalker, Jedi Knight. "
    "Romas 'Lock' Navander dested Romas 'Lock' Navander. "
    "Escape Pod struck omitted; Desperate Reach dested Desperate Reach (V). "
    "All Wings combo dested All Wings Report In & Darklighter Spin. "
    "Houjix combo dested Houjix & Out Of Nowhere. "
    "Spaceport DB dested Spaceport Docking Bay. "
    "Obi-Wan in Rad VII dested Obi-Wan In Radiant VII. "
    "Leia RP dested Leia, Rebel Princess. Home One DB dested Home One: Docking Bay. "
    "Master QuiGon dested Master Qui-Gon. "
    "Loyal Scoundrel dested Lando Calrissian, Scoundrel. "
    "Wedge Antilles, RSL dested Wedge Antilles, Red Squadron Leader. "
    "Lando's Luxury Yacht dested Lando's Luxury Yacht. "
    "Capt. Han Solo dested Captain Han Solo. "
    "Booster's Destroyer dested Errant Venture. "
    "CEC dested Corellian Engineering Corporation. "
    "Insurrection & Aim High dested Insurrection & Aim High. "
    "AFA dested Anger, Fear, Aggression. "
    "Extra shield 13 Your Ship? dested Your Ship?. "
    "Extra shield 14 Affect Mind dested Affect Mind (V). "
    "Form left column reprints 37-38 on lines 39-40 overwritten with Home One DB and Dash Rendar. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Aaron Nelson. Username Airdog2003. "
    "Deck title Slightly Spicy. DARK. "
    "Do not rewrite the 2013 MPC Aaron Nelson leftover. "
    "Kessel: Spice Mine - Admin Office dested Kessel: Spice Mines - Administrator's Office. "
    "Kessel: Spice Mine - Prison dested Kessel: Spice Mines - Prison. "
    "Kessel: Spice Mine - Docking Bay dested Kessel: Spice Mines - Docking Bay. "
    "Blockade Flagship Bridge dested Blockade Flagship: Bridge. "
    "EP1 Maul dested Darth Maul With Lightsaber. "
    "Darth Vader, DLOTS dested Darth Vader, Dark Lord Of The Sith. "
    "Darth Vader, Betrayer of the Jedi dested Darth Vader, Betrayer Of The Jedi. "
    "The Mandalorian FOF dested The Mandalorian. "
    "Moynleyneugh dested as written. "
    "Emperor Palpatine struck on line 20; The Emperor dested The Emperor (V). "
    "Spice Mine Administrator dested as written. "
    "Galen's Lightsaber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Slave I SoF dested Slave I, Symbol Of Fear. "
    "Plan B written over struck Begin Landing Your Troops & TDF dested Plan B. "
    "Begin Landing / Planetary Justice line 36 fully struck omitted. "
    "Sniper & Dark Strike struck omitted; Alter dested Alter. "
    "Short Range Fighters combo dested Short Range Fighters & Watch Your Back!. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "Masterful Move combo dested Masterful Move & Endor Occupation. "
    "Where Are You Taking This ... Thing? dested Where Are You Taking This ... Thing?. "
    "Ni Chuba Na dested Ni Chuba Na??. "
    "Additional Death Star Sentry / Abyss / A Useless Gesture moved to Dark shields. "
    "Form left column reprints 37-38 on lines 39-40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Millennium Falcon", True),
    n("Han Solo", True),
    n("Chewie", True),
    n("Antilles Maneuver & Rebel Reinforcements", qty=2),
    n("Mirax Terrik"),
    n("Tantive IV", True),
    n("Corran Horn"),
    n("Sense", qty=2),
    n("Spaceport Street"),
    n("Antilles Maneuver", True),
    n("Imperial Atrocity", True),
    n("Spaceport Scoundrels Guild"),
    n("Punch It!"),
    n("Rebel Barrier"),
    n("No Questions Asked", True, qty=3),
    n("Evacuation Control", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("Mace Windu, Master Of The Order"),
    n("Palejo Reshad"),
    n("Superficial Damage", True),
    n("Luke Skywalker, Jedi Knight", qty=2),
    n("Romas 'Lock' Navander"),
    n("Desperate Reach", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Houjix & Out Of Nowhere"),
    n("Spaceport Docking Bay"),
    n("Punch It!"),
    n("Obi-Wan In Radiant VII"),
    n("Dash Rendar", True),
    n("Leia, Rebel Princess"),
    n("Home One: Docking Bay"),
    n("Dash Rendar", True),
    n("Master Qui-Gon", True),
    n("Lando Calrissian, Scoundrel"),
    n("Corellian Retort", True),
    n("Fallen Jedi"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Lando's Luxury Yacht"),
    n("Booster Terrik"),
    n("Captain Han Solo"),
    n("Seeking An Audience", True),
    n("Errant Venture"),
    n("Menace Fades"),
    n("K'lor'slug"),
    n("Mercenary Armor", True),
    n("That's One", True),
    n("Demotion", True),
    n("Han's Toolkit", True),
    n("Rycar Ryjerd", True),
    n("Corellian Engineering Corporation", True),
    n("Insurrection & Aim High"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Wise Advice"),
    n("Simple Tricks And Nonsense"),
    n("Yavin Sentry", True),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred", True),
    n("Chasm", True),
    n("Battle Plan", True),
    n("The Professor", True),
    n("Your Ship?"),
    n("Affect Mind", True),
]
LS_ADD = []


DS_START = "Kessel"
DS_CARDS = [
    n("Kessel"),
    n("Kessel: Spice Mines - Administrator's Office"),
    n("Kessel: Spice Mines - Prison"),
    n("Kessel: Spice Mines - Docking Bay"),
    n("Cloud City: Security Tower", True),
    n("Blockade Flagship: Bridge"),
    n("Lord Sidious", qty=2),
    n("Galen, Secret Apprentice", qty=2),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Darth Maul With Lightsaber", qty=2),
    n("Arica"),
    n("Boba Fett, Prepared Hunter"),
    n("The Mandalorian"),
    n("Moynleyneugh", True),
    n("Emperor Palpatine"),
    n("The Emperor", True),
    n("Spice Mine Administrator"),
    n("Garindan", True),
    n("Vader's Lightsaber"),
    n("Sidious' Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Slave I, Symbol Of Fear"),
    n("Maul's Sith Infiltrator"),
    n("Kessel Surveillance System"),
    n("Presence Of The Force"),
    n("Plan B"),
    n("Protocol Failure"),
    n("Jabba's Haven"),
    n("Special Delivery", True),
    n("Disarmed"),
    n("Imperial Justice", True),
    n("Much Anger In Him"),
    n("Spice Mine Operations"),
    n("Blaster Rack", True),
    n("Sense"),
    n("Short Range Fighters & Watch Your Back!", qty=2),
    n("Ghhhk"),
    n("Alter", True),
    n("Sonic Bombardment", True, qty=2),
    n("Force Field", True, qty=2),
    n("We Must Accelerate Our Plans", qty=2),
    n("Lightsaber Deficiency", True),
    n("Masterful Move & Endor Occupation"),
    n("Force Lightning"),
    n("Force Push", True),
    n("Where Are You Taking This ... Thing?"),
    n("Combat Readiness", True),
    n("I'll Take Them Myself"),
    n("Gift Of The Master"),
    n("Ni Chuba Na??", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("There Is No Try"),
    n("Do They Have A Code Clearance?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Battle Order", True),
    n("Secret Plans"),
    n("Allegations Of Corruption", True),
    n("You Cannot Hide Forever", True),
    n("Resistance"),
    n("Firepower", True),
    n("Weapon Of A Sith"),
    n("Fanfare", True),
    n("Come Here You Big Coward"),
    n("Death Star Sentry", True),
    n("Abyss", True),
    n("A Useless Gesture", True),
]
DS_ADD = []
