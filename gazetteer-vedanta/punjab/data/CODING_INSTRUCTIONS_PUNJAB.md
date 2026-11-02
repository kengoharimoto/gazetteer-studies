# Coding instructions: Daśanāmīs in the Punjab

Follow `../../north/data/CODING_INSTRUCTIONS_NORTH.md` in full: same output files
(`results/coded/<VOL>.counts.tsv`, `<VOL>.notes.tsv`), same columns, `group_std`, `kind` and `order` codes,
same rules. Changes and additions for the Punjab:

## Sources

- `PA01…`: *Gazetteer of the … District 1883–84* (first Punjab series). Census 1881. These usually print a caste
  table with "Gosain", "Jogi", "Bairagi", "Faqir" and others, and a religion section with sects.
- `PB01…`: revised *Punjab District Gazetteers*, Part A (1897–1918). Census 1901 (sometimes 1891 or 1911).
- `ROSE1–3`: H. A. Rose, *A Glossary of the Tribes and Castes of the Punjab and NWFP* (1911–19). Province-wide;
  district = "Punjab (all)". Vol. I is the religion volume. Vols II–III are the caste entries: Gosain,
  Sanyasi, Jogi, Bairagi, Udasi, Suthra and others. Code their statements as notes (CASTE / DOCTRINE / MATH /
  LAND / TRADE / MILITARY). Code their figures as counts with scope `province`, or `district` when a district
  is named.
- Selections: `data/selection_p1883.tsv`, `data/selection_p1904.tsv`, `data/selection_rose.tsv`.
  Packets: `results/packets/<VOL>.txt`.

## Terms in this region

- **Daśanāmī:** Gosain / Gusain / Gosaiñ, Sanyasi / Sannyasi, Dandi, Paramhans, and the ten names (Giri, Puri,
  Bharti, Ban, Parbat, Sagar, Tirath, Asram, Saraswati, Aranya). In the hills (Kangra) Gosains were
  well-known traders and bankers.
- **Comparison orders, often stronger than the Daśanāmīs in the Punjab:**
  - Jogis / Naths / Kanphatas (`JOGI`): Tilla Jogian (Jhelum), Jakhbar (Gurdaspur), Bohar (Rohtak). The
    "Jogi" also exists as a menial or musician caste; code that as `OTHER`.
  - Udasis (`UDASI`): Nanakshahi, Ram Rai, Suthra Shahi; Nirmalas as `OTHER` or `UDASI` with a note.
  - Bairagis (`BAIRAGI`).
- **"Gosain" is not always Daśanāmī.** Vaiṣṇava "Gosains" (Vallabha or Chaitanya gurus) and Sikh "Gosains" are
  `OTHER` with a note.
- Watch for: the Kurukshetra and Thanesar fairs (Karnal), Hardwar's neighbour districts (Ambala, Karnal), the
  Jwalamukhi temple (Kangra), and Daśanāmī akhāṛās or maṭhs in Lahore and Amritsar.
