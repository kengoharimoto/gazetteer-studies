# Madras 1891: Brahman sub-divisions and devotees by district (Table XVI-A)

Source: *Census of India 1891, vol. XIV, Madras, Tables I–XVII-C, British Territory* (IA
`india.history.resource.52257`), Table XVI-A "Castes, Tribes and Races" by linguistic division. The figures were read
from the full-resolution page images (`page/n<N>.jpg`, 4200 px; the `_w1600` images are too small for the figures),
in crops. The OCR was used only to find the pages.

## Pages

| division | columns | Brahmans (Class B, Group 5) | devotees etc. |
|---|---|---|---|
| I. Telugu | division total T/M/F; 10 districts (Ganjam … North Arcot), persons only; feudatories Banganapalle, Sandur | pp. 334–337 (n343–n346) | B-5/B-6 p. 337 (n346), B-6/B-7 p. 338 (n347), Dasari p. 351 (n360) |
| II. Tamil | division total T/M/F; 10 districts (Madras … Tinnevelly); feudatory Pudukota | pp. 361–364 (n370–n373) | p. 364 (n373), p. 365 (n374), Dasari p. 374 (n383) |
| III. Malabar | Malabar district T/M/F; feudatories Travancore, Cochin | pp. 381–382 (n390–n391) | p. 382 (n391), Dasari p. 387 (n396) |
| IV. Canara | South Canara district T/M/F only | p. 391, scanned as two halves (n400 left, n401 right) | p. 391 (n401), Dasari p. 394 (n405) |
| V. Agencies | division total T/M/F; Ganjam, Vizagapatam, Godavari Agencies | pp. 399–400 (n411–n412) | p. 400 (n412), Dasari p. 404 (n416) |

District figures in this table are **persons only**; males and females are printed only for the division (or the
single district of Malabar and Canara). The division totals exclude the feudatory states (table note).

## Files

- `madras1891_brahman_subdivisions.tsv`: **every** Brahman sub-division row printed, not only the requested
  ones, so the columns can be reconciled. Long format: one line per (division, district, sub-division, religion).
  `district = Division total` carries the division M/F/persons. Blank cells (printed "…") are omitted.
  - `requested = yes` marks the sub-divisions asked for (Smarta, Vaishnava, Srivaishnava, Madhva, Uttaradi, Tengalai,
    Vadagalai, Vadama, Brahacharanam, Ashtasahasram, Vattiman, Niyogi, Vaidiki, Sivalli, Havig, Sakalapura, and the
    sect-named Vaikhanasa, Pancharatra, Adisaiva, Aradhya, Lingadhari, Sivadvija, Bairagi) and the Brahman total.
  - `note = sect-named` marks the rows whose printed name is a sect name. No row is re-classified. Names are
    transliterated without diacritics; "Sivalli" is the table's spelling of Shivalli.
- `madras1891_devotees.tsv`: Group B-6 Devotees, all rows (Atita, Bairagi, Bavaji, Boishnobo, Fakir, Gosayi,
  Haridas, Sadu, Sanjogi, Sanyasi, Tambiran, Udasi). Also, with their own group in column 1:
  - Jangam, Pandaram, Tambala, Valluva and Gurukkal, which the table puts under B-5 Priests;
  - Satani under B-7 Temple-servants;
  - Dasari under E-45a Beggars.
- No sect table: see below.

## Reconciliation

1. **Rows.** Every transcribed row was checked two ways: males + females = total, and the district columns sum to
   the division total. All rows pass, in both files.
2. **Columns against "Total, Brahmans".**
   - **Tamil, Malabar, Canara, Agencies:** every column (T, M, F, each district, each feudatory) sums exactly to the
     printed total, with one exception. The printed Trichinopoly total "86,676" (checked in a zoomed crop) must be
     36,676: the rows sum to 36,676, and the printed row total 423,578 also requires 36,676. It is a misprint. The TSV
     keeps the printed figure with a note.
   - **Telugu:** T, M, F and seven of the ten districts reconcile, as do both feudatories. Three do not, and
     **these are flagged, not resolved**:

     | district | rows sum to | printed total | difference |
     |---|---|---|---|
     | Ganjam | 117,908 | 117,911 | rows 3 short |
     | Anantapur | 15,974 | 15,975 | rows 1 short |
     | North Arcot | 46,418 | 46,414 | rows 4 over |

     The differences net to zero, as they must, since every row and the printed total row each balance across. The
     small figures in these three columns were re-read in zoomed crops, and they are as transcribed. So either the
     printed column total is wrong, or a figure was printed in the wrong column on the page.
3. **Group B-6 Devotees** reconciles exactly in every column in all five divisions.
4. **Against Table XVI (presidency, p. 313, n322).**
   - The five division Brahman totals sum to **1,121,110 (551,951 M, 569,159 F)**, which is the printed presidency
     total.
   - Presidency rows checked against the sum of the divisions all match: Smarta 7,021; Vadama (Hindu) 139,012; Vattiman 11,006; Vaidiki
     116,192; Vaishnava 4,878; Srivaishnava 5,481; Tengalai 46,698; Vadagalai 65,352; Sivalli 28,680.
5. **Single cells to note.**
   - Telugu "Nandavaidiki" and "Tuluva" have no British-territory figures, only Sandur 7 and 15.
   - Malabar's italic rows (Dravida, Maharashtra, Malavala, Nambi, Potti, Kasi, Kannada) have figures only for
     Travancore or Cochin.
   - Non-Hindu lines are kept separately with their religion: for example Vadama Christian 9 (Nilgiris), Niyogi
     Christian 9 (Nellore) and Theist 1 (Cuddapah).

## What the table shows (for `../madras/`)

- **"Smarta" as a printed sub-division is tiny: 7,021 in the whole presidency** (Telugu 2,923, Tamil 4,027, Malabar
  41, Canara 28, Agencies 2). The Tamil Smārta Brahmans were returned under their sub-caste names. Per district,
  persons:

  | district | Vadama | Brahacharanam | Ashtasahasram | Vattiman |
  |---|---|---|---|---|
  | Tanjore | 52,020 | 16,104 | 6,267 | 7,477 |
  | Tinnevelly | 19,446 | 4,999 | 1,955 | 585 |
  | Malabar | 18,299 | 8,311 | 1,953 | 1,194 |

  Presidency totals (Hindu) are Vadama 139,012, Brahacharanam 55,190, Ashtasahasram 16,342 and Vattiman 11,006.
  Sozhiya, Kesika, Mukkani and others also occur.
- Vaiṣṇava Brahmans appear mainly as **Tengalai (46,698) and Vadagalai (65,352)**. The rows "Srivaishnava" (5,481)
  and "Vaishnava" (4,878) are small.
- In the Telugu districts the large rows are the Niyogi/Vaidiki split (Niyogi 100,942; Vaidiki 113,427) and the
  regional names (Velanadu, Murikinadu, Telaganya …). These do not state sect.
- In South Canara the large rows are Sivalli (28,660), Sarasvata (30,273), Havig (11,234) and Kota (11,017).
  Sakalapura has 463.
- So "Smarta Brahmans by district" cannot be read off one row. It needs a decision on which sub-caste names count as
  Smārta (Vadama, Brahacharanam, Ashtasahasram, Vattiman, Havig …). That decision belongs to the study, not to the
  transcription.

## Sect table

**This volume has no table of sects.** The table of contents (n8) lists Tables I–XVII-C. Table VI "Religions" gives
religions only, plus a note on "Others" (Sikh, Agnostic, Theist …). The 1891 Śaiva/Vaiṣṇava/Lingāyat figures by
district are in the report volume (Stuart), as already used in `../madras/data/census/sect_ratios_1871_1891.tsv`.
`madras1891_sects.tsv` was therefore not written.

## Doubts

- Telugu Ganjam, Anantapur and North Arcot Brahman column totals: see above.
- Tamil Trichinopoly: printed 86,676 is taken as a misprint for 36,676.
- "Gurukkal" occurs twice in the Tamil division: as a Brahman sub-division (8,338) and as a separate B-5 caste (243
  Hindu, plus a few Musalman, Christian and Jain). Malabar likewise has Gurukkal 59 under Brahmans. They are kept
  where printed.
- Jangam and Pandaram are B-5 Priests in this table, not B-6 Devotees.
- Working transcriptions (pipe-delimited, with the check scripts) were kept in `/tmp/m91/tr/`. They are not part of
  the repository.
