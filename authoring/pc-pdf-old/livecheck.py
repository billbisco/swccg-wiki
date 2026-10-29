import json,urllib.request,urllib.parse,collections,sys,time
T=[l.split('\t')[0] for l in open('pkg/all.tsv').read().splitlines() if '\t' in l]
def q(p):
    p.update(format='json',formatversion=2)
    for i in range(5):
        try: return json.load(urllib.request.urlopen(urllib.request.Request('https://wiki.swccg.com/api.php',data=urllib.parse.urlencode(p).encode()),timeout=90))
        except Exception: time.sleep(3)
missing=collections.defaultdict(set); notexist=[]
for i in range(0,len(T),20):
    batch=T[i:i+20]
    r=q(dict(action='query',titles='|'.join(batch),prop='info'))
    notexist+=[p['title'] for p in r['query']['pages'] if p.get('missing')]
    cont={}
    while True:
        p=dict(action='query',titles='|'.join(batch),generator='links',gpllimit='max',prop='info'); p.update(cont)
        r=q(p)
        for pg in r.get('query',{}).get('pages',[]):
            if pg.get('missing'): missing[pg['title']].add('?')
        if 'continue' not in r: break
        cont=r['continue']
print('pages not existing:',len(notexist),notexist[:5])
print('red link targets:',len(missing),sorted(missing)[:30])
