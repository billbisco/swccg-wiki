"""After an apply: list lines another editor added the same day that our edit removed (edit-conflict check). Usage: clobber_check.py TSV..."""
import sys,json,urllib.request,urllib.parse,difflib
API="https://wiki.swccg.com/api.php"
def q(**k):
    k.update(format='json',formatversion=2)
    return json.load(urllib.request.urlopen(API+'?'+urllib.parse.urlencode(k),timeout=60))
titles=[]
for f in sys.argv[1:]:
    titles+=[l.split('\t')[0] for l in open(f,encoding='utf-8') if l.strip()]
titles=list(dict.fromkeys(titles))
for t in titles:
    r=q(action='query',titles=t,prop='revisions',rvlimit=6,rvprop='ids|timestamp|user|content',rvslots='main')
    revs=r['query']['pages'][0].get('revisions',[])
    for i in range(len(revs)-1):
        mine,prev=revs[i],revs[i+1]
        if mine['user']=='Holocron Claude' and prev['user']!='Holocron Claude' and mine['timestamp'][:10]==prev['timestamp'][:10]:
            a=prev['slots']['main']['content'].splitlines(); b=set(mine['slots']['main']['content'].splitlines())
            # lines prev added vs its parent
            if i+2<len(revs): pa=set(revs[i+2]['slots']['main']['content'].splitlines())
            else: pa=set()
            lost=[l for l in a if l not in b and l not in pa and l.strip()]
            if lost: print('LOST',t,prev['user'],prev['timestamp'],'->',mine['timestamp'],len(lost),lost[:2])
