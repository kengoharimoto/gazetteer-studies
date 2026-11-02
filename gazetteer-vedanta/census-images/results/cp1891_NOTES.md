# Central Provinces 1891: ascetic castes (Table XVI)

Source: *Census of India 1891*, vol. XII, *The Central Provinces and Feudatories*, Part II, Imperial Tables
(IA `india.history.resource.52255`). Table XVI, "The Population by Caste, Tribe or Race".

## Pages used

| image | printed page | content |
|---|---|---|
| n10 (also n8, n9) | v (iii–iv) | Caste Index. Bhárthi-, Giri- and Puri-Gosain are indexed as sub-divisions on p. 150, group 6. There is no separate sub-caste table: sub-divisions are printed inside Table XVI. |
| n163 | 148 | British Districts, Group VI "Devotees" rows 1–13 (Aghori … Bairági with 7 sub-divisions … Dandi, Dandigán, Fakir …): totals, sex, and the first five districts (Saugor–Seoni) |
| n164 | 149 | the same rows, other 13 districts (Narsinghpur–Sambalpur) |
| n165 | 150 | Group VI rows 14–29 (Gosáin with Bhárthi/Giri/Puri, Jogi, Náth, Sanyási …), Total Group VI, first five districts |
| n166 | 151 | the same rows, other 13 districts, and Remarks |
| n339 (full resolution `n339.jpg`; page printed sideways) | xxxviii | Feudatory States, Group VI, 15 states |

District values are for persons only. Sex is given only in the provincial total columns. The `division`
column is not printed in the table: it is the 1891 administrative division, added for grouping.

## Result: `cp1891_castes.tsv`

Provincial totals for the British Districts (persons / males / females):

- **Gosáin 24,796 (12,927 / 11,869)**:
  - Bhárthi 1,412 (740 / 672)
  - Giri 9,333 (4,839 / 4,494)
  - Puri 6,050 (3,090 / 2,960)
  - not sub-divided: 8,001 (derived)
- Sanyási 2,449 (1,248 / 1,201). Dandi 1. Dandigán 536 (218 / 318).
- **Bairági 29,298 (15,536 / 13,762)**:
  - Digambari 1,186
  - Kabirpanthi 399
  - Rámánandi 7,731
  - Rámánuj 303
  - Ramáwat 1,507
  - Sanjogi 1,531
  - Vaishnava 2,152
  - not sub-divided: 14,489 (derived)
- Jogi 6,094 (2,925 / 3,169). Náth 5,008 (2,574 / 2,434). Aghori 36. Bramhachári 69.
- Fakir 4,559 (2,253 / 2,306). The religion column gives it as Musalman ("M."). There is no Hindu Fakir row
  for the British Districts.

Feudatory States: Gosáin 1,038 (537 / 501), with no sub-divisions. Sanyási 758. Bairági 6,712. Jogi 900.
Náth 706. Fakir: Hindu 23 and Musalman 242. In the States table Rámánandi (8), Ramáwat (75), Sanjogi (3) and
Vaishnava (2,084) are separate castes, not sub-divisions of Bairági. In the TSV they sit in the `bairagi_*`
columns only for comparison.

Remark column: "C. 6." against Gosáin (religion "H. c."). This presumably means 6 Christian Gosains, included
in the total.

## Reconciliation

- **British Districts.** In every transcribed column the 18 district values sum to the printed provincial
  total. In each total row, males + females = persons.
- **Group VI check.** All 29 Group VI rows were transcribed. In all 18 districts their sum equals the printed
  "Total Group VI" (85,438 in all). Province-wide, the caste totals (persons, males, females) also sum to the
  printed Group VI totals.
- **Feudatory States.** Every row and all 15 state "Total Group VI" figures reconcile (12,839).

## Doubtful readings (resolved by totals, flagged in `note`)

1. **Saugor Bairági.** The print reads 1,290, with a damaged final digit. The caste total and the Saugor
   Group VI total both require **1,299**.
2. **Bilaspur Gosáin-Giri.** The print reads "8·6", with a broken middle digit. The column total requires
   **866**.
3. **Bhandara Dandigán.** The print reads 106. The caste total (536) and the Bhandara Group VI total both
   require **196**. Balaghat Dandigán is a faint "9", which is consistent with its Group VI total.

No unreconciled column remains.
