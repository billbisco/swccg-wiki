import json,re,sys
from pathlib import Path
sys.path.insert(0,'work/wiki-tools');from style_lint import lint,URL_RX
root=Path(__file__).parent;stage=sys.argv[1]
rows=json.loads((root/(stage+'-family-packet.json')).read_bytes());report=[];urls=set()
for row in rows:
    flags=lint(row['text'],row['title'])[0]
    report.append(dict(title=row['title'],lint=flags))
    for flag in flags:
        if flag.startswith('ARCHIVE'):
            match=re.search(r'https?://\S+',flag)
            if match:urls.add(match[0])
(root/(stage+'-inherited-lint.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
(root/(stage+'-citation-urls.json')).write_text(json.dumps(sorted(urls),indent=2),encoding='utf8')
print(sum(bool(r['lint']) for r in report),'pages have inherited flags;',len(urls),'citation URLs')
