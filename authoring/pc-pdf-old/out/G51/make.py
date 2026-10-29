#!/usr/bin/env python3
"""G51 deck data -> JSON (2011Reg_GermanNational2011Decklistspost pages 1-20)."""
import json, os, re
OUT = os.path.dirname(os.path.abspath(__file__))
STEM = "2011Reg_GermanNational2011Decklistspost"
EV = ""

def L(text, card=None, v=None, c=1, **kw):
    if v is None:
        v = bool(re.search(r"\((v|V)\)|\s[vV]$", text))
    if card is None:
        card = re.sub(r"\s*\((v|V|AI|x\d+|1 starting)\)", "", text)
        card = re.sub(r"\s+[vV]$", "", card).replace("*", "").replace("<>", "").strip()
    d = {"text": text, "card": card, "v": v}
    if c != 1: d["count"] = c
    d.update(kw)
    return d

FIX = {"Obi-Wan in Radiant VII": "Obi-Wan In Radiant VII", "Blind Jedi": "Rahm Kota, Blind Jedi",
       "Fallen Jedi": "Maris Brood, Fallen Jedi", "Cyborg Commander, Hunter Of Jedi": "Grievous, Hunter Of Jedi",
       "Cyborg Commander, Hunter of Jedi": "Grievous, Hunter Of Jedi", "Are You Braindead?!": "Are You Brain Dead?!",
       "Ice-Heart": "", "Guild of Assassins": "Guild Of Assassins", "Han, Courageous Smuggler": "Han Solo, Courageous Smuggler",
       "Let's Keep A Little Optimism Here (Death Star II)": "Let's Keep A Little Optimism Here", "IG Bodyguard droid": "", "Do, Or Do Not & There Is No Try": ""}

def deck(pages, name, side, start, lines, shields, deck_name="", event=EV, date="", notes=(), username=""):
    for x in lines + shields:
        if x["card"] in FIX: x["card"] = FIX[x["card"]]
    for i, x in enumerate(lines, 1): x["n"] = i
    for i, x in enumerate(shields, 1): x["n"] = i
    d = {"pdf": STEM, "pages": pages, "name_written": name, "username": username, "side": side,
         "deck_name": deck_name, "event_written": event, "date_written": date, "start": start,
         "lines": [dict(n=x.pop("n"), **x) for x in lines],
         "shields": [dict(n=x.pop("n"), **x) for x in shields],
         "same_as": "", "changes": [], "notes": list(notes)}
    tot = sum(x.get("count", 1) for x in d["lines"])
    print(pages, name, side, "cards", tot, "shields", sum(x.get("count", 1) for x in d["shields"]))
    json.dump(d, open(f"{OUT}/{STEM}-p{pages[0]}.json", "w"), indent=1, ensure_ascii=False)
    return d

def T(s):
    """typed list line: '*Name (V) (x2)' -> L with count."""
    m = re.search(r"\(x(\d+)\)", s)
    return L(s, c=int(m.group(1)) if m else 1)

RALLOPS = "Ralltiir Operations / In The Hands Of The Empire"
WYS = "Watch Your Step / This Place Can Be A Little Rough"
STUN = "A Stunning Move / A Valuable Hostage"
HDADTJ = "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe"
QMC = "Quiet Mining Colony / Independent Operation"
PROFIT = "You Can Either Profit By This... / Or Be Destroyed"
SYCFA = "Set Your Course For Alderaan / The Ultimate Power In The Universe"
NMNPND = "No Money, No Parts, No Deal! / You're A Slave?"
POD = "Podrace Prep / Everything You Need To Know"  # placeholder, fixed below if needed
HD = "Hidden Base / Systems Will Slip Through Your Fingers"
REND = "Rendezvous Point On Tatooine"

decks = []

# ---------------- p1 Ziemowit Skwara DS (typed list) ----------------
P1 = """*Grand Moff Tarkin (V)
*Imperial Command
*Outflank (V)
*Sniper & *Dark Strike
*Imbalance & *Kintan Strider
Cold Feet (V)
Imperial Barrier
*Limited Resources
*Close Call (V)
Alter (Premiere) (V)
Sense
*You Are Beaten
Monnok
Ghhhk
*Masterful Move & *Endor Occupation
I Have You Now
*Emperor's Personal Shuttle
*Boba Fett In Slave I (V)
*Dengar In Punishing One
*Zuckuss In Mist Hunter
*Victory
*Blizzard 4 (V)
*Blizzard 2 (V)
*Kir Kanos With Force Pike
*Ice-Heart
*Sergeant Major Bursk (V)
*Janus Greejatus
*Colonel Davod Jon
*Grand Admiral Thrawn
*Admiral Ozzel
*General Veers (V)
*General Nevar
*Mara Jade With Lightsaber
*Darth Vader With Lightsaber (x2)
*Darth Maul With Lightsaber (x3)
*Emperor Palpatine (x3)
*Kashyyyk
*Ralltiir: Spaceport Financial District
<>Spaceport Docking Bay
<>Spaceport Prefect's Office
<>Spaceport Street
*Something Special Planned For Them (V)
*Search And Destroy
*Tarkin's Bounty (V)
*First Strike
*The Phantom Menace (AI)
Imperial Decree (V)
*Ni Chuba Na?? (V)
*Endor Shield (V)
*Insignificant Rebellion (V)
*Prepared Defenses (V)
*Ralltiir"""
l = [T(s) for s in P1.splitlines()]
for x in l:
    if x["text"] == "Alter (Premiere) (V)": x["card"] = "Alter"
l.insert(0, L("Sunsdown Combo", "Sunsdown & Too Cold For Speeders", False))
l.append(L("Ralltiir Operations/In The Hands Of The Empire", RALLOPS, False))
l.append(L("*Knowledge And Defense (V) (1 starting)", "Knowledge And Defense", True))
SH = """*Do They Have A Code Clearance? (V) (1 starting)
*Leave Them To Me (V) (1 starting)
*A Useless Gesture (V) (1 starting)
*We'll Let Fate-a Decide, Huh? (V) (1 starting)
*Resistance (1 starting)
Abyss (V) (1 starting)
*Battle Order (1 starting)
*Secret Plans (1 starting)
*Come Here You Big Coward (1 starting)
*Allegations Of Corruption (1 starting)
*Firepower (V) (1 starting)"""
sh = [T(s) for s in SH.splitlines()]
sh.insert(2, L("*You Cannot Hide Forever (V) (1 starting) [struck] -> Imperial Detention", "Imperial Detention", False))
decks.append(deck([1], "Ziemowit Skwara \"Kryptofis\"", "DS", RALLOPS, l, sh, deck_name="Super Rops",
     notes=["Typed list headed 'Dark Side - Super Rops'; handwritten 'DS 1ST PLACE 12 VP (1.22)' and stats box.",
            "'Sunsdown Combo' handwritten at top left (added card) -> Sunsdown & Too Cold For Speeders.",
            "Shield 'You Cannot Hide Forever (V)' struck and replaced by handwritten 'Imperial Detention' (no (V) written).",
            "'(xN)' recorded as count; '(AI)' on The Phantom Menace = alternate image.",
            "UNSURE: '*Ice-Heart' - no card of that title found in GEMP or wiki; card left blank, printed as written."]))

# ---------------- p2 Ziemowit Skwara LS (typed list) ----------------
P2 = """*No Questions Asked (V) (x3)
*Punch It!
*Dark Approach (V)
*Grimtaash
Houjix & Out Of Nowhere
*Goo Nee Tay
*Scrambled Transmission (V)
*Honor Of The Jedi
Imperial Atrocity (V)
Rebel Barrier (x2)
*Corellian Retort (V)
**All Wings Report In & *Darklighter Spin (x2)
*Antilles Maneuver (V) (x2)
*Antilles Maneuver & *Rebel Reinforcements (x2)
*Booster In Pulsar Skate
*Obi-Wan in Radiant VII
*BoShek's Modified Light Freighter
*Padme Naberrie (V) (AI)
*Blind Jedi
*Fallen Jedi
*Dash Rendar (V)
*Laudica (V)
*Chewie (V)
*BoShek, Brash Smuggler
*General Crix Madine
*Lando Calrissian, Scoundrel
*Yoda, Great Warrior
*Corran Horn
*Leia, Rebel Princess (x2)
*Wedge Antilles (V)
*Wedge Antilles, Red Squadron Leader
*Luke Skywalker, Jedi Knight (x2)
*Mirax Terrik
*Palejo Reshad
*Romas 'Lock' Navander
*Sergeant Bruckman
<>Spaceport Street
<>Spaceport Docking Bay
<>Spaceport Scoundrels Guild
*Home One: Docking Bay
*Seeking An Audience (V)
Evacuation Control (V)
*Corellian Engineering Corporation (V)
*Wokling (V)
*Insurrection & *Aim High
*Heading For The Medical Frigate
<>Spaceport City
*Captain Han Solo
*Millennium Falcon (V)
*Corellia (V)
Watch Your Step/This Place Can Be A Little Rough (V)
*Anger, Fear, Aggression (V) (1 starting)"""
l = [T(s) for s in P2.splitlines()]
for x in l:
    if x["text"].startswith("Watch Your Step"): x["card"] = WYS
    if x["text"].startswith("*Antilles Maneuver & "):
        x["card"] = "Antilles Maneuver & Rebel Reinforcements"
SH = """*Let's Keep A Little Optimism Here (V) (1 starting)
*Ultimatum (1 starting)
Chasm (V) (1 starting)
*Weapons Display (V) (1 starting)
*Simple Tricks And Nonsense (1 starting)
*The Professor (V) (1 starting)
*A Tragedy Has Occurred (1 starting)
*Don't Do That Again (1 starting)
*Battle Plan (1 starting)
*Do, Or Do Not (1 starting)
*Yavin Sentry (V) (1 starting)
Jabba's Prize/Jabba's Prize (1 starting)"""
sh = [T(s) for s in SH.splitlines()]
sh[-1]["card"] = "Jabba's Prize"
decks.append(deck([2], "Ziemowit Skwara \"Kryptofis\"", "LS", WYS, l, sh, deck_name="WYS(v)",
     notes=["Typed list headed 'Light Side - WYS(v)'; handwritten 'LS 1ST PLACE 12 V (1.22)' and stats box.",
            "'*Blind Jedi' -> Rahm Kota, Blind Jedi; '*Fallen Jedi' -> Maris Brood, Fallen Jedi (short deckbuilder names).",
            "'(xN)' recorded as count; '(AI)' on Padme Naberrie (V) = alternate image."]))

# ---------------- p3 Chris Menzel DS (typed spreadsheet) ----------------
l = [L("A Stunning Move / A Valuable Hostage (V)", STUN, True),
     L("Coruscant: Palpatines Quarters (V)", "Coruscant: Palpatine's Quarters", True),
     L("Coruscant: Private Platform (Docking Bay) (V)", "Coruscant: Private Platform (Docking Bay)", True),
     L("Insidious Prisoner (V)"), L("Prepared Defenses (V)"), L("Gift of the Master (V)", "Gift Of The Master", True),
     L("Ni Chuba Na?? (V)"), L("Jabba's Haven (V)"), L("Knowledge and Defense (V)", "Knowledge And Defense", True),
     L("Cyborg Commander, Hunter of Jedi (V)", "Cyborg Commander, Hunter Of Jedi", True, 3),
     L("Galen, Secret Apprentice (V)", c=3), L("Darth Maul, Young Apprentice", c=2), L("Darth Maul"), L("P-59"),
     L("Dengar with Blaster Carbine (V)", "Dengar With Blaster Carbine", True),
     L("Battle Droid Squad (V)", c=2), L("Dr. Evazan and Ponda Baba", "Dr. Evazan & Ponda Baba"),
     L("4-Lom with Concussion Rifle (V)", "4-LOM With Concussion Rifle", True),
     L("Victory (V)"), L("Zuckuss in Mist Hunter", "Zuckuss In Mist Hunter"), L("Boba Fett in Slave I (V)", "Boba Fett In Slave I", True),
     L("Maul's Sith Infiltrator", c=2), L("Dark Jedi Lightsaber (V)"), L("Maul's Double Bladed Lightsaber", "Maul's Double-Bladed Lightsaber"),
     L("Galens Lightsaber, Vader's Gift (V)", "Galen's Lightsaber, Vader's Gift", True), L("Trophy of a Kill (V)", "Trophy Of A Kill", True),
     L("Hoth: Wampa Cave"), L("Death Star: War Room (V)"), L("Nal Hutta"), L("Blockade Flagship: Bridge"), L("Blockade Flagship: Docking Bay"),
     L("Blaster Rack (V)"), L("No Escape"), L("The Phantom Menace", c=2), L("Imperial Justice (V)"),
     L("Why Didn't You Tell Me? (V)", c=2), L("ComScan Detection (V)", c=2), L("Imbalance & Kintan Strider (V)"),
     L("A Dark Time For The Rebellion", c=2), L("They're Still Coming Through!"),
     L("Operational As Planned (V) [2 corrected to 1]", "Operational As Planned", True),
     L("Force Field (V)", c=2), L("Control", c=2), L("Force Push (V)"), L("Masterful Move & Endor Occupation"),
     L("Sniper & Dark Strike"), L("Monnok (handwritten)", "Monnok", False)]
sh = [L("A Useless Gesture (V)"), L("Abyss (V)"), L("Allegations Of Corruption"), L("Battle Order"),
      L("Come Here You Big Coward"), L("Firepower (V)"), L("I Find Your Lack of Faith Disturbing (V)", "I Find Your Lack Of Faith Disturbing", True),
      L("Imperial Detention (V)"), L("Resistance"), L("Secret Plans"), L("Wipe Them Out All Of Them (V)", "Wipe Them Out, All Of Them", True),
      L("You Cannot Hide Forever (V)")]
decks.append(deck([3], "Chris Menzel", "DS", STUN, l, sh, deck_name="General Grievous Deck",
     event="Germany National 2011", date="18.06.2011",
     notes=["'Cyborg Commander, Hunter of Jedi (V)' -> Grievous, Hunter Of Jedi (deck named 'General Grievous Deck'; working title of the virtual card).",
            "Typed spreadsheet ('V 07.03'); handwritten 'DS 2ND PLACE 12 VP (1.19/1.26)'.",
            "Interrupts: Operational As Planned (V) count 2 hand-corrected to 1; '1 Monnok' handwritten in."]))

# ---------------- p4 Chris Menzel LS (typed list with handwritten changes) ----------------
l = [L("Anger, Fear Aggression v", "Anger, Fear, Aggression", True), L("Coruscant: Night Club"),
     L("It Is The Future You See v"), L("Battle Plan & Draw Their Fire"), L("Do, Or Do Not & There Is No Try"),
     L("Quick Draw v"), L("Coruscant: Jedi Council Chamber"),
     L("Naboo: Boss Nass Chambers (handwritten)", "Naboo: Boss Nass' Chambers", False),
     L("Corran Horn"), L("3x Luke Skywalker, Strong In The Force", "Luke Skywalker, Strong In The Force", False, 3),
     L("2 [3x struck] Mace Windu v", "Mace Windu", True, 2), L("2x Master Qui-Gon v", "Master Qui-Gon", True, 2),
     L("Tawss Khaa v"), L("Threepio With His Parts Showing"),
     L("3 [4x struck] Yoda, Master Of The Force", "Yoda, Master Of The Force", False, 3),
     L("Ki Adi Mundi (V) (handwritten)", "Ki-Adi-Mundi", True),
     L("2 [3x struck] Artoo-Detoo In Red 5", "Artoo-Detoo In Red 5", False, 2),
     L("2x Han, Chewie, And The Falcon v", "Han, Chewie, And The Falcon", True, 2),
     L("Bravo Fighter (V) (handwritten)", "Bravo Fighter", True),
     L("2x Jedi Lightsaber v", "Jedi Lightsaber", True, 2), L("Luke's Lightsaber"),
     L("Qui-Gon's Lightsaber (Destiny 5)", "Qui-Gon Jinn's Lightsaber", False, unsure=True),
     L("2 [3x struck] Are You Braindead?!", "Are You Braindead?!", False, 2),
     L("2x Blaster Deflection", "Blaster Deflection", False, 2), L("Control & Tunnel Vision"), L("Dodge"),
     L("2x Jedi Levitation v", "Jedi Levitation", True, 2), L("3x Let The Wookie Win v", "Let The Wookiee Win", True, 3),
     L("2x [Sense struck] Wesa Gotta Grand Army", "Wesa Gotta Grand Army", False, 2),
     L("2x Sorry About The Mess & Blaster Proficiency", "Sorry About The Mess & Blaster Proficiency", False, 2),
     L("5x Speak With The Jedi Council", "Speak With The Jedi Council", False, 5),
     L("1x [2x struck] Were You Looking For Me?", "Were You Looking For Me?", False),
     L("Weapon Levitation (handwritten)", "Weapon Levitation", False),
     L("1x [2x struck] Imperial Atrocity v", "Imperial Atrocity", True), L("Sai'tor Kal Fas v", "Sai'torr Kal Fas", True),
     L("A Few Manouvers (handwritten)", "A Few Maneuvers", False), L("Escape Pod (V) (handwritten)", "Escape Pod", True),
     L("Grimteash (handwritten)", "Grimtaash", False), L("Clash of Sabers (handwritten)", "Clash Of Sabers", False),
     L("Impressive Most Impressive (V) (handwritten)", "Impressive, Most Impressive", True)]
sh = [L("Affect Mind"), L("A Tragedy has Occured", "A Tragedy Has Occurred", False), L("Aim High"),
      L("Another Pathetic Lifeform"), L("Chasm"), L("Don't Do Dat Again'", "Don't Do That Again", False),
      L("Simple Tricks + Nonsense", "Simple Tricks And Nonsense", False), L("Ultimatum"), L("Professor", "The Professor", False),
      L("Weapons Display"), L("Your Insight Serves you well", "Your Insight Serves You Well", False),
      L("Only Jedi Carry this Weapon", "Only Jedi Carry That Weapon", False)]
decks.append(deck([4], "Chris Menzel", "LS", "Coruscant: Night Club", l, sh,
     deck_name="Emperor Too Likes Titty Bars aka Sonn v Mains aka The 2/2 deck",
     notes=["Printout of a web decklist ('Yoda Likes Titty Bars aka Sonn v Mains aka The 2/2 deck', written by Joe Olsen, 2010); "
            "'Yoda' struck and 'Emperor ... too' handwritten; 'Shamelessly copied + changed by CHRIS MENZEL'. "
            "Handwritten 'LS 2ND PLACE 12 VP (1.19/1.26)' and thanks note.",
            "No objective; starting group AFA (V), Coruscant: Night Club, It Is The Future You See (V), BP&DTF, DoDoNot&TINT, Quick Draw (V). start = starting location.",
            "Handwritten count corrections applied (Mace 3->2, Yoda 4->3, Artoo 3->2, Braindead 3->2, WYLFM 2->1, Imperial Atrocity 2->1); "
            "'Sense' struck -> Wesa Gotta Grand Army; Scrambled Transmission v and Seeking An Audience v struck; handwritten additions included. Shields handwritten, no (V) marks.",
            "UNSURE: 'Qui-Gon's Lightsaber (Destiny 5)' -> Qui-Gon Jinn's Lightsaber (check title).",
            "UNSURE: 'Do, Or Do Not & There Is No Try' - no such combo card; card left blank, printed as written."]))

CCT = "Carbon Chamber Testing / My Favorite Decoration"
COT = "Center Of Tyranny / A Liberated World"
# ---------------- p5 Marvin Tegeler DS (handwritten, abbreviations) ----------------
l = [L("Knowledge + Defense V", "Knowledge And Defense", True), L("CCT", CCT, False),
     L("CL: CC", "Cloud City: Carbonite Chamber", False), L("CC: Tower", "Cloud City: Security Tower", False),
     L("CCC", "Carbonite Chamber Console", False), L("Any Methods", "Any Methods Necessary", False),
     L("IG-88 V", "IG-88", True), L("IG-88's Neural Inhibitor"), L("JP: Dungeon", "Jabba's Palace: Dungeon", False),
     L("JP: Audience Chamber", "Jabba's Palace: Audience Chamber", False), L("Death Star"),
     L("Death Star: WR V", "Death Star: War Room", True), L("Naboo"),
     L("D: PO", "Dengar In Punishing One", False), L("B: HT V", "Bossk In Hound's Tooth", True),
     L("Bis in Ship", "", False), L("Victory"), L("Emperors Shuttle", "Emperor's Personal Shuttle", False),
     L("Mauls Ship", "Maul's Sith Infiltrator", False),
     L("EPP Maul x3", "Darth Maul With Lightsaber", False, 3), L("EPP Vader x3", "Darth Vader With Lightsaber", False, 3),
     L("Emperor V x2", "The Emperor", True, 2), L("GMT V x2", "Grand Moff Tarkin", True, 2),
     L("Stormtrooper Garrison x2", "Stormtrooper Garrison", False, 2), L("ISB Sector Commander"),
     L("EPP Kir Kanos", "Kir Kanos With Force Pike", False), L("EPP Mara", "Mara Jade With Lightsaber", False),
     L("Dr. E. Combo", "Dr. Evazan & Ponda Baba", False), L("Lando V", "Lando Calrissian", True),
     L("First Strike"), L("Blast Door Controls"), L("Security Precautions"),
     L("Image of a Dark Lord", "Image Of The Dark Lord", False), L("Presence of the Force", "Presence Of The Force", False),
     L("Propaganda V", "Imperial Propaganda", True), L("TPM", "The Phantom Menace", False),
     L("Dark Jedi Presence x2", "Dark Jedi Presence", False, 2), L("Sniper Combo x2", "Sniper & Dark Strike", False, 2),
     L("Dark Time V x3", "A Dark Time For The Rebellion", True, 3), L("Imbalance Combo", "Imbalance & Kintan Strider", False),
     L("Barrier (written over)", "Imperial Barrier", False), L("Stunning Leader"),
     L("Aiii Aaa... x2", "Aiiii! Aaa! Agggggggggg!", False, 2), L("Blow Parried"),
     L("Control Combo", "Control & Set For Stun", False), L("Ghhh Combo", "Ghhhk & Those Rebels Won't Escape Us", False),
     L("Sense x2", "Sense", False, 2)]
sh = [L("Secret Plans"), L("Grabber", "", False), L("Abyss V", "Abyss", True), L("Battle Order"),
      L("Oppressive Enforcement"), L("Coward", "Come Here You Big Coward", False),
      L("Leave them to me V", "Leave Them To Me", True), L("You Cannot Hide V", "You Cannot Hide Forever", True),
      L("Firepower V", "Firepower", True), L("Resistance"), L("A Useless Gesture V", "A Useless Gesture", True),
      L("Code Clearance V", "Do They Have A Code Clearance?", True)]
decks.append(deck([5], "Marvin Tegeler", "DS", CCT, l, sh,
     notes=["Handwritten on squared paper; 'DS MARVIN TEGELER 3RD PLACE 12 VP (1.19/1.21)'. Lines in reading order, 'xN' as count. 'V' after a title = (V).",
            "'D: PO' / 'B: HT V' read as pilot-in-ship abbreviations (Dengar In Punishing One; Bossk In Hound's Tooth (V)).",
            "UNSURE: 'Bis in Ship' (first letter overwritten) - not identified; card left blank.",
            "UNSURE: 'Barrier' written over another word -> Imperial Barrier.",
            "UNSURE: shield 'Grabber' - no such DS card found; card left blank.",
            "'EPP' = Darth Maul/Darth Vader/Mara Jade/Kir Kanos 'With Lightsaber/Force Pike' cards; 'Emperor V' -> The Emperor (V)."]))

# ---------------- p6 Marvin Tegeler LS (handwritten, abbreviations) ----------------
l = [L("Anger, Fear, Aggression V", "Anger, Fear, Aggression", True), L("Center of Tyranny", COT, False),
     L("Coruscant V", "Coruscant", True), L("Coruscant: Power Plant", "Coruscant: Main Power Plant", False), L("Coruscant: Lower Level", "Coruscant: Lower Levels", False),
     L("Planet Shield", "Planetary Shiel", False), L("Rogue Insertion"), L("Medical Frigate", "Heading For The Medical Frigate", False),
     L("Infirmary", "Bacta Infirmary", False), L("Rogue Squadron Tactics"),
     L("Declaration", "Declaration Of Rebellion", False), L("Dressel"),
     L("Coruscant: SLP", "Coruscant: Senate Landing Platform", False),
     L("N: BNC", "Naboo: Boss Nass' Chambers", False), L("H1: WR", "Home One: War Room", False),
     L("HCF x2", "Han, Chewie, And The Falcon", False, 2), L("R2 in R5 x2", "Artoo-Detoo In Red 5", False, 2),
     L("B in PS", "Booster In Pulsar Skate", False), L("Obi in RVII", "Obi-Wan In Radiant VII", False),
     L("GL in Go1 V", "Gold Leader In Gold 1", True),
     L("Luke, Rebel Hero x3", "Luke Skywalker, Rebel Hero", False, 3), L("Corran x2", "Corran Horn", False, 2),
     L("Wedge, RSL x2", "Wedge Antilles, Red Squadron Leader", False, 2),
     L("New Wes x2", "Wes Janson", True, 2), L("New Tycho", "Tycho Celchu", True), L("New Ten Numb", "Ten Numb", True),
     L("New Dutch", "Dutch", True), L("Kin Kian"), L("Keir Santage"), L("Biggs, Dead Rogue", "Biggs, Rogue Legend", False),
     L("New Hobbie", "Derek 'Hobbie' Klivian", True), L("Dash V", "Dash Rendar", True),
     L("Narra x2", "Commander Narra", False, 2), L("Lukes Blaster V", "Luke's Blaster Pistol", True),
     L("Disruptor Pistol"), L("Yub Yub Commander x3", "Yub Yub, Commander", False, 3),
     L("Take the Initiative x3", "Take The Initiative", False, 3), L("Rebel Artillery x2", "Rebel Artillery", False, 2),
     L("Houjix Combo", "Houjix & Out Of Nowhere", False), L("Wesa Gotta Grand Army"),
     L("Rebel Leadership V", "Rebel Leadership", True), L("Flash of Insight V", "Flash Of Insight", True),
     L("Commando Training Combo", "Commando Training & K'lor'slug", False),
     L("Imperial Atrocity V", "Imperial Atrocity", True), L("Coruscant Celebration"),
     L("Nabrun x2", "Nabrun Leids", False, 2)]
sh = [L("Battle Plan"), L("Professor V", "The Professor", True), L("Simple Tricks", "Simple Tricks And Nonsense", False),
      L("Wise Advice"), L("Insight V", "Your Insight Serves You Well", True),
      L("Don't do that again V", "Don't Do That Again", True), L("Weapons Display V", "Weapons Display", True),
      L("Grabber", "", False), L("Chasm V", "Chasm", True), L("Optimism V", "Let's Keep A Little Optimism Here", True),
      L("Aim High V", "Aim High", True), L("Ultimatum")]
decks.append(deck([6], "Marvin Tegeler", "LS", COT, l, sh,
     notes=["Handwritten on squared paper; 'LS MARVIN TEGELER 3RD PLACE 12 VP (1.19/1.21)'. Lines in reading order, 'xN' as count.",
            "UNSURE: 'New Wes x2', 'New Tycho', 'New Ten Numb', 'New Dutch', 'New Hobbie' -> base character with v=true (\"new\" = virtual version); exact virtual title not confirmed.",
            "UNSURE: 'Infirmary' -> Bacta Infirmary; 'Biggs, Dead Rogue' -> Biggs, Rogue Legend.",
            "UNSURE: shield 'Grabber' - no such LS card found; card left blank.",
            "'Center of Tyranny' -> Center Of Tyranny / A Liberated World (objective). Coruscant sites / 'Planet Shield' -> Virtual Block 7 cards (wiki title of the device is 'Planetary Shiel')."]))

DDT_NOTE = "Players Committee 2010 form; name 'David DeStefanis', username 'DDT'; no event/date; defensive shields section left blank."
# ---------------- p7 David DeStefanis DS ----------------
l = [L("Executor - Med Chamber", "Executor: Meditation Chamber", False), L("Prepared Defenses", "Prepared Defenses", False),
     L("I'll Take Them Myself", "I'll Take Them Myself", True), L("IAO & SP", "Imperial Arrest Order & Secret Plans", False),
     L("YCHF & MP", "You Cannot Hide Forever & Mobilization Points", False),
     L("Exe:", "", False, unsure=True), L("Exe:", "", False, unsure=True), L("Exe:", "", False, unsure=True), L("Exe:", "", False, unsure=True),
     L("Flagship Exe", "Flagship Executor", False), L("Katana", "Katana", True),
     L("Dreadnaught (+6 ditto)", "Dreadnaught-Class Heavy Cruiser", False, 7),
     L("TIE Assault Squadron (+5 ditto)", "TIE Assault Squadron", False, 6),
     L("The Emperor's Sword"), L("———— Shield", "The Emperor's Shield", False),
     L("EPP Maul (+ditto)", "Darth Maul With Lightsaber", False, 2), L("Nizuc Bek (+ditto)", "Nizuc Bek", True, 2),
     L("Juri Juice"), L("EPP 4-LOM (+ditto)", "4-LOM With Concussion Rifle", True, 2), L("R2-Q5", "", False),
     L("U-3PO"), L("Grand Adm. Thrawn", "Grand Admiral Thrawn", True), L("Imperial Command (+ditto)", "Imperial Command", False, 2),
     L("Something SP", "Something Special Planned For Them", True), L("Lateral Damage"),
     L("Lightsaber Def (+ditto)", "Lightsaber Deficiency", True, 2), L("Gravity Sh (+ditto)", "Gravity Shadow", False, 2),
     L("WMAOP (+ditto)", "We Must Accelerate Our Plans", False, 2), L("Imp Decree", "Imperial Decree", True),
     L("Ghhhk & TRWEU", "Ghhhk & Those Rebels Won't Escape Us", False), L("Protocol Failure", "Protocol Failure", True),
     L("Fondor"), L("Wakeelmui"), L("Tatooine"), L("Naboo"), L("Sienar Fl Syst", "Sienar Fleet Systems", False),
     L("Galactic Dom", "Galactic Domination", True), L("Tarkin's Orders"), L("Flops", "Flagship Operations", False),
     L("Look Sir Droids", "Look Sir, Droids", True), L("Force Push", "Force Push", True),
     L("Knowledge & Def", "Knowledge And Defense", True)]
decks.append(deck([7], "David DeStefanis", "DS", "Executor: Meditation Chamber", l, [], deck_name="Katana Flops", username="DDT",
     notes=[DDT_NOTE, "Handwritten 'DS 4TH PLACE 12 VP (1.13)'. Numbered lines 1-60; ditto runs recorded as count.",
            "Lines 6-9 written only as 'Exe:' (four Executor sites, unspecified) - card left blank.",
            "UNSURE: line 34 'R2-Q5' - not found in GEMP or wiki; card left blank.",
            "UNSURE: line 55 'Galactic Dom' -> Galactic Domination; line 57 'Flops' -> Flagship Operations (effect; no objective in deck)."]))

# ---------------- p8 David DeStefanis LS ----------------
l = [L("Hidden Base", HD, True), L("Tatooine"), L("Rebel Cell: Hidden Landing Site", "Rebel Cell - Hidden Landing Site", True),
     L("Uncharted Settlements", "Uncharted Settlements", True), L("HFTMF", "Heading For The Medical Frigate", False),
     L("Wokling", "Wokling", True), L("Nick Of Time", "Nick Of Time", True), L("Superficial Damage", "Superficial Damage", True),
     L("Tatooine Celebration (+ditto)", "Tatooine Celebration", False, 2),
     L("Incom Corp. & Koensayr FC.", "Incom Corporation & Koensayr Manufacturing", True),
     L("Sandspeeder (+6 ditto)", "Sandspeeder", False, 7), L("Houjix"),
     L("Dash In Rogue 10", "Dash In Rogue 10", True), L("Dual Laser Cannons (+2 ditto)", "Dual Laser Cannon", True, 3),
     L("Golan Laser Batt", "Golan Laser Battery", False), L("Medium Repeating Bl", "Medium Repeating Blaster Cannon", False),
     L("Heavy Turbo", "Heavy Turbolaser Battery", False), L("Home One (+ditto)", "Home One", False, 2),
     L("Admiral Ackbar", "Admiral Ackbar", True), L("General Carlist Rieekan", "General Carlist Rieekan", True),
     L("Kin Kian"), L("Cmdr Wedge", "Commander Wedge Antilles", True), L("Luke Skywalker", "Luke Skywalker", True),
     L("Artillery Remote (+ditto)", "Artillery Remote", False, 2), L("Corporal Beezer"),
     L("Slight Weapon M (+2 ditto)", "Slight Weapons Malfunction", False, 3), L("Desperate Tactics"),
     L("Rapid Fire"), L("C&TV", "Control & Tunnel Vision", False), L("Sorry ATM & BP (+ditto)", "Sorry About The Mess & Blaster Proficiency", False, 2),
     L("On Target"), L("Rebel Artillery (+ditto)", "Rebel Artillery", False, 2),
     L("Rebel Cell:", "", True, unsure=True), L("———— :", "", True, unsure=True), L("———— :", "", True, unsure=True),
     L("Home One: War Room"), L("Rebel Leadership (+ditto)", "Rebel Leadership", True, 2),
     L("Antilles Man & RR", "Antilles Maneuver & Rebel Reinforcements", True),
     L("Noco", "", True, unsure=True), L("Noco", "", True, unsure=True),
     L("Hoth: War Room", "Hoth: Echo Command Center (War Room)", False), L("Home One: War Room (2nd copy)", "Home One: War Room", False),
     L("Captain Verrack", "Captain Verrack", True), L("Anger Fear Aggression", "Anger, Fear, Aggression", True)]
decks.append(deck([8], "David DeStefanis", "LS", HD, l, [], deck_name="The Green Line", username="DDT",
     notes=[DDT_NOTE, "Handwritten 'LS 4TH PLACE 12 VP (1.13)'. Numbered lines 1-60; ditto runs recorded as count.",
            "Lines 48-50 'Rebel Cell:' plus two ditto dashes - three Rebel Cell sites, unspecified; card left blank.",
            "UNSURE: lines 55-56 'Noco' (V) - not identified; card left blank.",
            "Home One: War Room written twice (lines 51 and 58) - transcribed as written."]))

def typed(block):
    out = []
    for s in block.strip().splitlines():
        x = T(s.strip())
        if x["card"].startswith("Alter (Premiere)") or x["card"].startswith("Alter (Coruscant)"): x["card"] = "Alter"
        out.append(x)
    return out

# ---------------- p9 Angelo DS (typed 'DS-HDv.txt') ----------------
l = typed("""Cold Feet (V)
*You Are Beaten
*Outflank (V)
*Hound's Tooth (V)
*Bossk (V)
*Conquest (V)
*Mara Jade's Lightsaber
*Jabba's Palace: Lower Passages
*Blast Door Controls
*Jabba's Palace: Audience Chamber
*Tatooine: Jabba's Palace
*The Emperor (V)
*According To My Design
*Aurra Sing
*Guild of Assassins (1 starting)
*Arica (V)""")
l.append(L("Hunt Down And Destroy The Jedi/Their Fire Has Gone Out Of The Universe (V) (1 starting)", HDADTJ, True))
l += typed("""*Coruscant (1 starting)
*Coruscant: Imperial City (1 starting)
*A Sith's Plans (1 starting)
*Prepared Defenses (V) (1 starting)
*Gift Of The Master (1 starting)
*Endor Shield (V) (1 starting)
*Combat Response (1 starting)
*Knowledge And Defense (V) (1 starting)
*Black Leader (AI)
*P-59
*Kir Kanos With Force Pike
*Grand Admiral Thrawn
*Dr. Evazan & *Ponda Baba
*Boba Fett, Bounty Hunter
*Zuckuss (V)
*Dengar With Blaster Carbine (V)
*Cyborg Commander, Hunter Of Jedi
*Galen, Secret Apprentice (x2)
*Darth Vader, Betrayer Of The Jedi (x2)
*Vader's Lightsaber
*Galen's Lightsaber, Vader's Gift
Dark Jedi Lightsaber (V)
*Galen's Fighter
*Mist Hunter (V)
*Victory
*Close Call (V) (x2)
*Sniper & *Dark Strike
*Force Field (V) (x2)
*One Beautiful Thing
*Blow Parried
*Masterful Move & *Endor Occupation
*Weapon Levitation & The Empire's Back
*Force Push (V)
Elis Helrot
Sense
Alter (Premiere) (V)
Blaster Rack (V)""")
l.append(L("Endor (handwritten)", "Endor", False))
sh = [L("*Imperial Detention (1 starting) [struck] -> Abyss (V)", "Abyss", True)] + typed("""*Leave Them To Me (V) (1 starting)
*Resistance (1 starting)
*Weapon Of A Sith (1 starting)
I Find Your Lack Of Faith Disturbing (V) (1 starting)
*You Cannot Hide Forever (V) (1 starting)
*Battle Order (1 starting)
*Come Here You Big Coward (1 starting)
*A Useless Gesture (V) (1 starting)
*Allegations Of Corruption (1 starting)
*Firepower (V) (1 starting)
*Secret Plans (1 starting)""")
decks.append(deck([9], "Angelo", "DS", HDADTJ, l, sh,
     notes=["Typed list 'DS-HDv.txt' (shields interleaved with starting cards, separated here); handwritten 'Angelo 5 PLACE 10 VP (1.25)'. Surname not written.",
            "Shield 'Imperial Detention' struck, 'Abyss (V)' handwritten. 'Endor' handwritten at end (60th card).",
            "'Cyborg Commander, Hunter Of Jedi' -> Grievous, Hunter Of Jedi. '(AI)' on Black Leader = alternate image.",
            "Sheet totals 59 cards (plus 12 shields) as written, even with handwritten 'Endor'."]))

# ---------------- p10 Angelo LS (typed 'LS-QMC.txt') ----------------
l = [L("Quiet Mining Colony/Independent Operation (1 starting)", QMC, False)]
l += typed("""*Bespin (1 starting)
*Cloud City: Guest Quarters (1 starting)
*Heading For The Medical Frigate (1 starting)
*Squadron Assignments (1 starting)
*Beldon's Eye (V) (1 starting)
*Keeping The Empire Out Forever (1 starting)
*Anger, Fear, Aggression (V) (1 starting)
Escape Pod (V)
*Grimtaash
**All Wings Report In & *Darklighter Spin
*Dark Approach (V)
We're Doomed
The Bith Shuffle & Desperate Reach
Houjix & Out Of Nowhere
*It's A Hit!
It Could Be Worse
Alternatives To Fighting
Alter (Coruscant) (V)
Sense
Rebel Barrier
Nabrun Leids
*Path Of Least Resistance (x2)
*Sorry About The Mess & *Blaster Proficiency (x2)
*Cloud City Celebration
*Flash Of Insight (V)
*Menace Fades
Imperial Atrocity (V)
**Landing Claw
X-wing Laser Cannon
*Leia's Blaster Rifle
*Spiral
*Han, Chewie, And The Falcon
*BoShek's Modified Light Freighter
*Overseer
*Red Squadron 1
*Artoo-Detoo In Red 5
*Harc Seff (V)
*Wedge Antilles, Red Squadron Leader
*BoShek (V)
*Luke Skywalker (V)
*Pucumir Thryss
*Kebyc (V)
*Yoxgit
*Mirax Terrik
*Lando Calrissian, Scoundrel
*Corran Horn
*Padme Naberrie (V)
*Leia, Rebel Princess
*Princess Leia (V)
*Obi-Wan With Lightsaber (x2)
*Qui-Gon Jinn With Lightsaber (x2)
*Bespin: Cloud City
*Cloud City: West Gallery
*Cloud City: Upper Plaza Corridor
*Cloud City: North Corridor""")
sh = typed("""*Your Insight Serves You Well (V) (1 starting)
*Simple Tricks And Nonsense (1 starting)
*Don't Do That Again (V) (1 starting)
*Another Pathetic Lifeform (V) (1 starting)
*Do, Or Do Not (1 starting)
*Ultimatum (1 starting)
*Battle Plan (1 starting)
*A Tragedy Has Occurred (1 starting)
Chasm (V) (1 starting)
*The Professor (V) (1 starting)
*Aim High (1 starting)
*Weapons Display (V) (1 starting)""")
decks.append(deck([10], "Angelo", "LS", QMC, l, sh,
     notes=["Typed list 'LS-QMC.txt' ('Seite 1', single page; shields interleaved with starting cards, separated here); handwritten 'Angelo 5 PLACE 10 VP (1.25)'.",
            "Small handwritten '<- 1' marks beside 'Do, Or Do Not' and 'The Professor' (meaning unclear; no effect on list)."]))

def cat_list(path, objective_text=None, obj_card=None):
    """typed list with [Category] headers; returns lines, shields."""
    lines, shields, sec = [], [], ""
    for s in open(path).read().splitlines():
        s = s.strip()
        if not s: continue
        m = re.match(r"^\[([^\]]+)\]\s*(.*)$", s)
        if m:
            sec = m.group(1); s = m.group(2)
            if not s: continue
        if objective_text and s == objective_text:
            lines.append(L(s, obj_card, False)); continue
        x = T(s)
        if x["card"].startswith("Alter ("): x["card"] = "Alter"
        (shields if sec == "Defensive Shield" else lines).append(x)
    return lines, shields

l, sh = cat_list("/tmp/claude-0/-home-claude/89b0b907-d4b4-53cc-bc54-8fba9b724b03/scratchpad/old/hi/G51/p11.txt", "A Stunning Move/A Valuable Hostage", STUN)
decks.append(deck([11], "Cedrik Vanderhaegen", "DS", STUN, l, sh,
     notes=["Typed list grouped by card type; header 'Cedrik Vanderhaegen - DS'; handwritten 'DS 6 PLACE 10 VP (1.25)'.",
            "'Cyborg Commander, Hunter Of Jedi' -> Grievous, Hunter Of Jedi.",
            "UNSURE: '***IG Bodyguard droid (x2)' - no such card in GEMP or wiki; card left blank.",
            "UNSURE: 'He Is Not Ready & Imperial Propaganda' kept as written (combo not found in GEMP or wiki)."]))
l, sh = cat_list("/tmp/claude-0/-home-claude/89b0b907-d4b4-53cc-bc54-8fba9b724b03/scratchpad/old/hi/G51/p12.txt")
decks.append(deck([12], "Cedrik Vanderhaegen", "LS", "", l, sh,
     notes=["Typed list grouped by card type; header 'Cedrik Vanderhaegen - LS'; handwritten 'LS 6 PLACE 10 VP (1.25)'.",
            "No objective; only starting card marked is Anger, Fear, Aggression (V) (1 starting) - start left blank.",
            "'*Blind Jedi' -> Rahm Kota, Blind Jedi; '*Fallen Jedi' -> Maris Brood, Fallen Jedi (short deckbuilder names)."]))

BHBM = "Bring Him Before Me / Take Your Father's Place"
MB_NOTE = "Players Committee 2010 form; name 'Mario Boley'; no username/event/date/deck name."
# ---------------- p13 Mario Boley DS ----------------
l = [L("Knowledge and Defense", "Knowledge And Defense", True), L("Bring Him Before Me", BHBM, False),
     L("Death Star II: Throne Room"), L("Insignificant Rebellion"), L("Your Destiny"),
     L("Look Sir, Droids", "Look Sir, Droids", True), L("Tatooine: Mos Eisley"), L("Ni Chuba Na??", "Ni Chuba Na??", True),
     L("You Cannot Hide Forever & Mo. Points", "You Cannot Hide Forever & Mobilization Points", False),
     L("Rendili"), L("Blockade Flagship: Bridge"), L("Blizzard 4"), L("Stinger"), L("Justifier", "Justifier", True),
     L("Maul's Sith Infiltrator"), L("Boba Fett In Slave I", "Boba Fett In Slave I", True), L("Zuckuss In Mist Hunter"),
     L("Janus Greejatus (+2 ditto)", "Janus Greejatus", False, 3),
     L("Darth Vader With Lightsaber (+2 ditto)", "Darth Vader With Lightsaber", False, 3),
     L("Darth Maul With Lightsaber (+2 ditto)", "Darth Maul With Lightsaber", False, 3),
     L("Dr. Evazan & Ponda Baba"), L("The Emperor", "The Emperor", True), L("Grand Moff Tarkin", "Grand Moff Tarkin", True),
     L("Admiral Pellaeon", "Admiral Pellaeon", True), L("Emperor Palpatine"),
     L("Mara Jade With Lightsaber", "Mara Jade With Lightsaber", True), L("Guri"), L("Sim Aloo"),
     L("Force Lightning (+2 ditto)", "Force Lightning", False, 3),
     L("We Must Accelerate Our Plans (+2 ditto)", "We Must Accelerate Our Plans", False, 3),
     L("They're Still Coming Through", "They're Still Coming Through!", False), L("The Circle Is Now Complete (+ditto)", "The Circle Is Now Complete", False, 2),
     L("Your Powers Are Weak, Old Man"), L("Sense"), L("Cease Fire!"), L("Force Field"),
     L("Force Push", "Force Push", True), L("I Have You Now"), L("Imperial Command"), L("Cold Feet", "Cold Feet", True),
     L("Imperial Barrier"), L("Sacrifice"), L("Presence Of The Force"),
     L("Something Special Plann.", "Something Special Planned For Them", True), L("Emperor's Power", "Emperor's Power", True),
     L("So Be It, Jedi", "So Be It, Jedi", True), L("The Phantom Menace (+2 ditto)", "The Phantom Menace", False, 3)]
sh = [L("We'll Let Fate-a Decide, Huh?", "We'll Let Fate-a Decide, Huh?", True),
      L("Wipe Them Out, All Of Them", "Wipe Them Out, All Of Them", True), L("Secret Plans"), L("Oppressive Enforcement"),
      L("Abyss", "Abyss", True), L("Allegations Of Corruption"), L("Imperial Detention", "Imperial Detention", True),
      L("There Is No Try"), L("Battle Order"), L("Firepower", "Firepower", True),
      L("A Useless Gesture", "A Useless Gesture", True), L("Come Here You Big Coward")]
decks.append(deck([13], "Mario Boley", "DS", BHBM, l, sh,
     notes=[MB_NOTE, "Handwritten 'DS 7 PLACE 10 VP (0,95)'. Numbered lines 1-60; ditto runs recorded as count.",
            "Line 33 'Gari' read as Guri."]))

# ---------------- p14 Mario Boley LS ----------------
l = [L("Anger, Fear, Aggression", "Anger, Fear, Aggression", True), L("Dagobah: Yoda's Hut"),
     L("Communing", "Communing", True), L("Master Kenobi", "Master Kenobi", True), L("Rogue Insertion", "Rogue Insertion", True),
     L("Declaration Of Rebellion", "Declaration Of Rebellion", True), L("First Aid"), L("Rebel Artillery"), L("Rebel Barrier"),
     L("Hear Me Baby, Hold Together", "Hear Me Baby, Hold Together", True), L("Sabotage", "Sabotage", True),
     L("Yub Yub, Commander", "Yub Yub, Commander", True), L("Jedi Levitation", "Jedi Levitation", True),
     L("We'll Find Han", "We'll Find Han", True), L("Control & Tunnel Vision"), L("Were You Looking For Me?"),
     L("Run Luke, Run!", "Run Luke, Run!", True, 2), L("Rebel Leadership", "Rebel Leadership", True, 2),
     L("Use The Force", "Use The Force", True), L("Tatooine: Cantina"), L("Tatooine"),
     L("Tatooine: City Outskirts", "Tatooine: City Outskirts", True), L("Hoth: Echo Command Center"),
     L("Home One: War Room"), L("Tatooine: Obi-Wan's Hut", "Tatooine: Obi-Wan's Hut", True),
     L("I Can't Believe He's Gone", "I Can't Believe He's Gone", True), L("What're You Tryin' To Push On Us?"),
     L("Launching The Assault"), L("Obi-Wan's Apparition", "Obi-Wan's Apparition", True),
     L("Commando Training & K'lor'slug", "Commando Training & K'lor'slug", True),
     L("Stone Pile", "Stone Pile", False, 2), L("Alderaan Consular Ship", "Alderaan Consular Ship", True), L("Spiral"),
     L("Home One"), L("Tantive IV", "Tantive IV", True), L("Bright Hope", "Bright Hope", True),
     L("Threepio With His Parts", "Threepio With His Parts Showing", False), L("Han With Heavy Blaster Pistol"),
     L("Bail Organa, Father of Rebellion", "Bail Organa, Father Of Rebellion", True), L("Corran Horn"),
     L("Dack Ralter", "Dack Ralter", True), L("Derek 'Hobbie' Klivian", "Derek 'Hobbie' Klivian", True),
     L("Admiral Ackbar", "Admiral Ackbar", True), L("Princess Leia", "Princess Leia", True, 2),
     L("Rebel Scout", "Rebel Scout", True, 2), L("Blind Jedi", "Rahm Kota, Blind Jedi", True),
     L("Luke Skywalker, Rebel Hero", "Luke Skywalker, Rebel Hero", True, 2), L("Chewie, Enraged"),
     L("Wedge Antilles, Red Squad. L.", "Wedge Antilles, Red Squadron Leader", True),
     L("Wedge Antilles, RSL", "Wedge Antilles, Red Squadron Leader", False),
     L("Lando Cal., Scoundrel", "Lando Calrissian, Scoundrel", False, 2),
     L("Leia's Sporting Blaster", "Leia's Sporting Blaster", True), L("Luke's Blaster Pistol", "Luke's Blaster Pistol", True)]
sh = [L("Battle Plan"), L("A Tragedy has occured", "A Tragedy Has Occurred", False), L("Wise Advice"),
      L("Chasm", "Chasm", True), L("Aim High"), L("Your Insight Serves You Well", "Your Insight Serves You Well", True),
      L("Simple Tricks and Nonsense", "Simple Tricks And Nonsense", True), L("Do, Or Do Not"),
      L("Don't Do That Again", "Don't Do That Again", True), L("The Professor", "The Professor", True),
      L("Affect Mind", "Affect Mind", True), L("Let's Keep A Little Optimism", "Let's Keep A Little Optimism Here", True)]
decks.append(deck([14], "Mario Boley", "LS", "Dagobah: Yoda's Hut", l, sh,
     notes=[MB_NOTE, "Handwritten 'LS 7 PLACE 10 VP (0,95)'. Numbered lines 1-60, repeated titles written out (recorded as count).",
            "No objective; start = starting location Dagobah: Yoda's Hut (line 2).",
            "Wedge Antilles, Red Squadron Leader x2: first copy (V) ticked, second not. 'Blind Jedi' -> Rahm Kota, Blind Jedi."]))

def numbered(block):
    """'text | card | v | count' lines (card '=' -> same as text; v 1/0)."""
    out = []
    for s in block.strip().splitlines():
        p = [x.strip() for x in s.split("|")]
        text = p[0]; card = p[1] if len(p) > 1 and p[1] not in ("", "=") else (None if len(p) < 2 or p[1] == "=" else "")
        if len(p) > 1 and p[1] == "": card = re.sub(r"\s*\(V\)", "", text)
        v = (p[2] == "1") if len(p) > 2 else None
        c = int(p[3]) if len(p) > 3 else 1
        x = L(text, card, v, c)
        if len(p) > 4: x["ep1"] = True
        out.append(x)
    return out

# ---------------- p15 Dirk Friedrichs DS (typed 2002 PC form) ----------------
l = numbered("""Knowledge And Defense (V)
No Money, No Parts, No Deal! | No Money, No Parts, No Deal! / You're A Slave? | 0
Tatooine: Watto's Junkyard
Tatooine: Mos Espa
Prepared Defenses (V)
Kuat Drive Yards (V)
Endor Shield (V)
Breached Defenses & Molator (V)
Blockade Flagship: Bridge
Endor
Tatooine (Premiere) | Tatooine | 0
Jabba's Palace: Audience Chamber
Darth Vader With Lightsaber | | 0 | 2
Darth Maul With Lightsaber | | 0 | 2
Mara Jade With Lightsaber (V) | | 1 | 2
Emperor Palpatine
Grand Admiral Thrawn
Admiral Chiraneau
General Veers (V)
General Nevar (V)
Grand Moff Tarkin (V)
Ice-Heart (V) | - | 1
ISB Sector Commander (V)
Dr. Evazan | | 0 | 2
Velken Tezeri (V)
J'Quille (V)
Watto (V) | | 1 | 3
Battle Droid Squad (V)
Conquest (V)
Boba Fett In Slave I (V)
Bossk In Hound's Tooth (V)
Victory (V)
Zuckuss In Mist Hunter
Devastator (V)
Blizzard 2 (V)
Blizzard 4 (V)
We're In Attack Position Now
You Cannot Hide Forever
Search And Destroy
Disarmed | | 0 | 2
Lateral Damage
Tatooine Occupation | | 0 | 2
We Must Accelerate Our Plans | | 0 | 2
Tarkin's Orders
According To My Design (V)
Imperial Barrier | | 0 | 2
Force Push (V)
Imperial Command
Control & Set For Stun
Ghhhk & Those Rebels Won't Escape Us""")
for x in l:
    if x["text"] == "Ice-Heart (V)": x["card"] = ""
sh = numbered("""A Useless Gesture (V)
Wipe Them Out, All Of Them (V)
Battle Order
There Is No Try
Come Here You Big Coward
I Find Your Lack Of Faith Disturbing (V)
Leave Them To Me (V)
Firepower (V)
Allegations Of Corruption
You Cannot Hide Forever (V)
Secret Plans
Resistance""")
decks.append(deck([15], "Dirk Friedrichs", "DS", NMNPND, l, sh, deck_name="Watto New Deal",
     event="Ralltiir Regionals", date="18/06/11",
     notes=["Typed 2002 SWCCG Players Committee form (no (V) boxes; v taken from '(V)' in the title); handwritten 'DS 8 PLACE 8 VP (1.13/1.18)'.",
            "Repeated lines recorded as count. UNSURE: 'Ice-Heart (V)' - no card of that title found; card left blank."]))

# ---------------- p16 Dirk Friedrichs LS (typed 2010 PC form) ----------------
l = numbered("""Watch Your Step | Watch Your Step / This Place Can Be A Little Rough | 0
Tatooine (Episode I) | Tatooine | 0 | 1 | ep1
Tatooine: Cantina
Tatooine: Docking Bay 94
Podrace Prep
Tatooine: Podrace Arena
Boonta Eve Podrace
Anakin's Podracer
Squadron Assignments
Kessel
Corellia | | 1
Luke Skywalker | | 1 | 2
Han, Courageous Smuggler | | 1 | 2
Chewbacca | | 1 | 2
Mirax Terrik
BoShek, Brash Smuggler | | 1
Dash Rendar
Melas | | 1
Ralltiir Freighter Captain
Talon Karrde | | 0 | 2
Wedge Antilles | | 1
Phylo Gandish
Red Squadron 1
BoShek's Modified Light Freighter | | 1
Millenium Falcon | Millennium Falcon | 0
Outrider
Artoo-Detoo In Red 5
Pulsar Skate
Chewie's AT-ST | | 1 | 2
X-Wing Laser Cannon | X-wing Laser Cannon | 0
Combined Fleet Action
I'll Take The Leader
I Did It!
Imperial Atrocity | | 1
Menace Fades
Old Ben
It Could Be Worse
Corellian Retort | | 1 | 2
It's A Hit!
Hyper Escape
A Few Maneuvers
Out Of Commission & Transmission Terminated
Don't Get Cocky
Jedi Levitation | | 1
Life Debt
Power Pivot
Control & Tunnel Vision | | 0 | 2
All Wings Report In & Darklighter Spin | | 0 | 3
Rebel Barrier | | 0 | 2
Anger, Fear, Aggression | | 1""")
sh = numbered("""Jabba's Prize | | 1
Battle Plan
A Tragedy Has Occured | A Tragedy Has Occurred | 0
Aim High
Chasm | | 1
The Professor | | 1
Simple Tricks And Nonsense | | 1
Don't Do That Again | | 1
Yavin Sentry | | 1
Ultimatium | Ultimatum | 0
Your Insight Serves You Well | | 1
Weapons Display | | 1""")
decks.append(deck([16], "Dirk Friedrichs", "LS", WYS, l, sh, deck_name="WYS racing", username="Uber-Obi",
     event="Ralltiir Regionals", date="06/28/11",
     notes=["Typed 2010 SWCCG Players Committee form with ticked (V) boxes; handwritten '8 PLACE 8 VP (1.13/1.18)' with a struck-through 'DS' at top though the sheet is Light.",
            "Event 'Ralltiir Regionals' typed on both of his sheets (dates 18/06/11 and 06/28/11) though filed with the German National 2011 lists."]))

def two_col(block):
    out = []
    for s in block.strip().splitlines():
        s = s.strip()
        m = re.match(r"^(.*?)\s*\{(.*)\}$", s)   # explicit card in {}
        card = m.group(2) if m else None
        if m: s = m.group(1)
        v = "(v)" in s or "(V)" in s
        base = card if card is not None else re.sub(r"\s*\((v|V)\)", "", s).strip()
        if out and out[-1]["text"] == s and "count" not in out[-1].get("_", ""):
            out[-1]["count"] = out[-1].get("count", 1) + 1; continue
        out.append({"text": s, "card": base, "v": v})
    return out

HK_NOTE = "Typed two-column list; handwritten name reads 'Horst Knepper' (spelling uncertain). Repeated typed lines recorded as count."
# ---------------- p17 Horst Knepper DS ----------------
l = two_col("""Set Your Course For Alderaan {Set Your Course For Alderaan / The Ultimate Power In The Universe}
Dreaded Imperial Starfleet (v)
Kuat Drive Yards (v)
A Million Voices Crying Out
Prepared Defenses
Alderaan
Death Star Docking Bay {Death Star: Docking Bay 327}
Death Star
In Range
In Range
In Range
In Range
In Range
Relentless Pursuit
Relentless Pursuit
Tractor Beam
Tractor Beam
Tractor Beam
Tractor Beam
Laser Cannon Battery
Laser Cannon Battery
Emperor Palpatine
Emperor Palpatine
Emperor Palpatine
Emperor Palpatine
They´ve Shut Down The Main Reactor {They've Shut Down The Main Reactor}
They´ve Shut Down The Main Reactor {They've Shut Down The Main Reactor}
Our First Catch Of The Day
Our First Catch Of The Day
Superlaser
I Can´t Shake Him {I Can't Shake Him!}
I Can´t Shake Him {I Can't Shake Him!}
Flawless Marksmanship
Flawless Marksmanship
Vengeance
Visage
Tyrant
Avenger
Judicator
Thunderflare
Chimera {Chimaera}
Cpt. Lennox {Captain Lennox}
Stalker
Warrant Officer M´kae {Warrant Officer M'Kae}
Imperial Barrier
Imperial Barrier
Rendili
Carida
Intensify The Forward Batterys {Intensify The Forward Batteries}
Cpt. Godherdt {Captain Godherdt}
Raithal
Devastator (v)
4-Lom With Concussion Rifle (v) {4-LOM With Concussion Rifle}
4-Lom With Concussion Rifle (v) {4-LOM With Concussion Rifle}
Death Star War Room (v) {Death Star: War Room}
Evacuate (v) {Evacuate?}
Evacuate (v) {Evacuate?}
Death Star Central Core (v) {Death Star: Central Core}
Commence Primary Ignition (v)
Knowledge And Defense (v)""")
sh = two_col("""I Find Your Lack Of Faith Disturbing (v)
Firepower (v)
Do They Have A Code Clearance (v) {Do They Have A Code Clearance?}
After her (v) {After Her!}
Abyss (v)
Resistance
There is no try {There Is No Try}
Come here you big coward {Come Here You Big Coward}
Allegations of Corruption {Allegations Of Corruption}
A Useless Guesture (v) {A Useless Gesture}
Battle Order (v)
You Cannot Hide Forever (v)""")
decks.append(deck([17], "Horst Knepper", "DS", SYCFA, l, sh, deck_name="Set Your Course 4 Euro Worlds",
     notes=[HK_NOTE, "Header handwritten 'Dark Side (Set Your Course 4 Euro Worlds) Horst Knepper'; 'DS (9) PLACE 8VP (1.13)'.",
            "Shields listed under 'Nich Im Deck Drin' (not in deck)."]))

# ---------------- p18 Horst Knepper LS ----------------
l = two_col("""Tatooine Slave Quarters {Tatooine: Slave Quarters}
Rogue Insertion (v)
Maneuvering Flaps/ Nick Of Time (v) {Maneuvering Flaps & Nick Of Time}
Communing (v)
Master Kenobi (v)
Artoo Detoo In Red 5 {Artoo-Detoo In Red 5}
Artoo Detoo In Red 5 {Artoo-Detoo In Red 5}
Artoo Detoo In Red 5 {Artoo-Detoo In Red 5}
Corran Horn
Sandspeeder [struck] -> Rebel Barrier {Rebel Barrier}
Sandspeeder
Sandspeeder
Sandspeeder
Sandspeeder
Sandspeeder
Yub Yub, Commander (v)
Yub Yub, Commander (v)
Cmd. Narra (v) {Commander Narra}
Sabotage (v)
Senator Leia Organa (v)
Tatooine Desert {Tatooine: Desert}
Alderan Consular Ship (v) {Alderaan Consular Ship}
Dual Laser Cannon (v)
Tycho Celchu
Sandwhirl
Tatooine City Outskirts {Tatooine: City Outskirts}
Rebel Gunrunner (v)
Keir Santage
Red 6
Wes Janson, Rogue Veteran (v)
Tatooine Celebration
Kin Kian
Insurrection [struck] -> Bith Shuffle/Desperate Reach {The Bith Shuffle & Desperate Reach}
Biggs, Rogue Legend (v)
I Can´t Believe He´s Gone (v) {I Can't Believe He's Gone}
Threepio With His Parts Showing
Blind Jedi (v) {Rahm Kota, Blind Jedi}
Draw Their Fire
Dack Ralter (v)
Luke Skywalker (v)
Luke Skywalker (v)
Tatooine Obi Wan´s Hut (v) {Tatooine: Obi-Wan's Hut}
Shmi Skywalker
Tatooine
Tatooine Hutt Trade Route {Tatooine: Hutt Trade Route (Desert)}
Derek "Hobbie" Klivian {Derek 'Hobbie' Klivian}
Zev Senesca
Jedi Levitation (v)
T 47 Battle Formation [struck] -> Insurrection {Insurrection}
T 47 Battle Formation {T-47 Battle Formation}
Use The Force (v)
Use The Force (v)
Wedge Antilles, RSL {Wedge Antilles, Red Squadron Leader}
Wedge Antilles, RSL {Wedge Antilles, Red Squadron Leader}
Run Luke Run (v) {Run Luke, Run!}
Run Luke Run (v) {Run Luke, Run!}
Desperate tactics {Desperate Tactics}
Desperate tactics {Desperate Tactics}
Tatooine Celebration
An Unusual Amount Of Fear""")
sh = two_col("""Affect Mind (v)
Don´t Do That Again (v) {Don't Do That Again}
Your Insight Serves You Well (v)
A Tragedy Has Occured (v) {A Tragedy Has Occurred}
Battle Plan (v)
Do, Or Do Not (v)
Chasm (v)
Weapons Display (v)
Simple Tricks And Nonsense (v)
Ultimatum (v)""")
decks.append(deck([18], "Horst Knepper", "LS", "Tatooine: Slave Quarters", l, sh, deck_name="Really Grinds My Gears",
     notes=[HK_NOTE, "Header handwritten 'Light Side (Really Grinds My Gears) Horst Knepper'; handwritten 'DS (9) PLACE 8 VP (1.13)' (DS written though LS sheet).",
            "Handwritten replacements applied: Sandspeeder -> Rebel Barrier; Insurrection -> Bith Shuffle/Desperate Reach; T 47 Battle Formation -> Insurrection (a second T 47 line remains).",
            "No objective; start = first listed site Tatooine: Slave Quarters. Only 10 shields listed under 'Nich Im Deck Drin'."]))

# ---------------- p19 Benjamin Jakob DS (typed spreadsheet) ----------------
l = numbered("""No Money No Parts No Deal / You're A Slave | No Money, No Parts, No Deal! / You're A Slave? | 0
Tatooine (Premiere) | Tatooine | 0
Tatooine: Mos Espa
Tatooine: Watto's Junkyard
Prepared Defenses
Kuat Drive Yards (V)
Endor Shield (V)
Breached Defenses & Molator (V)
Knowledge and Defense (V) | Knowledge And Defense | 1
Darth Vader with Lightsaber | Darth Vader With Lightsaber | 0 | 2
Darth Maul with Lightsaber | Darth Maul With Lightsaber | 0 | 2
Mara Jade with Lightsaber (V) | Mara Jade With Lightsaber | 1 | 2
Watto | | 0 | 3
Admiral Ozzel
Grand Admiral Thrawn
General Veers (V)
The Emperor (V)
Janus Greejatus
Dr. Evazan (non-combo) | Dr. Evazan | 0 | 2
Myn Kyneugh (V)
Darth Sidious
Blizzard 4 (V) | | 1 | 2
Conquest (V)
Tyrant
Thunderflare
Devastator
Stalker (V)
Zuckuss in Mist Hunter | Zuckuss In Mist Hunter | 0
Endor
Blockade Flagship Bridge | Blockade Flagship: Bridge | 0
Executor: Meditation Chamber
Hoth: Wampa Cave
Dismarmed | Disarmed | 0 | 2
No Escape
Imperial Decree (V)
Tatooine Occupation | | 0 | 2
Security Precautions
He Is Not Ready & Imperial Propaganda
Comscan Detection (V) | ComScan Detection | 1 | 2
We Must Accelerate Our Plans | | 0 | 2
Imperial Barrier | | 0 | 2
Projective Telepathy
Control & Set For Stun
Masterful Move & Endor Occupation
Elis Helrot
Sniper & Dark Strike
Imperial Command
Ghhhk & Those Rebels Won't Escape Us""")
sh = numbered("""A Useless Gesture (V)
Abyss (V)
Allegations Of Corruption
Battle Order
Come Here You Big Coward
Do They Have A Code Clearance? (V)
Firepower (V)
Resistance
Secret Plans
Wipe Them Out All Of Them (V) | Wipe Them Out, All Of Them | 1
I Find Your Lack of Faith Disturbing (V) | I Find Your Lack Of Faith Disturbing | 1
You Cannot Hide Forever (V)""")
decks.append(deck([19], "Benjamin Jakob", "DS", NMNPND, l, sh, deck_name="Watto: White Slavery Done Right (after Hunter)",
     event="Regional 2011", date="18.06.2011",
     notes=["Typed spreadsheet ('V 07.00', same template as Chris Menzel's); handwritten 'DS (10) PLACE 8 VP (1.10) BEN JAKOB'.",
            "Four empty character rows with count 0 omitted. UNSURE: 'He Is Not Ready & Imperial Propaganda' kept as written (combo not found in GEMP or wiki)."]))

# ---------------- p20 Benjamin Jakob LS (typed 'LS-Profit.txt', page rotated) ----------------
l = typed("""*Anger, Fear, Aggression (V) (1 starting)""")
l.append(L("You Can Either Profit By This.../Or Be Destroyed (1 starting)", PROFIT, False))
l += typed("""*Tatooine: Jabba's Palace (1 starting)
*Jabba's Palace: Audience Chamber (1 starting)
*Han (V) (1 starting)
*Heading For The Medical Frigate (1 starting)
*I Must Be Allowed To Speak (V) (1 starting)
Quick Draw (V) (1 starting)
*Seeking An Audience (V) (1 starting)
*Scrambled Transmission (V) (1 starting)
*Home One: War Room
*Naboo: Boss Nass' Chambers
<>Farm
Sai'torr Kal Fas (V)
*A Gift
Imperial Atrocity (V)
*Impressive, Most Impressive (V)
*It's A Trap!
Rebel Leadership (V) (x2)
It Could Be Worse
*Let The Wookiee Win (V)
*It's A Hit!
*Harvest (V)
*Inconsequential Barriers
We're Doomed
*Wesa Gotta Grand Army (x2)
*Blaster Deflection
*Sorry About The Mess & *Blaster Proficiency (x2)
Nabrun Leids
*A Jedi's Resilience
*Don't Forget The Droids (V) (x2)
Jedi Levitation (V)
Tatooine Utility Belt (V)
*Leia's Blaster Rifle
*Anakin's Lightsaber (V)
Jedi Lightsaber (V)
*Obi-Wan's Lightsaber
*Luke's Lightsaber
*Home One
*Admiral Ackbar (V)
*R2-D2 (Artoo-Detoo) (V)
*Threepio With His Parts Showing
*Padme Naberrie (V)
*Corran Horn
*Lando Calrissian, Scoundrel
*Chewbacca, Protector
*Yoda, Great Warrior (x2)
*Leia, Rebel Princess
*Boushh
*Obi-Wan Kenobi (V) (x3)
*Luke Skywalker, Strong In The Force (x3)""")
for x in l:
    if x["text"].startswith("*R2-D2"): x["card"] = "R2-D2 (Artoo-Detoo)"
sh = typed("""*Your Insight Serves You Well (V) (1 starting)
*Ultimatum (1 starting)
*The Professor (V) (1 starting)
*Simple Tricks And Nonsense (1 starting)
*Only Jedi Carry That Weapon (1 starting)
*Let's Keep A Little Optimism Here (V) (1 starting)
*Don't Do That Again (V) (1 starting)
*Do, Or Do Not (1 starting)
*Battle Plan (1 starting)
*Another Pathetic Lifeform (V) (1 starting)
*Aim High (1 starting)
*A Tragedy Has Occurred (1 starting)""")
decks.append(deck([20], "Benjamin Jakob", "LS", PROFIT, l, sh,
     notes=["Typed list 'LS-Profit.txt' printed sideways ('Seite 1', single page); some characters smudged by the scan. Handwritten 'LS BEN JAKOB (10) PLACE 8 VP (1.10)'.",
            "Shields interleaved with starting cards in the list, separated here. Sheet order kept otherwise."]))
