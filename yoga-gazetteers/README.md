# Yoga, yogis and Jogis in the gazetteers, 1866–1989

What did "yoga", "yogi" and "Jogi" mean to the people who wrote the colonial district gazetteers, caste glossaries
and census reports, and did that change by the time of the revised state gazetteers after independence?

**Synthesis page:** `SYNTHESIS.html`, published at https://claude.ai/artifact/SxskLHSxdoBHtVTZ5U9znQ.

**Public repository:** https://github.com/kengoharimoto/gazetteer-studies, with `../gazetteer-vedanta/`. It leaves out
the raw passage layers, which carry long extracts from the post-independence gazetteers that may still be in
copyright: `data/*passages.tsv`, `data/batches/`, `data/fakir_batches/`, `data/order_batches/`,
`data/region_batches/` and `results/kwic.tsv`. The coded results (`results/*coded*`), with their short quotations,
are included. The scripts rebuild the left-out files from the Internet Archive OCR (`scripts/fetch.py`, then
`scripts/passages.py` and the other `*_passages.py`). Licence: CC BY 4.0 for the reports, notes and coded data, MIT
for the scripts (`../LICENSE.md` in the public repository).

## The answer

Matching the synthesis page (`SYNTHESIS.html`). Figures include the regional supplement (Bombay after 1890, Rajputana,
revised Rajasthan, Baluchistan).

1. **The officials split "yogi" into two words.** *Yoga* was Patañjali's philosophy, learned and respectable. *Jogi*
   named living people: a caste, members of the Nāth order, a census heading. Their definitions trace the Jogi to
   Patañjali's Yoga and then describe living Jogis as a caste or as mendicants; the census merged Jogis with every
   other ascetic heading.
2. **They wrote about Jogis as administrators, not as critics.** Their judgement is neutral in 94% of passages
   (691 of 737). The fakir-showman of the travel books hardly appears even under other words. Contempt is confined to
   the criminal-caste literature and a few quoted authorities. An officer recording castes, land and revenue had
   little use for the exotic ascetic.
3. **The prestige of the word changed hands later.** Between 1901 and 1931 the Jugi weavers of Bengal and Assam
   claimed the names Jogi and Yogi as a sign of ascetic descent, against the resistance of census officials. After
   independence the revised gazetteers treat yoga with respect, but mostly as philosophy and spirituality; yoga as
   exercise first appears in the 1950s and 1960s.

Against the literature (`results/literature.md`): the broad narrative of a disreputable "Jogi" replaced by a
respectable "yoga" holds, with four refinements:
- the officials draw the yoga/Jogi split themselves, through the spelling;
- the colonial district record is neutral and taxonomic rather than hostile;
- the Jogi is a caste or a Nāth ascetic depending on region, not a fakir-performer;
- the hostile stereotype survives mainly in the criminal-tribes literature and in Barnett's sentence, reprinted in
  1968.

## Evidence

### 1. What the words meant

- **Frequency.** The district writers' word is **Jogi** (about 11–22 hits per million words); "yoga" occurs 1–2
  times and "yogi" 1.5–2.5 times per million words. Yoga as a philosophy or practice is 4–5% of the colonial
  passages on these words.
- **Definitions trace the Jogi to Patañjali, then describe someone else.** Several writers say the living Jogi bears the name of a philosophy he no
  longer represents:
  - "The Jogi is, strictly speaking, a Shaiva, and a follower of the Yoga, or philosophical school of Patanjali"
    (Atkinson, NWP Gazetteer V, 1879; P00637). The same entry then describes Jogis as mountebanks and mendicants.
  - "In its literal and much-respected sense, Yogi means a follower of Patanjali's Yoga school who is devoted to
    divine meditation" (Bombay Gazetteer IX-1, 1901; P00284), set against the vagrant Jogi.
  - "Jogis … derive the name from a Yoga school of philosophy" (NWP and Oudh Census Report, 1891; P00413); "many"
    are then called mountebanks and fortune-tellers.
  - "The term Jogi is derived from the Sanskrit yoga, union, and means a follower of the Yoga or Patanjal school of
    philosophy" (Bombay Census 1911, PR00055; Enthoven II, 1922, PR00015), followed in both by an account of a caste.
  - Sind is blunter: "the word Jogi, or Yogi, simply means one who practises yog, i.e., an ascetic" (1907; PR00042;
    OCR "Jopi").
  - Rose's *Glossary* (1911; P01009) has two classes: "the Jogis proper, a regular religious order", and low-caste
    Jogis who are rascally beggars.
- **Classification blurs the Jogi into the other ascetics.** Gait: "Yogi or Jogi is a word of much greater ambiguity … used in a very wide sense
  of any ascetic" (Bengal 1901, para. 787). The NWP census of 1891: "the words Goshain, Bairagi, Jogi, Saniyasi were
  apparently used by a considerable proportion of the enumerators as interchangeable". The census filed Jogis under
  "Faqir" (at least eight UP district gazetteers of 1903–11; Punjab 1891 "Jogi & Rawal"), merged them with "Nath"
  (Rajputana 1931), and lists "Sanyasis, Vairagis, Jogis, Atits or Gosais" together (Cutch, 1880).
- **Yoga as practice** is rare and means meditation or trance: Dayānanda's yoga vidyā (UP07 1911; RUS1 1916), the
  Bairāgī's yoga-daṇḍa (Thurston 1909), prāṇāyāma in the Brahman sandhyā (Thurston 1909), the Radhasoami "practice
  of yoga according to the modified forms taught by the gurus" (Bombay Census 1901). No colonial passage treats
  āsana as exercise or health.

### 2. Who the Jogi was

- **By period** (passages on Jogis only): caste 50%, ascetic order 31%, saint 11%, beggar 9% in 1866–1890 (266
  passages); caste 30%, order 42%, saint 19%, beggar 9% in 1891–1935 (356); caste 40%, order 28%, saint 22%, beggar
  10% in 1954–1989 (50). The rise of "order" after 1891 comes largely from Rose's Punjab glossary.
- **By region** (1866–1935): mainly a **caste** in Bengal (32 of 43), Madras (22 of 28), the CP (21 of 35) and the
  UP (103 of 201); mainly a **Nāth ascetic or saint** in the Punjab (161 of 194) and in Mysore and Kanara; as often a
  **beggar or performer** as anything else in Bombay (21 of 77). Rajputana: Kānphaṭa temple priests at Pushkar,
  officiants at Bhil death rites, a low burying caste, a "wandering tribe" blamed for smallpox (Adams 1899).
  Baluchistan (1906–08): snake-catching Jogis "begging from village to village" in a Brahui ballad (Jhalawan;
  PR00198), and the shrine in Quetta fort of Pani Nath, "a Hindu Yogi" and disciple of Gorakhnāth, buried alive after
  forty years' contemplation, with a Shivratri fair since 1892 (Quetta-Pishin; PR00202). The Hinglaj volume (Las Bela)
  describes the goddess pilgrimage without naming Jogis.
- **Muslim Jogis.** In the Punjab census of 1891, 36,718 of the 75,469 under "Jogi & Rawal" were Musalmān; the
  glossaries describe Muhammadan Jogis (Rawals).
- **Bengal and Assam:** a **weaving caste** (Hunter 1875–77, ten districts; Bengal District Gazetteers 1909–12);
  see Evidence 5. Malabar's "Yogi Gurukkals" are a low but learned caste of exorcists and schoolmasters (Thurston
  1909; P00406).

### 3. How they were judged

- Neutral in 94% of colonial passages on yoga, yogis and Jogis; negative in 27 of 737. These come from:
  - the **criminal-caste and vagrancy literature**: Thurston on the Telugu Jogis (1909), the CP gazetteers (1907,
    1909), the Etah police circle (1911);
  - **Rose's Punjab glossary** (1911–19), on the Rawals and Muhammadan Jogis;
  - comments on **Nāth institutions**, such as Tilla, "not a very estimable body" (1883; P01112);
  - **L. D. Barnett**: "the Yoga system in its practical side is largely based upon vulgar ideas of magic and
    Shamanism, and hence many of its professors have always been vulgar charlatans" (Damoh 1911; P00166), copied
    unchanged into the revised Amravati gazetteer of 1968 (P01260).
- The only positive colonial passage on a Jogi caste is Noakhali's "well educated and enterprising race" (1911;
  P00016). The other positive colonial passages concern Gorakhnāth as a learned author, respected Kānphaṭa hermits
  and ancient yogis of the caves.

### 4. Under other words: fakirs, sādhus and the ascetic orders

Round two coded 1,508 "fakir/faqir" and "sādhu" passages (1,267 relevant; `results/fakir_coded_all.tsv`); round
three 1,074 sannyāsī, gosāīn and bairāgī passages (883 relevant; `results/order_coded_all.tsv`). The test: are
contempt and spectacle recorded under these words instead?
- **Judgement is just as neutral:** negative in 5% of fakir and sādhu passages (66) and 3% of order passages (29).
  The order passages' negatives concern money-lending, lapsed celibacy, the Vallabha Gosains' authority and the
  historical raiders.
- **Practice is rarely described:** 5% of fakir and sādhu passages (58), 10% of order passages (92). Most are Sufi
  exercises recorded by the glossaries (dhikr, the forty-day chilla, ecstatic ḥāl, self-wounding for alms; Russell &
  Hira Lal 1916, Rose 1919) or saints' legends (twelve years in the Chenab, fifty-one years on a sandhill). The
  spectacle-ascetic is nearly absent: one bed of thorns (Thurston 1909), hook-swinging only as a practice "stopped by
  Akbar" (Allahabad 1911). The one detailed account of feats is Adams on Dādūpanthī sādhus, "never requiring to sleep
  in the recumbent position, others being able to withstand all weathers without clothes, lie on sharp points"
  (Western Rajputana States, 1899), a medical officer's neutral observation.
- **"Fakir" was not a Muslim word.** Where a religion is stated, Hindu or Sikh ascetics are 29% of "fakir" passages in
  1866–1890 (41 against 99 Muslim) and 24% in 1891–1935 (92 against 297): "the caste of faqirs called Sattnami" (Oudh
  1877), the Udāsī "fakirs" of Guru Ram Rai (Dehra Dun 1911). Half of the colonial "fakir" passages name no religion.
  "Sādhu" is rare before independence (113 colonial passages against 987 for "fakir"), except in Rajputana, where the
  census treats "the ascetic caste of Sadhus" as a caste (1911). After 1954 "sādhu" replaces "fakir" for Hindu
  ascetics.
- **The orders are seldom connected with yoga:** 45 of 883 passages, almost always through classification (above)
  or shared seated burial ("Gosains and Jogis are buried sitting up in salt; and used to be so buried alive before
  our rule", Karnal 1919). Only three link an order to yoga as practice: the Dandis' "Yoga practices as preached by
  Patanjali" (Bombay 1901), the Bairāgī's yoga-daṇḍa (Thurston 1909), Dayānanda (UP 1911).
- **The orders appear as institutions and estates.** In 1891–1935 a fifth of order passages describe married
  householders (Gosain and Bairāgī zamindars, money-lenders, Atīth castes), who "have fallen away from the ideas of
  self-sacrifice and poverty in which the orders originated" (Bilaspur 1910). Armed ascetics appear in 72 passages in
  the past tense and 2 in the present (Pinch's claim confirmed): the Hardwar battles of 1760 and 1796, the Sannyāsī
  raids in Bengal in the 1780s, "Formerly Gosavis took service as soldiers" (Satara 1885).

### 5. Change: the Jugis who became Yogis, and yoga after independence

- **The Jugi campaign** (`census/README.md`): the thread and Brahman-descent legends (Risley 1891); objection to the
  spelling "Jugi", popularly derived from "Jungi" (Gait, Bengal 1901); "Most Jugis call themselves Nath" (BG17 1910,
  P00020) and "the Jugis, or Jogis as they prefer to be called" (Noakhali 1911, P00015); "Yogi" claimed (O'Malley,
  Bengal 1911); a Brahman enumerator "would rather cut off his hand than write down a Jugi as Jogi" (Thompson, Bengal
  1921); "Yogi" tabulated as the caste name in Assam, "to emphasise their ascetic origin" (Lloyd 1921); the priests'
  claim to be recorded "merely as Brahmans" refused (Porter, Bengal 1931). The claim rested on lineage, never on
  bodily practice.
- **Modern yoga before independence** appears in three places: the Theosophical Society (13 institutional notices,
  1901–31 census returns); Keshub Sen's "relapse" into "the mysticism of the Yogis" (Russell & Hira Lal 1916;
  P00131); and Vivekananda in the Howrah gazetteer, where the Ramakrishna Mission had its headquarters: he
  "travelled in America, expounding the doctrines of yoga and Vedântism" (O'Malley 1909; P00031–36).
- **After independence** (revised gazetteers 1954–89) Jogis are rarely mentioned. Yoga appears in Sanskrit curricula
  and manuscripts ("Sankhya, Yoga, Nyaya, Vedanta"; P01517, P01339); through Vivekananda, Aurobindo and the
  Ramakrishna Mission, always respectfully; and in a few institutions: Kaivalyadhāma's "Physical Culture and Yoga
  School" and "College of Yoga" at Lonavla (Poona 1954; P01316, P01322), the Śivayoga Mandira (Bijapur 1959;
  P01391), a "Patanjal Yoga Ashram" (Churu 1970). The first definition of yoga as exercise is the Alwar glossary's
  "Hath-yogi: a person following Yoga as a means of physical cultures" (1968). The many "physical culture" clubs in
  these volumes are gymnasia, not yoga.

## Corpus

The OCR downloaded for `../gazetteer-vedanta/` was reused; nothing new was fetched. Duplicate scans were dropped: three
Cornell scans of Atkinson are copies of AT01, AT02 and AT11 by text overlap (`scripts/merge.py`).

| generation | years | volumes | words | contents |
|---|---|---|---|---|
| G1 | 1866–1890 | 103 | 21.2 M | Bombay Gazetteer (Campbell), Hunter's *Statistical Account of Bengal*, Atkinson's NWP Gazetteer, Oudh Gazetteer, Punjab Gazetteers 1883–84, Grant's CP, Madras manuals, Rice's Mysore |
| G2 | 1891–1935 | 165 | 21.2 M | UP (Nevill), Bengal, Bihar and Orissa, CP, Punjab and Madras district gazetteers; Rose, Russell & Hira Lal, Thurston; census reports (NWP 1891, Madras, Bombay 1901) |
| G3 | 1954–1989 | 38 | 9.6 M | revised state gazetteers (Maharashtra, Karnataka, Madras, UP, Bihar, West Bengal, Orissa, Haryana, MP) |

A regional supplement adds 53 volumes (`regions/data/selection.tsv`; OCR gitignored, re-fetch with
`scripts/fetch.py`; catalogue `data/corpus_regions.tsv`; term counts `results/term_counts_regions.tsv`):
- **Bombay 1891–1935 (G2):** Enthoven's *Tribes and Castes of Bombay* (1920–22), the *Imperial Gazetteer* Bombay
  volumes (1909), the Sind gazetteers (1907, 1919, 1927), Nasik (1913), and the census reports 1891–1931.
- **Rajputana 1875–1931 (G1, G2):** the *Rajputana Gazetteer* (1879–80), Ajmer-Merwara (1875, 1904), Adams's
  *Western Rajputana States* (1899), Eastern Rajputana (1906), Erskine's Mewar (1908) and Western Rajputana and
  Bikaner (1909) volumes, the *Imperial Gazetteer* Rajputana volume (1908), and the census reports 1881–1931.
- **Revised Rajasthan district gazetteers (G3):** 15 volumes, 1964–79.

- **Baluchistan 1906–1908 (G2):** the Imperial Gazetteer provincial volume (1908) and six Baluchistan District
  Gazetteers (Sarawan–Kachhi–Jhalawan, Makran, Las Bela, Loralai, Quetta-Pishin, Bolan–Chagai), downloaded for the
  Xuanzang study and added on 2026-11-06. They give 5 round-one passages (PR00198–PR00202) and 50 round-two passages
  (FR00196–FR00246; mostly the name of a chief, Mir Fakir Muhammad, and Muslim fakirs, including Rifāʿī zikr and
  self-wounding in Makran; "Hindu Fakirs" on pilgrimage in Kachhi), and none for round three. Batches
  `data/region_batches/*_baluch.tsv`, codes `results/region_coded/*_baluch.coded.tsv`.

Remaining gaps: Madras G1 and G2 are thin; there is no Hyderabad, Kashmir or Assam gazetteer volume (Assam is
covered only through the census, in `census/`).

## Method

1. `scripts/corpus.py`: catalogue of the OCR files with region, year and generation (`data/corpus.tsv`).
2. `scripts/lexicon.py`: counts of 13 term families per volume (`results/term_counts.tsv`) and keyword-in-context
   lines for the core families (`results/kwic.tsv`).
3. `scripts/passages.py`: nearby hits merged into 1,592 passages; 254 index or table passages set aside; the rest
   split into nine batches (`data/batches/`).
4. Coding by nine agents following `data/CODING_INSTRUCTIONS.md`:
   - **sense** (PHIL, DISCIPLINE, MODERN, ASCETIC, MENDICANT, CASTE, SAINT, or irrelevant);
   - the **writer's attitude**;
   - **tags**;
   - a **verbatim quote** for each passage.
5. `scripts/merge.py`:
   - merges the batches (`results/coded_all.tsv`, 1,338 rows);
   - checks every quote against its passage (1,002 of 1,004 verbatim; the two failures are a doubled quotation mark
     and an OCR fragment);
   - drops duplicate-scan rows and repeats within a generation (68 rows);
   - flags revised-gazetteer passages copied from colonial ones (`copy_of`);
   - writes `results/sense_by_gen.tsv` and `results/tags_by_gen.tsv`.
6. Check: 20 randomly drawn coded passages were reread against the text, and all 20 codes were acceptable.

Passage ids (P00001…) refer to `data/passages.tsv` and `results/coded_all.tsv`, where the full context, volume and
year are given. Page numbers are given where the OCR shows a folio.

## Caveats

- **Counts are of passages, not of opinions.** One glossary article on Jogis yields many passages, so Rose
  (Punjab) and Thurston (Madras) weigh heavily in G2.
- **Attitude is coded conservatively**, from the writer's own wording. Reported opinions ("the people revere him")
  are neutral.
- **Round two** coded 1,332 "fakir/faqir/fakeer" and "sādhu" passages with `data/CODING_INSTRUCTIONS_FAKIR.md`. Its
  pipeline is `scripts/fakir_passages.py` and `scripts/fakir_merge.py`. All 1,162 quotes were verbatim, 7 repeats
  were excluded, and 15 of 16 randomly checked codes were right; the miss was minor. Religion is coded only where
  the passage states it, so the Hindu share of "fakir" is a lower bound.
- **Round three** coded 963 sannyāsī, gosāīn/gosāvī/gosvāmī and bairāgī passages with
  `data/CODING_INSTRUCTIONS_ORDERS.md` (`scripts/order_passages.py`, `scripts/order_merge.py`). All 787 quotes were
  verbatim, 4 repeats were excluded, and 13 of 14 randomly checked codes were right. The miss was a "no yoga link"
  for a list that groups Jogis with Sannyāsīs, so the yoga-link count is a lower bound. Many of these passages were
  coded in `../gazetteer-vedanta/` for Daśanāmī allegiance; this round asks different questions.
- **The term list is English-spelling based** (yoga, yogi, jogi, jugi, Kanphata, Gorakhnath, samādhi, āsana,
  prāṇāyāma …). Passages that describe yogic practice without these words (e.g. "an ascetic sitting with his arm
  raised") are not captured. *Udāsī*, *nāgā* (as a separate search term) and *aghorī* were not searched separately.
