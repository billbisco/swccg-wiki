import json,re,sys,subprocess
R=json.load(open('name_rules.json'))
rows=open('names-auto.tsv').read().splitlines()
out=[rows[0]]; flag=[]
for l in rows[1:]:
    st,key,side,nw,u,g,how=l.split('\t')
    k=f"{st}|{key}"; nwc=re.sub(r'\(.*?\)','',nw).replace('!','').replace('?','').replace('..','').strip(' .')
    p=R['by_key'].get(k) or R['by_written'].get(nwc) or (g if how=='exact' else None) or R['by_user'].get(u.lower()) or R['by_written'].get(nwc) or (g if how in('exact','user') or how.startswith('fuzzy') or how=='NEW' else '')
    if how.startswith('fuzzy') and nwc not in R['by_written'] and k not in R['by_key'] and u.lower() not in R['by_user']: flag.append(('FUZZY',st,key,nw,u,g))
    if not p: flag.append(('NONAME',st,key,nw,u,how[:60]))
    out.append('\t'.join([st,key,side,nw,u,p]))
open('names.tsv','w').write('\n'.join(out)+'\n')
for f in flag: print(*f,sep=' | ')
