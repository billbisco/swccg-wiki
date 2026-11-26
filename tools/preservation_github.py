"""Git-object identity for GitHub commit/blob web pages (swccg-guild/work#1377).

GitHub renders ``github.com/<owner>/<repo>/commit/<sha>`` and
``.../blob/<sha>/<path>`` fresh on every request, so the HTML bytes never match
a registered fetch twice. A source with representation
``checked_github_git_object`` keeps its backed-up page bytes (``sha256`` /
``bytes`` still bind the registration's job and source backup) but the central
owner checks the git object instead of the HTML:

* commit: the page answers 200 and names the full 40-hex commit SHA that was
  bound at registration (``github_object.commit``);
* blob: the raw file at
  ``raw.githubusercontent.com/<owner>/<repo>/<commit>/<path>`` (and at the
  cited short ref, if the URL uses one) has the registered
  ``file_sha256`` / ``file_bytes``.

An archived capture of such a page is verified when its strict indexed raw
replay answers 200 and names the same full commit SHA.

This module is pure: callers pass their own ``fetch`` (the worker's, which
returns status/sha256/size and the first bytes of the body).
"""
from __future__ import annotations

import re
import urllib.parse

GITHUB_REPRESENTATION = "checked_github_git_object"
_SHA256 = re.compile(r"[0-9a-f]{64}")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_PAGE = re.compile(
    r"https://github\.com/([A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))/([A-Za-z0-9._-]{1,100})/"
    r"(commit|blob)/([0-9a-f]{7,40})(?:/(.+))?"
)


def parse_github_page(url: object) -> dict | None:
    """Return {owner, repo, kind, ref, path} for a pinned commit/blob page URL."""
    if not isinstance(url, str):
        return None
    try:
        parts = urllib.parse.urlsplit(url)
    except ValueError:
        return None
    if parts.query or parts.fragment or url.endswith("/") or any(c.isspace() for c in url):
        return None
    match = _PAGE.fullmatch(url)
    if not match:
        return None
    owner, repo, kind, ref, path = match.groups()
    if repo in {".", ".."} or repo.endswith(".git"):
        return None
    if kind == "commit":
        if path is not None:
            return None
    else:
        if not path:
            return None
        segments = path.split("/")
        if any(segment in {"", ".", ".."} for segment in segments):
            return None
        if any(urllib.parse.unquote(segment) in {"", ".", ".."} or "/" in urllib.parse.unquote(segment)
               for segment in segments):
            return None
    return {"owner": owner, "repo": repo, "kind": kind, "ref": ref, "path": path}


def is_github_object_url(url: object) -> bool:
    return parse_github_page(url) is not None


def raw_url(source: dict, ref: str | None = None) -> str:
    """The raw file at the bound full commit (or another ref of the same URL)."""
    obj = source["github_object"]
    if obj.get("kind") != "blob":
        raise ValueError("only a blob page has a raw file")
    return "https://raw.githubusercontent.com/{}/{}/{}/{}".format(
        obj["owner"], obj["repo"], ref or obj["commit"], obj["path"])


def validate_github_object(source: object) -> list[str]:
    """Validate the recorded binding; performs no network access."""
    if not isinstance(source, dict):
        return ["GitHub source must be an object"]
    errors = []
    if source.get("representation") != GITHUB_REPRESENTATION:
        errors.append("source representation is not " + GITHUB_REPRESENTATION)
    url = source.get("url")
    if source.get("primary_url", url) != url:
        errors.append("a GitHub page is its own capture target; primary_url must equal url")
    parsed = parse_github_page(url)
    if parsed is None:
        return errors + ["source.url is not a pinned github.com commit/<sha> or blob/<sha>/<path> page"]
    obj = source.get("github_object")
    if not isinstance(obj, dict):
        return errors + ["github_object binding is required"]
    for field in ("owner", "repo", "kind", "ref", "path"):
        if obj.get(field) != parsed[field]:
            errors.append("github_object." + field + " does not match source.url")
    commit = obj.get("commit")
    if not isinstance(commit, str) or not _COMMIT.fullmatch(commit):
        errors.append("github_object.commit must be the full lowercase 40-hex commit SHA")
    elif not commit.startswith(parsed["ref"]):
        errors.append("github_object.commit does not extend the cited ref")
    if parsed["kind"] == "blob":
        if not isinstance(obj.get("file_sha256"), str) or not _SHA256.fullmatch(obj["file_sha256"]):
            errors.append("github_object.file_sha256 must be the raw file's lowercase SHA-256")
        if type(obj.get("file_bytes")) is not int or obj["file_bytes"] < 0:
            errors.append("github_object.file_bytes must be a nonnegative integer")
    elif "file_sha256" in obj or "file_bytes" in obj:
        errors.append("a commit page binds no raw file")
    allowed = {"owner", "repo", "kind", "ref", "path", "commit", "file_sha256", "file_bytes"}
    extra = sorted(set(obj) - allowed)
    if extra:
        errors.append("github_object has unsupported fields: " + ", ".join(extra))
    return errors


def names_commit(body: object, commit: str) -> bool:
    """The page (or its archived replay) names the exact full commit SHA."""
    if not isinstance(body, (bytes, bytearray)) or not _COMMIT.fullmatch(commit or ""):
        return False
    return commit.encode("ascii") in body


def check_public(fetch, source: dict) -> dict:
    """Freshly verify the bound git object. Returns {matches, method, observations}."""
    errors = validate_github_object(source)
    if errors:
        raise ValueError("; ".join(errors))
    obj = source["github_object"]
    observations = []
    if obj["kind"] == "commit":
        page = fetch(source["url"])
        named = page.get("status") == 200 and names_commit(page.get("body"), obj["commit"])
        observations.append({"url": source["url"], "status": page.get("status"), "names_commit": named})
        return {"matches": named, "method": "github_commit_oid", "commit": obj["commit"],
                "observations": observations}
    refs = [obj["commit"]] + ([obj["ref"]] if obj["ref"] != obj["commit"] else [])
    matches = True
    for ref in refs:
        url = raw_url(source, ref)
        raw = fetch(url)
        same = (raw.get("status") == 200 and raw.get("sha256") == obj["file_sha256"] and
                raw.get("size") == obj["file_bytes"])
        observations.append({"url": url, "status": raw.get("status"), "sha256": raw.get("sha256"),
                             "bytes": raw.get("size"), "matches": same})
        if not same:
            matches = False
            break
    return {"matches": matches, "method": "github_blob_raw_file", "commit": obj["commit"],
            "observations": observations}
