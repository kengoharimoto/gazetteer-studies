# The rivals of Śaṅkara's following

Part of `../`. This layer asks who else held the ground where Śaṅkara's following was strong or weak, and how
their institutions compared. It reads the volumes already downloaded for the study, and adds the revised Mathura
gazetteer (1968) and four Calcutta texts.

## Sources and method

- **Coding.** Four coders followed `CODING_INSTRUCTIONS.md`. They searched by order name and OCR variant, read
  each entry in full, and recorded a verbatim quote, a page and a confidence for every row.

  | file | scope | rows | report |
  |---|---|---|---|
  | `results/coded/BAM.tsv` | Benares, Ayodhyā (Fyzabad), Mathura at three dates (Atkinson 1880s, Nevill 1900s, revised 1960s) | 131 | `results/benares_ayodhya_mathura.md` |
  | `results/coded/N.tsv` | Bairāgīs, Nāth Jogīs, Udāsīs/Nirmalas, Kabīrpanthīs, Satnāmīs, Aghorīs in the north, Punjab and CP | 95 | `results/north_centre.md` |
  | `results/coded/S.tsv` | Mādhva, Śrīvaiṣṇava, Liṅgāyat, Tamil Śaiva, Vallabha, Svāminārāyaṇa, Gauḍīya houses in the south, west and east | 225 | `results/south_west_east.md` |
  | `results/coded/R.tsv` | reform movements in all volumes (Brahmo, Prārthanā, Ārya Samāj, Theosophy, Ramakrishna, Bharat Dharma Mahāmaṇḍal); the Calcutta area | 164 | `results/reform_calcutta.md` |

- **Quote check.** All 615 rows were checked (`../mathas/scripts/check_quotes.py`, whitespace-normalised):
  - 608 quote the OCR, and all of them are found. Seven of these match only once OCR line-break hyphens or curly
    quotation marks are allowed for.
  - The other 7 quote transcribed census-table rows.
- **Downloads.** The revised Mathura gazetteer (`dli.csl.3090`) and the Calcutta texts (in `data/ia_ocr/`, not in
  git).

## Results

1. **Wherever both are described, the rivals are as rich as the Śaṅkara houses or richer.**
   - Tanjore: Tiruvāvaḍuturai, about 29,000 acres and Rs 2 lakhs a year, against Rs 14,000 for the Kumbakoṇam
     Śaṅkara maṭh.
   - Purī: 29 maṭhs drew Rs 1,45,400 a year from land in 1848. The Govardhan maṭh is given no estate, and the
     Śaṅkara-line houses are about 7 of some 130 in 1977.
   - Chhattisgarh: the Bairāgī Feudatory State of Nandgaon (560 villages, granted 1723), plus Lormi (104 villages)
     and Seorinarayan (18), against the largest Gosāin estate, Dharampuri (40).
   - Oudh: a Nānakshāhī (Udāsī) taluqdar, Maswasi, with 17,215 acres in Gonda.
   - Punjab: the institutions with land and royal sanads are Nāth and Udāsī (Tilla, Koh Kirana, Bohar, Dera Baba
     Nanak). In Rohtak the Gosāins come fourth among 299 asthals.
   - Upper Ganges: rough parity. At Kankhal, Gokul Dās Udāsī holds 3,199 acres against Bhola Gir Goshain's 4,024.
   - The exception is the Bombay Karnatak. There Saṅkeśvar (30 inām villages, Rs 30,000) and Kudli out-endow the
     Liṅgāyat maṭhs, whose network is denser rather than richer.
2. **The rival followings are larger, and they are not confined to Brahmans.**
   - Gujarat: Vallabhas 647,256 and Svāminārāyaṇs 287,687 (1901). The Dvārkā pīṭha has no stated following.
   - Mysore: in Kadur, Śṛṅgeri's own district, Liṅgāyats outnumber all Brahmans more than two to one.
   - CP: Kabīrpanthī and Satnāmī gaddīs rest on huge low-caste lay followings (the Kawardha line claimed 500,000).
   - Bengal: the Gosvāmī houses govern their followers through "circles" and fees.
3. **The three cities.**
   - **Benares:** the one place where Śaṅkara's following is institutionally present at every date (Daṇḍīs, Gosāin
     estates of 10,304 acres, three Nāgā akhāṛās, the Daṇḍī satra). The rivals are many but small. The Gosāin
     estates vanish from the 1965 volume.
   - **Ayodhyā:** a Bairāgī town in every layer; Hanumāngaṛhī had 300–400 resident disciples in 1877 and about 200 in
     1960, but grew richer. The district still returns 5,371 Daśanāmīs (1891). The one explicit Daśanāmī–Bairāgī
     conflict in the three cities is the Gosāins' expulsion from Hanumāngaṛhī, told only in 1960.
   - **Mathura:** no Śaṅkara following at any date. There "Gosāin" means a Vaiṣṇava temple lineage.
4. **Direct conflict with the Śaṅkara side is rare in the texts.**
   - Hardwar, 1760: the Bairāgīs were defeated, with 1,800 dead, in a dispute over bathing precedence. Russell
     says the Bairāgī akhāṛās were founded to fight the Gosāins.
   - The Gosāins were expelled from Hanumāngaṛhī.
   - The Kudalgi palanquin suit against the Liṅgāyat Mūrusāvira svāmī was lost up to the Privy Council (c. 1830).
   - Śṛṅgeri won 14,812 Konkan Kuṇbīs from the Chitradurga guru (1881).
   - Rose records a Jogī–Sannyāsī feud.
   - Most recorded disputes are inside the rival traditions: Teṅgalai against Vaḍagalai, Uttarādi against
     Rāghavendra, and the Bairāgī akhāṛās among themselves.
5. **The rivals share the Gosāins' social form.** Chela succession turns into married family estates, mahants
   become moneylenders and landlords, and settlement and the courts fix private title. Two Bairāgī lines reached
   princely rank (Nandgaon, Chhuikhadan).
6. **The reform movements.**
   - **Colonial texts:** the movements are urban and countable: Brahmos in the dozens to the low thousands, Ārya
     Samājīs 12,298 in Bulandshahr at their peak. The Daśanāmīs are rural, endowed and almost uncounted. No colonial
     text sets a reform movement against a Śaṅkara seat. The orthodox side is the lay Dharma Sabhās and the pandits.
   - **Revised texts:** the Ramakrishna movement becomes the growth story (Howrah 1972: 115 centres). The Brahmos are
     relics (Howrah 63 in 1961).
   - **Links to Śaṅkara:** only three texts link the Ramakrishna movement to Śaṅkara or Advaita (Howrah 1909,
     Hooghly 1972, Puri 1977). Puri's list files the Ramakrishna Matha as "Dashnami Sannyasi" (medium confidence).
7. **Calcutta.**
   - In 1901 the city had 1,799 Brahmos and 14,079 Baishnabs, and no Sannyāsī or Gosāin heading.
   - Kālīghāṭ belongs to householder Haldār priests.
   - The Daśanāmīs appear only as endowed maṭhs centred on Tārakeśvar, which a court found "governed by the
     Sankaracharya school of thought" (Hooghly 1972).

## Corrections made along the way

- **Mathura's 17,131 "unspecified" Goshains (1891)** are probably the district's whole ascetic population, not
  Vaiṣṇava gosvāmīs alone. The same row returns no Bairāgīs or Jogīs; in 1881 there were 9,812 Bairāgīs and 3,627
  Jogīs. Corrected in the census, north and synthesis files and the places finder.
- **`north/results/coded/UP23.counts.tsv`:** a page number ("241") had been read as a Bairāgī akhāṛā's disciple
  count. The count is blanked.
- **Catalogue errors noted in the selection files:**
  - `dli.ministry.07867` (backup for Nimar) is the Balaghat gazetteer.
  - `glossaryoftribes03rose` is Rose vol. II, not III.
  - Aligarh (UP06) and Basti (UP28) are the 1909 and 1907 Nevill volumes, not "1879" and "1801".

## Limits

- **Not covered.** Srirangam, Ahobila, Śrīperumbudūr and Tirukkōyilūr are undescribed, because their districts
  (Trichinopoly, Kurnool, Ramnad) are not in the downloaded set. The Chhattisgarh Feudatory States gazetteer was not
  downloaded. Rose vol. I was searched but not coded.
- **Calcutta.** The census tables of 1901 and 1911 are illegible, so the Ārya and Ramakrishna figures for the city
  are missing. Cotton's *Calcutta Old and New* (1907) stands in for a descriptive Calcutta gazetteer.
- **Inferred affiliations.** Some sect affiliations are inferred and flagged in notes, for example the Gopāl Mandir
  and the Dwārkādhīś temple as Vallabha.
- **Page numbers.** Some are inferred from running heads.
