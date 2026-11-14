"""Verify exact draft/live Wiki source via an independent immutable GitHub read."""
import base64,hashlib,json,subprocess
from pathlib import Path
root=Path(__file__).parent;commit=(root/'wiki-commit.txt').read_text().strip();prefix='authoring/reflections_foil_tables430/work/reflections-foil-tables/'
expected={prefix+p.name:p.read_bytes().replace(b'\r\n',b'\n').rstrip()+b'\n' for p in root.glob('draft-*.wiki')}
if (root/'published-heads.json').exists():
    index=dict(line.split('\t',1) for line in subprocess.check_output(['git','-C','work/wiki-source','show',commit+':pages/INDEX.tsv']).decode().splitlines())
    for title,h in json.loads((root/'published-heads.json').read_bytes()).items():expected[index[title]]=(h['revisions'][0]['slots']['main']['content'].rstrip()+'\n').encode()
proof=[]
for path,data in expected.items():
    j=json.loads(subprocess.check_output(['gh','api','repos/billbisco/swccg-wiki/contents/'+path+'?ref='+commit]));raw=base64.b64decode(j['content']);assert raw==data,path
    proof.append(dict(repository='https://github.com/billbisco/swccg-wiki',commit=commit,path=path,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),independent_readback_verified=True))
(root/('live-backup-readback.json' if (root/'published-heads.json').exists() else 'draft-backup-readback.json')).write_text(json.dumps(proof,ensure_ascii=False,indent=2),encoding='utf8');print(len(proof),'exact immutable remote Wiki drafts/revisions independently restored and matched')
