# RH-ANA-003 — index/height and cancellation audit, R1

**Authority:** SOURCE_BOUND_ROUTE_DIAGNOSTIC / COMPOSITIONAL_SUBPROBLEM / NO_RH_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE

**Prospective binding:** the registered discriminator was frozen before this result in `RH_ANA_003_CONTEXT_FIBER_20260811_R1.json`, `RH_ANA_003_RESEARCH_MEMORY_REVIEW_20260811_R1.json`, `SAME_CONTEXT_REVIEW_RH_ANA_003_20260811_R1.md`, and pre-candidate trace through `RH-ANA-003-R1-E07`. Earlier source scouting in the run is background only and receives no prospective evidence credit.

## Question

For the exact Li-coefficient / explicit-formula route, what is the first source-bound coordinate that explains why finite-height, zero-density, or finite-prime information does not automatically become all-index positivity?

This is a candidate-free localization audit. It does not search for a new positivity inequality.

## Primary-source reconstruction

### 1. The finite-place term is an incomplete Li coefficient at height about `sqrt(n)`

Jeffrey C. Lagarias, *Li Coefficients for Automorphic L-Functions*, arXiv:math/0404394v4, pp. 3–4, equations (1.14)–(1.18), decomposes the generalized Li coefficient into an archimedean main term and a finite-place term. The finite-place contribution satisfies, with the source's contragredient convention,

```text
S_f(n, pi) = lambda_n(sqrt(n), pi^vee) + O(sqrt(n) log n).
```

The incomplete coefficient `lambda_n(T,pi)` is the zero sum restricted to `|Im rho| < T`. Thus, for this representation, the sharper finite-place residual is not “prime positivity” in isolation. It is an incomplete Li coefficient whose natural height scale grows like `sqrt(n)`, plus a controlled remainder.

For the zeta specialization this means that any prime-side method intended to control all `lambda_n` must eventually control an equivalent finite-place/incomplete-Li quantity on an unbounded height scale.

### 2. Finite-height RH gives only a bounded Li-index window

The same primary source states that if RH holds up to height `T`, a bound of the RH-shaped finite-place form holds only for

```text
n <= T^2 / [4 (log T)^2].
```

This is an explicit scale-transfer law. It provides a source-bound reason that finite verification of zeros cannot be extrapolated to all-index Li positivity. As `n` grows, the height required by this route must also grow.

This does **not** say finite-height work is useless. It says its licensed conclusion is range-limited unless supplemented by a theorem closing the unbounded index/height limit.

### 3. Off-RH finite-place behavior can be exponentially large

Immediately after Theorem 1.1, Lagarias notes that if RH fails, the incomplete Li coefficient term can sometimes be exponentially large in `n`; for zeta this is traced back to Bombieri–Lagarias. This makes the incomplete-Li residual root-sensitive rather than a benign lower-order term.

### 4. Positive source coordinates do not remove the transform cancellation

André Voros, *Sharpenings of Li's criterion for the Riemann Hypothesis*, arXiv:math/0506326v2, p. 3, equations (9)–(12), writes

```text
lambda_n = -n sum_{j=1}^n [(-1)^j/j] binom(n+j-1, 2j-1) Z(j).
```

Voros explicitly notes that `Z(j)` is positive and gently varying for real `j >= 1`, while the displayed formula remains an oscillatory sum and is difficult to control directly. Therefore a method that tries to prove positivity of prime-derived or zeta-derived source coordinates term by term has not yet solved the signed transform problem.

Bombieri and Lagarias, *Complements to Li's Criterion for the Riemann Hypothesis*, J. Number Theory 77 (1999), 274–287, DOI `10.1006/jnth.1999.2392`, is the source of the arithmetic formula via the Guinand–Weil explicit formula and the relation to Weil positivity. The exact regularization and source convention remain load-bearing.

## Hostile single-zero calculation

For one zero `rho = beta + i gamma`, the exact Li summand contains

```text
q(rho)^n,  q(rho) = 1 - 1/rho.
```

Elementary algebra gives

```text
|q(rho)|^2
= |rho-1|^2 / |rho|^2
= [ (beta-1)^2 + gamma^2 ] / [ beta^2 + gamma^2 ]
= 1 + (1 - 2 beta)/(beta^2 + gamma^2).
```

Hence a zero with `beta < 1/2` has `|q(rho)| > 1`. By the functional-equation/conjugation symmetry, any off-critical quartet has a reflected member on the left of the critical line. Therefore one surviving off-line quartet contains an exponentially amplifying factor in the Li zero representation.

This is an **envelope** statement, not a sign theorem. The factor has complex phase and quartet contributions may cancel at particular indices. No claim is made that one selected zero forces every later `lambda_n` negative.

For `beta = 1/2 - delta` with small positive `delta`,

```text
log |q(rho)|
= 1/2 log(1 + 2 delta/(beta^2+gamma^2))
approx delta/(beta^2+gamma^2).
```

So the rough one-e-fold activation scale is

```text
n_* ~ (beta^2 + gamma^2)/delta.
```

This scale is only a hostile calibration. It explains why a high, very-near-line defect can be invisible for a long finite prefix while remaining all-index relevant.

## What this falsifies

The audit rejects the following inference patterns **within their stated scope**:

1. `finite zero verification -> all-index Li positivity` without an unbounded height/index closure theorem;
2. `zero-density sparsity -> all-index Li positivity` when the density hypothesis is compatible with one off-line zero and no separate exclusion/cancellation theorem is supplied;
3. `positive prime/zeta source coordinates -> lambda_n >= 0` when the exact transform remains oscillatory;
4. `finite prime truncation looks positive -> root progress` without a uniform all-`n` tail theorem.

These are route-pruning results, not impossibility theorems for zero-free, zero-density, mollifier, resonance, or explicit-formula methods as entire research programs.

## Sharper residual

The smallest current analytic interface is:

> Obtain genuinely unconditional control of the exact incomplete-Li / finite-place residual at the `sqrt(n)` scale, uniformly for all positive integers `n`, or prove an alternative exact representation whose remainder has equivalent all-index authority, without importing an RH-equivalent zero-exclusion or growth hypothesis.

A future zero-density, zero-free, mollifier, resonance, or prime-sum proposal should first state exactly how it acts on this residual. If it acts only on an average or finite-height surrogate, it needs a separate bridge theorem.

## Solved-subproblem novelty classification

The scoped diagnostic is classified `RAKL_TRIVIAL` / compositional under the v3 ancestry taxonomy. The ingredients are existing primary-source theorems plus elementary algebra; no new operator, representation, ontology, or mathematical theorem is claimed. The research value is localization and route pruning.

## Source boundary

- Lagarias statements are bound to arXiv:math/0404394v4 and the published Annales de l'Institut Fourier paper; the v4 page explicitly notes a corrected remainder term in Theorem 1.1.
- Voros statements are bound to arXiv:math/0506326v2 / Math. Phys. Anal. Geom. 9 (2006), 53–63.
- Bombieri–Lagarias arithmetic-formula attribution is bound to JNT 77 (1999), DOI `10.1006/jnth.1999.2392`.
- No numerical zero verification is used as proof evidence.
