import sys,re,json;sys.path.insert(0,'.')
from fetch import *
def check_links(paths):
    allt=set()
    for p in paths:
        for m in re.findall(r'\[\[([^\]|#]+)',open(p).read()):
            m=m.strip()
            if m.startswith(':') or m.lower().startswith(('file:','category:')): continue
            allt.add(m[0].upper()+m[1:])
    allt=sorted(allt); bad={}
    for i in range(0,len(allt),50):
        r=q(action='query',titles='|'.join(allt[i:i+50]))
        norm={n['from']:n['to'] for n in r['query'].get('normalized',[])}
        for pg in r['query']['pages'].values():
            if 'missing' in pg or 'invalid' in pg: bad[pg.get('title')]='missing'
        rr=q(action='query',titles='|'.join(allt[i:i+50]),redirects=1)
        for m in rr['query'].get('redirects',[]): bad[m['from']]='redirect->'+m['to']
    return bad
if __name__=='__main__':
    import glob
    print(json.dumps(check_links(sys.argv[1:]),indent=0))
