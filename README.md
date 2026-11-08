# Gazetteer studies

Two studies of religious life in the British Indian district gazetteers, caste glossaries and census reports
(1866–1918), followed into the revised state gazetteers after independence (1954–1989).

| folder | question | start here |
|---|---|---|
| `gazetteer-vedanta/` | How widespread was allegiance to Śaṅkara's lineages, region by region, and did the picture change? | `gazetteer-vedanta/README.md`, `SYNTHESIS.md` |
| `yoga-gazetteers/` | What did "yoga", "yogi" and "Jogi" mean to the officials who wrote the gazetteers, and did that change after independence? | `yoga-gazetteers/README.md`, `SYNTHESIS.html` |

The two studies share their sources and refer to each other (`../gazetteer-vedanta/`, `../yoga-gazetteers/`).

## What is not included

The colonial sources are public domain. The post-independence revised gazetteers may still be in copyright, so the
raw text layers that carry long extracts from them are left out:
- `gazetteer-vedanta/revised/results/packets/`;
- `gazetteer-vedanta/mathas/results/hits.tsv` and `hits_dedup.tsv`;
- `gazetteer-vedanta/sringeri/results/hits.tsv`;
- `yoga-gazetteers/data/*passages.tsv`, `data/*batches/` and `results/kwic.tsv`.

The coded results, with their short quotations, are included. The downloaded OCR was never part of the repository.
Each study's README says which script fetches it from the Internet Archive and which rebuilds the left-out files.
The references to those files in the study READMEs are kept as they are.

## Licence

CC BY 4.0 for the reports, notes and coded data; MIT for the scripts. See `LICENSE.md`. Quotations from the sources
remain under the terms of those sources.
