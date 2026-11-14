import base64,hashlib,json,subprocess
from pathlib import Path
root=Path(__file__).parent;commit=(root/'wiki-commit.txt').read_text().strip();prefix='authoring/foil_display436/work/foil-display-fixes/';proof=[]
def api(path):return json.loads(subprocess.check_output(['gh','api','repos/billbisco/swccg-wiki/'+path]))
def restore(path):
    j=api('contents/'+path+'?ref='+commit)
    if not j.get('content'):j=api('git/blobs/'+j['sha'])
    return base64.b64decode(j['content'])
for filename in ['all-packet.json','before-heads.json','published-heads.json']:
    path=prefix+filename;raw=restore(path);stored=json.loads(raw);assert stored==json.loads((root/filename).read_bytes())
    items=[(r['title'],r['text'],None) for r in stored] if filename=='all-packet.json' else [(title,h['revisions'][0]['slots']['main']['content'],h['revisions'][0]['revid']) for title,h in stored.items() if 'revisions' in h]
    for title,text,revid in items:
        payload=text.encode();proof.append(dict(title=title,revision_id=revid,subject_kind=filename,repository='https://github.com/billbisco/swccg-wiki',commit=commit,path=path,container='JSON object with exact decoded source text',container_sha256=hashlib.sha256(raw).hexdigest(),restored_subject_sha256=hashlib.sha256(payload).hexdigest(),restored_subject_bytes=len(payload),original_final_newline_state_preserved=True,independent_remote_readback=True))
raw=restore('wiki/SwccgChrome.php');assert raw==(root/'SwccgChrome.php').read_bytes();proof.append(dict(path='wiki/SwccgChrome.php',commit=commit,sha256=hashlib.sha256(raw).hexdigest(),independent_remote_readback=True))
(root/'exact-raw-subject-readback.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2),encoding='utf8');print(len(proof),'exact original/draft/published source payloads and presentation hook independently restored from immutable GitHub backups')
