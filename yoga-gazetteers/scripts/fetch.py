#!/usr/bin/env python3
"""Sequentially download IA OCR (*_djvu.txt) for each row of a selection table: primary, else backup.
Usage (from research/): python3 -I yoga-gazetteers/scripts/fetch.py <selection.tsv> <outdir>"""
import csv, json, os, sys, time, urllib.request, urllib.parse
sel, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)

def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=180) as r:
                return r.read()
        except Exception as e:
            err = e; time.sleep(5 * (i + 1))
    raise err

def fetch(ident):
    dest = os.path.join(outdir, ident + ".txt")
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return "cached"
    meta = json.loads(get(f"https://archive.org/metadata/{ident}"))
    names = [f["name"] for f in meta.get("files", []) if f["name"].endswith("_djvu.txt")]
    if not names:
        return "no-djvu-txt"
    # The storage server directly: archive.org/download/ redirects there and often fails with SSL EOF under load.
    try:
        data = get(f"https://{meta['server']}{meta['dir']}/" + urllib.parse.quote(names[0]))
    except Exception:
        data = get(f"https://archive.org/download/{ident}/" + urllib.parse.quote(names[0]))
    open(dest, "wb").write(data)
    return f"ok {len(data)}"

for r in csv.DictReader(open(sel, encoding="utf-8"), delimiter="\t"):
    for ident in filter(None, (r["primary"], r["backup"])):
        try:
            st = fetch(ident)
        except Exception as e:
            st = f"error {e}"
        print(r["vol"], ident, st, flush=True)
        if st.startswith("ok") or st == "cached":
            break
        time.sleep(2)
