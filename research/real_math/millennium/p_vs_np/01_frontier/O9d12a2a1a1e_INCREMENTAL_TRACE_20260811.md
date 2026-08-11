# O9d12a2a1a1e — base-normalized trace entropy: local accounting closes, target/cyclic gluing stays open

**Framework source of truth:** `SzeChunYiu/RAKL@f224d91d9fbd2844a89921ca4a30b77a7954ecd2`; canonical method manifest `3.0.0`.  
**Application main at cycle start:** `SzeChunYiu/RAKL_math@47f56df0492339097a651d40b6c7289c4e2d4034`.  
**Parent shadow evidence:** draft PR #128 at `ede7a19d8110e90a60e66d18f95237cfbbd4d1b4` (`O9d12a2a1a1d`).  
**Authority:** proposal/shadow local route evidence only. Root authority remains none.

## Exact atom

Let `Γ` be finite, `B` a base family, `H ⊇ B` a current family, and `A ⊆ Γ` a fixed target. Let `U(H)` denote finite union closure and

`T_A(H) = { C ∩ A : C ∈ U(H) }`.

The parent atom falsified *absolute* trace entropy because the free base can already shatter a target at zero counted intersection cost. The smallest surviving question is whether the base-normalized potential

`Φ_A(H;B) = log2 |T_A(H)| - log2 |T_A(B)|`

has a legal one-step marginal bound.

## Primary-source binding

Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033, 18 March 2025: `https://eccc.weizmann.ac.il/report/2025/033/`.

Section 2.5 defines cyclic discrete complexity by least-fixed-point evaluation of a syntactic sequence and defines cyclic intersection complexity by counting intersection operations in the syntax. Corollary 17 states, in the paper's notation, that ordinary intersection complexity is at most the square of cyclic intersection complexity. This cycle uses that source only for the model/transport boundary; the entropy lemma below is elementary and proved here.

A bounded ECCC/arXiv search through 11 August 2026 found no directly applicable follow-up that changes this specific cyclic-discrete-complexity accounting question. This is a bounded-search statement, not an absence theorem.

## Local lemma — exact one-added-set accounting

For every `D ⊆ Γ`,

`0 ≤ Φ_A(H ∪ {D};B) - Φ_A(H;B) ≤ 1`.

**Proof.** Every element of `U(H ∪ {D})` is either `C` or `C ∪ D` for some `C ∈ U(H)`. Hence every trace on `A` is either `X = C ∩ A` or `X ∪ (D ∩ A)`, with `X ∈ T_A(H)`. Therefore `|T_A(H ∪ {D})| ≤ 2 |T_A(H)|`. Monotonicity gives the lower inequality. Taking base-2 logarithms gives the claim. QED.

Thus an **acyclic** construction that introduces `k` charged intersection-result sets, with arbitrary free unions between them, can increase this normalized trace entropy by at most `k`.

### What this does not prove

A cyclic syntactic intersection coordinate is not simply an immutable set adjoined once: it is evaluated in a monotone fixed-point network. Therefore the lemma is **not** promoted to a direct `≤1` marginal theorem per cyclic intersection gate. The same-context cyclic-semantics review rejected that transport. Any use in the cyclic lane must go through a separately proved transport statement; the source's Corollary 17 supplies only the known quadratic acyclic/cyclic comparison.

## Counterexample-first gluing audit — target-adjoin invisibility

Assume `Γ ∈ U(B)`, as in the graph row/column base. Then for every `H ⊇ B`,

`T_A(H ∪ {A}) = T_A(H)`.

Indeed, a union using the newly adjoined `A` has trace `A`, but `A = Γ ∩ A` was already in `T_A(H)` because `Γ ∈ U(B)`. Thus the terminal presence of the target itself need not force *any* increase in `Φ_A`.

This is a **local-to-global/target-value gluing failure**, not a failure of the local marginal lemma. Any successful lower-bound coordinate now needs both: (1) a legal accounting law compatible with cyclic semantics; and (2) a target-forcing theorem showing that every relevant construction of an explicit hard graph must accumulate a large value before the terminal target appears.

## Same-context expert cell

Five role-separated passes were delegated; none receives independent-review credit.

- **Fusion/circuit-complexity specialist:** bound the claim to the graph/discrete-complexity lane and rejected any inference to unrestricted circuit lower bounds.
- **Extremal set-systems specialist:** proved the two-copy trace decomposition and the factor-2 cardinality bound.
- **Cyclic fixed-point specialist:** blocked the unsafe identification “one cyclic intersection gate = one immutable added set”; retained only the source-bounded acyclic/cyclic comparison.
- **Adversarial lower-bound/gluing specialist:** supplied the `Γ ∈ U(B)` target-adjoin invisibility control, separating local success from target-value failure.
- **Verification/metrology specialist:** checked exact atom/fibre binding, negative-history preservation, proposal-only authority, finite calibration scope, and metric non-escalation.

Consensus: the one-added-set/acyclic marginal law is closed. Disagreement/uncertainty remains entirely in cyclic transport and target forcing.

## Episode -> diagnosis -> proposal lesson

**Episode.** Base-normalized target-trace entropy is 1-Lipschitz under adjoining one arbitrary set, but the terminal target can be invisible.

**Diagnosis.** Normalization fixed the parent's zero-cost blow-up locally, yet it did not bind the state potential to the target. Moreover, direct cyclic gatewise transport would conflate immutable-set addition with fixed-point syntax.

**Proposal-only lesson/obstruction.** A lower-bound potential in this lane needs a *paired certificate*: local charged-operation Lipschitzness **and** a target-forcing invariant that survives cyclic semantics. Checking only one half should route the candidate to failure before hard-graph scoring.

Novelty class, if a protected gate later certifies retention: `compositional`. No novelty authority is claimed here.

## Verification

A pure finite enumerator exhaustively checked every set family, target, and added set for `|Γ|=3`: 16,384 marginal cases satisfy the factor-2 bound; 1,744 cases with `Γ ∈ U(H)` satisfy target-adjoin invisibility. This calibrates the implementation only; it is not the proof.

## Outcome / next atom

Local mathematical status: `SOLVED_PROPOSAL_SHADOW_ONE_ADDED_SET_ACYCLIC`.

Local-to-global gluing status: `OPEN`.

Residual signature: `PNP_INCREMENTAL_TRACE_TARGET_FORCE_AND_CYCLIC_TRANSPORT_MISSING`.

Next child atom: `O9d12a2a1a1f` — test whether a target-intrinsic **quotient of trace partitions** (not terminal target membership) can be forced large for every construction and whether its cyclic transport is better than the generic quadratic unfolding bound.

## Root status

`OPEN_NO_SOLUTION_CERTIFICATE`.

No explicit super-logarithmic graph cover lower bound, unrestricted circuit lower bound for an NP-complete language, proof of `P != NP`, formal certificate, novelty certificate, or independent mathematical review is produced.
