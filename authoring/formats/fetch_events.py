import json,re,urllib.request,urllib.parse
API='https://wiki.swccg.com/api.php'
def texts(titles):
    out={}
    for i in range(0,len(titles),50):
        q=dict(action='query',prop='revisions',rvprop='content',rvslots='main',titles='|'.join(titles[i:i+50]),redirects='1',format='json',formatversion='2')
        r=json.load(urllib.request.urlopen(API,urllib.parse.urlencode(q).encode(),timeout=120))
        red={x['from']:x['to'] for x in r['query'].get('redirects',[])}
        got={p['title']:p['revisions'][0]['slots']['main']['content'] for p in r['query']['pages'] if 'revisions' in p}
        for t in titles[i:i+50]: out[t]=got.get(red.get(t,t))
    return out
L=texts(['List of SWCCG tournaments'])['List of SWCCG tournaments']
ev=[]
for m in re.finditer(r'^\| ([^\n]*)$',L,re.M):
    c=[x.strip() for x in m.group(1).split('||')]
    if len(c)>=2:
        k=re.match(r'\[\[([^\]|]+)',c[1])
        if k: ev.append(k.group(1).strip())
ev=sorted(set(ev)); H=texts(ev)
json.dump({'list':L,'hubs':H},open('/tmp/claude-0/fmt/events.json','w'))
print(len(ev),sum(1 for v in H.values() if v))
