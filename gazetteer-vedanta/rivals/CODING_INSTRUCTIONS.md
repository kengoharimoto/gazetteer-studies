# Coding instructions: the rivals of Śaṅkara's following

Goal: the institutions and followings of the traditions that competed with Śaṅkara's, as the volumes already
downloaded describe them. Use the same discipline as the rest of the study: verbatim quotes, pages, confidence.

The traditions:
- Vaiṣṇava orders and houses: Rāmānandī Bairāgīs, Rāmānujīya/Śrīvaiṣṇava, Vallabha (Puṣṭimārga), Gauḍīya
  (Chaitanya), Mādhva, Svāminārāyaṇa, Nimbārka, Kabīrpanthī, Dādūpanthī;
- Nāth/Kānphaṭā Jogīs;
- Udāsīs and Nirmalas;
- Liṅgāyats (Vīraśaiva maṭhs);
- the Tamil non-Brahmin Śaiva maṭhs;
- Aghorīs;
- the reform movements: Brahmo, Prārthanā and Ārya Samāj, Theosophy, the Ramakrishna movement.

Working directory: `/mnt2/kengo/research/gazetteer-vedanta/`. Run Python only with `python3 -I`. Write only your
own output files (given in your assignment).

## Where the texts are
- OCR files live in `<region>/data/ia_ocr/<identifier>.txt`, where region is one of `data` (Bombay), `madras`,
  `north`, `bengal`, `punjab`, `cp`, `revised` or `sringeri`.
- Volume labels are in each region's `data/selection*.tsv`.
- Find passages with grep, using the order names and their OCR variants (Bairagi, Byragi, Ramanandi, Ramanuji,
  Vallabh, Gokulastha, Chaitanya, Baishnab, Madhva, Madhwa, Swaminarayan, Kabirpanthi, Jogi, Kanphata, Nath,
  Gorakhnath, Udasi, Nirmala, Lingayat, Jangam, math, mutt, akhara, mahant, Brahmo, Arya Samaj, Theosoph,
  Ramkrishna, Vivekanand …).
- Then open the OCR around each relevant line and read the whole entry.

## Output
One TSV, with this header:

```
id	tradition	volume	year	district	place	institution	kind	what_is_said	figures	quote	page	confidence	notes
```

- **tradition:** one of bairagi_ramanandi, vaishnava_other (name it in notes), vallabha, gaudiya, madhva,
  srivaishnava, swaminarayan, kabirpanthi, nath_jogi, udasi, lingayat, tamil_saiva, aghori, brahmo, arya_samaj,
  theosophy, ramakrishna, other.
- **kind:** one of
  - `institution` (maṭh, akhāṛā, gaddī, temple run by the order);
  - `estate` (villages, ināms, revenue);
  - `following` (who follows them, how many);
  - `conflict` (with Gosāins/Daśanāmīs or Śaṅkara seats, or among themselves);
  - `event`;
  - `count` (a headcount);
  - `comparison` (a text comparing them with Śaiva/Śaṅkara followers).
- **figures:** any numbers (persons, villages, acres, rupees, dates).
- **quote:** VERBATIM from the OCR (≥ 12 words), with OCR errors kept as they are.
- **page:** the printed page if findable, else "s.v. <entry>".
- Give one row per institution or statement per volume. Concentrate on substance: institutions, estates,
  followings with numbers, and conflicts with the Daśanāmīs or the Śaṅkara seats. Generic one-line caste-religion
  statements do not need rows; give per-volume counts of them in a final comment line `# generic: …`.
- When done, write a short report (Markdown) to the path in your assignment, with these headings: Sources read;
  What the texts show (with figures); Comparison with Śaṅkara's following in the same places; Limits. Then reply
  with a ≤15-line summary.
