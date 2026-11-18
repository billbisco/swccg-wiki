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

Cookies are reused (swccg-guild/work#632): every fresh sign-in leaves a session row on the wiki, so
the cookies are kept in one jar per account and the next run reuses them. Only when the jar's wiki
session has ended does the script sign in again (often with no password, through the still-valid
swccg.com site session). Jar: $WIKI_COOKIE_JAR, default ~/.cache/swccg-wiki/cookies-<account>.txt
(mode 600, never print or commit it). WIKI_COOKIE_JAR=none turns reuse off.

    python3 swccg_signin.py            # prints SIGNIN_OK <name> or SIGNIN_FAIL <reason>
"""
from __future__ import annotations

import atexit
import html
import http.cookiejar
import json
import os
import re
import sys
import urllib.parse
import urllib.error
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


def jar_path(name: str) -> str | None:
    """Cookie jar for this account (one per account), or None when reuse is turned off."""
    env = os.environ.get("WIKI_COOKIE_JAR", "")
    if env.lower() == "none":
        return None
    if env:
        return os.path.expanduser(env)
    slug = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower() or "account"
    return os.path.expanduser(f"~/.cache/swccg-wiki/cookies-{slug}.txt")


def _save(jar, path: str | None) -> None:
    if not path:
        return
    os.makedirs(os.path.dirname(path), mode=0o700, exist_ok=True)
    old = os.umask(0o077)
    try:
        jar.save(path, ignore_discard=True, ignore_expires=False)
    finally:
        os.umask(old)
    os.chmod(path, 0o600)


def sign_in(user: str | None = None, password: str | None = None, ua: str = "swccg-wiki-bot/1.0"):
    user = user or os.environ.get("WIKI_BOT_USER") or ""
    password = password or os.environ.get("WIKI_BOT_PASS") or ""
    if not user or not password:
        raise SignInError("WIKI_BOT_USER / WIKI_BOT_PASS not set")
    name = user.split("@", 1)[0].strip()
    path = jar_path(name)
    jar = http.cookiejar.MozillaCookieJar()
    if path and os.path.exists(path):
        try:
            jar.load(path, ignore_discard=True, ignore_expires=False)
        except (OSError, http.cookiejar.LoadError):
            jar = http.cookiejar.MozillaCookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    op.addheaders = [("User-Agent", ua)]
    atexit.register(_save, jar, path)  # keep MediaWiki's renewed cookies for the next run
    # 1) the saved wiki session still works: no new session row at all
    if len(jar) and whoami(op).casefold() == name.casefold():
        _save(jar, path)
        return op
    # 2) sign in through swccg.com; a still-valid site session skips the password form
    with op.open(START, timeout=60) as r:
        page, url = r.read().decode("utf-8", "replace"), r.geturl()
    if not url.startswith(SITE + "/wiki/"):
        if not url.startswith(SITE + "/login/login"):
            raise SignInError("sign-in page not reached")
        m = re.search(r'<form[^>]*action="(/login/login)"[^>]*>(.*?)</form>', page, re.S)
        if not m:
            raise SignInError("sign-in form not found")
        data = {**_fields(m.group(2)), "name": name, "password": password}
        req = urllib.request.Request(urllib.parse.urljoin(url, m.group(1)), urllib.parse.urlencode(data).encode(),
                                     headers={"Origin": SITE, "Referer": url})  # the service checks Origin, as a browser sends it
        try:
            with op.open(req, timeout=60) as r:
                r.read()
                final = r.geturl()
        except urllib.error.HTTPError as e:  # swccg.com answers a wrong name or password with 401
            final = ""
            if e.code not in (401, 403):
                raise
        if not final.startswith(SITE + "/wiki/"):
            raise SignInError("site sign-in refused (wrong name or password, banned, or locked)")
    who = whoami(op)
    if who.casefold() != name.casefold():
        raise SignInError("wiki did not sign in")
    _save(jar, path)
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
