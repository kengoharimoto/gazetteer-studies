#!/usr/bin/env python3
"""Check each coded quote against the OCR of its own file (whitespace-normalised, case-insensitive).
Usage: python3 -I mathas/archives/scripts/check_quotes.py mathas/archives/results/coded/*.tsv"""
import csv, re, sys, os
norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
for path in sys.argv[1:]:
    ok = bad = skip = 0
    for r in csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t"):
        q = r["quote"].strip().strip('"“”')
        if not q or q.startswith("(no legible") or q.startswith("("):
            skip += 1; continue
        f = f"mathas/data/archives/ocr/{r['identifier']}.txt"
        t = norm(open(f, encoding="utf-8", errors="replace").read()) if os.path.exists(f) else ""
        parts = [p for p in re.split(r"\s*(?:…|\.\.\.)\s*", norm(q)) if len(p) > 12]
        if parts and all(p in t for p in parts): ok += 1
        else: bad += 1; print("NOT FOUND", r["id"], q[:80])
    print(path, "found", ok, "missing", bad, "no-quote", skip)
