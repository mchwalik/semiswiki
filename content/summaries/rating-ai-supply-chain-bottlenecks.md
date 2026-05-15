---
title: "Rating AI supply chain bottlenecks"
created: 2026-05-15
updated: 2026-05-15
type: summary
tags: [ai-infrastructure, semiconductors, photonics, power, supply-chain, thesis]
sources: [raw/articles/rating-ai-supply-chain-bottlenecks-irrational-analysis-interview.md]
confidence: medium
contested: false
contradictions: []
---

## Summary
This interview with Irrational Analysis is a cross-stack bottleneck map for AI infrastructure. Its main claim is that the tightest constraints have shifted toward indium-phosphide lasers and processing, DRAM/HBM capacity, and still-tight logic/CPU supply, while power semiconductors are not the immediate bottleneck but may become the next major upside area because idle EV-linked capacity can be repurposed for AI power conversion.

## What it adds to the wiki
- Sharpens [[photonics-cpo-supply-chain]] by arguing that the real pain point is not generic optics demand but the indium-phosphide laser chain, especially as CPO and 1.6T ramp.
- Adds a more explicit second-leg to [[ai-power-supply-chain-inheritance]]: solid-state transformers and grid-side load regulation outside the data center may matter as much as rack-internal power hardware.
- Gives a much richer explanation of why [[taalas]] is technically interesting even if the fixed-weight premise remains commercially uncertain.
- Pushes back on the idea that [[advanced-packaging]] is the single dominant bottleneck right now, arguing that Intel capacity and EMIB progress make optics and memory look tighter on a relative basis.

## Key takeaways
- Preferred alternative-inference names in the interview are Positron and Cerebras, with MatX viewed as underdisclosed and [[taalas]] treated as a clever but premise-dependent outlier.
- The most acute optics constraint is framed as indium-phosphide processing and laser capacity, with [[lumentum]] and [[aixtron]] highlighted as practical ways to express that view.
- The interview also points toward a fuller InP chain spanning [[coherent]], [[iqe]], [[axt]], [[sumitomo-electric]], and [[tower-semiconductor]].
- Memory remains structurally tight because DRAM/HBM capacity is concentrated in only three vendors and cannot be trivially reallocated from logic fabs.
- Power semis are framed as the next likely squeeze: not scarce yet, but potentially re-rated as AI load volatility pushes spending toward SiC, GaN, and eventually solid-state-transformer architectures.
- CPU and logic-fab tightness still matters, but the interview suggests that bottleneck severity has worsened more in optics and memory than in packaging over the last six months.

## Related pages
- [[photonics-cpo-supply-chain]]
- [[ai-power-supply-chain-inheritance]]
- [[advanced-packaging]]
- [[taalas]]
- [[lumentum]]
- [[aixtron]]
- [[coherent]]
- [[iqe]]
- [[axt]]
- [[sumitomo-electric]]
- [[tower-semiconductor]]
