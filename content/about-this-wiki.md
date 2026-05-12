---
title: About This Wiki
publish: true
---

# About This Wiki

## Domain
This wiki tracks public-equity research across AI infrastructure, semiconductor supply chains, photonics/optics, agentic internet infrastructure, macro/policy trades, global thematic baskets, and related single-name theses from research memos.

## Conventions
- File names: lowercase, hyphens, no spaces
- Every wiki page starts with YAML frontmatter
- Use [[wikilinks]] between pages; minimum 2 outbound links per page
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md`
- Every action must be appended to `log.md`
- Raw sources in `raw/` are immutable
- Use concise investor-oriented summaries, not full transcript rewrites

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true | false
contradictions: [other-page-slug]
---
```

## Tag Taxonomy
- ai-infrastructure
- semiconductors
- photonics
- optics
- networking
- data-centers
- power
- agentic
- payments
- security
- observability
- cloud
- public-equities
- supply-chain
- company
- thesis
- basket

## Page Thresholds
- Create a page when a concept is central to one source or appears across multiple sources
- Prefer updating existing pages over creating duplicates
- Split pages over ~200 lines
- Avoid pages for passing mentions only

## Entity Pages
Use for notable companies or platforms with recurring relevance across memos.

## Concept Pages
Use for durable themes, architectures, and investment frameworks.

## Update Policy
When sources conflict:
1. Preserve both claims with dates and sources
2. Prefer newer dated evidence
3. Mark `contested: true` when unresolved
4. Flag in future lint reports
