#!/usr/bin/env python3
"""Classify the Karnataka State Archives items found by description search (Sringeri / Kudli variants).
Usage: python3 -I mathas/archives/scripts/classify.py mathas/data/archives/ksa_list.tsv > mathas/archives/results/catalogue.tsv
Columns: identifier year title description matha topic include
"""
import csv, re, sys
rows = [r for r in csv.reader(open(sys.argv[1], encoding="utf-8"), delimiter="\t") if len(r) >= 4]
def matha(d):
    if re.search(r"akshobhya|ashobhya|ahobala|uttaradi|raghavendra|vyasaraja", d, re.I) and not re.search(r"sringeri|singeri", d, re.I): return "madhva (exclude)"
    if re.search(r"kud(?:l[ie]?|i)\s*(?:sri\s*)?s[h]?ri?n?ge?r|kund?li\s*s[h]?ri?n?ge?r|kudli sri sringeri|kundli sringeri|kudi sringeri|kudli swami|kudli and murgi|kudli singeri|kudli matt\b|kudli matta|kudli mutt|kudli math", d, re.I): return "kudli_sringeri"
    if re.search(r"avani", d, re.I): return "avani_sringeri"
    if re.search(r"hubli sringeri", d, re.I): return "hubli_sringeri"
    if re.search(r"s[h]?ri?n?ge?r|sringa", d, re.I): return "sringeri"
    if re.search(r"kudli", d, re.I): return "kudli (place/temple)"
    return "?"
TOPICS = [("succession", r"succession|successor|appoint\w* (of )?sri chandra|sanyas|demise|nominat|priestship|recogni[sz]\w* .*guru|rightful owner"),
          ("honours_tour", r"visit|tour|honou?r|insignia|rahadari|palakki|palanquin|procession|guard|escort|ceremonial|biksha|reception|maryad|isthakapal|swords|arms regul"),
          ("estate_revenue", r"inam|jah?a?gh?ir|ganja|toddy|excise|kandayam|nazarana|land revenue|tasdik|cash allowance|mineral|cart tax|cattle pound|village|lease|mortgage|forest|sandalwood|quarry"),
          ("management_finance", r"management|loan|budget|mismanag|affairs|agent|officer in charge|audit|dearness|salary|allowance|recovery|legac|shares|o\.s\. no|suit|civil courts"),
          ("branches_property", r"branch|benar|rames|tirupati|nasik|haridwar|sultanpet|madras|coimbatore|tinnevel|erode|ramanad|outside the state|sangli|dharwar|bijapur"),
          ("municipal_local", r"municipal|sweeper|school|road|well|plague|infected|taluk|sheristedar|toddy revenue of the inamdar|car festival|jatra|police guard"),
         ]
w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
w.writerow(["identifier", "year", "title", "description", "matha", "topic", "include"])
for ident, yr, title, desc in [r[:4] for r in rows]:
    m = matha(desc)
    topics = [t for t, p in TOPICS if re.search(p, desc, re.I)]
    topic = ";".join(topics) or "other"
    newspaper = "Pathrike" in desc
    gazette_notice = bool(re.match(r"^\d", title)) and "MUZ" not in title.upper()
    inc = "no" if (m in ("madhva (exclude)", "?") or newspaper) else "yes"
    if m == "kudli (place/temple)" and not re.search(r"inam|temple|mutt|matt", desc, re.I): inc = "no"
    if gazette_notice and re.search(r"plague|infected|SAN |HOBLIES|ESTATE OF LATE|ABDUL", desc): inc = "no"
    w.writerow([ident, yr, title, desc, m, topic, inc])
