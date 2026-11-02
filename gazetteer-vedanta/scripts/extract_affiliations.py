#!/usr/bin/env python3
"""Extract sect-affiliation statements from Bombay Gazetteer OCR text.

Usage: python3 -I scripts/extract_affiliations.py VOL OCRFILE > out.tsv

For every sentence that mentions a sect / teacher / monastery term, output:
  vol, page (nearest running-head page number), section (population / other),
  caste_head (opening words of the caste account the sentence falls in),
  head_count (number given in that opening, if any), labels, sentence.

Matching is done on a "skeleton" of the text (lowercase, diacritics and common
OCR vowel garbles folded to plain letters), which has the same length as the
original so offsets carry back.
"""
import re, sys, unicodedata

vol, path = sys.argv[1], sys.argv[2]
raw = open(path, encoding="utf-8", errors="replace").read()
# join hyphenated line breaks, collapse whitespace but keep paragraph breaks
raw = re.sub(r"-\s*\n\s*(?=[a-z])", "", raw)
raw = re.sub(r"[ \t]+", " ", raw)
raw = re.sub(r"\n\s*\n+", "\n\n", raw)
raw = re.sub(r"(?<!\n)\n(?!\n)", " ", raw)
text = raw

GARBLE = {"4": "a", "é": "a", "á": "a", "à": "a", "â": "a", "ä": "a", "ã": "a", "6": "o",
          "0": "o", "1": "i", "|": "i", "!": "i"}


def skel_char(ch, prev, nxt):
    if ch in GARBLE and ch.isdigit() or ch in "|!":
        # digits / bars only count as letters when inside a word
        if prev.isalpha() and nxt.isalpha():
            return GARBLE[ch]
        return ch.lower()
    if ch in GARBLE:
        return GARBLE[ch]
    base = unicodedata.normalize("NFKD", ch)[0]
    return base.lower() if len(base) == 1 else "?"


skel = "".join(skel_char(c, text[i - 1] if i else " ", text[i + 1] if i + 1 < len(text) else " ")
               for i, c in enumerate(text))
assert len(skel) == len(text)

# vowel class tolerant of OCR: a e o i u and leftovers
V = r"[aeiouy]"
LEX = [
    # Śaṅkara / Smārta
    ("SMARTA", r"\bsm[a-z]{0,2}r?ts?\b|\bsmarth?a?s?\b|\bsmarta"),
    ("SHANKARACHARYA", r"\bs[h]?[a-z]?nk[a-z]?r[a-z]{0,2}ch[a-z]{0,2}r[iy]?a?\b|\bshankar[a-z]{0,3}ch|\bsankar[a-z]{0,3}ch"),
    ("SRINGERI", r"\bs[h]?r[i1l]?[a-z]?ng[ae]?r[iy]\b|\bs[h]?r[i1l]ng[a-z]?ri\b"),
    ("SANKESHVAR", r"\bs[h]?[a-z]nk[e]?sh?[vw][a-z]r\b"),
    ("KUDALI", r"\bk[uo]d[a-z]?l[iy]\b"),
    ("KARVIR_PITHA", r"\bkarv[i1]r\b.{0,40}\b(?:math|pith|sv[a-z]m[i1]|swami|shankar)"),
    ("DVARKA_PITHA", r"\bd[vw][a-z]rk[a-z]\b.{0,40}\b(?:math|pith|shankar)"),
    ("ADVAITA", r"\badv[a-z]{1,2}t[a-z]?\b|\badwait|\bved[a-z]nt[a-z]?\b"),
    ("DASHNAMI", r"\bd[a-z]?sh?n[a-z]m|\bgos[a-z]v[i1]s?\b|\bgos[a-z]{0,2}[i1]ns?\b|\bs[a-z]nn?y[a-z]s[i1]"),
    ("BHAGVAT", r"\bbh[a-z]g[a-z]?v[a-z]?ts?\b"),
    # Vaiṣṇava
    ("MADHVA", r"\bm[a-z]dhv(?:[a-z]{0,2}ch|a\b|as\b|s\b)|\buttr[a-z]d[iy]|\br[a-z]gh[a-z]vendr|\bvy[a-z]sr[a-z]y"),
    ("RAMANUJA", r"\br[a-z]m[a-z]n[uo]j|\bs[h]?r[i1]\s?v[a-z]{1,2}shn[a-z]v|\bt[ae]ng[a-z]l|\bv[a-z]d[a-z]g[a-z]l"),
    ("VALLABHA", r"\bv[a-z]ll[a-z]bh|\bpusht[i1]|\bgos[a-z]{0,2}[i1]j[i1]\s+m[a-z]h[a-z]r[a-z]j"),
    ("SVAMINARAYAN", r"\bs[vw][a-z]m[i1]n[a-z]r[a-z]y[a-z]n"),
    ("RAMANANDI", r"\br[a-z]m[a-z]nand|\br[a-z]m[a-z]v[a-z]t|\bb[a-z]{1,2}r[a-z]g[i1]s?\b"),
    ("VAISHNAV", r"\bv[a-z]{1,2}shn[a-z]vs?\b|\bvaishn"),
    ("SHAIVA", r"\bsh?[a-z]{1,2}v[a-z]?s?\b(?=\s+(?:and|or|by|sect))|\bshaiv|\bsaiv"),
    ("LINGAYAT", r"\bl[i1]ng[a-z]{1,2}y[a-z]ts?\b"),
    ("NATH", r"\bk[a-z]nph[a-z]t|\bn[a-z]th\s?p[a-z]nth|\bgor[a-z]?kh?n[a-z]th"),
    ("KABIR", r"\bk[a-z]b[i1]rp[a-z]nth|\bk[a-z]b[i1]r\b"),
    ("WARKARI", r"\bv[a-z]rk[a-z]r[i1]|\bw[a-z]rk[a-z]r[i1]"),
    ("MAHANUBHAV", r"\bm[a-z]h[a-z]nubh[a-z]v|\bm[a-z]nbh[a-z]v"),
    ("GURU", r"\bspiritual\s+(?:teacher|guide|head|guru|adviser|lord)|\bguru\b|\bpontiff|\bsv[a-z]m[i1]\b|\bswami\b|\bmath\b|\bmonaster"),
]
LEXC = [(lab, re.compile(p)) for lab, p in LEX]
CORE = {"SMARTA", "SHANKARACHARYA", "SRINGERI", "SANKESHVAR", "KUDALI", "KARVIR_PITHA", "DVARKA_PITHA",
        "MADHVA", "RAMANUJA", "VALLABHA", "SVAMINARAYAN", "RAMANANDI", "VAISHNAV", "BHAGVAT",
        "SHAIVA", "LINGAYAT", "DASHNAMI", "NATH", "KABIR", "MAHANUBHAV", "ADVAITA"}

# page numbers from running heads: "[Bombay Gazetteer, 56 DISTRICTS." or "DHARWAR. 57"
PAGE_RE = re.compile(r"Bombay\s+Gazetteer,?\]?\s+(\d{1,4})\b|\b[A-Z]{4,}[.:,]?\s+(\d{1,4})\s*\n")
pages = [(m.start(), m.group(1) or m.group(2)) for m in PAGE_RE.finditer(text)]

# caste-account openings: a paragraph that begins "Name(s)[ or Name], [...] numbering/returned/are found/..."
HEAD_RE = re.compile(
    r"(?:^|\n\n)\s*([A-Z][A-Za-zÀ-ɏ'’]+(?:[ -][A-Z][A-Za-zÀ-ɏ'’]+){0,2}"
    r"(?:,?\s+or\s+[A-Z][^,.\n]{1,40})?)"
    r"(?:,|\s)[^.\n]{0,120}?"
    r"\b(?:numbering|numbered|returned|number about|are found|are a |are said|strength of|are|is)\b[^.\n]{0,40}?"
    r"(?:(?:about|in all|as)\s+)?([\d,]{2,9})?",
)
heads = []
for m in HEAD_RE.finditer(text):
    name = m.group(1).strip()
    if len(name) < 3 or name.split()[0] in {"The", "They", "These", "This", "In", "Their", "Of", "On", "At", "A", "As",
                                          "When", "Chapter", "Population", "Some", "Most", "All", "Besides", "Under",
                                          "Among", "There", "It", "He", "She", "Each", "From", "Like", "With", "If",
                                          "Before", "After", "Except", "During", "Since", "Both", "Many", "Few", "To",
                                          "Its", "Every", "Such", "Its", "Then", "That", "Formerly", "Except"}:
        continue
    heads.append((m.start(), name, (m.group(2) or "").strip(",")))

# population chapter span: first "Chapter III" + "Population" to first "Chapter IV"
pop_start = re.search(r"Chapter\s+I[IT1l]{2}\.?\s+Population", text)
pop_end = re.search(r"Chapter\s+I[V¥]\.?\s+(?:Agriculture|Agri)", text)
ps = pop_start.start() if pop_start else -1
pe = pop_end.start() if pop_end and pop_end.start() > ps else len(text)

# sentences
sent_spans = []
start = 0
for m in re.finditer(r"(?<=[a-z\)\]’'”])[.;]\s+(?=[A-Z‘'\"“])|\n\n", text):
    sent_spans.append((start, m.end()))
    start = m.end()
sent_spans.append((start, len(text)))

import bisect
page_pos = [p for p, _ in pages]
head_pos = [h[0] for h in heads]

print("vol\toffset\tpage\tsection\tcaste_head\thead_count\tlabels\tsentence")
for a, b in sent_spans:
    s = skel[a:b]
    labs = [lab for lab, rx in LEXC if rx.search(s)]
    if not (set(labs) & CORE):
        continue
    sent = re.sub(r"\s+", " ", text[a:b]).strip()
    if len(sent) > 600:
        sent = sent[:600] + "…"
    i = bisect.bisect_right(page_pos, a) - 1
    page = pages[i][1] if i >= 0 else ""
    j = bisect.bisect_right(head_pos, a) - 1
    hname, hcount = (heads[j][1], heads[j][2]) if j >= 0 and a - heads[j][0] < 20000 else ("", "")
    section = "population" if ps <= a < pe else "other"
    print("\t".join([vol, str(a), page, section, hname, hcount, ",".join(labs), sent.replace("\t", " ")]))
