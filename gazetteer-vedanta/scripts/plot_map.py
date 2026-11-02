#!/usr/bin/env python3
"""Schematic map: share of Hindus stated to follow a Shankaracharya / Smarta teacher, by district.

Usage: python3 scripts/plot_map.py   (from the study directory; needs matplotlib, so not -I) -> results/smarta_map.png

Each district is a dot at its headquarters town (approximate lat/lon; no boundaries).
Colour = tier 2 share ("asserted" + castes split Smarta/Bhagvat), single-hue sequential ramp.
Label = district, asserted–with-mixed range. Grey = no caste-level Smarta data
(Gujarat district volumes, Khandesh: only the 1872 sect census, which has no Smarta class).
"""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize

HQ = {  # district: (lat, lon)
    "Surat": (21.17, 72.83), "Broach": (21.70, 72.98), "Kaira": (22.75, 72.68), "Panch Mahals": (22.78, 73.62),
    "Ahmedabad": (23.03, 72.58), "Cutch": (23.25, 69.67), "Kathiawar": (22.30, 70.80), "Baroda": (22.31, 73.18),
    "Khandesh": (20.90, 74.77), "Nasik": (20.00, 73.79), "Thana": (19.20, 72.97), "Kolaba": (18.64, 72.87),
    "Ratnagiri": (16.99, 73.30), "Ahmadnagar": (19.09, 74.74), "Poona": (18.52, 73.86), "Satara": (17.68, 74.00),
    "Sholapur": (17.66, 75.91), "Kolhapur": (16.70, 74.24), "Belgaum": (15.85, 74.50), "Dharwar": (15.46, 75.01),
    "Bijapur": (16.83, 75.71), "Kanara": (14.81, 74.13),
}
rng = {r["district"]: r for r in csv.DictReader(open("results/smarta_range.tsv", encoding="utf-8"), delimiter="\t")}

ramp = LinearSegmentedColormap.from_list("blue", ["#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"])
norm = Normalize(0, 40)
INK, MUTED, GREY = "#1f1f1d", "#6b6a66", "#c9c8c3"

fig, ax = plt.subplots(figsize=(7.2, 9.2), dpi=160)
fig.patch.set_facecolor("white")
for name, (lat, lon) in HQ.items():
    r = rng.get(name)
    if r and r["with_mixed_pct"]:
        lo, mid = float(r["asserted_pct"]), float(r["with_mixed_pct"])
        ax.scatter(lon, lat, s=260, color=ramp(norm(mid)), edgecolor="white", linewidth=2, zorder=3)
        rngtxt = f"{lo:.1f}%" if abs(mid - lo) < 0.05 else f"{lo:.1f}–{mid:.1f}%"
        left = name in ("Ratnagiri", "Kolaba", "Thana")
        ax.annotate(f"{name}\n{rngtxt}", (lon, lat), xytext=(-10 if left else 10, -2), textcoords="offset points",
                    fontsize=8, color=INK, va="center", ha="right" if left else "left")
    else:
        ax.scatter(lon, lat, s=90, color=GREY, edgecolor="white", linewidth=1.5, zorder=2)
        ax.annotate(name, (lon, lat), xytext=(8, -2), textcoords="offset points", fontsize=7.5, color=MUTED,
                    va="center")

ax.set_xlim(68.8, 77.6); ax.set_ylim(14.2, 24.2); ax.set_aspect(1.03)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_xticks([]); ax.set_yticks([])
ax.set_title("Hindus stated to follow a Śaṅkarācārya / Smārta teacher\nBombay Gazetteer district volumes, 1880–86",
             fontsize=11, color=INK, loc="left")
cb = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=ramp), ax=ax, orientation="horizontal", fraction=0.035,
                  pad=0.02, aspect=40)
cb.outline.set_visible(False)
cb.set_label("% of district Hindu population (castes asserted Smārta + castes split Smārta/Bhāgavata)",
             fontsize=7.5, color=MUTED)
cb.ax.tick_params(labelsize=7, colors=MUTED)
fig.text(0.02, 0.012, "Dots at district headquarters (schematic, no boundaries). Grey: no caste-level Smārta "
         "statements coded (Gujarat district volumes defer castes to vol. IX; Khandesh).\n"
         "Excludes castes the text calls nominal (Kuṇbīs of Poona and Ahmadnagar who 'cannot tell whether they are "
         "Smarts or Bhāgvats'). Census: 1881 (Ratnagiri, Thana 1872).", fontsize=6.3, color=MUTED)
plt.savefig("results/smarta_map.png", bbox_inches="tight")
print("results/smarta_map.png")
