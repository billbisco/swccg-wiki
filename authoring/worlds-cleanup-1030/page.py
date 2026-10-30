import json, re
rows = json.load(open("rows.json"))
PH = {2003:"Jonny Chu 2016 Endor Grand Prix.jpg",2007:"Jonny Chu 2016 Endor Grand Prix.jpg",2008:"Kevin Shannon 2013 Hall of Fame.jpg",
      2009:"Brian Hunter FreedomCon 2001.jpg",2012:"Emil Wallin 2015 Hall of Fame.jpg",2014:"Emil Wallin 2015 Hall of Fame.jpg",
      2015:"Justin Desai 2013 Hall of Fame.jpg",2016:"Tom Haid 2021 World Championship.jpg",2018:"Bastian Winkelhaus 2019 Hall of Fame.jpg"}
DATES = {2005:"2005 (days not confirmed)", 2020:"5–13 December 2020"}
PLAY = {1996:"38", 2000:"70 (Day 2)", 2020:"97", 2017:"59", 1998:"56"}
def era(y): return "Decipher" if y<=2001 else "Players Committee"
out = []
for r in rows:
    y = r["year"]
    img = r["img"] or PH.get(y, "")
    cap = ""
    if img and str(y) not in img: cap = "<br/><small>(" + re.sub(r"\.\w+$", "", img).split(" ", 2)[-1] + ")</small>"
    photo = f"[[File:{img}|80px]]{cap}" if img else "—"
    dates = DATES.get(y, r["dates"].split(" (")[0].split(";")[0])
    venue = r["venue"].replace(" (as named in the wrap-up)", "")
    players = PLAY.get(y, r["players"]) or "—"
    decks = f"{r['dark']}<br/>{r['light']}" if r["dark"] != "—" or r["light"] != "—" else "—"
    if y == 2006: decks = "—"
    out.append(f'|-\n| [[{r["hub"]}|{y}]] || {photo} || {r["champ"]} || {r["ru"]} || {venue} || {dates} || {players} || {r["fmt"]} || {decks}')
table = "\n".join(out)
from collections import Counter
c = Counter(r["champ"] for r in rows)
multi = [(n, [str(r["year"]) for r in rows if r["champ"] == n]) for n, k in c.most_common() if k > 1]
multi.sort(key=lambda x: (-len(x[1]), x[1][0]))
mt = "\n".join(f"|-\n| {n} || {len(ys)} || {', '.join(ys)}" for n, ys in multi)
page = f"""'''World Championships''' are the annual Star Wars CCG World Championship tournaments: run by [[Decipher]] from 1996 to 2000, by [[DeckTech]] at [[FreedomCon]] in 2001 (counted by the [[Players Committee]] as that year's championship), and by the Players Committee since 2002. The 2026 event was the 31st. Each year has a hub page with the full results, the published decklists in finish order, side events and photographs; the facts in the table below are sourced on those hubs.

How the circuit was run (Swiss, ratings, decklist sheets): [[Tournaments]]. Every event by year: [[List of SWCCG tournaments]]. Other title events: [[European Championships]]. Inductees and annual awards: [[Hall of Fame]].

== Champions ==

Winning decks are the champion's final-day decks (Dark above Light) where a list was published.

{{| class="wikitable sortable" style="font-size:95%;"
|-
! Year !! class="unsortable" | Champion photo !! Champion<ref name="awards">[https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20230817222457/https://www.starwarsccg.org/community/awards/ Internet Archive, 17 August 2023]</ref> !! Runner-up !! Site !! Dates !! Players !! Format !! class="unsortable" | Winning decks
{table}
|}}

A photo captioned with another event is the champion at that event; no photograph of the champion is on the wiki for the years marked "—".

== Multiple champions ==

{{| class="wikitable sortable"
! Player !! Titles !! Years
{mt}
|}}

== Eras and formats ==

* '''[[Decipher era]] (1996–2001):''' Decipher's official World Championships to 2000 and the DeckTech-run 2001 event, each played with the newest expansion legal ([[Premiere - A New Hope]] through [[Premiere - Reflections III]]). The 1999, 2000 and 2002 events were part of Decipher's conventions ([[DecipherCon 1999]], [[DecipherCon 2000]], [[DecipherCon 2002]]); 2001 was at [[FreedomCon]].
* '''[[Virtual Original]] (2002–2008):''' the Players Committee took over organized play and added virtual sets; each Worlds used the virtual pool of its day ([[Premiere - Original VS3]] to [[Premiere - Original VS16]]).
* '''[[Virtual Legacy]] (2009–2014):''' the Virtual Block pools. Worlds used the pool legal on its date, from [[Premiere - Virtual Block 6.1]] (2009) to [[Premiere - Virtual Block 9.1]] (2014). The fixed post-reset version of this card pool is [[Legacy Open]].
* '''[[Virtual Modern]] (2015–):''' after the 2014 reset, Worlds has been played in [[Open]].

Published 60s: [[Decklists]]. Playtest and travel groups: [[Star Wars CCG teams]].

== See also ==

* [[2026 World Championship]] (latest)
* [[Hall of Fame]]
* [[European Championships]]
* [[Formats]]
* [[List of SWCCG tournaments]]
* [[Tournaments]]

{{{{Eras}}}}

== References ==
<references />

[[Category:Championships]]
[[Category:World Championships]]
"""
open("World_Championships.wiki", "w", encoding="utf-8").write(page)
print(page[:600]); print(mt)
