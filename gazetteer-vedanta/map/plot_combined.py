#!/usr/bin/env python3
"""Combined map of Śaṅkara's following across the six regions (Bombay, Madras, UP, Bengal, Punjab, CP).

Usage: python3 map/plot_combined.py   (from gazetteer-vedanta/; needs matplotlib, so not -I)
Writes map/combined_map.png and map/combined_points.tsv.

Two layers, circle AREA proportional to persons (no common denominator exists across the sources):
  ochre  = Daśanāmī persons by district:
           UP 1891 Goshain-Dasnami; Bengal 1901 Atith; CP 1891 Gosain (all sub-divisions);
           Punjab 1891 Gosain + Sanniasi (Faqir sub-heads); Madras 1891 Sanyasi;
           Bombay 1881 Gosavi, by region only (dashed outline, at regional centres).
  teal   = Smārta persons:
           Bombay: castes the 1880s gazetteers assert are Smārta or split Smārta/Bhāgavata
                   (results/smarta_range.tsv, `with_mixed`; census 1881/1872 caste figures);
           Madras Tamil division 1891: Brahman sub-castes listed by Thurston as Smārta
                   (census-images/results/madras1891_tamil_smarta_vs_aiyangar.tsv).
Coordinates are approximate district headquarters (schematic). Country outlines: Natural Earth 1:50m.
"""
import csv, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

OCHRE, TEAL = "#b5651d", "#008b9a"
INK, MUTED, LAND, SEA, EDGE = "#1d2128", "#5c6470", "#efeee9", "#ffffff", "#b9bcb4"

XY = {  # district: (lat, lon), approximate headquarters
    # UP
    "Dehra Dun": (30.32, 78.03), "Saharanpur": (29.97, 77.55), "Muzaffarnagar": (29.47, 77.70), "Meerut": (28.98, 77.71),
    "Bulandshahr": (28.40, 77.85), "Aligarh": (27.88, 78.08), "Muttra": (27.49, 77.67), "Agra": (27.18, 78.01),
    "Farukhabad": (27.39, 79.58), "Mainpuri": (27.23, 79.02), "Etawah": (26.78, 79.02), "Etah": (27.56, 78.66),
    "Bareilly": (28.37, 79.43), "Bijnor": (29.37, 78.14), "Budaun": (28.04, 79.12), "Moradabad": (28.84, 78.77),
    "Shahjahanpur": (27.88, 79.91), "Pilibhit": (28.63, 79.80), "Cawnpore": (26.45, 80.33), "Fatehpur": (25.93, 80.81),
    "Banda": (25.48, 80.33), "Hamirpur": (25.95, 80.15), "Allahabad": (25.44, 81.85), "Jhansi": (25.45, 78.57),
    "Jalaun": (26.15, 79.33), "Lalitpur": (24.69, 78.42), "Benares": (25.32, 83.01), "Mirzapur": (25.15, 82.57),
    "Jaunpur": (25.75, 82.69), "Ghazipur": (25.58, 83.58), "Ballia": (25.76, 84.15), "Gorakhpur": (26.76, 83.37),
    "Basti": (26.80, 82.73), "Azamgarh": (26.07, 83.18), "Kumaun": (29.60, 79.66), "Garhwal": (30.15, 78.78),
    "Tarai": (28.98, 79.40), "Lucknow": (26.85, 80.95), "Unao": (26.55, 80.49), "Rae Bareli": (26.23, 81.24),
    "Sitapur": (27.57, 80.68), "Hardoi": (27.40, 80.13), "Kheri": (27.95, 80.78), "Fyzabad": (26.78, 82.13),
    "Gonda": (27.13, 81.97), "Bahraich": (27.57, 81.60), "Sultanpur": (26.26, 82.07), "Partabgarh": (25.90, 81.95),
    "Bara Banki": (26.93, 81.19),
    # Bengal, Bihar, Chota Nagpur
    "Calcutta": (22.57, 88.36), "Murshidabad": (24.18, 88.27), "Rajshahi": (24.37, 88.60), "Jalpaiguri": (26.52, 88.72),
    "Darjeeling": (27.04, 88.26), "Rangpur": (25.75, 89.25), "Pabna": (24.00, 89.24), "Patna": (25.59, 85.14),
    "Gaya": (24.79, 85.00), "Shahabad": (25.56, 84.66), "Saran": (25.78, 84.73), "Champaran": (26.65, 84.92),
    "Muzaffarpur": (26.12, 85.39), "Monghyr": (25.38, 86.47), "Bhagalpur": (25.25, 87.01), "Malda": (25.00, 88.14),
    "Hazaribagh": (23.99, 85.36), "Ranchi": (23.34, 85.31), "Palamau": (24.04, 84.07), "Singhbhum": (22.55, 85.81),
    "Hill Tippera": (23.84, 91.28),
    # Central Provinces
    "Saugor": (23.84, 78.74), "Damoh": (23.83, 79.44), "Jubbulpore": (23.18, 79.95), "Mandla": (22.60, 80.37),
    "Seoni": (22.09, 79.55), "Narsinghpur": (22.95, 79.19), "Hoshangabad": (22.75, 77.72), "Nimar": (21.82, 76.35),
    "Betul": (21.90, 77.90), "Chhindwara": (22.06, 78.94), "Wardha": (20.74, 78.60), "Nagpur": (21.15, 79.09),
    "Chanda": (19.96, 79.30), "Bhandara": (21.17, 79.65), "Balaghat": (21.80, 80.18), "Raipur": (21.25, 81.63),
    "Bilaspur": (22.08, 82.15), "Sambalpur": (21.47, 83.97), "Bastar": (19.08, 82.02), "Kanker": (20.27, 81.49),
    "Nandgaon": (21.10, 81.03), "Khairagarh": (21.42, 80.98), "Chhuikhadan": (21.52, 80.99), "Kawardha": (22.01, 81.23),
    "Sakti": (22.03, 82.96), "Raigarh": (21.90, 83.40), "Sarangarh": (21.59, 83.08), "Bamra": (21.62, 84.20),
    "Rairakhol": (21.07, 84.38), "Sonpur": (20.84, 83.92), "Kalahandi": (19.91, 83.17), "Makrai": (22.07, 77.10),
    # Punjab
    "Hissar": (29.15, 75.72), "Rohtak": (28.90, 76.61), "Gurgaon": (28.46, 77.03), "Delhi": (28.65, 77.23),
    "Karnal": (29.69, 76.99), "Ambala": (30.38, 76.78), "Simla": (31.10, 77.17), "Kangra": (32.10, 76.27),
    "Hoshiarpur": (31.53, 75.91), "Jalandhar": (31.33, 75.58), "Ludhiana": (30.90, 75.85), "Firozpur": (30.93, 74.61),
    "Multan": (30.20, 71.47), "Jhang": (31.27, 72.32), "Montgomery": (30.66, 73.11), "Lahore": (31.55, 74.34),
    "Amritsar": (31.63, 74.87), "Gurdaspur": (32.04, 75.40), "Sialkot": (32.49, 74.53), "Gujrat": (32.57, 74.08),
    "Gujranwala": (32.16, 74.19), "Shahpur": (32.27, 72.47), "Jhelum": (32.93, 73.73), "Rawalpindi": (33.60, 73.05),
    "Hazara": (34.15, 73.21), "Peshawar": (34.01, 71.58), "Kohat": (33.59, 71.44), "Bannu": (32.99, 70.60),
    "Dera Ismail Khan": (31.83, 70.90), "Dera Ghazi Khan": (30.05, 70.63), "Muzaffargarh": (30.07, 71.19),
    # Madras
    "Anantapur": (14.68, 77.60), "Bellary": (15.14, 76.92), "Chingleput": (12.69, 79.98), "Cuddapah": (14.47, 78.82),
    "Ganjam": (19.31, 84.79), "Godavari": (16.99, 82.25), "Kistna": (16.19, 81.13), "Kurnool": (15.83, 78.04),
    "Madras": (13.08, 80.27), "Madura": (9.93, 78.12), "Malabar": (11.25, 75.78), "Nellore": (14.44, 79.99),
    "North Arcot": (12.92, 79.13), "Salem": (11.66, 78.15), "South Canara": (12.87, 74.84), "Tanjore": (10.79, 79.14),
    "Travancore": (8.52, 76.94), "Vizagapatam": (17.69, 83.22), "Coimbatore": (11.02, 76.96), "Nilgiris": (11.41, 76.70),
    "South Arcot": (11.75, 79.75), "Trichinopoly": (10.80, 78.69), "Tinnevelly": (8.73, 77.70), "Pudukota": (10.38, 78.82),
    # Bombay
    "Ratnagiri": (16.99, 73.30), "Kolaba": (18.64, 72.87), "Thana": (19.20, 72.97), "Kanara": (14.81, 74.13),
    "Nasik": (20.00, 73.79), "Ahmadnagar": (19.09, 74.74), "Poona": (18.52, 73.86), "Satara": (17.68, 74.00),
    "Sholapur": (17.66, 75.91), "Belgaum": (15.85, 74.50), "Dharwar": (15.46, 75.01), "Bijapur": (16.83, 75.71),
    "Kolhapur": (16.70, 74.24),
}
GOSAVI_1881 = {"Deccan": (19.0, 75.6, 19247), "Gujarat": (22.6, 72.4, 6036), "Konkan": (17.9, 73.15, 5269),
               "Karnatak": (15.9, 75.6, 1352), "Bombay City": (18.95, 72.83, 1947)}


def num(x):
    try:
        return int(str(x).replace(",", "").strip() or 0)
    except ValueError:
        return 0


R = "census-images/results/"
pts = []  # (layer, region, district, persons, source)
for r in csv.DictReader(open(R + "up1891_goshain.tsv"), delimiter="\t"):
    if r["serial"] != "T":
        pts.append(("dasnami", "UP", r["district"], num(r["dasnami_m"]) + num(r["dasnami_f"]), "UP 1891 Goshain-Dasnami"))
for r in csv.DictReader(open(R + "bengal1901_atith_gosain.tsv"), delimiter="\t"):
    if r["district"] != "TOTAL":
        pts.append(("dasnami", "Bengal", r["district"], num(r["atith_total"]), "Bengal 1901 Atith"))
for r in csv.DictReader(open(R + "cp1891_castes.tsv"), delimiter="\t"):
    if r["sex"] == "persons" and not r["district_or_state"].startswith("TOTAL"):
        pts.append(("dasnami", "CP", r["district_or_state"], num(r["gosain"]), "CP 1891 Gosain"))
for r in csv.DictReader(open(R + "punjab1891_castes.tsv"), delimiter="\t"):
    if not r["district"].startswith("TOTAL"):
        pts.append(("dasnami", "Punjab", r["district"], num(r["gosain_t"]) + num(r["sanniasi_t"]), "Punjab 1891 Gosain+Sanniasi"))
for r in csv.DictReader(open(R + "madras1891_devotees.tsv"), delimiter="\t"):
    if r["sub_division"] == "Sanyasi" and r["district"] != "Division total":
        pts.append(("dasnami", "Madras", r["district"], num(r["persons"]), "Madras 1891 Sanyasi"))
for r in csv.DictReader(open("results/smarta_range.tsv"), delimiter="\t"):
    if r["district"] in XY:
        pts.append(("smarta", "Bombay", r["district"], num(r["with_mixed"]), f"Bombay gazetteer castes asserted/split Smarta ({r['census']})"))
for r in csv.DictReader(open(R + "madras1891_tamil_smarta_vs_aiyangar.tsv"), delimiter="\t"):
    if r["district"] in XY:
        pts.append(("smarta", "Madras", r["district"], num(r["smarta_thurston"]), "Madras 1891 Tamil Smarta sub-castes (Thurston list)"))

missing = sorted({p[2] for p in pts if p[2] not in XY and p[3] > 0})
pts = [p for p in pts if p[2] in XY and p[3] > 0]
with open("map/combined_points.tsv", "w", encoding="utf-8") as f:
    f.write("layer\tregion\tdistrict\tlat\tlon\tpersons\tsource\n")
    for p in pts:
        f.write(f"{p[0]}\t{p[1]}\t{p[2]}\t{XY[p[2]][0]}\t{XY[p[2]][1]}\t{p[3]}\t{p[4]}\n")

SCALE = 0.012  # points^2 per person -> 10,000 persons = 120 pt^2
fig, ax = plt.subplots(figsize=(9.0, 12.2), dpi=170)
fig.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.235)
fig.patch.set_facecolor(SEA)
ax.set_facecolor(SEA)
gj = json.load(open("map/ne_50m_admin0.geojson"))
for feat in gj["features"]:
    if feat["properties"].get("ADM0_A3") not in {"IND", "PAK", "BGD", "NPL", "BTN", "LKA", "MMR", "CHN", "AFG"}:
        continue
    g = feat["geometry"]
    polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    for poly in polys:
        xs, ys = zip(*poly[0])
        ax.fill(xs, ys, color=LAND, ec=EDGE, lw=0.5, zorder=0)

for layer, col, z in (("smarta", TEAL, 2), ("dasnami", OCHRE, 3)):
    P = sorted([p for p in pts if p[0] == layer], key=lambda p: -p[3])  # large first, small on top
    ax.scatter([XY[p[2]][1] for p in P], [XY[p[2]][0] for p in P], s=[p[3] * SCALE for p in P],
               c=col, alpha=0.72, edgecolors="white", linewidths=0.8, zorder=z)
for name, (la, lo, n) in GOSAVI_1881.items():
    ax.scatter([lo], [la], s=[n * SCALE], facecolors="none", edgecolors=OCHRE, linewidths=1.3, linestyle=(0, (3, 2)), zorder=4)

# Śaṅkara maṭhas located by the colonial gazetteers (mathas/results/mathas.tsv, sringeri/results/places.tsv).
# kind: seat = a named Śaṅkara seat; dep = branch, estate or temple of a named seat; other = Smārta house or
# Śaṅkarācārya site tied to no named seat. (lat, lon, label, dx, dy, ha)
MATHAS = [
    ("seat", 13.42, 75.25, "Śṛṅgeri", -0.35, -0.35, "right"),
    ("seat", 16.27, 74.48, "Saṅkeśvar", 0.35, 0.05, "left"),
    ("seat", 22.24, 68.97, "Dvārkā", 0.3, 0.35, "left"),
    ("seat", 30.56, 79.56, "Jyotirmaṭh", 0.35, 0.3, "left"),
    ("seat", 19.81, 85.83, "Purī", 0.35, -0.2, "left"),
    ("seat", 10.96, 79.38, "Kumbakoṇam", 0.4, 0.45, "left"),
    ("seat", 14.00, 75.68, "Kudali", 0.3, -0.32, "left"),
    ("seat", 13.17, 77.22, "Śivagaṅgā", 0.35, 0.15, "left"),
    ("dep", 16.70, 74.24, "Kolhapur", -0.95, 0.45, "right"),
    ("dep", 16.63, 74.70, "", 0, 0, "left"),        # Khidrapur, inām village of Saṅkeśvar
    ("dep", 14.87, 75.68, "", 0, 0, "left"),        # Hallur, village of the Kudali svāmī
    ("dep", 15.36, 75.12, "", 0, 0, "left"),        # Hubli, Kudali svāmī's procession privilege
    ("dep", 12.83, 79.70, "Conjeeveram", -0.3, -0.4, "right"),  # temple managed from Kumbakoṇam
    ("other", 20.00, 73.79, "Nasik", -0.35, 0.3, "right"),
    ("other", 19.40, 72.80, "Nirmal", -0.35, -0.1, "right"),
    ("other", 24.70, 84.99, "Bodh Gayā", 0.3, -0.45, "left"),
    ("other", 14.72, 74.82, "", 0, 0, "left"),      # Sonda, Svarṇavallī
    ("other", 13.10, 78.33, "", 0, 0, "left"),      # Avani, Smārta guru
    ("other", 18.66, 77.88, "", 0, 0, "left"),      # Bodhan, Bhāskarācārya
    ("other", 19.15, 77.31, "", 0, 0, "left"),      # Nander, Bhāskarācārya
    ("other", 15.64, 74.51, "", 0, 0, "left"),      # Khanapur, Shenvi Smārta svāmī
    # Branch maṭhs and houses of Śṛṅgeri (and Kudli's Bombay residence) named in the Mysore government files,
    # 1891–1945 (mathas/archives/results/archive_rows.tsv)
    ("arch", 9.29, 79.31, "Rameswaram", 0.3, -0.15, "left"),
    ("arch", 10.17, 76.44, "Kaladi", -0.3, -0.1, "right"),
    ("arch", 13.63, 79.42, "Tirupati", 0.3, 0.2, "left"),
    ("arch", 29.95, 78.16, "Haridwar", -0.3, 0.15, "right"),
    ("arch", 25.32, 83.01, "Benares", -0.25, 0.4, "right"),
    ("arch", 24.79, 85.00, "", 0, 0, "left"),       # Gaya
    ("arch", 9.93, 78.12, "", 0, 0, "left"),        # Madura
    ("arch", 12.97, 77.58, "Bangalore", -0.25, -0.45, "right"),
    ("arch", 13.70, 75.24, "", 0, 0, "left"),       # Tīrthamuttūr, a 'vassal Mutt'
    ("arch", 14.55, 75.70, "", 0, 0, "left"),       # Udagatti, Kudli svāmīs' residence in Bombay
]
# Kudli Śṛṅgeri maṭh: taluks and states outside Mysore holding its properties, from its Agent's list of March 1934
# (mathas/archives/results/coded/K.tsv, K32). Hyderabad State is left out: it reported no property found.
# Approximate taluk headquarters.
KUDLI_ESTATES = [
    (14.62, 75.62, "Ranibennur"), (14.86, 75.45, "Karajgi"), (14.76, 75.12, "Hangal"), (14.46, 75.39, "Kod"),
    (14.99, 75.22, "Shiggaon"), (15.56, 75.37, "Navalgund"), (15.18, 74.97, "Kalghatgi"), (15.46, 75.01, "Dharwar"),
    (15.36, 75.12, "Hubli"), (15.70, 75.73, "Ron"), (15.43, 75.63, "Gadag"),            # Dharwar District
    (14.97, 75.04, "Mundgod"),                                                          # North Kanara
    (15.77, 75.12, "Parasgad"),                                                         # Belgaum
    (15.92, 75.68, "Badami"), (16.18, 75.70, "Bagalkot"), (16.57, 75.97, "Bagevadi"), (16.83, 75.71, "Bijapur"),
    (16.92, 76.23, "Sindgi"), (16.06, 76.06, "Hungund"),                                # Bijapur District
    (14.90, 76.38, "Kudligi"), (14.79, 75.99, "Harapanahalli"),                         # Bellary
    (13.94, 77.27, "Madakasira"),                                                       # Anantapur
    (15.97, 75.16, "Torgal (Kolhapur State)"), (15.95, 75.30, "Ramdurg"), (15.23, 75.58, "Shirahatti (Sangli)"),
    (15.13, 75.47, "Lakshmeshwar (Miraj Sr)"), (15.12, 75.37, "Gudageri (Miraj Jr)"), (14.97, 75.33, "Savanur"),
    (15.68, 75.27, "Sirasangi"), (15.26, 75.25, "Kundgol (Jamkhandi)"),
]
ax.scatter([e[1] for e in KUDLI_ESTATES], [e[0] for e in KUDLI_ESTATES], marker="x", s=13, c=INK, linewidths=0.9,
           alpha=0.85, zorder=6)
ax.annotate("Kudli's Bombay estates\n(1934 list, ×)", (75.9, 16.4), xytext=(77.6, 17.6), fontsize=7.2, color=MUTED, zorder=8,
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
# Rival centres noted in the synthesis ("Rivals: who else held the ground"): (lat, lon, label, dx, dy, ha)
RIVALS = [
    (26.80, 82.20, "Ayodhyā (Bairāgī)", -0.25, -0.6, "right"),
    (27.49, 77.67, "Mathura (Vallabha, Gauḍīya)", -0.3, -0.45, "right"),
    (26.76, 83.37, "", 0, 0, "left"),               # Gorakhpur: Nāth Jogīs (district already labelled)
    (29.69, 76.99, "Karnal (Nāth)", -0.3, 0.0, "right"),
    (13.34, 74.75, "Uḍupi (Mādhva)", -0.3, 0.1, "right"),
    (22.57, 88.36, "Calcutta\n(Kālī, Vaiṣṇava,\nBrahmo)", 0.25, -1.0, "left"),
    # rival seats from the coded rivals layer (rivals/README.md)
    (32.88, 73.36, "Tilla (Nāth)", 0.3, 0.2, "left"),
    (28.86, 76.65, "", 0, 0, "left"),               # Bohar: Nāth maṭh (Rohtak)
    (32.03, 75.03, "", 0, 0, "left"),               # Dera Baba Nanak: Udāsī
    (21.10, 81.03, "Nandgaon (Bairāgī state)", -0.3, -0.5, "right"),
    (22.28, 81.70, "", 0, 0, "left"),               # Lormi: Bairāgī estate
    (22.01, 81.23, "", 0, 0, "left"),               # Kawardha: Kabīrpanthī gaddī
    (11.03, 79.53, "", 0, 0, "left"),               # Tiruvāvaḍuturai: Tamil Śaiva ādhīnam
    (11.08, 79.65, "", 0, 0, "left"),               # Dharmapuram: Tamil Śaiva ādhīnam
    (14.23, 76.40, "Chitradurga (Liṅgāyat)", 0.3, 0.25, "left"),
    (22.60, 72.87, "Vadtal (Svāminārāyaṇa)", 0.3, 0.3, "left"),
]
ax.scatter([r[1] for r in RIVALS], [r[0] for r in RIVALS], marker="P", s=34, c="#7a4fa3", edgecolors="white",
           linewidths=0.6, zorder=7)
for la, lo, txt, dx, dy, ha in RIVALS:
    if txt:
        ax.annotate(txt, (lo, la), xytext=(lo + dx, la + dy), fontsize=7, color="#7a4fa3", style="italic", zorder=8,
                    ha=ha, va="center")
MSTYLE = {"seat": dict(marker="D", s=46, c=INK, edgecolors="white", linewidths=1.0),
          "dep": dict(marker="D", s=20, facecolors="white", edgecolors=INK, linewidths=1.1),
          "other": dict(marker="s", s=14, facecolors="white", edgecolors=MUTED, linewidths=1.0),
          "arch": dict(marker="^", s=24, facecolors="white", edgecolors=INK, linewidths=1.1)}
for kind in ("arch", "other", "dep", "seat"):
    P = [m for m in MATHAS if m[0] == kind]
    ax.scatter([m[2] for m in P], [m[1] for m in P], zorder=7, **MSTYLE[kind])
for kind, la, lo, txt, dx, dy, ha in MATHAS:
    if txt:
        ax.annotate(txt, (lo, la), xytext=(lo + dx, la + dy), fontsize=7.6 if kind == "seat" else 7, zorder=8,
                    color=MUTED if kind in ("other", "arch") else INK, fontweight="bold" if kind == "seat" else "normal",
                    ha=ha, va="center")
with open("map/mathas_points.tsv", "w", encoding="utf-8") as f:
    f.write("kind\tlat\tlon\tlabel\n")
    for m in MATHAS:
        f.write(f"{m[0]}\t{m[1]}\t{m[2]}\t{m[3]}\n")

LABEL = {  # selective direct labels: the places the text discusses
    "Kanara": ("Kanara", -0.9, -0.75), "Tinnevelly": ("Tinnevelly", 0.6, 0),
    "Saran": ("Saran", 0, 0.5), "Gonda": ("Gonda", -0.3, 0.6), "Gorakhpur": ("Gorakhpur", 0.35, 0.6),
    "Champaran": ("Champaran", 0.45, 0.25), "Kangra": ("Kangra", 0.3, 0.2), "Hissar": ("Hissar", -0.35, -0.2),
    "Hoshangabad": ("Hoshangabad", -0.5, -0.5), "Raipur": ("Raipur", 0.35, -0.3),
    "Meerut": ("Meerut", -0.3, 0.35),
}
for d, (txt, dx, dy) in LABEL.items():
    la, lo = XY[d]
    ax.annotate(txt, (lo, la), xytext=(lo + dx, la + dy), fontsize=8, color=INK, zorder=6,
                ha="left" if dx >= 0 else "right", va="center")
ax.annotate("Bombay Gosāvīs 1881\n(by region, dashed)", (75.6, 19.0), xytext=(68.3, 20.8), fontsize=7.5, color=MUTED,
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6), zorder=6)

ax.annotate("Gujarat", (72.4, 22.6), xytext=(71.2, 23.3), fontsize=7.5, color=MUTED, zorder=6)
# Inset: census 1891 totals of the Daśanāmīs and rival ascetic orders (census-images/README.md, "Rival orders").
# Daśanāmī = Goshain-Dasnami (NWP), Gosain + Sanniasi (Punjab, whole province), Gosain + Sanyasi (CP British districts).
RIVAL_TOTALS = [
    ("NWP & Oudh", [("Daśanāmī", 103320), ("Jogī", 78387), ("Bairāgī", 31979)]),
    ("Punjab", [("Daśanāmī", 23143), ("Jogī", 91937), ("Bairāgī", 47561), ("Udāsī", 15194)]),
    ("C. Provinces", [("Daśanāmī", 27245), ("Bairāgī", 29298), ("Jogī, Nāth", 11102)]),
]
ins = ax.inset_axes([0.665, 0.035, 0.32, 0.27])
ins.set_facecolor("white")
yy, yt, ylab = 0, [], []
for prov, bars in RIVAL_TOTALS:
    for name, v in bars:
        ins.barh(yy, v, height=0.72, color=OCHRE if name == "Daśanāmī" else "#7a4fa3", alpha=0.85)
        ins.text(v + 1500, yy, f"{name} {v:,}", va="center", fontsize=6.3, color=INK)
        yy -= 1
    ins.text(-2000, yy + len(bars) / 2 + 0.5, prov, ha="right", va="center", fontsize=6.8, color=INK, fontweight="bold")
    yy -= 0.6
ins.set_xlim(0, 150000); ins.set_ylim(yy + 0.2, 0.7)
ins.set_xticks([]); ins.set_yticks([])
for sp in ins.spines.values():
    sp.set_color(EDGE)
ins.set_title("Census 1891: Daśanāmīs and rivals", fontsize=6.8, color=INK, loc="left", pad=3)
ax.set_xlim(67.5, 93.0); ax.set_ylim(7.5, 36.0); ax.set_aspect(1 / 0.92)
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values():
    s.set_visible(False)

handles = [Line2D([], [], marker="o", ls="", ms=9, mfc=OCHRE, mec="white", alpha=0.8,
                  label="Daśanāmī persons (census 1891; Bengal 1901)"),
           Line2D([], [], marker="o", ls="", ms=9, mfc=TEAL, mec="white", alpha=0.8,
                  label="Smārta persons (Bombay 1880s; Tamil Madras 1891)"),
           Line2D([], [], marker="D", ls="", ms=6.5, mfc=INK, mec="white", label="Śaṅkara seat located by the gazetteers"),
           Line2D([], [], marker="D", ls="", ms=4.5, mfc="white", mec=INK, mew=1.1, label="branch, inām village or temple of a seat"),
           Line2D([], [], marker="s", ls="", ms=4, mfc="white", mec=MUTED, label="other Smārta maṭh or Śaṅkarācārya site"),
           Line2D([], [], marker="^", ls="", ms=5.5, mfc="white", mec=INK, mew=1.1, label="Śṛṅgeri branch or house in the Mysore files, 1891–1945"),
           Line2D([], [], marker="x", ls="", ms=5, mec=INK, mew=1.0, label="taluk with Kudli maṭh property outside Mysore (1934)"),
           Line2D([], [], marker="P", ls="", ms=6.5, mfc="#7a4fa3", mec="white", label="rival centre or seat (Vaiṣṇava, Nāth, Udāsī, Liṅgāyat, Śaiva …)")]
for n in (2000, 10000, 50000):
    handles.append(Line2D([], [], marker="o", ls="", ms=(n * SCALE) ** 0.5, mfc="none", mec=MUTED, label=f"{n:,} persons"))
leg = fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.02, 0.11), fontsize=7.6, frameon=False,
                labelspacing=1.5, handletextpad=1.2, ncol=2, columnspacing=2.5)
for t in leg.get_texts():
    t.set_color(INK)
ax.set_title("Śaṅkara's following in British India: Daśanāmī and Smārta persons, and the maṭhas",
             fontsize=12, color=INK, loc="left", pad=32)
ax.text(0, 1.006, "Regional, not dominant: as an organised following it led only on the Kanara coast, among Tamil Brahmans, "
        "in the eastern Ganges plain\nand in the Bombay Karnatak. Elsewhere Vaiṣṇava, Nāth, Udāsī, Bairāgī or Liṅgāyat "
        "bodies held the larger followings (purple crosses).",
        transform=ax.transAxes, ha="left", va="bottom", fontsize=7.6, color=MUTED, style="italic")
import textwrap
FOOT = ("Circle area ∝ persons. Daśanāmī: UP 1891 Goshain-Dasnami, Bengal 1901 Atīth, CP & Punjab 1891 Gosain/Sanniasi, Madras 1891 Sanyāsī; Smārta: Bombay castes asserted Smārta (1880s gazetteers), Tamil Madras 1891 Smārta Brahman sub-castes.\nThe two layers count different things (an order and caste vs a Brahman sect "
         "or caste allegiance) and come from different dates; Smārtas are mapped only where the sources allow "
         "(Bombay Presidency, Tamil Madras).\nGujarat, Bengal proper and the western Punjab show near-zero Daśanāmīs. "
         "District positions are approximate headquarters.\nMaṭhas as located by the gazetteers 1876–1910 (Rice's Mysore incl.); Kolhapur shown as Saṅkeśvar's branch (Karvīr Pīṭha only from c. 1909); triangles from the Mysore government files 1891–1945, unlabelled: Gaya, Madura, Tīrthamuttūr, Udagatti (Kudli); × = 30 taluks and states listed by the Kudli maṭh's Agent in 1934 as holding its properties (Hyderabad omitted: none found). Purple crosses: rival centres and seats (rivals/README.md); unlabelled: Gorakhpur (Nāth), Bohar (Nāth), Dera Baba Nanak (Udāsī), Lormi (Bairāgī), Kawardha (Kabīrpanthī), Tiruvāvaḍuturai and Dharmapuram (Tamil Śaiva). Inset: 1891 census totals; Daśanāmī = Goshain-Dasnami (NWP), Gosain + Sanniasi (Punjab), Gosain + Sanyasi (CP British districts). "
         "Sources: gazetteer-vedanta/ (census-images/, results/, sringeri/, mathas/, mathas/archives/, rivals/).")
FOOT = "\n".join(textwrap.fill(par, 150) for par in FOOT.split("\n"))
fig.text(0.02, 0.008, FOOT, fontsize=6.6, color=MUTED, va="bottom")
plt.savefig("map/combined_map.png", bbox_inches="tight", facecolor=SEA)
print(len(pts), "points; not placed:", missing)
