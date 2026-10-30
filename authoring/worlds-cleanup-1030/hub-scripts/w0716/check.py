import sys,re,json;sys.path.insert(0,'.')
from fetch import *
I=json.load(open('info.json'));D=json.load(open('decks.json'))
# resolve redirects
reds=[t for t,v in I.items() if v['redirect']]
target={}
for i in range(0,len(reds),50):
    r=q(action='query',titles='|'.join(reds[i:i+50]),redirects=1)
    for m in r['query'].get('redirects',[]): target[m['from']]=m['to']
json.dump(target,open('redirects.json','w'),indent=0)
def norm(t): 
    t=t.replace('_',' ').strip(); t=t[0].upper()+t[1:]
    return target.get(t,t)
def check(y,path):
    txt=open(path).read()
    links=[norm(m.split('|')[0]) for m in re.findall(r'\[\[([^\]]+)\]\]',txt)]
    decks=set(t for t in set(D[str(y)]['prefix'])|set(D[str(y)]['backlinks']) if 'Category:Decklists' in I[t]['cats'] and not I[t]['redirect'])
    from collections import Counter
    c=Counter(l for l in links if l in decks)
    missing=sorted(decks-set(c)); dup={k:v for k,v in c.items() if v>1}
    return len(decks),missing,dup
if __name__=='__main__':
    for y in range(2007,2017):
        n,m,d=check(y,f'live_{y}.wiki'); print(y,n,len(m),d)
    print(target)
