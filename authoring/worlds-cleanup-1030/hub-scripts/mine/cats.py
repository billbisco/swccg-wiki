import sys,json;sys.path.insert(0,'.');import api
res=json.load(open('pages.json'))
allt=sorted({t for y in res for t in res[y]})
cats={}
for i in range(0,len(allt),50):
    ch=allt[i:i+50]
    for r in api.allq(action='query',prop='categories',titles='|'.join(ch),cllimit='500',redirects='1'):
        for p in r['query']['pages']:
            cats.setdefault(p['title'],[]).extend(c['title'] for c in p.get('categories',[]))
        for rd in r['query'].get('redirects',[]): cats.setdefault('__redir__',[]).append([rd['from'],rd['to']])
json.dump(cats,open('cats.json','w'),indent=0)
from collections import Counter
c=Counter(x for t,v in cats.items() if t!='__redir__' for x in set(v))
print(c.most_common(40)); print(len(cats.get('__redir__',[])))
