"""Read-only acceptance against actual deployed native pages; no routed pilot assets."""
import json,sys,time
from pathlib import Path
from urllib.parse import urlencode
from playwright.sync_api import sync_playwright
from PIL import Image
p=Path(__file__).parent
cases=json.loads((p/'query-cases.json').read_bytes())
manifest=json.loads((p/'build-manifest.json').read_bytes())
phase=sys.argv[1] if len(sys.argv)>1 else 'test'
urls={'wiki':'https://wiki.swccg.com/wiki/SWCCG_Wiki:Samples/Shared_search_pilot','scomp':'https://swccg.com/snapshots/review/shared-search-449/scomp.html',phase:f'https://{phase}.swccg.com/gemp-swccg/searchPilot.html'}
report={'phase':phase,'snapshotId':manifest['snapshotId'],'urls':urls,'results':[],'archive_requests':0}
with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='chrome',headless=True)
    context=browser.new_context(permissions=['clipboard-read','clipboard-write'])
    def forbid(route):
        raise AssertionError('Archive.org hold: forbidden request '+route.request.url)
    context.route('**/*archive.org/**',forbid)
    try:
        for kind,url in urls.items():
            page=context.new_page();errors=[]
            page.on('pageerror',lambda error:errors.append(str(error)))
            page.goto(url,wait_until='networkidle',timeout=60000)
            page.wait_for_function('window.SharedSearchPilot && window.SharedSearchPilot.last')
            assert page.evaluate('SharedSearchPilot.data.snapshotId')==manifest['snapshotId']
            actual=page.evaluate('cases=>cases.map(c=>{try{let r=SharedSearchPilot.search(c.query);return {ids:r.ids,counts:Object.fromEntries(r.records.map(x=>[x.id,x.matchedCount]))}}catch(e){return {error:e.message}}})',cases)
            for c,r in zip(cases,actual):
                if 'error' in c:assert c['error'] in r.get('error',''),(kind,c,r)
                else:
                    assert set(r['ids'])==set(c['ids']),(kind,c,r)
                    if 'counts' in c:assert r['counts']==c['counts'],(kind,c,r)
            root=page.locator('[data-swccg-search-pilot]')
            for width in [1280,390]:
                page.set_viewport_size({'width':width,'height':1000})
                root.get_by_role('button',name='Mentions JP',exact=True).click()
                assert page.locator('[data-result-id]').count()==3
                old=page.locator('[data-result-id]').evaluate_all('xs=>xs.map(x=>x.dataset.resultId)')
                root.get_by_label('Read card text as').select_option('readable')
                assert page.locator('[data-result-id]').evaluate_all('xs=>xs.map(x=>x.dataset.resultId)')==old
                root.get_by_role('button',name='Copy readable card text',exact=True).first.click()
                text=root.locator('.ssp-copy').inner_text();assert '[Jabba' in text and 'icon] icon' not in text
                root.get_by_label('Read card text as').select_option('symbols')
                assert root.locator('.ssp-symbol img').evaluate_all('xs=>xs.every(x=>x.complete&&x.naturalWidth>0)')
                assert root.evaluate('x=>x.scrollWidth<=x.clientWidth+1'),(kind,width,'root overflow')
                assert root.locator('input,select').evaluate_all('xs=>xs.filter(x=>!x.disabled).every(x=>x.labels.length>0)')
                if kind=='wiki':assert root.get_by_role('link',name='Search the whole Wiki').count()==1
                root.get_by_role('button',name='Copy search link',exact=True).click()
                shared=root.locator('.ssp-copy').inner_text();assert 'sp_symbol=jp' in shared or 'sp_symbol=jabbaspalace' in shared
                assert root.get_by_role('link',name='SCOMPLINK pilot',exact=True).get_attribute('href').endswith('sp_display=symbols')
                root.get_by_role('button',name='Two dots',exact=True).click();assert page.locator('[data-result-id]').count()==3
                root.get_by_role('button',name='Decks with Officer Evax',exact=True).click();assert page.locator('[data-result-id]').count()==2
                assert root.get_by_label('Set symbol').is_hidden()
                assert root.locator('.ssp-result').filter(has_text='1 matching main-deck copies').count()==2
                shot=p/f'live-{kind}-{width}.webp';png=shot.with_suffix('.png');root.screenshot(path=str(png));Image.open(png).save(shot,quality=86);png.unlink()
                root.get_by_role('button',name='Reset',exact=True).click();assert page.locator('[data-result-id]').count()==23
                root.get_by_label('Title or text',exact=True).fill('zzzz-no-card-match')
                root.get_by_role('button',name='Search',exact=True).click();assert page.locator('[data-result-id]').count()==0
                assert 'No matches in this pilot snapshot' in root.inner_text()
                root.get_by_role('button',name='Reset',exact=True).click()
            for query,expected in [({'mode':'decks','symbol':'JP'},'filters apply to Cards'),({'symbol':'bad-symbol'},'Unknown set symbol'),({'uniqueness':'bad-mark'},'Unknown uniqueness')]:
                page.goto(url+'?'+urlencode({'sp_'+k:v for k,v in query.items()}),wait_until='networkidle')
                assert expected in page.locator('[data-swccg-search-pilot] [role=alert]').inner_text()
                assert page.locator('[data-result-id]').count()==0
            assert not errors,(kind,errors)
            report['results'].append({'adapter':kind,'golden_cases':len(cases),'widths':[1280,390],'display_copy_share_labels_empty_invalid':'PASS','browser_errors':errors})
            page.close()
    finally:browser.close()
(p/f'live-{phase}-report.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps(report,indent=2))
