import json,re,sys,os
sys.path.insert(0,'/home/claude/swccg-wiki/authoring'); import style_lint as SL
idx={i['file']:i for i in json.load(open('index.json'))}
batches=sys.argv[2:]; out=sys.argv[1]
done=set(json.load(open('published.json'))) if os.path.exists('published.json') else set()
man=[];rep=[]
for b in batches:
    for it in json.load(open(f'batch{int(b):02d}.json')):
        f=it['file']; p=f'out/{f}.wiki'
        if not os.path.exists(p) or it['title'] in done: continue
        new=open(p).read(); old=open(f'pages/{f}.wiki').read()
        if new.strip()==old.strip(): continue
        defs=set(re.findall(r'<ref\s+name\s*=\s*"?([^">/]+?)"?\s*>',new)); uses=set(re.findall(r'<ref\s+name\s*=\s*"?([^">/]+?)"?\s*/>',new))
        dang=uses-defs
        big=len(new)>150000 or len(old)>150000
        fl,n=SL.lint(new,it['title']) if not big else ([],0); n0=SL.lint(old,it['title'])[1] if not big else 0
        fl=[x for x in fl if "'Sources'" not in x]
        bad=[x for x in fl if not re.search(r"'we'|'we'll'",x)]
        rep.append(f"{it['title']}: words {n0}->{n} flags {len(fl)} dangling {sorted(dang)}")
        if dang: continue
        talk=open(f'out/{f}.talk').read() if os.path.exists(f'out/{f}.talk') else None
        summ=open(f'out/{f}.sum').read().strip() if os.path.exists(f'out/{f}.sum') else 'Style pass per SWCCG Wiki:Style guide'
        man.append({'title':it['title'],'ts':it['ts'],'text':new,'talk':talk,'summary':summ[:250]})
json.dump(man,open(out,'w'))
print('\n'.join(rep)); print('manifest',len(man))
