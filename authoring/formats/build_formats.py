#!/usr/bin/env python3
"""Build the [[Formats]] page, each format page's Tournaments table, and List of SWCCG tournaments Format fixes
from formats/registry.json (Bill 2026-10-24). Run fetch_events.py first (writes /tmp/claude-0/fmt/events.json).

  python3 build_formats.py BATCH     -> /tmp/claude-0/BATCHpkg + /mnt/user-data/outputs/BATCH-apply.tar
"""
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
R = json.loads((HERE / "registry.json").read_text(encoding="utf-8"))
BY = {r["title"]: r for r in R}
EV = json.load(open("/tmp/claude-0/fmt/events.json"))
API = "https://wiki.swccg.com/api.php"
START, END = "<!-- format-tournaments:start (generated from formats/registry.json; edit the event pages) -->", "<!-- format-tournaments:end -->"


def texts(titles):
    out = {}
    for i in range(0, len(titles), 50):
        q = dict(action="query", prop="revisions", rvprop="content", rvslots="main", titles="|".join(titles[i:i + 50]),
                 format="json", formatversion="2")
        r = json.load(urllib.request.urlopen(API, urllib.parse.urlencode(q).encode(), timeout=120))
        out.update({p["title"]: p["revisions"][0]["slots"]["main"]["content"] for p in r["query"]["pages"] if "revisions" in p})
    return out


ASSIGNED = {x["event"]: x["format"] for x in json.load(open(HERE / "drafts" / "event_formats.json")) if x.get("format")}


def hub_format(t):
    m = re.search(r"^\* '''(?:Format|Environment):'''([^\n]*)", t or "", re.M)
    if not m:
        return None
    for x in re.findall(r"\[\[([^\]|]+)", m.group(1)):
        if x.strip() in BY:
            return x.strip()
    return None


# ---------- List of SWCCG tournaments: one row per event, 6 cells, Format filled from the event page ----------
L = EV["list"]
rows_out, events = [], []
fixed5 = filled = 0
for row in L.split("\n|-\n"):
    lines = row.split("\n")
    i = next((k for k, l in enumerate(lines) if l.startswith("| ") and "||" in l), None)
    if i is None:
        rows_out.append(row)
        continue
    cells = [c.strip() for c in lines[i][2:].split("||")]
    orig = list(cells)
    m = re.match(r"\[\[([^\]|]+)", cells[1]) if len(cells) > 1 else None
    if m and len(cells) == 5:  # Tag, Event, Dates, Site, Winner: the Format cell is missing
        cells.insert(4, "")
        fixed5 += 1
    if m:
        ev = m.group(1).strip()
        f = hub_format(EV["hubs"].get(ev)) or ASSIGNED.get(ev)
        cur = re.match(r"\[\[([^\]|]+)", cells[4]) if len(cells) > 4 else None
        if f and len(cells) > 4 and not cells[4].strip():
            cells[4] = f"[[{f}]]"
            filled += 1
        fmt = f or (cur.group(1).strip() if cur and cur.group(1).strip() in BY else None)
        events.append((ev, fmt, cells))
        if cells != orig:
            lines[i] = "| " + " || ".join(cells)
    rows_out.append("\n".join(lines))
L_new = "\n|-\n".join(rows_out)

# ---------- tournaments per format ----------
per = {}
for ev, fmt, cells in events:
    if fmt:
        per.setdefault(fmt, []).append((cells[0], ev, cells[2], cells[3], cells[5] if len(cells) > 5 else ""))


def tournaments_section(title):
    xs = per.get(title, [])
    head = (f"== Tournaments ==\n{START}\n")
    if not xs:
        body = ("No tournament on [[List of SWCCG tournaments]] is recorded in this format yet. Events are added here "
                "when their page gives this format.\n")
    else:
        body = (f"{len(xs)} tournament{'s' if len(xs) != 1 else ''} on [[List of SWCCG tournaments]] used this format, newest first.\n\n"
                '{| class="wikitable sortable"\n|-\n! Tag !! Event !! Dates !! Site !! Winner\n'
                + "".join(f"|-\n| {t} || [[{e}]] || {d} || {s} || {w}\n" for t, e, d, s, w in xs) + "|}\n")
    return head + body + END + "\n"


# ---------- the Formats page ----------
FAM = {"decipher-pool": "Decipher card pool", "decipher-special": "Decipher format", "pc-championship": "PC championship",
       "pc-alternate": "PC alternate", "gemp": "GEMP", "wiki": "Wiki-named"}
Y = "✓"


def row(r):
    n = len(per.get(r["title"], []))
    return (f"|-\n| [[{r['title']}]] || {r['type']} || {FAM[r['family']]} || {r['pool']} || {r['years']} || "
            f"{Y if r['decipher'] else ''} || {Y if r['pc'] else ''} || {r['gemp_pc'] or ''} || {r['gemp_ours'] or ''} || "
            f"{'<code>' + r['code'] + '</code>' if r['code'] else ''} || {n or ''}")


def bullets(fam):
    return "\n".join(f"* [[{r['title']}]] — {r['pool']}" + (f" ({r['years']})" if r['years'] else "")
                     + (f"; also called {', '.join(r['also'])}" if r['also'] else "") for r in R if r["family"] == fam)


cur = texts(["Formats"])["Formats"]
refdefs = {m.group(1): m.group(0) for m in re.finditer(r'<ref name="([^"]+)">.*?</ref>', cur, re.S)}
def ref(n):
    return refdefs.get(n, f'<ref name="{n}" />')


old_gemp_diff = re.search(r"=== Differences from the Players Committee GEMP ===\n(.*?)\n(?===)", cur, re.S).group(1).strip()
old_rules = re.search(r"== Rules documents ==\n(.*?)\n(?===)", cur, re.S).group(1).strip()
old_see = re.search(r"== See also ==\n(.*?)\n\{\{Eras\}\}", cur, re.S).group(1).strip()
pools = [r for r in R if r["family"] == "decipher-pool"]

page = f"""'''Formats''' are the card pools and deck rules that Star Wars CCG games and tournaments are played under. This page lists every format the wiki documents, where each one comes from, and how many recorded tournaments used it. Each format has its own page with its card pool, history and tournaments.

== How to read this page ==

* '''Four sources.''' A format can come from [[Decipher]] (1995–2002), from the [[Players Committee]] (PC, 2002–), from the PC's [[GEMP]] server, or only from this wiki's own GEMP at [https://play.swccg.com/ play.swccg.com].{ref('play')} Many formats belong to more than one: the 2000 World Championship pool, [[Premiere - Death Star II]], is also a GEMP format on both servers.
* '''Historical card pools are named for what was legal.''' Decipher did not name its constructed pools: each new expansion simply became legal, and the Players Committee likewise points players to the latest pool. But the game played at the 1999 World Championship is not the game of 2001, so the wiki names each period's pool after the last set it contains: ''Premiere - X'' means every Decipher set from [[Premiere]] through X; ''Premiere - Original VSn'' adds the Players Committee's original Virtual Sets 1–n (2002–2009 slips), which are not the post-2014 ''Virtual Set n''. These names let a reader rebuild and replay a deck as it was legal at the time.
* '''Fixed formats keep their originator's name.''' A format whose definition never changed (a sealed product, a closed environment) uses Decipher's or the PC's own wording, with other names noted on its page: [[Death Star II Closed Environment]], [[First Anthology Sealed]].
* '''(Modified)''' means the same card pool with a ban list.

== All formats ==

Sort by any column. ''Decipher'' and ''PC'' mark who defined or ran the format; the GEMP columns give its name on each server; ''Tournaments'' counts the events on [[List of SWCCG tournaments]] whose page gives this format.

{{| class="wikitable sortable" style="font-size:90%"
|-
! Format !! Type !! Source !! Card pool !! Years !! Decipher !! PC !! PC GEMP name !! play.swccg.com name !! GEMP code !! Tournaments
{chr(10).join(row(r) for r in R)}
|}}

== Decipher era (1995–2002) ==

Era hub: [[Decipher era]]. Decipher's sanctioned constructed play used every printed set legal on the event day, so the pool grew with each expansion; its events were described as ''Constructed'' or ''Sealed Deck'' rather than by a named format.

=== Constructed card pools ===

{{| class="wikitable"
|-
! Format !! Card pool !! In use
{"".join(f"|-{chr(10)}| [[{r['title']}]] || {r['pool']} || {r['years']}{chr(10)}" for r in pools)}|}}

=== Decipher's special formats ===

{bullets("decipher-special")}

== Players Committee (2002–) ==

Era hubs: [[Virtual Original]], [[Virtual Legacy]], [[Virtual Modern]].{ref('pc-home')} From March 2002 championship constructed added the Players Committee's Virtual Sets to the Decipher pool. Each original Virtual Set cutoff is its own format; the 2009 reorganization led to [[Legacy Open]], and the 2014 Virtual Card Reset to today's [[Open]] (the PC's ''Standard'').

=== Championship constructed ===

{bullets("pc-championship")}

=== Alternate formats ===

The PC's ''Alternate Format Tournament Guide'' and its formats pages define these.{ref('afg')}

{bullets("pc-alternate")}

== GEMP ==

[[GEMP]] is the online client. Each GEMP format has a display name and a code; the table above gives both servers' names.{ref('gemp')}{ref('pc-gemp')}

=== Differences from the Players Committee GEMP ===
{old_gemp_diff}

== Formats only on play.swccg.com ==

{bullets("gemp")}

== Formats named by this wiki ==

{bullets("wiki")}

== Rules documents ==

{old_rules}

== See also ==

{old_see}

{{{{Eras}}}}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Rules]]
[[Category:Formats]]
"""


def main():
    batch = sys.argv[1]
    pk = Path(f"/tmp/claude-0/{batch}pkg")
    shutil.rmtree(pk, ignore_errors=True)
    (pk / "pages").mkdir(parents=True)
    rows = []

    def emit(t, x):
        fn = "pages/" + t.replace(" ", "_").replace("/", "%2F") + ".wiki"
        (pk / fn).write_text(x, encoding="utf-8")
        rows.append(f"{t}\t{fn}")

    emit("Formats", page)
    if L_new != L:
        emit("List of SWCCG tournaments", L_new)
    F = texts([r["title"] for r in R])
    D = HERE / "drafts"
    for r in R:
        dfile = D / (r["title"].replace(" ", "_") + ".wiki")
        t = dfile.read_text(encoding="utf-8") if dfile.exists() else F.get(r["title"])
        if t is None:
            print("MISSING page", r["title"])
            continue
        sec = tournaments_section(r["title"])
        if START in t:
            a = t.find("== Tournaments ==\n" + START)
            a = a if a >= 0 else t.find(START)
            b = t.find(END) + len(END) + 1
            new = t[:a] + sec + t[b:]
        else:
            k = min([i for i in (t.find("\n== See also =="), t.find("\n== References =="), t.find("\n{{#if:1"), t.find("\n[[Category:")) if i >= 0] or [len(t)])
            new = t[:k].rstrip("\n") + "\n\n" + sec + t[k:]
        if new != t:
            emit(r["title"], new)
    # the product page "Jabba's Palace Sealed Deck" carried the format's Tournaments block before the format got its own page
    prod = texts(["Jabba's Palace Sealed Deck"]).get("Jabba's Palace Sealed Deck", "")
    if START in prod:
        a = prod.find("== Tournaments ==\n" + START); b = prod.find(END) + len(END) + 1
        emit("Jabba's Palace Sealed Deck", prod[:a].rstrip("\n") + "\n\n" + prod[b:].lstrip("\n"))
    for line in open(D / "redirects.tsv", encoding="utf-8"):
        if "\t" in line:
            a, b = line.rstrip("\n").split("\t")
            emit(a, f"#REDIRECT [[{b}]]\n")
    (pk / f"y-{batch}.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    shutil.copy(HERE.parent / "wiki_api_apply.py", pk)
    (pk / "since.txt").write_text(dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") + "\n")
    subprocess.run(["tar", "cf", f"/mnt/user-data/outputs/{batch}-apply.tar", "-C", str(pk), "."], check=True)
    print(f"{len(rows)} pages; List rows fixed (missing Format cell) {fixed5}, Format filled from event pages {filled}; "
          f"events with a format {sum(len(v) for v in per.values())} of {len(events)}")


if __name__ == "__main__":
    main()
