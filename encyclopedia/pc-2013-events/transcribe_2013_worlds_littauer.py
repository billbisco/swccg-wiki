#!/usr/bin/env python3
"""2013 World Championship Day 1: Ross Littauer Xerox LS+DS."""
from __future__ import annotations

PLAYER = "Ross Littauer"
USERNAME = ""
STAGE = "Day 1"
PDF = "2013 Worlds Day 1.pdf"
LS_PAGE = 6
DS_PAGE = 5
LS_SCAN = "2013 Worlds Day 1 p06 Ross Littauer LS.png"
DS_SCAN = "2013 Worlds Day 1 p05 Ross Littauer DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Ross Littauer. Username blank. "
    "Email Ross.Littauer. Event World Champs Day 1, dated 08/09/13. "
    "Deck title Stuff. LIGHT. "
    "Dap-stration / New Hope Allies dested Infiltration / Unlikely Allies. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Rebel Agent dested Kyle Katarn. Rebel Agent's Blaster Rifle dested Kyle Katarn's Blaster Rifle. "
    "JATM / blaster pack dested Kyle Katarn's Blaster Rifle. "
    "Boushh's Staff Destroyed dested Boushh. "
    "Imperial Navy Charts dested Imperial Navigation Charts. "
    "Scoundrel's Guild dested Spaceport Scoundrels Guild. "
    "Scoundrel's Perk dested Nar Shaddaa: Scoundrel's Rest. "
    "ICBZ dested as written. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form. Ross Littauer. Username blank. "
    "Email Ross.Littauer. Event Worlds Day 1, dated 08/09/13. "
    "Deck title Norsense. DARK. "
    "Hunt Down / Their Fire has gone out dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "A Sith's Plans and Gift Of The Master have the (V) box struck; dested without (V). "
    "p59 struck (V) dested P-59. "
    "Weapon Lev & Emperor's luck dested Weapon Levitation & The Empire's Back. "
    "Masterful Move / Galactic Evolution dested Masterful Move & Endor Occupation. "
    "Vengeance of the Sith dested as written. "
    "Vengeance w/ Lightsaber Combine dested Dengar With Blaster Carbine. "
    "Galen, Secret Apprentice dested Galen Marek, Starkiller. "
    "Galen's Fighter dested Rogue Shadow. Black Leader dested Juno Eclipse, Black Leader. "
    "Commander dested as written. "
    "Imperial Gesture dested Imperial Justice. "
    "Alter last shield dested Alter. "
    "Form left column reprints 37–38 on lines 39–40. "
    "(V) from the checkbox; dittos inherit the first named line."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies"),
    n("Anger, Fear, Aggression", True),
    n("Scoundrel's Luck"),
    n("Scoundrel's Bravado"),
    n("Scoundrel's Charm"),
    n("Scoundrel's Ingenuity"),
    n("Nar Shaddaa"),
    n("Nar Shaddaa: Undercity"),
    n("Heading For The Medical Frigate"),
    n("Kyle Katarn", qty=3),
    n("Wokling", True),
    n("Imperial Navigation Charts"),
    n("A Good Blaster At Your Side"),
    n("Sai'torr Kal Fas", True),
    n("Scrambled Transmission", True),
    n("Escape Pod", True, qty=2),
    n("Obi-Wan In Radiant VII"),
    n("Corran Horn", qty=2),
    n("Seeking An Audience", True),
    n("Booster Terrik", qty=2),
    n("Booster In Pulsar Skate"),
    n("Houjix"),
    n("Mirax Terrik"),
    n("Chewbacca's Bowcaster"),
    n("Chewbacca, Walking Carpet", qty=2),
    n("Boushh"),
    n("K'lor'slug", True),
    n("Nar Shaddaa: Undercity Street"),
    n("Inconsequential Barriers"),
    n("We Wish To Board At Once", qty=2),
    n("Lando's Luxury Yacht"),
    n("Leia's Blaster Rifle"),
    n("Kyle Katarn's Blaster Rifle"),
    n("Han's Toolkit"),
    n("ICBZ", True),
    n("Han Solo, Innocent Scoundrel", qty=2),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("All Wings Report In & Darklighter Spin"),
    n("Han's Heavy Blaster Pistol"),
    n("Sergeant Doallyn", True),
    n("Landing Claw"),
    n("Either Way, You Win", True),
    n("Redeemed Apprentice", True),
    n("I Can't Believe He's Gone", True),
    n("Spaceport Scoundrels Guild"),
    n("Nar Shaddaa: Scoundrel's Rest"),
    n("Imperial Atrocity", True),
    n("Much To Learn, You Still Have"),
    n("Kyle Katarn's Blaster Rifle"),
    n("Let The Wookiee Win", True),
    n("Armed And Dangerous & Krayt Dragon Howl"),
]
LS_SHIELDS = [
    n("Battle Plan", True),
    n("Chasm", True),
    n("A Tragedy Has Occurred"),
    n("Aim High"),
    n("Weapons Display", True),
    n("Yavin Sentry", True),
    n("He Can Go About His Business", True),
    n("Your Insight Serves You Well", True),
    n("Wise Advice", True),
    n("Don't Do That Again", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
]
LS_ADD = [
    n("Ultimatum"),
    n("Affect Mind"),
    n("Simple Tricks And Nonsense"),
]


DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses", True),
    n("Gift Of The Master"),
    n("Endor Shield", True),
    n("Ni Chuba Na?", True),
    n("Protocol Failure"),
    n("Cold Feet", True),
    n("We Must Accelerate Our Plans", qty=3),
    n("Emperor Palpatine", qty=2),
    n("Control & Set For Stun"),
    n("Emperor's Power", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Imperial Reinforcements", True),
    n("Victory"),
    n("Vengeance Of The Sith"),
    n("Boba Fett, Bounty Hunter", qty=2),
    n("Weapon Levitation & The Empire's Back"),
    n("Galen Marek, Starkiller", qty=3),
    n("Alter"),
    n("Blizzard 4", qty=2),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Sniper & Dark Strike"),
    n("Ghhhk"),
    n("Blaster Rack", True),
    n("Darth Vader, Betrayer Of The Jedi"),
    n("Dengar With Blaster Carbine", True),
    n("Masterful Move & Endor Occupation"),
    n("Vader's Lightsaber"),
    n("Hoth: Defensive Perimeter (3rd Marker)"),
    n("Presence Of The Force"),
    n("One Beautiful Thing"),
    n("Lightsaber Deficiency", True),
    n("Darth Vader, Dark Lord Of The Sith", qty=2),
    n("Force Lightning"),
    n("Force Field", True),
    n("Force Push", True),
    n("A Sith's Weapon"),
    n("Grand Moff Tarkin", True),
    n("P-59"),
    n("Commander", True),
    n("Rogue Shadow"),
    n("Blockade Flagship: Bridge"),
    n("Juno Eclipse, Black Leader"),
    n("Grand Admiral Thrawn"),
    n("General Nevar", True),
    n("Ghhhk"),
    n("Imperial Justice", True),
    n("No Escape"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("Abyss", True),
    n("Come Here You Big Coward"),
    n("There Is No Try", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("You Cannot Hide Forever"),
    n("Fanfare", True),
    n("Death Star Sentry", True),
    n("Alter", True),
]
DS_ADD = [
    n("A Useless Gesture", True),
    n("Battle Order", True),
    n("Imperial Detention"),
]
