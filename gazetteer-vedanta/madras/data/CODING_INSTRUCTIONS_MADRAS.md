# Coding instructions: Madras manuals and gazetteers (supplement)

Follow `../../data/CODING_INSTRUCTIONS.md` (the Bombay rules) in full, with these changes.

## Sources and layout

- Two layers per district: the **District Manual** (`M-XXX`, 1869–87) and the **District Gazetteer**
  (`G-XXX`, 1904–18). Code both, so the district can be compared over time. `vol` = the code in
  `data/selection.tsv`.
- Madras volumes have no marginal caste notes. Work directly from the OCR: find the chapter on the people
  (Manuals: "Population", "Castes", "Religion"; Gazetteers: chapter III "The People") and the
  "Religious life"/"Religion" sections, and grep (OCR-tolerant):
  `grep -n -i -E 'sm[aāâá]rt|s[ah]?ankar[aā]?ch|sringeri|sringiri|kumbak[oō]n|kanchi|conjeeveram|kamakoti|pushpagiri|virupaksh|hampi|sivaganga|ahobil|vanamamalai|tengalai|tenkalai|vadagalai|vadakalai|madhva|ramanuj|lingay|tiruvadu|tiruvavadu|dharmapur|mutt|matha?\b|guru|spiritual|sect'`
- Populations: Manuals use 1871 (sometimes 1881) census; Gazetteers 1901 (sometimes 1911). Take the
  figure the volume gives for the caste in that district; record `pop_year`.

## Extra codes and seats

- `SAIVA_MATH`: a caste said to be under a non-Brahmin Śaiva maṭha (Tiruvāvaḍuturai, Dharmapuram,
  Tiruppanandāḷ, Kuṉṟakkuḍi, etc.) or a pandāram/Śaiva guru of that kind. Name the maṭha in `pitha`.
- `RAMANUJA`: add `Tenkalai` / `Vadakalai` in `note` when stated.
- `pitha` normalisations: `Sringeri`, `Sivaganga` (Sringeri branch), `Kanchi/Kumbakonam` (the
  Kāmakoṭi seat; say which town the text names), `Pushpagiri`, `Virupaksha (Hampi)`, `Ahobilam`,
  `Vanamamalai`, `Uttaradi`, `Raghavendra`, `Udipi`, etc.
- Keep the Bombay rule: code only what this volume says about this district; no outside knowledge.
  If a volume describes a caste in general terms ("the Smarta Brahmans of the Tamil country…"), code it
  with `scope` = `general` unless it is clearly about the district's members.

## Output

`results/coded/<vol>.coded.tsv`, same 14 columns as Bombay (district = the Madras district).
