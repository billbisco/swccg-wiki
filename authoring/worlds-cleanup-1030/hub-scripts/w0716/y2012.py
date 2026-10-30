from lib import *
y=2012
t=open(f'live_{y}.wiki').read()
defs=dict(COMMON); defs.update(refdefs(t)); defs['awards']=COMMON['awards']
defs['decklists']='[https://www.starwarsccg.org/2012-decklists/ 2012 Decklists], starwarsccg.org'
defs['tdl']='[https://www.starwarsccg.org/resources/tournament-decklists/ Tournament Decklists], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261020044435/https://swccg.com/snapshots/pc/tournament-decklists.html Internet Archive]'
results=[['1','[[Emil Wallin]]','—','—'],['2','[[Angelo Consoli]]','—','—']]
ib=infobox(y,None,None,'12–14 October 2012<ref name="decklists" />','Bochum, Germany<ref name="awards" />',
 '[[Premiere - Virtual Block 8.2]]','54<ref name="wp" />','[[Emil Wallin]]','[[Angelo Consoli]]',2011,2013)
lead="""'''2012 World Championship''' was the 17th Star Wars CCG World Championship, run by the [[Players Committee]] in Bochum, Germany, on 12–14 October 2012.<ref name="awards" /><ref name="decklists" /> [[Chris Menzel]] was instrumental in bringing the event to Europe.<ref name="awards" /> The constructed pool was [[Premiere - Virtual Block 8.2]]. 54 players took part.<ref name="wp" /> [[Emil Wallin]] of Sweden won, defeating [[Angelo Consoli]] in the final by 1 card; the title capped a year in which Wallin also won the Swedish Nationals and the European Championship.<ref name="awards" /> The Players Committee published only the Day 2 decklists.<ref name="decklists" /><ref name="tdl" />"""
d2=get(t,'Day 2')
side="""=== Lifetime achievement award ===

At the 2012 World Championship the European players presented [[Chris Menzel]] with a lifetime achievement award, which earned him the title "Euro Emperor".<ref name="awards" />"""
src=merge_sources(bullets(get(t,'Sources')),[SRC_WP,
 '* [https://www.starwarsccg.org/resources/tournament-decklists/ Tournament Decklists], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261020044435/https://swccg.com/snapshots/pc/tournament-decklists.html Internet Archive]'])
src=[SRC_AWARDS if b.strip().endswith('Awards and Hall of Fame], starwarsccg.org') else b for b in src]
page=assemble(y,ib,lead,"Only the final is known; no Top 8 standings or Day 3 lists have been found. Wallin's and Consoli's Day 2 lists are in the Day 2 table.<ref name=\"awards\" />",
 results,None,[('Day 2',d2)],None,[],side,None,
 see(y,'Premiere - Virtual Block 8.2',['[[Formats]]']),src)
notes="""# 2012 World Championship — draft notes

Draft: hubs_draft/2012_World_Championship.wiki (live hub unchanged since the local copy; re-fetched 30 Oct 2026).

## What changed
- Standard infobox (17th edition, PC, 12–14 Oct 2012, Bochum, [[Premiere - Virtual Block 8.2]], 54 players, Wallin def. Consoli, 2011 · 2013). No photo exists for 2012.
- [[Legacy Open]] replaced by the pool page everywhere.
- `== Results ==` has only places 1–2 (no Top 8 or Day 3 lists published); deck cells "—" because both players' Day 2 lists are linked once in the Day 2 table.
- New `== Side events ==`: Chris Menzel's lifetime achievement award from the European players at Worlds 2012 ("Euro Emperor").
- Lead: Menzel instrumental in bringing Worlds to Europe; Wallin's 2012 (Swedish Nationals, European Championship, Worlds); final "by 1 card" now cited to the Awards page (Consoli HoF blurb).
- Bare-URL refs given titles; Wikipedia and Tournament Decklists added to Sources; categories completed.

## Facts added (source)
- 54 players: Wikipedia. Menzel items, Wallin's 2012, "by 1 card": PC Awards page (HoF blurbs).

## Deck pages
94 deck pages; all linked exactly once (checked).

## Unresolved
- Top 8 and places 3–8; Day 3 lists; venue (hotel) in Bochum; team event.
"""
write(y,page,defs,notes)
