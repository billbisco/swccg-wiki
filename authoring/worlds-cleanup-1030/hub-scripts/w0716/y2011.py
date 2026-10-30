from lib import *
y=2011
t=open(f'live_{y}.wiki').read()
defs=dict(COMMON); defs.update(refdefs(t)); defs['awards']=COMMON['awards']
defs['forum']='[https://forum.starwarsccg.org/viewforum.php?f=565 2011 Worlds], forum.starwarsccg.org'
defs['decklists']='[https://www.starwarsccg.org/2011-decklists/ 2011 Decklists], starwarsccg.org'
defs['banner']='[https://web.archive.org/web/20110905074028/http://starwarsccg.org/ starwarsccg.org homepage] (5 September 2011), Internet Archive; see [[:File:Kevin Shannon 2011 Worlds champion banner.jpg]]'
d3=table_rows(get(t,'Day 3'))
def res(p,n): r=deckrow_by_player(d3,n); return [p,r[0],r[1],r[2]]
results=[res('1','Kevin Shannon'),res('2','Brian Herold'),res('3–4','Justin Desai'),res('3–4','Steve Baroni'),
 res('5–8','Reid Smith'),res('5–8','Aaron Nelson'),res('5–8','Jonny Chu'),res('5–8','Chris Terwilliger')]
ib=infobox(y,'Kevin Shannon 2011 Worlds champion banner.jpg','Kevin Shannon on the starwarsccg.org homepage banner as 2011 World Champion',
 '11–14 August 2011<ref name="forum" />','Washington, D.C., USA<ref name="awards" />',
 '[[Premiere - Virtual Block 7.3]]','63<ref name="wp" />','[[Kevin Shannon]]','[[Brian Herold]]',2010,2012)
lead="""'''2011 World Championship''' was the 16th Star Wars CCG World Championship, run by the [[Players Committee]] in Washington, D.C., on 11–14 August 2011.<ref name="forum" /><ref name="awards" /> The constructed pool was [[Premiere - Virtual Block 7.3]]. 63 players took part.<ref name="wp" /> [[Kevin Shannon]], the sixth seed, defeated [[Brian Herold]] in the final, playing Hunt Down And Destroy The Jedi (V) and Heading For The Medical Frigate on Day 3.<ref name="f75427-1300387" /> He was the second player, after [[Jonny Chu]], to win two World Championships (2008 and 2011).<ref name="awards" /> The Players Committee published the Day 2 and Day 3 decklists; no Day 1 or Team Tournament lists were published.<ref name="decklists" />"""
br=shorten_refs(get(t,'Top 8 bracket'))
d2full=get(t,'Day 2'); i=d2full.index('\n|}')+3; d2tab,d2=d2full[:i],d2full[i:]
for a,b in [("[[2011 Worlds Day 2 Unknown player DS Kessel (page 39)|Kessel]]","Kessel"),
 ("[[2011 Worlds Day 2 Unknown player LS Coruscant: Night Club (page 120)|Coruscant: Night Club]]","Coruscant: Night Club"),
 ("[[2011 Worlds Day 2 Unknown player LS Watch Your Step (page 121)|Watch Your Step]]","Watch Your Step"),
 ("[[2011 Worlds Day 2 Josh Mack DS Same As Day 1|Same As Day 1]]","''Same As Day 1''"),
 ("[[2011 Worlds Day 2 Josh Mack LS Communing|Communing]]","Communing"),
 ("named by PDF page: p39","named by PDF page (see [[#Other published decklists|Other published decklists]]): p39")]:
    assert a in d2,a; d2=d2.replace(a,b)
d2=d2tab+d2
other=[['Day 2','Unknown player (PDF page 39)','[[2011 Worlds Day 2 Unknown player DS Kessel (page 39)|Kessel]]','—'],
 ['Day 2','Unknown player (PDF page 120)','—','[[2011 Worlds Day 2 Unknown player LS Coruscant: Night Club (page 120)|Coruscant: Night Club]]'],
 ['Day 2','Unknown player (PDF page 121)','—','[[2011 Worlds Day 2 Unknown player LS Watch Your Step (page 121)|Watch Your Step]]']]
src=merge_sources(bullets(get(t,'Sources')),[SRC_WP,
 '* [https://web.archive.org/web/20110905074028/http://starwarsccg.org/ starwarsccg.org homepage] (5 September 2011, champion banner), Internet Archive'])
src=[SRC_AWARDS if b.strip().endswith('Awards and Hall of Fame], starwarsccg.org') else b for b in src]
gallery=['File:Kevin Shannon 2011 Worlds champion banner.jpg|[[Kevin Shannon]], 2011 World Champion, on the starwarsccg.org homepage banner']
page=assemble(y,ib,lead,'Places follow the published Top 8 bracket; semifinal and quarterfinal losers are shown as ties. Decks are the Day 3 lists.',
 results,br,[('Day 2',d2)],'Three Day 2 sheets carry no player name.',other,None,gallery,
 see(y,'Premiere - Virtual Block 7.3',['[[Formats]]']),src)
notes="""# 2011 World Championship — draft notes

Draft: hubs_draft/2011_World_Championship.wiki (live hub unchanged since the local copy; re-fetched 30 Oct 2026).

## What changed
- Standard infobox (16th edition, PC, 11–14 Aug 2011, Washington D.C., [[Premiere - Virtual Block 7.3]], 63 players, Shannon def. Herold, 2010 · 2012) with File:Kevin Shannon 2011 Worlds champion banner.jpg (already on the wiki, previously unused on the hub). Also in `== Photographs ==`.
- [[Legacy Open]] replaced by the pool page everywhere.
- `== Results ==` from the forum bracket: 1 Shannon (seed 6), 2 Herold, 3–4 Desai / Baroni, 5–8 R. Smith, Nelson, Chu, C. Terwilliger.
- The three ''Unknown player'' Day 2 decks moved from prose into `== Other published decklists ==`; the duplicate prose links to Josh Mack's Day 2 decks removed (they stay in the Day 2 table). The redirect link to Steve Baroni's Day 2 Light deck now points at the real page.
- Bare-URL refs given titles; Wikipedia and homepage-banner capture added to Sources; [[Category:Tournaments]], [[Category:Championships]] added.

## Facts added (source)
- 63 players: Wikipedia. Shannon second two-time champion (2008, 2011): PC Awards page (Shannon HoF blurb); the banner caption says the same.

## Deck pages
129 deck pages; all linked exactly once (checked).

## Unresolved
- Venue. Day 2 standings. No side-event results found. The three unnamed Day 2 sheets.
"""
write(y,page,defs,notes)
