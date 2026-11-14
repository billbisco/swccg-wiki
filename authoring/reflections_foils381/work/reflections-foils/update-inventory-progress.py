import collections,csv,json,re
from pathlib import Path
root=Path(__file__).parent;manifest=json.loads((root/'manifest.json').read_bytes());heads=json.loads((root/'published-heads.json').read_bytes());completed=[];pending=[];deferred=[]
stages=['first']+sorted({p.name.split('-new-receipts.jsonl')[0] for p in root.glob('batch*-new-receipts.jsonl') if re.fullmatch(r'batch\d+-new-receipts.jsonl',p.name)},key=lambda s:int(s[5:]))
for stage in stages:
    receipt_file=root/(stage+'-new-receipts.jsonl')
    if not receipt_file.exists():continue
    receipts={r['title']:r for r in map(json.loads,receipt_file.read_text().splitlines())};verified=(root/(stage+'-public-verification.json')).exists()
    for reading in json.loads((root/(stage+'-readings.json')).read_bytes()):
        title=reading['article']
        if title not in receipts:continue
        row=next(r for r in manifest if r['proposed_article']==title)
        revision=heads[title]['revisions'][0]['revid'] if verified else receipts[title]['revid']
        marker_file=root/(stage+'-publication-verification.json')
        marker=json.loads(marker_file.read_bytes()) if marker_file.exists() else {}
        if marker.get('archive_deferred'):
            verified=marker.get('publication_verified') and marker.get('visual_inspection')=='inspected and accepted by MemoryCoreChatGPT'
            status='created_preservation_queued' if verified else 'published_pending_batch_verification'
        else:status='created' if verified else 'published_pending_batch_verification'
        evidence='Independent physical-foil transcription; original photograph, reviewed source/public/navigation/conservation verified; source citations and exact wiki-image binaries preserved; playable mapping omitted' if verified else 'Article published from independent physical-foil reading and reviewed by own bot; full family/checklist/public/preservation batch verification remains in progress'
        if status=='created_preservation_queued':evidence='Independent foil reading, original hash, supported review, reciprocal checklist/family navigation, source conservation and public/visual checks passed; external preservation queued under Bill’s explicit14 November authorization and task412, not falsely verified'
        row.update(status=status,existing_article=title,existing_revid=revision,source_photo_sha256=reading.get('source_sha256',reading.get('sha256')),evidence_status=evidence)
        (deferred if status=='created_preservation_queued' else completed if verified else pending).append(title)
(root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
fields=['product','checklist_number','side','rarity','label','language','alternate_image','status','existing_article','existing_revid','proposed_article','evidence_status']
with (root/'inventory.csv').open('w',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(manifest)
additional=root/'additional-existing-foils.json'
if additional.exists():
    for found in json.loads(additional.read_bytes()):
        row=next(r for r in manifest if r['proposed_article']==found['article'])
        if row['status']=='missing':row.update(status='existing_pending_integration_audit',existing_article=found['article'],existing_revid=found['revid'],evidence_status='Discovered after initial census; reuse existing article, independently read foil, full integration audit pending')
    (root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
    with (root/'inventory.csv').open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(manifest)
for packet in root.glob('batch*-new-packet.json'):
    for draft in json.loads(packet.read_bytes()):
        row=next((r for r in manifest if r['proposed_article']==draft['title']),None)
        if row and row['status'] in ['missing','draft_prepared_awaiting_preservation']:
            row.update(status='draft_prepared_awaiting_preservation',evidence_status='Independent physical foil reading and lint-clean shared Card draft; not published, original-image preservation and family citation completion pending')
(root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
with (root/'inventory.csv').open('w',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(manifest)
if (root/'publication-authorization.json').exists():
    for row in manifest:
        if row['status']=='existing_pending_preservation':row['status']='existing_preservation_queued'
    (root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
    with (root/'inventory.csv').open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(manifest)
counts=collections.Counter(r['status'] for r in manifest);per_product={p:dict(collections.Counter(r['status'] for r in manifest if r['product']==p)) for p in dict.fromkeys(r['product'] for r in manifest)}
report=dict(total=len(manifest),initially_missing=298,remaining_to_complete=298-len(completed)-len(deferred)-sum(r['status']=='existing_preservation_queued' for r in manifest),counts=dict(counts),per_product=per_product,verified_new_articles=completed,published_preservation_queued=deferred,published_pending_batch_verification=pending)
(root/'completion-progress.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report['counts']))
