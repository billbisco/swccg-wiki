#!/usr/bin/env python3
"""Sign a bot in to the wiki through swccg.com (the one site sign-in) and return a cookie session.

The wiki has no password sign-in of its own any more (#266 AC8): Special:UserLogin, action=login,
clientlogin and bot passwords are off. A bot signs in exactly like a person does:
    wiki Special:SwccgSignIn -> swccg.com/login (player name + password) -> back to the wiki.
The returned urllib opener carries the wiki session cookie; call the API with it as usual
(meta=tokens for the CSRF token, then action=edit ...).

Credentials come from WIKI_BOT_USER / WIKI_BOT_PASS (or arguments). An old bot-password login
name such as "Holocron Claude@claude" is accepted: the "@app" part is dropped. Nothing secret is
printed or logged. Standard library only; normal TLS verification.

    python3 swccg_signin.py            # prints SIGNIN_OK <name> or SIGNIN_FAIL <reason>
"""
from __future__ import annotations

import html
import http.cookiejar
import json
import os
import re
import sys
import urllib.parse
import urllib.request

SITE = "https://swccg.com"
API = SITE + "/wiki/api.php"
START = SITE + "/wiki/Special:SwccgSignIn?returnto=Special:BlankPage"


class SignInError(RuntimeError):
    pass


def _fields(form: str) -> dict:
    out = {}
    for tag in re.findall(r"<input\b[^>]*>", form):
        n = re.search(r'\bname="([^"]*)"', tag)
        v = re.search(r'\bvalue="([^"]*)"', tag)
        if n and re.search(r'type="hidden"', tag):
            out[html.unescape(n.group(1))] = html.unescape(v.group(1)) if v else ""
    return out


def sign_in(user: str | None = None, password: str | None = None, ua: str = "swccg-wiki-bot/1.0"):
    user = user or os.environ.get("WIKI_BOT_USER") or ""
    password = password or os.environ.get("WIKI_BOT_PASS") or ""
    if not user or not password:
        raise SignInError("WIKI_BOT_USER / WIKI_BOT_PASS not set")
    name = user.split("@", 1)[0].strip()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    op.addheaders = [("User-Agent", ua)]
    with op.open(START, timeout=60) as r:
        page, url = r.read().decode("utf-8", "replace"), r.geturl()
    if not url.startswith(SITE + "/login/login"):
        raise SignInError("sign-in page not reached")
    m = re.search(r'<form[^>]*action="(/login/login)"[^>]*>(.*?)</form>', page, re.S)
    if not m:
        raise SignInError("sign-in form not found")
    data = {**_fields(m.group(2)), "name": name, "password": password}
    req = urllib.request.Request(urllib.parse.urljoin(url, m.group(1)), urllib.parse.urlencode(data).encode(),
                                 headers={"Origin": SITE, "Referer": url})  # the service checks Origin, as a browser sends it
    with op.open(req, timeout=60) as r:
        r.read()
        final = r.geturl()
    if not final.startswith(SITE + "/wiki/"):
        raise SignInError("site sign-in refused (wrong name or password, banned, or locked)")
    who = whoami(op)
    if who.casefold() != name.casefold():
        raise SignInError("wiki did not sign in")
    return op


def whoami(op) -> str:
    q = urllib.parse.urlencode({"action": "query", "meta": "userinfo", "format": "json", "formatversion": "2"})
    with op.open(API + "?" + q, timeout=60) as r:
        u = json.loads(r.read().decode())["query"]["userinfo"]
    return "" if u.get("anon") else u.get("name", "")


if __name__ == "__main__":
    try:
        print("SIGNIN_OK", whoami(sign_in()))
    except SignInError as e:
        print("SIGNIN_FAIL", e)
        sys.exit(1)
