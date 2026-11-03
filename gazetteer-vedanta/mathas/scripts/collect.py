#!/usr/bin/env python3
"""Collect mentions of Śaṅkara maṭhas (by seat) from every downloaded OCR text in the study.
Usage (from gazetteer-vedanta/): python3 -I mathas/scripts/collect.py > mathas/results/hits.tsv
Columns: hit_id seat file line page_guess match context
Text is whitespace-joined so patterns can span line breaks. Overlapping hits (<300 chars apart, same seat) are merged.
"""
import bisect, glob, os, re, sys
S = r"(?:sh?ankar[aáā]?ch[aáā]r\w*|s[aā]nkar[aā]ch\w*)"
M = r"(?:math\w*|mutt\w*|monaster\w*|m[aā]tam|p[iī]th\w*|peeth\w*|seat|gadi|pontiff|svami|swami)"
SEATS = {
  "sankeshvar": r"\b(?:sa?n?k[eé]sh?[vw]a?r|sank[eé]s[vw]a?r|shank[eé]sh?[vw]a?r|sankeshwar)\b",
  "karvir": r"karav?[eií]e?r.{0,60}(?:p[iī]th|peeth|math|" + S + r")|" + S + r".{0,40}karav?[ií]e?r",
  "dvarka": r"(?:d[vw][aā]?r[aā]?k[aā]).{0,120}(?:" + S + r"|s[h]?[aā]rad[aā] ?(?:math|p[iī]th|peeth))|(?:" + S + r"|s[h]?[aā]rad[aā] ?(?:math|p[iī]th|peeth)).{0,120}d[vw][aā]?r[aā]?k[aā]",
  "govardhan": r"go[vb]a?rdhan\w* ?(?:math|mutt|p[iī]th|peeth)|" + S + r".{0,60}\bpuri\b.{0,40}" + M + r"|" + S + r"[’'`s]{0,2} ?(?:math|mutt|monaster)",
  "jyotirmath": r"jy?ot[iīh]?[rs]?h? ?ma[tṭ]h|josh[iī] ?ma[tṭ]h|joshimath|jotirmath|jyotish ?math|badr[ií]n[aā]th.{0,80}" + S,
  "sringeri": r"s[h]?r[iíī]?[nñṅ]?g[eéēè]?[eiéēí]?r[iíī]\b|sring[aá]-? ?giri",
  "kudali": r"\bk[uū]d[aā]l[iī]\b.{0,100}(?:math|matha|guru|sw[aā]mi|sm[aā]rt)|\bkudalgi\b",
  "kanchi_kumbakonam": r"k[aā]m[aā]ko[tṭ]i|(?:kumbak[oó]n\w*|conje+v\w*|k[aā][nñ]ch[iī]).{0,120}(?:sm[aā]rt\w* ?(?:math|mutt)|" + S + r")|" + S + r".{0,120}(?:kumbak[oó]n\w*|conje+v\w*|k[aā][nñ]ch[iī])",
  "pushpagiri": r"pu[sṣ]h?pa ?giri",
  "virupaksha_hampi": r"vir[uū]p[aā]ksh\w*.{0,100}(?:sw[aā]mi|math|guru|" + S + r")",
  "sivaganga": r"s[h]?iva ?gang[aā]\b.{0,100}(?:math|sw[aā]mi|guru|" + S + r")",
  "generic": S + r".{0,80}" + M,
}
PAT = {k: re.compile(v, re.I) for k, v in SEATS.items()}
dirs = sorted(set(glob.glob("*/data/ia_ocr")) | {"data/ia_ocr"})
print("hit_id\tseat\tfile\tline\tpage_guess\tmatch\tcontext")
n = 0
for d in dirs:
    for f in sorted(glob.glob(d + "/*.txt")):
        raw = open(f, encoding="utf-8", errors="replace").read()
        lines = raw.split("\n")
        starts, pos, pages = [], 0, []
        page = ""
        for ln in lines:
            starts.append(pos); pos += len(ln) + 1
            m = re.match(r"^\s*(\d{1,4})\s*$", ln)
            if m: page = m.group(1)
            pages.append(page)
        txt = raw.replace("\n", " ")
        ident = (d.split("/data")[0] if d != "data/ia_ocr" else "bombay") + "/" + os.path.basename(f)[:-4]
        for seat, p in PAT.items():
            last = -10**9
            for m in p.finditer(txt):
                if m.start() - last < 300: continue
                last = m.start()
                li = bisect.bisect_right(starts, m.start()) - 1
                ctx = " ".join(txt[max(0, m.start() - 400): m.end() + 400].split())
                n += 1
                print(f"H{n:04d}\t{seat}\t{ident}\t{li+1}\t{pages[li]}\t{' '.join(m.group(0).split())[:80]}\t{ctx}")
