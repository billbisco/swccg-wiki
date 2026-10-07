#!/usr/bin/env python3
"""Canonical full-name dests for 2022–2024 last-name hub cells; 2023 GEMPC stages."""
from __future__ import annotations

import re
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"

GLOBAL = {
    "Birgander": "Pär Birgander",
    "Gabor": "Gabor Szegedi",
    "George": "Eric George",
    "Petersson": "Tony Petersson",
    "Póra": "György Póra",
    "Tegeler": "Marvin Tegeler",
    "Wauters": "Jeroen Wauters",
    "Winkelhaus": "Bastian Winkelhaus",
    "OlsonJ": "Joe Olson",
    "Olson S": "Sam Olson",
    "OlsonS": "Sam Olson",
    "Bolletino": "Andrew Bollentino",
    "ChuB": "Benji Chu",
    "ChuJ": "Jonny Chu",
    "d'Amboise": "Mike d'Amboise",
    "d’Amboise": "Mike d'Amboise",
    "HunterE": "Eric Hunter",
    "HunterH": "Hayes Hunter",
    "KellyC": "Chris Kelly",
    "Lauer": "Cory Lauer",
    "Napolitano": "Jared Napolitano",
    "Sammartano": "Isaak Sammartano",
    "Sarachan": "Tom Sarachan",
    "ScottM": "Matt Scott",
    "ScottR": "Randy Scott",
    "WestergardC": "Chris Westergard",
    "Butterworth": "Ben Butterworth",
    "Groth": "Aaron Groth",
    "Morris": "Travis Morris",
    "Partridge": "Trevor Partridge",
    "DiPaolo": "Jeremy DiPaolo",
    "Herold": "Ben Herold",
    "Lichtenstein": "Drew Lichtenstein",
    "LaPorta": "Joe Laporta",
    "LutzL": "Leif Lutz",
    "LutzM": "Matt Lutz",
    "Murray": "Jonathan Murray",
    "PittmanB": "Bill Pittman",
    "PittmanJ": "Joel Pittman",
    "Sesnick": "Steve Sesnick",
    "Davis": "Nate Davis",
    "Frede": "Aaron Frede",
    "Jackson": "Derek Jackson",
    "JGosiaco": "Jordan Gosiaco",
    "SGosiaco": "Spencer Gosiaco",
    "TGosiaco": "Taylor Gosiaco",
    "Kahler": "Aaron Kahler",
    "Atkin": "Clayton Atkin",
    "Bacheler": "Bill Bacheler",
    "Chien": "Edward Chien",
    "Herren": "Charlie Herren",
    "Miller": "Sean Miller",
    "Nelson": "Jake Nelson",
    "Rossi": "Vincent Rossi",
    "Yaeger": "Steve Yaeger",
    "Luhks": "Sean Luhks",
    "Carr": "John Carr",
    "Drentlaw": "Dan Drentlaw",
    "Usnats23": "Bill Kafer",
    "Marlin": "Tom Marlin",
    "Scinocca": "Will Scinocca",
    "Tarbox": "Will Tarbox",
    "Jimboyle": "Jim Boyle",
    "Christiana": "CJ Christiana",
    "Gardner": "Jeremy Gardner",
    "Haid": "Tom Haid",
    "Kristiansen": "Magnus Kristiansen",
    "Louderback": "Nate Louderback",
    "Bailey": "Brett Bailey",
    "Boyd": "Bentley Boyd",
    "CarulliJ": "Justin Carulli",
    "CarulliM": "Matt Carulli",
    "Dixon": "Chad Dixon",
    "Fuentes": "Al Fuentes",
    "Hedlund": "Ben Hedlund",
    "Hull": "Chris Hull",
    "Wexstten": "Andy Wexstten",
    "Edwards": "Lee Edwards",
    "Pistone": "Mike Pistone",
    "Tarin Vegas": "Miguel Tarin Vegas",
    "Le": "Thang Le",
    "Freeman": "Max Freeman",
    "Fulner": "Stephen Fulner",
    "Schellberg": "Adam Schellberg",
    "Yoo": "Stewart Yoo",
}

PER_HUB = {
    "2024_Supreme_Southern_Showdown.wiki": {"Cooper": "Travis Cooper"},
    "2023_U.S._National_Championship.wiki": {"Cooper": "Joel Cooper", "Joe": "Joe Olson"},
    "2023_Outrider_Cup_III.wiki": {"Hayes": "Hayes Hunter"},
    "2024_World_Championship.wiki": {"Smolarek": "Julian Smolarek"},
}

HUBS = [
    p.name
    for p in PAGES.glob("202[2-5]_*.wiki")
    if p.name
    in {
        "2025_Online_Championship_Series_Playoffs.wiki",
        "2025_World_Championship.wiki",
        "2025_European_Championship.wiki",
        "2025_U.S._National_Championship.wiki",
        "2025_Online_Retro_Event_for_Charity.wiki",
        "2025_Ninth_Annual_GEMPC.wiki",
        "2025_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki",
        "2025_Regional_Championships.wiki",
        "2025_Morristown_Melee.wiki",
        "2025_Las_Vegas_Grand_Prix.wiki",
        "2024_Champions_League.wiki",
        "2024_Retro_Online_Championship_Series_Playoffs.wiki",
        "2024_Online_Championship_Series_Playoffs.wiki",
        "2024_World_Championship.wiki",
        "2024_North_American_Continental_Championship.wiki",
        "2024_Online_Retro_Event_for_Charity.wiki",
        "2024_European_Championship.wiki",
        "2024_Eighth_Annual_GEMPC.wiki",
        "2024_Eclipse_Major.wiki",
        "2024_Jawa_Cup.wiki",
        "2024_Regional_Championships.wiki",
        "2024_Supreme_Southern_Showdown.wiki",
        "2023_Outrider_Cup_III.wiki",
        "2023_Online_Championship_Series_Playoffs.wiki",
        "2023_Endor_Grand_Prix.wiki",
        "2023_European_Championship.wiki",
        "2023_World_Championship.wiki",
        "2023_Online_Retro_Event.wiki",
        "2023_Seventh_Annual_GEMPC.wiki",
        "2023_U.S._National_Championship.wiki",
        "2023_Regional_Championships.wiki",
        "2023_San_Diego_Super_Open.wiki",
        "2023_Champions_League.wiki",
        "2022_Online_Championship_Series_Playoffs.wiki",
        "2022_World_Championship.wiki",
        "2022_European_Championship.wiki",
        "2022_U.S._National_Championship.wiki",
        "2022_Regional_Championships.wiki",
        "2022_Decipher_Cards_Only_Retro_Event.wiki",
        "2022_PC20_Tournament.wiki",
        "2022_Endor_Grand_Prix.wiki",
        "2022_Sixth_Annual_GEMPC.wiki",
        "2022_Jawa_Cup.wiki",
        "2022_Match_Play_Championship.wiki",
    }
]

changed: list[tuple[str, str]] = []


def stub_path(name: str) -> Path:
    return STUBS / (name.replace(" ", "_") + ".wiki")


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = text.replace("\r\n", "\n")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")


def is_redirect(path: Path) -> bool:
    return path.exists() and path.read_text(encoding="utf-8").lstrip().startswith("#REDIRECT")


def extract_rows(text: str) -> list[str]:
    m = re.search(r"== Tournament Results ==.*?\{\|.*?\|-(.*)\|\}", text, re.S)
    if not m:
        return []
    body = m.group(1)
    rows = []
    for chunk in re.split(r"\n\|-\s*\n", body):
        chunk = chunk.strip()
        if chunk.startswith("!"):
            continue
        if not chunk:
            continue
        if not chunk.startswith("|-"):
            chunk = "|- \n" + chunk
        rows.append(chunk if chunk.endswith("\n") else chunk)
    return rows


def insert_rows(text: str, rows: list[str]) -> str:
    if not rows or "|}" not in text:
        return text
    existing = text
    add = []
    for row in rows:
        key = re.search(r"\[\[([^\]|#]+)", row)
        if key and key.group(1) in existing and row.split("||", 1)[-1][:40] in existing:
            continue
        add.append(row if row.endswith("\n") else row + "\n")
    if not add:
        return text
    return text.replace("|}\n", "\n".join(add) + "\n|}\n", 1)


NEW_STUB = """'''{name}''' played Players Committee constructed events.

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
{rows}
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[Championships]]

== Sources ==

* [https://www.starwarsccg.org/category/tournament-decklists/ Tournament Decklists Archives], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
"""


def ensure_dest(full: str, last: str | None):
    dest = stub_path(full)
    src = stub_path(last) if last else None
    if dest.exists() and not is_redirect(dest):
        text = dest.read_text(encoding="utf-8")
        if src and src.exists() and not is_redirect(src):
            text = insert_rows(text, extract_rows(src.read_text(encoding="utf-8")))
        if f"[[Category:" in text and "[[Category:Players]]" in text:
            pass
        write(dest, text)
        changed.append((full, f"pages/player-stubs/{dest.name}"))
        print("MERGE", full)
        return
    if dest.exists() and is_redirect(dest) and full == "Bill Kafer":
        pass  # rebuild later
    elif dest.exists() and is_redirect(dest):
        print("KEEP-REDIR", full)
        return
    if src and src.exists() and not is_redirect(src):
        text = src.read_text(encoding="utf-8")
        text = text.replace(f"'''{last}'''", f"'''{full}'''", 1)
        write(dest, text)
        changed.append((full, f"pages/player-stubs/{dest.name}"))
        print("FROM-LAST", last, "->", full)
        return
    write(dest, NEW_STUB.format(name=full, rows=""))
    changed.append((full, f"pages/player-stubs/{dest.name}"))
    print("BLANK", full)


def redir(src: str, dest: str):
    if src == dest:
        return
    p = stub_path(src)
    write(p, f"#REDIRECT [[{dest}]]\n")
    changed.append((src, f"pages/player-stubs/{p.name}"))
    print("REDIR", src, "->", dest)


def replace_cell(text: str, old: str, new: str) -> str:
    return re.sub(r"\[\[" + re.escape(old) + r"\]\]", f"[[{new}]]", text)


# --- hub player-cell patches ---
for fname in sorted(set(HUBS)):
    path = PAGES / fname
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    orig = text
    for old, new in PER_HUB.get(fname, {}).items():
        text = replace_cell(text, old, new)
    # longest keys first so Olson S beats Olson
    for old, new in sorted(GLOBAL.items(), key=lambda kv: -len(kv[0])):
        text = replace_cell(text, old, new)
    if fname == "2023_U.S._National_Championship.wiki":
        text = text.replace(
            "| 18 || [[Bill Kafer]] || [[2023 US Nationals Usnats23 DS Kafer TTO|Endor Operations]] || —",
            "| 18 || [[Bill Kafer]] || [[2023 US Nationals Usnats23 DS Kafer TTO|Endor Operations]] || [[2023 US Nationals Bill Kafer LS ObiWanCom|Communing]]",
        )
        text = re.sub(
            r"\n\|-\n\| 31 \|\| \[\[Bill Kafer\]\] \|\| — \|\| \[\[2023 US Nationals Bill Kafer LS ObiWanCom\|Communing\]\]\n",
            "\n",
            text,
        )
    if text != orig:
        write(path, text)
        title = fname[:-5].replace("_", " ")
        changed.append((title, f"pages/{fname}"))
        print("HUB", fname)

# --- 2023 GEMPC stages ---
GEMPC23 = """'''2023 Seventh Annual GEMPC''' (GEMPC7) was the Players Committee online match-play championship on GEMP, January–April 2023. [[Tom Strother]] defeated [[Mike Kessling]] in the Final Confrontation.<ref name="pc">https://www.starwarsccg.org/2023-05-gempc7-match-play-tournament-jan-april-2023/</ref>

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' GEMP
* '''Dates:''' January–April 2023
* '''GEMP importable decks:''' [https://forum.starwarsccg.org/viewtopic.php?p=1404368 forum]

Players published a different pair in the quarterfinals, semifinals, and finals.

== Finals ==

{| class="wikitable sortable"
! Finish !! Player !! Dark !! Light
|-
| 1 || [[Tom Strother]] || [[2023 GEMPC Top 8 Tom Strother DS Troopers|Slip Sliding Away (V)]] || [[2023 GEMPC Top 8 Tom Strother LS HB|Hidden Base]]
|-
| 2 || [[Mike Kessling]] || [[2023 GEMPC Top 8 Mike Kessling DS HD|Hunt Down And Destroy The Jedi]] || [[2023 GEMPC Top 8 Mike Kessling LS OA|Old Allies]]
|}

== Semifinals ==

{| class="wikitable sortable"
! Player !! Dark !! Light
|-
| [[Tom Strother]] || [[2023 GEMPC Semifinals Tom Strother DS SSav9s|Slip Sliding Away (V)]] || [[2023 GEMPC Semifinals Tom Strother LS ZH|Zero Hour]]
|-
| [[Anthony Howard]] || [[2023 GEMPC Semifinals Anthony Howard DS Senate|My Lord, Is That Legal?]] || [[2023 GEMPC Semifinals Anthony Howard LS Y4O|Yavin 4 Base Operations]]
|-
| [[Mike Kessling]] || [[2023 GEMPC Semifinals Mike Kessling DS Invasion|Invasion]] || [[2023 GEMPC Semifinals Mike Kessling LS OA|Old Allies]]
|-
| [[Quirin Fürgut]] || [[2023 GEMPC Semifinals Quirin Fürgut DS ROpsv|Moment Of Triumph (V)]] || [[2023 GEMPC Semifinals Quirin Fürgut DS TIGIH|There Is Good In Him]]
|}

== Quarterfinals ==

{| class="wikitable sortable"
! Player !! Dark !! Light
|-
| [[Tom Strother]] || [[2023 GEMPC Quarterfinals Tom Strother DS SSAv9s|Slip Sliding Away (V)]] || [[2023 GEMPC Quarterfinals Tom Strother LS LTWWvMains|Let The Wookiee Win (V)]]
|-
| [[Charlie Arlandson]] || [[2023 GEMPC Quarterfinals Charlie Arlandson DS Invasion|Invasion]] || [[2023 GEMPC Quarterfinals Charlie Arlandson LS No Idea|They Have No Idea We're Coming]]
|-
| [[Anthony Howard]] || [[2023 GEMPC Quarterfinals Anthony Howard DS ROpsv|Moment Of Triumph (V)]] || [[2023 GEMPC Quarterfinals Anthony Howard LS YodaComm|Communing]]
|-
| [[Conor Britain]] || [[2023 GEMPC Quarterfinals Conor Britain DS HDv|Hunt Down And Destroy The Jedi (V)]] || [[2023 GEMPC Quarterfinals Conor Britain LS ObiComm|Communing]]
|-
| [[Quirin Fürgut]] || [[2023 GEMPC Quarterfinals Quirin Fürgut DS ROpsv|Moment Of Triumph (V)]] || [[2023 GEMPC Quarterfinals Quirin Fürgut LS ObiComm|Communing]]
|-
| [[Joe Olson]] || [[2023 GEMPC Quarterfinals Joe Olson DS Thrawn|A Great Tactician Creates Plans]] || [[2023 GEMPC Quarterfinals Joe Olson LS YodaComm|Communing]]
|-
| [[Mike Kessling]] || [[2023 GEMPC Quarterfinals Mike Kessling DS BHBM|Bring Him Before Me]] || [[2023 GEMPC Quarterfinals Mike Kessling LS HITCO|He Is The Chosen One]]
|-
| [[Greg Shaw]] || [[2023 GEMPC Quarterfinals Greg Shaw DS ROpsv|Moment Of Triumph (V)]] || [[2023 GEMPC Quarterfinals Greg Shaw LS ObiComm|Communing]]
|}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [https://www.starwarsccg.org/2023-05-gempc7-match-play-tournament-jan-april-2023/ PC results]

== Sources ==

* [https://www.starwarsccg.org/2023-05-gempc7-match-play-tournament-jan-april-2023/ 2023 Seventh Annual GEMPC], starwarsccg.org
* [https://forum.starwarsccg.org/viewtopic.php?p=1404368 GEMP Importable Decklists]

{{#if:1|<nowiki />
<h2>References</h2>
<references />}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2023]]
"""
write(PAGES / "2023_Seventh_Annual_GEMPC.wiki", GEMPC23)
changed.append(("2023 Seventh Annual GEMPC", "pages/2023_Seventh_Annual_GEMPC.wiki"))
print("HUB 2023 GEMPC stages")

# --- dest stubs ---
# extra dests whose last-name token is not the only source
EXTRA_COPY = {
    "Pär Birgander": "Par Birgander",
    "Ben Butterworth": "Ben Buttersworth",
}
for last, full in list(GLOBAL.items()) + list(
    {k: v for d in PER_HUB.values() for k, v in d.items()}.items()
):
    ensure_dest(full, last)

for full, last in EXTRA_COPY.items():
    ensure_dest(full, last)

# Par Birgander / Ben Buttersworth become redirects after dest exists
redir("Par Birgander", "Pär Birgander")
redir("Ben Buttersworth", "Ben Butterworth")
redir("Kafer 2022", "Bill Kafer")
redir("Tarin Vegas", "Miguel Tarin Vegas")

for last, full in GLOBAL.items():
    if last in ("Joe", "Cooper", "Hayes", "Smolarek"):
        continue
    src = stub_path(last)
    if src.exists():
        redir(last, full)

# disambiguation pages
write(
    stub_path("Cooper"),
    """'''Cooper''' may refer to:

* [[Joel Cooper]]
* [[Travis Cooper]]

[[Category:Players]]
""",
)
changed.append(("Cooper", "pages/player-stubs/Cooper.wiki"))
write(
    stub_path("Smolarek"),
    """'''Smolarek''' may refer to:

* [[Julian Smolarek]]
* [[Robert Smolarek]]

[[Category:Players]]
""",
)
changed.append(("Smolarek", "pages/player-stubs/Smolarek.wiki"))
write(
    stub_path("Joe"),
    """'''Joe''' may refer to:

* [[Joe Olson]]
* [[Joe Horbey]]
* [[Joe Phillips]]
* [[Joe Pinto]]
* [[Joe Laporta]]
* [[Joe Giannetti]]
* [[Joe Hosking]]

[[Category:Players]]
""",
)
changed.append(("Joe", "pages/player-stubs/Joe.wiki"))

# --- rebuild Bill Kafer from hubs ---
from generate_2025_missing_players import parse_cells, player_and_sides, split_sections  # noqa: E402

rows = []
seen = set()
for fname in sorted(PAGES.glob("202[2-6]_*.wiki")):
    if fname.name.count("_") > 6 and not fname.name.endswith(
        ("Championship.wiki", "GEMPC.wiki", "Playoffs.wiki", "Cup.wiki", "Event.wiki", "Showdown.wiki", "Major.wiki", "Melee.wiki", "Prix.wiki", "Open.wiki", "Tournament.wiki", "League.wiki")
    ):
        # skip most deck pages; still allow hubs
        pass
    text = fname.read_text(encoding="utf-8")
    if "[[Bill Kafer]]" not in text:
        continue
    hub = fname.stem.replace("_", " ")
    # only tournament hubs, not deck pages
    if re.match(r"^20\d\d .*(DS|LS) ", hub) or " DS " in hub or " LS " in hub:
        continue
    year = hub[:4]
    for heading, body in split_sections(text):
        if heading.startswith(("See also", "Sources", "Format", "References")):
            continue
        for block in re.split(r"\n\|-\n", body):
            cells = parse_cells(block)
            if len(cells) < 2:
                continue
            parsed = player_and_sides(cells)
            if not parsed:
                continue
            player, finish, dark, light = parsed
            if player != "Bill Kafer":
                continue
            key = (hub, heading, dark, light)
            if key in seen:
                continue
            seen.add(key)
            st = f" ({heading})" if heading not in ("Results", hub, "Decklists") else ""
            rows.append(
                f"|- \n| {year} || [[{hub}]]{st} || [[Open]] || {finish} || {dark} || {light}"
            )

kafer_body = f"""'''Bill Kafer''' played Players Committee constructed events.

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
{chr(10).join(rows)}
|}}

== See also ==

* [[List of SWCCG tournaments]]
* [[Championships]]

== Sources ==

* [https://www.starwarsccg.org/category/tournament-decklists/ Tournament Decklists Archives], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2022]]
[[Category:2023]]
[[Category:2024]]
[[Category:2025]]
"""
write(stub_path("Bill Kafer"), kafer_body)
changed.append(("Bill Kafer", "pages/player-stubs/Bill_Kafer.wiki"))
print("REBUILT Bill Kafer rows", len(rows))

# --- TSV + tar ---
# de-dupe keeping last write
uniq = {}
for t, rel in changed:
    uniq[t] = rel
rows_tsv = [f"{t}\t{rel}" for t, rel in uniq.items()]
tsv = ROOT / "y2022-canon-players.tsv"
tsv.write_text("\n".join(rows_tsv) + "\n", encoding="utf-8", newline="\n")
print("tsv", len(rows_tsv), tsv)

sh = ROOT / "apply-y2022-canon-players.sh"
sh.write_text(
    """#!/bin/bash
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
tar -xf /tmp/y2022-canon-players.tar
bash "$ROOT/apply-tsv.sh" "$ROOT/y2022-canon-players.tsv" "canonical player names 2022-2024 hubs and dest stubs"
echo "== extra purge =="
printf '%s\\n' \\
  "List of SWCCG tournaments" \\
  "Bill Kafer" \\
  "Pär Birgander" \\
  "Ben Butterworth" \\
  "2023 Seventh Annual GEMPC" \\
  "2023 U.S. National Championship" \\
  "2024 World Championship" \\
  "2024 Eclipse Major" \\
  "2024 Supreme Southern Showdown" \\
  "2022 PC20 Tournament" \\
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo CANON_PLAYERS_DONE
""",
    encoding="utf-8",
    newline="\n",
)

tar_path = ROOT / "y2022-canon-players.tar"
n = 0
with tarfile.open(tar_path, "w") as tar:
    tar.add(tsv, arcname=tsv.name)
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(sh, arcname=sh.name)
    n += 3
    for t, rel in uniq.items():
        p = ROOT / rel
        if not p.exists():
            print("MISSING", rel)
            continue
        tar.add(p, arcname=rel.replace("\\", "/"))
        n += 1
print("tar", tar_path, "files", n, "bytes", tar_path.stat().st_size)
