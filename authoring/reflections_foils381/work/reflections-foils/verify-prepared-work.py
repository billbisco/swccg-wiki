"""Verify draft evidence without certifying unpublished or unpreserved work."""
import collections,hashlib,json,sys
from pathlib import Path
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent
manifest=json.loads((root/'manifest.json').read_bytes());readings={};stages={}
for file in [root/'first-readings.json',*[root/('batch'+str(n)+'-readings.json') for n in range(2,32)],root/'batch12-existing-readings.json']:
    for row in json.loads(file.read_bytes()):
        assert row['article'] not in readings,row['article']
        readings[row['article']]=row;stages[row['article']]=file.name.replace('-readings.json','')
assert len(readings)==298,len(readings)
assert set(readings)=={r['proposed_article'] for r in manifest if r['status']!='existing'}
for title,row in readings.items():
    assert row['game_text'] and row['printed_title'] and row['icons'],title
    assert row['language']=='English' and row['finish']=='Foil',title
    assert hashlib.sha256((root/row['source_photo']).read_bytes()).hexdigest()==row['source_sha256'],title
drafts=[]
for n in range(9,32):
    stage='batch'+str(n);packet=json.loads((root/(stage+'-new-packet.json')).read_bytes())
    files={r['card_title']:r for r in json.loads((root/(stage+'-files-payload.json')).read_bytes())}
    for row in packet:
        title=row['title'];reading=readings[title];assert not lint(row['text'],title)[0],title
        card=next(t for t in mw.parse(row['text']).filter_templates(recursive=False) if str(t.name).strip()=='Card')
        assert not any(card.has(k) for k in ['gemp_id','card_uid']),title
        for k in ['printed_label','destiny','power','ability','armor','maneuver','hyperspeed','landspeed','deploy','forfeit','parsec','light_icons','dark_icons']:
            if k in reading:assert str(card.get(k).value).strip()==reading[k],(title,k)
        assert str(card.get('image').value).strip()==files[title]['name'],title
        assert files[title]['draft_only'] and not files[title].get('data'),title
        assert (root/(stage+'-new-sandbox-previews.json.gz')).exists(),title
        drafts.append(dict(title=title,stage=stage,source_sha256=reading['source_sha256'],style_flags=0,template_preview=True,published=False))
assert len(drafts)==217,len(drafts)
art=json.loads((root/'artwork-verification.json').read_bytes());assert len(art)==12 and all(r['verified'] for r in art)
for row in art:assert readings[row['article']]['source_sha256']==row['source_sha256']
report=dict(scope='Evidence/draft readiness only; does not certify publication, reciprocal links, preservation or visual QA of unpublished pages',physical_faces_read=len(readings),per_product=dict(collections.Counter(r['product'] for r in readings.values())),new_unsaved_drafts=len(drafts),verified_alternate_art_comparisons=12,drafts=drafts)
(root/'prepared-work-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
text='# Unpublished foil drafts — story381\n\n217 new articles remain unpublished. Each draft links to its exact physical reading and source hash. Images are draft identities, not uploaded or preserved assets. Rebuild from fresh family/set heads before publication.\n\n| Article | Stage | Physical reading | Draft |\n|---|---|---|---|\n'
for row in drafts:
    stage=row['stage'];text+='| '+row['title']+' | '+stage+' | ['+stage+'-readings.json]('+stage+'-readings.json) | ['+stage+'-new-packet.json]('+stage+'-new-packet.json) |\n'
(root/'draft-index.md').write_text(text,encoding='utf8')
print('298 unique faces, exact original hashes; 217 unsaved drafts/field values/style/previews; 12 artwork comparisons verified')
