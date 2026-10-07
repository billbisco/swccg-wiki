#!/usr/bin/env python3
"""2013 SoCal Grand Prix Day 1: Jan Westergard Print Form LS+DS.

Name field JAN / Jan. Username Ghosttrain. Dest Jan Westergard
(2014 Philadelphia Ghosttrain analog). Do not dest as a new person.
"""
from __future__ import annotations

PLAYER = "Jan Westergard"
USERNAME = "Ghosttrain"
STAGE = "Day 1"
PDF = "2013 SoCal Grand Prix Day 1.pdf"
LS_PAGE = 43
DS_PAGE = 44
LS_SCAN = "2013 SoCal Grand Prix Day 1 p43 Jan Westergard LS.png"
DS_SCAN = "2013 SoCal Grand Prix Day 1 p44 Jan Westergard DS.png"
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, "
    "Jedi Tests 2 and 5 checked). Name JAN dested Jan Westergard. "
    "Username Ghosttrain. Deck Name Lama Glama. Event SCGP. LIGHT checked. "
    "WATCH YOUR STEP BITCH! empty dested Watch Your Step / This Place Can Be A Little Rough. "
    "CANTINA a.k.a. DANGER ZONE dested Tatooine: Cantina. "
    "DB 94 dested Tatooine: Docking Bay 94. "
    "Squassin dested Squadron Assignments. "
    "QD dested Quick Draw. "
    "HFTMF dested Heading For The Medical Frigate. "
    "Saitor dested Sai'torr Kal Fas. "
    "Alternatives To Fighting crossed, It's A Hit dested It's A Hit. "
    "ICBW dested It Could Be Worse. "
    "Han Solo, IS dested Han Solo, Innocent Scoundrel. "
    "BoShek Brash Smuggler dested BoShek, Brash Smuggler. "
    "NQA dested No Questions Asked. "
    "AiR5 dested Artoo-Detoo In Red 5. "
    "Chewbacca, Carpet dested Chewbacca, Walking Carpet. "
    "Control & TV dested Control & Tunnel Vision. "
    "Pulsar Skate dested Booster In Pulsar Skate. "
    "Sgt Doallyn dested Sergeant Doallyn. "
    "Lando, Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "MIRAX dested Mirax Terrik. "
    "SATM & BP dested Sorry About The Mess & Blaster Proficiency. "
    "Han's Heavy Blaster Pistol dested Han With Heavy Blaster Pistol. "
    "Bounty crossed, Moving to Attack Position dested Moving To Attack Position. "
    "We DGOOOOOMED dested We're Doomed. "
    "Houjix & OON dested Houjix & Out Of Nowhere. "
    "AWRI & DS dested All Wings Report In & Darklighter Spin. "
    "Not My Fault crossed, Melas dested Melas. "
    "Infinity dested as written. "
    "Barrier dested Rebel Barrier. "
    "STAN dested Simple Tricks And Nonsense. "
    "Your Ship dested Your Ship?. "
    "Planetary Def dested Planetary Defenses. "
    "AFA dested Anger, Fear, Aggression. "
    "Jedi Tests 2 and 5 dested A Jedi's Strength and A Jedi's Focus. "
    "Unique overcounts sheet-accurate. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Typed 2013 Print Form green (15 shields, Jedi Tests empty, "
    "Hidden Fortress empty). Name Jan dested Jan Westergard. Username Ghosttrain. "
    "Deck Name Pizza To Go. Event SoCal GP. DARK checked. "
    "Invasion empty dested Invasion / In Complete Control. "
    "Naboo: Throne Room dested Naboo: Theed Palace Throne Room. "
    "Oh Switch Off dested Oh, Switch Off. "
    "He is Not Ready dested He Is Not Ready. "
    "A Useless Guesure dested A Useless Gesture. "
    "Do They Have A Code Clearance dested Do They Have A Code Clearance?. "
    "Unique overcounts sheet-accurate. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Docking Bay 94"),
    n("Squadron Assignments"),
    n("Quick Draw", True),
    n("Wokling", True),
    n("Heading For The Medical Frigate"),
    n("Melas", True),
    n("It's A Hit"),
    n("Disarmed"),
    n("Sai'torr Kal Fas", True),
    n("Kyle Katarn"),
    n("It Could Be Worse"),
    n("Corellia", True),
    n("Han Solo, Innocent Scoundrel", qty=2),
    n("BoShek, Brash Smuggler"),
    n("Black Market Dealer"),
    n("Outrider"),
    n("No Questions Asked", qty=2),
    n("A Good Blaster At Your Side"),
    n("Rebel Barrier"),
    n("Artoo-Detoo In Red 5", qty=2),
    n("Luke Skywalker", True, qty=2),
    n("Chewbacca, Walking Carpet"),
    n("Control & Tunnel Vision", qty=2),
    n("Lady Luck"),
    n("Tatooine Celebration", qty=2),
    n("Booster In Pulsar Skate"),
    n("Ison Corridor"),
    n("Sergeant Doallyn", True),
    n("Dash Rendar"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Mirax Terrik"),
    n("Imperial Atrocity", True),
    n("Wedge Antilles", True),
    n("Sorry About The Mess & Blaster Proficiency", qty=2),
    n("Menace Fades"),
    n("Han With Heavy Blaster Pistol", True),
    n("We'll Find Han", True),
    n("Moving To Attack Position"),
    n("We're Doomed", True),
    n("Houjix & Out Of Nowhere"),
    n("All Wings Report In & Darklighter Spin"),
    n("Desperate Reach", True),
    n("A Few Maneuvers", qty=2),
    n("Melas", True),
    n("Infinity"),
    n("Rebel Barrier"),
    n("Kyle Katarn"),
    n("Tatooine: Mos Eisley"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Aim High"),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Battle Plan"),
    n("Ultimatum"),
    n("Don't Do That Again"),
    n("Weapons Display", True),
    n("Your Insight Serves You Well", True),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Jabba's Prize", True),
    n("Simple Tricks And Nonsense"),
    n("Your Ship?"),
    n("Planetary Defenses"),
    n("Affect Mind", True),
]
LS_ADD = [
    n("A Jedi's Strength"),
    n("A Jedi's Focus"),
]


DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Naboo"),
    n("Naboo: Swamp"),
    n("Droid Racks", True),
    n("Prepared Defenses"),
    n("Crossfire"),
    n("At Last We Are Getting Results", True),
    n("Imperial Justice", True),
    n("Where Are Those Droidekas?", True),
    n("Oh, Switch Off", qty=2),
    n("You Cannot Hide Forever"),
    n("Maul's Sith Infiltrator"),
    n("He Is Not Ready", True),
    n("Naboo: Theed Palace Throne Room"),
    n("Naboo: Theed Palace Generator"),
    n("Naboo: Theed Palace Courtyard"),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("Darth Maul"),
    n("Daultay Dofine", True),
    n("Guri", qty=2),
    n("Jango Fett, The Assassin"),
    n("Blockade Flagship"),
    n("Blockade Support Ship", qty=2),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Search And Destroy"),
    n("3,720 To 1", True),
    n("Destroyer Droid", qty=9),
    n("Master, Destroyers!", qty=3),
    n("Sonic Bombardment", True),
    n("Rolling, Rolling, Rolling", qty=2),
    n("Wounded Warrior", qty=2),
    n("Self-Destruct Mechanism"),
    n("P-59", qty=2),
    n("P-60", qty=2),
    n("Cloud City: Security Tower", True),
    n("Sniper & Dark Strike"),
    n("Abyssin Ornament"),
    n("Elis Helrot"),
    n("We Must Accelerate Our Plans", qty=2),
    n("P-13 & P-14"),
    n("Forced Servitude", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("Secret Plans"),
    n("Abyss", True),
    n("Fanfare", True),
    n("A Useless Gesture", True),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Resistance"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Allegations Of Corruption"),
    n("Do They Have A Code Clearance?", True),
    n("You Cannot Hide Forever", True),
    n("There Is No Try"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Oppressive Enforcement"),
    n("Leave Them To Me", True),
]
DS_ADD = []
