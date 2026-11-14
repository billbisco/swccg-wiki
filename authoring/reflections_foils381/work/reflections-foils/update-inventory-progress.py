import collections,csv,json,re
from pathlib import Path
root=Path(__file__).parent;manifest=json.loads((root/'manifest.json').read_bytes());heads=json.loads((root/'published-heads.json').read_bytes());completed=[]
for stage in ['first']+sorted({p.name.split('-public-verification.json')[0] for p in root.glob('batch*-public-verification.json') if re.fullmatch(r'batch\d+-public-verification.json',p.name)},key=lambda s:int(s[5:])):
    if not (root/(stage+'-public-verification.json')).exists():continue
    for reading in json.loads((root/(stage+'-readings.json')).read_bytes()):
        title=reading['article'];row=next(r for r in manifest if r['proposed_article']==title)
        row.update(status='created',existing_article=title,existing_revid=heads[title]['revisions'][0]['revid'],source_photo_sha256=reading.get('source_sha256',reading.get('sha256')),evidence_status='Independent physical-foil transcription; original photograph, reviewed source/public/navigation/conservation verified; source citations and exact wiki-image binaries preserved; playable mapping omitted')
        completed.append(title)
(root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
fields=['product','checklist_number','side','rarity','label','language','alternate_image','status','existing_article','existing_revid','proposed_article','evidence_status']
with (root/'inventory.csv').open('w',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(manifest)
counts=collections.Counter(r['status'] for r in manifest);per_product={p:dict(collections.Counter(r['status'] for r in manifest if r['product']==p)) for p in dict.fromkeys(r['product'] for r in manifest)}
report=dict(total=len(manifest),initially_missing=298,counts=dict(counts),per_product=per_product,verified_new_articles=completed)
(root/'completion-progress.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report['counts']))
