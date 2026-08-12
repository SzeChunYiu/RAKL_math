# NS-B1a3a-C001 — finite-I expanding-ball backward-L3 extractor and far-tail reduction

**Authority:** `PROPOSAL_SHADOW / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`  
**Framework:** RAKL v3.0.0 @ `43897d3afaf0038385102d5acc64793c05ec40f0`

## Exact atom

Let `(v,q)` be the non-trivial mild bounded ancient Navier–Stokes solution supplied by the Albritton–Barker Type-I equivalence, and write `M = I(v,q) < infinity`. The consumer to be matched is Albritton–Barker Theorem 1.2: a mild ancient solution with `sup_k ||v(t_k)||_{L^3(R^3)} < infinity` along some `t_k -> -infinity` is identically zero.

The active question is narrower than the previous `NS-B1a3` global-critical-tightness obligation:

> What part of the backward global-L3 consumer signature is forced directly by the `C` summand of finite `I`, before any global compactness, profile decomposition, pressure argument, or unique continuation is invoked?

## Source-bound lemma

For `R>0`, take the parabolic cylinder `Q(0,2R)=B_{2R} x (-4R^2,0)`. Since
`C(Q(0,2R))=(2R)^(-2) ∫_{-4R^2}^0 ∫_{B_{2R}} |v|^3 <= M`,
we have

`∫_{-4R^2}^0 ∫_{B_{2R}} |v|^3 <= 4 M R^2`.                                    (1)

Restrict to `J_R=(-4R^2,-R^2)`, whose length is `3R^2`. Define

`G_R = { t in J_R : ∫_{B_{2R}} |v(x,t)|^3 dx <= 8M/3 }`.

By Chebyshev/Markov applied to (1), the bad-time set has measure at most

`(4MR^2)/(8M/3) = (3/2)R^2`.

Therefore

`|G_R| >= (3/2)R^2`.                                                            (2)

In particular, for every `R>0` there exists an a.e.-good `t_R in J_R` satisfying

`||v(t_R)||_{L^3(B_{2R})} <= (8M/3)^(1/3)`.                                     (3)

For any sequence `R_n -> infinity`, every choice `t_n in G_{R_n}` obeys `t_n <= -R_n^2 -> -infinity`. Thus finite `I` already supplies a positive-measure reservoir of backward times with a uniform `L^3` bound on an expanding spatial ball.

No pressure estimate, compactness limit, derivative estimate, global critical topology, or numerics enters this lemma.

## Exact gluing interface

Theorem 1.2 still requires the **global** norm at those same times. Hence it is sufficient to prove, for some `R_n -> infinity` and some choices `t_n in G_{R_n}`,

`sup_n ∫_{R^3 \ B_{2R_n}} |v(x,t_n)|^3 dx < infinity`.                           (TAIL)

Then (3)+(TAIL) gives `sup_n ||v(t_n)||_{L^3(R^3)}<infinity`, so Theorem 1.2 yields `v=0`. That contradicts the non-trivial ancient solution attached to a Type-I singularity.

The new residual is therefore **same-time far-tail boundedness on the automatically generated good-time reservoir**, not a full global-critical precompactness certificate. Tightness/vanishing of the tail would be stronger than necessary for this consumer.

A useful density-gluing formulation follows from (2): any independently proved tail-good subset `H_R subset J_R` with `|H_R| > (3/2)R^2` must intersect `G_R`. A future tail mechanism may therefore target temporal density rather than a predetermined time sequence.

## Adversarial audit

This does **not** prove (TAIL). Existing translation/profile-leakage experience remains a valid topological falsifier: local/expanding-ball control by itself cannot prevent critical mass from living farther away at the same time. Nor does summing local `C` bounds over translated balls help: the definition of `I` controls each cylinder separately and supplies no summability over infinitely many spatial centers.

The pressure is absent from the extractor, but a proposed PDE mechanism for (TAIL) must separately audit pressure localization and far-field harmonic/nonlocal effects. Backward uniqueness is not used. Self-similar stationary-Leray rigidity is not used, so there is no equation-change transfer here. Type-II scenarios are outside this atom because `I<infinity` is the producer premise.

## Limit-passage audit

No new limit passage occurs in this lemma. The prior Albritton–Barker producer remains the exact source of the mild bounded ancient state. Consequently there is no weak-to-strong upgrade hidden here. The only gluing step left is spatial: an expanding-ball core bound and a same-time far-tail bound must be joined in the same ancient solution and at the same selected times.

## Same-context expert cell

Five roles reviewed the derivation: (E1) blow-up/compactness analyst checked the Type-I ancient producer and scaling; (E2) critical-space analyst checked the exact Theorem-1.2 consumer; (E3) local-energy analyst checked the cylinder normalization, slab length, and Chebyshev constants; (E4) pressure/far-field analyst verified that pressure is not needed for the extractor and identified where it can re-enter a tail proof; (E5) adversarial gluing reviewer checked time quantifiers, expanding radii, noncompact-symmetry leakage, and prohibited the missing global inference.

Consensus: the extractor and positive-measure good-time reservoir are valid source-bound consequences of finite `I`. Dissent/limit: none of the five roles can certify (TAIL), and all five are same-context reviews, not independent mathematical reviews.

## Outcome

`PARTIAL_SUCCESS / COMPOSITIONAL_INTERFACE_REDUCTION`.

Residual before: `finite I -> unknown global critical tightness/backward-global-L3 interface`.

Residual after: `finite I -> positive-measure backward expanding-ball L3 reservoir`, with one explicit local-to-global residual: `O-NS-B1a3a-SAME-TIME-FAR-L3-TAIL`.

Novelty class, conservatively: `COMPOSITIONAL` (the `C`-bound, time-slab averaging, and an existing Liouville consumer are composed; no new theorem is claimed beyond the proved intermediate lemma).

Root remains open. There is no Type-I exclusion, Type-II classification, root certificate, formal proof certificate, novelty certificate, or isolated review.

## Primary-source provenance

Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502, current arXiv rendering checked 2026-08-12: equations (1.2), (1.5), Theorems 1.1 and 1.2.
