import sys,json;sys.path.insert(0,'.');import api
res={}
for y in range(2017,2027):
    s={}
    for r in api.allq(action='query',list='backlinks',bltitle=f'{y} World Championship',bllimit='500',blnamespace='0'):
        for b in r['query']['backlinks']: s[b['title']]='bl'
    for pre in [f'{y} World Championship',f'{y} Worlds',f'{y} Decipher World Championship',f'{y} WC',f'{y} World']:
        for r in api.allq(action='query',list='allpages',apprefix=pre,aplimit='500',apnamespace='0'):
            for b in r['query']['allpages']: s.setdefault(b['title'],'pre')
    res[y]=s
    print(y,len(s))
json.dump(res,open('pages.json','w'),indent=0)
