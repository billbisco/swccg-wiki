#!/usr/bin/env python3
"""Day 2 Xerox transcription: Pierre Dubreuil (BRINGHIMB4ME).

Source scans: extract/day2/d2p2_p11.png (Dark, Spice a la Reid Smith) and
extract/day2/d2p2_p12.png (Light, SCOUNDRELS). 2010 form, WORLDS 2014 TO.
Kessel spice mines and Infiltration / Nar Shaddaa. (V) follows the sheet
checkbox. Dittos expanded. Cross-outs keep the remaining title.
"""
from __future__ import annotations


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


PLAYER = "Pierre Dubreuil"
USERNAME = "BRINGHIMB4ME"
PDF = "2014 Worlds Day 2 Part 2.pdf"


# --- Dark: d2p2_p11.png, 2010 form. DARK checked. ---

DS_DECK_NAME = "Spice a la Reid Smith"
DS_SIDE = "Dark"
DS_FORM = "xerox_2010"
DS_SCAN = "extract/day2/d2p2_p11.png"
DS_PDF_PAGE = 11
DS_STARTING = ("Kessel", False)

DS_RESERVE = [
    n("Kessel"),  # 1
    n("Combat Readiness", True),  # 2
    n("Kessel: Spice Mines - Prison", True),  # 3  Kessel Spice Mine Prison
    n("Ni Chuba Na??", True),  # 4  Nichu Bana
    n("I'll Take Them Myself", True),  # 5
    n("Gift Of The Master", True),  # 6
    n("Something Special Planned For Them", True),  # 7  Something Special P.F.T.
    n("Surprise"),  # 8
    n("Spice Mine Operations", True),  # 9  Spice Mine OPPS
    n("Cloud City: Security Tower", True),  # 10
    n("Darth Maul With Lightsaber"),  # 11  Dark Maul with saber
    n("Darth Maul With Lightsaber"),  # 12  ditto
    n("Sniper & Dark Strike"),  # 13  Sniper Dark Strike
    n("Short Range Fighters & Watch Your Back!"),  # 14  Short Range Fighters w/ B
    n("Force Push", True),  # 15
    n("Force Lightning"),  # 16
    n("Lightsaber Deflection", True),  # 17  Lightsaber Def (V); Light title
    n("Dooku's Lightsaber", True),  # 18
    n("Sonic Bombardment", True),  # 19
    n("Sonic Bombardment", True),  # 20  ditto (V)
    n("Sonic Bombardment", True),  # 21  ditto (V)
    n("Count Dooku", True),  # 22
    n("Count Dooku", True),  # 23  ditto (V)
    n("P-59"),  # 24
    n("Dark Maneuvers"),  # 25
    n("Dark Maneuvers"),  # 26  ditto
    n("Limited Resources"),  # 27
    n("Stop Motion", True),  # 28
    n("Maul's Sith Infiltrator"),  # 29
    n("The Phantom Menace"),  # 30
    n("Galen's Lightsaber, Vader's Gift", True),  # 31  Calen's Saber / Vader's Gift
    n("Arica"),  # 32
    n("Galen Marek, Starkiller", True),  # 33  Galen Marek Star
    n("Galen Marek, Starkiller", True),  # 34  ditto (V)
    n("Slave I, Symbol Of Fear", True),  # 35
    n("Boba Fett, Prepared Hunter", True),  # 36  Boba Fett, PREP; Assassin crossed
    n("Jango Fett, The Assassin", True),  # 37
    n("Blizzard 4", True),  # 38  Blizzard 4 now (V) handwritten
    n("I Have You Now"),  # 39
    n("Moruth Doole, Kessel Administrator", True),  # 40  Haruth Doole VA
    n("Blaster Rack", True),  # 41
    n("Kessel Surveillance System", True),  # 42  Kessel Surveillance Sys
    n("Kessel: Spice Mines - Extraction Facility", True),  # 43
    n("Kessel: Spice Mines - Administrator's Office", True),  # 44  Admin.
    n("Cold Feet", True),  # 45
    n("Force Field", True),  # 46  prior title crossed
    n("Short Range Fighters & Watch Your Back!"),  # 47  SR FWYB
    n("Evader & Monnok"),  # 48
    n("Purge", True),  # 49  OURGE
    n("Alter", True),  # 50
    n("Crush The Rebellion"),  # 51
    n("Vader's Lightsaber"),  # 52
    n("Garindan", True),  # 53
    n("Protocol Failure", True),  # 54
    n("Darth Vader, Dark Lord Of The Sith", True),  # 55  DVBOTS
    n("Force Lightning"),  # 56
    n("Ghhhk & Those Rebels Won't Escape Us"),  # 57
    n("Dr. Evazan & Ponda Baba", True),  # 58
    n("Imperial Propaganda", True),  # 59
    n("Knowledge And Defense", True),  # 60  Knowledge & Defence
]

DS_SHIELDS = [
    n("Firepower", True),  # 1  Fire Power
    n("Imperial Detention"),  # 2
    n("There Is No Try"),  # 3
    n("I Find Your Lack Of Faith Disturbing", True),  # 4
    n("Allegations Of Corruption"),  # 5
    n("Battle Order"),  # 6
    n("Do They Have A Code Clearance?"),  # 7  Do they have a code cl
    n("Come Here You Big Coward"),  # 8  Coward
    n("You Cannot Hide Forever", True),  # 9
    n("Abyss", True),  # 10
    n("Fanfare", True),  # 11
    n("Death Star Sentry", True),  # 12  A Useless Gesture crossed
]

DS_ADD = [
    n("Oppressive Enforcement"),  # 1
    n("Resistance"),  # 2
    n("Secret Plans"),  # 3
    n("Death Star Sentry", True),  # 4  Death Star ...
]

DS_UNREAD: list[int] = []
DS_NO_DEST: list[str] = []


# --- Light: d2p2_p12.png, 2010 form. LIGHT checked. ---

LS_DECK_NAME = "SCOUNDRELS"
LS_SIDE = "Light"
LS_FORM = "xerox_2010"
LS_SCAN = "extract/day2/d2p2_p12.png"
LS_PDF_PAGE = 12
LS_STARTING = ("Infiltration / Unlikely Allies", False)

LS_RESERVE = [
    n("Infiltration / Unlikely Allies"),  # 1  INFILTRATION
    n("Scoundrel's Ingenuity", True),  # 2  Surgemacity / Ingenuity
    n("Scoundrel's Charm", True),  # 3  SC CHARM
    n("Scoundrel's Luck", True),  # 4  SC LUCK
    n("Scoundrel's Bravado", True),  # 5  BRAVADO
    n("Nar Shaddaa: Undercity", True),  # 6  Nar Shaddaa Under City
    n("Nar Shaddaa", True),  # 7
    n("Wokling", True),  # 8
    n("Kal'Falnl C'ndros", True),  # 9  See Tor Kal Fas
    n("Imperial Atrocity", True),  # 10
    n("A Good Blaster At Your Side", True),  # 11  A Good Blaster BYS
    n("Lady Luck", True),  # 12
    n("Let The Wookiee Win", True),  # 13
    n("Houjix"),  # 14
    n("Out Of Commission"),  # 15
    n("Imperial Navy Chart", True),  # 16  Imperial Nau Chart; see NOTES
    n("Errant Venture", True),  # 17
    n("Tanus Spijek", True),  # 18
    n("Corran Horn"),  # 19
    n("Out Of Commission & Transmission Terminated"),  # 20  Out of Com / TT
    n("Escape Pod", True),  # 21
    n("Too Close For Comfort"),  # 22
    n("Starship Levitation", True),  # 23  Starship Lef
    n("Lando Calrissian, Unlikely Hero", True),  # 24  Lando Calrissian U.H.
    n("Too Close For Comfort"),  # 25  Too Close For C
    n("Flash Of Insight", True),  # 26
    n("Han Solo, Innocent Scoundrel", True),  # 27
    n("Booster In Pulsar Skate", True),  # 28
    n("Artoo, Brave Little Droid"),  # 29
    n("Blast The Door, Kid!"),  # 30  Blast The Door Kid
    n("Boushh"),  # 31
    n("Leia's Blaster Rifle"),  # 32
    n("Sorry About The Mess & Blaster Proficiency"),  # 33  Sorry About TM / B Prof
    n("Double Agent"),  # 34
    n("Han Solo, Innocent Scoundrel", True),  # 35  H.S. Inn Scoundrel
    n("Boushh"),  # 36
    n("Antilles Maneuver & Rebel Reinforcements", True),  # 37  Antilles Man - Reb Rein
    n("Landing Claw"),  # 38
    n("Han's Blaster, So Uncivilized", True),  # 39  Han's Blaster So Uncivilized
    n("Kyle Katarn's Blaster Rifle", True),  # 40  Kyle Katarn's B.R
    n("Kyle Katarn", True),  # 41
    n("Dodge"),  # 42
    n("Jedi Levitation", True),  # 43  Jedi Lev
    n("Corellian Retort", True),  # 44  Cor. Retort
    n("Lando Calrissian, Unlikely Hero", True),  # 45
    n("Chewbacca, Protector", True),  # 46  Chewbacca Corret
    n("Kyle Katarn", True),  # 47
    n("Corran Horn"),  # 48
    n("Imperial Atrocity", True),  # 49  Atrocity
    n("Dark Approach", True),  # 50
    n("Double Agent", True),  # 51
    n("Lucky Shot", True),  # 52
    n("Heading For The Medical Frigate"),  # 53  Heading for Med Fr
    n("Nar Shaddaa: Undercity Street", True),  # 54  Nar Shaddaa Under Street
    n("Nar Shaddaa: Scoundrel's Rest", True),  # 55  Nar Shaddaa Sc. Rest
    n("Spaceport Scoundrels Guild", True),  # 56  Spaceport Sc. Guild
    n("Mirax Terrik"),  # 57
    n("Errant Venture", True),  # 58
    n("Menace Fades"),  # 59
    n("Anger, Fear, Aggression", True),  # 60  AFA; KAD crossed
]

LS_SHIELDS = [
    n("Jabba's Prize", True),  # 1  Jabba's Prize
    n("Your Insight Serves You Well", True),  # 2
    n("Wise Advice"),  # 3
    n("Weapons Display", True),  # 4
    n("Ultimatum"),  # 5
    n("The Professor", True),  # 6  The Prof V handwritten
    n("Simple Tricks And Nonsense", True),  # 7  Simple Trick
    n("Don't Do That Again", True),  # 8
    n("Chasm", True),  # 9
    n("Battle Plan"),  # 10
    n("Affect Mind", True),  # 11
    n("Aim High"),  # 12
]

LS_ADD = [
    n("A Tragedy Has Occurred"),  # 1  A Tragedy
    n("Yavin Sentry", True),  # 2  Y4. Sentry
]

LS_UNREAD: list[int] = []
LS_NO_DEST: list[str] = []


NOTES = """
Pierre Dubreuil / BRINGHIMB4ME, WORLDS 2014 TO, 2010 form.
Dark d2p2_p11.png Spice a la Reid Smith (DARK checked). Kessel spice.
Light d2p2_p12.png SCOUNDRELS (LIGHT checked). Infiltration / Nar Shaddaa.
Email [redacted].com truncated on the Dark sheet.

DS uncertain:
- No objective title in the 60; line 1 is Kessel. STARTING is the system.
- 3/43/44 Kessel spice sites expanded to vb4/vb7 titles.
- 14 and 47 both Short Range Fighters & Watch Your Back! (unique combo
  listed twice as written).
- 17 Lightsaber Def (V) kept as Lightsaber Deflection (Light title on DS).
- 31 Calen's Saber / Vader's Gift -> Galen's Lightsaber, Vader's Gift (vb6).
- 33-34 Galen Marek Star (V) -> Galen Marek, Starkiller (vb4); unique x2.
- 36 Boba Fett Assassin crossed, PREP remains -> Boba Fett, Prepared Hunter.
- 38 Blizzard 4 now (V) handwritten; is_v True.
- 40 Haruth Doole VA -> Moruth Doole, Kessel Administrator (vb7).
- 46 prior title crossed, Force Field remains.
- 49 OURGE (V) -> Purge as written.
- Shield 12 A Useless Gesture crossed, Death Star Sentry remains.

LS uncertain:
- 2 Scoundrel's Ingenuity (vb8); 3 Charm; 4 Luck; 5 Bravado.
- 9 See Tor Kal Fas -> Kal'Falnl C'ndros.
- 16 Imperial Nau Chart (V) as Imperial Navy Chart (no pre-check title).
- 39 Han's Blaster So Uncivilized -> Han's Blaster, So Uncivilized (vb8).
- 44 Cor. Retort (V) -> Corellian Retort.
- 54-56 Nar Shaddaa: Undercity Street, Scoundrel's Rest, Spaceport
  Scoundrels Guild (vb6/vb8).
- 60 KAD crossed, AFA remains.
- Shield 6 The Prof V -> The Professor with handwritten V (box empty).
""".strip()


if __name__ == "__main__":
    assert len(DS_RESERVE) == 60, len(DS_RESERVE)
    assert len(DS_SHIELDS) == 12, len(DS_SHIELDS)
    assert len(LS_RESERVE) == 60, len(LS_RESERVE)
    assert len(LS_SHIELDS) == 12, len(LS_SHIELDS)
    print("file", __file__)
    print("player", PLAYER, "username", USERNAME)
    print("DS", DS_DECK_NAME, DS_SIDE, "reserve", len(DS_RESERVE), "shields", len(DS_SHIELDS), "add", len(DS_ADD), "unread", DS_UNREAD, "no_dest", DS_NO_DEST)
    print("LS", LS_DECK_NAME, LS_SIDE, "reserve", len(LS_RESERVE), "shields", len(LS_SHIELDS), "add", len(LS_ADD), "unread", LS_UNREAD, "no_dest", LS_NO_DEST)
