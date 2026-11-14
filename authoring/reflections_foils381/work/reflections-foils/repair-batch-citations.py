import json,re,sys
from pathlib import Path
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent;stage=sys.argv[1]
latest={r['url']:r for r in map(json.loads,(root/(stage+'-citation-captures.jsonl')).read_text().splitlines())}
if (root/(stage+'-primary-preservation.json')).exists():
    preserved=json.loads((root/(stage+'-primary-preservation.json')).read_bytes());assert preserved['verified']
    for r in json.loads((root/(stage+'-primary-manifest.json')).read_bytes()):
        latest[r['url']]=dict(r,capture=preserved['capture'],status='verified',method='Original resource / selected primary source fields in verified snapshot',snapshot_sha256=preserved['sha256'])
assert all(r['status']=='verified' for r in latest.values()),[r for r in latest.values() if r['status']!='verified']
corrections={r['url']:r['preserved_url'] for r in latest.values() if r.get('correction')}
def fix(text):
    # Correct broken GIF links to the PNG actually added at the exact cited commit.
    for old,new in corrections.items():text=text.replace(old,new)
    def additions(s):
        return list(dict.fromkeys('Preserved copy: ['+r['capture']+' Internet Archive primary-source copy].' for u,r in latest.items() if (corrections.get(u,u) in s) and r['capture'] not in s))
    def ref(m):
        s=m[0];add=additions(s)
        return s[:-6].rstrip()+' '+' '.join(add)+'</ref>' if add else s
    parts=re.split(r'(<ref\b[^>]*>.*?</ref>|<ref\b[^>]*/\s*>)',text,flags=re.S)
    result=[]
    for part in parts:
        if part.startswith('<ref'):
            add=additions(part)
            result.append(part[:-6].rstrip()+' '+' '.join(add)+'</ref>' if add and part.endswith('</ref>') else part)
        else:
            lines=[]
            for line in part.splitlines(keepends=True):
                ending='\n' if line.endswith('\n') else '';body=line[:-1] if ending else line;add=additions(body)
                lines.append(body+(' '+' '.join(add) if add else '')+ending)
            result.append(''.join(lines))
    return ''.join(result)
rows=json.loads((root/(stage+'-family-packet.json')).read_bytes());report=[];multi=[]
for row in rows:
    original=row['text'];row['text']=fix(original);flags=lint(row['text'],row['title'])[0];assert not flags,(row['title'],flags)
    if row['text']!=original:row['summary']='Link verified foil and preserve inherited primary-source citations (#381)'
    if re.search(r'^==[^=]',row['text'],re.M):
        row['section']=None;row['atomic_reason']='Navigation and inherited citation repairs span existing sections; exact revision, hash and timestamp guards preserve other content';multi.append(row['title'])
    report.append(dict(title=row['title'],lint=flags,citation_repairs=row['text']!=original))
for suffix,data in [('family-final-packet',rows),('family-final-lint',report),('citation-final',latest),('citation-corrections',corrections),('section-scope',multi)]:
    (root/(stage+'-'+suffix+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'family drafts lint 0;',len(multi),'guarded multiple-section repairs;',len(corrections),'broken source URLs corrected')
