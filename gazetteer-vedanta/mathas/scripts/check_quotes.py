#!/usr/bin/env python3
"""Check that each coded quote occurs verbatim (whitespace-normalised) in some downloaded OCR text.
Usage: python3 -I mathas/scripts/check_quotes.py mathas/results/coded/*.tsv"""
import csv, glob, re, sys
norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
texts = {f: norm(open(f, encoding="utf-8", errors="replace").read()) for f in glob.glob("*/data/ia_ocr/*.txt") + glob.glob("data/ia_ocr/*.txt")}
for path in sys.argv[1:]:
    ok = bad = 0
    for r in csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t"):
        q = norm(r["quote"].strip('"“”'))
        parts = [p for p in re.split(r"\s*(?:…|\.\.\.)\s*", q) if len(p) > 15]
        found = all(any(p in t for t in texts.values()) for p in parts) if parts else False
        if found: ok += 1
        else:
            bad += 1; print("NOT FOUND", path.split("/")[-1], r["id"], r["quote"][:90])
    print(path, "found", ok, "missing", bad)
