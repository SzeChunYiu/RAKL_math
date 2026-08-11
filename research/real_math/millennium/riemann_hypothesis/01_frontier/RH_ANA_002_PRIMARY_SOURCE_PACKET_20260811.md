# RH-ANA-002 primary-source packet — prime-side strength audit

**Authority:** `SOURCE_BOUND_PRE_CANDIDATE_ROUTE_CLASSIFICATION / NO_MATHEMATICAL_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`.

## Why this child exists

`RH-ANA-001` killed only a shortcut: a long finite positive prefix of Li-type coefficients is not a global RH certificate. The next atom must add genuinely zeta-specific structure and must not merely compute more coefficients.

This packet asks a narrower question before any new inequality is proposed:

> Which zeta-specific Li/prime-side bounds are genuine intermediate targets, and which are already equivalent-strength rewritings of RH?

## Lagarias arithmetic decomposition

Primary source: Jeffrey C. Lagarias, *Li coefficients for automorphic L-functions*, Annales de l'Institut Fourier 57 (2007), 1689–1740, DOI `10.5802/aif.2311`, arXiv `math/0404394`.

For the automorphic setting, with the zeta function as the `GL(1)` trivial specialization, Lagarias writes the Li coefficient as an archimedean contribution minus a finite-place contribution plus the pole term. The source then proves:

- the archimedean term has unconditional dominant growth `(N/2) n log n + C_1 n + O(1)`;
- the finite-place contribution is the incomplete Li coefficient using zeros with height below `sqrt(n)`, up to `O(sqrt(n) log n)`;
- under RH the incomplete coefficient is `O(sqrt(n) log n)`;
- if RH holds only up to height `T`, a bound of this shape is licensed only for a finite index range of order `T^2 / (log T)^2`;
- if RH fails, the incomplete Li term is sometimes exponentially large in `n`.

The paper also gives the finite-place arithmetic expression through coefficients of `-L'/L` at `s=1`. For the zeta specialization these coefficients are defined by a **regularized** prime sum: a divergent von-Mangoldt sum is paired with an explicit logarithmic subtraction before the limit is taken. In the Li test-function appendix, an unbounded transform contribution is likewise cancelled by the finite-prime side in the cutoff explicit formula.

### Route-strength consequence

This is a source-derived implication, not a novelty claim.

For zeta, the exact relation

`S_f(n) = incomplete_Li(n, sqrt(n)) + O(sqrt(n) log n)`

and Lagarias' RH-failure alternative imply:

- under RH, `S_f(n)` has polynomial growth (indeed the source gives `O(sqrt(n) log n)`);
- if RH fails, `S_f(n)` is sometimes exponentially large, because a polynomial error cannot cancel the source-described exponential incomplete-Li excursions.

Therefore a theorem of the form

> `|S_f(n)| <= C n^A` for every sufficiently large `n`

for fixed `C,A`, when applied to the exact zeta finite-place term, is **root-strength**: it would rule out RH failure. It is not an appropriate “small child lemma” merely because it is written with primes.

This route-pruning observation prevents the next search from disguising the root as a prime-sum growth estimate.

## Finite Li information should map to partial zero geometry

Primary source: Francis C. S. Brown, *Li's criterion and zero-free regions of L-functions*, Journal of Number Theory 111 (2005), 1–32, DOI `10.1016/j.jnt.2004.07.016`.

Brown's primary abstract states a two-way quantitative relation: finitely many Li inequalities imply a zero-free region, and conversely a zero-free region implies a finite amount of Li-inequality control. This is the correct logical shape for finite-prefix progress: **partial coefficient information -> partial zero exclusion**, not finite prefix -> RH.

This packet deliberately does not reuse Brown's detailed constants or internal lemmas without a separate correction audit; later literature reports corrections to parts of that argument. Only the primary article's high-level published claim is used here as a method-transfer anchor.

Primary source: Pedro Freitas, *A Li-type criterion for zero-free half-planes of Riemann's zeta function*, arXiv `math/0507368` (2005). Freitas defines a parameterized Li-type family giving necessary and sufficient conditions for zero-free strips inside the critical strip. This supports a **graded target representation**: choose an exact partial zero-free region first, then ask for a cheaper coefficient/prime condition that reaches it.

## Current zeta-specific partial-control calibration

Primary source: Chiara Bellotti, Tim Trudgian, Andrew Yang, *Zero-free regions inspired by work of Heath-Brown*, arXiv `2603.21490` (2026).

The paper proves an explicit unconditional zero-free region for zeta near `Re(s)=1` for `t>=3`. This is retained only as a current partial-control benchmark. A coefficient-based route would need to state what registered zero-free region it improves; no extrapolation toward the critical line is licensed.

## Implication-strength ladder

| Level | Statement family | Licensed interpretation |
|---|---|---|
| L0 | finitely many Li inequalities | finite/quantified zero-exclusion only; use Brown/Freitas-type geometry |
| L1 | RH/zero-location known only up to finite height `T` | Lagarias gives finite-index control, not all-index control |
| L2 | improved zeta-specific zero-free region | genuine partial progress if proved beyond current bounds |
| L3 | all-`n` polynomial bound on exact `S_f(n)` | root-strength by the Lagarias incomplete-Li dichotomy |
| L4 | all Li coefficients nonnegative | exact RH criterion |

The high-information search frontier is **between L1/L2 and L3**. A useful next candidate must be strong enough to improve a named partial zero-exclusion target while remaining demonstrably weaker than L3/RH.

## Regularization warning

A naive prime-by-prime positivity proof is not licensed. The finite-place formulas contain conditionally convergent/regularized sums and cancellation against explicit subtraction/cutoff terms. Every future prime-side candidate must freeze:

1. cutoff or summation convention;
2. subtraction/renormalization term;
3. order of limits;
4. uniformity in the Li index;
5. the exact zero-free consequence;
6. an argument that the claimed intermediate condition is not already RH-equivalent.

## Cross-Millennium transfer

The RAKL tool `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` is applicable only at the abstract audit level.

**DifferenceWitness.** Yang–Mills source: a positive finite-cutoff dimensionless gap can collapse after continuum normalization. RH target: a finite-index or partial zero-exclusion certificate can fail to preserve the all-index/root zero-location coordinate. Shared structure is the missing quantitative bridge; the mathematical mechanisms, units, and limits are different. No Yang–Mills theorem transfers.

## Selected next action

Do **not** propose a global polynomial `S_f(n)` bound as a child lemma. Instead, after the strict packet passes current RAKL gates, choose one exact partial zero-free target and derive the weakest coefficient/prime residual inequality that would improve it. The first candidate must be paired with:

- a proof that the target is strictly weaker than RH;
- an exact cutoff/regularization contract;
- the `RH-ANA-001` quartet falsifier for any finite-prefix shortcut;
- a current-best-bound comparison at matching height/region;
- a negative branch stating what failure teaches about the representation.

No RH solution or new theorem is claimed here.
