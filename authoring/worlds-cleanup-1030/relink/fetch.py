import json,urllib.request,urllib.parse,time
API="https://wiki.swccg.com/api.php"
def q(**k):
    k.update(format='json',formatversion=2)
    for a in range(6):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(API,data=urllib.parse.urlencode(k).encode(),headers={'User-Agent':'HolocronClaude-relink'}),timeout=120))
        except Exception: time.sleep(5)
bl=[];cont={}
while True:
    r=q(action='query',list='backlinks',bltitle='Legacy Open',bllimit=500,**cont)
    bl+=[x['title'] for x in r['query']['backlinks']]
    if 'continue' not in r: break
    cont=r['continue']
print(len(bl))
pages={}
for i in range(0,len(bl),50):
    r=q(action='query',titles='|'.join(bl[i:i+50]),prop='revisions',rvprop='content|timestamp',rvslots='main')
    for p in r['query']['pages']:
        if p.get('revisions'): pages[p['title']]=dict(ts=p['revisions'][0]['timestamp'],text=p['revisions'][0]['slots']['main']['content'])
json.dump(pages,open('pages.json','w'))
print(len(pages))
