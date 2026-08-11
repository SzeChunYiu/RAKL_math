# RH-SPEC-003 — weak-L1 endpoint context defect and retrospective summability calibration

**Authority:** `PRE_CANDIDATE_CONTEXT_DEFECT / RETROSPECTIVE_ANALYTIC_CALIBRATION / SEARCH_CONTROL_ONLY / NO_RH_CANDIDATE / ROOT_AUTHORITY_NONE`

**Frozen parent atom:** `RH-SPEC-003`  
**Frozen context hash:** `sha256:90a186d8e391a32b0aaa061f3c9cd42ad009633caa0232f190562e894769d529`  
**Pre-defect PR head:** `ae10691d5857924dbec6ad0555d57db059c8a979`  
**Current framework read before this audit:** `SzeChunYiu/RAKL@60a38728d0ebace2fa2312bcad81d1d3f9df757c`  
**Current application main read before this audit:** `SzeChunYiu/RAKL_math@5d2977892f6fe726e1c983e5f50c55869ecc18e1`

This document records a defect found **after** the `RH-SPEC-003` context had been frozen but **before** any `CANDIDATE_PROPOSED` event. The frozen packet is not rewritten or backdated. The calculation below is therefore retrospective calibration/search control only. It is not preregistered candidate evidence and cannot be promoted as an `RH-SPEC-003` theorem candidate.

## Exact defect

The frozen context contains the near-solved-analogue sentence

> “the RH counting law suggests a weak-L1 endpoint rather than trace class”

and later lists “Dixmier/weak traces” among possible endpoint escape routes. For the **naive first-order compact-resolvent operator** `A_1=(I+H^2)^(-1/2)`, that endpoint classification is false under the exact Riemann zero-counting growth assumed by the atom. The logarithmic excess in `N(T) ~ C T log T` makes `A_1` strictly larger than the usual weak trace class.

The sharp Schatten threshold `alpha*p>1` targeted by the parent atom survives this correction. What fails is the parent packet's endpoint interpretation.

## Conditional spectral setup

Assume only for this filter that:

1. `H` is densely defined and self-adjoint on a specified Hilbert space;
2. `H` has compact resolvent, equivalently a purely discrete finite-multiplicity spectrum for the present calculation;
3. after a declared one-sided/two-sided convention and finite perturbation, the absolute eigenvalue counting function `M(T)` matches the complete nontrivial Riemann-zero counting multiset with multiplicity, so
   `M(T) ~ C T log T` for a constant `C>0` fixed by that convention;
4. no conclusion about existence of such `H`, prime matching, positivity, or RH is inferred from these assumptions.

The arithmetic input is von Mangoldt's zero-counting theorem. Primary source: H. von Mangoldt, *Zur Verteilung der Nullstellen der Riemannschen Funktion ξ(t)*, Math. Ann. 60 (1905), 1–19, DOI `10.1007/BF01447494` (full-text index: https://eudml.org/doc/158173).

## Step 1 — invert the count

Let `nu_n` be the nondecreasing absolute eigenvalues, repeated with multiplicity. From

`M(T) ~ C T log T`

monotonic inversion gives

`nu_n ~ n / (C log n)`.

Indeed, for `T_n=n/(C log n)`, one has `log T_n/log n -> 1`, hence `C T_n log T_n/n -> 1` and therefore `M(T_n)/n -> 1`; the standard `(1±epsilon)` monotonic squeeze yields the generalized-inverse asymptotic.

Finite spectral changes and constant-factor one-sided/two-sided duplication alter `C` but not any threshold below.

## Step 2 — exact Schatten threshold

For `alpha>0`, put

`A_alpha=(I+H^2)^(-alpha/2)`.

Its singular values satisfy

`s_n(A_alpha) ~ (C log n / n)^alpha`.

Therefore, for every `p>0`,

`sum_n s_n(A_alpha)^p`

has the same convergence behavior as

`sum_n (log n)^(alpha p) / n^(alpha p)`.

By the integral test,

`A_alpha in S_p  <=>  alpha*p > 1`.

At the critical exponent `alpha*p=1`, the partial sums diverge at logarithmic-square order rather than logarithmic order.

For `alpha=1,p=1`, more precisely,

`sum_{n<=N} s_n(A_1) ~ (C/2) (log N)^2`.

Thus neither `(I+H^2)^(-1/2)` nor the first-order resolvent scale `(H-i)^(-1)` can be trace class in an exact compact-resolvent Hilbert–Pólya realization with the Riemann counting law.

## Step 3 — the weak-Schatten endpoint also fails

At the critical index `p=1/alpha`, ordinary weak Schatten membership would require

`sup_n n^(1/p) s_n(A_alpha) < infinity`.

But

`n^(1/p) s_n(A_alpha) ~ C^alpha (log n)^alpha -> infinity`.

Hence

`A_alpha notin S_{1/alpha, infinity}`

at the uncorrected endpoint. In particular, `A_1` is not in the usual weak trace ideal on the singular-value criterion. Under the Macaev/Dixmier partial-sum criterion for `p=1`, the same failure is visible from

`(1/log N) sum_{n<=N}s_n(A_1) ~ (C/2) log N -> infinity`.

So a standard Dixmier trace is **not** automatically available for the naive first-order operator. Any use of a weak/Dixmier trace must first change the operator/weight or prove membership in the precise ideal being used.

## Step 4 — exact logarithmic correction phase diagram

The counting law itself suggests a clean calibration family, not an RH construction:

`B_{alpha,beta}=(I+H^2)^(-alpha/2) [log(e+|H|)]^(-beta)`.

Using `log nu_n ~ log n`,

`s_n(B_{alpha,beta}) ~ C^alpha n^(-alpha) (log n)^(alpha-beta)`.

At the critical power `p=1/alpha`:

- weak `S_p` membership holds exactly when `beta >= alpha`;
- ordinary `S_p` membership holds exactly when `beta > 2 alpha`;
- at `beta=alpha`, `s_n(B_{alpha,alpha}) ~ C^alpha n^(-alpha)`.

The especially transparent first-order case is

`B_{1,1}=(I+H^2)^(-1/2) [log(e+|H|)]^(-1)`,

for which

`s_n(B_{1,1}) ~ C/n`

and

`(1/log N) sum_{n<=N}s_n(B_{1,1}) -> C`.

This is only a target-specific summability calibration. It supplies no prime-power trace formula, no canonical-system representation, no positivity theorem, and no existence theorem for `H`.

## Same-context expert cell

**Operator theorist.** The functional calculus is legitimate only after the densely defined self-adjoint domain and compact-resolvent hypothesis are separately established. Under those hypotheses the singular-value calculation is exact, and the naive first-order endpoint is not weak Schatten.

**Analytic number theorist.** The only arithmetic ingredient used is the global von Mangoldt zero count with multiplicity. The argument cannot import prime weights or an explicit formula from the count alone.

**Trace-formula / dynamical specialist.** Ordinary trace class, weak/Dixmier ideals, zeta regularization, relative traces and distributional trace formulas are distinct. The calculation rejects a blanket first-order ordinary/weak-trace claim but does not touch independently justified noncompact or distributional trace formulas. Connes' primary construction is explicitly an absorption/resonance and adelic trace-formula framework, so it is outside this compact-resolvent filter: A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, arXiv:math/9811068.

**de Branges / canonical-systems specialist.** The filter may be applied only after a concrete canonical system supplies its operator, domain, boundary conditions, multiplicities and a non-circular Xi identification. It cannot manufacture de Branges positivity.

**de Bruijn–Newman / random-matrix specialist.** Flow and random-matrix information do not change the counting-to-ideal calculation and remain proposal/calibration signals. The de Bruijn–Newman lane has its own exact global obstruction; for current primary-source calibration see B. Rodgers and T. Tao, *The De Bruijn-Newman constant is non-negative*, arXiv:1801.05914.

**Adversarial verifier.** Two independent candidate blockers are present: the frozen weak-L1 endpoint statement is false, and the focused `RH spectral assurance` workflow at pre-defect head did not list `test_rh_spec_003_strict_packet.py`, even though the general pinned-application suite did execute the full test directory. A green focused workflow therefore did not by itself certify the new strict packet against current framework main.

## Freshness and non-circularity audit

Framework freshness: `RAKL@15f1c3a... -> 60a3872...` changes only `pyproject.toml` (`pythonpath` adds the repository root); no mathematical context, memory, trace, metacognition, breakthrough, or assurance runtime file changed in that one-commit delta. This is an infrastructure freshness fact, not theorem evidence.

Application freshness: the PR's prior base `29d566f... -> current main 5d29778...` changes only Navier–Stokes application artifacts and `.gitattributes`; no RH file is changed by that main-line delta. This avoids a same-file conflict but does not waive exact-head CI.

The present calculation assumes the full exact spectral counting multiset only to derive a **necessary** ideal-membership filter. It never uses self-adjointness to conclude that the zeta zeros are on the critical line and never uses RH to prove the counting theorem. There is no root edge.

## Chronology consequence

Because this endpoint result was discovered while auditing an already-frozen packet, it cannot now be backfilled as a preregistered `RH-SPEC-003` candidate. The correct state transition is:

`RH-SPEC-003 PRE-CANDIDATE -> CONTEXT DEFECT FOUND -> CANDIDATE GENERATION BLOCKED -> RETROSPECTIVE CALIBRATION ONLY`.

A future successor atom may use the corrected endpoint picture only if its exact question, evaluator, method-transfer assumptions/disanalogies, expert cell, dual memory review and hash-chained trace are frozen **before** any new candidate result is generated.

## Root status

`RH-SPEC-003` supplies no RH theorem, no Hilbert–Pólya operator, no Weil/de Branges positivity proof, no prime matching, no de Bruijn–Newman conclusion, no closed proof DAG, and no root certificate.
