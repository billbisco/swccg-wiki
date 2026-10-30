import sys;sys.path.insert(0,'.')
from fetch import *
import json,re
res={}
for y in range(2007,2017):
    hub=f'{y} World Championship'
    s=set()
    for d in allq(list='backlinks',bltitle=hub,bllimit=500,blnamespace=0):
        for b in d['query']['backlinks']: s.add(b['title'])
    pre=set()
    for p in [f'{y} World Championship',f'{y} Worlds',f'{y} Decipher World Championship',f'{y} World']:
        for d in allq(list='prefixsearch',pssearch=p,pslimit=500,psnamespace=0):
            for b in d['query']['prefixsearch']: pre.add(b['title'])
    # links from hub
    links=set()
    for d in allq(prop='links',titles=hub,pllimit=500,plnamespace=0):
        for p in d['query']['pages'].values():
            for l in p.get('links',[]): links.add(l['title'])
    res[y]=dict(backlinks=sorted(s),prefix=sorted(pre),hublinks=sorted(links))
    print(y,len(s),len(pre),len(links))
json.dump(res,open('decks.json','w'),indent=1)
