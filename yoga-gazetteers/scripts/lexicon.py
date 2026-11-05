#!/usr/bin/env python3
"""Count yoga-related terms in every selected OCR volume and pull keyword-in-context lines.

Reads data/corpus.tsv. Volumes counted: role primary, or backup when the primary scan is absent
(dup empty), and not 'unselected'. Writes
  results/term_counts.tsv   one row per volume: words, and hits per term family
  results/kwic.tsv          every hit of the core families (yoga, yogi, jogi, patanjali, practice terms),
                            with ~300 characters of context
Usage (from research/): python3 -I yoga-gazetteers/scripts/lexicon.py
"""
import csv, re

FAM = {  # family -> regex (case-insensitive, on whitespace-normalised text)
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
CORE = {"yoga", "yogasutra", "patanjali", "yogi", "jogi", "nath_kanphata", "practice", "modern"}
RX = {k: re.compile(v, re.I) for k, v in FAM.items()}

rows = [r for r in csv.DictReader(open("yoga-gazetteers/data/corpus.tsv", encoding="utf-8"), delimiter="\t")
        if r["role"] in ("primary", "backup") and not r["dup"]]
counts, kwic = [], []
for r in rows:
    t = re.sub(r"\s+", " ", open(r["path"], encoding="utf-8", errors="replace").read())
    c = dict(ident=r["ident"], region=r["region"], vol=r["vol"], district=r["district"], year=r["year"],
             gen=r["gen"], kind=r["kind"], words=len(t.split()))
    for k, rx in RX.items():
        hits = list(rx.finditer(t))
        c[k] = len(hits)
        if k in CORE:
            for m in hits:
                if k == "practice" and m.group(0).lower().startswith("posture"):
                    continue  # too common in other senses; counted only
                kwic.append(dict(ident=r["ident"], region=r["region"], vol=r["vol"], year=r["year"],
                                 gen=r["gen"], kind=r["kind"], family=k, term=m.group(0), pos=m.start(),
                                 context=t[max(0, m.start() - 300):m.end() + 300]))
    counts.append(c)

for name, data in (("term_counts", counts), ("kwic", kwic)):
    with open(f"yoga-gazetteers/results/{name}.tsv", "w", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(data[0]), delimiter="\t")
        w.writeheader()
        w.writerows(data)
print(len(counts), "volumes;", len(kwic), "core hits")
