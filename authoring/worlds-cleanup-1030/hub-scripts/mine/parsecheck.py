import sys,json,urllib.request,urllib.parse
API='https://wiki.swccg.com/api.php'
for y in range(2017,2027):
    txt=open(f'../hubs_draft/{y}_World_Championship.wiki').read()
    data=urllib.parse.urlencode(dict(action='parse',format='json',formatversion=2,title=f'{y} World Championship',text=txt,prop='links|images|parsewarnings|text',contentmodel='wikitext',disablelimitreport=1)).encode()
    r=json.load(urllib.request.urlopen(urllib.request.Request(API,data=data,headers={'User-Agent':'HolocronClaude-draft/1.0'}),timeout=120))['parse']
    red=[l['title'] for l in r['links'] if not l['exists']]
    html=r['text']
    import re
    errs=re.findall(r'class="(?:error|cite-error|mw-ext-cite-error)"[^>]*>(.{0,150})',html)
    # images exist?
    imgs=r['images']
    missimg=[]
    if imgs:
      q=urllib.parse.urlencode(dict(action='query',format='json',formatversion=2,titles='|'.join('File:'+i for i in imgs)))
      pr=json.load(urllib.request.urlopen(urllib.request.Request(API+'?'+q,headers={'User-Agent':'x'})))['query']['pages']
      missimg=[p['title'] for p in pr if p.get('missing') and 'imagerepository' not in p or p.get('imagerepository')=='']
    open(f'render_{y}.html','w').write(html)
    print(y,'red',red,'errors',errs[:3],'warn',r.get('parsewarnings'),'imgs',len(imgs),'missing imgs',missimg)
