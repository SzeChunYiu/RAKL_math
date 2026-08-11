# YM-E4b2a — source-binding audit for Appendix-D OS-form domination (D.5)

**Parent obstruction:** `YM-E4b2`, RAKL_math issue #133  
**Root:** RAKL_math issue #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Atom signature:** `YM-E4b2a-D5-SOURCE-BINDING-SAME-ALGEBRA-REGULATOR-LIMIT`  
**Current framework used:** `SzeChunYiu/RAKL@787c7e00af2a5877ccb715bc807ec14f52974e9c`, method `3.0.0`, package `0.1.0`  
**Application pre-action state:** branch commit `7978b1cb7e782eea87213a3f5b43c0dc143c2014`; main base `dc83b72201cb58844b2bdc76117e4dcb9190211d`  
**Pre-action receipt:** `YM-E4b2a-PRE-ACTION-20260811T174111Z`, sha256 `dd0730ee6f92a88b2efba83473f89ac32bb216e6d5815bc2a524d08df8015500`  
**Frozen fibre:** sha256 `de9667b809f78318ad2a852576e9f94091a5602cbfd5355d582421731619db17`  
**Authority:** `PROPOSAL_SHADOW / PROSPECTIVE_TEST_BOUND / SAME_CONTEXT_VERIFICATION_ONLY / NO_SOURCE_REPAIR_CERTIFICATE / ROOT_AUTHORITY_NONE`.

## 1. Discriminator

Appendix D of arXiv:2606.19362v1 introduces the common positive-time algebra `A+`, OS forms `Q_k`, the continuum form `Q_infty`, and the estimate

`sup_k Q_k(F,F) <= M Q_infty(F,F)` for all `F in A+`.  (D.5)

The parent atom established that this domination is exactly strong enough to force `N_infty subseteq N_k` and to give a uniformly bounded comparison map `J_k:H->H_k`. This cycle prospectively tested whether the current primary source actually derives (D.5), or an equivalent exact null-inclusion plus uniform-extension estimate, from earlier constructive estimates on the same objects.

## 2. Primary-source surfaces checked after the receipt

The full current arXiv v1 PDF was queried for the equation label, the two forms, null-space inclusion language, bounded-extension language, tightness/moment estimates, and regulator-equivalence estimates.

### 2.1 Continuum extraction gives pointwise form convergence and absolute moment bounds

Main §7.1, PDF pages 79–82, proves subsequential convergence of Schwinger functionals and OS inner products. The relevant estimates are uniform absolute Sobolev/moment bounds (for example equations (7.8), (7.9), (7.12)) followed by convergence of each fixed OS inner product (equations (7.15)–(7.16)). These statements control the size and convergence of the forms in a topology independent of the *degeneracy* of the limiting OS form.

They do not imply a relative estimate of the shape

`Q_k(F,F) <= M Q_infty(F,F)`.

The distinction is structural: the right side of (D.5) vanishes on the entire continuum null space, so (D.5) contains exact null-space information. A uniform absolute moment bound can remain positive on a continuum-null vector and therefore cannot by itself force `N_infty subseteq N_k`.

### 2.2 The main §7 OS-limit proof preserves positivity, not regulator null spaces

The source argues that reflection positivity passes to the limit because nonnegative finite-scale OS forms converge pointwise to a nonnegative limiting form. This correctly preserves positive semidefiniteness of the limit, but the implication is one-way: new null vectors may appear in a pointwise limit. The two-dimensional hostile family from `YM-E4b2` is an exact model of this possibility.

Thus the §7 limit construction does not, from the statements inspected, supply the missing exact finite-k null inclusion.

### 2.3 Appendix-D (D.5) is the unique located source surface with the required relative domination

The full-text query for `M Q_infty`, `Q_k(F,F) <=`, null-space inclusion variants, and bounded-extension language located the relative domination at Appendix D, PDF page 544. The text immediately before (D.5) says that two uniform estimates are imposed and attributes them to the constructive locality/clustering setting. It then uses (D.5) to bound `J_k`.

The immediately following representative-independence sentence instead reasons from `Q_k(F-G,F-G) -> 0` to consistency. That limit is insufficient for equality of quotient classes at a fixed `k`; (D.5) itself would repair the step because it gives exact zero whenever `Q_infty(F-G,F-G)=0`.

No earlier full-text hit was located that states or proves `N_infty subseteq N_k`, or an equivalent bounded comparison theorem on the continuum OS quotient, before Appendix D imposes (D.5).

This is a bounded source audit, not a universal impossibility claim about every rearrangement of the 593-page manuscript.

### 2.4 Additive regulator-equivalence estimates do not close the gap as stated

An earlier regulator-comparison estimate in the long-form material controls an absolute difference of OS forms by a locality-weighted regulator difference and then states equivalence under additional convergence. This is an additive comparison between regulator choices. It is not, in the inspected form, a multiplicative domination by the *limit* quadratic form `Q_infty`. In particular an additive error need not vanish on `N_infty`, so it does not automatically imply the exact null inclusion required by (D.5).

A valid route could still exist if that estimate were strengthened to an error bounded by `c_k Q_infty(F,F)` with `c_k` controlled, or if a separate exact identification of null spaces were proved. Neither such bridge was located in the inspected source surfaces.

## 3. Expert-cell review of the discriminator

These six passes share context and are not independent review.

- **Constructive QFT / OS reconstruction:** confirmed that §7 establishes a valid limiting PSD form but that positivity under weak/pointwise convergence does not preserve equality of null spaces in the direction needed for `J_k`.
- **Functional analysis / spectral convergence:** confirmed that (D.5) is a relative form-boundedness statement, strictly stronger than uniform absolute moment bounds and pointwise form convergence. It is sufficient for exact quotient descent and a uniform bounded extension.
- **Lattice gauge spectral theory:** kept the result upstream of transfer-gap interpretation. No finite-lattice gap can be transported through a comparison operator whose quotient-space definition remains source-unbound.
- **RG / continuum analysis:** checked scale/volume content. The inspected §7 bounds are uniform in scale/volume for observables, but the missing property is *relative-to-the-limit-form* domination on the same common algebra. Uniformity alone does not change that distinction.
- **Adversarial verifier:** reused the PSD family `Q_n=x^2+y^2/n`, which satisfies pointwise convergence and simple uniform absolute bounds while violating null inclusion. This directly falsifies the inference class that would turn those weaker hypotheses into (D.5).
- **RAKL v3 assurance / metrology:** this child was frozen after refreshing to the then-current RAKL main `787c7e00...`. The parent `YM-E4b2` receipt had pinned the immediately preceding RAKL commit because main advanced during the run; the one-commit delta touched inference/experience-benchmark/promotion surfaces, not the pre-action or mathematical-method contracts used for the parent, but the freshness miss is preserved as a meta-policy failure rather than silently ignored.

## 4. Outcome and exact residual

**Outcome:** `PARTIAL_SUCCESS_LOCAL_DIAGNOSIS__SOURCE_GLUING_BLOCKED`.

The source-facing obligation is now sharper:

1. derive (D.5) from a theorem actually proved earlier in the construction, with the exact common `A+`, embeddings, cutoff/regulator sequence, volume limit, and continuum subsequence; or
2. replace (D.5) with a proved exact `N_infty subseteq N_k` statement plus a regulator-uniform bounded comparison-map estimate;
3. only then use the Appendix-D strong-semigroup/resolvent argument, after separately repairing the OS time-translation/isometry issue tracked in #126;
4. only after that test fixed-physical-time `INT`/`UGAP`, physical spectral identification, source-family completeness, RG trajectory and remaining continuum/root obligations.

The local failure is not a proof that (D.5) is false. It is a **source/gluing verification gap**: the current primary manuscript, on the bounded surfaces checked in this cycle, uses the needed domination as an imposed estimate rather than supplying a located derivation from the earlier weaker bounds.

## 5. Source-verification and tooling status

Primary-source text was read directly from arXiv:2606.19362v1 with exact page/line selectors. The mandated PDF screenshot surface was invoked after the pre-action freeze for both the §7 moment-bound page and the Appendix-D page; the backend returned cache-miss failures. Therefore image-level page verification is `CANNOT_CHECK` for this run. Parsed-text verification remains available but is not silently upgraded to screenshot verification.

No numerics were used as proof. No independent mathematical review, formal verifier, dependency/axiom audit, or root review gate was completed.

## 6. Novelty/saturation disposition

The child diagnosis is a **representation/transfer-interface** refinement, not a new Yang–Mills theorem. It links the abstract quotient-descent criterion to the exact source hypothesis (D.5) and separates that hypothesis from the weaker source estimates that were actually located. Protected retained semantic novelty remains zero on all RAKL metrology axes because no lesson/tool/obstruction/theorem was promoted through a protected gate.

Operationally, `KNOWLEDGE`, `OBSTRUCTION`, `RELATION`, `PATH`, and `META_METHOD` were reopened for search by the new source binding and framework-freshness evidence; `OPERATOR` remains flat and `EXPERIENCE_PATTERN` is reused rather than promoted.

The next atomic action is to trace the claimed provenance of (D.5) into the exact earlier locality/clustering/RG lemmas and attempt a line-by-line derivation with constants and null-space quantifiers. Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.
