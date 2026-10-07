#!/usr/bin/env python3
"""2014 Match Play Championship Day 1 Print Form: Joe Gagliardi.

Source: MPC-2014-Day-1-Main-Event.pdf pages 41–42 (2013 Print Form).
Username DVMABA22. Name Joseph Gagliardi dested Joe Gagliardi.
"""
from __future__ import annotations

PLAYER = "Joe Gagliardi"
USERNAME = "DVMABA22"
STAGE = "Day 1"
PDF = "2014 Match Play Championship Day 1.pdf"
LS_PAGE = 42
DS_PAGE = 41
LS_SCAN = "2014 Match Play Championship Day 1 Joe Gagliardi LS.png"
DS_SCAN = "2014 Match Play Championship Day 1 Joe Gagliardi DS.png"
LS_DECK_NAME = "Cooper Cheese"
DS_DECK_NAME = "Sicilian Pizza"
NOTE = "Typed 2013 Print Form."
LS_NOTE = (
    "Typed 2013 Print Form. Username DVMABA22. Deck name Cooper Cheese. Hidden Base. "
    "Line 14 crossed, Surprise Assault dested Surprise Assault. antilles Manueer dested "
    "Antilles Maneuver & Rebel Reinforcements. Houjix & Out of nowhere dested Houjix & "
    "Out Of Nowhere. Sorry about the mess / Blaster Prof dested Sorry About The Mess & "
    "Blaster Proficiency. The Planet that it's farthest from dested The Planet That's "
    "Farthest From. You will take me to Yavin Now dested You Will Take Me To Jabba Now. "
    "Hidden Fortress ADD CU dested Corulag, Kif dested Kiffex. (V) from checkbox. Unique "
    "overcounts sheet-accurate (X-wing x8, Hyper Escape x2, Rebel Barrier x2, Houjix & "
    "Out Of Nowhere x2, It Could Be Worse x2, Kessel Run x2, All Wings Report In x2, "
    "Darklighter Spin (V) x2, X-wing Laser Cannon x2)."
)
DS_NOTE = (
    "Typed 2013 Print Form. Username DVMABA22. Deck name Sicilian Pizza. Hunt Down And "
    "Destroy The Jedi empty (V). YCHF / Mob Points dested You Cannot Hide Forever & "
    "Mobilization Points. IAO / Secret Plans dested Imperial Arrest Order & Secret Plans. "
    "Sniper / Dark Strike dested Sniper & Dark Strike. Omni Box / Its Worse dested Omni "
    "Box & It's Worse. Ghyyk / those rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Grevious dested Grievous, Hunter Of Jedi. Darth Vader DLOTS dested Darth Vader, Dark "
    "Lord Of The Sith. Boba fett in Slave 1 dested Boba Fett In Slave I. (V) from checkbox. "
    "Unique overcounts sheet-accurate (Visage Of The Emperor x2, Vader's Anger (V) x2, "
    "Darth Vader, Dark Lord Of The Sith x3, Darth Maul, Young Apprentice x2, Mara Jade "
    "With Lightsaber (V) x2, Do They Have A Code Clearance? (V) x2)."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Hidden Base / Systems Will Slip Through Your Fingers"
LS_CARDS = [
    n("Hidden Base / Systems Will Slip Through Your Fingers"),
    n("Rendezvous Point"),
    n("Heading For The Medical Frigate"),
    n("Anger, Fear, Aggression", True),
    n("Get To Your Ships"),
    n("We Didn't Hit It"),
    n("Hidden Fortress", True),
    n("Legendary Starfighter"),
    n("Dash Rendar"),
    n("Antilles Maneuver & Rebel Reinforcements", True),
    n("X-wing", qty=3),
    n("Surprise Assault"),
    n("Organized Attack"),
    n("BoShek", True),
    n("Rebel Barrier"),
    n("Hyper Escape"),
    n("The Bith Shuffle & Desperate Reach"),
    n("Endor"),
    n("Jek Porkins"),
    n("X-wing"),
    n("Han, Chewie, And The Falcon", True),
    n("Aquaris"),
    n("Rebel Barrier"),
    n("X-wing"),
    n("Kessel Run"),
    n("Houjix & Out Of Nowhere"),
    n("Hyper Escape"),
    n("Naboo"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("X-wing"),
    n("Mirax Terrik"),
    n("Luke Skywalker", True),
    n("Red Leader In Red 1"),
    n("All Wings Report In"),
    n("Coruscant"),
    n("Darklighter Spin", True),
    n("Rycar Ryjerd", True),
    n("Pulsar Skate", True),
    n("Red 6"),
    n("Boushh"),
    n("Artoo-Detoo In Red 5"),
    n("It Could Be Worse"),
    n("It's A Hit"),
    n("Houjix & Out Of Nowhere"),
    n("It Could Be Worse"),
    n("Kessel"),
    n("All Wings Report In"),
    n("Honor Of The Jedi"),
    n("Kessel Run"),
    n("X-wing Laser Cannon"),
    n("The Planet That's Farthest From", True),
    n("Darklighter Spin", True),
    n("Medium Bulk Freighter", True),
    n("X-wing Laser Cannon"),
    n("Starship Levitation", True),
    n("Outrider", True),
    n("X-wing", qty=2),
]
LS_SHIELDS = [
    n("Battle Plan"),
    n("Traffic Control", True),
    n("Another Pathetic Lifeform", True),
    n("Chasm", True),
    n("Ultimatum"),
    n("Your Insight Serves You Well", True),
    n("Do, Or Do Not", True),
    n("Yavin Sentry", True),
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Don't Do That Again", True),
    n("Ounee Ta", True),
    n("You Will Take Me To Jabba Now", True),
    n("The Professor", True),
    n("Affect Mind", True),
]
LS_ADD = [
    n("Corulag"),
    n("Kiffex"),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"),
    n("Executor: Holotheater"),
    n("Executor: Meditation Chamber"),
    n("Visage Of The Emperor"),
    n("You Cannot Hide Forever & Mobilization Points"),
    n("Imperial Arrest Order & Secret Plans"),
    n("Blaster Rack", True),
    n("Knowledge And Defense", True),
    n("Prepared Defenses"),
    n("Sith Fury", True),
    n("Zuckuss In Mist Hunter"),
    n("Lateral Damage"),
    n("Mara Jade With Lightsaber", True),
    n("Sniper & Dark Strike"),
    n("IG-88 With Riot Gun"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("I Am Your Father", True),
    n("Imperial Barrier"),
    n("I Have You Now"),
    n("Vader's Anger", True),
    n("Carida"),
    n("Cloud City: East Platform (Docking Bay)"),
    n("Weapon Levitation"),
    n("Force Field"),
    n("Masterful Move"),
    n("Dengar With Blaster Carbine", True),
    n("Darth Maul, Young Apprentice"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Arica", True),
    n("Darth Vader With Lightsaber"),
    n("Focused Attack"),
    n("Dark Jedi Lightsaber", True),
    n("Grievous, Hunter Of Jedi", True),
    n("Search And Destroy"),
    n("Projective Telepathy"),
    n("Aurra Sing", True),
    n("No Escape"),
    n("Vader's Lightsaber", True),
    n("Bossk In Hound's Tooth"),
    n("Boba Fett In Slave I", True),
    n("Vader's Anger", True),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("First Strike"),
    n("You Are Beaten"),
    n("Disarmed"),
    n("Visage Of The Emperor"),
    n("Kir Kanos With Force Pike", True),
    n("The Emperor", True),
    n("Put All Sections On Alert", True),
    n("Darth Maul, Young Apprentice"),
    n("Death Star: Docking Bay 327"),
    n("Maul's Sith Infiltrator"),
    n("Prince Xizor"),
    n("Omni Box & It's Worse"),
    n("Mara Jade With Lightsaber", True),
    n("Twi'lek Advisor"),
    n("Limited Resources"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Dr. Evazan & Ponda Baba"),
    n("Maul's Double-Bladed Lightsaber"),
]
DS_SHIELDS = [
    n("Do They Have A Code Clearance?", True),
    n("Fanfare", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("Come Here You Big Coward", True),
    n("Allegations Of Corruption"),
    n("Abyss", True),
    n("Firepower", True),
    n("Resistance"),
    n("Death Star Sentry", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Reactor Terminal"),
    n("Battle Order"),
    n("Do They Have A Code Clearance?", True),
    n("Crossfire"),
]
DS_ADD = []
