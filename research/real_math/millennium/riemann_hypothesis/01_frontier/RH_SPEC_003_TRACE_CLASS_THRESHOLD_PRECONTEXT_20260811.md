# RH-SPEC-003 — Trace-class threshold pre-candidate contract

Status: **FROZEN PRE-CANDIDATE**. This file registers the exact atom and evaluator before any theorem candidate is recorded. It is not an RH proof and creates no root authority.

## Exact RH binding and success contract

The root statement remains the repository canonical statement: every nontrivial zero \(\rho\) of \(\zeta(s)\) satisfies \(\Re \rho=1/2\). Root success still requires the complete proof DAG and all verifier/dependency/axiom/novelty/isolated-review obligations in `00_problem_contract/success_contract.yaml`.

RH-SPEC-003 has a strictly smaller success contract: derive, from a separately assumed exact compact-resolvent Hilbert–Pólya spectral bridge and the classical zero-counting theorem, the sharp Schatten membership threshold for
\[
A_\alpha=(I+H^2)^{-\alpha/2},
\]
then record the result only as a necessary-condition/no-go filter. Success on this atom **must not** be promoted to RH.

## Atomic decomposition

- **A0 — spectral bridge assumptions.** Specify a densely defined self-adjoint \(H\), its domain, compact resolvent (or an explicitly equivalent discrete-spectrum hypothesis), one- vs two-sided spectral convention, exact multiplicity rule, and completeness mapping from the spectrum to all nontrivial zeta zeros. These are assumptions for this filter, not achievements.
- **A1 — counting transfer.** Under A0, transfer von Mangoldt's zero-counting asymptotic to the eigenvalue counting function, allowing only a fixed finite perturbation and the declared constant duplication factor.
- **A2 — Stieltjes/dyadic summability.** For \(q=\alpha p\), decide convergence of \(\sum (1+\lambda_n^2)^{-q/2}\) from \(N(T)\asymp T\log T\).
- **A3 — exact Schatten statement.** Use self-adjoint functional calculus to identify the singular values of \(A_\alpha\), proving the iff threshold.
- **A4 — cheapest falsifiers.** Specialize to \(q=1\): ordinary trace class must fail for \((I+H^2)^{-1/2}\) and the first-order resolvent scale. Verify that finite changes and ± duplication do not repair the endpoint.
- **A5 — exemptions and non-circularity.** Explicitly preserve stronger smoothing, heat kernels, relative/zeta/weak/distributional trace mechanisms and noncompact/continuous-spectrum models as outside the no-go; forbid prime matching, positivity, or RH conclusions from A1–A4 alone.

A0 → A1 → A2 → A3 → A4 → A5. No root edge exists from A5 to RH.

## Frozen candidate evaluator

A later candidate will pass only if all of the following are proved from the frozen assumptions:

1. For every \(\alpha>0\) and \(p>0\), \(A_\alpha\in S_p\) iff \(\alpha p>1\).
2. At \(\alpha p=1\), divergence is shown rather than hidden in big-O notation.
3. \((H-i)^{-1}\notin S_1\) is justified from the same eigenvalue multiset (its singular values are \((1+\lambda_n^2)^{-1/2}\)).
4. For each \(p>1\), the first-order resolvent scale lies in \(S_p\).
5. No assertion is made that a compact-resolvent HP operator exists, that its spectrum actually equals the zeta zeros, or that RH follows.
6. The operator obligation matrix below is explicitly audited.

## Operator obligation matrix

| Obligation | RH-SPEC-003 requirement |
|---|---|
| Domain | Must be explicitly assumed/specified for any concrete H; no formal differential expression is treated as an operator. |
| Self-adjointness | Required before functional calculus or “real spectrum” language. |
| Positivity | Not needed for the Schatten filter and may not be inferred; Weil/de Branges positivity remains a separate RH-sensitive obligation. |
| Trace legitimacy | Central: distinguish ordinary trace/Schatten class from regularized or distributional traces. |
| Prime matching | Not supplied by zero counting; any prime-power weights/test-function identity requires an independent derivation. |
| Multiplicity | Exact multiplicities must be included in the spectral count; simple-zero assumptions are forbidden. |
| Completeness | All target zero ordinates must be represented under the declared convention; finite-zero matching is insufficient. |
| Non-circularity | The spectral identification, domain and self-adjointness cannot be obtained by assuming RH, real zeros, or an equivalent positivity statement. |
| Limits/interchanges | Any trace, Stieltjes integration, cutoff removal or regularization must state the convergence/interchange theorem used. |
| Representation | de Branges/canonical-system or dynamical representations require an independently constructed target-side object, not a representation manufactured from the desired zero set. |

## Primary source anchor

The counting input is H. von Mangoldt, *Zur Verteilung der Nullstellen der Riemannschen Funktion ξ(t)*, Mathematische Annalen **60** (1905), 1–19, DOI:10.1007/BF01447494. The only asymptotic consequence needed by this atom is \(N(T)\sim (T/(2\pi))\log T\); the exact lower-order terms are not used to infer anything stronger.

## Cheap-counterexample priority

Before attempting a new operator construction, test whether its claimed ordinary trace uses first-order resolvent smoothing. If yes, an exact RH spectral count would itself force failure of trace class; the model must change the trace notion or smoothing order. Numerical spectra and finite-zero agreement cannot repair this functional-analytic obstruction.
