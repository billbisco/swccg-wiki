#!/usr/bin/env python3
"""2013 World Championship Day 2: Brian Herold Xerox Infiltration + Hunt Down."""
from __future__ import annotations

PLAYER = "Brian Herold"
LS_USERNAME = "Zero Cool"
DS_USERNAME = "Crash Override"
STAGE = "Day 2"
PDF = "2013 Worlds Day 2.pdf"
LS_PAGE = 44
DS_PAGE = 45
LS_SCAN = "2013 Worlds Day 2 p44 Brian Herold LS.png"
DS_SCAN = "2013 Worlds Day 2 p45 Brian Herold DS.png"
LS_NOTE = (
    "Handwritten 2009 Xerox Print Form (uniqueness dots). "
    "Name Brian Herold. Username Zero Cool. LIGHT. Worlds, dated 8/10/13. "
    "Deck title a YouTube URL. "
    "Infiltration / Unlikely Allies dested Infiltration / Unlikely Allies. "
    "Nar Shaddaa: Undercity dested Nar Shaddaa: Undercity. "
    "I Can't Believe That He's Gone dested I Can't Believe He's Gone. "
    "Armed & Dangerous & Krayt Dragon Howl dested Armed And Dangerous & Krayt Dragon Howl. "
    "We Wish A Board At Once dested We Wish To Board At Once. "
    "R2-D2 [Artoo-Detoo] dested R2-D2 (Artoo-Detoo). "
    "Obi-Wan In Red 7 dested Obi-Wan In Radiant VII. "
    "LE-BO2D9 (Leebo) dested LE-BO2D9 (Leebo). "
    "Rebel Agent dested Kyle Katarn. "
    "Rebel Agent's Blaster Rifle dested Kyle Katarn's Blaster Rifle. "
    "Lando's Luxury Yacht dested Lando's Luxury Yacht. "
    "Red Squadron 7 dested Red Squadron 7. "
    "Spaceport Scoundrel's Guild dested Spaceport Scoundrels Guild. "
    "Nar Shaddaa: Scoundrel's Rest dested Nar Shaddaa: Scoundrel's Rest. "
    "Form left column reprints 37-38 on lines 39-40 are Kyle Katarn. "
    "Additional Battle Plan / Aim High / YISYW moved to Light shields. "
    "(V) from the checkbox."
)
DS_NOTE = (
    "Handwritten 2009 Xerox Print Form (uniqueness dots). "
    "Name Brian Herold. Username Crash Override. DARK. Worlds, dated 8/10/13. "
    "Deck title a YouTube URL. "
    "Hunt Down & Destroy The Jedi dested Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe. "
    "Coruscant (Special Ed) dested Coruscant. "
    "A Sith's Plan dested A Sith's Plans. "
    "Ni Chuba Na?? dested Ni Chuba Na??. "
    "Ice-Heart dested Ysanne Isard. "
    "Trophy Of Akil dested Trophy Of A Kill. "
    "Weapon Lev & The Empire's Back dested Weapon Levitation & The Empire's Back. "
    "Naboo: Theed Palace Generator Core dested Naboo: Theed Palace Generator Core. "
    "Dr. E & Ponda Baba dested Dr. Evazan & Ponda Baba. "
    "Black Leader dested Juno Eclipse, Black Leader. "
    "Galen, Secret Apprentice dested Galen, Secret Apprentice. "
    "Darth Vader, Dark Lord OTS dested Darth Vader, Dark Lord Of The Sith. "
    "Mandalorian, Father Of Fett dested Jango Fett, The Assassin. "
    "Galen's Fighter dested Galen's Fighter. "
    "Retraining Bolt dested as written. "
    "Galen's Saber, Vader's Gift dested Galen's Lightsaber, Vader's Gift. "
    "Ability Ability Ability dested Ability, Ability, Ability. "
    "Weapon Lev & TEB dested Weapon Levitation & The Empire's Back. "
    "Control & SFS dested Control & Set For Stun. "
    "WMAOP dested We Must Accelerate Our Plans. "
    "We'll Let Fate-a Decide, Huh? dested We'll Let Fate-a Decide, Huh?. "
    "I Find Your Lack dested I Find Your Lack Of Faith Disturbing. "
    "Form left column reprints 37-38 on lines 39-40 are Aurra Sing's Blaster Rifle. "
    "Additional Oppressive Enforcement / There Is No Try / Battle Order moved to Dark shields. "
    "(V) from the checkbox."
)


def n(name: str, v: bool = False, qty: int = 1) -> tuple[int, str, bool]:
    return (qty, name, v)


LS_START = "Infiltration / Unlikely Allies"
LS_CARDS = [
    n("Infiltration / Unlikely Allies"),
    n("Nar Shaddaa"),
    n("Nar Shaddaa: Undercity"),
    n("Scoundrel's Luck"),
    n("Scoundrel's Bravado"),
    n("Scoundrel's Charm"),
    n("Scoundrel's Ingenuity"),
    n("Heading For The Medical Frigate"),
    n("Wokling", True),
    n("Luke, Trust Me"),
    n("Squadron Assignments"),
    n("Houjix"),
    n("I Can't Believe He's Gone", True),
    n("Armed And Dangerous & Krayt Dragon Howl"),
    n("Menace Fades"),
    n("All Wings Report In & Darklighter Spin"),
    n("Escape Pod", True),
    n("Captain Han Solo"),
    n("Imperial Navigation Charts"),
    n("Moving To Attack Position"),
    n("Scrambled Transmission", True),
    n("Rebel Barrier"),
    n("Kessel"),
    n("Redeemed Apprentice"),
    n("Imperial Atrocity", True),
    n("Kyle Katarn"),
    n("Pulsar Skate"),
    n("Flash Of Insight", True),
    n("We Wish To Board At Once"),
    n("Han's Toolkit"),
    n("Dash Rendar"),
    n("Corran Horn"),
    n("All Wings Report In & Darklighter Spin"),
    n("R2-D2 (Artoo-Detoo)", True),
    n("Hear Me Baby, Hold Together", True),
    n("Rebel Artillery"),
    n("Kessel Run", True),
    n("We Wish To Board At Once"),
    n("Kyle Katarn", qty=2),
    n("Projection Of A Skywalker"),
    n("Chewbacca, Walking Carpet"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Outrider"),
    n("Landing Claw"),
    n("Obi-Wan In Radiant VII"),
    n("Escape Pod", True),
    n("Nar Shaddaa: Scoundrel's Rest"),
    n("LE-BO2D9 (Leebo)", True),
    n("Kyle Katarn's Blaster Rifle"),
    n("Kyle Katarn"),
    n("Millennium Falcon"),
    n("Lando's Luxury Yacht"),
    n("Boushh"),
    n("Mirax Terrik"),
    n("Corran Horn"),
    n("Spaceport Scoundrels Guild"),
    n("Red Squadron 7", True),
    n("Weapon Levitation"),
    n("Anger, Fear, Aggression", True),
]
LS_SHIELDS = [
    n("Wise Advice"),
    n("Only Jedi Carry That Weapon"),
    n("Chasm", True),
    n("Simple Tricks And Nonsense"),
    n("A Tragedy Has Occurred"),
    n("Do, Or Do Not"),
    n("Don't Do That Again", True),
    n("Weapons Display", True),
    n("The Professor", True),
    n("There Is Another"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Battle Plan", True),
    n("Aim High"),
    n("Your Insight Serves You Well", True),
]
LS_ADD = []

DS_START = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
DS_CARDS = [
    n("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", True),
    n("Coruscant"),
    n("Coruscant: Imperial City"),
    n("A Sith's Plans"),
    n("Prepared Defenses"),
    n("Ni Chuba Na??", True),
    n("Gift Of The Master"),
    n("Drop!", True),
    n("Aurra Sing, Deadly Assassin", qty=2),
    n("Ysanne Isard"),
    n("Trophy Of A Kill", qty=4),
    n("Weapon Levitation & The Empire's Back"),
    n("Sonic Bombardment", True, qty=3),
    n("Cloud City: Security Tower", True),
    n("Naboo: Theed Palace Generator Core"),
    n("Blockade Flagship: Bridge"),
    n("Grand Moff Tarkin", True),
    n("Arica", True),
    n("Dr. Evazan & Ponda Baba"),
    n("Juno Eclipse, Black Leader"),
    n("Galen, Secret Apprentice", qty=3),
    n("Darth Vader, Dark Lord Of The Sith", qty=3),
    n("Jango Fett, The Assassin"),
    n("Boba Fett, Prepared Hunter"),
    n("Slave I, Symbol Of Fear"),
    n("Galen's Fighter"),
    n("Retraining Bolt", qty=2),
    n("Aurra Sing's Blaster Rifle", qty=2),
    n("Vader's Lightsaber"),
    n("Galen's Lightsaber, Vader's Gift"),
    n("Ability, Ability, Ability", True),
    n("Blaster Rack", True),
    n("Weapon Levitation & The Empire's Back", qty=2),
    n("One Beautiful Thing"),
    n("A Dark Time For The Rebellion", True),
    n("Control & Set For Stun"),
    n("Alter", True),
    n("Levitation Attack", qty=3),
    n("Force Field", True, qty=2),
    n("We Must Accelerate Our Plans", qty=3),
    n("One Beautiful Thing"),
    n("Knowledge And Defense", True),
]
DS_SHIELDS = [
    n("You Cannot Hide Forever", True),
    n("Do They Have A Code Clearance?", True),
    n("Firepower", True),
    n("A Useless Gesture", True),
    n("Weapon Of A Sith"),
    n("Abyss", True),
    n("Resistance"),
    n("We'll Let Fate-a Decide, Huh?"),
    n("Come Here You Big Coward"),
    n("Secret Plans"),
    n("I Find Your Lack Of Faith Disturbing", True),
    n("Allegations Of Corruption"),
    n("Oppressive Enforcement"),
    n("There Is No Try"),
    n("Battle Order"),
]
DS_ADD = []
