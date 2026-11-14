"""Publish one complete reviewed batch; stop for visual inspection afterwards."""
import datetime,hashlib,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).parent;stage=sys.argv[1];assert stage.startswith('batch') and 8<=int(stage[5:])<=31
env=dict(os.environ,PYTHONIOENCODING='utf8')
def run(script,*args):
    print('STEP',stage,script,flush=True)
    subprocess.run([sys.executable,str(root/script),*args],env=env,check=True)
if stage!='batch8':run('upload-batch.py',stage)
run('fetch-families.py',stage)
run('build-batch.py',stage)
run('build-shared-nav.py',stage)
run('scan-batch-citations.py',stage)
run('prepare-deferred-family.py',stage)
run('queue-preservation.py',stage)
if stage=='batch8':
    import requests
    sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
    rows=json.loads((root/(stage+'-new-packet.json')).read_bytes())
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(r['title'] for r in rows),prop='revisions',rvprop='ids|content',rvslots='main'),timeout=60);response.raise_for_status();heads={p['title']:p for p in response.json()['query']['pages']}
    for row in rows:
        rev=heads[row['title']]['revisions'][0];old=rev['slots']['main']['content'];code=mw.parse(old);card=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card');draft=next(t for t in mw.parse(row['text']).filter_templates(recursive=False) if str(t.name).strip()=='Card')
        card.get('versions').value=draft.get('versions').value
        row.update(text=str(code),new=False,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Complete foil family navigation, retaining printed fields and original image (#381)')
    (root/(stage+'-new-packet.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
run('build-batch-set-talk.py',stage)
for kind in ['new','family-final']:
    run('preview.py',stage+'-'+kind,'--sandbox')
for kind in ['new','family-final','shared-nav','set']:
    run('publish.py',stage+'-'+kind)
if stage!='batch8':run('publish.py',stage+'-talk')
run('verify-batch.py',stage)
run('capture-batch.py',stage)
marker=dict(stage=stage,at=datetime.datetime.now(datetime.timezone.utc).isoformat(),publication_verified=True,original_images_sha_checked=True,archive_deferred=True,preservation_task=412,visual_inspection='screenshots captured; inspect before accepting this stage',authorization='publication-authorization.json')
(root/(stage+'-publication-verification.json')).write_text(json.dumps(marker,indent=2),encoding='utf8')
run('update-inventory-progress.py')
run('update-publication-report.py')
print('READY_FOR_VISUAL_INSPECTION',stage,flush=True)
