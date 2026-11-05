# Coding instructions, round three: sannyāsī, gosāīn and bairāgī in the gazetteers

You code passages from British Indian district gazetteers, caste glossaries and census reports (1866–1935), and from
the revised Indian state gazetteers (1954–1989). The study asks what "yoga", "yogi" and "Jogi" meant to the writers of
these texts. Earlier rounds coded passages containing yoga, yogi and Jogi, and then fakir and sādhu. This round codes
passages containing **sannyāsī (sanyasi, sunnyasee), gosāīn (gosain, gosavi, goswami) and bairāgī (vairagi)**.

The questions:
1. **What are these people to the writer?** A renunciant order, a hereditary householder caste, a Vaiṣṇava
   hereditary guru family (e.g. Vallabha or Chaitanya Gosains, Bengal Goswamis), a census category, or a local holy man?
2. **Practice and yoga.** Does the passage describe ascetic or contemplative practice? Does it connect the order with
   yoga or yogis?
3. **Armed ascetics.** Are armed or fighting ascetics (Nāgās, Gosain soldiers, Sannyasi raiders) mentioned, and in
   the past or the present tense? This tests the claim that by 1900 the armed ascetic had dropped out of view.

Each input row is one passage: `id`, volume metadata, the `terms` that matched, and `text` (about 1000 characters of
OCR). Code what the passage says about **the people the matched terms refer to**.

## Output

Write one TSV row per input passage (never skip a passage), with a header line and these columns:

`id	referent	order	attitude	practice	yoga_link	armed	tags	page	quote	note`

- **referent**: use one code:

  | code | use when the term refers to … |
  |---|---|
  | RENUNCIANT | celibate renunciants, an ascetic order, its monasteries (maṭh, akhāṛā, asthal), mahants and disciples, initiation |
  | HOUSEHOLDER | married members living as a hereditary caste (Gharbari Gosains, Atiths, Bairagis with families, "Sannyasi" castes of Orissa and Midnapore), traders, money-lenders, landholders, cultivators |
  | VAISHNAVA_GURU | "Gosain/Goswami" as a hereditary Vaiṣṇava teacher or temple-owner lineage (Vallabha Maharajas, Chaitanya Goswamis of Bengal and Brindaban, Assamese sattra Gosains) |
  | CENSUS_CATEGORY | a census or caste heading, a population figure, a list of groups classed under it |
  | SAINT_SHRINE | a named holy man, a legend about one, or his tomb, shrine or samādhi |
  | NAME | the term is only part of a personal or place name, and the passage says nothing about these people |
  | OTHER | an unrelated sense |
  | JUNK | OCR garbage, an index or a table line with no readable statement |

- **order**: the order or tradition as the passage states or makes plain:
  - `dasnami`: Śaiva sannyāsīs of Śaṅkara's ten names, Giri, Puri, Bharati, Dandi, Paramahansa, Atit;
  - `bairagi`: Vaiṣṇava renunciants, Rāmānandī, Nimbārkī, Rāmānujī, Vallabha ascetics;
  - `vaishnava_gosain`: hereditary Vaiṣṇava gurus;
  - `naga`: naked or armed Nāgās of any order;
  - `mixed`;
  - `unclear`.
- **attitude**: the writer's own stance: `neg`, `neu`, `pos` or `mixed`. Reported opinions are `neu` unless the
  writer adds his own judgement.
- **practice**: `yes` if the passage describes a bodily or contemplative practice (meditation, austerities, postures,
  fasting, nakedness and ashes, sitting among fires, a raised arm, burial in a seated posture, samādhi), otherwise `no`.
  Describe it in `note`.
- **yoga_link**: `yes` if the passage connects these people with yoga, yogis or Jogis: calls them yogis, says they
  practise yoga, or groups them with Jogis. Otherwise `no`.
- **armed**:
  - `none`;
  - `past`: armed or fighting ascetics described as history ("formerly", events before about 1850);
  - `present`: described as a current fact at the time of writing.
- **tags**: comma-separated, possibly empty, from:
  - fraud, crime, low_status, beggar, performer, magic, healing, austerity, meditation, burial, learning, sanctity,
    order, householder, political, numbers, reform, western, health, land;
  - `trade`: trading, money-lending, banking.
- **page**: the printed page number if visible in the passage; otherwise empty. Never guess.
- **quote**: the shortest verbatim span (8–40 words) from `text` that supports your referent code, or the practice,
  yoga link or armed code if one of those is the point. Copy it exactly as it stands in the OCR, errors included. Use …
  only between two verbatim pieces. Leave it empty for NAME, OTHER and JUNK. No double-quote characters: stop a quote
  before one.
- **note**: optional, at most 20 words.

## Rules

- When a passage covers several orders, code the dominant one. Put anything notable about the others in `note`.
- Be literal. Do not import what you know about Daśanāmīs, Rāmānandīs or Nāgās into a passage that does not say it.
