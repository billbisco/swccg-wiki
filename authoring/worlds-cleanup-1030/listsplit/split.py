import json, re
L = open("live2.wiki", encoding="utf-8").read()
lines = L.split("\n")
a = lines.index("== Decipher-era regionals and opens ==")
b = lines.index("== Decipher World Championships ==")
c = lines.index("== See also ==")
block = "\n".join(lines[a:b])
rows = re.findall(r"^\| (.*)$", block, re.M)
rows = [r for r in rows if "||" in r]
W = {r["year"]: r for r in json.load(open("../champ/wc/rows.json"))}
TAG = {1996: "1996-12", 1997: "1997-12", 1998: "1998-11", 1999: "1999-11", 2000: "2000-10", 2001: "2001-11"}
SITE = {}
for l in lines[b:c]:
    m = re.match(r"\| (\d{4}) \|\| .*? \|\| (.*?) \|\| ", l)
    if m: SITE[int(m.group(1))] = m.group(2)
by, undated = {}, []
for r in rows:
    tag = r.split("||")[0].strip()
    (by.setdefault(tag[:4], []) if tag else undated).append(r)
pages = {}
for y in range(1996, 2002):
    w = W[y]
    wrow = f"{TAG[y]} || [[{w['hub']}|World Championship]] || {w['dates'].split(' (')[0].split(';')[0]} || {SITE[y]} || {w['fmt'].split(' (')[0]} || {w['champ']}"
    rs = [wrow] + by.get(str(y), [])
    rs.sort(key=lambda r: r.split("||")[0].strip(), reverse=True)  # stable: newest month first, original order within month
    body = "\n".join(f"|-\n| {r}" for r in rs)
    pages[y] = f"""Star Wars CCG tournaments of {y} that this wiki has sourced, newest first. The year's World Championship is [[{w['hub']}]] (champion {w['champ']}, runner-up {w['ru']}); every year's Worlds is on [[World Championships]]. Other years: [[List of SWCCG tournaments]].

Most rows come from the published constructed 60s in Decipher Deck Designs and other period sources that name a tournament; each event page cites its source. '''Format''' is the constructed pool named for that event.

{{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Format !! Winner
{body}
|}}

== See also ==

* [[List of SWCCG tournaments]] (all years)
* [[World Championships]]
* [[Decipher era]]
* [[Decklists]]
* [[Tournaments]]

[[Category:Tournaments]]
[[Category:{y}]]
"""
    print(y, len(rs))
# main list
nav = "'''Decipher era (1996–2001):''' " + " · ".join(f"[[List of SWCCG tournaments in {y}|{y}]]" for y in range(1996, 2002))
und = "\n".join(f"|-\n| {r}" for r in undated)
dec = f"""== 1996–2001 (Decipher era) ==

The {len(rows) + 6} sourced tournaments of the Decipher era, including the six Decipher-period World Championships, are on one page per year:

* [[List of SWCCG tournaments in 2001|2001]] ({len(by.get('2001', [])) + 1} events)
* [[List of SWCCG tournaments in 2000|2000]] ({len(by.get('2000', [])) + 1} events)
* [[List of SWCCG tournaments in 1999|1999]] ({len(by.get('1999', [])) + 1} events)
* [[List of SWCCG tournaments in 1998|1998]] ({len(by.get('1998', [])) + 1} events)
* [[List of SWCCG tournaments in 1997|1997]] ({len(by.get('1997', [])) + 1} events)
* [[List of SWCCG tournaments in 1996|1996]] ({len(by.get('1996', [])) + 1} events)

=== Undated ===

Decipher-era events whose date the source does not give.

{{| class="wikitable sortable"
! Tag !! Event !! Dates !! Site !! Format !! Winner
{und}
|}}
"""
head = "\n".join(lines[:a])
head = head.replace("Worlds hubs start at [[Championships]].", "Every World Championship, with champions, sites and winning decks: [[World Championships]].")
head = head.replace("then earlier years.", "then earlier years. Years 1996–2001 are on their own pages (see [[#1996–2001 (Decipher era)|below]]).")
tail = "\n".join(lines[c:]).replace("* [[Championships]]\n", "* [[World Championships]]\n* [[Hall of Fame]]\n")
for y in range(1996, 2002):
    tail = tail.replace(f"[[Category:{y}]]\n", "")
main = head + "\n" + dec + "\n" + tail
open("out_main.wiki", "w", encoding="utf-8").write(main)
for y, t in pages.items(): open(f"out_{y}.wiki", "w", encoding="utf-8").write(t)
print("main", len(main), "undated", len(undated), "total rows", len(rows))
print(head[:900])
