import sys;sys.path.insert(0,'.')
from fetch import *
import json
d=json.load(open('decks.json'))
for y in range(2007,2017):
    mem=[]
    for r in allq(list='categorymembers',cmtitle=f'Category:{y}',cmlimit=500,cmnamespace=0):
        mem+=[m['title'] for m in r['query']['categorymembers']]
    known=set(d[str(y)]['prefix'])
    odd=[t for t in mem if t not in known and ('world' in t.lower() or 'wc' in t.lower().split())]
    print(y,len(mem),odd)
