# YM-E4b2b — ordinary tightness + perfect clustering do not imply Appendix-D OS-form domination

**Parent:** `YM-E4b2`, RAKL_math issue #133  
**Prospective control:** `YM-E4b2b`, issue #138  
**Root:** RAKL_math issue #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Atom signature:** `YM-E4b2b-D5-TIGHTNESS-CLUSTERING-IMPLICATION-DISCRIMINATOR`  
**Framework frozen for this discriminator:** `SzeChunYiu/RAKL@812e9cf18345ef430f0a4cc3ff78f93d7f18ed22`, method `3.0.0`, package `0.1.0`  
**Application base:** `SzeChunYiu/RAKL_math@812addd25a7f34d3c6272143e21d5d7db34539aa`  
**Pre-action receipt:** `YM-E4b2b-PRE-ACTION-20260811T180732Z`, canonical sha256 `1eed5f083fa5be599f38277d1f116cc9065bbcc808deb02801cbf25b046b3231`  
**Authority:** `PROPOSAL_SHADOW / EXACT_ABSTRACT_COUNTERMODEL / SOURCE_ROUTE_DIAGNOSTIC / SAME_CONTEXT_REVIEW_ONLY / NO_SOURCE_REPAIR_CERTIFICATE / NO_ROOT_AUTHORITY`.

## 1. Frozen question and chronology boundary

The exact prospective discriminator was frozen before its verification:

> Does reflection positivity on one common positive-time algebra, tightness/weak convergence, pointwise convergence of the associated OS forms, and one regulator-uniform exponential clustering rate imply a regulator-uniform relative estimate
>
> `Q_k(F,F) <= M Q_infty(F,F)` for every source `F`?

The prior observation that Faizal–Shabir Appendix D imposes this estimate as (D.5), while the inspected Section 7 surfaces supply absolute moment/tightness estimates and pointwise OS-form convergence, is retrospective motivation inherited from draft PR #135. The hostile-model *idea* was also available before the receipt. Prospective credit here is therefore limited to the exact post-receipt verification of the declared discriminator and its scoped consequence.

## 2. Primary-source interface being tested

Primary source: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1, 9 June 2026, https://arxiv.org/abs/2606.19362.

The primary PDF was rechecked after the receipt.

- Section 7.1, equations (7.12)–(7.16), gives scale-uniform **absolute** moment estimates, weak/subsequential convergence of Schwinger functionals, and pointwise convergence of OS inner products.
- Section 7.2 states scale-uniform exponential clustering for separated observables and passes that property to the limit.
- Appendix D, page 544, first assumes weak convergence of reflection-positive measures and then separately says: “We impose two uniform estimates.” The first is (D.5),
  `sup_k Q_k(F,F) <= M Q_infty(F,F)`.
  The second, (D.6), is the uniform time-decay estimate. The text calls (D.5) “a quantitative form of tightness of the OS forms.”

The discriminator asks whether *ordinary measure tightness/weak convergence plus even perfect clustering* is logically sufficient for the relative quadratic-form domination in (D.5). This is narrower than asking whether the manuscript may prove (D.5) from additional Yang–Mills-specific structure elsewhere.

Mandatory PDF image verification was attempted on the relevant Appendix-D and Section-7 pages. The web PDF screenshot backend returned `Cache miss` on both attempts. Exact parsed-text page/equation selectors were available; screenshot verification remains `CANNOT_CHECK` and is a tooling/verification limitation, not mathematical evidence.

## 3. Exact reflection-positive countermodel

Let

`Omega = ({0,1} x {0,1})^(Z^4)`.

Write the two coordinates at a lattice site `x` as `(Y_x,Z_x)`. For `0 < epsilon < 1`, let `mu_epsilon` be the translation-invariant product probability measure under which

- `Y_x ~ Bernoulli(1/2)`,
- `Z_x ~ Bernoulli(epsilon)`,

independently over sites and between the two fields. Let `mu_0` be the product measure with the same nontrivial `Y` field and `Z_x=0` almost surely. Thus the limiting probability system remains nontrivial.

Reflect Euclidean time in the mid-plane by

`theta(t,mathbf{x}) = (1-t,mathbf{x})`.

Let `A_+` be the bounded cylinder algebra depending only on sites with `t >= 1`. For the complexified algebra use the standard anti-linear reflected involution

`(Theta F)(omega) = conjugate(F(theta omega))`.

This is the convention compatible with a sesquilinear OS form; on the real cylinder algebra the conjugation is immaterial.

Define

`Q_epsilon(F,G) = E_mu_epsilon[(Theta F) G]`.

### Reflection positivity

The positive-time and reflected nonpositive-time sigma-algebras are independent under each product measure and have the same law. Hence, for every `F in A_+`,

`Q_epsilon(F,F)
 = E[conjugate(F o theta) F]
 = conjugate(E[F]) E[F]
 = |E[F]|^2 >= 0`.

More generally,
`Q_epsilon(F,G)=conjugate(E[F]) E[G]`,
so every finite OS Gram matrix is rank-one positive semidefinite. The same holds for `mu_0`.

Thus this is a genuine reflection-positive common-algebra family, not merely an abstract family of PSD forms.

### Tightness and weak convergence

`Omega` is compact metrizable because `Z^4` is countable and each site space is finite. Therefore the family is uniformly tight.

If `epsilon_k -> 0`, then every finite-site marginal of `mu_epsilon_k` converges to the corresponding marginal of `mu_0`. Cylinder functions are convergence determining on this compact product space, so

`mu_epsilon_k => mu_0`.

Consequently, for every bounded cylinder `F,G`,

`Q_epsilon_k(F,G) -> Q_0(F,G)`.

This gives the requested pointwise OS-form convergence.

### Uniform exponential clustering

If bounded local cylinder observables `A` and `B` have disjoint supports, product independence gives

`Cov_mu_epsilon(A,B)=0`

for every `epsilon`, including `epsilon=0`. Hence every ordinary separated-support exponential-clustering estimate

`|Cov(A,B)| <= C(A,B) exp(-m dist(supp A,supp B))`

holds uniformly in `epsilon` for any chosen `m>0` (indeed with zero left-hand side whenever the supports are disjoint).

Thus the family has stronger mixing than the hypothesis being tested: separated local observables are exactly independent.

### Failure of relative OS domination

Choose a positive-time site `x_+=(1,0,0,0)` and let

`F(omega) = Z_{x_+}`.

Then

`E_mu_epsilon[F] = epsilon`,
so
`Q_epsilon(F,F)=epsilon^2 > 0`.

But under `mu_0`, `F=0` almost surely, hence

`Q_0(F,F)=0`.

Therefore no finite constant `M` can satisfy

`Q_epsilon(F,F) <= M Q_0(F,F)`

for even one `epsilon>0`, and a fortiori no regulator-uniform `M` can satisfy the Appendix-D form of (D.5).

For exact arithmetic calibration only, `epsilon=1/2,1/3,1/5,1/10` gives OS norms squared `1/4,1/9,1/25,1/100`, while the limit norm is exactly zero. The calculation is not used as proof.

## 4. Diagnosis

The generic implication is **false**.

Ordinary measure tightness, weak convergence, pointwise convergence of OS forms, reflection positivity, and even exact independence at separated supports do not control *how null spaces change in the limit*. A source can have positive regulated OS norm at every cutoff while becoming exactly null in the limiting OS form.

The missing logical type is therefore not “more clustering” or “more ordinary tightness.” Before defining comparison maps on quotient Hilbert spaces, one needs an exact **relative OS-form control** strong enough to preserve continuum null vectors at the regulated levels. The already-registered parent obstruction #133 states the precise local requirements:

- quotient descent: `N_infty subseteq N_k` (or the appropriate representative-map version);
- bounded extension: a bound of the form `Q_k(F,F) <= C_k^2 Q_infty(F,F)`;
- for the source's uniform varying-space argument, a regulator-uniform bound on the comparison operators.

Equation (D.5) has exactly this relative strength. The present countermodel only proves that the ordinary compactness/clustering package cannot supply that strength *as a generic theorem*.

## 5. What this does and does not say about the Yang–Mills source

This is a **source-route diagnostic**, not a counterexample to Yang–Mills and not a proof that arXiv:2606.19362v1 cannot establish (D.5).

The countermodel is deliberately not a gauge theory. Its role is to falsify the generic inference from the properties explicitly named in the Appendix-D sentence and in Section 7. A Yang–Mills-specific derivation can still succeed if it uses additional structure—for example an exact regulator comparison theorem, a direct relative estimate for the reflected quadratic forms, or an equivalent exact null-inclusion plus uniform bounded-extension theorem on the same `A_+`.

Accordingly, the next source-facing discriminator is sharper than in PR #135:

**Trace the claim that (D.5) is satisfied in the constructive setting to a theorem whose conclusion is genuinely relative to `Q_infty`, rather than another absolute moment/tightness/clustering bound. If no such theorem is present, isolate the first missing regulator-comparison estimate.**

Only after that can the program safely compose the comparison maps with the corrected OS contraction semigroup (#126), fixed-physical-time intertwining/uniform physical contraction (draft PR #130), source-family completeness (#109 / PR #62), and the remaining RG/continuum obligations.

## 6. Same-context expert cell

These are role-separated checks performed in one shared context. They provide **zero independent-review credit**.

1. **Constructive QFT / OS reconstruction.** Verified the reflection algebra, positive-time/reflected-half independence, the rank-one positive OS Gram form, and the null-space consequence. Verdict: the countermodel is genuinely reflection positive, and its failure mode is exactly quotient/null compatibility.
2. **Probability / mixing.** Verified compact-product tightness, convergence of finite marginals/cylinder expectations, and exact independence of separated local observables. Verdict: the model has stronger-than-exponential clustering uniformly in the regulator.
3. **Functional analysis / varying Hilbert spaces.** Checked that pointwise convergence of positive forms permits enlargement of the limiting null space and does not imply a uniform relative form bound. Verdict: (D.5) is a bounded-comparison statement, not ordinary tightness.
4. **Lattice gauge / RG applicability.** Checked disanalogy. Verdict: the model falsifies only the generic implication; it gives no authority against a stronger gauge/RG-specific estimate and no continuum-Yang–Mills conclusion.
5. **Adversarial verification.** Required a nontrivial limit sector, genuine probability measures, a common algebra, an exact reflection-positive calculation, and exact clustering rather than a bare PSD example. Verdict: all declared antecedents survive; the D.5 conclusion fails.
6. **RAKL v3 assurance / metrology.** Verified the pre-action receipt precedes the exact discriminator execution, while preserving the retrospective status of the motivating source observation/model idea; separated episode -> diagnosis -> existing obstruction, with no new lesson/tool/motif promotion.

## 7. Local result versus local-to-global gluing

**Local mathematical result:** `PARTIAL_SUCCESS / GENERIC_IMPLICATION_FALSIFIED`. The abstract implication is exactly falsified.

**Same-theory Yang–Mills gluing:** `BLOCKED`. No source-bound theorem has yet been produced that derives (D.5), exact null inclusion, or equivalent bounded comparison from the actual RG/regulator construction on the same source algebra and continuum trajectory.

This failure is classified as **source/gluing/representation**, not a local Yang–Mills mathematical contradiction. The solved local subproblem is classified for RAKL routing as **compositional**: it composes the stored quotient-null obstruction with a stronger source-interface countermodel. This is not a novelty certificate.

## 8. Saturation and residual

The current v3 seven **method saturation** axes are kept distinct from the seven semantic-growth/metrology axes.

- `theory_route`: `FLATTENED` — no new Yang–Mills theory family was opened.
- `proof_route`: `REOPENED` — “ordinary tightness/clustering => D.5” is closed as a generic route; direct relative regulator comparison is the reopened proof route.
- `tool_route`: `FLATTENED` — no new mathematical tool is required by this local discriminator.
- `decomposition`: `REOPENED` — the former single “tightness” phrase is split into ordinary measure compactness versus relative OS-form domination.
- `local_expert_coverage`: `FLATTENED` — six same-context roles cover the current interface; this is not independent review.
- `analogue_coverage`: `REOPENED` — an exact reflection-positive/nontrivial-limit hostile analogue now covers the source-interface claim.
- `structural_novelty`: `FLATTENED` — the mechanism is a stronger realization of the already-known null-space obstruction, not a new protected structure.

No protected semantic novelty is retained in this proposal/shadow cycle. `KNOWLEDGE=0`, `OPERATOR=0`, `EXPERIENCE_PATTERN=0`, `OBSTRUCTION=0`, `RELATION=0`, `PATH=0`, `META_METHOD=0`.

Root issue #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`. There is no root statement closure, no closed proof DAG, no formal/verifier/dependency/axiom/barrier closure, no isolated recheck, no bounded novelty certificate, and no genuinely isolated mathematical review.
