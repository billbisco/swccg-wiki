from contextlib import closing
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request
import uuid

import websocket

sources = SOURCE_MAP

def solver(cmd, **fields):
    request = urllib.request.Request("http://127.0.0.1:8191/v1", json.dumps(dict(cmd=cmd, **fields)).encode(),
                                     {"Content-Type": "application/json"})
    try:
        response = urllib.request.urlopen(request, timeout=115)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        return json.load(response)

def debug_ports():
    ports = set()
    for proc in Path("/proc").iterdir():
        if not proc.name.isdecimal():
            continue
        try:
            args = (proc / "cmdline").read_bytes().split(b"\0")
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            continue
        for arg in args:
            if arg.startswith(b"--remote-debugging-port="):
                ports.add(int(arg.split(b"=")[1]))
    return ports

def get_original(ports, url):
    tabs = []
    for port in ports:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=2) as response:
                tabs.extend(tab for tab in json.load(response) if tab.get("url") == url)
        except OSError:
            continue
    if len(tabs) != 1:
        return dict(error=f"Expected one owned image tab, saw {len(tabs)}")
    with closing(websocket.create_connection(tabs[0]["webSocketDebuggerUrl"], suppress_origin=True, timeout=18)) as conn:
        conn.send(json.dumps(dict(id=1, method="Runtime.evaluate", params=dict(awaitPromise=True, returnByValue=True,
            expression='''(async () => {
                const img = document.querySelector('body > img');
                const response = await fetch(img.currentSrc || img.src);
                const type = response.headers.get('content-type');
                const result = {status: response.status, type, width: img.naturalWidth, height: img.naturalHeight};
                if (response.ok && type?.startsWith('image/')) {
                    result.data = await new Promise((resolve, reject) => {
                        const reader = new FileReader();
                        reader.onload = () => resolve(reader.result.split(',', 2)[1]);
                        reader.onerror = reject;
                        response.blob().then(blob => reader.readAsDataURL(blob), reject);
                    });
                }
                return result;
            })()'''))))
        while True:
            message = json.loads(conn.recv())
            if message.get("id") == 1:
                return message.get("result", {}).get("result", {}).get("value", {})

session = "memorycore-reflections381-originals-" + uuid.uuid4().hex
existing = debug_ports()
created = solver("sessions.create", session=session)
assert created["status"] == "ok", created["message"]
ports = debug_ports() - existing
try:
    for key in sys.argv[1:] or sources:
        url = "https://theswca.com/" + sources[key]
        response = solver("request.get", url=url, session=session, maxTimeout=55000, returnScreenshot=True, disableMedia=False)
        solution = response.get("solution") or {}
        title = re.search(r"<title>(.*?)</title>", solution.get("response") or "")
        if response["status"] != "ok" or not title or not re.search(r"\(\d+×\d+\)", title[1]):
            result = dict(error=response.get("message"), title=title[1] if title else "")
        else:
            try:
                result = get_original(ports, url)
            except (OSError, websocket.WebSocketException) as error:
                result = dict(error=type(error).__name__)
            if not result.get("data") and solution.get("screenshot"):
                result["rendered_png"] = solution["screenshot"]
            result["title"] = title[1]
        print(json.dumps(dict(id=key, source=url, **result)), flush=True)
finally:
    solver("sessions.destroy", session=session)
