#!/usr/bin/env python3
"""2013 Match Play Championship Day 1: Cuong Nguyen Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Cuong Nguyen"
USERNAME = "OmegaXen"
STAGE = "Day 1"
PDF = "2013 Match Play Championship.pdf"
LS_PAGE = 66
DS_PAGE = 65
LS_SCAN = "2013 Match Play Championship p66 Cuong Nguyen LS.png"
DS_SCAN = "2013 Match Play Championship p65 Cuong Nguyen DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Cuong Nguyen (username OmegaXen). Light. "
    "Deck title Lando Unchained. "
    "MWYHL WYS dested Watch Your Step / This Place Can Be A Little Rough "
    "(sheet abbreviation; the list is Corellia / General Solo / Falcon / spaceport sites). "
    "General Solo dested General Solo. Medical Frigate (Starting Interrupt) dested "
    "Heading For The Medical Frigate. CEC dested Corellian Engineering Corporation. "
    "Obi w/ saber dested Obi-Wan With Lightsaber. Qui-Gon w/ saber dested Qui-Gon Jinn With Lightsaber. "
    "Corian Horn dested Corran Horn. Boshek dested BoShek. Harr Seff dested Harc Seff. "
    "Threepio w/ Parts Showing dested Threepio With His Parts Showing. "
    "Artoo in Red 5 dested Artoo-Detoo In Red 5. Booster In Pulsar Skate as written. "
    "Boshek's Modified Light Freighter dested YT-1300 Transport. "
    "Home One Docking Bay dested Home One: Docking Bay. "
    "Spaceport Scoundrel's Guild dested Spaceport Scoundrels Guild. "
    "Caso Nector kept as written (unknown). Fallen Jedi dested Maris Brood, Fallen Jedi. "
    "Antilles Maneuver / Rebel Reinforcements dested Antilles Maneuver & Rebel Reinforcements. "
    "Yub Yub Commander dested Yub Yub, Commander. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Another Pathetic Lifeform dested Another Pathetic Lifeform. "
    "Do or do not dested Do, Or Do Not. Let's Keep A Little Optimism dested "
    "Let's Keep A Little Optimism Here. "
    "Form left column reprints 37–38 on lines 39–40 are Home One: Docking Bay and Spaceport Docking Bay. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Cuong Nguyen (username OmegaXen). Dark. "
    "Deck title Cloud City Bitch Cloud Cloud City Bitch. "
    "Carbon Chamber Testing / My Favorite… dested Carbon Chamber Testing / My Favorite Decoration. "
    "According To My Design dested According To My Design. T I'm Sorry dested I'm Sorry. "
    "CC: Carbonite Chamber dested Cloud City: Carbonite Chamber. "
    "Jabba's Prize dested Jabba's Prize / Jabba's Prize. Darth Vader / Betrayer dested "
    "Darth Vader, Betrayer Of The Jedi. Ice-Heart dested Ysanne Isard. "
    "The Emperor's Reach dested Maarek Stele, The Emperor's Reach. "
    "Captain Gilad Pellaeon dested Captain Gilad Pellaeon. "
    "General Nevar dested General Nevar. Corporal Danduran dested Corporal Drazin. "
    "Command Praji dested Commander Praji. OS-72-1 in Obsidian 1 dested OS-72-1 In Obsidian 1. "
    "OS-72-2 in Obsidian 2 dested OS-72-2 In Obsidian 2. "
    "Obsidian Squadron TIE dested Obsidian Squadron TIE. "
    "Vader's Saber dested Vader's Lightsaber. Mara's Saber dested Mara Jade's Lightsaber. "
    "Floating Refinery dested Tibanna Floating Refinery. "
    "Talon Roll / Dark Maneuvers and Dark Maneuvers / Talon Roll dested Dark Maneuvers & Tallon Roll. "
    "All Power To Weapons x3 occupies lines 50–51 only (qty 2). "
    "Sniper and Dark Strike as separate lines. "
    "Form left column reprints 37–38 on lines 39–40 are Clouds and A Dark Time For The Rebellion. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough", True),
    n("General Solo", True),
    n("Millennium Falcon", True),
    n("Corellia", True),
    n("Spaceport City"),
    n("Heading For The Medical Frigate"),
    n("Insurrection"),
    n("Corellian Engineering Corporation", True),
    n("Menace Fades"),
    n("Seeking An Audience", True),
    n("Scrambled Transmission", True),
    n("Squadron Assignments"),
    n("Obi-Wan With Lightsaber"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Yoda, Great Warrior"),
    n("Luke Skywalker", True),
    n("Lando Calrissian, Scoundrel", True),
    n("Chewie", True),
    n("Corporal Marmor"),
    n("Romas 'Lock' Navander"),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Corran Horn"),
    n("Dash Rendar", True),
    n("Mirax Terrik"),
    n("BoShek", True),
    n("Harc Seff"),
    n("Laudica", True),
    n("Palejo Reshad"),
    n("Threepio With His Parts Showing"),
    n("Artoo-Detoo In Red 5"),
    n("Outrider"),
    n("Booster In Pulsar Skate", True),
    n("YT-1300 Transport", True),
    n("Han's Toolkit", True),
    n("Fusion Generator Supply Tanks", True),
    n("No Questions Asked", True, qty=3),
    n("Home One: Docking Bay"),
    n("Spaceport Docking Bay"),
    n("Spaceport Street"),
    n("Spaceport Scoundrels Guild", True),
    n("Caso Nector"),
    n("Corellian Retort", True, qty=2),
    n("Life Debt", qty=2),
    n("Rebel Barrier", qty=2),
    n("Let The Wookiee Win", True, qty=3),
    n("It's A Hit!"),
    n("Punch It!"),
    n("Maris Brood, Fallen Jedi", True),
    n("Honor Of The Jedi"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("Antilles Maneuver", True),
    n("Yub Yub, Commander"),
    n("Anger, Fear, Aggression"),
]
LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Don't Do That Again", True),
    n("Another Pathetic Lifeform", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Your Insight Serves You Well"),
    n("Do, Or Do Not"),
    n("Let's Keep A Little Optimism Here"),
    n("Wise Advice"),
]
LS_ADD = []

DS_START = "Carbon Chamber Testing / My Favorite Decoration"
DS_CARDS = [
    n("Carbon Chamber Testing / My Favorite Decoration"),
    n("According To My Design", True),
    n("The Emperor", True),
    n("I'm Sorry", True),
    n("Endor Shield", True),
    n("Special Delivery", True),
    n("Carbonite Chamber Console"),
    n("Cloud City: Carbonite Chamber"),
    n("Cloud City: Security Tower", True),
    n("Jabba's Prize / Jabba's Prize"),
    n("Lord Vader"),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Arica"),
    n("Grand Admiral Thrawn"),
    n("Grand Moff Tarkin", True),
    n("Ysanne Isard", True),
    n("Maarek Stele, The Emperor's Reach"),
    n("Captain Gilad Pellaeon"),
    n("Admiral Chiraneau"),
    n("General Nevar", True),
    n("Corporal Drazin", True),
    n("Admiral Ozzel"),
    n("Commander Praji", True),
    n("ISB Sector Commander", True),
    n("Sergeant Wallen", True),
    n("Executor"),
    n("Chimaera"),
    n("OS-72-1 In Obsidian 1"),
    n("OS-72-2 In Obsidian 2"),
    n("Obsidian 7"),
    n("Obsidian Squadron TIE", qty=3),
    n("Vader's Lightsaber"),
    n("Mara Jade's Lightsaber", True),
    n("Tibanna Floating Refinery", True),
    n("Bespin", True),
    n("Storm Clouds", True),
    n("Clouds"),
    n("A Dark Time For The Rebellion", True, qty=2),
    n("Blaster Rack", True),
    n("Imperial Domination", True),
    n("Imperial Arrest Order"),
    n("Imperial Decree", True),
    n("Come With Me", True),
    n("Image Of The Dark Lord"),
    n("Dark Maneuvers & Tallon Roll", qty=2),
    n("All Power To Weapons", qty=2),
    n("Imperial Barrier"),
    n("Cold Feet", True),
    n("Dark Strike"),
    n("Sniper"),
    n("Sense", qty=2),
    n("Ghhhk"),
    n("Despair"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Firepower", True),
    n("You Cannot Hide Forever", True),
    n("Abyss", True),
    n("Secret Plans", True),
    n("Resistance"),
    n("Oppressive Enforcement"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?"),
    n("There Is No Try"),
    n("A Useless Gesture"),
]
DS_ADD = []
