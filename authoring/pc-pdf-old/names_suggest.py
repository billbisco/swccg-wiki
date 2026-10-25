import json,glob,difflib,re,sys,pathlib
players=open('players.txt').read().split('\n'); um=json.load(open('usernames.json'))
pl_low={p.lower():p for p in players}
stems=sys.argv[1].split(',')
rows=[]
for f in sorted(glob.glob('out/G*/*.json')):
    if 'results' in f: continue
    d=json.load(open(f))
    if d['pdf'] not in stems: continue
    st=pathlib.Path(f).stem; key='p'+st.split('-p',1)[1]
    nw=(d.get('name_written') or '').strip(); u=(d.get('username') or '').strip()
    g=''
    if u.lower() in um: g=max(um[u.lower()],key=um[u.lower()].get)
    elif nw.lower() in pl_low: g=pl_low[nw.lower()]
    else:
        m=difflib.get_close_matches(nw,players,n=1,cutoff=0.82)
        if m: g=m[0]
        else:
            sur=nw.replace('?','').replace('!','').split()[-1].lower() if nw.split() else ''
            c=[p for p in players if p.lower().split()[-1]==sur] if sur else []
            if len(c)==1: g=c[0]+' ?'
            elif c: g='?? '+' | '.join(c[:5])
    rows.append([d['pdf'],key,d['side'][:1],nw,u,g])
print('stem\tkey\tside\tname_written\tusername\tplayer')
for r in rows: print('\t'.join(r))
