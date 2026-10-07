#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: Bobby Hilbun Xerox Ralltiir Ops / Communing."""
from __future__ import annotations

PLAYER = "Bobby Hilbun"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 17
DS_PAGE = 16
LS_SCAN = "2013 Texas Mini Worlds Day 1 p17 Bobby Hilbun LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p16 Bobby Hilbun DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Bobby Hilbun. Username blank. "
    "Deck Name Communichkin. LIGHT checked. "
    "Autow Nedow in Red 5 dested Artoo-Detoo In Red 5. "
    "Sorry Combo dested Sorry About The Mess & Blaster Proficiency. "
    "Threepio w/ parts dested Threepio With His Parts Showing. "
    "Chewbacca's Crossbow dested Chewbacca's Bowcaster. "
    "Tat: Obi Hut dested Tatooine: Obi-Wan's Hut. "
    "Luke SS LTF dested Luke Skywalker, Strong In The Force. "
    "Chewie Enraged dested Chewie, Enraged. "
    "Yoda Great Warrior dested Yoda, Great Warrior. "
    "Padme Naberrie dested Padme Naberrie. "
    "Artiller Maneuver dested Antilles Maneuver. "
    "Run Luke Run dested Run Luke, Run!. "
    "Han epp dested Captain Han Solo. "
    "Tatooine ep 4 dested Tatooine. "
    "Let The Wookiee Win line 45 unchecked, line 46 (V) checked dested separately. "
    "Use The Force line 23 (V) checked, line 60 unchecked dested separately. "
    "Insight Serve you well dested Your Insight Serves You Well. "
    "The Prof dested The Professor. "
    "Clue dested Chasm. "
    "Keep a little optimism dested Let's Keep A Little Optimism Here. "
    "Simple Tricks dested Simple Tricks And Nonsense. "
    "Tragedy dested A Tragedy Has Occurred. "
    "Only Jedi Carry dested Only Jedi Carry That Weapon. "
    "Unique overcounts sheet-accurate: Blaster Deflection x2, "
    "Sorry About The Mess & Blaster Proficiency x3, Power Pivot x2, Red 6 x2, "
    "Luke Skywalker, Strong In The Force x3, Chewie, Enraged x2, "
    "Luke's Bionic Hand x2, Run Luke, Run! x2, Rebel Artillery x2, "
    "Captain Han Solo x2, Artoo-Detoo In Red 5 x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Name Bobby Hilbun. Username blank. "
    "Deck Name Ral OPS. DARK checked. "
    "Ralltiir Ops / In the Hands dested Ralltiir Operations / In The Hands Of The Empire. "
    "Why Didn't You Tell Me dested Why Didn't You Tell Me?. "
    "Spaceport Street dested Spaceport Street. "
    "Control + Set For Stun dested Control & Set For Stun. "
    "Lt Commander Ardan dested Lieutenant Commander Ardan. "
    "Imbalance / Kintan Strider dested Imbalance & Kintan Strider. "
    "Avica dested Arica. "
    "Spaceport Docking Bay dested Spaceport Docking Bay. "
    "Spaceport Prefect's Office dested Spaceport Prefect's Office. "
    "Masterful Move / Endor Occ dested Masterful Move & Endor Occupation. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "Occupier dested Occupier as written. "
    "Ghhhk + Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "Darth Vader lots dested Darth Vader, Dark Lord Of The Sith. "
    "Col. Davod Jon dested Colonel Davod Jon. "
    "Imperial Dom dested Imperial Domination. "
    "Gen. Veers dested General Veers. "
    "Darth Vader BOTJ dested Darth Vader, Betrayer Of The Jedi. "
    "Ralltiir: Spaceport Financial dested Ralltiir: Spaceport Financial District. "
    "Kir Kanos w/ Forcepike dested Kir Kanos With Force Pike. "
    "Ice-Heart dested Ysanne Isard. "
    "Where are you taking this thing dested Where Are You Taking This ... Thing?. "
    "Emperor Reach dested Maarek Stele, The Emperor's Reach. "
    "Abyss dested Abyss. "
    "Useless Gesture dested A Useless Gesture. "
    "Wipe Them Out dested Wipe Them Out, All Of Them. "
    "We'll Let Fate dested We'll Let Fate-A Decide, Huh?. "
    "You Cannot Hide Forever dested You Cannot Hide Forever. "
    "Oppressive enforcement dested Oppressive Enforcement. "
    "There is no try dested There Is No Try. "
    "After Her dested After Her!. "
    "Unique overcounts sheet-accurate: Close Call x2, Why Didn't You Tell Me? x2, "
    "A Dark Time For The Rebellion x2, Emperor Palpatine x2, Outflank x2, "
    "Imperial Command x2, Imperial Domination x2. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Communing"
LS_CARDS = [
    n("Artoo-Detoo In Red 5"),
    n("Blaster Deflection", qty=2),
    n("Sorry About The Mess & Blaster Proficiency", qty=3),
    n("Threepio With His Parts Showing"),
    n("Luke's Lightsaber"),
    n("Jek Porkins", True),
    n("Amidala's Blaster"),
    n("Chewbacca's Bowcaster"),
    n("Tatooine: Cantina"),
    n("Tatooine: City Outskirts"),
    n("Tatooine: Slave Quarters"),
    n("Tatooine: Obi-Wan's Hut"),
    n("Power Pivot", qty=2),
    n("Red 6", qty=2),
    n("Luke Skywalker, Strong In The Force", True, qty=3),
    n("Use The Force", True),
    n("Chewie, Enraged", True, qty=2),
    n("Superficial Damage", True),
    n("Master Kenobi", True),
    n("Luke's Bionic Hand", True, qty=2),
    n("Yoda, Great Warrior", True),
    n("Padme Naberrie", True),
    n("Princess Leia", True),
    n("Antilles Maneuver", True),
    n("Communing", True),
    n("Imperial Atrocity", True),
    n("Seeking An Audience", True),
    n("Scrambled Transmission", True),
    n("Escape Pod", True),
    n("Sai'torr Kal Fas", True),
    n("Quick Draw", True),
    n("Run Luke, Run!", True, qty=2),
    n("Leia's Sporting Blaster", True),
    n("Jedi Lightsaber", True),
    n("Let The Wookiee Win"),
    n("Let The Wookiee Win", True),
    n("Houjix"),
    n("Rebel Artillery", qty=2),
    n("X-wing Laser Cannon"),
    n("Disarmed"),
    n("Weapon Levitation"),
    n("Captain Han Solo", qty=2),
    n("Draw Their Fire"),
    n("Tatooine"),
    n("Lando Calrissian, Scoundrel"),
    n("Artoo-Detoo In Red 5"),
    n("Anger, Fear, Aggression", True),
    n("Use The Force"),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Wise Advice"),
    n("Battle Plan"),
    n("Aim High"),
    n("The Professor", True),
    n("Your Insight Serves You Well", True),
    n("Ultimatum"),
    n("Affect Mind", True),
    n("Yavin Sentry", True),
    n("Don't Do That Again", True),
    n("Chasm", True),
    n("Simple Tricks And Nonsense", True),
]
LS_ADD = [
    n("A Tragedy Has Occurred"),
    n("Weapons Display", True),
    n("Only Jedi Carry That Weapon"),
]

DS_START = "Ralltiir Operations / In The Hands Of The Empire"
DS_CARDS = [
    n("Ralltiir Operations / In The Hands Of The Empire"),
    n("Janus Greejatus"),
    n("Close Call", True),
    n("Why Didn't You Tell Me?", True),
    n("A Dark Time For The Rebellion", True),
    n("Spaceport Street"),
    n("Emperor Palpatine"),
    n("Something Special Planned For Them", True),
    n("Garindan", True),
    n("Victory", True),
    n("Conquest", True),
    n("Ghhhk"),
    n("Control & Set For Stun"),
    n("Cold Feet", True),
    n("Outflank", True),
    n("Lieutenant Commander Ardan"),
    n("A Dark Time For The Rebellion", True),
    n("Why Didn't You Tell Me?", True),
    n("Imperial Barrier"),
    n("Close Call", True),
    n("Imbalance & Kintan Strider", True),
    n("Emperor Palpatine"),
    n("Imperial Command"),
    n("Trample"),
    n("Imperial Justice", True),
    n("Arica"),
    n("Spaceport Docking Bay"),
    n("Spaceport Prefect's Office"),
    n("Outflank", True),
    n("Masterful Move & Endor Occupation"),
    n("Grand Admiral Thrawn"),
    n("Knowledge And Defense", True),
    n("Occupier"),
    n("Admiral Ozzel"),
    n("Blizzard 1", True),
    n("Admiral Motti", True),
    n("Prepared Defenses"),
    n("Tempest 1"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Devastator", True),
    n("Grand Moff Tarkin"),
    n("Darth Vader, Dark Lord Of The Sith"),
    n("Colonel Davod Jon"),
    n("Imperial Command"),
    n("Blizzard 4"),
    n("Imperial Domination", True),
    n("Ralltiir"),
    n("General Veers", True),
    n("Blizzard 2", True),
    n("Endor"),
    n("Imperial Domination", True),
    n("Kuat Drive Yards", True),
    n("Insignificant Rebellion", True),
    n("Endor Shield", True),
    n("Darth Vader, Betrayer Of The Jedi", True),
    n("Ralltiir: Spaceport Financial District"),
    n("Kir Kanos With Force Pike", True),
    n("Ysanne Isard", True),
    n("Where Are You Taking This ... Thing?", True),
    n("Maarek Stele, The Emperor's Reach", True),
]
DS_SHIELDS = [
    n("Abyss"),
    n("Secret Plans"),
    n("Battle Order"),
    n("A Useless Gesture", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Wipe Them Out, All Of Them", True),
    n("Fanfare"),
    n("Allegations Of Corruption"),
    n("Firepower", True),
    n("We'll Let Fate-A Decide, Huh?", True),
    n("You Cannot Hide Forever", True),
]
DS_ADD = [
    n("Oppressive Enforcement"),
    n("There Is No Try", True),
    n("After Her!", True),
]
