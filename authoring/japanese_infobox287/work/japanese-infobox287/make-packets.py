import hashlib
import json
from pathlib import Path
root=Path(__file__).parent
heads=json.loads((root/'heads-before.json').read_bytes())
title='Template:Card/sandbox';before=heads[title]['revisions'][0]
row=dict(title=title,text=(root/'template-draft.wiki').read_text(encoding='utf8'),before_revid=before['revid'],before_sha256=hashlib.sha256(before['slots']['main']['content'].encode()).hexdigest(),summary='Sandbox generic printing-language fields and conservative metadata preservation (#287)',section=0)
(root/'sandbox-packet.json').write_text(json.dumps([row],ensure_ascii=False,indent=2),encoding='utf8')
