import sys,json;sys.path.insert(0,'.');import api
res=json.load(open('pages.json'));cats=json.load(open('cats.json'))
out={}
for y in res:
    ts=[t for t in res[y] if t.startswith(y) and 'Category:Decklists' not in cats.get(t,[])]
    for i in range(0,len(ts),50):
        for r in api.allq(action='query',prop='info',titles='|'.join(ts[i:i+50])):
            for p in r['query']['pages']:
                out[p['title']]=dict(redirect=p.get('redirect',False),len=p.get('length'))
    tgt={}
    rds=[t for t in ts if out.get(t,{}).get('redirect')]
    for i in range(0,len(rds),50):
        r=api.q(action='query',titles='|'.join(rds[i:i+50]),redirects='1')
        for rd in r['query'].get('redirects',[]): tgt[rd['from']]=rd['to']
    nonred=[t for t in ts if not out.get(t,{}).get('redirect')]
    print(y,'redirects',len(rds),'nonredirect nondeck:',nonred)
    for t in rds: out[t]['to']=tgt.get(t)
json.dump(out,open('info.json','w'),indent=0)
