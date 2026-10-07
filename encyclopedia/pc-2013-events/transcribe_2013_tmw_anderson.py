#!/usr/bin/env python3
"""2013 Texas Mini Worlds Day 1: John Anderson Xerox Contract Killers / WYS."""
from __future__ import annotations

PLAYER = "John Anderson"
LS_USERNAME = "puck71"
DS_USERNAME = "Puck71"
STAGE = "Day 1"
PDF = "2013 Texas Mini Worlds Day 1.pdf"
LS_PAGE = 31
DS_PAGE = 30
LS_SCAN = "2013 Texas Mini Worlds Day 1 p31 John Anderson LS.png"
DS_SCAN = "2013 Texas Mini Worlds Day 1 p30 John Anderson DS.png"
LS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name John Anderson. Username puck71. Deck Name Wha? IDK. "
    "Event Date 4/20/13. Event Name TMW 2013. LIGHT checked. "
    "Do not dest as a new person. Do not rewrite 2013 Worlds Anderson "
    "Infiltration leftover or 2013 MPC Anderson leftover. "
    "Watch Your Step checkbox empty dested Watch Your Step / This Place Can Be A Little Rough. "
    "Tatooine EP1 dested Tatooine. "
    "Booster in Pulsar Skate dested Booster In Pulsar Skate. "
    "Lando's Luxury Yacht dested Lady Luck. "
    "Han's Blaster So Uncivilized dested Han's Blaster, So Uncivilized. "
    "Rebel Agent dested Rebel Agent as written. "
    "Han Solo Innocent Scoundrel dested Han Solo, Innocent Scoundrel. "
    "Chewbacca Walking Carpet dested Chewbacca, Walking Carpet. "
    "Lando Calrissian Unlikely Hero dested Lando Calrissian, Unlikely Hero. "
    "Sgt. Doallyn dested Sergeant Doallyn. "
    "Tala Verde dested Tala Verde as written. "
    "Armed & Dangerous & Krayt Dragon Howl dested Armed And Dangerous & Krayt Dragon Howl. "
    "Sorry About The Mess & Blaster Proficiency dested Sorry About The Mess & Blaster Proficiency. "
    "Can You Growl dested Can You Growl as written. "
    "Houjix & Out of Nowhere dested Houjix & Out Of Nowhere. "
    "Anger Fear Aggression dested Anger, Fear, Aggression. "
    "Let's Keep a Little Optimism dested Let's Keep A Little Optimism Here. "
    "Yavin Sentry dested Yavin Sentry. "
    "Simple Tricks & Nonsense dested Simple Tricks And Nonsense. "
    "Your Insight Serves You Well dested Your Insight Serves You Well. "
    "Jabba's Prize dested Jabba's Prize. "
    "Unique overcounts sheet-accurate: Booster In Pulsar Skate x2, "
    "No Questions Asked x2, Luke Skywalker, Rebel Hero x2, Rebel Agent x2, "
    "Han Solo, Innocent Scoundrel x3, Chewbacca, Walking Carpet x2, "
    "Lando Calrissian, Unlikely Hero x2, Imperial Atrocity x2, "
    "All Wings Report In & Darklighter Spin x2, Control & Tunnel Vision x2. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)
DS_NOTE = (
    "Handwritten 2010 Xerox Print Form (12 shields + Additional Cards). "
    "Name John Anderson. Username Puck71. "
    "Deck Name Please No Blow The Bunker Decks. Please. Seriously. "
    "Event Date 4/20/13. Event Name TMW 2013. DARK checked. "
    "Do not dest as a new person. Do not rewrite 2013 Worlds Anderson "
    "Contract Killers leftover or 2013 MPC Anderson leftover. "
    "Contract Killers dested Contract Killers / Feared Throughout The Galaxy. "
    "Coruscant (SE) dested Coruscant. "
    "Cor: Sub City Lair dested Coruscant: Sub City Lair. "
    "Cloud City Security Tower dested Cloud City: Security Tower. "
    "Slave I Symbol of Fear dested Slave I, Symbol Of Fear. "
    "Ket Maliss Shadow Killer dested Ket Maliss, Shadow Killer. "
    "Weapon Lev & The Empire's Back dested Weapon Levitation & The Empire's Back. "
    "Imp. Propaganda dested Imperial Propaganda. "
    "Mandalorian Father of Fett dested Jango Fett, The Assassin. "
    "Imbalance & Kintan Strider dested Imbalance & Kintan Strider. "
    "Greedo w Blaster Pistol dested Greedo With Blaster Pistol. "
    "Death Mark & Hutt Bounty dested Death Mark & Hutt Bounty. "
    "Galen Secret Apprentice dested Galen, Secret Apprentice as written. "
    "Galen's Saber Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Knowledge & Defense dested Knowledge And Defense. "
    "You Cannot Hide Forever dested You Cannot Hide Forever. "
    "Do They Have a Code Clearance dested Do They Have A Code Clearance?. "
    "Come Here You Big Coward dested Come Here You Big Coward. "
    "Weapon of a Sith dested Weapon Of A Sith. "
    "We'll Let Fate Decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "I Find Your Lack Of Faith Disturbing dested I Find Your Lack Of Faith Disturbing. "
    "There Is No Try on Additional crossed with no replacement, skipped. "
    "Unique overcounts sheet-accurate: Disarmed x2, Arica x3, "
    "Trophy Of A Kill x3, Aurra Sing x2, Sonic Bombardment x3, "
    "Abyssin Ornament x3, Imbalance & Kintan Strider x2, "
    "Galen, Secret Apprentice x3. "
    "(V) from the checkbox; dittos inherit the first named line except where "
    "the ditto line's checkbox differs."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Watch Your Step / This Place Can Be A Little Rough"
LS_CARDS = [
    n("Watch Your Step / This Place Can Be A Little Rough"),
    n("Tatooine"),
    n("Tatooine: Cantina", True),
    n("Tatooine: Docking Bay 94"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("A Good Blaster At Your Side"),
    n("Quick Draw", True),
    n("Booster In Pulsar Skate", qty=2),
    n("Lady Luck"),
    n("No Questions Asked", qty=2),
    n("Tatooine: Mos Eisley"),
    n("Black Market Blaster"),
    n("Chewbacca's Bowcaster"),
    n("Luke's Blaster Pistol", True),
    n("Han's Blaster, So Uncivilized"),
    n("Wedge Antilles", True),
    n("Luke Skywalker, Rebel Hero", qty=2),
    n("Rebel Agent", qty=2),
    n("Han Solo, Innocent Scoundrel", qty=3),
    n("Chewbacca, Walking Carpet", qty=2),
    n("Lando Calrissian, Unlikely Hero", qty=2),
    n("Melas", True),
    n("Sergeant Doallyn", True),
    n("Dash Rendar", True),
    n("Tala Verde"),
    n("Mirax Terrik"),
    n("Redeemed Apprentice"),
    n("Disarmed"),
    n("Scrambled Transmission", True),
    n("Tatooine Celebration"),
    n("Seeking An Audience", True),
    n("Imperial Atrocity", True, qty=2),
    n("Sai'torr Kal Fas", True),
    n("Old Ben"),
    n("All Wings Report In & Darklighter Spin", qty=2),
    n("Rebel Barrier"),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("It's A Hit!"),
    n("Can You Growl"),
    n("It Could Be Worse"),
    n("Corellian Slip", True),
    n("A Few Maneuvers"),
    n("Alternatives To Fighting"),
    n("Control & Tunnel Vision", qty=2),
    n("Houjix & Out Of Nowhere"),
    n("YT-1300 Transport", True),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Let's Keep A Little Optimism Here", True),
    n("Affect Mind", True),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Planetary Defenses", True),
    n("Ultimatum"),
    n("Don't Do That Again", True),
    n("Aim High"),
    n("Battle Plan"),
    n("Weapons Display", True),
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
]
LS_ADD = [
    n("Simple Tricks And Nonsense"),
    n("Your Insight Serves You Well", True),
    n("Jabba's Prize", True),
]


DS_START = "Contract Killers / Feared Throughout The Galaxy"
DS_CARDS = [
    n("Contract Killers / Feared Throughout The Galaxy"),
    n("Coruscant"),
    n("Coruscant: Sub City Lair"),
    n("Prepared Defenses", True),
    n("On The Hunt"),
    n("Gift Of The Master"),
    n("Guild Of Assassins"),
    n("Jabba's Haven"),
    n("Cloud City: Security Tower", True),
    n("We Must Accelerate Our Plans"),
    n("Disarmed", qty=2),
    n("Keder The Black"),
    n("Arica", True, qty=3),
    n("Slave I, Symbol Of Fear"),
    n("Ket Maliss, Shadow Killer"),
    n("Trophy Of A Kill", qty=3),
    n("Aurra Sing", True, qty=2),
    n("Dark Jedi Lightsaber", True),
    n("Weapon Levitation & The Empire's Back"),
    n("Coruscant: Casino"),
    n("Nevar Yalnal"),
    n("Blaster Rack", True),
    n("Mara Jade's Lightsaber", True),
    n("Imperial Propaganda", True),
    n("Nal Hutta"),
    n("Guri"),
    n("Cold Feet", True),
    n("Sonic Bombardment", True, qty=3),
    n("Boba Fett, Prepared Hunter"),
    n("Abyssin Ornament", True, qty=3),
    n("J'Quille", True),
    n("Jango Fett, The Assassin"),
    n("Force Field", True),
    n("Imbalance & Kintan Strider", qty=2),
    n("Coruscant: Palpatine's Quarters"),
    n("Greedo With Blaster Pistol"),
    n("Bane Malar", True),
    n("Levitation Attack", True),
    n("Stop Motion", True),
    n("Masterful Move"),
    n("Death Mark & Hutt Bounty"),
    n("A Sith's Weapon"),
    n("Galen, Secret Apprentice", qty=3),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Ghhhk"),
    n("Force Push", True),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever"),
    n("Fanfare", True),
    n("Resistance"),
    n("Battle Order"),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Do They Have A Code Clearance?", True),
    n("Oppressive Enforcement"),
    n("Come Here You Big Coward"),
    n("Weapon Of A Sith"),
    n("Abyss", True),
    n("Secret Plans"),
]
DS_ADD = [
    n("Allegations Of Corruption"),
    n("We'll Let Fate-a Decide, Huh?", True),
    n("I Find Your Lack Of Faith Disturbing", True),
]
