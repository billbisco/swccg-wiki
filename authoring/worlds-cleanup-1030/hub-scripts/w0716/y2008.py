from lib import *
y=2008
t=open(f'live_{y}.wiki').read()
defs=dict(COMMON); defs.update(refdefs(t)); defs['awards']=COMMON['awards']
d3=table_rows(get(t,'Day 3'))
def res(p,n): r=deckrow_by_player(d3,n); return [p,r[0],r[1],r[2]]
results=[res('1','Kevin Shannon'),res('2','Kyle Krueger'),res('3–4','Michael Raveling'),res('3–4','Steve Baroni'),
 res('5–8','Tom Frafjord'),res('5–8','Jonny Chu'),res('5–8','Brian Hunter'),res('5–8','Garrett Larson')]
ib=infobox(y,None,None,'10–12 October 2008 (Day 1 10 October, Day 2 11 October, Day 3 12 October)<ref name="tdl" />',
 'Minneapolis, Minnesota, USA<ref name="awards" />','[[Premiere - Original VS16]]','60<ref name="wp" />','[[Kevin Shannon]]','[[Kyle Krueger]]',2007,2009)
lead="""'''2008 World Championship''' was the 13th Star Wars CCG World Championship, run by the [[Players Committee]] in Minneapolis, Minnesota, on 10–12 October 2008. The constructed pool was [[Premiere - Original VS16]].<ref name="awards" /><ref name="tdl" /> 60 players took part.<ref name="wp" /> [[Kevin Shannon]] defeated [[Kyle Krueger]] in the final, playing Ralltiir Operations and Dantooine Base Operations on Day 3; Krueger had reached the final as the eighth seed.<ref name="awards" /><ref name="f75427-1300387" /> [[Justin Desai]]'s team, the [[Kashyyyk Train of Dominance]], won the team championship for the second year running.<ref name="awards" /> The Day 1, Day 2, Day 3 and Team decklists were published as PDFs; the sheets are dated 10 October (Day 1), 11 October (Day 2) and 12 October 2008 (Day 3).<ref name="tdl" />"""
br=shorten_refs(get(t,'Top 8 bracket'))
d2=get(t,'Day 2'); d1=get(t,'Day 1'); team=get(t,'Team Tournament')
side="""=== Team tournament ===

The [[Kashyyyk Train of Dominance]], [[Justin Desai]]'s team, won the 2008 Worlds team championship.<ref name="awards" />

"""+team.strip()
src=merge_sources(bullets(get(t,'Sources')),[SRC_WP])
page=assemble(y,ib,lead,'Places follow the published Top 8 bracket; semifinal and quarterfinal losers are shown as ties. Decks are the Day 3 lists.',
 results,br,[('Day 2',d2),('Day 1',d1)],None,[],side,None,
 see(y,'Premiere - Original VS16',['[[Virtual Sets (2002-2009)]]','[[Formats]]']),src)
notes="""# 2008 World Championship — draft notes

Draft: hubs_draft/2008_World_Championship.wiki (live hub unchanged since the local copy; re-fetched 30 Oct 2026).

## What changed
- Standard infobox (13th edition, PC, 10–12 Oct 2008 with day dates from the sheets, Minneapolis, VS16, 60 players, Shannon def. Krueger, 2007 · 2009). No photo of any kind exists for 2008; image row and Photographs section omitted. Venue (hotel) not found.
- Lead rewritten (edition, field, final, winning decks, eighth seed Krueger reaching the final, KToD team title).
- `== Format ==` bullets dropped (facts in infobox and lead).
- `== Results ==` in finish order from the forum bracket: 1 Shannon, 2 Krueger, 3–4 Raveling / Baroni, 5–8 Frafjord, Chu, Hunter, Larson; Day 3 deck links moved into it. Bracket kept as `=== Top 8 bracket ===`.
- Team table moved to `== Side events ==`.
- Added [[Category:World Championships]]; Wikipedia added to Sources.

## Facts added (source)
- 60 players: Wikipedia SWCCG article.
- KToD won the 2007 and 2008 Worlds Team Championship: PC Awards page (Desai HoF blurb).
- Krueger was seed 8: forum t=75427 bracket post (already on hub).

## Deck pages
211 deck pages for 2008 (redirect titles excluded); all linked exactly once (checked by script).

## Unresolved
- Venue; Day 2 / Day 1 standings; members of the KToD team entry are not identified in the team table.
"""
write(y,page,defs,notes)
