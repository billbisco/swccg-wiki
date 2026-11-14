import base64,json,subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
p=Path(__file__).parent;tree=json.loads((p/'cardmaker-tree.json').read_bytes());(p/'cardmaker').mkdir(exist_ok=True)
paths=[x for x in tree['tree'] if x['type']=='blob' and (x['path'] in ['STANDARD.md','CLAUDE.md','AGENTS.md','CODEX.md','assets/icons/SET-ICONS-PROVENANCE.md','assets/icons/SET-ICONS-PROVENANCE.json','tools/set_spheres/cut_set_spheres.py','tools/set_spheres/sources.json','cut_set_icon.py'] or x['path'].startswith('assets/icons/set-') and ('decipher' in x['path'] or '-pc.' in x['path']))]
def fetch(x):
    j=json.loads(subprocess.check_output(['gh','api','repos/billbisco/swccg-cardmaker/git/blobs/'+x['sha']]));raw=base64.b64decode(j['content']);f=p/'cardmaker'/x['path'];f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(raw);return x['path'],len(raw)
with ThreadPoolExecutor(max_workers=3) as pool:out=list(pool.map(fetch,paths))
(p/'cardmaker-import.json').write_text(json.dumps(dict(commit_tree=tree['sha'],files=out),indent=2),encoding='utf8');print('Downloaded',len(out),'existing assets, provenance and source scripts; no assets generated')
