import re,json,sys,urllib.request,urllib.parse,pathlib,collections
final=pathlib.Path(sys.argv[1])
rows=[l.split('\t') for l in (final/'all.tsv').read_text().splitlines() if '\t' in l]
created={t for t,_ in rows}
links=collections.defaultdict(set)
for t,rel in rows:
    s=(final/rel).read_text()
    for m in re.finditer(r'\[\[([^\]|#]+)',s):
        x=m.group(1).strip()
        if x.startswith((':File:','File:','Category:')) : 
            if x.startswith(':File:'): links['File:'+x[6:]].add(t)
            continue
        links[x].add(t)
    for m in re.finditer(r'\{\{CardLink\|([^|}]+)',s): links[m.group(1).strip()].add(t)
need=[x for x in links if x not in created]
missing=[]
for i in range(0,len(need),50):
    q=urllib.parse.urlencode(dict(action='query',titles='|'.join(need[i:i+50]),format='json',formatversion=2))
    r=json.load(urllib.request.urlopen(urllib.request.Request('https://wiki.swccg.com/api.php',data=q.encode())))
    norm={n['to']:n['from'] for n in r['query'].get('normalized',[])}
    for p in r['query']['pages']:
        if p.get('missing'): missing.append(norm.get(p['title'],p['title']))
for x in missing: print('MISSING',x,'<-',sorted(links[x])[:2])
print(len(need),'checked',len(missing),'missing')
