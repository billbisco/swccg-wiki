import csv,gzip,html,json,re,sys
from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).parent
sys.path[:0]=[str(root/'vendor')]
import mwparserfromhell as mw
details=json.loads((root/'conversion-details.json').read_bytes())
before=json.load(gzip.open(root/'before-renders.json.gz','rt',encoding='utf8'))
after=json.load(gzip.open(root/'drafts-renders.json.gz','rt',encoding='utf8'))
def visible(value):
    value=re.sub(r'<ref\b(?![^>]*?/\s*>)[^>]*>.*?</ref>|<ref[^>]*/>','',value,flags=re.S)
    # No Unicode normalization: retain Japanese punctuation, width and characters.
    return ''.join(html.unescape(mw.parse(value).strip_code()).split())
report=[]
for item in details:
    title=item['title'];params=item['params'];sections=item['source_sections']
    checks={}
    for section,param in [('Title','printed_title'),('Card Text','printed_game_text' if params['language']=='ja' else 'game_text'),('Lore','printed_lore' if params['language']=='ja' else 'lore'),('Translation of Japanese Text','translation'),('Comparison with the English printing','translation_note')]:
        if section in sections:checks[param]=visible(sections[section])==visible(params[param])
    def urls(text):
        return {a['href'] for a in BeautifulSoup(text,'html.parser').select('a.external[href]')}
    missing_urls=sorted(urls(before[title]['text'])-urls(after[title]['text']))
    refs_before=BeautifulSoup(before[title]['text'],'html.parser').select('.references li')
    refs_after=BeautifulSoup(after[title]['text'],'html.parser').select('.references li')
    def reftext(node):
        for el in node.select('.mw-cite-backlink,.mw-ext-cite-error'):el.decompose()
        return ''.join(node.get_text().split())
    oldrefs=[reftext(x) for x in refs_before];newrefs=[reftext(x) for x in refs_after]
    missing_refs=[x for x in oldrefs if x and x not in newrefs]
    report.append(dict(title=title,native_translation_checks=checks,missing_external_urls=missing_urls,missing_reference_text=missing_refs,passed=all(checks.values()) and not missing_urls and not missing_refs))
(root/'fidelity-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
with (root/'content-diff.csv').open('w',encoding='utf8',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['title','native_translation_exact','external_urls_preserved','references_preserved','pass']);writer.writeheader()
    for row in report:writer.writerow(dict(title=row['title'],native_translation_exact=all(row['native_translation_checks'].values()),external_urls_preserved=not row['missing_external_urls'],references_preserved=not row['missing_reference_text'],**{'pass':row['passed']}))
with (root/'categories-before-after.csv').open('w',encoding='utf8',newline='') as f:
    writer=csv.writer(f);writer.writerow(['title','before','after','reason'])
    for row in json.loads((root/'drafts-conservation.json').read_bytes()):
        t=row['title'];writer.writerow([t,'; '.join(sorted(x['category'] for x in before[t]['categories'])),'; '.join(sorted(x['category'] for x in after[t]['categories'])),'; '.join(row['allowed_category_changes'])])
failed=[x for x in report if not x['passed']]
print(len(report)-len(failed),'/',len(report),'exact native/translation and source conservation checks pass')
for row in failed[:10]:print(json.dumps(row,ensure_ascii=False))
