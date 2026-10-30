import sys,re,html
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8',errors='replace').read()
    s=re.sub(r'data:[^"\')\s]+','',s)
    s=re.sub(r'(?is)<(script|style|svg).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</h\d>|</li>|</tr>','\n',s)
    s=re.sub(r'<[^>]+>','',s); s=html.unescape(s)
    s=re.sub(r'\n\s*\n+','\n',s)
    open(f.replace('.html','.txt'),'w').write(s)
    print(f,len(s))
