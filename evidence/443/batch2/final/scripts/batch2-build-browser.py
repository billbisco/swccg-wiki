from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'browser-qa/prove.cjs').read_text(encoding='utf-8')
s=s.replace("require('playwright-core')","require('./browser-qa/node_modules/playwright-core')").replace("path.resolve(__dirname,'..')","path.resolve(__dirname,'batch2')")
start=s.index('const pages=');end=s.index(';',start)
s=s[:start]+"const pages=Object.fromEntries(require('./batch2/inventory.json').map(r=>[r.key,r.canonical.replaceAll(' ','_')]))"+s[end:]
s=s.replace('headless-browser-checks.json','browser-checks.json')
(P/'batch2-browser.cjs').write_bytes(s.encode())
