# Punjab 1891: ascetic castes and Hindu sects

The source is the Census of India 1891, vol. XX, *The Punjab and its Feudatories*, Part II, Imperial Tables,
British Territory (IA `india.history.resource.117714`). The page images are in `pages/pj1891_n*.jpg` (w1600).
The caste pages are printed sideways and were rotated −90° to read.

## Files

- `punjab1891_castes.tsv`: Table XVI (Castes by religion and district). There is one row per district (32
  districts, table columns 10–41), followed by the printed totals for British Territory, Native States and the
  Province. Each caste has T / M / F columns. An empty cell is "..." in print.
- `punjab1891_sects.tsv`: Table F, the rows that bear on Śaṅkara's following and its comparators.

## Where things are

In Table XVI, Gosain, Sanniasi, Bairagi and Udasi are not separate castes. They are sub-heads of the caste
**Faqír** (class B, group 6). The sub-heads are Bairágí, Benawá, Chishtí, Darvesh, Gosáín, Husainí, Jalálí,
Madárí, Nirmalá, Qádirí, Sádh, Sanniásí, Súthra Sháhí, Udásí, Faqír (unspecified), and Total Faqírs.

| content | image (n) | printed page |
|---|---|---|
| Faqír: Bairágí, Gosáín | n289–n292 | pp. 280–283 |
| Faqír: Sanniásí, Udásí, Total Faqírs | n293–n296 | pp. 284–287 |
| Jogí and Ráwal, a separate caste (class E, group 45; printed "42" on p. 319) | n325–n328 | pp. 316–319 |

On each page set, the first page has the Province, Native States, British Territory, Hissár, Rohtak and Gurgáon.
The next three pages have the other districts: Delhi to Firozpur, Multán to Sháhpur, and Jhelum to Biloch
Trans-frontier.

Other points about the caste table:

- **No Giri, Puri or other Daśanāmī sub-divisions appear in it.** Gosáín and Sanniásí are themselves the lowest
  level.
- **The district figures are not split by religion.** The province and British Territory columns are.
- **There is no separate "Rawal" caste.** "Ráwat" (p. 384) is an agricultural caste and has nothing to do with
  Jogis.

Table F (Religious Sects) is on n835–n848:

| part | image (n) | printed page | content |
|---|---|---|---|
| Part A, Hindu sects | n835–n838 | pp. 826–829 | an alphabetical list of about 800 sects, with British Territory totals only (no sex, no districts) |
| Part B | n838–n841 | from p. 829 | sects of religions classed as Hindu (Brahmo, Arya, "religions" such as Jogi, Bairagi or Udasi), by sex |
| Part G | n845–n848 | — | district figures for selected sects only |

The sects in Part G are Aria, Brahmo, Jain/Sikh/Dadupanthi, Guru Gobind Singhie, Kabir Panthi, Kalu Baba, Kuka,
Nanak Panthi, Narinjani, Nirankari, Namdeo Panthi, Ram Dasi, Ram Raia, Sultani, Digambari, Svetambari and the
Muslim sects. **None of the target sects has district figures.**

## Reconciliation

All three checks below were done.

1. **Faqír sub-heads.** For Bairágí, Gosáín, Sanniásí, Udásí and Total Faqírs:
   - each district row satisfies T = M + F;
   - each of the 15 columns sums exactly to the printed British Territory total.
2. **Province totals.** For every caste, Province = British Territory + Native States, in T, M and F.
3. **Religion split for British Territory.** For every caste, the religion figures sum to the total:
   - Gosáín: Hindu 9,289, Musalmán 611, Sikh 3.
   - Sanniásí: Hindu 4,965, Musalmán 128, Sikh 70.
   - Bairágí: Hindu 34,000, Musalmán 48, Sikh 54.
   - Udásí: Hindu 7,076, Musalmán 188, Sikh 2,192, Christian 3.
   - Total Faqírs: Hindu 71,049, Musalmán 170,869, Sikh 7,351, Jain 37, Christian 3. Hindu Faqírs are 71,049 in
     British Territory and 103,015 in the Province.
   - Jogí & Ráwal: Hindu 38,530, Musalmán 36,718, Sikh 220, Jain 1.

**Jogí & Ráwal does not reconcile.** The printed British totals are 75,469 / 40,433 / 35,036, and the district
rows as printed sum to 75,439 / 40,423 / 35,066. Two rows are internally inconsistent in print. Both were checked
on zoomed crops, and the errata slip (n8) has no correction for pp. 316–319.

| district | printed T | printed M | printed F | M + F |
|---|---|---|---|---|
| Montgomery | 422 | 322 | 120 | 442 |
| Lahore | 2,147 | 1,292 | 885 | 2,177 |

Two two-digit emendations each make everything reconcile:

- (a) Lahore T = 2,177, and Montgomery M = 332, F = 90.
- (b) Lahore F = 855, and Montgomery T = 452, M = 332.

The table cannot decide between them, so the printed figures are kept and flagged in `note`. The district
figures for Jogí & Ráwal are therefore exact except for these two rows: Montgomery is uncertain by about 30 and
Lahore by about 30.

Other notes on the caste figures:

- Jhelum's Jogí female figure (875) is labelled "T." in print. This is a misprint for "F."; the arithmetic
  confirms it.
- **Table F Part A was not reconciled.** Its only check is the grand total, "Total Hindus returned as such"
  7,095,142, and that would require transcribing every entry. The rows taken are single printed numbers read on
  zoomed crops.

## Findings

- **Gosáín (9,903 in British Territory) are a south-eastern and hill group.** By district:
  - Hissár 2,318
  - Kángra 1,912
  - Karnál 1,843
  - Ambála 1,081
  - Delhi 992
  - Rohtak 568

  The Delhi division and Kángra (with Simla) hold 91% of them. They are almost absent west of the Sutlej. Some 611 are
  Musalmán.
- **Sanniásí (5,163) are a central-Punjab group.** By district:
  - Hoshiárpur 825
  - Jalandhar 570
  - Amritsar 435
  - Firozpur 428
  - Gurdáspur 395
  - Ludhiána 312
  - Rawalpindi 267
- **The two distributions barely overlap.** Taken together, Gosáín plus Sanniásí are 15,066. The leading
  districts are Hissár 2,383, Kángra 2,096, Karnál 1,931, Ambála 1,165, Delhi 996 and Hoshiárpur 980.
- **Both are small beside the comparators in British Territory:**
  - Bairágí 34,102, led by Rohtak 6,317, Karnál 4,781, Delhi 4,491 and Gurgáon 4,155;
  - Udásí 9,459, of whom 2,192 are Sikh; it is a Jalandhar-Doab group, led by Jalandhar 2,056 and Ludhiána 1,865;
  - Jogí & Ráwal 75,469, almost half of them Musalmán, led by Ambála 11,033 and Karnál 9,052.
- **In the sect table, Śaṅkara's tradition is almost invisible:**
  - Smártak: 123;
  - Advaita labels: Vedántí 232, Advaiat 8, Shankar Achárj 15, Shankará Nand 8, Paramahans 52;
  - individual Daśanāmī names: Purí 12, Gangá Bhárthí 1, Aságirí 1.

  Ascetic labels are larger: Saniási 10,356 and Gusáín 4,906.
- **The sect table's ascetic figures do not match the caste table's.** "Saniási" as a sect (10,356) is twice the
  caste figure (5,163). "Gusáín" as a sect (4,906) is half the caste figure (9,903). The caste and sect
  classifications cut across each other.
- **Śaiva returns are "Shiv Worshipper" 125,328 and "Maheshí" 6,202.** There are also small Shiv- and Mahádev-
  labels. The only literal "Shaiv" is one Vaidak woman in Part B. All of these are dwarfed by "Vaishnav"
  1,709,033, "Devi Worshippers" 500,666 and "Sultání" 415,768. Of the 7,095,142 Hindus, 2,538,628 returned no
  sect.
