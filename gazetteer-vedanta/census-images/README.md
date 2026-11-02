# Census caste tables read from page images

The OCR of the census caste tables is unusable: columns are scrambled, and the Bombay 1881 tables are printed
sideways and upside down. So the tables were read directly from Internet Archive page images.

Method:

1. Find the pages in the item's per-page OCR (`*_djvu.xml`, one object per page) by searching for the caste
   name.
2. Download the page image: `https://archive.org/download/<id>/page/n<N>_w1600.jpg`. The district names are on
   the facing page.
3. Read the image and transcribe it to TSV.
4. Check every column against the printed totals.

Page images and the downloaded OCR XML are in `pages/` (kept out of git).

## Tables

| file | source | content | check |
|---|---|---|---|
| `results/up1891_goshain.tsv` | Census of India 1891, NWP & Oudh, Part III Imperial Caste Tables (`india.history.resource.117715`), Table XVI Part A, p. 51 (image n92; districts on p. 50, n91) | caste **Fakir**, sub-division **Goshain**, by 49 districts, split Brindabani / **Dasnami** / Gauriya / Gokulastha / Niranjani / Radhavallabhi / Unspecified, by sex | all 18 columns sum to the printed provincial totals; all district rows sum to their totals |
| `results/up1891_ascetics.tsv` | same, pp. 49–52 (n90–n93) | per district (persons): all Hindu Fakirs, Goshain (all / Dasnami / unspecified / Vaiṣṇava-named), Bairagi, Jogi | Fakir and Jogi columns match the printed totals; Bairagi is off by 100 males (Allahabad division: Allahabad "236" or Lalitpur "197") and 1 female; flagged in `note` |
| `results/bengal1901_atith_gosain.tsv` | Census of India 1901, vol. VI-A, Bengal, Part II Imperial Tables (`in.ernet.dli.2015.55931`), Table XIII Part A, p. 194 (n200, ATITH) and p. 215 (n221, GOSAIN) | Atith and Gosain (Hindu), by 53 districts and states, by sex; remark on Gosain sub-groups | both columns match the printed totals (Shahabad Atith males read as 3,699 and Patna Gosain males as 1,149, as the division totals require) |
| `results/bombay1881_gosavi.tsv` | Imperial Census 1881, Bombay, vol. 2 Tables (`wbsl.9142`), alphabetical caste list, p. viii (n189, printed upside down) | **Gosávi** ("Devotees, &c.", class XI) by region | the five regions sum to the total 33,851 |
| `results/punjab1891_castes.tsv`, `punjab1891_sects.tsv` | Census of India 1891, Punjab, Part II Imperial Tables, British Territory (`india.history.resource.117714`), Table XVI (Faqir: Gosain, Sanniasi, Bairagi, Udasi; Jogi & Rawal), pp. 280–287, 316–319 (n289–n296, n325–n328); Table F, Religious Sects (n835–n848) | by 32 districts, by sex; Native States and religion splits at provincial level | all columns except Jogi & Rawal reconcile; Jogi has two rows inconsistent in print (Lahore, Montgomery), flagged; sect table only partly checkable. Notes: `results/punjab1891_NOTES.md` |
| `results/cp1891_castes.tsv` | Census of India 1891, CP, Part II Imperial Tables (`india.history.resource.52255`), Table XVI, Group VI Devotees, pp. 148–151 (n163–n166); Feudatory States p. xxxviii (n339) | Gosain (with Bharthi, Giri, Puri), Sanyasi, Dandi/Dandigan, Bairagi (with sub-divisions), Jogi, Nath, Fakir, by 18 districts and 15 states | all columns reconcile, including Group VI totals per district; three damaged digits resolved from the totals and flagged. Notes: `results/cp1891_NOTES.md` |
| `results/madras1891_brahman_subdivisions.tsv`, `madras1891_devotees.tsv`, `madras1891_tamil_smarta_vs_aiyangar.tsv` | Census of India 1891, Madras, Tables (`india.history.resource.52257`), Table XVI-A by linguistic division (n343–n396) | every Brahman sub-division by district; devotee castes (Sanyasi, Bairagi, Jangam, Pandaram, Satani, Dasari …); derived Tamil Smārta vs Aiyaṅgār shares | Brahman totals reconcile except 3 Telugu columns off by 1–4 (print) and the misprinted Trichinopoly total (86,676 for 36,676); devotees reconcile. Notes: `results/madras1891_NOTES.md` |

## What the tables change

1. **UP 1891: Daśanāmī Goshains were 103,320 (55,347 men + 47,973 women), not 108,320.** The report figure
   used earlier came from its OCR. With unspecified Goshains (38,477) and the few Vaiṣṇava-named ones, all
   Goshains were 142,578.
   - By district, Daśanāmī persons:
     - Gonda 11,478
     - Gorakhpur 7,010
     - Fyzabad 5,371
     - Meerut 5,083
     - Sitapur 4,414
     - Mirzapur 4,258
     - Bareilly 4,023
     - Ballia 3,804
     - Jaunpur 3,638
     - Fyzabad division 27,844 in all.
   - **Muttra's 17,131 Goshains are all "unspecified"**, the Vaiṣṇava lineages of Brindaban and Gokul. The
     Vaiṣṇava sub-headings (Brindabani, Gokulastha, Radhavallabhi) were barely used, so Vaiṣṇava Gosains must
     be separated by district, not by sub-heading.
   - **Azamgarh has no Goshains at all but 5,764 Jogis.** In 1881 the same district had 2,186 Goshains and
     3,456 Atits (Atkinson). The Atits were evidently returned as Jogis in 1891, an instance of the conflation
     the 1891 report admits.
   - Jogis (78,387) outnumber Daśanāmīs in the upper Doab: Saharanpur 13,713, Meerut 11,987, Muzaffarnagar
     9,229.
2. **Bengal 1901: Atith 50,042 (23,130 + 26,912).** They are almost all in Bihar:
   - Saran **26,753**, which confirms the gazetteer's quotation exactly;
   - Champaran 9,768; Shahabad 7,246; Muzaffarpur 3,469; Palamau 1,063; Gaya 949; Patna 677.
   - Bengal proper has a handful.
   "Gosain" (29,534) is a mixed column. Over half are in Chota Nagpur (Ranchi 9,707, Hazaribagh 4,527), and
   the census's own remark lists "Gosain Puran", "Dorihar", Jogi and Nepali Gosains in it. Only Bharati (32)
   and Giri (200, Hooghly) are explicitly Daśanāmī names.
3. **Bombay 1881: Gosávis 33,851.** By region: Deccan 19,247, Gujarat 6,036, Konkan 5,269, Bombay City 1,947,
   Karnatak 1,352. The Daśanāmī householder and mendicant caste was thus a Deccan phenomenon, alongside the
   Smārta Brahmans the Bombay study counted.
4. **Punjab 1891.**
   - Gosain 9,903 (British territory): 91% in the Delhi division, Kangra and Simla (Hissar 2,318, Kangra
     1,912, Karnal 1,843).
   - Sanniasi 5,163, in a different belt: central Punjab (Hoshiarpur 825, Jalandhar 570, Amritsar 435).
   - Both are dwarfed by Jogi & Rawal (75,469) and Bairagi (34,102).
   - The sect table has almost no Śaṅkara labels: Smartak 123, Vedanti 232, Shankar Acharj 15.
5. **Central Provinces 1891.**
   - Gosain 24,796, sub-divided Giri 9,333, Puri 6,050, Bharthi 1,412.
   - Top districts: Hoshangabad 3,291, Raipur 3,194, Nagpur 2,914.
   - Sanyasi 2,449; Dandigan 536; Bairagi 29,298.
6. **Madras 1891.**
   - The census row "Smarta" is tiny (7,021): Smārta Brahmans were returned under sub-caste names.
   - Taking Thurston's own list of Smārta sub-castes (Vadama, Brahacharanam, Vattiman, Ashtasahasram etc.),
     **Smārtas are 48% of Tamil-division Brahmans and Aiyaṅgārs (Tengalai, Vadagalai, Srivaishnava,
     Vaishnava) 23%**.
   - By district: Tanjore 64% Smārta; Trichinopoly and Tinnevelly about 55%.
   - **Chingleput is the exception, 60% Aiyaṅgār**, as the 1871 report noted. The derived table states its
     classification rule.
