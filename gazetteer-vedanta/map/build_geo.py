#!/usr/bin/env python3
"""Simplify Natural Earth 1:50m countries and Indian states to the study's frame for the interactive map.
Usage: python3 -I map/build_geo.py  -> map/geo_small.json"""
import json
BOX = (66.0, 4.0, 98.0, 38.0)
def simp(ring, tol=0.04):
    out = []
    for x, y in ring:
        x, y = round(x, 2), round(y, 2)
        if not out or abs(x - out[-1][0]) + abs(y - out[-1][1]) >= tol: out.append([x, y])
    return out if len(out) >= 4 else None
def inbox(ring):
    return any(BOX[0] <= x <= BOX[2] and BOX[1] <= y <= BOX[3] for x, y in ring)
def polys(g):
    return g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
out = {"countries": [], "states": []}
for f in json.load(open("map/ne_50m_admin0.geojson"))["features"]:
    a3 = f["properties"].get("ADM0_A3")
    rings = [simp(p[0]) for p in polys(f["geometry"]) if inbox(p[0])]
    rings = [r for r in rings if r]
    if rings: out["countries"].append({"id": a3, "name": f["properties"].get("NAME"), "rings": rings})
for f in json.load(open("map/ne_50m_admin1.geojson"))["features"]:
    if f["properties"].get("adm0_a3") != "IND": continue
    rings = [r for r in (simp(p[0], 0.03) for p in polys(f["geometry"])) if r]
    out["states"].append({"name": f["properties"].get("name"), "rings": rings})
json.dump(out, open("map/geo_small.json", "w"), separators=(",", ":"))
import os; print(os.path.getsize("map/geo_small.json"), len(out["countries"]), len(out["states"]), sorted(s["name"] for s in out["states"])[:40])
