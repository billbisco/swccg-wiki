from pilotlib import *
B=P/'batch2';H=Path('C:/Users/gythe/Documents/Codex/2026-11-06/implement-legacy-lane-e-block-4/work/holotable/preservation-repo/historical-recovery/419')
rows=json.loads((B/'inventory.json').read_bytes());cdx=json.loads((H/'metadata/archive-original-virtual-cdx.json').read_bytes())
for r in rows:
 d=(B/'assets'/f'{r["number"]:02}-historical.gif').read_bytes();digest=base64.b32encode(hashlib.sha1(d).digest()).decode();matches=[x for x in cdx if x[5]==digest];print(r['number'],digest,[x[2]for x in matches])
print('RECONCILIATION',str(json.loads((H/'metadata/archive-digest-reconciliation.json').read_bytes()))[:2300])
