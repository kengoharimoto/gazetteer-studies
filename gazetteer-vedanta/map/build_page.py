#!/usr/bin/env python3
"""Inject places.tsv and geo_small.json into the page template.
Usage: python3 -I map/places_data.py && python3 -I map/build_geo.py && python3 -I map/build_page.py"""
import csv, json
rows = list(csv.DictReader(open("map/places.tsv", encoding="utf-8"), delimiter="\t"))
for r in rows: r["lat"], r["lon"] = float(r["lat"]), float(r["lon"])
t = open("map/places_map.template.html", encoding="utf-8").read()
t = t.replace("/*PLACES*/[]", json.dumps(rows, ensure_ascii=False, separators=(",", ":")))
t = t.replace("/*GEO*/{}", open("map/geo_small.json").read())
open("map/places_map.html", "w", encoding="utf-8").write(t)
print(len(t))
