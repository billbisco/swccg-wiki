import sys;sys.path.insert(0,'.')
from fetch import *
import json
d=json.load(open('decks.json'))
allt=set()
for y,v in d.items():
    allt|=set(v['prefix'])|set(v['backlinks'])|set(v['hublinks'])
allt=sorted(allt)
info={}
for i in range(0,len(allt),50):
    chunk=allt[i:i+50]
    for r in allq(action=None,prop='info|categories',titles='|'.join(chunk),cllimit=500) if False else []:
        pass
    cont={}
    while True:
        p=dict(action='query',prop='info|categories',titles='|'.join(chunk),cllimit=500,format='json')
        p.update(cont)
        r=q(**p)
        for pg in r['query']['pages'].values():
            t=pg['title']
            e=info.setdefault(t,{'redirect':False,'missing':False,'cats':[]})
            if 'missing' in pg: e['missing']=True
            if 'redirect' in pg: e['redirect']=True
            e['cats']+= [c['title'] for c in pg.get('categories',[])]
        if 'continue' not in r: break
        cont=r['continue']
json.dump(info,open('info.json','w'),indent=0)
print(len(info))
from collections import Counter
c=Counter(x for v in info.values() for x in v['cats'])
print(c.most_common(40))
