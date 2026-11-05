# Coding instructions: yoga, yogis and Jogis in the gazetteers

You code passages from British Indian district gazetteers, caste glossaries and census reports (1866–1935), and from
the revised Indian state gazetteers (1954–1989). The study asks **what "yoga", "yogi" and "Jogi" meant to the
writers of these texts, and whether that changed over time and between regions.**

Each input row is one passage: `id`, volume metadata, the `terms` that matched, and `text` (about 1000 characters of
OCR, whitespace normalised). Code what the passage says about **the matched terms only**. Ignore the rest of the
passage.

## Output

Write one TSV row per input passage (never skip a passage), with a header line and these columns:

`id	sense	sense2	attitude	tags	page	quote	note`

- **sense**: the main sense of the matched term(s) in this passage. Use one code from the list below.
- **sense2**: a second sense if the passage clearly has one (e.g. CASTE + MENDICANT); else empty.
- **attitude**: the writer's own stance toward the yogi/Jogi/yoga, as the wording shows it. Use `neg`, `neu`,
  `pos` or `mixed`. Use `neu` when there is no evaluation. The writer's stance is not the stance of the people
  reported: "the people revere him" is `neu` unless the writer adds his own judgement.
- **tags**: a comma-separated list, possibly empty, from:
  - `fraud`: imposture, quackery, "pretends";
  - `crime`: theft, cheating, a criminal tribe, a dangerous wanderer;
  - `low_status`: low caste or degraded;
  - `beggar`: alms or begging;
  - `performer`: snake-charming, juggling, singing, showing animals, fortune-telling;
  - `magic`: sorcery, charms, spells, miracles, siddhis;
  - `healing`: medicines, cures;
  - `austerity`: penance, self-mortification, nakedness, ashes;
  - `meditation`: contemplation, trance, breath control, posture;
  - `burial`: burial instead of cremation, samādhi tomb, buried alive;
  - `learning`: textual, philosophical or Sanskrit learning;
  - `sanctity`: holiness, a saint, a revered founder;
  - `order`: a monastic order, its sects, initiation, ear-rings, gurus, monasteries;
  - `householder`: married, with a hereditary trade or land;
  - `weaver`: weaving as a trade;
  - `political`: rebellion, sedition, raids, armed ascetics;
  - `numbers`: census or population figures;
  - `reform`: modern reform or revival movements;
  - `western`: European or theosophical interest;
  - `health`: yoga as physical exercise or health.
- **page**: the printed page number if it is visible in the passage (a running header or folio near the hit).
  Otherwise leave it empty. Never guess.
- **quote**: the shortest verbatim span (8–40 words) from `text` that supports your sense code. Copy it exactly
  as it stands in the OCR, errors included, because a script will check it against the source. Use … only between two
  verbatim pieces. Leave it empty for NAME, ASTRO, OTHER and JUNK.
- **note**: optional, at most 20 words. Use it for anything notable, e.g. "equates jogi with fakir", "calls yoga
  'the Yoga philosophy'", "distinguishes true yogi from vagrant Jogi".

## Sense codes

| code | use when the term refers to … |
|---|---|
| PHIL | yoga as a philosophical system or darśana: Patañjali, Sāṅkhya-Yoga, the "Yoga school", subjects in a Sanskrit curriculum |
| DISCIPLINE | yoga as a contemplative or bodily discipline aimed at liberation or powers: meditation, postures, breath, trance, samādhi as a state, a person "practising yoga" |
| MODERN | modern yoga: Vivekananda, Aurobindo, yoga āśramas and institutes, yoga classes, yoga as health or physical culture, theosophical or Western interest |
| ASCETIC | yogi/Jogi as a member of an ascetic order or a renunciant holy man: Nāth/Kanphaṭa/Gorakhnāthī Jogīs, their monasteries (asthals, maṭhs), mahants, initiation, ear-rings |
| MENDICANT | yogi/Jogi as a wandering beggar, entertainer, snake-charmer, fortune-teller or itinerant seller, as a way of life (not a hereditary caste) |
| CASTE | Jogi/Jugi/Yogi as a hereditary caste or community of householders: endogamy, marriage, trade (weavers, cultivators, lime-burners …), census numbers, status claims (e.g. Jugis calling themselves "Yogi" or "Nath") |
| SAINT | a named yogi or Jogi saint, a legend about one, or his shrine or samādhi tomb |
| PRACTICE_OTHER | a "practice" term (samādhi, āsana, buried alive …) used for something other than yoga: a samādhi as a tomb of a non-yogi, voluntary burial, a seat or throne. Use SAINT if the person is a yogi. |
| NAME | the term is only part of a personal or place name and the passage says nothing about yogis or yoga |
| ASTRO | yoga as a calendrical or astronomical unit |
| OTHER | an unrelated sense (e.g. *hatha* as a wheat variety; "posture" in a non-yogic sense) |
| JUNK | OCR garbage, an index or a table line with no readable statement |

Rules:
- If one passage shows both an ascetic order and a hereditary caste, choose by what the sentence that contains the
  term is about. Put the other sense in sense2.
- "Fakir" is not a matched term, but note it when the passage equates yogis or Jogis with fakirs.
- A caste glossary article on "Jogi" often runs through several senses; code the passage's own sentences only.
- Be literal. Do not import what you know about Nāth Yogīs or modern yoga into a passage that does not say it.
