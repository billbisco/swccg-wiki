import sys;sys.path.insert(0,'.')
from fetch import *
import os
for y in range(2007,2017):
    t=text(f'{y} World Championship')
    open(f'live_{y}.wiki','w').write(t)
    old=open(f'../hub_{y}_World_Championship.wiki').read()
    print(y,len(t),'same' if t.strip()==old.strip() else 'DIFF')
