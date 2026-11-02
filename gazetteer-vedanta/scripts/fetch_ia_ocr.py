#!/usr/bin/env python3
"""Download the Internet Archive OCR text (*_djvu.txt) for every candidate scan.

Usage: python3 -I scripts/fetch_ia_ocr.py (data/ia_candidates.tsv | data/selection.tsv) data/ia_ocr [max_year]

Skips identifiers already downloaded. Writes data/ia_ocr/<identifier>.txt and
logs failures to data/ia_ocr/_failed.tsv.
"""
import csv, json, os, sys, time, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor

cand, outdir = sys.argv[1], sys.argv[2]
max_year = int(sys.argv[3]) if len(sys.argv) > 3 else 1913
os.makedirs(outdir, exist_ok=True)


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=180) as r:
                return r.read()
        except Exception as e:
            err = e
            time.sleep(3 * (i + 1))
    raise err


def fetch(ident):
    dest = os.path.join(outdir, ident + ".txt")
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return ident, "cached"
    try:
        meta = json.loads(get(f"https://archive.org/metadata/{ident}/files"))
        names = [f["name"] for f in meta.get("result", []) if f["name"].endswith("_djvu.txt")]
        if not names:
            return ident, "no-djvu-txt"
        data = get(f"https://archive.org/download/{ident}/" + urllib.parse.quote(names[0]))
        with open(dest, "wb") as f:
            f.write(data)
        return ident, f"ok {len(data)}"
    except Exception as e:
        return ident, f"error {e}"


rows = list(csv.DictReader(open(cand, encoding="utf-8"), delimiter="\t"))
ids = []
if "primary" in rows[0]:            # selection.tsv: primary + backup per volume
    ids = [x for r in rows for x in (r["primary"], r.get("backup", "")) if x]
    rows = []
for r in rows:
    try:
        y = int(str(r["year"])[:4])
    except ValueError:
        y = 0
    if y <= max_year and "imperial" not in r["title"].lower():
        ids.append(r["identifier"])

failed = []
with ThreadPoolExecutor(3) as ex:
    for ident, status in ex.map(fetch, ids):
        print(ident, status, flush=True)
        if not (status.startswith("ok") or status == "cached"):
            failed.append((ident, status))
with open(os.path.join(outdir, "_failed.tsv"), "w") as f:
    for a, b in failed:
        f.write(f"{a}\t{b}\n")
print(f"{len(ids)} candidates, {len(failed)} failed")
