import re,json,sys
sys.path.insert(0,'.')
from parse import *
RED=json.load(open('redirects.json'))
def ordinal(n):
    s='th' if 10<=n%100<=20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')
    return f'{n}{s}'
def fixlinks(s):
    def rep(m):
        inner=m.group(1)
        if inner.startswith((':','File:','Category:')): return m.group(0)
        tgt,_,lab=inner.partition('|')
        t=tgt.strip(); t2=t[0].upper()+t[1:] if t else t
        if t2 in RED:
            return f'[[{RED[t2]}|{lab or t}]]'
        return m.group(0)
    return re.sub(r'\[\[([^\]]+)\]\]',rep,s)
def refdefs(text):
    d={}
    for m in re.finditer(r'<ref name="([^"]+)">(.*?)</ref>',text,flags=re.S):
        d.setdefault(m.group(1),m.group(2))
    return d
def shorten_refs(s):
    return re.sub(r'<ref name="([^"]+)">.*?</ref>',lambda m:f'<ref name="{m.group(1)}" />',s,flags=re.S)
def finalize_refs(page,defs):
    used=[]
    def rep(m):
        n=m.group(1)
        if n not in used:
            used.append(n)
            if n not in defs: raise KeyError(n)
            return f'<ref name="{n}">{defs[n]}</ref>'
        return m.group(0)
    return re.sub(r'<ref name="([^"]+)"\s*/>',rep,page),used
def get(text,name):
    for n,l,t in sections(text):
        if n==name: return t
    return None
def table_rows(sec):
    tb=tables(sec); 
    return rows(tb[0])[1] if tb else []
def mk_table(header,rowlist,sortable=True):
    out=['{| class="wikitable%s"'%(' sortable' if sortable else ''),header]
    for r in rowlist:
        out.append('|-'); out.append('| '+' || '.join(r))
    out.append('|}')
    return '\n'.join(out)
def infobox(y,img,cap,dates,venue,fmt,players,champ,runner,prev,nxt):
    L=['{| class="wikitable expansion-infobox" style="float:right; margin:0 0 1em 1em; width:300px;"',
       f'! colspan="2" | {y} World Championship']
    if img:
        L+=['|-',f'| colspan="2" style="text-align:center;" | [[File:{img}|280px]]<br/><small>{cap}</small>']
    rows_=[('Edition',ordinal(y-1995)),('Organizer','[[Players Committee]]'),('Dates',dates),('Venue',venue),
           ('Format',fmt),('Players',players),('Champion',champ),('Runner-up',runner),
           ('Previous / Next',f'[[{prev} World Championship|{prev}]] · [[{nxt} World Championship|{nxt}]]')]
    for k,v in rows_:
        if v: L+=['|-',f'! {k}',f'| {v}']
    L.append('|}')
    return '\n'.join(L)
TAIL='''{{#if:1|<nowiki />
<h2>References</h2>
<references />}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:World Championships]]
[[Category:%d]]'''
COMMON={
 'awards':'[https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261016161923/https://swccg.com/snapshots/pc/community-awards.html Internet Archive]',
 'wp':'[https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Star Wars Customizable Card Game], Wikipedia (World Championship table).',
 'f75427-1300387':'[https://forum.starwarsccg.org/viewtopic.php?p=1300387#p1300387 Post by Yoshi], "SWCCG Worlds Day 3 Standings History", forum.starwarsccg.org (28 May 2020). Preserved copy: [https://web.archive.org/web/20261012152200/https://swccg.com/snapshots/forum/t75427.html#p1300387 Internet Archive]',
}
SRC_AWARDS='* [https://www.starwarsccg.org/community/awards/ Awards and Hall of Fame], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261016161923/https://swccg.com/snapshots/pc/community-awards.html Internet Archive]'
SRC_WP='* [https://en.wikipedia.org/wiki/Star_Wars_Customizable_Card_Game Star Wars Customizable Card Game], Wikipedia (World Championship table: site and field size).'
def merge_sources(old_bullets,add):
    out=[];seen=set()
    def key(b):
        m=re.search(r'\[(https?://\S+)',b); u=m.group(1) if m else b
        return re.sub(r'^https?://(www\.)?','',u).rstrip('/')
    for b in old_bullets+add:
        k=key(b)
        if k in seen: continue
        seen.add(k); out.append(b)
    return out
def bullets(sec):
    return [l for l in (sec or '').split('\n') if l.startswith('*')]
def deckrow_by_player(rowsl,needle,col0=0):
    for r in rowsl:
        if needle in r[col0]: return r
    raise KeyError(needle)
def write(y,page,defs,notes):
    page=fixlinks(page)
    page,used=finalize_refs(page,defs)
    page=re.sub(r'\n{3,}','\n\n',page)
    open(f'../hubs_draft/{y}_World_Championship.wiki','w').write(page.strip()+'\n')
    open(f'../hubs_draft/{y}.notes.md','w').write(notes.strip()+'\n')
    return page

def assemble(y,ib,lead,results_intro,results,bracket,days,other_intro,other_rows,side,gallery,seealso,src,tail_extra=''):
    P=[ib,lead,'','== Results ==','']
    if results_intro: P+=[results_intro,'']
    P+=[mk_table('! Place !! Player !! Dark !! Light',results),'']
    if bracket: P+=['=== Top 8 bracket ===','',bracket.strip(),'']
    for h,body in days:
        P+=[f'== {h} ==','',body.strip(),'']
    if other_rows:
        P+=['== Other published decklists ==','']
        if other_intro: P+=[other_intro,'']
        P+=[mk_table('! Stage !! Player !! Dark !! Light',other_rows),'']
    if side:
        P+=['== Side events ==','',side.strip(),'']
    if gallery:
        P+=['== Photographs ==','','<gallery>']+gallery+['</gallery>','']
    P+=['== See also ==','']+['* '+x for x in seealso]+['','== Sources ==','']+src+['',TAIL%y]
    return '\n'.join(P)
def see(y,fmt,extra=()):
    return ['[[World Championships]]',f'[[{y-1} World Championship]] · [[{y+1} World Championship]]',f'[[{fmt}]]']+list(extra)+['[[Championships]]','[[List of SWCCG tournaments]]']
