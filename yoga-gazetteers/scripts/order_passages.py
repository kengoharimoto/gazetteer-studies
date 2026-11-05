#!/usr/bin/env python3
"""Passages for the third coding round: sannyasi, gosain/gosavi/goswami and bairagi.

Hits less than 500 characters apart in one volume form one passage (450 characters of context each side).
Index-like passages are flagged and not sent to coders. Volumes as in lexicon.py, minus the three duplicate
Cornell scans of Atkinson. Writes data/order_passages.tsv (ids S00001...) and data/order_batches/batch_NN.tsv.
Usage (from research/): python3 -I yoga-gazetteers/scripts/order_passages.py
"""
import csv, os, re
DUP = {"cu31924023947736", "cu31924023947744", "cu31924023947751"}
RX = re.compile(r"\bsan(?:n)?y[aā]s(?:i|ee)s?\b|\bgos[aā](?:i|y)ns?\b|\bgos[aā]v(?:i|ee)s?\b|\bgosw[aā]mis?\b"
                r"|\bb[aā]ir[aā]g(?:i|ee)s?\b|\bvair[aā]g(?:i|ee)s?\b", re.I)
rows = [r for r in csv.DictReader(open("yoga-gazetteers/data/corpus.tsv", encoding="utf-8"), delimiter="\t")
        if r["role"] in ("primary", "backup") and not r["dup"] and r["ident"] not in DUP]
out, n = [], 0
for c in rows:
    t = re.sub(r"\s+", " ", open(c["path"], encoding="utf-8", errors="replace").read())
    groups = []
    for m in RX.finditer(t):
        if groups and m.start() - groups[-1]["end"] < 500:
            groups[-1]["end"] = m.end(); groups[-1]["terms"].add(m.group(0))
        else:
            groups.append(dict(start=m.start(), end=m.end(), terms={m.group(0)}))
    for g in groups:
        n += 1
        text = t[max(0, g["start"] - 450):g["end"] + 450]
        toks = text.split()
        nums = sum(bool(re.fullmatch(r"[\d,;:.\-—\[\]()]+", x)) for x in toks)
        out.append(dict(id=f"S{n:05d}", ident=c["ident"], region=c["region"], vol=c["vol"], district=c["district"],
                        year=c["year"], gen=c["gen"], kind=c["kind"], terms=",".join(sorted(g["terms"])),
                        index=int(nums / max(1, len(toks)) > 0.18), text=text))
cols = list(out[0])
with open("yoga-gazetteers/data/order_passages.tsv", "w", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, cols, delimiter="\t"); w.writeheader(); w.writerows(out)
todo = sorted((p for p in out if not p["index"]), key=lambda p: (p["region"], p["year"], p["id"]))
os.makedirs("yoga-gazetteers/data/order_batches", exist_ok=True)
size = 160
for i in range(0, len(todo), size):
    with open(f"yoga-gazetteers/data/order_batches/batch_{i // size + 1:02d}.tsv", "w", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, cols, delimiter="\t"); w.writeheader(); w.writerows(todo[i:i + size])
print(len(out), "passages;", sum(p["index"] for p in out), "index-like;", len(todo), "to code in", -(-len(todo) // size), "batches")
