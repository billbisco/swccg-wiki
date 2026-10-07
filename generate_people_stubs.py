#!/usr/bin/env python3
"""Generate SWCCG historian person stubs, Squadron Members hub, and fan-site articles."""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
PEOPLE_DIR = PAGES / "people"
ROSTER = ROOT / "people" / "sm_roster.tsv"

GEO = "https://www.geocities.ws/plarathas/SMs.html"
GEO_ANA = "https://www.geocities.ws/plarathas/anagrams.html"
OOC = "https://www.oocities.org/collegepark/plaza/9433/anagrams.html"
REO = "https://web.archive.org/web/20160406045459/http://www.reocities.com/CollegePark/plaza/9433/anagrams.html"
PC = "https://www.starwarsccg.org/decipher-swccg-squadron-members/"
ENCYC = "https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf"
RFD = "https://wiki.lotrtcgpc.net/wiki/Radio_Free_Decipher"
PC_ADV = "https://web.archive.org/web/20160117001353/http://decipher.ruddog.com/starwars/playerscommittee1.html"
TFN = "http://www.theforce.net/ccg/flashback/article.asp"

# Existing well-sourced stubs: do not overwrite; generator writes extras into people/ for new names only.
SKIP_WRITE = {
    "Chuck Kallenbach",
    "Tom Braunlich",
    "Rollie Tesh",
    "Jerry Darcy",
    "Warren Holland",
    "Tom Lischke",
    "Justin Pakes",
    "Joe Alread",
}

# Anagram extras keyed by wiki title.
ANAGRAMS = {
    "Chuck Kallenbach": [
        ("[[Chall Bekan]]", "Kallenbach (family)"),
        ("[[Imperial Helmsman]] (Bachenhall)", "Kallenbach (family)"),
        ("[[Blizzard 2]] (Nevar) / [[Nevar Yalnal]]", "Raven, Kallenbach's dog"),
        ("[[Chyler]]", "Cheryl Kallenbach"),
    ],
    "Jonathan Quesenberry": [("[[Bren Quersey]]", "Jonathan Quesenberry, Red Leader")],
    "Rob Burns": [("[[Bron Burs]]", "Rob Burns, artist; ''The Good, the Bad and the Ugly''")],
    "Michael Girard": [("[[Caldera Righim]]", "Michael Girard, Gold 120")],
    "Sandy Wible": [
        ("[[Captain Bewil]]", "Sandy Wible, game designer"),
        ("[[Nysad]]", "Sandy Wible"),
    ],
    "John Sarnecki": [("[[Corporal Kensaric]]", "John Sarnecki, Gold 7")],
    "Jerry Darcy": [
        ("[[Rayc Ryjerd]] / [[Rycar Ryjerd]]", "Jerry Darcy"),
        ("[[Djas Puhr]]", "Jasper, Jerry Darcy's cat"),
        ("[[Laudica]]", "Claudia Darcy"),
    ],
    "Rollie Tesh": [("[[Elis Helrot]]", "Rollie Tesh, game creator")],
    "Kyle Heuer": [("[[Elyhek Rue]]", "Kyle Heuer, Rogue Leader")],
    "Maarten Logge": [("[[Ghana Gleemort]]", "Maarten Logge")],
    "Mark Schaffer": [("[[Harc Seff]]", "Mark Schaffer, Gold 41")],
    "Jason Winter": [("[[Chief Retwin]]", "Jason Winter, former Decipher staff")],
    "Becky Higgerson": [("[[Kebyc]]", "Becky Higgerson")],
    "Claudia Darcy": [("[[Laudica]]", "Claudia Darcy, Jerry Darcy's wife")],
    "Leslie Burns": [("[[Leesub Sirlin]]", "Leslie Burns")],
    "Stacy Mollema": [("[[Leslomy Tacema]]", "Stacy Mollema, Lucasfilm licensing")],
    "Tom Lischke": [("[[Lieutenant Sheckil]]", "Tom Lischke, game designer")],
    "Bill Martinson": [("[[Lieutenant Tarn Mison]]", "Bill Martinson")],
    "Eric Olson": [("[[Loci Rosen]]", "Eric Olsen / Olson, Bravo 7")],
    "Tim Courtney": [("[[Murttoc Yine]]", "Tim Courtney, Red 37")],
    "Tom Braunlich": [("[[Nabrun Leids]]", "Braunlich, game creator")],
    "Joe Alread": [("[[Palejo Reshad]]", "Joseph Alread, Gold 79 intern")],
    "Keith Skipton": [("[[Pote Snitkin]]", "Keith Skipton (uncertain on the fan list)")],
    "Curtiss Murphy": [("[[Pucumir Thryss]]", "Curtiss Murphy (relation marked ???? on the fan list)")],
    "Kendrick Summers": [("[[R'kik D'nec]]", "Kendrick Summers, Gold Leader")],
    "Warren Holland": [("[[Sandcrawler]] lore (Warren-like)", "Warren Holland, Decipher CEO")],
    "Carol Wisely": [("[[Swilla Corey]]", "Carol Wisely")],
    "Justin Pakes": [("[[Tanus Spijek]]", "Justin Pakes (listed as AUSSIE on the fan page)")],
    "Kevin Reitzel": [("[[Velken Tezeri]]", "Kevin Reitzel, Bravo Leader")],
    "Mark Tuttle": [("[[Warrant Officer M'Kae]]", "Mark McKay, Mark Tuttle's radio name")],
    "Mike Gray": [("[[Yerka Mig]]", "Mike Gray")],
    "Cheryl Kallenbach": [("[[Chyler]]", "Cheryl Kallenbach")],
    "Bob Madison": [("[[Dainsom]]", "Bob / Will Madison")],
}

EXTRA_PEOPLE = [
    # name, lead extra sentences (wikitext, already cited where needed)
    (
        "Sandy Wible",
        "'''Sandy Wible''' (also '''Will \"Sandy\" Wible''') was Decipher's official online network representative in the Premiere era and later a Product Development game designer.",
        [
            "In January 1996 he posted a SWCCG rarity list to Usenet as \"Official Online Network Representative for Decipher Inc.\" with the Genie address used for Decipher's online presence.",
            "Chuck Kallenbach later recalled that Decipher needed an internet representative on the Genie boards; Wible won the role over Kallenbach, then invited Kallenbach to playtest SWCCG.",
            "Radio Free Decipher broadcast 25 (17 September 1999) interviewed \"Product Development's Sandy Wible\" on fall 1999 CCG news. In that episode Carol Wisely walked the succession of Rebel Base Leader / Jedi Master online-rules accounts, placing Wible after Tom Braunlich (\"Answer Man\") and Jerry Darcy as an early Rebel Base Leader / first Jedi Master.",
        ],
        [
            f"[https://groups.google.com/g/rec.arts.sf.starwars.collecting/c/mVSQQWI1He4 rec.arts.sf.starwars.collecting rarity list, 4 January 1996] (Will \"Sandy\" Wible byline)",
            f"[{TFN} TheForce.Net Flashback interview with Chuck Kallenbach] (Red 84 / Josh Radke)",
            f"[{RFD} Radio Free Decipher episode index] (broadcast 25)",
            f"[{GEO_ANA} Anagramed Decipherians] (Captain Bewil / Nysad)",
        ],
        ["People", "Decipher", "History"],
    ),
    (
        "Carol Wisely",
        "'''Carol Wisely''' was Decipher's Vice President of Marketing and the original host of [[Radio Free Decipher]].",
        [
            "The LOTR-TCG Players Committee's RFD index states the show ran 1998–2004 (196 episodes) and was originally hosted by Wisely; after episode 30, Kyle Heuer and Evan Lorentz took over regular hosting.",
            "Decipher's contemporary RFD blurb called the show the authentic voice of Young Jedi, Austin Powers, Star Trek and Star Wars CCGs.",
        ],
        [
            f"[{RFD} Radio Free Decipher episode index], LOTR-TCG PC wiki",
            f"[{GEO_ANA} Anagramed Decipherians] (Swilla Corey)",
        ],
        ["People", "Decipher", "History"],
    ),
    (
        "Mark Tuttle",
        "'''Mark Tuttle''' was a Decipher playtester and later staffer (rules \"net rep\" / PR). The anagram list records [[Warrant Officer M'Kae]] as Mark McKay, \"Mark Tuttle's radio name.\"",
        [
            "In a 2018 Fantha Tracks interview Tuttle described SWCCG as \"Tom and Rollie's game\" and recalled being recruited from ''Star Trek'' CCG community work into ''Star Wars'' playtesting around ''A New Hope''.",
            "He later hosted Decipher WARS Radio (2004–2005) and Decipher Games Radio (2005) after Radio Free Decipher ended.",
        ],
        [
            "[https://www.fanthatracks.com/interviews/guest-interview-mark-tuttle/ Guest Interview: Mark Tuttle], Fantha Tracks, 15 March 2018",
            f"[{RFD} Radio Free Decipher / WARS / Games Radio index]",
            f"[{GEO_ANA} Anagramed Decipherians]",
        ],
        ["People", "Decipher", "History"],
    ),
    (
        "Bill Martinson",
        "'''Bill Martinson''' was a Decipher Product Development staffer; the anagram list unscrambles [[Lieutenant Tarn Mison]] as Bill Martinson.",
        [
            "Radio Free Decipher broadcast 1 (4 December 1998, audio missing from the public rehost) listed Carol Wisely hosting with guests Bill Martinson and Tim Ellington on Star Trek CCG's Dominion expansion.",
            "Broadcast 4 (8 January 1999) interviewed Martinson on the Trek set after Dominion and on SWCCG Endor. Broadcasts 12–13 (April 1999) paired him with Jerry Darcy on Young Jedi and Endor.",
        ],
        [
            f"[{RFD} Radio Free Decipher episode index]",
            f"[{GEO_ANA} Anagramed Decipherians]",
        ],
        ["People", "Decipher", "History"],
    ),
    (
        "Cheryl Kallenbach",
        "'''Cheryl Kallenbach''' is named on the fan anagram list as the unscrambling of [[Chyler]]. The same list treats [[Chall Bekan]] and Imperial Helmsman (Bachenhall) as Kallenbach family names.",
        [
            "No independent Decipher staff title for Cheryl was located this pass beyond the anagram relation. Do not invent a job.",
        ],
        [
            f"[{GEO_ANA} Anagramed Decipherians]",
            f"[{ENCYC} SWCCG Collecting Encyclopedia 3.2] (p.200)",
        ],
        ["People", "Decipher", "History"],
    ),
    (
        "Rob Burns",
        "'''Rob Burns''' is named on the fan anagram list as the artist unscrambling of [[Bron Burs]] (the card is tagged UGLY on that list, pairing it with ''The Good, the Bad and the Ugly'' in-jokes [[Debnoli]] / [[Gela Yeens]]).",
        [
            "No separate Decipher employment record was located this pass. The relation is the published anagram mapping only.",
        ],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "Decipher", "History"],
    ),
    (
        "Jason Winter",
        "'''Jason Winter''' is named on the fan anagram list as a former Decipherian, the unscrambling of [[Chief Retwin]].",
        [],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "Decipher", "History"],
    ),
    (
        "Becky Higgerson",
        "'''Becky Higgerson''' is named on the fan anagram list as a Decipherian, the unscrambling of [[Kebyc]].",
        [],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "Decipher", "History"],
    ),
    (
        "Claudia Darcy",
        "'''Claudia Darcy''' is named on the fan anagram list as Jerry Darcy's wife, the unscrambling of [[Laudica]].",
        [
            "This stub records only the published anagram relation. It is not a biography.",
        ],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "Decipher", "History"],
    ),
    (
        "Leslie Burns",
        "'''Leslie Burns''' is named on the fan anagram list as a Decipherian, the unscrambling of [[Leesub Sirlin]].",
        [],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "Decipher", "History"],
    ),
    (
        "Stacy Mollema",
        "'''Stacy Mollema''' is named on the fan anagram list as Lucasfilm licensing, the unscrambling of [[Leslomy Tacema]].",
        [
            "The relation is the published fan mapping (also copied onto Encyclopedia 3.2 p.200). No separate Lucasfilm staff directory was located this pass.",
        ],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "History"],
    ),
    (
        "Maarten Logge",
        "'''Maarten Logge''' is named on the fan anagram list as the unscrambling of [[Ghana Gleemort]]. The relation column on that list is blank.",
        [],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "History"],
    ),
    (
        "Keith Skipton",
        "'''Keith Skipton''' is the uncertain unscrambling of [[Pote Snitkin]] on the fan anagram list (printed with question marks as a Decipherian).",
        [
            "Treat as unconfirmed until a Decipher primary credit is found.",
        ],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "Decipher", "History"],
    ),
    (
        "Curtiss Murphy",
        "'''Curtiss Murphy''' is named on the fan anagram list as the unscrambling of [[Pucumir Thryss]], with the relation column marked \"????\".",
        [],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "History"],
    ),
    (
        "Mike Gray",
        "'''Mike Gray''' is named on the fan anagram list as a Decipherian, the unscrambling of [[Yerka Mig]].",
        [],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "Decipher", "History"],
    ),
    (
        "Bob Madison",
        "'''Bob Madison''' / '''Will Madison''' is the fan-list unscrambling of Imperial Trooper Guard [[Dainsom]] (\"[Bob/Will] Madison\", Decipherian).",
        [
            "The published list does not choose between Bob and Will. Do not invent which Madison is meant.",
        ],
        [f"[{GEO_ANA} Anagramed Decipherians]", f"[{ENCYC} Encyclopedia 3.2 p.200]"],
        ["People", "Decipher", "History"],
    ),
]

# Extra sourced notes for squadron / staff people (beyond the roster row).
NOTES = {
    "Kendrick Summers": [
        "Gold Leader at Decipher Inc. He hosted early [[Radio Free Decipher]] broadcasts (including broadcast 2 with Jerry Darcy, Tom Lischke, and Chuck Kallenbach on 11 December 1998) and later appeared as a regular SWCCG organized-play guest (Endor, DecipherCon).",
        "The anagram list unscrambles [[R'kik D'nec]] as Kendrick Summers.",
    ],
    "Jonathan Quesenberry": [
        "Red Leader at Decipher Inc. Radio Free Decipher broadcast 10 (5 March 1999) lists him as host, interviewing Sean Smallman on tournament software.",
        "The anagram list unscrambles [[Bren Quersey]] as Jonathan Quesenberry. The published squadron tables sometimes spell the given name Jonathon.",
    ],
    "Kyle Heuer": [
        "Listed as Red 7 (Decipher Inc.), later Rogue Leader. After RFD episode 30 he and Evan Lorentz took over regular hosting from Carol Wisely.",
        "The anagram list unscrambles [[Elyhek Rue]] as Kyle Heuer.",
    ],
    "Kevin Reitzel": [
        "Bravo Leader at Decipher Inc. RFD broadcast 3 (18 December 1998) interviewed him with Kyle Heuer as a new marketing-team member. A fan world-finals history page lists Kevin Reitzel among the 1996 Vail world-final field (Joe Alread 3rd, Reitzel 4th).",
        "The anagram list unscrambles [[Velken Tezeri]] as Kevin Reitzel.",
    ],
    "Chuck Kallenbach": [
        "Gold 2, Overland, Missouri, on the published squadron roster (status Retired). See the main article for playtest / 1997 staff path.",
    ],
    "Joe Alread": [
        "Gold 79 FL, Normal, Illinois, on the published squadron roster; the anagram list calls Joseph Alread a Gold 79 intern and unscrambles [[Palejo Reshad]]. A fan world-finals history page places Joe Alread 3rd at the 1996 Vail world finals.",
    ],
    "Michael Girard": [
        "Gold 120, Apache Junction, Arizona. Named in Warren Holland's 25 January 2002 Players' Committee announcement as the first Player Advocate for Player Support.",
        "The anagram list unscrambles [[Caldera Righim]] as Michael Girard.",
    ],
    "John Arendt": [
        "Bravo 16, Boulder, Colorado. Named in Holland's 25 January 2002 announcement as the first Player Advocate for Tournament Support.",
    ],
    "Joe Helfrich": [
        "Bravo 15, Westminster, Colorado. Named in Holland's 25 January 2002 announcement as a first Player Advocate for Rules Support (with Greg Anderson).",
    ],
    "Greg Anderson": [
        "Rogue 31, Ellicott City, Maryland. Named in Holland's 25 January 2002 announcement as a first Player Advocate for Rules Support (with Joe Helfrich).",
    ],
    "Eric Olson": [
        "Bravo 7, Lisle, Illinois. Named in Holland's 25 January 2002 announcement as a first Player Advocate for Gameplay Support (with Doug Taylor). The anagram list spells the unscrambling of [[Loci Rosen]] as Eric Olsen.",
    ],
    "Doug Taylor": [
        "Red 4 FL, Lynnwood, Washington. Named in Holland's 25 January 2002 announcement as a first Player Advocate for Gameplay Support (with Eric Olson).",
    ],
    "John Sarnecki": [
        "Gold 7, Munster, Indiana. The anagram list unscrambles [[Corporal Kensaric]] as John Sarnecki.",
    ],
    "Mark Schaffer": [
        "Gold 41, Hampton, Virginia. The anagram list unscrambles [[Harc Seff]] as Mark Schaffer.",
    ],
    "Tim Courtney": [
        "Red 37, Webster, Texas (status Retired on the fan table). The anagram list unscrambles [[Murttoc Yine]] as Tim Courtney.",
    ],
    "Josh Radke": [
        "Red 84, Terryville, Connecticut. Wrote TheForce.Net Flashback Premiere interview with Chuck Kallenbach, bylined as Red 84.",
    ],
    "Marcus Certa": [
        "Red 5, Burlington, Vermont. Frequent Radio Free Decipher guest in 1999 (broadcasts 5, 19, 21, 22) on SWCCG / Young Jedi organized play.",
    ],
    "Alex Alcalde": [
        "Gold 31 FL, Indianapolis, Indiana. RFD broadcast 9 (26 February 1999) included a squadron/ambassador call-in with Chris Swearingen, Alex Alcalde, Mike Hardy, and Guy Kargl.",
    ],
    "Carl \"Mike\" Hardy": [
        "Red 32 FL, Pleasanton, California. RFD broadcast 9 call-in guest (billed Mike Hardy).",
    ],
    "Guy Kargl": [
        "Red 61 FL, Tulsa, Oklahoma. RFD broadcast 9 call-in guest.",
    ],
    "Jim Colson": [
        "Gold 5 FL, Huntsville, Alabama. RFD broadcast 10 discussed Star Trek CCG in the Alabama region with Jonathan Quesenberry.",
    ],
    "Dan Bojanowski": [
        "Gold 95, Springfield, Missouri. Later RFD appearances discuss Territorial Opens / LOTR organized play (broadcast 121 index).",
    ],
    "Ryan Morris": [
        "Red 69 FL, Santa Barbara, California. RFD broadcast 23 (20 August 1999) interviewed him on Young Jedi decks.",
    ],
    "Doug Faust": [
        "Rogue 40, Ithaca, New York. A 2005 DeckTech LOTR tournament report on archive.org is signed Doug Faust and mentions Jim Van Fleet running the event.",
    ],
    "Jim Van Fleet": [
        "Red 15 FL, Mifflinburg, Pennsylvania. Named as tournament organizer in a 2005 archived DeckTech LOTR report by Doug Faust.",
    ],
    "Justin Pakes": [
        "The anagram list unscrambles [[Tanus Spijek]] as Justin Pakes (AUSSIE). See the main article for RFD design-guest labels.",
    ],
    "Tom Lischke": [
        "The anagram list unscrambles [[Lieutenant Sheckil]] as Tom Lischke. See the main article for RFD design-guest labels.",
    ],
}


def load_roster():
    rows = []
    with ROSTER.open(encoding="utf-8") as f:
        for rec in csv.DictReader(f, delimiter="\t"):
            rows.append(rec)
    return rows


def rank_label(rec) -> str:
    sq = rec["squadron"]
    num = rec["number"]
    fl = " FL" if rec["fl"] == "FL" else ""
    if num == "Leader":
        return f"{sq} Leader"
    return f"{sq} {num}{fl}"


def wiki_title(name: str) -> str:
    return name


def fname(title: str) -> str:
    return title.replace(" ", "_").replace('"', "").replace("'", "'") + ".wiki"


def cats(names) -> str:
    return "\n".join(f"[[Category:{c}]]" for c in names)


def stub_for_person(name: str, recs: list[dict], extra_lead: str | None = None, extra_paras=None, extra_sources=None, extra_cats=None) -> str:
    recs = recs or []
    extra_paras = extra_paras or NOTES.get(name, [])
    lines = []
    if extra_lead:
        lines.append(extra_lead)
    elif recs:
        bits = []
        for r in recs:
            bits.append(f"{rank_label(r)} from {r['town']}")
        lead = f"'''{name}''' was a Decipher-era [[Squadron Members|Squadron Member]], listed as {'; '.join(bits)}."
        if recs[0]["status"] and recs[0]["status"] not in ("Retired",):
            lead += f" The published fan table records status: {recs[0]['status']}."
        else:
            lead += " The published fan table marks the slot Retired after Decipher's SWCCG run."
        lines.append(lead)
    else:
        lines.append(f"'''{name}''' appears in Decipher-era SWCCG sources (anagram list and/or staff credits).")

    lines.append("")
    lines.append("This page is a '''fan encyclopedia''' stub. It records only published SWCCG-related facts. It is not a biography and does not add private life.")
    lines.append("")

    if recs:
        lines.append("== Squadron listing ==")
        lines.append("")
        lines.append('{| class="wikitable"')
        lines.append("! Slot !! Town !! Status (fan table)")
        for r in recs:
            lines.append("|-")
            lines.append(f"| {rank_label(r)} || {r['town']} || {r['status']}")
        lines.append("|}")
        lines.append("")
        lines.append("Decipher recruited volunteer Squadron Members in the 1990s to promote SWCCG locally (tournaments, demos, player support). \"FL\" is printed on some slots in the surviving tables; the tables do not spell out the abbreviation.")
        lines.append("")

    if name in ANAGRAMS:
        lines.append("== Anagrams ==")
        lines.append("")
        lines.append("A GeoCities fan page (copied onto Encyclopedia 3.2 p.200) maps these printed titles:")
        lines.append("")
        for card, rel in ANAGRAMS[name]:
            lines.append(f"* {card} — {rel}")
        lines.append("")

    if extra_paras:
        lines.append("== Other sourced notes ==")
        lines.append("")
        for p in extra_paras:
            lines.append(p)
            lines.append("")

    lines.append("== See also ==")
    lines.append("")
    lines.append("* [[Squadron Members]] · [[Anagrams]] · [[Creators of SWCCG]] · [[Radio Free Decipher]]")
    lines.append("* [[Corellian Engineering Corporation (fan site)]]")
    lines.append("")
    lines.append("== Sources ==")
    lines.append("")
    srcs = extra_sources or []
    if recs:
        srcs = [
            f"[{GEO} Squadron Members] (geocities.ws/plarathas, Corellian Engineering fan site)",
            f"[{PC} Decipher SWCCG Squadron Members] (Players Committee reprint)",
        ] + srcs
    if name in ANAGRAMS:
        srcs += [
            f"[{GEO_ANA} Anagramed Decipherians] (geocities.ws)",
            f"[{OOC} Anagramed Decipherians] (oocities.org)",
            f"[{REO} Anagramed Decipherians] (reocities / Wayback 6 April 2016)",
            f"[{ENCYC} SWCCG Collecting Encyclopedia 3.2] (p.200)",
        ]
    # de-dupe preserve order
    seen = set()
    for s in srcs:
        if s not in seen:
            lines.append(f"* {s}")
            seen.add(s)
    lines.append("")
    lines.append(cats(extra_cats or (["People", "Squadron Members", "History"] if recs else ["People", "History"])))
    lines.append("")
    return "\n".join(lines)


def write_page(title: str, body: str, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    path = dest_dir / fname(title)
    path.write_text(body.replace("\r\n", "\n"), encoding="utf-8")
    return path


def hub(rows: list[dict]) -> str:
    by = defaultdict(list)
    for r in rows:
        by[r["squadron"]].append(r)
    order = ["Gold", "Red", "Bravo", "Rogue"]
    out = []
    out.append("'''Squadron Members''' (often abbreviated '''SM''') were Decipher's volunteer local promoters for ''Star Wars'' CCG in the 1990s: they hosted tournaments, ran demos, and helped players.")
    out.append("")
    out.append("Decipher organized them as Gold, Red, Bravo, and Rogue squadrons, with Leaders usually listed at Decipher Inc. The surviving public tables are a fan transcription of that roster (GeoCities ''Corellian Engineering Corporation'' / plarathas) later reprinted by the [[Players Committee]].")
    out.append("")
    out.append("This wiki keeps the list as '''history'''. Towns are as published on those public volunteer tables. Vacant numbered slots (printed \"-----\") are omitted. Obvious typing errors on the GeoCities HTML (for example Virgina, Elletsville, Mithc, An=rendain) are repaired in the person titles; the original strings remain on the source pages.")
    out.append("")
    out.append("The same fan site asked Squadron Members to help complete a set of black-border signed X-wings, Y-wings, Snowspeeders, and Naboo Starfighters.")
    out.append("")
    out.append("== How the lists survive ==")
    out.append("")
    out.append("* Original GeoCities path: <code>geocities.com/plarathas/</code> and <code>geocities.com/CollegePark/Plaza/9433/</code> (same site; last homepage note 15 August 2005, GenCon / SWCCG Worlds in Indianapolis).")
    out.append("* Live mirrors: [https://www.geocities.ws/plarathas/SMs.html geocities.ws] · [https://www.oocities.org/collegepark/plaza/9433/ oocities.org].")
    out.append("* Reocities copy used by Encyclopedia 3.2 for [[Anagrams]].")
    out.append(f"* PC reprint (1 July 2021): [{PC} Decipher SWCCG Squadron Members] (\"This is the original list of Squadron Members.\"). The PC table drops the fan site's Status column and fills some truncated names (Red 3 [[Jason Robinette]] vs GeoCities \"Jason R\").")
    out.append("")
    out.append("== First Players' Committee advocates (January 2002) ==")
    out.append("")
    out.append("Warren Holland's 25 January 2002 announcement named six Player Advocates. Several were already Squadron Members:")
    out.append("")
    out.append("* [[Michael Girard]] — Player Support (Gold 120)")
    out.append("* [[John Arendt]] — Tournament Support (Bravo 16)")
    out.append("* [[Joe Helfrich]] and [[Greg Anderson]] — Rules Support (Bravo 15 / Rogue 31)")
    out.append("* [[Eric Olson]] and [[Doug Taylor]] — Gameplay Support (Bravo 7 / Red 4 FL)")
    out.append("")
    out.append("Holland wrote that the committee would become a new Product Champion Squadron working beside the existing squadrons, and that GamePlayers Network would help with web tools and prize shipping after 30 April 2002.")
    out.append("")
    for sq in order:
        out.append(f"== {sq} Squadron ==")
        out.append("")
        out.append('{| class="wikitable sortable"')
        out.append("! Slot !! Name !! Town !! Status")
        for r in by[sq]:
            title = wiki_title(r["name"])
            out.append("|-")
            out.append(f"| {rank_label(r)} || [[{title}]] || {r['town']} || {r['status']}")
        out.append("|}")
        out.append("")
    out.append("== See also ==")
    out.append("")
    out.append("* [[Anagrams]] · [[Anagramed Decipherians]] · [[Creators of SWCCG]] · [[Radio Free Decipher]]")
    out.append("* [[Corellian Engineering Corporation (fan site)]] · [[DeckTech]] · [[GamePlayers Network]]")
    out.append("* [[History of the Players Committee]] · [[Players Committee]]")
    out.append("")
    out.append("== Sources ==")
    out.append("")
    out.append(f"* [{GEO} Squadron Members] at geocities.ws/plarathas")
    out.append("* [https://www.oocities.org/collegepark/plaza/9433/ oocities.org CollegePark/plaza/9433] (same GeoCities site)")
    out.append(f"* [{PC} Decipher SWCCG Squadron Members], starwarsccg.org, published 1 July 2021")
    out.append(f"* [{PC_ADV} The Star Wars Players' Committee], Warren Holland, 25 January 2002 (ruddog / Wayback)")
    out.append("")
    out.append("[[Category:History]]")
    out.append("[[Category:Decipher]]")
    out.append("[[Category:Squadron Members]]")
    out.append("[[Category:People]]")
    out.append("")
    return "\n".join(out)


def site_pages() -> dict[str, str]:
    cec = r"""'''Corellian Engineering Corporation (fan site)''' was a GeoCities SWCCG fan site for the Corellia region, hosted at <code>geocities.com/plarathas/</code> and <code>geocities.com/CollegePark/Plaza/9433/</code>. The surviving homepage calls it an unofficial site (not produced or endorsed by Decipher or Lucasfilm) with decks, strategy, card reviews, a player database, [[Anagrams|Anagramed Decipherians]], and the [[Squadron Members]] roster.

The webmaster mailbox on the preserved pages is the Indiana State University address used as <code>plarathas</code> on Yahoo GeoCities. A sidebar ranks the site in a Top 100 CCG list as id <code>gold31</code>. The last homepage note on the mirrors is 15 August 2005 (GenCon / SWCCG Worlds in Indianapolis; the editor wrote the site had reopened and was looking for contributors).

== Pages preserved ==

{| class="wikitable"
! Page !! Live mirror !! Notes
|-
| Home || [https://www.geocities.ws/plarathas/index-2.html geocities.ws] · [https://www.oocities.org/collegepark/plaza/9433/ oocities] || Awards, anagrams teaser, player database, links
|-
| Squadron Members || [https://www.geocities.ws/plarathas/SMs.html SMs.html] || Gold / Red / Bravo / Rogue tables; signed-card appeal
|-
| Anagramed Decipherians || [https://www.geocities.ws/plarathas/anagrams.html anagrams.html] || Source copied onto Encyclopedia 3.2 p.200
|-
| Player database || [https://www.geocities.ws/plarathas/playerdbase.html playerdbase.html] || Replacement for Decipher's vanished player registry (city + email form; do not copy emails here)
|-
| Opinions / tournaments / decks / card reviews || articles, tournaments, decks, cardrev || Linked from the nav bar; some original <code>geocities.com/plarathas/rules</code> and strategy URLs are dead on the live web
|}

Nav-bar \"Top SWCCG Sites\" on the 2005 homepage: Decipher Inc, Corellian Engineering, SWCCG Players Committee, [[DeckTech]], [[GamePlayers Network]], HoloTable, SWCCG Database.

== Mirrors and archives ==

* [https://www.geocities.ws/plarathas/ geocities.ws/plarathas]
* [https://www.oocities.org/collegepark/plaza/9433/ oocities.org/collegepark/plaza/9433]
* [https://web.archive.org/web/20160406045459/http://www.reocities.com/CollegePark/plaza/9433/anagrams.html reocities anagrams] (Wayback 6 April 2016) — the URL Encyclopedia 3.2 cites

Yahoo closed GeoCities in 2009. These third-party mirrors are why the roster and anagram table still exist.

== See also ==

* [[Squadron Members]] · [[Anagrams]] · [[Anagramed Decipherians]]
* [[DeckTech]] · [[GamePlayers Network]] · [[Radio Free Decipher]]

== Sources ==

* [https://www.geocities.ws/plarathas/index-2.html Corellian Engineering homepage] (geocities.ws)
* [https://www.geocities.ws/plarathas/SMs.html Squadron Members]
* [https://www.geocities.ws/plarathas/anagrams.html Anagramed Decipherians]
* [https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf SWCCG Collecting Encyclopedia 3.2] (p.200 cites the reocities anagrams URL)

[[Category:History]]
[[Category:Websites]]
[[Category:Fan sites]]
"""
    ana = r"""'''Anagramed Decipherians''' is the GeoCities fan page that collected SWCCG card-title anagrams of Decipher staff, squadron members, pets, and movie in-jokes while Decipher employees were still adding them.

The page quotes two unnamed Decipher employees: one said Premiere still hid names of then-current employees; the other said the public list was missing quite a few and would not say which. Encyclopedia 3.2 p.200 copies the table and cites the reocities/Wayback URL.

The wiki reading copy of that table is [[Anagrams]]. Person stubs linked from that page (and from [[Squadron Members]]) are the historian layer: sourced facts only.

== URLs ==

* [https://www.geocities.ws/plarathas/anagrams.html geocities.ws/plarathas/anagrams.html]
* [https://www.oocities.org/collegepark/plaza/9433/anagrams.html oocities.org/collegepark/plaza/9433/anagrams.html]
* [https://web.archive.org/web/20160406045459/http://www.reocities.com/CollegePark/plaza/9433/anagrams.html reocities Wayback 2016-04-06]

== See also ==

* [[Anagrams]] · [[Easter eggs]] · [[Corellian Engineering Corporation (fan site)]] · [[Squadron Members]]

[[Category:History]]
[[Category:Websites]]
[[Category:Fan sites]]
"""
    rfd = r"""'''Radio Free Decipher''' ('''RFD''') was Decipher's weekly RealAudio show, 4 December 1998 – 30 April 2004, about 196 episodes. It predated the word podcast. Topics included SWCCG, Young Jedi, Jedi Knights, Star Trek CCG, Austin Powers, spoilers, DecipherCon, and staff interviews.

[[Carol Wisely]] (VP of Marketing) hosted originally. After episode 30, [[Kyle Heuer]] and Evan Lorentz took over regular hosting. Early SWCCG-heavy episodes also feature [[Kendrick Summers]], [[Jerry Darcy]], [[Chuck Kallenbach]], [[Tom Lischke]], [[Kevin Reitzel]], [[Sandy Wible]], [[Bill Martinson]], [[Justin Pakes]], [[Joe Alread]], [[Marcus Certa]], and squadron call-ins ([[Alex Alcalde]], [[Carl "Mike" Hardy]], [[Guy Kargl]]).

The LOTR-TCG Players Committee rehosted surviving audio on YouTube (Player's Council channel) and keeps an episode index. Many Wayback files truncate at 1&nbsp;MB (~8:43) because of a contemporary RealAudio streaming bug; Evan Lorentz's files filled most gaps. A handful of episodes remain missing.

Successors: Decipher WARS Radio (25 June 2004 – 21 January 2005, host [[Mark Tuttle]]) and a short Decipher Games Radio (March 2005).

== See also ==

* [[Carol Wisely]] · [[Kyle Heuer]] · [[Kendrick Summers]] · [[Creators of SWCCG]]
* [[Squadron Members]]

== Sources ==

* [https://wiki.lotrtcgpc.net/wiki/Radio_Free_Decipher Radio Free Decipher episode index] (LOTR-TCG PC wiki)
* [https://www.youtube.com/playlist?list=PLYLMRQ0b_feAbpbNVQwlw3y8XH30ZQS1U RFD YouTube playlist] (Player's Council)
* [http://web.archive.org/web/20080511223849/http://www.decipher.com/rfd/factsandtips/index.html Decipher RFD facts and tips] (Wayback; RealAudio truncation note)

[[Category:History]]
[[Category:Decipher]]
[[Category:Websites]]
"""
    decktech = r"""'''DeckTech''' (decktech.net) was a major SWCCG (and later other CCG) deck-list and tournament-report site in the late 1990s–2000s. The [[Players Committee]] later wrote that PC forums slowly overtook DeckTech, GamePlayers Network, and other sites as the primary online hangout.

A fan GitHub Pages mirror, [https://stevetotheizz0.github.io/decktech_archives/ SWCCG Decktech Archives] (Stephen Skilton), keeps many posts (1999–2002 and later), including Worlds reports. Wayback still has live decktech.net HTML (for example LOTR reports that name SWCCG Squadron Members as organizers).

== See also ==

* [[GamePlayers Network]] · [[Corellian Engineering Corporation (fan site)]] · [[Squadron Members]]
* [[History of the Players Committee]]

== Sources ==

* [https://www.starwarsccg.org/community-network/ Community Network], starwarsccg.org (forums overtook DeckTech / GPN)
* [https://stevetotheizz0.github.io/decktech_archives/ SWCCG Decktech Archives]
* [https://web.archive.org/web/20050830191851/http://www.decktech.net/lotr/treports/treports.php?id=3842&view=2 Example decktech.net report] (Wayback, 2005; Doug Faust / Jim Van Fleet)

[[Category:History]]
[[Category:Websites]]
[[Category:Fan sites]]
"""
    gpn = r"""'''GamePlayers Network''' (gameplayersnetwork.com) was a fan-run gaming site that, in Warren Holland's 25 January 2002 Players' Committee announcement, offered web-team help getting information to decipher.com, tools for email / boards / chat, and prize-support shipping for sanctioned SWCCG, Young Jedi, and Jedi Knights tournaments after 30 April 2002.

The [[Players Committee]] later listed GPN with [[DeckTech]] among the sites the PC forums overtook as the main community hub.

== See also ==

* [[History of the Players Committee]] · [[DeckTech]] · [[Squadron Members]]

== Sources ==

* [https://web.archive.org/web/20160117001353/http://decipher.ruddog.com/starwars/playerscommittee1.html The Star Wars Players' Committee], Warren Holland, 25 January 2002
* [https://www.starwarsccg.org/community-network/ Community Network], starwarsccg.org

[[Category:History]]
[[Category:Websites]]
[[Category:Fan sites]]
"""
    cat_people = "This category lists '''people''' in SWCCG history (Decipher staff, squadron members, and other sourced names).\n\n[[Category:History]]\n"
    cat_sm = "Decipher-era volunteer '''Squadron Members''' and the roster article.\n\n[[Category:People]]\n[[Category:History]]\n[[Category:Decipher]]\n"
    cat_sites = "Preserved SWCCG '''websites''' (official, PC, and fan).\n\n[[Category:History]]\n"
    cat_fan = "Fan sites documenting SWCCG.\n\n[[Category:Websites]]\n[[Category:History]]\n"
    return {
        "Corellian Engineering Corporation (fan site)": cec,
        "Anagramed Decipherians": ana,
        "Radio Free Decipher": rfd,
        "DeckTech": decktech,
        "GamePlayers Network": gpn,
        "Category:People": cat_people,
        "Category:Squadron Members": cat_sm,
        "Category:Websites": cat_sites,
        "Category:Fan sites": cat_fan,
    }


def update_anagrams(text: str) -> str:
    repl = [
        ("Chuck Kallenbach's dog", "[[Chuck Kallenbach]]'s dog"),
        ("| Jonathan Quesenberry\n| Red Leader", "| [[Jonathan Quesenberry]]\n| Red Leader"),
        ("| Rob Burns\n| artist", "| [[Rob Burns]]\n| artist"),
        ("| Michael Girard\n| Gold 120", "| [[Michael Girard]]\n| Gold 120"),
        ("| Sandy Wible\n| game designer", "| [[Sandy Wible]]\n| game designer"),
        ("| Jason Winter\n| former Decipher staff", "| [[Jason Winter]]\n| former Decipher staff"),
        ("| Cheryl Kallenbach", "| [[Cheryl Kallenbach]]"),
        ("| John Sarnecki\n| Gold 7", "| [[John Sarnecki]]\n| Gold 7"),
        ("| Jerry Darcy's cat", "| [[Jerry Darcy]]'s cat"),
        ("| Rollie Tesh\n| game creator", "| [[Rollie Tesh]]\n| game creator"),
        ("| Kyle Heuer\n| Rogue Leader", "| [[Kyle Heuer]]\n| Rogue Leader"),
        ("| Maarten Logge", "| [[Maarten Logge]]"),
        ("| Mark Schaffer\n| Gold 41", "| [[Mark Schaffer]]\n| Gold 41"),
        ("| Bob / Will Madison\n| Decipher staff", "| [[Bob Madison|Bob / Will Madison]]\n| Decipher staff"),
        ("| Becky Higgerson\n| Decipher staff", "| [[Becky Higgerson]]\n| Decipher staff"),
        ("| Claudia Darcy\n| Jerry Darcy's wife", "| [[Claudia Darcy]]\n| [[Jerry Darcy]]'s wife"),
        ("| Leslie Burns\n| Decipher staff", "| [[Leslie Burns]]\n| Decipher staff"),
        ("| Stacy Mollema\n| Lucasfilm licensing", "| [[Stacy Mollema]]\n| Lucasfilm licensing"),
        ("| Tom Lischke\n| game designer", "| [[Tom Lischke]]\n| game designer"),
        ("| Bill Martinson\n| Decipher staff", "| [[Bill Martinson]]\n| Decipher staff"),
        ("| Eric Olsen\n| Bravo 7", "| [[Eric Olson|Eric Olsen]]\n| Bravo 7"),
        ("| Tim Courtney\n| Red 37", "| [[Tim Courtney]]\n| Red 37"),
        ("| Braunlich\n| game creator", "| [[Tom Braunlich|Braunlich]]\n| game creator"),
        ("| Sandy Wible\n| game designer", "| [[Sandy Wible]]\n| game designer"),
        ("| Joseph Alread\n| Gold 79", "| [[Joe Alread|Joseph Alread]]\n| Gold 79"),
        ("| Keith Skipton (uncertain)\n| Decipher staff", "| [[Keith Skipton]] (uncertain)\n| Decipher staff"),
        ("| Curtiss Murphy\n|", "| [[Curtiss Murphy]]\n|"),
        ("| Kendrick Summers\n| Gold Leader", "| [[Kendrick Summers]]\n| Gold Leader"),
        ("| Jerry Darcy\n| game designer", "| [[Jerry Darcy]]\n| game designer"),
        ("| Jerry Darcy (extra R)\n| game designer", "| [[Jerry Darcy]] (extra R)\n| game designer"),
        ("| Warren Holland\n| Decipher CEO", "| [[Warren Holland]]\n| Decipher CEO"),
        ("| Carol Wisely\n| Decipher staff", "| [[Carol Wisely]]\n| Decipher staff"),
        ("| Justin Pakes\n| Decipher staff (Australia)", "| [[Justin Pakes]]\n| Decipher staff (Australia)"),
        ("| Kevin Reitzel\n| Bravo Leader", "| [[Kevin Reitzel]]\n| Bravo Leader"),
        ("| Mark McKay\n| Mark Tuttle's radio name", "| Mark McKay\n| [[Mark Tuttle]]'s radio name"),
        ("| Mike Gray\n| Decipher staff", "| [[Mike Gray]]\n| Decipher staff"),
    ]
    for a, b in repl:
        text = text.replace(a, b)
    if "[[Squadron Members]]" not in text:
        text = text.replace(
            "== See also ==\n* [[Easter eggs]]\n* [[Creators of SWCCG]]",
            "== See also ==\n* [[Easter eggs]]\n* [[Squadron Members]]\n* [[Anagramed Decipherians]]\n* [[Creators of SWCCG]]\n* [[Corellian Engineering Corporation (fan site)]]\n* [[Radio Free Decipher]]",
        )
    return text


def main() -> None:
    rows = load_roster()
    by_name: dict[str, list] = defaultdict(list)
    for r in rows:
        by_name[r["name"]].append(r)

    PEOPLE_DIR.mkdir(parents=True, exist_ok=True)
    titles = []

    for name, recs in sorted(by_name.items(), key=lambda x: x[0].lower()):
        if name in SKIP_WRITE:
            continue
        body = stub_for_person(name, recs)
        p = write_page(name, body, PEOPLE_DIR)
        titles.append(name)
        print("person", p.name)

    extra_names = {e[0] for e in EXTRA_PEOPLE}
    for name, lead, paras, srcs, c in EXTRA_PEOPLE:
        if name in SKIP_WRITE:
            continue
        recs = by_name.get(name, [])
        body = stub_for_person(name, recs, extra_lead=lead, extra_paras=paras, extra_sources=srcs, extra_cats=c)
        p = write_page(name, body, PEOPLE_DIR)
        if name not in titles:
            titles.append(name)
        print("extra", p.name)

    # redirects
    redirects = {
        "Jonathon Quesenberry": "Jonathan Quesenberry",
        "Joseph Alread": "Joe Alread",
        "Juz Pakes": "Justin Pakes",
        "Will Wible": "Sandy Wible",
        "Eric Olsen": "Eric Olson",
        "Joel An=rendain": "Joel Arendain",
        "Mithc Velasco": "Mitch Velasco",
        "plarathas": "Corellian Engineering Corporation (fan site)",
        "GeoCities plarathas": "Corellian Engineering Corporation (fan site)",
        "Anagramed Decipherians (GeoCities)": "Anagramed Decipherians",
    }
    for src, dest in redirects.items():
        if src == dest:
            continue
        write_page(src, f"#REDIRECT [[{dest}]]\n", PEOPLE_DIR)
        titles.append(src)

    write_page("Squadron Members", hub(rows), PAGES)
    for title, body in site_pages().items():
        write_page(title, body, PAGES)

    ana_path = PAGES / "Anagrams.wiki"
    ana = ana_path.read_text(encoding="utf-8")
    ana_path.write_text(update_anagrams(ana).replace("\r\n", "\n"), encoding="utf-8")

    manifest = PEOPLE_DIR / "_manifest.txt"
    manifest.write_text("\n".join(titles) + "\n", encoding="utf-8")
    print("people", len(titles), "roster", len(rows), "unique", len(by_name))


if __name__ == "__main__":
    main()
