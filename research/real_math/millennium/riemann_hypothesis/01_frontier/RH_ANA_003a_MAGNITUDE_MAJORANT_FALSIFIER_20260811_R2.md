# RH-ANA-003a — magnitude-majorant transport falsifier (R2)

**Authority:** exact route-local algebra / source-bound representation diagnostic / same-context expert synthesis / proposal-shadow only / no RH theorem / no Li-sign theorem / no novelty claim / root authority none.

## Frozen atom and chronology

This result was generated only after materializing the R2 pre-candidate packet on branch `research/rh-ana003-prime-tail-v3-20260811`:

- context fibre `RH_ANA_003a_CONTEXT_FIBER_20260811_R2.json`, hash `sha256:867cb8e271decdfc186fe9a68e9a5e5cdd3c2ed9fb551d7e57e60d0227bbb34b`;
- dual-memory review `RH_ANA_003a_RESEARCH_MEMORY_REVIEW_20260811_R2.json`, hash `sha256:7925d40689c941f998d72e529f8eee41d81c5b864d53d5be306c399c285d30fe`;
- seven-event hash-chained pre-candidate trace ending at `RH-ANA-003a-E07`, hash `sha256:1dd04026b4825ee99899f56449472ff0a733983772bbbfe099fbf1c1573e46db`.

The executable `plan_math_research` gate from current RAKL could not be run through the connected GitHub execution surface, so this entire continuation remains proposal/shadow evidence even though chronology is externally commit-ordered.

## Primary-source binding

Mark W. Coffey, *Toward verification of the Riemann hypothesis: Application of the Li criterion*, arXiv:`math-ph/0505052`, Theorem 1, gives the exact representation

`lambda_n = - sum_{m=1}^n binom(n,m) eta_{m-1} + sum_{m=2}^n (-1)^m binom(n,m)(1-2^{-m}) zeta(m) + 1 - n( gamma + log(pi) + 2 log 2 )/2`.

The same source defines the `eta_k` by a renormalized von-Mangoldt limit and records

`zeta'(s)/zeta(s) = -(s-1)^{-1} - sum_{p>=0} eta_p (s-1)^p`.

It explicitly states that this Laurent/Taylor regular part has radius of convergence `3`, with the first encountered singularity at the trivial zero `s=-2`. Exact source: arXiv:`math-ph/0505052`, equations (10)-(12), pp. 5-6 of the PDF, accessed 2026-08-11.

A second primary source, Coffey, *The Stieltjes constants, their relation to the eta_j coefficients, and representation of the Hurwitz zeta function*, arXiv:`0706.0343`, reorganizes the crucial oscillatory Li subsum as `S_2(n)=S_gamma(n)+S_Lambda(n)` and proves `S_gamma(n)=O(n)`. This matters here only as evidence that cancellation-aware reorganization can change the scale of a component; it is not treated as an all-index positivity theorem.

A bounded current-literature search on 2026-08-11 also checked later Li-criterion representations, including Suzuki arXiv:`2301.05779`; no later source is used to overwrite the exact Coffey formula or to claim closure of the eta/binomial bridge.

## Exact discriminator 1 — Cauchy magnitude transport

Fix any `0 < r < 3` and write

`M_r = max_{|s-1|=r} | zeta'(s)/zeta(s) + 1/(s-1) |`.

Cauchy's coefficient estimate gives

`|eta_{m-1}| <= M_r r^{-(m-1)}`.

If these coefficientwise magnitudes are propagated to the Li transform by triangle inequality, then

`| sum_{m=1}^n binom(n,m) eta_{m-1} |`

`<= M_r sum_{m=1}^n binom(n,m) r^{-(m-1)}`

`= M_r r [ (1+1/r)^n - 1 ]`.

For every fixed `r<3`, this envelope is exponential in `n`. Therefore the local radius theorem plus coefficientwise Cauchy bounds, when transported **only by absolute majorization**, does not yield a polynomial/linear-sized mechanism for the root-facing all-index sign problem. This does not say the actual signed transform grows exponentially; it says the chosen transport forgets the cancellations that could prevent that growth.

## Exact discriminator 2 — nearest-singularity geometric calibration

The source identifies the nearest singularity scale as distance `3`. Test the signed geometric coefficient family

`a_{m-1} = (-1)^m / 3^m`, `m>=1`.

This is the coefficient pattern of a unit-residue simple-pole geometric contribution at that distance and is used only as a calibration of the transport, not as an assertion that `eta_{m-1}=a_{m-1}`.

The binomial theorem gives exactly

`sum_{m=1}^n binom(n,m) a_{m-1} = (2/3)^n - 1`,

which is bounded, whereas coefficientwise absolute values give

`sum_{m=1}^n binom(n,m) |a_{m-1}| = (4/3)^n - 1`,

which is exponential. The same coefficient magnitudes therefore support qualitatively different conclusions depending on whether signed correlation is preserved.

A private SymPy finite-sum calculation reproduced both identities and the general Cauchy-envelope identity. That computation is calibration only; the proof is the finite binomial theorem.

## Expert-cell synthesis

The analytic-number-theory lead accepted the exact Coffey representation and radius statement but rejected any inference from the radius alone to Li signs. The asymptotic/complex-analysis lead identified the exponential `M_r r[(1+1/r)^n-1]` envelope as the decisive loss caused by triangle inequality. The Li/positivity lead required the conclusion to remain strictly route-local: no eta-sign conjecture or RH-equivalent all-index condition may be smuggled in as a repair. The adversarial falsification lead selected the signed geometric calibration because it satisfies the same radius-scale magnitude pattern while making the exact/absolute transform gap explicit. The formal/verification lead checked the finite-sum identities separately from the source theorem. The RAKL v3 provenance/metrology lead classified the result as shadow representation/bridge pruning only; these six passes are same-context roles, not independent mathematical reviews.

## Result and failure separation

**Local representation/mathematical failure:** `F-RH-ANA-003a-TERM-WISE-ABSOLUTE-MAJORANT`. The method family “sharpen marginal `|eta_j|`/`|C_j|` bounds, then use triangle inequality through the binomial transform” is structurally too coarse. Even the nearest-singularity geometric scale admits bounded exact signed transform and exponential absolute envelope.

**Local-to-global/gluing failure:** `F-RH-ANA-003a-MAGNITUDE-TO-LI-SIGN`. A coefficientwise magnitude certificate cannot be glued directly to every-index Li positivity without an additional theorem preserving signed/correlated cancellation.

This does **not** prove that no useful coefficient bounds exist. Coffey's `S_gamma(n)=O(n)` result is a positive calibration that structured reorganization can recover much smaller scale for one component. Accordingly, the route is rotated rather than retired.

## New residual

`RH-ANA-003b — CANCELLATION_PRESERVING_PRIME_COMPONENT`:

> In a source-bound cancellation-aware decomposition such as `S_2(n)=S_gamma(n)+S_Lambda(n)`, isolate the exact remaining prime/von-Mangoldt component and determine whether any unconditional signed/correlated bound is strong enough to combine with the explicit archimedean terms for every `n`, without importing an RH-equivalent eta-sign, zero-location, or full Li-positivity condition.

The next cycle should first reconstruct the exact definition and source-proved bounds for `S_Lambda(n)` and compare them with the root-facing sign scale. No numerical prefix can promote this residual.

**Root state:** `OPEN_NO_SOLUTION_CERTIFICATE`.
