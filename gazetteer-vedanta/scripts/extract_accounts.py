#!/usr/bin/env python3
"""Segment a Bombay Gazetteer volume into caste accounts and pull out their religious-affiliation statements.

Usage: python3 -I scripts/extract_accounts.py VOL OCRFILE OUT_PREFIX

Writes
  OUT_PREFIX.accounts.tsv  one row per caste account:
      vol, acc_id, page, caste, gloss, population, labels, n_relig_sents, opening
  OUT_PREFIX.statements.tsv  one row per religion sentence inside an account:
      vol, acc_id, page, caste, labels, sentence

A caste account begins at a sentence of the Campbell template
  "<Caste>[, or <gloss>,] [are] returned as numbering [about] <N> ..."  (or "<Caste>, numbering about <N>")
and runs to the next such opening.  Matching is done on a length-preserving "skeleton"
(lowercase, diacritics and OCR vowel garbles folded) so offsets carry back to the original.
"""
import bisect, re, sys, unicodedata

vol, path, out = sys.argv[1], sys.argv[2], sys.argv[3]
text = open(path, encoding="utf-8", errors="replace").read()
text = re.sub(r"-\s*\n\s*(?=[a-z])", "", text)   # de-hyphenate line breaks
text = re.sub(r"\s+", " ", text)

FOLD = {"é": "a", "á": "a", "à": "a", "â": "a", "ä": "a", "ã": "a", "’": "'", "‘": "'"}


def skeleton(t):
    out = []
    for i, c in enumerate(t):
        if c in FOLD:
            out.append(FOLD[c]); continue
        if c in "4106|!" and 0 < i < len(t) - 1 and t[i - 1].isalpha() and t[i + 1].isalpha():
            out.append({"4": "a", "1": "i", "0": "o", "6": "o", "|": "i", "!": "i"}[c]); continue
        b = unicodedata.normalize("NFKD", c)[0]
        out.append(b.lower() if len(b) == 1 else "?")
    return "".join(out)


skel = skeleton(text)
assert len(skel) == len(text)

# ---------------------------------------------------------------- lexicon
LEX = [
    ("SMARTA", r"\bsm[a-z]{1,2}r?ts?\b|\bsmart[h]?a?s?\b"),
    ("SHANKARACHARYA", r"\bs[h]?[a-z]?nk[a-z]?r[a-z]{0,3}ch[a-z]{0,2}r[iy]?a?\b|\bs[h]?ankar[a-z]{0,3}ch"),
    ("SRINGERI", r"\bs[h]?r[i]?[a-z]?ng[ae]?r[iy]\b|\bs[h]?ring[a-z]?ri\b"),
    ("SANKESHVAR", r"\bs[h]?[a-z]nk[e]?sh?[vw][a-z]r\b"),
    ("KUDALI", r"\bk[uo]d[a-z]?l[iy]\b"),
    ("KARVIR_PITHA", r"\bk[a-z]rv[i]r\b"),
    ("ADVAITA", r"\badv[a-z]{1,2}t|\badwait|\bved[a-z]nt"),
    ("GOSAVI", r"\bd[a-z]?sh?n[a-z]m|\bgos[a-z]v[i]s?\b|\bgos[a-z]{0,2}ins?\b|\bs[a-z]nn?y[a-z]s[i]"),
    ("BHAGVAT", r"\bbh[a-z]g[a-z]?v[a-z]?ts?\b"),
    ("MADHVA", r"\bm[a-z]dhv(?:[a-z]{0,2}ch|a\b|as\b|s\b)|\buttr[a-z]d[iy]|\br[a-z]gh[a-z]vendr|\bvy[a-z]sr[a-z]y"),
    ("RAMANUJA", r"\br[a-z]m[a-z]n[uo]j|\bs[h]?r[i]\s?v[a-z]{1,2}shn[a-z]v"),
    ("VALLABHA", r"\bv[a-z]ll[a-z]bh|\bpusht[i]m|\bgos[a-z]{0,2}ij[i]\b|\bm[a-z]h[a-z]r[a-z]j\b"),
    ("SVAMINARAYAN", r"\bs[vw][a-z]m[i]n[a-z]r[a-z]y[a-z]n"),
    ("RAMANANDI", r"\br[a-z]m[a-z]n[a-z]nd|\br[a-z]m[a-z]v[a-z]t|\bb[a-z]{1,2}r[a-z]g[i]s?\b"),
    ("VAISHNAV", r"\bv[a-z]{1,2}shn[a-z]vs?\b|\bvaishn"),
    ("SHAIVA", r"\bsh[a-z]{1,2}v[a-z]?s\b|\bshaiv|\bsaiv"),
    ("LINGAYAT", r"\bl[i]ng[a-z]{1,2}y[a-z]ts?\b|\bjang[a-z]ms?\b"),
    ("NATH", r"\bk[a-z]nph[a-z]t|\bn[a-z]thp[a-z]nth|\bgor[a-z]?kh?n[a-z]th"),
    ("KABIR", r"\bk[a-z]b[i]r"),
    ("MAHANUBHAV", r"\bm[a-z]h[a-z]nubh[a-z]v|\bm[a-z]nbh[a-z]v"),
    ("JAIN", r"\bj[a-z]{1,2}ns?\b"),
    ("MUSLIM", r"\bmusalm[a-z]n|\bp[i]r\b|\bf[a-z]q[i]r"),
]
LEXC = [(lab, re.compile(p)) for lab, p in LEX]
# a sentence counts as a religion statement only if it also has one of these cues
CUE = re.compile(r"spiritual|teacher|guru|pontiff|\bsect|follower|disciple|religio|worship|"
                 r"\bthey are\b|\bare (?:all )?(?:either )?(?:sm|v[a-z]ishn|bh[a-z]g|l[i]ng|m[a-z]dhv)|"
                 r"\bsv[a-z]m[i]\b|\bswami\b|\bmath\b|monaster|initiat|belong")

# ---------------------------------------------------------------- caste-account openings
NUMWORD = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
    "seventeen eighteen nineteen".split())}
NUMWORD.update({"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
                "eighty": 80, "ninety": 90, "hundred": 100})


def parse_count(s):
    s = s.strip().strip(",.")
    d = re.sub(r"[^\d]", "", s)
    if d:
        return int(d)
    tot = 0
    for w in re.split(r"[\s-]+", s):
        if w in NUMWORD:
            tot = tot * 100 if NUMWORD[w] == 100 else tot + NUMWORD[w]
    return tot or None


OPEN = re.compile(
    r"(?:(?<=[.;:|}]\s)|(?<=\]\s)|(?<=\d\s)|(?<=[A-Z]\.\s)|^)"                 # sentence start
    r"(?P<caste>[A-Z][\w'’‘\"À-ɏ-]+(?:\s+[A-Z][\w'’‘\"À-ɏ-]+){0,3})"  # caste name
    r"(?P<gloss>[^.;|\d]{0,170}?)"                                                     # gloss, no full stop
    r",?\s+(?:(?:are|aro|arc|ave|ate|is)\s+)?(?:return[\w-]*\s*(?:ed\s+)?(?:as\s+)?)?"
    r"num[\w-]*\s*b?[\w]*\s+(?:about|abont|only|perhaps about|in all)?\s*"
    r"(?P<n>[\d,]{1,9}|(?:[a-z]+[- ]?){1,3}?)(?=[\s,.;]|$)(?!\s*(?:houses|families|famil))"
)
BAD_FIRST = {"The", "They", "These", "This", "In", "Their", "Of", "On", "At", "A", "As", "When", "Chapter", "Some",
             "Most", "All", "Besides", "Under", "Among", "There", "It", "He", "Each", "From", "Total", "Hindus",
             "Musalmans", "Christians", "Parsis", "Jains"}

# population chapter = span of the marginal running note "Chapter III. Population." (OCR-tolerant)
marks = [m.start() for m in re.finditer(r"Chapter\s*I[IT1lI]{1,2}[.,]?\s*Population", text)]
if marks:
    # drop isolated stray hits: keep the densest run (gaps < 60k chars)
    runs, cur = [], [marks[0]]
    for x in marks[1:]:
        if x - cur[-1] < 60000: cur.append(x)
        else: runs.append(cur); cur = [x]
    runs.append(cur)
    best = max(runs, key=len)
    POP_A, POP_B = max(0, best[0] - 20000), best[-1] + 8000
else:
    POP_A, POP_B = 0, len(text)
print(f"{vol}: population chapter chars {POP_A}-{POP_B} ({len(marks)} marginal notes)", file=sys.stderr)

opens = []
for m in OPEN.finditer(text, POP_A, POP_B):
    caste = m.group("caste")
    if caste.split()[0] in BAD_FIRST:
        continue
    n = parse_count(m.group("n") or "")
    if n is None:
        continue
    opens.append((m.start(), caste, re.sub(r"^\s*,?\s*", "", m.group("gloss") or "").strip(" ,"), n, m.group(0)))

# running-head page numbers: "[Bombay Gazetteer, 56 DISTRICTS." / "DHARWAR. 57"
PAGE = re.compile(r"Bombay\s+Gazetteer,?\]?\s+(\d{1,4})\b|\b[A-Z]{4,}[.:,]?\s+(\d{1,4})(?=\s+[A-Z(‘'])")
pages = [(m.start(), m.group(1) or m.group(2)) for m in PAGE.finditer(text)]
page_pos = [p for p, _ in pages]


def page_at(a):
    i = bisect.bisect_right(page_pos, a) - 1
    return pages[i][1] if i >= 0 else ""


# sentence boundaries
bounds = [0] + [m.end() for m in re.finditer(r"(?<=[a-z\)\]'’”])[.;]\s+(?=[A-Z‘'\"“])", text)] + [len(text)]

acc_rows, st_rows = [], []
for k, (a, caste, gloss, n, opening) in enumerate(opens):
    b = opens[k + 1][0] if k + 1 < len(opens) else min(POP_B, a + 40000)
    b = min(b, a + 40000)
    acc_id = f"{vol}:{k:04d}"
    i0 = bisect.bisect_right(bounds, a) - 1
    labels = {}
    nrel = 0
    for i in range(i0, len(bounds) - 1):
        s0, s1 = bounds[i], bounds[i + 1]
        if s0 >= b:
            break
        sk = skel[s0:s1]
        labs = [lab for lab, rx in LEXC if rx.search(sk)]
        if not labs or not CUE.search(sk):
            continue
        nrel += 1
        for l in labs:
            labels[l] = labels.get(l, 0) + 1
        sent = text[s0:s1].strip()
        st_rows.append([vol, acc_id, page_at(s0), caste, ",".join(labs),
                        (sent[:700] + "…" if len(sent) > 700 else sent)])
    acc_rows.append([vol, acc_id, page_at(a), caste, gloss, str(n),
                     ",".join(f"{l}:{c}" for l, c in sorted(labels.items(), key=lambda x: -x[1])),
                     str(nrel), opening[:160]])

with open(out + ".accounts.tsv", "w", encoding="utf-8") as f:
    f.write("vol\tacc_id\tpage\tcaste\tgloss\tpopulation\tlabels\tn_relig_sents\topening\n")
    for r in acc_rows:
        f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
with open(out + ".statements.tsv", "w", encoding="utf-8") as f:
    f.write("vol\tacc_id\tpage\tcaste\tlabels\tsentence\n")
    for r in st_rows:
        f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
print(f"{vol}: {len(acc_rows)} accounts, {len(st_rows)} religion sentences", file=sys.stderr)
