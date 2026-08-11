# RH-ANA-002 — Suzuki Li-norm faithfulness matrix

**Atom:** `RH-ANA-002 — LI_NORM_IDENTITY_DEFECT`  
**Action:** registered candidate-free `LI_NORM_FAITHFULNESS_MATRIX`  
**Context hash:** `sha256:300b787769442af040d944e0b52db106881844a9238c021e8804c7f382660742`  
**Authority:** `SOURCE_BOUND_ROUTE_DIAGNOSTIC / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`

## Discriminator

The strict packet asked a deliberately narrow question before any new inequality was allowed:

> Does the unconditional part of Suzuki's Li-norm construction expose an exact, source-proved sub-obligation that is strictly weaker than the RH-equivalent all-index identity `lambda_n=(2 pi)^(-1)||G_n||_2^2` and can transport positivity to the true Li coefficients?

The audit is dependency-first and counterexample-first. A manifestly nonnegative norm is not counted as progress unless the source also supplies an unconditional faithfulness map to `lambda_n`. Defining `D_n=(2 pi)^(-1)||G_n||_2^2-lambda_n` is bookkeeping only.

## Primary source

Masatoshi Suzuki, *Li coefficients as norms of functions in a model space*, Journal of Number Theory 252 (2023), 177–194; arXiv:2301.05779, especially Theorem 1.1, Propositions 2.1, 2.2, 3.1, 3.2, the proof of Theorem 1.1, and Section 4.1.

No secondary exposition is used to assign a dependency class.

## Dependency matrix

| ID | Source step | Classification | What it gives | Why it does not yet transport positivity |
|---|---|---|---|---|
| U1 | Definitions of `H_n` and `G_n` from `xi`, `xi'/xi` and the zeta Laurent data | `UNCONDITIONAL` | A concrete zeta-specific analytic object for each positive integer `n` | Definition alone gives no equality with `lambda_n` |
| U2 | Proposition 2.1 | `UNCONDITIONAL` | An exact identity relating `H_n` to the zero-sum meromorphic function through `xi/(xi+xi')`, derived using the explicit formula | It is not an unconditional norm-to-Li identity and does not make the Li sign manifest |
| U3 | Proposition 2.2 | `UNCONDITIONAL` | `G_n|_R` is bounded, real-analytic and in `L^2(R)` | It implies only that `P_n=(2 pi)^(-1)||G_n||_2^2` exists and is nonnegative |
| U4 | Hilbert-space norm nonnegativity | `UNCONDITIONAL` | `P_n >= 0` | A positive surrogate has zero Li-sign authority without faithfulness |
| R1 | Proposition 3.1: Hermite–Biehler / meromorphic-inner condition for the associated `E`/`Theta` | `RH_EQUIVALENT` | The model-space structure needed for the later orthogonal machinery | Importing it unconditionally would already import an RH-equivalent condition |
| C1 | Proposition 3.2 | `RH_CONDITIONAL` | Under RH, an orthonormal basis in `K(Theta)` indexed by real zero ordinates | This is the first load-bearing positivity-transport machinery in the theorem proof and explicitly assumes RH |
| C2 | Expansion of `G_n` in that basis and Parseval-type norm calculation in the proof of Theorem 1.1 | `RH_CONDITIONAL` | Converts the model-space expansion into the norm identity | The calculation inherits Proposition 3.2's RH assumption; ordinary Parseval cannot be detached from the conditional basis/completeness statement |
| R2 | Theorem 1.1, all `n`: `lambda_n=(2 pi)^(-1)||G_n||_2^2` | `RH_EQUIVALENT` | Exact faithfulness, hence Li positivity | This is the root-coupled bridge itself, not a cheaper lemma |
| O1 | Section 4.1 discussion of the unconditional/false-RH relation | `SOURCE_OPEN` | Suzuki identifies concrete difficulty in relating `lambda_n` and `G_n` without RH; the displayed integrals lead to vertical-line expressions involving `xi+xi'` and off-line zeros | The paper supplies no replacement unconditional identity or sign theorem; zeros of `xi+xi'` become an unresolved coordinate rather than a solved bridge |

## Counterexample-first / hostile checks

1. **Positive-surrogate check.** `P_n>=0` is automatic from U3/U4. If that alone carried Li-sign authority, Theorem 1.1 would be unnecessary; the source instead states the all-index equality as equivalent to RH. Therefore a proposal of the form “construct a positive `P_n` and identify it heuristically with `lambda_n`” fails at the faithfulness edge.
2. **Conditional-Parseval check.** The norm calculation is not licensed by generic Parseval alone. The relevant orthonormal basis/completeness statement is supplied in Proposition 3.2 under RH, after Proposition 3.1 places the inner-function coordinate at RH-equivalent strength.
3. **Defect-relabeling check.** “Prove `D_n=0` for every `n`” is exactly the all-index norm identity and therefore does not atomize the root obstruction.
4. **Finite-computation check.** Numerical agreement for finitely many `n` cannot repair an all-index faithfulness gap; the prior `RH-ANA-001` finite-prefix falsifier remains the registered warning.
5. **Source-open check.** Section 4.1 is evidence that the author does not supply an unconditional bridge; it is not evidence that such a bridge is mathematically impossible.

## Result

`NO_STRICTLY_WEAKER_BRIDGE_EXPOSED_IN_AUDITED_SUZUKI_SOURCE`.

This means exactly: within the audited source dependency chain, the first mechanism that actually transports the unconditional positive norm to the Li coefficients passes through RH-conditional / RH-equivalent model-space structure. Propositions 2.1 and 2.2 do not, by themselves, expose a source-proved defect identity, one-sided inequality, orthogonality correction, or other exact sub-obligation that is known to be strictly weaker than RH.

It does **not** mean that no new theorem about `G_n`, `xi+xi'`, a different norm, or a later representation can exist. The negative result is route-local and source-bounded.

## Competing diagnoses

- **D1 — root-equivalent transport is intrinsic to this representation.** If this is correct, further norm/probability/operator rewritings that retain the same faithfulness edge are a saturated family and should not be repeated.
- **D2 — a weaker bridge exists but is missing from the source.** Section 4.1 suggests the unresolved `xi+xi'` zero geometry or a non-orthogonal expansion as possible coordinates, but no theorem is currently registered. This remains a hypothesis, not a diagnosis with authority.
- **D3 — the useful all-index coordinate lies elsewhere.** The Bombieri–Lagarias prime/archimedean formula or a Lagarias–Voros global growth exclusion may expose a smaller uniformity obligation than the norm route.

The v3 failure record therefore remains `OBSERVED_ONLY`; this cycle does not promote D1, D2 or D3 to a reusable obstruction theorem.

## Representation rotation

The highest-information next move is not another positive norm. Open `RH-ANA-003` as `CONTEXT_REQUIRED` and localize the exact prime/archimedean cancellation and uniform-tail coordinate in an arithmetic/explicit-formula representation of `lambda_n`.

Before any `RH-ANA-003` candidate, freeze a fresh context fiber, equivalent/near-solved analogues, method-transfer/disanalogy matrix, structural analogy, same-context expert cell, dual success/failure memory review and hash-chained pre-candidate trace. The first hostile test must reject any finite prime truncation or termwise-positivity story that lacks a rigorous all-`n` remainder theorem.
