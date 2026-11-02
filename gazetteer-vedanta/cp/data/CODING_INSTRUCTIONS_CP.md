# Coding instructions: Daśanāmīs in the Central Provinces and Berar

Follow `../../north/data/CODING_INSTRUCTIONS_NORTH.md` in full: same output files
(`results/coded/<VOL>.counts.tsv`, `<VOL>.notes.tsv`), same columns, `group_std`, `kind` and `order` codes,
same rules. Changes and additions for the Central Provinces:

## Sources

- `GRANT`: C. Grant, *The Gazetteer of the Central Provinces of India*, 2nd ed. (1870). Province-wide, with
  district articles. Census 1866 or 1872. Fill `district` from the article.
- `CP01…CP21`: *Central Provinces (and Berar) District Gazetteers*, Vol. A (Russell and others, 1905–12).
  Census 1901.
- `RUS1/RUS2/RUS3/RUS4`: R. V. Russell and Hira Lal, *The Tribes and Castes of the Central Provinces of India*
  (1916). Province-wide. Vol. 3 (Gutenberg text `data/ia_ocr/russell_vol3_gutenberg.txt`) holds the entry
  "Gosain, Gusain, Sanniasi, Dasnami". Vols. 2–3 also have Jogi/Nath and Bairagi. Code their statements as
  notes, and their figures as counts with scope `province` (or `district` when one is named).
- Selections: `data/selection_cpg.tsv`, `data/selection_other.tsv`. Packets: `results/packets/<VOL>.txt`.

## Terms in this region

- Daśanāmī: Gosain / Gusain / Gosavi (Marathi, Berar), Sannyasi, Dasnami, Dandi, Paramhans, and the ten names.
  In Berar and Nagpur "Gosavi" is the Marathi form (cf. the Bombay study).
- Comparison orders: Bairagi (Ramanandi, often powerful mahants in Chhattisgarh, e.g. Raipur and Bilaspur),
  Jogi / Nath / Kanphata (`JOGI`; the Jogi musician caste is `OTHER`), Mahanubhav (Berar), Kabirpanthi and
  Satnami (Chhattisgarh; `OTHER` with a note).
- Watch for Gosain landholders, moneylenders and military Gosains under the Marathas (Nagpur Bhonslas,
  Saugor). Also the Narmada pilgrimage sites (Omkareshwar in Nimar, Jubbulpore's Bheraghat, Hoshangabad) with
  their maṭhs and akhāṛās.
