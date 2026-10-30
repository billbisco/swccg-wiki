from lib import *
y=2016
t=open(f'live_{y}.wiki').read()
defs=dict(COMMON); defs.update(refdefs(t)); defs['awards']=COMMON['awards']
defs['pc']='[https://www.starwarsccg.org/2016-world-championships/ 2016 World Championships], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261013125623/https://swccg.com/snapshots/pc/2016-world-championships.html Internet Archive]'
d3=table_rows(get(t,'Day 3'))
def res(p,n): r=deckrow_by_player(d3,n,1); return [p,r[1],r[2],r[3]]
results=[res('1','Tom Haid'),res('2','Reid Smith'),res('3–4','Emil Wallin'),res('3–4','Justin Desai'),
 res('5–8','Jonny Chu'),res('5–8','Tom Kelly'),res('5–8','Casey Anis'),res('5–8','Charlie Arlandson')]
d2=get(t,'Day 2').replace('! Day 2 !! Player !! Dark !! Light','! Place !! Player !! Dark !! Light')
ib=infobox(y,None,None,'11–15 August 2016<ref name="pc" />','Princeton, New Jersey, USA<ref name="awards" />',
 '[[Open]]','62<ref name="pc" />','[[Tom Haid]]','[[Reid Smith]]',2015,2017)
lead="""'''2016 World Championship''' was the 21st Star Wars CCG World Championship, run by the [[Players Committee]] in Princeton, New Jersey, on 11–15 August 2016.<ref name="pc" /><ref name="awards" /> The constructed format was [[Open]]. 62 players took part.<ref name="pc" /><ref name="wp" /> [[Tom Haid]] defeated [[Reid Smith]] in the final, playing Bring Him Before Me and Quiet Mining Colony on Day 3; it was Smith's second runner-up finish in four years, after 2013.<ref name="awards" /><ref name="pc" /> The Players Committee's wrap-up calls the Top 8 stage "Day 2" and the Swiss stage "Day 1"; this page follows the individual list titles (Day 3 = Top 8, Day 2 = Swiss).<ref name="pc" />"""
intro=("Places 1–2 are from the final.<ref name=\"awards\" /> The PC list numbers the rest of the Top 8 in Swiss order; the bracket was not published, so semifinal and quarterfinal places are shown as ties, assuming the listed 3rd and 4th were the losing semifinalists.<ref name=\"pc\" /> Decks are the Day 3 lists.")
src=merge_sources(bullets(get(t,'Sources')),[SRC_AWARDS,SRC_WP])
page=assemble(y,ib,lead,intro,results,None,[('Day 2',"Swiss standings as listed by the Players Committee.<ref name=\"pc\" />\n\n"+d2)],None,[],None,None,
 see(y,'Open',['[[Formats]]']),src)
notes="""# 2016 World Championship — draft notes

Draft: hubs_draft/2016_World_Championship.wiki (live hub unchanged since the local copy; re-fetched 30 Oct 2026).

## What changed
- Standard infobox (21st edition, PC, 11–15 Aug 2016, Princeton NJ, [[Open]], 62 players, Haid def. Reid Smith, 2015 · 2017). No photo of any kind exists for 2016; image row and Photographs omitted.
- Runner-up Reid Smith added (missing before); Smith's second runner-up finish (2013, 2016) from the Awards champions list.
- `== Results ==`: 1 Haid, 2 R. Smith, 3–4 Wallin / Desai, 5–8 Chu, Kelly, Anis, Arlandson. The old hub numbered 3–8 from the PC list; that list order matches Swiss order (Wallin 1, Desai 6; Chu 3, Kelly 4, Anis 7, Arlandson 8), so places are shown as ties. The 3–4 / 5–8 split assumes the PC's 3rd and 4th were the losing semifinalists — stated on the page; revert to the PC numbering if you prefer.
- Day 2 table header "Day 2" → "Place" (Swiss standing).
- No side events found (Mark Walseth's HoF enshrinement was 2017, Sokol/Gogolen 2019).
- Sources: added Awards and Wikipedia. [[Category:World Championships]] added.

## Facts added (source)
- Champion, runner-up, Princeton: PC Awards page. 62 players: PC list count (Wikipedia agrees).

## Deck pages
138 deck pages; all linked exactly once (checked). Tim Culver (Swiss 48) has no deck pages ("—").

## Unresolved
- Bracket and real places 3–8; venue (hotel); team event.
"""
write(y,page,defs,notes)
