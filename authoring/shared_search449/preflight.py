import json,subprocess,hashlib
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from PIL import Image
p=Path(__file__).parent;m=json.loads((p/'build-manifest.json').read_bytes());product=p/'product';rows=json.loads((p/'wiki-packet.json').read_bytes())
import sys
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
for row in rows:
    flags=lint(row['text'],row['title'])[0];assert not flags,flags
    j=requests.post('https://wiki.swccg.com/api.php',data=dict(action='parse',format='json',formatversion=2,title=row['title'],text=row['text'],prop='text|images|links'),timeout=60).json();assert 'error' not in j,j
    soup=BeautifulSoup(j['parse']['text'],'html.parser');assert soup.select_one('[data-swccg-search-pilot="wiki"]') and not soup.select('.mw-ext-cite-error,.error')
    (p/'wiki-preview.json').write_text(json.dumps(j,ensure_ascii=False,indent=2),encoding='utf8')
with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='chrome',headless=True)
    try:
        for context in ['wiki','gemp','scomp']:
            page=browser.new_page(viewport=dict(width=1280,height=1000));errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
            page.route('https://wiki.swccg.com/chrome/'+m['js'],lambda route:route.fulfill(body=(product/m['js']).read_bytes(),content_type='application/javascript'))
            page.route('https://wiki.swccg.com/chrome/'+m['css'],lambda route:route.fulfill(body=(product/m['css']).read_bytes(),content_type='text/css'))
            document=(product/'scomp.html').read_text(encoding='utf8').replace('data-swccg-search-pilot="scomp"','data-swccg-search-pilot="'+context+'"')
            page.set_content(document,wait_until='networkidle');page.wait_for_function('window.SharedSearchPilot && window.SharedSearchPilot.last')
            assert page.locator('[data-result-id]').count()==23,context
            assert page.locator('.ssp-symbol img').evaluate_all('xs=>xs.every(x=>x.complete&&x.naturalWidth)'),context
            page.get_by_role('button',name='Mentions JP',exact=True).click();assert page.locator('[data-result-id]').count()==3,context
            page.get_by_role('button',name='Decks with Officer Evax',exact=True).click();assert page.locator('[data-result-id]').count()==2,context
            assert not errors,(context,errors)
            png=p/('preflight-'+context+'.png');page.screenshot(path=str(png));Image.open(png).save(png.with_suffix('.webp'),quality=83);png.unlink();page.close()
    finally:browser.close()
report=dict(wiki_strict_lint_flags=[],wiki_parser_errors=0,root_preserved=True,local_native_browser_adapters=['wiki','gemp','scomp'],initial_cards=23,jp_reference_results=3,officer_evax_decks=2)
(p/'preflight-report.json').write_text(json.dumps(report,indent=2),encoding='utf8');print('Strict Wiki lint/parser and all three browser adapters PASS')
