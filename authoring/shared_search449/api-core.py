import argparse
import base64
import gzip
import http.cookiejar
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
import shlex

API = "https://wiki.swccg.com/api.php"
BOT = "Memory Core ChatGPT"

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Unexpected API redirect")

opener = urllib.request.build_opener(NoRedirect(), urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

def call(write=False, **params):
    data = urllib.parse.urlencode({"format":"json","formatversion":2,**params}).encode()
    request = urllib.request.Request(API if write else API+"?"+data.decode(), data=data if write else None,
        headers={"User-Agent":"SWCCG Wiki scoped title repair (Memory Core ChatGPT)"})
    for attempt in range(6):
        with opener.open(request, timeout=45) as response:
            payload = json.load(response)
        error = payload.get("error", {})
        if error.get("code") in ("maxlag", "ratelimited"):
            time.sleep((attempt + 1) * 8)
            continue
        if error:
            raise RuntimeError(error.get("code"))
        return payload
    raise RuntimeError("Wiki write throttle did not clear")

def fetch(title, **extra):
    return call(action="query",titles=title,prop="info|revisions",rvprop="ids|content",rvslots="main",**extra)["query"]["pages"][0]

def current(p):
    r=p["revisions"][0]
    return r["revid"],r["slots"]["main"]["content"]
