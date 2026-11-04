#!/usr/bin/env python3
"""Sequentially download the IA OCR text (_djvu.txt) for every catalogue row with include=yes.
Usage: python3 -I mathas/archives/scripts/fetch_ocr.py mathas/archives/results/catalogue.tsv mathas/data/archives/ocr
Skips files already present; logs failures to <outdir>/_failed.tsv."""
import csv, json, os, sys, time, urllib.parse, urllib.request
cat, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
def get(u):
    for i in range(4):
        try:
            with urllib.request.urlopen(u, timeout=180) as r: return r.read()
        except Exception as e: err = e; time.sleep(4 * (i + 1))
    raise err
for r in csv.DictReader(open(cat, encoding="utf-8"), delimiter="\t"):
    if r["include"] != "yes": continue
    ident = r["identifier"]; dst = f"{out}/{ident}.txt"
    if os.path.exists(dst): continue
    try:
        files = json.loads(get(f"https://archive.org/metadata/{ident}/files"))["result"]
        t = [f["name"] for f in files if f["name"].endswith("_djvu.txt")]
        data = get(f"https://archive.org/download/{ident}/{urllib.parse.quote(t[0])}") if t else b""
        open(dst, "wb").write(data)
    except Exception as e:
        open(f"{out}/_failed.tsv", "a").write(f"{ident}\t{e}\n")
print("done")
