# Yoga, yogis and Jogis in the gazetteers, 1866–1989

What did "yoga", "yogi" and "Jogi" mean to the officials who wrote the gazetteers, caste glossaries and census
reports, and how did that differ by region and change over time? The colonial volumes (1866–1935) are compared with
the revised state gazetteers (1954–1989). References and summaries of the literature: `results/literature.md`.

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

1. **Two words for two things.** *Yoga* meant Patañjali's philosophy, and the rare spelling *Yogi* mostly an
   ascetic of the past. *Jogi* meant living people. The officials knew that Jogi came from Yoga, and then described
   Jogis who had nothing to do with it.
2. **Who the Jogi was depended on the region.** In the east, the south and the Gangetic plain he was a member of a
   caste, low in rank and doing ordinary work: weaving, farming, catching snakes. In the Punjab he was an ascetic of
   the Nāth order. In Bombay he was often a wandering singer or beggar. Where he was a caste, the officials
   recorded him as they recorded any other caste: by rank and trade.
3. **The change came after 1900.** Within the colonial period the picture changed little. Then the Jugi weavers of
   Bengal and Assam claimed the names Jogi and Yogi (1901–1931). After independence the revised gazetteers seldom
   mention Jogis, and they treat yoga with respect: as philosophy, through Vivekananda, and from the 1950s as
   exercise.

## Evidence

### 1. Meaning: two words for two things

- **Frequency.** The district writers' word is **Jogi** (about 11–22 hits per million words); "yoga" occurs 1–2
  times and "yogi" 1.5–2.5 times per million words. Yoga as a philosophy or practice is 4–5% of the colonial
  passages on these words.
- **The spelling "Yogi" leans to the past.** It is rare: about 120 hits in the colonial volumes against about 1,270 for
  "Jogi". Of the 46 colonial coded passages that use it, 25 refer to an ascetic or holy man of antiquity, legend or
  sculpture (cave-dwellers at Kanheri, seven of them from the Thana volume of 1882; Śiva "the great Yogi"; saints'
  legends); 13 to living people (Śaiva sects in lists, a corporation of yogis under a mahant, Malabar's Yogi
  Gurukkals); 8 are definitions or general statements, only one of which (Bombay 1901, below) makes a Yogi a follower
  of Patañjali. "Jogi is a corruption of Yogi, a term applied originally to the Sanyāsis well advanced in the practice
  of yogābhyās" (Punjab 1914). Counts by hand from `results/coded_all.tsv`, November 2026.
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
- **When the census counted people, the word blurred.** Gait: "Yogi or Jogi is a word of much greater ambiguity …
  used in a very wide sense of any ascetic" (Bengal 1901, para. 787). The NWP census of 1891: "the words Goshain, Bairagi, Jogi, Saniyasi
  were apparently used by a considerable proportion of the enumerators as interchangeable". The census filed Jogis under
  "Faqir" (at least eight UP district gazetteers of 1903–11; Punjab 1891 "Jogi & Rawal"), merged them with "Nath"
  (Rajputana 1931), and lists "Sanyasis, Vairagis, Jogis, Atits or Gosais" together (Cutch, 1880).
- **Yoga as practice** is rare and means meditation or trance: Dayānanda's yoga vidyā (UP07 1911; RUS1 1916), the
  Bairāgī's yoga-daṇḍa (Thurston 1909), prāṇāyāma in the Brahman sandhyā (Thurston 1909), the Radhasoami "practice
  of yoga according to the modified forms taught by the gurus" (Bombay Census 1901). No colonial passage treats
  āsana as exercise or health.

### 2. Region: who the Jogi was

When a gazetteer speaks of living Jogis it means one of two kinds of people: most often a **caste** (born into, low
in rank, doing ordinary work), otherwise an **ascetic**, usually of the Nāth or Kānphaṭa order of Gorakhnāth. Which
of the two depends far more on the region than on the date.

- **Four kinds.** Each passage that uses *Jogi* or *Jugi* (607) is sorted by what it says the Jogi was:
  *caste* (birth, rank, occupation), *ascetic* (initiation, ear-rings, monasteries, temple service), *saint or shrine*
  (one holy man, living or legendary, or his shrine and fair), *beggar or performer* (wandering singers,
  snake-catchers, mendicants not tied to an order). Passages that speak of Gorakhnāth or the Kānphaṭas without calling
  anyone a Jogi (62; most are legends of Gorakhnāth himself, and two call the Kānphaṭas Gosāvis) are not counted.
- **By region, 1866–1935** (passages: caste / ascetic / saint / beggar): mostly **caste** in Madras (22/2/0/4),
  Bengal (32/8/1/1), the CP (21/7/4/3) and the UP (102/58/16/8); **caste or beggar** in Bombay and Sind (25/16/0/21);
  **caste or ascetic** in Rajputana (13/15/1/1); mostly **ascetic** in the Punjab (20/105/38/13; largely Rose's
  glossary, 1911–19) and Mysore and Kanara (1/8/0/4). Passages, not persons. Rajputana: Kānphaṭa temple priests at
  Pushkar, officiants at Bhil death rites, a low burying caste, a "wandering tribe" blamed for smallpox (Adams 1899).
  Baluchistan (1906–08): snake-catching Jogis "begging from village to village" in a Brahui ballad (Jhalawan;
  PR00198), and the shrine in Quetta fort of Pani Nath, "a Hindu Yogi" and disciple of Gorakhnāth, buried alive after
  forty years' contemplation, with a Shivratri fair since 1892 (Quetta-Pishin; PR00202). The Hinglaj volume (Las Bela)
  describes the goddess pilgrimage without naming Jogis.
- **What the Jogi caste did.** Where the officials meant a caste, it was one people were born into, low in rank,
  doing ordinary work; its tie to yoga was the name and a claimed descent from ascetics:

  | Region | What the Jogi caste did | In the gazetteers' words |
  |---|---|---|
  | Bengal and Assam | Weavers (“Jugi”), ranked below the Tantis; cultivators, lime-burners | "Weaving is the hereditary occupation of two Hindu castes, Tantis and Jugis" (Howrah 1909, P00037) |
  | United Provinces | Settled cultivators; in some villages, landholders | village lands "passed into the hands of Brahmans, Banias, Sonars and Jogis" (Aligarh 1909, P00584; also Saharanpur 1921, P00537) |
  | Punjab | Low-caste attendants at minor shrines, musicians, diviners; about half Muslim (1891) | "one of the lowest of all castes, and receives the offerings made to the impure gods" (Karnal 1884, P01102; Rose 1911, P01046) |
  | Rajputana | Holders of jāgīr villages with the Chāraṇs; makers of gunpowder and blankets; quarrymen | "gunpowder is manufactured here by Jogis" (Bharatpur 1906, PR00091) |
  | Central Provinces | Sub-castes such as the Bisātī pedlars; a village proprietor | "The proprietor is a Jogi" (Drug 1910, P00122) |
  | Madras | Telugu Jogis: snake-catchers, pig-keepers, mendicants; Malabar’s Yogi Gurukkals: exorcists and schoolmasters | "people who catch snakes, and keep pigs, and practise mendicancy" (Salem 1883, P00351; Thurston 1909, P00406) |
  | Bombay | Wandering singers and beggars, in many sub-divisions (Ker-, Kindri-, Mendar-jogi …) | "Jogerus or Jogis, originally Yogis that is meditators, a class of singing beggars" (Dharwar 1884, P00312) |

- **Muslim Jogis.** In the Punjab census of 1891, 36,718 of the 75,469 under "Jogi & Rawal" were Musalmān; the
  glossaries describe Muhammadan Jogis (Rawals).
- **Bengal and Assam:** a **weaving caste** (Hunter 1875–77, ten districts; Bengal District Gazetteers 1909–12);
  see section 3. Malabar's "Yogi Gurukkals" are a low but learned caste of exorcists and schoolmasters (Thurston
  1909; P00406).

### 3. Change: after 1900

- **Within the colonial period the kinds of Jogi change little:** caste 52%, ascetic 31%, saint 7%, beggar 9% in 1866–1890 (246 passages);
  33/44/13/10% in 1891–1935 (325); 50/33/6/11% in 1954–1989 (36). The rise of "ascetic" after 1891 comes largely
  from Rose's Punjab glossary.
- **The Jugi campaign** (`census/README.md`): the thread and Brahman-descent legends (Risley 1891); objection to the
  spelling "Jugi", popularly derived from "Jungi" (Gait, Bengal 1901); "Most Jugis call themselves Nath" (BG17 1910,
  P00020) and "the Jugis, or Jogis as they prefer to be called" (Noakhali 1911, P00015); "Yogi" claimed (O'Malley,
  Bengal 1911); a Brahman enumerator "would rather cut off his hand than write down a Jugi as Jogi" (Thompson, Bengal
  1921); "Yogi" tabulated as the caste name in Assam, "to emphasise their ascetic origin" (Lloyd 1921); the priests'
  claim to be recorded "merely as Brahmans" refused (Porter, Bengal 1931). The claim rested on lineage, never on
  bodily practice: the caste borrowed the prestige of ascetic descent that the word already carried. The dates
  correct Debnath (known only from a snippet), who places the change of name around 1911 and the Brahman claim in
  1931: the spelling campaign began in 1901, and the 1931 claim was the priests'.
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

## The gazetteers and the history of modern yoga

Historians describe a split in the colonial period: a respectable yoga rebuilt from Patañjali's text (De Michelis
2004; White 2014) and a living yogi lumped with the fakir and despised (Singleton 2010, ch. 2–3). Their evidence is
mainly travel writing, missionary tracts and the reformers' own books. Others see the living yogi differently: a
sinister figure of power long before colonial rule (White 2009), a soldier disarmed by the Company (Pinch 2006), a
caste of weavers in Bengal (Ondračka 2022; Bordeaux 2022). The officials' records agree in part:
- **Respectable yoga was Patañjali's** (De Michelis; White 2014): agrees; the officials draw the line themselves,
  between Yoga and Jogi.
- **The living yogi was a despised fakir and showman** (Singleton; White 2009): partly; Jogis were filed with fakirs
  as mendicants, but contempt and feats are rare.
- **Colonial "Jogi" meant mainly a caste** (Ondračka 2022; Bordeaux 2022): regional; true in Bengal, Madras, the CP
  and the UP, not in the Punjab.
- **The armed ascetic had vanished by 1900** (Pinch 2006): agrees; 72 passages in the past tense, 2 in the present.
- **Yoga as exercise appears only from the 1920s** (Alter; Singleton): agrees; first seen in 1954 and 1968.
- **The Jugis adopted "Yogi" around 1911** (Debnath, unchecked snippet): corrected; the spelling campaign dates from
  1901, Assam tabulated "Yogi" in 1921, and the 1931 Brahman claim was the priests'.

No published study has used these sources systematically on this question; Briggs (1938) comes closest.

### Evidence for the contempt, showman and soldier claims

To test these claims beyond the Jogi passages, round two coded 1,508 "fakir/faqir"
and "sādhu" passages (1,267 relevant; `results/fakir_coded_all.tsv`) and round three 1,074 sannyāsī, gosāīn and
bairāgī passages (883 relevant; `results/order_coded_all.tsv`), to see whether contempt, the spectacle-ascetic of the
travel books or the armed ascetic turns up under these words. Judgement was coded from the writer's own wording.
- **Contempt** is rare in the Jogi passages:
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
- **Contempt under the other words is as rare:** negative in 5% of fakir and sādhu passages (66) and 3% of order
  passages (29). The order passages' negatives concern money-lending, lapsed celibacy, the Vallabha Gosains' authority and the
  historical raiders.
- **The showman: practice is rarely described.** 5% of fakir and sādhu passages (58), 10% of order passages (92). Most are Sufi
  exercises recorded by the glossaries (dhikr, the forty-day chilla, ecstatic ḥāl, self-wounding for alms; Russell &
  Hira Lal 1916, Rose 1919) or saints' legends (twelve years in the Chenab, fifty-one years on a sandhill). The
  spectacle-ascetic is nearly absent: one bed of thorns (Thurston 1909), hook-swinging only as a practice "stopped by
  Akbar" (Allahabad 1911). The one detailed account of feats is Adams on Dādūpanthī sādhus, "never requiring to sleep
  in the recumbent position, others being able to withstand all weathers without clothes, lie on sharp points"
  (Western Rajputana States, 1899), a medical officer's neutral observation.
- **"Fakir" was not a Muslim word**, so filing Jogis under "Faqir" (section 1) classed them as mendicants. Where a religion is stated, Hindu or Sikh ascetics are 29% of "fakir" passages in
  1866–1890 (41 against 99 Muslim) and 24% in 1891–1935 (92 against 297): "the caste of faqirs called Sattnami" (Oudh
  1877), the Udāsī "fakirs" of Guru Ram Rai (Dehra Dun 1911). Half of the colonial "fakir" passages name no
  religion. "Sādhu" is rare
  before independence (113 colonial passages against 987 for "fakir"), except in Rajputana, where the census treats "the ascetic caste of Sadhus" as a caste (1911). After 1954 "sādhu" replaces "fakir" for Hindu
  ascetics.
- **The orders are seldom connected with yoga:** 45 of 883 passages, almost always through classification (above)
  or shared seated burial ("Gosains and Jogis are buried sitting up in salt; and used to be so buried alive before
  our rule", Karnal 1919). Only three link an order to yoga as practice: the Dandis' "Yoga practices as preached by
  Patanjali" (Bombay 1901), the Bairāgī's yoga-daṇḍa (Thurston 1909), Dayānanda (UP 1911).
- **The orders appear as institutions and estates.** In 1891–1935 a fifth of order passages describe married
  householders (Gosain and Bairāgī zamindars, money-lenders, Atīth castes), who "have fallen away from the ideas of
  self-sacrifice and poverty in which the orders originated" (Bilaspur 1910). **The soldier:** armed ascetics appear in 72 order passages in the past tense and 2 in the
  present: the Hardwar battles of 1760 and 1796, the Sannyāsī raids in Bengal in the 1780s, "Formerly Gosavis took
  service as soldiers" (Satara 1885).

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
