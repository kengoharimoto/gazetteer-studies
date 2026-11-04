# Madras Presidency: Śaṅkara's following (Thurston 1909 + census 1871/1891)

Part of `../` (the Bombay study). Bombay used the district gazetteers' caste accounts; the Madras manuals
(1869–87) and gazetteers (1904–18) do not give caste-level sect statements, so Madras uses two other sources
(chosen by the user, option 1 + 2 of the earlier scouting note):

1. **Thurston and Rangachari, *Castes and Tribes of Southern India* (1909, 7 vols)**, the caste-by-caste
   source the Madras gazetteers themselves refer to. Text: Project Gutenberg (`data/thurston/`). Split into
   2,265 entries, 332 with sect/guru cues (`scripts/thurston_entries.py` → `results/thurston/packets/`), coded
   by entry (`data/CODING_INSTRUCTIONS_THURSTON.md` → `results/thurston_coded/vol1–7.tsv`, 246 rows, every quote
   verbatim; 25/25 spot-check found in the text).
2. **Census of the Madras Presidency, 1871 (Cornish) and 1891 (Stuart)**, `data/census/`. District
   Śaiva:Vaiṣṇava ratios at both dates: `data/census/sect_ratios_1871_1891.tsv`.

The district manuals and gazetteers (`data/selection.tsv`, OCR in `data/ia_ocr/`) were downloaded and
surveyed but not coded; see §4.

## 1. The census: the Smārtas are inside "Śaiva"

- 1871: "the present arrangement classes the Sri Vishnavas and Mādhwās as 'Vishnavaites', and the Smārtas as
  'Sivaites'" (1871 report, Brahmans). 1891: "Smārta … is used in this presidency to denote a Brāhman of the
  Śaiva sect, a follower of Sankarāchārī" (¶121).
- So the 1871 **Śaivite Brahmans are the Smārta Brahmans: 717,774, or 65.5% of all Brahmans** (Vaiṣṇava
  Brahmans 365,952, 33.4%). Brahmans were 3.7% of Hindus, so Smārta Brahmans were **≈2.4% of the Hindu
  population**. They were the majority of Brahmans in every district except Ganjam, Bellary and Chingleput.
- Below the Brahmans the labels mean little. "To a large majority of Hindus sect has very little meaning.
  Thus the Paraiyans call themselves Saivites, but they know next to nothing of the tenets of Saivism" (1891
  ¶119). The 1871 artisan castes are 85% "Śaivite" because they worship Kāmākṣiyamma, Kālī or village deities.
- The district series (Śaiva:Vaiṣṇava) runs from Vaiṣṇava in the Telugu north (Ganjam 1:10) to Śaiva in the
  Tamil south (Tanjore 7:1) and Malabar (67:1 in 1871, 100:1 in 1891).
- Changes between 1871 and 1891 noted by the 1891 report:
  - Kistna moved from 6:7 to 1:2 ("Vaishnavism has made a great advance").
  - North Arcot moved from 9:10 to 104:100 (Śaivism "has made considerable progress").
  - South Canara moved from 2:1 to 7:1 (perhaps classification).
- These figures measure Śaiva vs Vaiṣṇava, mostly non-Brahmin. They do not measure Śaṅkara's following.

### Rival Brahman sects in the 1891 census

From the 1891 Brahman sub-division table, Tamil division
(`../census-images/results/madras1891_tamil_smarta_vs_aiyangar.tsv`):

| sect | persons | share of Brahmans | where strongest |
|---|---|---|---|
| Smārta sub-castes (Thurston's list) | 201,787 | 47.6% | Tanjore 63.8%; Trichinopoly and Tinnevelly about 55% |
| Aiyaṅgār (Teṅgalai, Vaḍagalai, Śrīvaiṣṇava) | 96,127 | 22.7% | Chingleput 60.3%; Madras 31.8%; Madura 26.1% |
| Mādhva | 2,650 | 0.6% | Coimbatore 686; Madras 448; Salem 380 |

In the Tamil country the rivalry is between Brahman sects: Smārta against Śrīvaiṣṇava. The ascetic orders that
compete in the north do not appear. The non-Brahmin Śaiva maṭhs are the other rival institution (section 2).

## 2. Thurston: who is tied to a Śaṅkara seat

41 rows are coded SMARTA. They fall into two quite different groups:

**(a) The west coast and Kanarese belt: a seat is named, and it reaches non-Brahmin castes.** Śṛṅgeri is named
for:

- Kharvis (Konkani fishermen, Kundapur): "All are Saivites, and disciples of the Sringeri mutt".
- Marāṭhās and Servegāras of South Canara.
- Ares (Marathi husbandmen; South Canara, Bellary, Anantapur).
- Chaptegāras (Konkani carpenters), whose "fines … paid to the Sringeri math".
- Gāṇigas. Here Śṛṅgeri is "a Smarta (Saivite) mutt … at several places, such as Tanjore and Kumbakonam".
- Tulu Brahmans in general, and the Smārta Marakas of Mysore.

Other Smārta seats in the same belt:

- Havik Brahmans under Rāmacandrapura, and the dissenting Saklapuris under their own maṭha.
- Konkani Vānis under "the head of the Kumbakonam math". Thurston does not say which maṭha; the only Brahman
  maṭha the Tanjore gazetteer places at Kumbakoṇam is Śaṅkarācārya's (finding 3).
- In Bellary, the 1888 visit of the Śṛṅgeri Svāmi led to a dispute with the Liṅgāyats over guru processions
  (Liṅgāyat entry).

**(b) The Tamil country: Smārta is a Brahman sub-caste label with no named seat.** Thurston lists the Tamil
Smārta divisions (Vaḍama, Bṛhaccaraṇam, Vāttima, Aṣṭasahasram, Kesigal, Choliya, Sanketi, Prathamaśākhī and
others) but names **no maṭha for any of them**: no Kumbakoṇam, Kāñcī or Śivagaṅgā.

- The only maṭha remark in the Tamil Smārta section is negative: the Dīkṣitars of Chidambaram do not accept any
  Śaṅkarācārya, and Gurukkals "do not regard themselves as disciples of Sankaracharya".
- The Tamil non-Brahmin castes, where a guru is named, look to non-Brahmin Śaiva maṭhas (Tiruvāvaḍuturai,
  Mailam, Kumbakoṇam's Umayorubhāgam), to Sātāni and Dāsari gurus, or to Śrīvaiṣṇava houses:
  - Vaḍagalai: Ahobilam, now at Narasimhapuram near Kumbakoṇam, and Parakāla.
  - Teṅgalai: Vānamāmalai, Śrīperumbudūr, Tirukkōyilūr.
- In Malabar, "Smarta" is mostly the Nambūtiri caste judge (*smārtavicāram*, not coded). The few sectarian uses
  are Unnis "all Smartas", Nāyar "Smartas converted to the tenets of Sankaracharya", and the tradition of the
  three Trichur maṭhas founded by Nambūtiri disciples of Śaṅkara.

Seats named across the 246 rows: Śṛṅgeri 8; Sātāni gurus 6; Parakāla 2; Vyāsarāya 2; Tiruvāvaḍuturai/Mailam 2;
every other seat once (Ahobilam, Vānamāmalai, Śrīperumbudūr, Tirukkōyilūr, Uttarādi, Udupi, Sumatīndra,
Rāmacandrapura, Saklapuri, Kumbakoṇam, Ujjani, …). Puṣpagiri and Virūpākṣa are never named.

## 3. Findings in relation to Bombay

1. **Śṛṅgeri's jurisdiction over non-Brahmin castes is a west-coast and Kanarese phenomenon in both
   presidencies.** Bombay's Kanara (32–39% of Hindus; Konkan Kuṇbīs won over in 1881) and Madras's South Canara
   (Kharvis, Marāṭhās, Servegāras, Ares, Chaptegāras) form one belt. Away from it the following is a Brahman
   matter: the Marathi Deccan in Bombay, the Tamil country in Madras.
2. **The form of the tie is the same: jurisdiction and dues.** Fines are paid to the maṭha (Chaptegāras), caste
   disputes go to it, and an agent collects. In Bombay the Śaṅkarācārya is the final court of caste disputes.
3. **Tamil Smārtas: many Brahmans, a seat that is described but not tied to them.** Smārta Brahmans are about
   2.4% of Madras Hindus in 1871 and the majority of Brahmans in most districts, yet neither Thurston nor the
   gazetteers tie them to any seat. The seat itself is visible:
   - **Tanjore gazetteer (Hemingway 1906), p. 72:** among the district's chief maṭhas, beside the Sudra Śaiva
     maṭhas of Dharmapuram, Tiruvāvaḍuturai, Tiruppanandāl and Tiruppugalūr, is "the Brahman Smarta math of
     Sankaracharya at Kumbakonam".
   - **Ibid., pp. 218–19 (Kumbakonam):** "an important Smārta religious institution here in the math of
     Sankaracharya, which is said to have been founded in the time of Sankarachārya himself by a Tanjore king,
     who wished the saint to reside in his dominions. Its income is nearly Rs. 14,000 annually, and the head of
     it appoints the managers of three temples, one of which is at Conjeeveram. He nominates his own successor.
     The math contains a library of some 150 books … in Telugu and Sanskrit."
   - **Chingleput Manual (Crole 1879), p. 26:** Śaṅkara "paid particular attention to Conjeveram, where he worked
     many miracles, and founded a matam". This is history; Crole does not say a maṭha exists there in his day.
   - **Ibid., pp. 116–17 (Conjeeveram):** the Kāmākṣī temple is "neither … Dwaita nor Adwaita", with no
     Śaṅkarācārya connection named. When Hyder Ali approached (c. 1780) the images were carried off, and "the
     image of Kamatshi was of gold, and is said to have been taken possession of by the Rajah of Tanjore". The
     maṭha's own tradition links this flight to its stay at Kumbakoṇam under Tanjore patronage; Crole does not.
   - The name **Kāmakoṭi** does not occur in any colonial volume read. It first appears in this study in the
     revised Puri gazetteer (1977): the Kāñcī Kāmakoṭi Pīṭha's ashram at Purī, founded 1973.
   - So the colonial record places the Śaṅkara maṭha at Kumbakoṇam, with Kāñcī as the scene of Śaṅkara's
     founding and the site of one temple it manages. It gives the maṭha an income, a temple patronage and a
     library, but no caste following. Thurston's Gāṇiga note places *Śṛṅgeri* branches at Tanjore and
     Kumbakoṇam too.
   - Whether the silence about followers reflects the informants or the institution is a question for other
     sources: maṭha records, Tamil and Sanskrit literature, inam registers. The 1932 Legislative Council lists of
     religious inams for Chingleput and South Arcot on IA (`TNLC-DB-1932-62-2-QH14/15`) do not name it in their
     OCR.
4. **Change over time.**
   - In Madras the census shows movement in the Śaiva/Vaiṣṇava balance between 1871 and 1891 (Kistna, North
     Arcot), but not in Śaṅkara's following as such.
   - The direct evidence of change is still Bombay's Kanara (1881).
   - Thurston's 1888 Bellary episode (Śṛṅgeri Svāmi vs Liṅgāyats) shows Śṛṅgeri touring and asserting
     precedence in the same years.

## 4. Not done / possible next steps

- **Done since:** district counts of Brahman sub-divisions, read from the 1891 table images
  (`../census-images/results/madras1891_*`). By Thurston's list of Smārta sub-castes, Smārtas are 48% of
  Tamil-division Brahmans against 23% Aiyaṅgārs. By district: Tanjore 64%, Trichinopoly and Tinnevelly about
  55%, Chingleput only 12% (60% Aiyaṅgār).

- **District counts of Smārta Brahmans.** These need the 1871 table volume (not found on IA) or the 1891 caste
  tables, where Brahman sub-divisions (Vaḍama, Bṛhaccaraṇam, Smārta, Teṅgalai, Vaḍagalai …) are tabulated by
  district (`data/census/india.history.resource.52257.txt`). The OCR tables there are badly scrambled.
- **Maṭha presence from the manuals and gazetteers (option 4).** Done for Kumbakoṇam and Kāñcī (finding 3)
  and for Śṛṅgeri (`../sringeri/README.md`: no Madras volume locates a Śṛṅgeri maṭha). Puṣpagiri, Virūpākṣa and
  Śivagaṅgā could still be collected from the "Places" chapters; the OCR is downloaded.
- **Missing volumes.** The North Arcot gazetteer (1905) failed to download. For Chingleput, IA has only the
  1915 *Statistical Appendix* (`dli.csl.3250`, `dli.ministry.08445`, `in.ernet.dli.2015.212648`); a search
  (Nov 2026) found no descriptive volume, so Crole's *Manual* (1879) remains the descriptive source.
- **Weak rows to review.** The weaker SMARTA rows (Tambala, Tigala, Sastri, Prathamaśākhī, the Dīkṣitars) are
  marked `low` in `results/thurston_coded/`.

## Files

| file | content |
|---|---|
| `data/thurston/vol1–7.txt` | Thurston, Gutenberg text |
| `results/thurston/entries.tsv`, `packets/` | entry index; cue-sentence packets |
| `results/thurston_coded/vol1–7.tsv` | coded rows (246) |
| `data/census/sect_ratios_1871_1891.tsv` | district Śaiva:Vaiṣṇava ratios |
| `data/census/*.txt` | census report OCR (1871, 1891 report and tables) |
| `data/selection.tsv`, `data/ia_ocr/` | manuals and gazetteers (surveyed, not coded) |
| `scripts/thurston_entries.py` | entry splitter |
