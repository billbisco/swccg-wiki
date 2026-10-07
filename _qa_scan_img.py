#!/usr/bin/env python3
import json
import re
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
page = "2014 Worlds Day 3 Matthew Harrison-Trainor LS Communing"
q = urllib.parse.urlencode({"action": "parse", "page": page, "prop": "text", "format": "json"})
req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "SWCCGWikiQA/1.0"})
html = json.loads(urllib.request.urlopen(req, timeout=60).read().decode())["parse"]["text"]["*"]
idx = html.rfind('id="Scan"')
print(html[idx : idx + 1400])
imgs = re.findall(r'src="(/[^"]*p05[^"]+)"', html)
print("IMGS", imgs)
for src in imgs:
    url = "https://wiki.swccg.com" + src
    r = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "SWCCGWikiQA/1.0"})
    with urllib.request.urlopen(r, timeout=30) as resp:
        print("HEAD", resp.status, url, resp.headers.get("Content-Type"), resp.headers.get("Content-Length"))
