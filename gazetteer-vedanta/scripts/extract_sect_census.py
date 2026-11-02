#!/usr/bin/env python3
"""Extract the district-level census sect summaries quoted in the Bombay Gazetteer.

The volumes built on the 1872 census print a table "<District> Hindu Sects, 1872" and then a prose
summary: "From this statement it would seem that of the total Hindu population the unsectarian
classes numbered 610,314 or 88.02 per cent; the Shaivs 72,863 or 10.50 per cent; ...".
Later volumes have analogous sentences.  We take every sentence in the first 40% of the volume
that contains a sect word and "per cent", and parse "<label> [numbered] N or P per cent" pairs.

Usage: python3 -I scripts/extract_sect_census.py VOL OCRFILE  >> results/sect_census_raw.tsv
"""
import re, sys

vol, path = sys.argv[1], sys.argv[2]
t = open(path, encoding="utf-8", errors="replace").read()
t = re.sub(r"-\s*\n\s*(?=[a-z])", "", t)
t = re.sub(r"\s+", " ", t)
t = re.sub(r"(?<=\d)\s?[*•·°:'’]\s?(?=\d{1,2}\s*(?:■\s*)?per)", ".", t)   # decimal point garbles
t = re.sub(r"(?<=\d)[\^](?=\d{3})", ",", t)                                  # thousands separator garbles

SECTW = re.compile(r"(?i)\b(?:unsectarian|un-sectarian|unseo|shaiv|s[hb]aiv|[vy]a[il]shn|smart|lingayat|lingdyat|ramanuj|vallabh|"
                   r"kabir|madhv|svamin|swamin|shr[aáâ]v[aá]k|shriv|ascetic|bhagvat)")
blocks = []
for m in re.finditer(r"(?i)(?:Hindu\s+Sects|sects?\s*:|following\s+sects|belong\s+to\s+the\s+following|"
                     r"from\s+this\s+(?:statement\s+)?it\s+(?:would\s+)?(?:seem|appear)s?)", t):
    blocks.append(m.start())

seen = set()
PAIR = re.compile(r"(?i)((?:the\s+)?[A-Za-z][A-Za-z' -]{2,40}?)\s+(?:numbered\s+|numbering\s+|were\s+)?"
                  r"([\d,]{3,9})[\s,}\]]+(?:souls\s+)?or\s+(\d{1,2}\.\d{1,2}|\d{1,2})\s*(?:■\s*)?per\s*cent")
dump = len(sys.argv) > 3 and sys.argv[3] == "--dump"   # print whole snippets for hand transcription
for b in blocks:
    seg = t[b:b + 1500]
    if not SECTW.search(seg) or (b // 1000) in seen:
        continue
    seen.add(b // 1000)
    if dump:
        print(f"### {vol} @{b}\n{t[max(0, b - 200):b + 1300]}\n")
        continue
    for m in PAIR.finditer(seg):
        label = re.sub(r"(?i)^(?:and\s+|the\s+|of\s+the\s+total\s+hindu\s+population\s+)", "", m.group(1)).strip()
        label = re.sub(r"(?i)^.*?\b(the\s+)", "", label) if len(label) > 30 else label
        if not SECTW.search(label) and not re.search(r"(?i)unsect|other|jain|hindu", label):
            continue
        pct = re.sub(r"[,' ]", ".", m.group(3)).replace("..", ".")
        print("\t".join([vol, str(b), label, m.group(2).replace(",", ""), pct, seg[:400].replace("\t", " ")]))
