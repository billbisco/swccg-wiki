#!/usr/bin/env python3
"""Turn a saved web page into ONE self-contained HTML file that displays anywhere
(static host -> Wayback Machine).

    python make_snapshot.py page.html --url https://forum.example.org/viewtopic.php?t=1 -o out.html
           [--fetcher direct|wayback|auto] [--cookie-file cookies.txt] [--user-agent UA]

- CSS: <link rel=stylesheet> fetched and inlined; @import followed; url(...) -> data: URIs
- images (img, input[type=image], inline style url()) -> data: URIs; srcset / lazy attrs dropped
- <script>, <noscript>, <iframe>, on* handlers, preload/manifest/app links removed
- links absolute; phpBB sid= stripped
- visible provenance banner: live URL + capture time
Asset fetch order (auto): direct HTTP (with optional cookies/UA from FlareSolverr),
then the Wayback Machine raw capture (id_) of the exact URL, then without its query string.
"""
import argparse, base64, datetime, mimetypes, re, sys, urllib.parse
import requests
from bs4 import BeautifulSoup

SID = re.compile(r'([?&])sid=[0-9a-f]+&?')

def clean(u):
    u = SID.sub(r'\1', u)
    return u[:-1] if u.endswith(('?', '&')) else u

class Fetcher:
    def __init__(self, mode, ua, cookie_file):
        self.mode, self.cache, self.log, self.rebase = mode, {}, [], {}
        self.s = requests.Session()
        self.s.headers['User-Agent'] = ua
        if cookie_file:
            for line in open(cookie_file, encoding='utf-8'):
                if '=' in line and not line.startswith('#'):
                    k, v = line.strip().split('=', 1)
                    self.s.cookies.set(k, v)

    def _get(self, url):
        try:
            r = self.s.get(url, timeout=60)
            if r.ok and 'cf-mitigated' not in r.headers and b'Just a moment...' not in r.content[:3000]:
                return r.content, r.headers.get('content-type', '')
        except requests.RequestException:
            pass
        return None

    def get(self, url):
        if url in self.cache:
            return self.cache[url]
        got, how = None, None
        if self.mode in ('direct', 'auto'):
            got, how = self._get(url), 'direct'
        if not got and 'font-awesome' in url and url.split('?')[0].endswith('font-awesome.min.css'):
            # phpBB 3.x bundles Font Awesome 4.7; use the identical public copy if the site's is unreachable
            got = self._get('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css')
            if got:
                how = 'cdnjs FA 4.7.0'; url_base = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/'
                self.rebase[url] = url_base
        if not got and self.mode in ('wayback', 'auto'):
            for cand in (url, url.split('?')[0]):
                got = self._get('https://web.archive.org/web/2026id_/' + cand)
                if got:
                    how = 'wayback' + ('' if cand == url else ' (no query)')
                    break
        self.log.append(f"{'OK ' + how if got else 'MISSING'}  {url}")
        self.cache[url] = got
        return got

def data_uri(fetch, url):
    got = fetch.get(url)
    if not got:
        return url
    body, ctype = got
    ctype = (ctype.split(';')[0].strip() or mimetypes.guess_type(url.split('?')[0])[0]
             or 'application/octet-stream')
    if ctype in ('text/html', 'text/plain') and re.search(r'\.(woff2?|ttf|eot|otf)(\?|$)', url):
        ctype = mimetypes.guess_type(url.split('?')[0])[0] or 'font/woff'
    return f'data:{ctype};base64,' + base64.b64encode(body).decode()

URL_RE = re.compile(r'url\(\s*([\'"]?)([^\'")]+)\1\s*\)')
IMPORT_RE = re.compile(r'@import\s+(?:url\()?\s*[\'"]?([^\'")\s;]+)[\'"]?\s*\)?[^;]*;')

def inline_css(fetch, css, base, depth=0):
    def imp(m):
        if depth > 3:
            return ''
        u = urllib.parse.urljoin(base, m.group(1))
        got = fetch.get(u)
        return inline_css(fetch, got[0].decode('utf-8', 'replace'), u, depth + 1) if got else ''
    css = IMPORT_RE.sub(imp, css)
    def rep(m):
        u = m.group(2).strip()
        if u.startswith(('data:', '#')):
            return m.group(0)
        return f'url("{data_uri(fetch, urllib.parse.urljoin(base, u))}")'
    return URL_RE.sub(rep, css)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('html'); ap.add_argument('--url', required=True); ap.add_argument('-o', required=True)
    ap.add_argument('--fetcher', default='auto', choices=['direct', 'wayback', 'auto'])
    ap.add_argument('--cookie-file'); ap.add_argument('--user-agent', default='Mozilla/5.0 (swccg-wiki snapshot)')
    ap.add_argument('--captured', help='ISO time the page was captured (default now)')
    a = ap.parse_args()
    live = clean(a.url)
    fetch = Fetcher(a.fetcher, a.user_agent, a.cookie_file)
    soup = BeautifulSoup(open(a.html, encoding='utf-8', errors='replace').read(), 'html.parser')

    for t in soup(['script', 'noscript', 'iframe', 'object', 'embed', 'template', 'base']):
        t.decompose()
    for m in soup.find_all('meta'):
        if m.get('http-equiv', '').lower() == 'refresh' or m.get('name') == 'apple-itunes-app' or m.get('charset'):
            m.decompose()
    # cookie-consent / GDPR popups and app banners are page chrome, not content
    for t in soup.select('.cc-window, .cc-banner, .cc-revoke, #cookieConsent, .cookie-notice, #cookie-notice, .smartbanner'):
        t.decompose()
    for t in soup.find_all(True):
        for k in [k for k in t.attrs if k.lower().startswith('on')]:
            del t[k]
    for l in soup.find_all('link'):
        rel = [r.lower() for r in (l.get('rel') or [])]
        if 'stylesheet' not in rel:
            l.decompose(); continue
        href = urllib.parse.urljoin(a.url, l.get('href', ''))
        got = fetch.get(href)
        st = soup.new_tag('style')
        if l.get('media'):
            st['media'] = l['media']
        st.string = f'/* inlined from {href} */\n' + (inline_css(fetch, got[0].decode('utf-8', 'replace'), fetch.rebase.get(href, href)) if got else '')
        l.replace_with(st)
    for st in soup.find_all('style'):
        if st.string and not st.string.startswith('/* inlined'):
            st.string = inline_css(fetch, st.string, a.url)
    for t in soup.find_all(style=re.compile('url\\(')):
        t['style'] = inline_css(fetch, t['style'], a.url)
    for im in soup.find_all(['img', 'input']):
        if im.name == 'input' and im.get('type') != 'image':
            continue
        src = im.get('data-src') or im.get('src')
        if src:
            im['src'] = data_uri(fetch, urllib.parse.urljoin(a.url, src))
        for k in ('srcset', 'data-src', 'data-srcset', 'loading', 'sizes'):
            im.attrs.pop(k, None)
    for s in soup.find_all('source'):
        s.decompose()
    for x in soup.find_all(['a', 'area'], href=True):
        h = x['href']
        if h.lower().startswith('javascript:'):
            del x['href']
        elif not h.startswith(('#', 'mailto:', 'tel:')):
            x['href'] = clean(urllib.parse.urljoin(a.url, h))
    for f in soup.find_all('form'):
        f['action'] = clean(urllib.parse.urljoin(a.url, f.get('action', '')))

    head = soup.head or soup.new_tag('head')
    if not soup.head:
        soup.html.insert(0, head)
    head.insert(0, soup.new_tag('meta', charset='utf-8'))
    when = a.captured or datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    banner = BeautifulSoup(
        '<div style="all:initial;display:block;box-sizing:border-box;width:100%;padding:8px 12px;'
        'background:#fff8d6;border-bottom:2px solid #c9a400;font:14px/1.4 Arial,sans-serif;color:#222">'
        f'<b>Preserved snapshot</b> of <a style="color:#0645ad" href="{live}">{live}</a>, captured {when} '
        'for <a style="color:#0645ad" href="https://wiki.swccg.com/">wiki.swccg.com</a>. '
        'Scripts removed; styles and images embedded.</div>', 'html.parser')
    soup.body.insert(0, banner)
    out = f'<!DOCTYPE html>\n<!-- snapshot-of: {live} captured: {when} -->\n' + str(soup)
    open(a.o, 'w', encoding='utf-8').write(out)
    print('\n'.join(fetch.log), file=sys.stderr)
    print(f'wrote {a.o} ({len(out.encode()):,} bytes); missing assets: '
          f'{sum(1 for l in fetch.log if l.startswith("MISSING"))}', file=sys.stderr)

if __name__ == '__main__':
    main()
