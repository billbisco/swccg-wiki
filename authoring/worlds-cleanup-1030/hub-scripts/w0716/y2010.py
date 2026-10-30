from lib import *
y=2010
t=open(f'live_{y}.wiki').read()
defs=dict(COMMON); defs.update(refdefs(t)); defs['awards']=COMMON['awards']
defs['forum']='[https://forum.starwarsccg.org/viewforum.php?f=559 2010 Worlds], forum.starwarsccg.org'
defs['decklists']='[https://www.starwarsccg.org/2010-decklists/ 2010 Decklists], starwarsccg.org'
d3=table_rows(get(t,'Day 3'))
def res(p,n): r=deckrow_by_player(d3,n); return [p,r[0],r[1],r[2]]
tw=deckrow_by_player(d3,'Chris Twiss')
results=[res('1','Dan Kim'),res('2','Kyle Krueger'),res('3–4','Jonny Chu'),res('3–4','Steve Baroni'),
 res('5–8','Aaron Kingery'),res('5–8','Matt Sokol'),res('5–8','Chris Terwilliger'),res('5–8','Justin Desai')]
ib=infobox(y,None,None,'12–15 August 2010<ref name="forum" />','Philadelphia, Pennsylvania, USA<ref name="awards" />',
 '[[Premiere - Virtual Block 7.1]]','61<ref name="wp" />','[[Dan Kim]]','[[Kyle Krueger]]',2009,2011)
lead="""'''2010 World Championship''' was the 15th Star Wars CCG World Championship, run by the [[Players Committee]] in Philadelphia, Pennsylvania, on 12–15 August 2010.<ref name="forum" /><ref name="awards" /> The constructed pool was [[Premiere - Virtual Block 7.1]]. 61 players took part.<ref name="wp" /> [[Dan Kim]] defeated [[Kyle Krueger]] in the final, playing Exploiting Opportunities and The Rebel Alliance! on Day 3; it was Krueger's second runner-up finish after 2008.<ref name="awards" /><ref name="f75427-1300387" /> The Players Committee published the Day 2 and Day 3 lists only; no Day 1 or Team Tournament lists were published.<ref name="decklists" />"""
br=shorten_refs(get(t,'Top 8 bracket'))
br=br.replace("[[2010 Worlds Day 3 Steve Baroni DS Hunt Down And Destroy The Jedi|Hunt Down And Destroy The Jedi (V)]]","Hunt Down And Destroy The Jedi (V)")
br=br.replace("[[Chris Twiss]], whose Light list is in the Day 3 PDF.","[[Chris Twiss]], whose Light list is in the Day 3 PDF (listed under [[#Other published decklists|Other published decklists]]).")
br=br.replace("Steve Baroni Dark (Hunt Down And Destroy The Jedi (V), deck name Dry Clean Only) is published","Steve Baroni's Dark list (deck name Dry Clean Only) is published")
d2=shorten_refs(get(t,'Day 2'))
src=merge_sources(bullets(get(t,'Sources')),[SRC_AWARDS,SRC_WP])
page=assemble(y,ib,lead,'Places follow the published Top 8 bracket; semifinal and quarterfinal losers are shown as ties. Decks are the Day 3 lists.',
 results,br,[('Day 2',d2)],
 "[[Chris Twiss]]'s Day 3 Light list is in the Day 3 PDF, but he is not in the published Top 8 bracket.<ref name=\"f75427-1300387\" />",
 [['Day 3',tw[0],tw[1],tw[2]]],None,None,
 see(y,'Premiere - Virtual Block 7.1',['[[Formats]]']),src)
notes="""# 2010 World Championship — draft notes

Draft: hubs_draft/2010_World_Championship.wiki (live hub unchanged since the local copy; re-fetched 30 Oct 2026).

## What changed
- Standard infobox (15th edition, PC, 12–15 Aug 2010, Philadelphia, [[Premiere - Virtual Block 7.1]], 61 players, Kim def. Krueger, 2009 · 2011). No photo exists for 2010; image row and Photographs omitted. Venue (hotel) not found.
- [[Legacy Open]] replaced by [[Premiere - Virtual Block 7.1]] everywhere (lead, infobox, See also). The odd See also links to 2009/2013 replaced by the standard previous/next line.
- `== Results ==` from the forum bracket: 1 Kim, 2 Krueger, 3–4 Chu / Baroni, 5–8 Kingery, Sokol, C. Terwilliger, Desai; Day 3 deck links moved in.
- Chris Twiss's Day 3 Light list (not in the bracket) moved to `== Other published decklists ==`.
- Removed the second link to Steve Baroni's Day 3 Dark list in the PDF paragraph (it is linked once, in Results).
- Bare-URL refs (forum, decklists) given titles; added Awards and Wikipedia to Sources; added [[Category:Tournaments]], [[Category:Championships]].

## Facts added (source)
- 61 players: Wikipedia. Krueger runner-up 2008 and 2010: PC Awards page champions list.

## Deck pages
130 deck pages; all linked exactly once (checked).

## Unresolved
- Chris Twiss's place (he has a Day 3 sheet but is not in the bracket). Venue. Day 2 standings. No side-event results found.
"""
write(y,page,defs,notes)
