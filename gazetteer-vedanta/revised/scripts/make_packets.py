#!/usr/bin/env python3
"""Cue-sentence packets for the revised state gazetteers (third date; copied from cp/scripts, + seats, Smarta, reform and endowment terms).

Usage: python3 -I scripts/make_packets.py data/selection_up.tsv   (from north/)
Writes results/packets/<VOL>.txt: every sentence mentioning an ascetic order or a math/akhara, with one
sentence of context either side and the nearest running-head page number; and results/packets/_summary.tsv.
"""
import csv, os, re, sys

CUE = re.compile(r"(?i)sm[aā]rt|sh?a[nṅ]kar[aā]ch|sringeri|shringeri|sankesh|karvir|dw?[aā]rk[aā] p|jyotir|joshimath|govardhan|kanchi|kamakoti|zamind[aā]ri abolition|religious (?:trust|endowment)|endowments? (?:act|board|commission)|temple act|bodh ?gaya temple|g[ou]ss?h?[aā][iī]n|g[ou]s[aā]v[iī]|\bgosai\b|gosw[aā]m|\batith?s?\b|sann?y[aā]s|\bdandis?\b|da[sś]n[aā]m|"
                 r"paramhans|bair[aā]g|r[aā]m[aā]nand|\bjogis?\b|kanph|ud[aā]s[iī]|n[aā]nak|\bfaq?k[iī]r|"
                 r"\bsadhus?\b|\bascetic|mendicant|\bmaths?\b|\bmutts?\b|akh[aā]r|sh?ankar[aā]ch|\bmahant|"
                 r"\bn[aā]g[aā]s?\b|\b[A-Z][a-z]+ (?:Giri|Puri|Bharti|Bharati)\b")   # Bengal: no bare "Puri" (district)
PAGE = re.compile(r"(?:^|\s)(\d{1,3})\s+[A-Z][A-Z' ]{3,}\.?(?=\s)|(?<=\s)[A-Z][A-Z' ]{3,}\.?\s+(\d{1,3})(?=\s)")
os.makedirs("results/packets", exist_ok=True)
summ = []
for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"):
    f = f"data/ia_ocr/{r['primary']}.txt"
    if not os.path.exists(f) or os.path.getsize(f) == 0:
        f = f"data/ia_ocr/{r['backup']}.txt" if r.get("backup") else f
    if not os.path.exists(f) or os.path.getsize(f) == 0:
        summ.append((r["vol"], r["district"], "MISSING", 0, 0)); continue
    t = re.sub(r"-\s*\n\s*(?=[a-z])", "", open(f, encoding="utf-8", errors="replace").read())
    t = re.sub(r"\s+", " ", t)
    pages = [(m.start(), m.group(1) or m.group(2)) for m in PAGE.finditer(t)]
    bounds = [0] + [m.end() for m in re.finditer(r"(?<=[a-z\)\]'’”])[.;]\s+(?=[A-Z‘'\"“])", t)] + [len(t)]
    sents = [t[bounds[i]:bounds[i + 1]].strip() for i in range(len(bounds) - 1)]
    hit = [i for i, s in enumerate(sents) if CUE.search(s)]
    keep = sorted({x for h in hit for x in (h - 1, h, h + 1) if 0 <= x < len(sents)})
    out, prev = [], -5
    for x in keep:
        pos = bounds[x]
        pg = next((p for o, p in reversed(pages) if o <= pos), "")
        if x != prev + 1:
            out.append(f"\n--- p.{pg} @{pos}")
        out.append(("* " if x in hit else "  ") + sents[x][:900])
        prev = x
    open(f"results/packets/{r['vol']}.txt", "w", encoding="utf-8").write(
        f"### {r['vol']} {r['district']} ({os.path.basename(f)})\n" + "\n".join(out))
    summ.append((r["vol"], r["district"], os.path.basename(f), len(hit), sum(len(o) for o in out)))
with open("results/packets/_summary.tsv", "a", encoding="utf-8") as fh:
    for s in summ:
        fh.write("\t".join(map(str, s)) + "\n")
for s in summ:
    print(*s, sep="\t")
