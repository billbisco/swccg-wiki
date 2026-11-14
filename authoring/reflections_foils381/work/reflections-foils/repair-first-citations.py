import json,re,sys
from pathlib import Path
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent
latest={r['url']:r for r in map(json.loads,(root/'old-citation-archives.jsonl').read_text().splitlines())}
fallback=json.loads((root/'old-primary-preservation.json').read_bytes());assert fallback['verified']
for r in json.loads((root/'old-primary-manifest.json').read_bytes()):
    latest[r['url']]=dict(url=r['url'],capture=fallback['capture'],status='verified',preserved_url=r.get('api_source',r['url']),method='Selected primary source data and original image in byte-verified snapshot',snapshot_sha256=fallback['sha256'])
assert all(r['status']=='verified' for r in latest.values())
(root/'old-citation-final.json').write_text(json.dumps(latest,ensure_ascii=False,indent=2),encoding='utf8')
def fix(text):
    def ref(m):
        old=m[0];add=[]
        for url,r in latest.items():
            if url in old and r['capture'] not in old:add.append('Preserved copy: ['+r['capture']+' '+('Original image at the cited commit' if 'raw.githubusercontent.com' in r.get('preserved_url','') else 'Internet Archive primary-source copy')+'].')
        return old[:-6].rstrip()+' '+ ' '.join(dict.fromkeys(add))+'</ref>' if add else old
    text=re.sub(r'<ref\b(?![^>]*?/\s*>)[^>]*>.*?</ref>',ref,text,flags=re.S)
    out=[]
    for line in text.splitlines():
        add=[]
        for url,r in latest.items():
            if url in line and r['capture'] not in line:add.append('Preserved copy: ['+r['capture']+' Internet Archive primary-source copy].')
        out.append(line+(' '+ ' '.join(dict.fromkeys(add)) if add else ''))
    return '\n'.join(out)+'\n'
rows=json.loads((root/'first-family-packet.json').read_bytes());report=[]
for row in rows:
    old=row['text'];row['text']=fix(old)
    row['summary']='Link verified Reflections foil; preserve existing family citations (#381)' if old!=row['text'] else row['summary']
    flags=lint(row['text'],row['title'])[0];report.append(dict(title=row['title'],lint=flags,citation_repairs=old!=row['text']));assert not flags,(row['title'],flags)
(root/'first-family-final-packet.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
(root/'first-family-final-lint.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'family drafts lint 0; inherited citations preserved')
