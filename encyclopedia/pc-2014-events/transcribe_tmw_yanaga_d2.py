#!/usr/bin/env python3
"""2014 Texas Mini Worlds Day 2 Xerox: Ganden Yanaga (Cam Solusar).

Source: 2014-TMW-Day-2.pdf pages 7–8 (2013 form).
"""
from __future__ import annotations

PLAYER = "Ganden Yanaga"
USERNAME = "Cam Solusar"
STAGE = "Day 2"
PDF = "2014 Texas Mini Worlds Day 2.pdf"
LS_PAGE = 8
DS_PAGE = 7
LS_SCAN = "2014 Texas Mini Worlds Day 2 p08 Ganden Yanaga LS.png"
DS_SCAN = "2014 Texas Mini Worlds Day 2 p07 Ganden Yanaga DS.png"
NOTE = "Handwritten 2013 Print Form (15 shields)."
LS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Camden Yanaga dested Ganden Yanaga. Username Cam Solusar. LIGHT checked. "
    "Deck Name Cloud Age Symplay The Remix. Event TMW Day 2. "
    "Quiet Mining Colony / IO dested Quiet Mining Colony / Independent Operation. "
    "HFTMF dested Heading For The Medical Frigate. "
    "KTEOF dested as written. "
    "All My Urchins & CC Celebration dested All My Urchins & Cloud City Celebration. "
    "CC: DB dested Cloud City: Downtown Plaza? CC: DB dested Cloud City: Platform? "
    "CC: DB dested Cloud City: Downtown Plaza Docking Bay analog; dest Cloud City: Platform. "
    "Tenas Spejix dested as written. "
    "AWRI & DS dested All Wings Report In & Darklighter Spin. "
    "Han Solo, Scoundrel dested as written. "
    "Foal Madama dested as written. "
    "ICBW dested It Could Be Worse. "
    "Luke w/ Lightsaber dested Luke With Lightsaber. "
    "NO_DEST remaining: KTEOF, Tenas Spejix, Han Solo Scoundrel, Ellor Madak, "
    "Foal Madama, Trooper I'turr M'tec, Tesolomy Taceme, Jar Jar Drinks, Blasted Orchid, "
    "Rolling #3, Hey You, Master Destroyers. "
    "Tesolomy Taceme dested as written. "
    "Jar Jar Drinks dested Jar Jar Drinks. "
    "LTWW dested Let The Wookiee Win. "
    "Houjix & OON dested Houjix & Out Of Nowhere. "
    "POLR dested Path Of Least Resistance. "
    "POLR & Revealed dested Path Of Least Resistance & Revealed. "
    "Harc Seff dested Harc Seff. "
    "I'll Take The Leader dested I'll Take The Leader. "
    "Nien Nunb Sullustan Smuggler dested Nien Nunb. "
    "Tragedy dested A Tragedy Has Occurred. "
    "DDTA dested Don't Do That Again. "
    "YISYW dested Your Insight Serves You Well. "
    "Optimism dested Let's Keep A Little Optimism Here. "
    "DODN dested Do, Or Do Not. "
    "Unique overcounts sheet-accurate (Let The Wookiee Win x2, Rebel Barrier x2, "
    "Houjix & Out Of Nowhere x2, Path Of Least Resistance lines). "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2013 Print Form (15 shields, Hidden Fortress empty, Jedi Tests empty). "
    "Name Camden Yanaga dested Ganden Yanaga. Username Cam Solusar. DARK checked. "
    "Deck Name Pew-Pew. Event TMW Day 2. "
    "Invasion / In Complete Control dested Invasion / In Complete Control. "
    "3-720 to 1 dested 3,720 To 1. "
    "Nute Gunray, NV dested Nute Gunray, Neimoidian Viceroy. "
    "P-60 dested P-60. "
    "Rolling #3 dested Rolling #9 analog; dest Rolling #3 as written. "
    "Master, Destroyers dested Masterful Move? Master, Destroyers dested as written. "
    "Naboo: TP TR dested Naboo: Theed Palace Throne Room. "
    "Ghhhk & Those Rebels dested Ghhhk & Those Rebels Won't Escape Us. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "BF: Bridge dested Blockade Flagship: Bridge. "
    "P-13 & P-14 dested P-13 & P-14. "
    "Oh, Switch Off dested Oh, Switch Off!. "
    "CC: Security Tower dested Cloud City: Security Tower. "
    "Naboo: TP Courtyard dested Naboo: Theed Palace Courtyard. "
    "Line 46 Naboo site crossed, Theed Palace Generator dested Naboo: Theed Palace Generator. "
    "Line 54 crossed, Force Push dested Force Push. "
    "Hey You dested as written. "
    "Jango Fett, Assassin dested Jango Fett, The Assassin. "
    "K&D dested Knowledge And Defense. "
    "CHYBC dested Come Here You Big Coward. "
    "TINT dested There Is No Try. "
    "YCHF dested You Cannot Hide Forever. "
    "We'll Let Fate Decide Huh dested We'll Let Fate-a Decide, Huh?. "
    "Unique overcounts sheet-accurate (Destroyer Droid x9, P-60 x2, Rolling #3 x2, "
    "Master, Destroyers x2, Why Didn't You Tell Me? x2, Wounded Warrior x2, "
    "Outflank x2, We Must Accelerate Our Plans x2, Sonic Bombardment x2, Guri x2, P-59 x2). "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Quiet Mining Colony / Independent Operation"
LS_CARDS = [
    n("Quiet Mining Colony / Independent Operation"),
    n("Bespin"),
    n("Cloud City: Guest Quarters"),
    n("Heading For The Medical Frigate", True),
    n("Beldon's Eye", True),
    n("KTEOF"),
    n("All My Urchins & Cloud City Celebration"),
    n("Cloud City: Downtown Plaza"),
    n("Seeking An Audience", True),
    n("Yoxgit"),
    n("Imperial Atrocity", True),
    n("Tenas Spejix", True),
    n("Rebel Barrier"),
    n("All Wings Report In & Darklighter Spin"),
    n("Melas", True),
    n("Kebyc", True),
    n("Han Solo, Scoundrel"),
    n("Lady Luck"),
    n("Ellor Madak", True),
    n("Foal Madama"),
    n("It's A Trap"),
    n("Trooper I'turr M'tec", True),
    n("Lando Calrissian, Unlikely Hero"),
    n("It Could Be Worse"),
    n("Cloud City: North Corridor"),
    n("Aayla Secura"),
    n("Cloud City: West Gallery"),
    n("Hiding In The Garbage", True),
    n("Dark Approach", True),
    n("Menace Fades"),
    n("Cloud City: Upper Plaza Corridor"),
    n("Kal'Falnl C'ndros"),
    n("Luke With Lightsaber"),
    n("Tesolomy Taceme", True),
    n("Mirax Terrik"),
    n("Booster In Pulsar Skate", True),
    n("Jar Jar Drinks"),
    n("Dash Rendar", True),
    n("Desperate Reach", True),
    n("Let The Wookiee Win", True),
    n("Houjix & Out Of Nowhere"),
    n("Let The Wookiee Win", True),
    n("Sergeant Edian"),
    n("Chewbacca, Walking Carpet"),
    n("Overseer", True),
    n("Path Of Least Resistance"),
    n("Rebel Barrier"),
    n("Blasted Orchid"),
    n("Alter"),
    n("I'll Take The Leader"),
    n("Harc Seff", True),
    n("Outrider"),
    n("Choke"),
    n("Path Of Least Resistance & Revealed"),
    n("Leia, Rebel Princess"),
    n("Houjix & Out Of Nowhere"),
    n("Nien Nunb"),
    n("Alternatives To Fighting"),
    n("Leesub Sirln", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm"),
    n("Battle Plan"),
    n("Don't Do That Again", True),
    n("Ultimatum"),
    n("Aim High"),
    n("Weapons Display", True),
    n("Yavin Sentry"),
    n("Simple Tricks And Nonsense"),
    n("The Professor"),
    n("Your Insight Serves You Well"),
    n("Let's Keep A Little Optimism Here"),
    n("Planetary Defenses"),
    n("Do, Or Do Not"),
    n("Jabba's Prize"),
]
LS_ADD = []


DS_START = "Invasion / In Complete Control"
DS_CARDS = [
    n("Invasion / In Complete Control"),
    n("Droid Racks", True),
    n("Naboo"),
    n("Blockade Flagship"),
    n("Naboo: Swamp"),
    n("Prepared Defenses"),
    n("3,720 To 1", True),
    n("Where Are Those Droidekas?", True),
    n("At Last We Are Getting Results", True),
    n("You Cannot Hide Forever"),
    n("Self-Destruct Mechanism"),
    n("Nute Gunray, Neimoidian Viceroy"),
    n("Destroyer Droid"),
    n("P-60", qty=2),
    n("Rolling #3"),
    n("Master, Destroyers"),
    n("Naboo: Theed Palace Throne Room"),
    n("Stinger", True),
    n("Why Didn't You Tell Me?", True, qty=2),
    n("P-59"),
    n("Ghhhk & Those Rebels Won't Escape Us"),
    n("Rolling #3"),
    n("Wounded Warrior"),
    n("Forced Servitude", True),
    n("Outflank"),
    n("We Must Accelerate Our Plans", qty=2),
    n("Blockade Flagship: Bridge"),
    n("Those Rebels Won't Escape Us", True),
    n("Sonic Bombardment", True),
    n("P-13 & P-14"),
    n("Sonic Bombardment", True),
    n("Oh, Switch Off!"),
    n("Cloud City: Security Tower", True),
    n("Destroyer Droid"),
    n("Sniper & Dark Strike"),
    n("Guri"),
    n("Master, Destroyers"),
    n("Outflank"),
    n("Destroyer Droid"),
    n("Daultay Dofine", True),
    n("Destroyer Droid"),
    n("Blockade Support Ship"),
    n("Naboo: Theed Palace Generator"),
    n("Crossfire"),
    n("Destroyer Droid", qty=2),
    n("Guri"),
    n("Destroyer Droid"),
    n("Naboo: Theed Palace Courtyard"),
    n("Destroyer Droid"),
    n("Force Push", True),
    n("P-59"),
    n("Hey You"),
    n("Destroyer Droid"),
    n("Wounded Warrior"),
    n("Jango Fett, The Assassin"),
    n("Knowledge And Defense"),
]
DS_SHIELDS = [
    n("Allegations Of Corruption"),
    n("Firepower", True),
    n("Oppressive Enforcement"),
    n("Abyss"),
    n("Come Here You Big Coward"),
    n("Battle Order"),
    n("Secret Plans"),
    n("There Is No Try"),
    n("Leave Them To Me"),
    n("You Cannot Hide Forever"),
    n("Death Star Sentry"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("A Useless Gesture"),
    n("Resistance"),
    n("Imperial Detention"),
]
DS_ADD = []
