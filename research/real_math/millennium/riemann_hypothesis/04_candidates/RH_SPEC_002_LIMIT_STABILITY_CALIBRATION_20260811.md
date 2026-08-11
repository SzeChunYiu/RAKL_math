# RH-SPEC-002 limit-stability calibration — CAL001

**Authority:** `RETROSPECTIVE_KNOWN_ANSWER_CALIBRATION / SEARCH_CONTROL_ONLY / NO_RH_EVIDENCE / NO_PROOF / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`.

**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`.

This is a retrospective assimilation of the five-case calibration from
`RAKL_math` PR #15 at `7f45008d`.  The accepted parent trace had selected a
broad hostile limit-stability calibration before result access, but the exact
five-case identity was first committed as a result and its
`CANDIDATE_PROPOSED` continuation was committed later.  Therefore this packet
does **not** claim exact preregistration or pre-result candidate freezing.  The
chronology and stale-hash failure are preserved in
`04_candidates/negative_history/RH_SPEC_002_PR15_CHRONOLOGY_HASH_AUDIT_20260811.json`.

The standard mathematical implications and counterexamples below remain
independently checkable and useful for search control. The same-context expert
cell remains non-independent.

## Expert cell and delegated checks

1. **Analytic-number-theory / entire-function lead** — prove the exact target-side implication supplied by local-uniform entire-function convergence; audit multiplicity and nonzero-limit requirements.
2. **Spectral/operator lead** — exhibit a self-adjoint strong-resolvent family whose spectral points disappear, separating operator convergence from complete spectral transport.
3. **Adversarial functional-analysis lead** — give a dense Galerkin approximation with a persistent spurious gap eigenvalue.
4. **Trace/determinant lead** — construct a real-rooted finite-zero-prefix sequence that still fails entire-function convergence, exposing normalization/growth debt.
5. **Formal-methods lead** — type every implication/counterexample and keep target-side sufficiency separate from source-side proof obligations.
6. **Novelty/research-value lead** — ensure all mathematical ingredients are recorded as known calibration facts and route-pruning, not new mathematics.

The joint result is not an average vote: every non-compensatory objection below remains explicit.

## CAL-HURWITZ-REAL-ZERO-TRANSPORT — positive control

Let `F_n` be entire functions with only real zeros and suppose `F_n -> F` locally uniformly on `C`, where `F` is entire and not identically zero.

Assume for contradiction that `F(z0)=0` for some nonreal `z0`. Choose a closed disk `D` around `z0` disjoint from the real axis. Every `F_n` is zero-free on `D`. By Hurwitz's zero-stability theorem, a locally uniform limit of zero-free holomorphic functions on the disk is either zero-free or identically zero there. Since `F(z0)=0`, `F` would be identically zero on the disk and hence, by the identity theorem, identically zero on `C`, contradiction.

Therefore every zero of `F` is real.

For an isolated zero `z0` of multiplicity `m`, choose a small disk whose boundary contains no zero of `F`. Local-uniform convergence plus Rouché/Hurwitz zero counting gives exactly `m` zeros of `F_n` in that disk for all sufficiently large `n`, counted with multiplicity.

### RH consequence — conditional only

If a source-defined, canonically normalized family of RH approximant entire functions is independently proved to:

- have only real zeros at every stage in a cofinal family;
- converge locally uniformly on all compact subsets of `C` to the exact nonzero Riemann `Xi` function;

then the **target-side** zero-transport step is sufficient for RH, and multiplicity is controlled compact-by-compact.

This calibration does **not** establish either source-side premise.

## CAL-STRONG-RESOLVENT-DISAPPEARING-SPECTRUM — negative control

On `l^2(N)`, let `P_n` be the rank-one orthogonal projection onto basis vector `e_n`, and put `A_n=P_n`. For every fixed vector `x`, `P_n x -> 0`, hence `A_n -> 0` strongly.

For `z` off the real axis,

`(P_n-zI)^(-1) = (-1/z)I + (1/(1-z)+1/z) P_n`.

The second term converges strongly to zero, so the resolvents converge strongly to `(-zI)^(-1)`. Thus `A_n -> 0` in strong-resolvent sense.

Nevertheless, `1` is an eigenvalue of every `A_n`, while `1` is absent from the spectrum of the limit operator `0`.

**Disposition:** `STRONG_RESOLVENT_WITHOUT_EXTRA_SPECTRAL_EXACTNESS = TOO_WEAK` for complete RH spectral transport.

This does not claim that a specific RH approximant family exhibits this pathology.

## CAL-GALERKIN-SPECTRAL-POLLUTION — negative control

Define a self-adjoint operator `A` on `l^2(N)` by

- `A e_(2k-1) = -e_(2k-1)`;
- `A e_(2k) = e_(2k)`.

Hence `sigma(A)={-1,+1}`.

For each `n`, set

`v_n = (e_(2n-1)+e_(2n))/sqrt(2)`

and

`L_n = span{e_1,...,e_(2n-2), v_n}`.

The union of the `L_n` is dense, because each previously mixed pair appears as ordinary basis vectors at the next stage. But

`A v_n = (-e_(2n-1)+e_(2n))/sqrt(2)`,

which is orthogonal to `L_n`. Therefore the Galerkin compression `P_{L_n} A|_{L_n}` has eigenvalue `0` for every `n`, even though `0` lies in the true spectral gap `(-1,1)`.

**Disposition:** finite-dimensional self-adjointness plus density of trial spaces does not exclude spectral pollution.

## CAL-TWO-PARAMETER-NONCOMMUTING-LIMIT — negative control

Let the one-dimensional self-adjoint operator `A_(N,lambda)` have eigenvalue

`a_(N,lambda)=N/(N+lambda)`.

Then

- first `N -> infinity`, then `lambda -> infinity`: limit `1`;
- first `lambda -> infinity`, then `N -> infinity`: limit `0`;
- along `N=lambda -> infinity`: limit `1/2`.

**Disposition:** an RH family indexed by more than one cutoff/scale must freeze a cofinal net/path or prove uniform path independence. Writing only `N,lambda -> infinity` is under-specified.

## CAL-FINITE-ZERO-PREFIX-WITHOUT-ENTIRE-CONVERGENCE — negative control

Define

`G_n(z)=exp(n z) * product_{k=1}^n (1-z^2/k^2)`.

Every zero of `G_n` is real, and its zeros `+/-1,...,+/-n` exactly match an increasing finite prefix of the zeros of `sin(pi z)/(pi z)`. Also `G_n(0)=1` for every `n`.

But at `z=1/2`,

`product_{k=1}^n (1-1/(4k^2)) -> 2/pi`,

while `exp(n/2) -> infinity`. Hence `G_n` does not converge locally uniformly to `sin(pi z)/(pi z)`.

**Disposition:** arbitrarily long exact zero-prefix agreement, real-rootedness, and a one-point normalization are insufficient. A source-side normalization/growth/compactness theorem is load-bearing.

## Package ranking after calibration

| Package | Disposition | Exact reason |
|---|---|---|
| locally uniform, source-normalized entire determinants -> exact nonzero `Xi` | `TARGET_SIDE_SUFFICIENT_BUT_SOURCE_SIDE_UNPROVED` | Hurwitz/Rouché transports zero reality and multiplicity once the exact entire-function convergence is proved |
| norm resolvent + route-specific compactness/no-pollution + exact arithmetic identity | `POTENTIALLY_SUFFICIENT_ROUTE_SPECIFIC` | could control isolated spectra, but the required RH-family hypotheses are not established |
| strong resolvent or Mosco/form convergence without extra spectral exactness | `TOO_WEAK` | exact disappearing-spectrum calibration plus known pollution theory |
| finite zero prefix / zero counting / UV or GUE asymptotics | `TOO_WEAK` | can fit arbitrarily much finite zero data while entire-function convergence fails |
| unspecified joint cutoff limit | `UNDER_SPECIFIED` | exact path-dependent two-parameter example |

## Six-role synthesis

- **Analytic-number-theory lead:** ACCEPT the local-uniform entire-function package as the cleanest target-side implication; BLOCK any claim that it has been derived from the arithmetic construction.
- **Spectral/operator lead:** REJECT strong-resolvent/Mosco language as sufficient by itself; retain norm-resolvent + compactness as a possible route-specific family.
- **Adversarial lead:** ACCEPT the pollution and disappearing-spectrum examples as generic falsifiers; explicitly refuses to extrapolate them into a claim about the CCM/Suzuki approximants.
- **Trace/determinant lead:** BLOCK post-hoc normalization and finite-zero fitting; require canonical source-side normalization before evaluating zeta agreement.
- **Formal-methods lead:** ACCEPT the calibration as a bounded result and require the next residual to get a fresh strict context before theorem generation.
- **Novelty/research-value lead:** classify the result as route-pruning and problem representation gain only; no novelty claim.

## Assurance supersession

The PR #15 implication that the exact suite was demonstrably frozen before
evaluation is superseded.  Later trace timestamps cannot substitute for a
repository-visible pre-result evaluator identity.  The retained Hurwitz tool
is `CONDITIONALLY_REUSABLE` from the standard theorem and its stated
hypotheses, not promoted by this retrospective execution record.

This identity is not merged with the distinct local 11-case calibration whose
evaluator was committed before execution.  Results, hashes, trace events and
authority do not transfer between those lineages.

## New residual

`RH-SPEC-002a — DETERMINANT-COMPACTNESS-BRIDGE`

> For the source-defined finite/restricted RH approximants, identify the exact source-side uniform bounds and canonical normalization that would imply local-uniform convergence of normalized entire determinants to `Xi` on every compact subset, or else decisively falsify that determinant route.

This residual is **not yet authorized for candidate generation**. It requires a new context fiber, method-transfer packet, same-context expert review, dual-memory review, and hash-chained pre-candidate trace.

Artifact identity is bound in `RH_SPEC_002_LIMIT_STABILITY_CALIBRATION_20260811.json`.
