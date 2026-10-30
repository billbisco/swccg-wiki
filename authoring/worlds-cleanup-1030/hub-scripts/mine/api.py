import json,sys,urllib.request,urllib.parse,time
API='https://wiki.swccg.com/api.php'
def q(**p):
    p.setdefault('format','json'); p.setdefault('formatversion','2')
    url=API+'?'+urllib.parse.urlencode(p)
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'HolocronClaude-draft/1.0'}),timeout=60) as r:
                return json.load(r)
        except Exception as e:
            err=e; time.sleep(2)
    raise err
def text(title):
    d=q(action='query',prop='revisions',rvprop='content|timestamp',rvslots='main',titles=title)
    pg=d['query']['pages'][0]
    if 'missing' in pg: return None
    return pg['revisions'][0]['slots']['main']['content']
def allq(**p):
    out=[];cont={}
    while True:
        d=q(**p,**cont)
        out.append(d)
        if 'continue' in d: cont=d['continue']
        else: return out
