from lib import *
y=2015
t=open(f'live_{y}.wiki').read()
defs=dict(COMMON); defs.update(refdefs(t)); defs['awards']=COMMON['awards']
defs['pc']='[https://www.starwarsccg.org/2015-world-championships/ 2015 World Championships], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261013125658/https://swccg.com/snapshots/pc/2015-world-championships.html Internet Archive]'
defs['crowned']='[https://www.starwarsccg.org/world-champion-crowned-in-philadelphia/ World Champion Crowned in Philadelphia], starwarsccg.org'
defs['olson2020']='[https://www.starwarsccg.org/joe-olson-wins-the-25th-star-wars-ccg-world-championship/ Joe Olson wins the 25th Star Wars CCG World Championship], starwarsccg.org (19 December 2020): Olson\'s Worlds Top 8 finishes include "2015-3rd".'
d3=table_rows(get(t,'Day 3'))
def res(p,n,extra=''): r=deckrow_by_player(d3,n,1); return [p,r[1]+extra,r[2],r[3]]
results=[res('1','Justin Desai'),res('2','Jonny Chu'),res('3','Joe Olson','<ref name="olson2020" />'),res('4','Matt Sokol','<ref name="awards" />'),
 res('5–8','Emil Wallin'),res('5–8','Matthew Harrison-Trainor'),res('5–8','Jan Westergard'),res('5–8','Mark Walseth')]
d2=get(t,'Day 2').replace('! Day 2 !! Player !! Dark !! Light','! Place !! Player !! Dark !! Light')
ib=infobox(y,None,None,'6–9 August 2015<ref name="pc" />','Philadelphia, Pennsylvania, USA<ref name="awards" />',
 '[[Open]]','61<ref name="pc" />','[[Justin Desai]]','[[Jonny Chu]]',2014,2016)
lead="""'''2015 World Championship''' was the 20th Star Wars CCG World Championship, run by the [[Players Committee]] in Philadelphia, Pennsylvania, on 6–9 August 2015.<ref name="pc" /><ref name="awards" /> The constructed format was [[Open]]. 61 players took part.<ref name="pc" /><ref name="wp" /> [[Justin Desai]] defeated [[Jonny Chu]] in the final, playing Combat Readiness (V) and Yavin 4: Massassi Throne Room on Day 3, for his second title after 2013.<ref name="crowned" /><ref name="awards" /> [[Scott Lingrell]], [[Chris Menzel]] and [[Emil Wallin]] were enshrined in the Players Committee Hall of Fame during the event.<ref name="awards" /> The Players Committee's wrap-up calls the Top 8 stage "Day 2" and the Swiss stage "Day 1"; this page follows the tournament-decklists naming (Day 3 = Top 8, Day 2 = Swiss).<ref name="pc" />"""
intro=("Places 1–2 are from the final.<ref name=\"crowned\" /> The PC decklist page lists [[Matt Sokol]] third and [[Joe Olson]] fourth,<ref name=\"pc\" /> but Olson's 2020 champion article gives him 3rd and Sokol's Hall of Fame biography gives him 4th, so the table follows those. "
 "The bracket was not published; the remaining quarterfinalists are shown as 5–8 in Swiss order. Decks are the Day 3 lists.")
side="""=== Hall of Fame ===

[[Scott Lingrell]], [[Chris Menzel]] and [[Emil Wallin]] were enshrined in the Players Committee Hall of Fame on 8 August 2015, during the World Championship.<ref name="awards" />"""
gallery=['File:Emil Wallin 2015 Hall of Fame.jpg|[[Emil Wallin]], Hall of Fame class of 2015',
 'File:Scott Lingrell 2015 Hall of Fame.jpg|[[Scott Lingrell]], Hall of Fame class of 2015',
 'File:Chris Menzel 2015 Hall of Fame.jpg|[[Chris Menzel]], Hall of Fame class of 2015',
 "File:Community card Emil W 2015 Hall of Fame.jpg|Community card ''Emil W'' (2015 Hall of Fame)",
 "File:Community card Scott L 2015 Hall of Fame.jpg|Community card ''Scott L'' (2015 Hall of Fame)",
 "File:Community card Chris M 2015 Hall of Fame.jpg|Community card ''Chris M'' (2015 Hall of Fame)"]
src=merge_sources(bullets(get(t,'Sources')),[SRC_AWARDS,SRC_WP,
 '* [https://www.starwarsccg.org/world-champion-crowned-in-philadelphia/ World Champion Crowned in Philadelphia], starwarsccg.org',
 "* [https://www.starwarsccg.org/joe-olson-wins-the-25th-star-wars-ccg-world-championship/ Joe Olson wins the 25th Star Wars CCG World Championship], starwarsccg.org (19 December 2020)"])
page=assemble(y,ib,lead,intro,results,None,[('Day 2',"Swiss standings as listed by the Players Committee.<ref name=\"pc\" />\n\n"+d2)],None,[],side,gallery,
 see(y,'Open',['[[2014 Virtual Card Pool Reset]]','[[Formats]]']),src)
notes="""# 2015 World Championship — draft notes

Draft: hubs_draft/2015_World_Championship.wiki (live hub unchanged since the local copy; re-fetched 30 Oct 2026).

## What changed
- Standard infobox (20th edition, PC, 6–9 Aug 2015, Philadelphia, [[Open]], 61 players, Desai def. Chu, 2014 · 2016). No champion photo for 2015 exists; image row omitted. The three 2015 HoF portraits and three HoF community cards go in `== Photographs ==` (previously unused on the hub).
- Runner-up Jonny Chu added (missing before).
- Lead: Desai's second title (2013, 2015); 2015 HoF class; wrap-up vs decklist day naming kept from the old lead.
- `== Results ==`: 1 Desai, 2 Chu, 3 Olson, 4 Sokol, 5–8 Wallin, Harrison-Trainor, Westergard, Walseth. The 3rd/4th disagreement is stated: PC list has Sokol 3rd, Olson 4th; Olson's 2020 article says "2015-3rd" and Sokol's HoF blurb says "4th place finish in 2015" (worlds_issues.md). The old hub's numbered 5–8 are shown as a tie (they match Swiss order 1, 2, 4, 6).
- Day 2 table header "Day 2" → "Place" (Swiss standing).
- `== Side events ==` → Hall of Fame: Lingrell, Menzel, Wallin enshrined 8 Aug 2015.
- Sources: added Awards, Wikipedia, champion post, Olson 2020 article. [[Category:World Championships]] added.

## Facts added (source)
- Champion/runner-up: "World Champion Crowned in Philadelphia" (PC) and Awards page. 61 players: PC list count (Wikipedia agrees).
- HoF class and date: PC Awards page. Olson 3rd: PC 2020 article (snapshot mine/snap_joe-olson-…txt). Sokol 4th: Awards page HoF blurb.

## Deck pages
137 deck pages; all linked exactly once (checked).

## Unresolved
- Top 8 bracket; venue (hotel); team event.
"""
write(y,page,defs,notes)
