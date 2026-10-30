from lib import *
y=2009
t=open(f'live_{y}.wiki').read()
defs=dict(COMMON); defs.update(refdefs(t)); defs['awards']=COMMON['awards']
defs['forum']='[https://forum.starwarsccg.org/viewforum.php?f=353 World Championships - Oct 8-11, 2009], forum.starwarsccg.org'
defs['dl2009']='[https://www.starwarsccg.org/2009-decklists/ 2009 Decklists], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261021002558/https://swccg.com/snapshots/pc/2009-decklists.html Internet Archive]'
d3=table_rows(get(t,'Day 3'))
def res(p,n,disp=None):
    r=deckrow_by_player(d3,n); return [p,disp or r[0],r[1],r[2]]
results=[res('1','Brian Hunter'),res('2','Justin Desai'),res('3–4','Jan Westergard'),
 res('3–4','Mike Gerome','[[Mike Gemme]] (Day 3 sheets: [[Mike Gerome]])<ref name="f75427-1300387" />'),
 res('5–8','Jonny Chu'),res('5–8','Matt Sokol'),res('5–8','Joe Olson'),res('5–8','Aaron Nelson')]
ib=infobox(y,None,None,'8–11 October 2009 (team event 8–9 October)<ref name="forum" /><ref name="dl2009" />',
 'Clarion Hotel, Princeton, New Jersey, USA<ref name="forum" />','[[Premiere - Virtual Block 6.1]]','53<ref name="wp" />','[[Brian Hunter]]','[[Justin Desai]]',2008,2010)
lead="""'''2009 World Championship''' was the 14th Star Wars CCG World Championship, run by the [[Players Committee]] at the Clarion Hotel in Princeton, New Jersey, on 8–11 October 2009.<ref name="forum" /><ref name="awards" /> The constructed pool was [[Premiere - Virtual Block 6.1]]. 53 players took part.<ref name="wp" /> [[Brian Hunter]] defeated [[Justin Desai]] in the final, playing No Money, No Parts, No Deal! and Watch Your Step on Day 3; it was Desai's second runner-up finish after 2007.<ref name="awards" /><ref name="f75427-1300387" /> The Players Committee published the Day 2, Day 3 and Team Tournament lists; no Day 1 lists were published.<ref name="dl2009" />"""
br=shorten_refs(get(t,'Top 8 bracket')).replace('where the Day 3 list above has Mike Gerome','where the Day 3 sheets have Mike Gerome')
d2=get(t,'Day 2'); team=get(t,'Team Tournament')
side="=== Team tournament ===\n\n"+team.strip()
src=merge_sources(bullets(get(t,'Sources')),[SRC_WP])
src=[b.replace('[https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame], starwarsccg.org',SRC_AWARDS[2:]) if b.strip().endswith('Awards and Hall of Fame], starwarsccg.org') else b for b in src]
page=assemble(y,ib,lead,'Places follow the published Top 8 bracket; semifinal and quarterfinal losers are shown as ties. Decks are the Day 3 lists.',
 results,br,[('Day 2',d2)],None,[],side,None,
 see(y,'Premiere - Virtual Block 6.1',['[[2009 Virtual Block Reorganization]]','[[Formats]]']),src)
notes="""# 2009 World Championship — draft notes

Draft: hubs_draft/2009_World_Championship.wiki (live hub unchanged since the local copy; re-fetched 30 Oct 2026).

## What changed
- Standard infobox (14th edition, PC, 8–11 Oct 2009 with team event 8–9 Oct, Clarion Hotel Princeton, [[Premiere - Virtual Block 6.1]], 53 players, Hunter def. Desai, 2008 · 2010). No photo exists for 2009; image row and Photographs omitted.
- Format changed from [[Legacy Open]] to [[Premiere - Virtual Block 6.1]] (pool_map.tsv); [[Legacy Open]] removed from lead, Format and See also. See also now links [[2009 Virtual Block Reorganization]].
- Lead rewritten (edition, venue, pool, field, final, winning decks, Desai's second runner-up finish).
- `== Results ==` from the forum bracket: 1 Hunter, 2 Desai, 3–4 Westergard / Gemme, 5–8 Chu, Sokol, Olson, Nelson. The Gemme row carries the Day 3 sheets filed under [[Mike Gerome]] (the bracket says Mike Gemme; very likely the same player, the sheet name probably a misreading) — flagged.
- Bare-URL refs (forum, awards) replaced with titled citations; "2009 Decklists" now cited inline.
- Team table moved to Side events.

## Facts added (source)
- 53 players: Wikipedia.
- Desai runner-up in 2007 and 2009: PC Awards page (Desai HoF blurb).

## Deck pages
136 deck pages; all linked exactly once (checked).

## Unresolved
- Gemme vs Gerome identity. Day 2 standings. Team event winner.
"""
write(y,page,defs,notes)
