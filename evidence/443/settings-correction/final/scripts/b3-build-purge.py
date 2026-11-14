from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'batch2-purge.py').read_text(encoding='utf-8').replace('from b2common import *','from b3common import *').replace("titles=[r['title']for r in read('plan.json')]","titles=list(read('source-manifest.json')['pages'])+[r['title']for r in read('plan.json')if r['title']not in read('source-manifest.json')['pages']]")
(P/'b3-purge.py').write_bytes(s.encode())
