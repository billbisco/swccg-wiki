import collections
import csv
import gzip
import json
from pathlib import Path
import re
import sys

from bs4 import BeautifulSoup,Comment
root=Path(__file__).parent
mode=sys.argv[1]
before=json.load(gzip.open(root/'before-renders.json.gz','rt',encoding='utf8'))
after=json.load(gzip.open(root/(mode+'-renders.json.gz'),'rt',encoding='utf8'))
reference_repairs={r['title'] for r in json.loads((root/'reference-repairs.json').read_bytes())}
def soup(text):
    node=BeautifulSoup(text,'html.parser')
    for comment in node.find_all(string=lambda x:isinstance(x,Comment)):comment.extract()
    for tag in node.select('style,script,.mw-editsection,#toc,.toc,.mw-cite-backlink,sup.reference,.mw-ext-cite-error'):tag.decompose()
    return node
def tokens(text):return collections.Counter(re.findall(r'\w+',soup(text).get_text(' ',strip=True)))
report=[]
if mode in ['english-sandbox','english-production']:
    if (root/'english-before-renders.json.gz').exists():before=json.load(gzip.open(root/'english-before-renders.json.gz','rt',encoding='utf8'))
    for title,new in after.items():
        a=str(soup(before[title]['text']));b=str(soup(new['text']))
        equal=a==b
        report.append(dict(title=title,identical=equal,before_chars=len(a),after_chars=len(b)))
        if not equal:
            import difflib
            (root/('english-diff-'+str(len(report))+'.diff')).write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True))),encoding='utf8')
    path=root/(mode+'-report.json')
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print(sum(r['identical'] for r in report),'of',len(report),'English rendered DOMs identical')
else:
    for title,new in after.items():
        old=before[title]
        old_links={r['title'] for r in old['links']};new_links={r['title'] for r in new['links']}
        oldcats={r['category'] for r in old['categories']};newcats={r['category'] for r in new['categories']}
        missing=tokens(old['text'])-tokens(new['text'])
        # The simple tables used their article title as a caption; the shared caption is Info.
        # The title remains in the lead and the new Title field. Report all other deficits.
        meaningful_missing={token:count for token,count in missing.items()}
        errors=soup(new['text']).select('.mw-ext-cite-error')
        raw_errors=BeautifulSoup(new['text'],'html.parser').select('.mw-ext-cite-error')
        entry=dict(title=title,missing_words=meaningful_missing,missing_links=sorted(old_links-new_links),missing_images=sorted(set(old['images'])-set(new['images'])),missing_categories=sorted(oldcats-newcats),added_categories=sorted(newcats-oldcats),cite_errors=[e.get_text(' ',strip=True) for e in raw_errors])
        entry.update(added_words=dict(tokens(new['text'])-tokens(old['text'])),added_links=sorted(new_links-old_links),added_images=sorted(set(new['images'])-set(old['images'])))
        expected_removed={'Pages_with_reference_errors'} if title in reference_repairs and not raw_errors else set()
        entry['allowed_category_changes']=['Remove maintenance category after restoring the existing photo reference'] if expected_removed & oldcats else []
        entry['unexpected_category_changes']=sorted((oldcats-newcats)-expected_removed)+entry['added_categories']
        entry['pass']=not any(entry[k] for k in ['missing_words','missing_links','missing_images','unexpected_category_changes','cite_errors'])
        report.append(entry)
    (root/(mode+'-conservation.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    failed=[r for r in report if not r['pass']]
    print(len(report)-len(failed),'of',len(report),'conservation checks pass')
    for entry in failed[:15]:print(json.dumps(entry,ensure_ascii=False))
