#!/usr/bin/env python3
"""Regional supplement (Bombay after 1890, Rajputana, Rajasthan revised): catalogue, term counts and passages
for all three coding rounds, without touching the ids of the original rounds.

Reads regions/data/selection.tsv and regions/data/ia_ocr/ (primary scan, else backup). Writes
  data/corpus_regions.tsv                  one row per volume (same columns as data/corpus.tsv)
  results/term_counts_regions.tsv          hits per term family (same families as scripts/lexicon.py)
  data/region_core_passages.tsv     PR#####  yoga/yogi/Jogi/... (round one: CODING_INSTRUCTIONS.md)
  data/region_fakir_passages.tsv    FR#####  fakir/sadhu (round two: CODING_INSTRUCTIONS_FAKIR.md)
  data/region_order_passages.tsv    SR#####  sannyasi/gosain/bairagi (round three: CODING_INSTRUCTIONS_ORDERS.md)
  data/region_batches/{core,fakir,order}_NN.tsv   non-index passages, 160 per batch
Usage (from research/): python3 -I yoga-gazetteers/scripts/region_passages.py
"""
import csv, os, re

BASE = "yoga-gazetteers"
FAM = {  # as in scripts/lexicon.py
    "yoga": r"\byoga(?!-?s[uû]tra)s?\b|\byog(?:a|ic)\b|\byogic\b",
    "yogasutra": r"\byoga[- ]?s[uûū]tras?\b",
    "patanjali": r"\bpatanjal[ia]\b|\bpatañjal[ia]\b",
    "yogi": r"\byog(?:i|ee|in)s?\b|\byogini?s?\b",
    "jogi": r"\bj(?:o|oo|u)g(?:i|ee|y)s?\b|\bjogin\b",
    "nath_kanphata": r"\bkan-?ph?ata\b|\bkanpha?tt?a\b|\bgorakh-?n[aā]th(?:i|is)?\b|\bgorakhpanth",
    "fakir": r"\bfa(?:k|q)(?:ee|i)rs?\b",
    "sannyasi": r"\bsan(?:n)?y[aā]s(?:i|ee)s?\b|\bsany[aā]si\b",
    "gosain": r"\bgos[aā](?:i|y)ns?\b|\bgos[aā]v(?:i|ee)s?\b|\bgosw[aā]mi",
    "bairagi": r"\bb[aā]ir[aā]g(?:i|ee)s?\b|\bvair[aā]g(?:i|ee)s?\b",
    "sadhu": r"\bs[aā]dhus?\b",
    "practice": r"\bsam[aā]dh[ie]\b|\bpr[aā]n[aā]y[aā]ma\b|\b[aā]sanas?\b|\bhatha\b|\bholding (?:his|the) breath\b"
                r"|\bbreath(?:ing)? (?:exercises?|control)\b|\bburied alive\b|\bpostures?\b",
    "modern": r"\bvivek[aā]nand|\btheosoph|\bblavatsky|\bphysical culture\b|\byogic exercises?\b",
}
RX = {k: re.compile(v, re.I) for k, v in FAM.items()}
CORE = [k for k in ("yoga", "yogasutra", "patanjali", "yogi", "jogi", "nath_kanphata", "practice", "modern")]
ROUNDS = {
    "core": ("PR", re.compile("|".join(f"(?:{FAM[k]})" for k in CORE), re.I)),
    "fakir": ("FR", re.compile(r"\bfa(?:k|q)(?:ee|i)rs?\b|\bs[aā]dhus?\b", re.I)),
    "order": ("SR", re.compile(r"\bsan(?:n)?y[aā]s(?:i|ee)s?\b|\bgos[aā](?:i|y)ns?\b|\bgos[aā]v(?:i|ee)s?\b"
                               r"|\bgosw[aā]mis?\b|\bb[aā]ir[aā]g(?:i|ee)s?\b|\bvair[aā]g(?:i|ee)s?\b", re.I)),
}

def gen(y):
    y = int(str(y)[:4]); return "G1" if y <= 1890 else "G2" if y <= 1935 else "G3"

corpus = []
for r in csv.DictReader(open(f"{BASE}/regions/data/selection.tsv", encoding="utf-8"), delimiter="\t"):
    for role, ident in (("primary", r["primary"]), ("backup", r["backup"])):
        p = f"{BASE}/regions/data/ia_ocr/{ident}.txt"
        if ident and os.path.exists(p) and os.path.getsize(p) > 50_000:
            corpus.append(dict(path=p, ident=ident, region=r["region"], vol=r["vol"], district=r["district"],
                               year=r["year"], gen=gen(r["year"]), kind=r["kind"], role=role, dup="",
                               note=r["note"], bytes=os.path.getsize(p)))
            break
    else:
        print("MISSING", r["vol"], r["primary"], r["backup"])
with open(f"{BASE}/data/corpus_regions.tsv", "w", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, list(corpus[0]), delimiter="\t"); w.writeheader(); w.writerows(corpus)

counts, out = [], {k: [] for k in ROUNDS}
n = {k: 0 for k in ROUNDS}
for c in corpus:
    t = re.sub(r"\s+", " ", open(c["path"], encoding="utf-8", errors="replace").read())
    row = dict(ident=c["ident"], region=c["region"], vol=c["vol"], district=c["district"], year=c["year"],
               gen=c["gen"], kind=c["kind"], words=len(t.split()))
    row.update({k: len(rx.findall(t)) for k, rx in RX.items()})
    counts.append(row)
    for name, (prefix, rx) in ROUNDS.items():
        groups = []
        for m in rx.finditer(t):
            if groups and m.start() - groups[-1]["end"] < 500:
                groups[-1]["end"] = m.end(); groups[-1]["terms"].add(m.group(0))
            else:
                groups.append(dict(start=m.start(), end=m.end(), terms={m.group(0)}))
        for g in groups:
            n[name] += 1
            text = t[max(0, g["start"] - 450):g["end"] + 450]
            toks = text.split()
            nums = sum(bool(re.fullmatch(r"[\d,;:.\-—\[\]()]+", x)) for x in toks)
            rec = dict(id=f"{prefix}{n[name]:05d}", ident=c["ident"], region=c["region"], vol=c["vol"],
                       district=c["district"], year=c["year"], gen=c["gen"], kind=c["kind"])
            if name == "core":  # round one also records the term families
                rec["families"] = ",".join(sorted({k for k in CORE for x in g["terms"] if RX[k].fullmatch(x)}))
            rec.update(terms=",".join(sorted(g["terms"])), index=int(nums / max(1, len(toks)) > 0.18), text=text)
            out[name].append(rec)

with open(f"{BASE}/results/term_counts_regions.tsv", "w", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, list(counts[0]), delimiter="\t"); w.writeheader(); w.writerows(counts)
os.makedirs(f"{BASE}/data/region_batches", exist_ok=True)
for name, rows in out.items():
    with open(f"{BASE}/data/region_{name}_passages.tsv", "w", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(rows[0]), delimiter="\t"); w.writeheader(); w.writerows(rows)
    todo = sorted((p for p in rows if not p["index"]), key=lambda p: (p["region"], p["year"], p["id"]))
    for i in range(0, len(todo), 160):
        with open(f"{BASE}/data/region_batches/{name}_{i // 160 + 1:02d}.tsv", "w", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, list(rows[0]), delimiter="\t"); w.writeheader(); w.writerows(todo[i:i + 160])
    print(name, len(rows), "passages;", sum(p["index"] for p in rows), "index-like;", len(todo), "to code")
print(len(corpus), "volumes")
