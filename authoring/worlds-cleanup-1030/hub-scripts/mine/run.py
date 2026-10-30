import sys,json,re;sys.path.insert(0,'.')
from lib import *
import gen_a,gen_b,gen_c
res=json.load(open('pages.json'));cats_=json.load(open('cats.json'))
Y={**gen_a.YEARS,**gen_b.YEARS,**gen_c.YEARS}
for y in sorted(Y):
    body,defs=Y[y]()
    out,unused=resolve_refs(body,defs)
    deck={t for t in res[str(y)] if 'Category:Decklists' in cats_.get(t,[])}
    n,d,m=check(y,out,deck)
    open(f'../hubs_draft/{y}_World_Championship.wiki','w').write(out+'\n')
    print(y,'decks',len(deck),'linked',n,'dups',d,'missing',m,'unused refs',unused,'len',len(out))
