#!/usr/bin/env python3
"""Sequentially fetch IA _djvu.txt for identifiers given on the command line into sringeri/data/ia_ocr/."""
import json, os, sys, time, urllib.request, urllib.parse
out = "sringeri/data/ia_ocr"
def get(u):
    for i in range(4):
        try:
            with urllib.request.urlopen(u, timeout=300) as r: return r.read()
        except Exception as e: err = e; time.sleep(5 * (i + 1))
    raise err
for ident in sys.argv[1:]:
    dst = f"{out}/{ident}.txt"
    if os.path.exists(dst): print("have", ident); continue
    try:
        files = json.loads(get(f"https://archive.org/metadata/{ident}/files"))["result"]
        t = [f["name"] for f in files if f["name"].endswith("_djvu.txt")]
        if not t: print("no text", ident); continue
        data = get(f"https://archive.org/download/{ident}/{urllib.parse.quote(t[0])}")
        open(dst, "wb").write(data); print("ok", ident, len(data))
    except Exception as e: print("FAIL", ident, e)
