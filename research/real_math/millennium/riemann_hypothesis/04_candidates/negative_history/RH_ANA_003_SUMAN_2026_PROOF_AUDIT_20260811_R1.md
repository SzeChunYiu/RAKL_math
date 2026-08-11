# RH-ANA-003 — Suman 2026 Laguerre/Bernoulli proof audit, R1

**Authority:** SOURCE-BOUND VERIFICATION / ROUTE-LOCAL REFUTATION / COMPOSITIONAL SUBPROBLEM / NO RH CANDIDATE / ROOT AUTHORITY NONE

## Exact root boundary

The root remains the classical Riemann Hypothesis: every nontrivial zero `rho` of `zeta(s)` has `Re(rho)=1/2`. The current Clay Mathematics Institute pages still list RH among the unsolved Millennium problems on 2026-08-11. This audit does not promote any neighboring Li/Laguerre statement to the root.

## Source family actually audited

| Family | Source | Role |
|---|---|---|
| Exact Li arithmetic/zero criterion | Bombieri–Lagarias, JNT 77 (1999), DOI `10.1006/jnth.1999.2392` | Exact Li/explicit-formula background and cancellation boundary |
| Li large-`n` dichotomy | A. Voros, arXiv `math/0506326`, MPAG 9 (2006) | The claimed `n log n + o(n)` asymptotic is root-equivalent, so its error term is proof-critical |
| Current claimed proof | S. Suman, *On the Asymptotics of Li coefficients and Proof of the Riemann Hypothesis* (2026), DOI `10.13140/RG.2.2.10579.03362` | Target of falsification/verification |
| Current Laguerre reduction | S. D. S. Khalsa, Zenodo DOI `10.5281/zenodo.18726797` (2026) | DifferenceWitness: Laguerre-weighted reduction is not itself a proof; this source explicitly leaves a uniform cancellation estimate open |
| Laguerre asymptotic scope | DLMF `18.15.14`; see also Frenzen–Wong, SIAM J. Math. Anal., DOI `10.1137/0519087` | Uniformity-domain audit |
| Bernoulli growth / Euler–Maclaurin | DLMF `24.11.1`, `2.10` | Term test and finite-remainder audit |

No authority is assigned to a preprint merely because it is current. The 2026 sources are frontier claims to be checked.

## F1 — Laguerre asymptotic does not justify the unbounded integral as written

Suman's equation (44) invokes the standard large-degree generalized Laguerre oscillatory asymptotic for fixed positive argument. The proof then uses that estimate in equations (48)–(51) to bound an integral extending over `x in [2, infinity)` and concludes `J_n^(2)=O(n^(3/4))`.

The standard formula identified by DLMF 18.15.14 is uniform only on **compact** `x`-intervals inside `(0,infinity)`. That scope does not provide a bound valid on the full unbounded integration domain after substituting the Laguerre argument `log x`. A separate uniform asymptotic theorem, a split into asymptotic regimes with compatible majorants, or another domination argument is required.

**Scoped verdict:** the implication `eq.44 -> global bound eq.50 -> eq.51` is not established by the cited fixed-argument asymptotic. This is a verification/gluing defect, not a theorem that no uniform Laguerre repair is possible.

## F2 — the infinite Bernoulli correction fails the term test

Later, equations (62) and (69)–(75) use an infinite Bernoulli correction of the schematic form

`sum_{k>=1} B_{2k} * n^(1-2k) / (4k)`

and then divide by `n` and pass to `n -> infinity`.

For each fixed positive integer `n`, DLMF 24.11.1 gives

`|B_{2k}| ~ 2 (2k)! / (2 pi)^(2k)`.

Hence the magnitude of the `k`th term after division by `n` behaves like

`(2k)! / (const * k * (2 pi n)^(2k))`.

For fixed `n` this does **not** tend to zero as `k -> infinity`; factorial growth eventually dominates every fixed exponential `(2 pi n)^(2k)`. Therefore the displayed infinite Bernoulli series is not an ordinary convergent series, and the limit manipulation in equations (71)–(75) is invalid as written.

Euler–Maclaurin supplies a **finite-order asymptotic expansion plus a remainder**, not authority to replace that expansion by a convergent infinite Bernoulli sum. A repair must choose a finite truncation order and prove a remainder bound with the exact quantifier order needed for `n -> infinity`.

**Scoped verdict:** this is an independent mathematical failure in the published proof chain as written.

## Combined diagnosis

Either defect is sufficient to break the derivation of the root-equivalent Li asymptotic. Together they localize the next admissible repair obligation:

1. obtain joint `(n,x)` control of the Laguerre kernel on the complete integral/prime-power domain, or rigorously partition the domain into regimes with compatible majorants; and
2. keep the Euler–Maclaurin/Bernoulli expansion finite and prove an explicit remainder estimate before the `n -> infinity` limit.

Only after both are supplied can the argument be rechecked against the exact Bombieri–Lagarias/Voros Li transform. The current audit says nothing about whether such a repair exists.

## RAKL route decision

The dual-memory review changed routing. `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` was reused with an explicit DifferenceWitness to inspect the local-asymptotic/global-integral bridge. `T-RH-LI-PREFIX-QUARTET-CALIBRATION` was retrieved but rejected because the audited proof is not a finite-prefix argument. Open PR `#118` was used only as negative-history routing evidence that the aggregate zero-density/zero-free family is already saturated for the universal-exception bridge; it carries no authority into this result. Open PR `#80` was retrieved as provenance but rejected as proof authority.

The solved subproblem is classified `RAKL_TRIVIAL` / **compositional**: standard source semantics plus an elementary convergence test invalidate this proof chain. There is no new RH theorem, operator, ontology, or independent review.

## Root and next action

`RH`: **OPEN**.

Next shadow atom: prove or refute a repair theorem for the joint-uniform Laguerre/Euler–Maclaurin remainder while preserving the exact Li transform and quantifier order. Any repair that assumes the Voros asymptotic, all-index Li positivity, or an equivalent zero-location statement is circular and must be rejected.
