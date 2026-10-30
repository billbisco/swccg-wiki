import json,urllib.request,urllib.parse,sys,time
API='https://wiki.swccg.com/api.php'
def q(**p):
    p.pop("action",None) if p.get("action") is None else None
    p['format']='json'
    url=API+'?'+urllib.parse.urlencode(p)
    for i in range(4):
        try:
            r=urllib.request.Request(url,headers={'User-Agent':'HolocronDraft/1.0'})
            return json.load(urllib.request.urlopen(r,timeout=60))
        except Exception as e:
            time.sleep(3); err=e
    raise err
def text(title):
    d=q(action='query',prop='revisions',rvprop='content|timestamp',rvslots='main',titles=title,redirects=1)
    for p in d['query']['pages'].values():
        if 'missing' in p: return None
        return p['revisions'][0]['slots']['main']['*']
def allq(**p):
    out=[];cont={}
    while True:
        d=q(action='query',**p,**cont)
        out.append(d)
        if 'continue' not in d: break
        cont=d['continue']
    return out
