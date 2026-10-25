#!/bin/bash
# rebuild given years then merge + hubs
cd "$(dirname "$0")"
for y in "$@"; do rm -rf final-$y; python3 build.py events-$y.json names-$y.tsv final-$y > build-$y.log 2>&1 & done; wait
for y in "$@"; do tail -1 build-$y.log; done
rm -rf final-all && mkdir -p final-all/pages
python3 - <<'PY'
import json,shutil,glob
E={}
for y in (2007,2010,2011): E.update(json.load(open(f'events-{y}.json')))
json.dump(E,open('events-all.json','w'),indent=1,ensure_ascii=False)
B=[];C=[]
for y in (2007,2010,2011):
    B+=json.load(open(f'final-{y}/decks-built.json')); C+=json.load(open(f'final-{y}/decks-canon.json'))
    for f in glob.glob(f'final-{y}/pages/*'): shutil.copy(f,'final-all/pages/')
json.dump(B,open('final-all/decks-built.json','w'),indent=1,ensure_ascii=False)
json.dump(C,open('final-all/decks-canon.json','w'),indent=1,ensure_ascii=False)
PY
date -u +%Y-%m-%dT%H:%M:%SZ > final-all/since.txt
python3 hubs.py events-all.json final-all
