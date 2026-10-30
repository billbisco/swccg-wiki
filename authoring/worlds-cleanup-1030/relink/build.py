import json,re,collections,os
pages=json.load(open('pages.json'))
pm={l.split('\t')[0]:l.rstrip('\n').split('\t')[2] for l in open('../champ/pool_map.tsv') if not l.startswith('event')}
WORLDS={f"{y} World Championship" for y in range(2009,2015)}
LO=re.compile(r"\[\[Legacy Open(?:\|([^\]]*))?\]\]")
os.makedirs('out/pages',exist_ok=True); rows=[]; rep=collections.Counter(); skipped=[]
def fn(t): return re.sub(r"[^\w.-]+","_",t)+".wiki"
for t,v in pages.items():
    if t in WORLDS: continue
    c=v['text']
    evs={m for m in re.findall(r"\[\[([^\]|#]+)",c) if m in pm}
    pools={pm[e] for e in evs}
    page_pool = pm[t] if t in pm else (next(iter(pools)) if len(pools)==1 else None)
    if not evs and t not in pm: rep['general-skip']+=1; continue
    out=[]; changed=False
    for line in c.split('\n'):
        if LO.search(line):
            le={m for m in re.findall(r"\[\[([^\]|#]+)",line) if m in pm}
            lp={pm[e] for e in le}
            pool = next(iter(lp)) if len(lp)==1 else (page_pool if (not lp and (t in pm or "'''Format:'''" in line or 'Environment:' in line)) else None)
            if pool:
                line=re.sub(r"the pre-reset virtual pool \(\[\[Legacy Open\]\]\)", f"the [[{pool}]] pool", line)
                line=re.sub(r"pre-reset virtual pool \(\[\[Legacy Open\]\]\)", f"[[{pool}]] pool", line)
                line=LO.sub(lambda m: f"[[{pool}]]", line); changed=True; rep['lines']+=1
            else:
                skipped.append((t,line[:160])); rep['line-skip']+=1
        out.append(line)
    if changed:
        open('out/pages/'+fn(t),'w').write('\n'.join(out)); rows.append(f"{t}\tpages/{fn(t)}"); rep['pages']+=1
open('out/all.tsv','w').write('\n'.join(rows)+'\n')
json.dump(skipped,open('skipped.json','w'),indent=0)
print(rep); print(skipped[:15])
