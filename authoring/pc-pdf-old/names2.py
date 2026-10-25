import json,glob,difflib,re,sys,pathlib,collections
players=[p for p in open('players.txt').read().split('\n') if p]; um=json.load(open('usernames.json'))
low={p.lower():p for p in players}
def clean(n):
    n=re.sub(r'\(.*?\)','',n).replace('?','').replace('!','').strip()
    if ',' in n:
        a,b=[x.strip() for x in n.split(',',1)]; n=b+' '+a
    return re.sub(r'\s+',' ',n)
rows=[]
for line in open('names-draft.tsv').read().splitlines()[1:]:
    st,key,side,nw,u,_=(line.split('\t')+['']*6)[:6]
    c=clean(nw); g='';how=''
    if u.lower() in um: g=max(um[u.lower()],key=um[u.lower()].get);how='user'
    elif c.lower() in low: g=low[c.lower()];how='exact'
    else:
        m=difflib.get_close_matches(c,players,n=3,cutoff=0.8)
        if m: g=m[0];how='fuzzy:'+'|'.join(m)
        elif len(c.split())>=2: g=c;how='NEW'
        else:
            sur=c.lower()
            cands=[p for p in players if p.lower().split()[-1]==sur or p.lower().split()[0]==sur]
            how='AMBIG:'+'|'.join(cands[:6]); g=''
    rows.append([st,key,side,nw,u,g,how])
with open('names-auto.tsv','w') as f:
    f.write('stem\tkey\tside\tname_written\tusername\tplayer\thow\n')
    for r in rows: f.write('\t'.join(r)+'\n')
for r in rows:
    if r[6]!='exact' and r[6]!='user':
        print(f"{r[0][5:]:22} {r[1]:5} {r[2]} | {r[3][:28]:28} | {r[4][:14]:14} | {r[5]:24} | {r[6][:70]}")
