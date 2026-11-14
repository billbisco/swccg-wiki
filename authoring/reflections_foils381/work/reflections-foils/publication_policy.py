"""Story381-only archive deferral explicitly authorized by Bill, 2026-11-14.

The standard linter is unchanged. ARCHIVE findings are retained in a ledger;
every other finding remains a hard failure. This does not verify any capture.
"""
import datetime,json
from pathlib import Path
from functools import lru_cache
from style_lint import lint as standard_lint
ROOT=Path(__file__).parent
AUTHORIZATION='Please don\'t let Wayback block this. Queue the preservation requests for later and proceed with publishing the remaining 217 foil articles and finishing the ten incomplete ones.'

@lru_cache(maxsize=1)
def allowed_titles():
    titles=set()
    for row in json.loads((ROOT/'manifest.json').read_bytes()):titles.update([row['proposed_article'],row['product']])
    for path in ROOT.glob('*-family-heads.json'):titles.update(json.loads(path.read_bytes()))
    for path in ROOT.glob('*-files-payload.json'):titles.update(r['title'] for r in json.loads(path.read_bytes()))
    return titles

def lint(text,title=None,cats=None):
    flags,count=standard_lint(text,title,cats)
    archive=[f for f in flags if f.startswith('ARCHIVE')]
    if not archive:return flags,count
    auth=json.loads((ROOT/'publication-authorization.json').read_bytes())
    assert auth['quote']==AUTHORIZATION and auth['archive_deferral'] is True
    base=title[5:] if title and title.startswith('Talk:') else title
    assert base in allowed_titles() or (title or '').startswith('File:Reflections'),('Outside authorized story381 publication scope',title)
    with (ROOT/'deferred-archive-findings.jsonl').open('a',encoding='utf8') as stream:
        stream.write(json.dumps(dict(title=title,at=datetime.datetime.now(datetime.timezone.utc).isoformat(),flags=archive,status='deferred by explicit user instruction; not verified'),ensure_ascii=False)+'\n')
    return [f for f in flags if not f.startswith('ARCHIVE')],count
