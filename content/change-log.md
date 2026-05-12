---
title: Change Log
publish: true
---

# Change Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-05-12] create | Wiki initialized
- Domain: AI infrastructure and agentic investment research
- Structure created with SCHEMA.md, index.md, log.md

## [2026-05-12] ingest | Initial batch of 3 research memos
- Raw sources created:
  - raw/articles/semis-memo-supply-chain.md
  - raw/articles/let-there-be-light.md
  - raw/articles/agentic-utilities.md
- Wiki pages created:
  - concepts/ai-power-supply-chain-inheritance.md
  - concepts/photonics-cpo-supply-chain.md
  - concepts/agentic-utilities.md
  - entities/nvidia.md
  - entities/ciena.md
  - entities/cloudflare.md
  - entities/himax.md

## [2026-05-12] ingest | Added supplemental source: 26 Trades for 2026
- Raw source created:
  - raw/articles/26-trades-for-2026.md
- Wiki pages created:
  - summaries/26-trades-for-2026.md
- Notes:
  - Source is primarily meta/contextual and did not introduce a new core entity or concept page on its own.

## [2026-05-12] ingest | Added full PDF-to-Markdown extract for 26 Trades for 2026
- Raw source created:
  - raw/articles/26-trades-for-2026-pdf-extract.md
- Wiki pages created:
  - concepts/inference-on-device.md
  - concepts/advanced-packaging.md
  - concepts/ai-materials.md
- Wiki pages updated:
  - summaries/26-trades-for-2026.md
  - index.md
- Notes:
  - Converted only the most durable AI-infrastructure-adjacent sections into dedicated pages.
  - Much of the broader macro/policy/consumer content remains available in the raw extract but outside the wiki's core scope.

## [2026-05-12] expand | Full pass over all sources to date
- Schema updated:
  - SCHEMA.md domain broadened from AI-infrastructure-only to full public-equity thematic research coverage
- Wiki pages created:
  - 32 new section summary pages under summaries/ covering the remaining numbered trades from 26 Trades for 2026
- Wiki pages updated:
  - index.md regenerated from current page set
- Notes:
  - The wiki now covers AI, semis, policy, macro, consumer, biotech, EM, media, autonomy, and pair-trade sections from the full PDF extract.
  - Total tracked pages increased to 43.

## [2026-05-12] enrich | Added recurring company/entity layer across sources
- Wiki pages created:
  - entities/lumentum.md
  - entities/applied-optoelectronics.md
  - entities/aixtron.md
  - entities/veeco.md
  - entities/axcelis-technologies.md
  - entities/wolfspeed.md
  - entities/sims.md
  - entities/molina-healthcare.md
  - entities/nerdwallet-company.md
  - entities/acm-research-company.md
  - entities/synopsys-company.md
  - entities/wpp.md
- Wiki pages updated:
  - concepts/photonics-cpo-supply-chain.md
  - concepts/ai-power-supply-chain-inheritance.md
  - summaries/synopsys.md
  - summaries/acm-research.md
  - summaries/nerdwallet.md
  - summaries/conditional-on-gop-losing.md
  - summaries/wpp-not-dead-yet.md
  - summaries/all-chips-go-to-heaven.md
  - summaries/midterm-media-spend.md
  - summaries/insurance-marketing.md
  - summaries/china-trades.md
  - summaries/bullshit-jobs.md
  - index.md
- Notes:
  - Added a reusable entity layer for recurring names that appeared across optics, power, policy, and single-name thesis pages.
  - Verified that all current wikilinks resolve successfully; total tracked pages increased to 55.

## [2026-05-12] setup | Obsidian vault and public-site publishing scaffold
- Vault config added:
  - .obsidian/templates.json
  - .obsidian/daily-notes.json
  - .obsidian/community-plugins.json
  - .obsidian/app.json updated
  - .obsidian/core-plugins.json updated
- Vault support files added:
  - PUBLISHING.md
  - publish.css
  - templates/entity-template.md
  - templates/concept-template.md
  - templates/summary-template.md
  - templates/comparison-template.md
  - templates/query-template.md
  - templates/daily-note-template.md
  - templates/README.md
- Public site scaffold added outside the vault:
  - /opt/data/wiki-site
  - /opt/data/wiki-site/scripts/sync-vault.py
  - /opt/data/wiki-site/.github/workflows/deploy.yml
- Notes:
  - Configured Quartz-based public site generation from the vault while excluding raw research archives from public output.
  - Verified a successful Quartz build to /opt/data/wiki-site/public.
  - Fixed YAML quoting in summaries/wpp-not-dead-yet.md so static-site parsing succeeds.

## [2026-05-12] enrich | Promoted 26 Trades themes into concepts and expanded entity coverage
- Wiki pages created:
  - entities/jumia-company.md
  - entities/boeing-company.md
  - entities/airbus-company.md
  - entities/microstrategy-company.md
  - entities/oppenheimer-holdings.md
  - entities/raiffeisen-bank-international.md
  - entities/thyssenkrupp-marine-systems.md
  - entities/dave-inc.md
  - entities/lendingtree.md
  - entities/mediaalpha.md
  - entities/quinstreet.md
  - entities/everquote.md
  - entities/cadence.md
  - entities/ansys.md
  - entities/applied-materials.md
  - entities/amkor.md
  - entities/broadcom.md
  - entities/advanced-micro-devices.md
  - entities/bhp-group.md
  - entities/freeport-mcmoran.md
  - entities/southern-copper.md
  - entities/antofagasta.md
- Wiki pages moved/retagged:
  - summaries/bullshit-jobs.md -> concepts/bullshit-jobs.md (type: concept)
  - summaries/post-traumatic-supply-disorder.md -> concepts/post-traumatic-supply-disorder.md (type: concept)
  - summaries/all-chips-go-to-heaven.md -> concepts/all-chips-go-to-heaven.md (type: concept)
  - summaries/china-trades.md -> concepts/china-trades.md (type: concept)
  - summaries/gop-loses-the-house.md -> concepts/gop-loses-the-house.md (type: concept)
  - summaries/midterm-media-spend.md -> concepts/midterm-media-spend.md (type: concept)
  - summaries/bread-and-circuses.md -> concepts/bread-and-circuses.md (type: concept)
  - summaries/earned-wage-access.md -> concepts/earned-wage-access.md (type: concept)
  - summaries/insurance-marketing.md -> concepts/insurance-marketing.md (type: concept)
  - summaries/rate-sensitive-regional-banks.md -> concepts/rate-sensitive-regional-banks.md (type: concept)
  - summaries/shipbuilding.md -> concepts/shipbuilding.md (type: concept)
  - summaries/geopolitical-special-situations.md -> concepts/geopolitical-special-situations.md (type: concept)
  - summaries/slop-bowl-economics.md -> concepts/slop-bowl-economics.md (type: concept)
  - summaries/next-gen-autonomous.md -> concepts/next-gen-autonomous.md (type: concept)
  - summaries/kicking-the-tires.md -> concepts/kicking-the-tires.md (type: concept)
  - summaries/fat-redistribution.md -> concepts/fat-redistribution.md (type: concept)
  - summaries/oncologys-copy-paste-era.md -> concepts/oncologys-copy-paste-era.md (type: concept)
  - summaries/the-girlfriend-index.md -> concepts/the-girlfriend-index.md (type: concept)
  - summaries/orbital-manufacturing.md -> concepts/orbital-manufacturing.md (type: concept)
- Wiki pages updated:
  - summaries/jumia.md
  - summaries/long-boeing-short-airbus.md
  - summaries/saylors-bluff.md
  - concepts/rate-sensitive-regional-banks.md
  - concepts/geopolitical-special-situations.md
  - concepts/shipbuilding.md
  - concepts/earned-wage-access.md
  - concepts/insurance-marketing.md
  - summaries/synopsys.md
  - concepts/advanced-packaging.md
  - concepts/ai-materials.md
  - concepts/post-traumatic-supply-disorder.md
  - index.md
- Notes:
  - Reclassified broad thematic trade pages from 26 Trades for 2026 as concepts where they function as durable investment frameworks rather than one-off source summaries.
  - Added a larger entity layer for named public companies that serve as explicit expressions of those themes.
  - Total tracked pages increased to 77.
