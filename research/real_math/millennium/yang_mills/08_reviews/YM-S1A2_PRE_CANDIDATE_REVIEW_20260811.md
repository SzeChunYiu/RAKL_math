# YM-S1a2 same-context expert pre-candidate review — 2026-08-11

**Atom:** `YM-S1a2`  
**Context:** `sha256:89ee3e1d735f6b3e5be46a2acfa1914da01ac3dce52227f2d83cf9d3832f7144`  
**Framework inspected:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Authority:** `ROLE_SEPARATED_SAME_CONTEXT_REVIEW / NOT_INDEPENDENT / PRE_CANDIDATE / ROOT_AUTHORITY_NONE`

This review is a same-session expert cell. The roles are analytical lenses, not independent human reviewers. Disagreement and residual uncertainty are preserved.

## 1. Constructive lattice-QFT / OS lead

**Background/role.** Reflection positivity, Gibbs limits, OS reconstruction, lattice gauge measure scope.

**Evidence inspected.** Lüscher 1977 OS positive-time construction and transfer reconstruction; Osterwalder–Seiler 1978 physical-positivity abstract; SZZ Theorem 1.2 convergence of finite-volume Wilson measures to a unique infinite-volume measure.

**Finding.** The finite-to-infinite reflection-positivity handoff should be local: for a fixed bounded continuous positive-time cylinder `F`, the OS quadratic form is a local bounded continuous observable, so finite-volume nonnegativity passes to the weak limit. Because SZZ identify the whole sequence with one limit, no choice among phases remains inside their regime.

**Strongest objection.** Reflection positivity must be checked for the exact finite periodic Wilson measures and coupling convention used in the subsequence. SZZ permit `|beta|` in their stochastic bound, while the standard positive Wilson transfer route is naturally `beta >= 0`. Do not state a negative-beta transfer theorem without a separate character-expansion proof.

**Vote.** `ALLOW_NARROW_CANDIDATE` restricted to positive beta, fixed lattice spacing, and the exact SZZ group/range.

## 2. Transfer-matrix / spectral-theory lead

**Background/role.** Positive self-adjoint contractions, spectral measures, Hamiltonian functional calculus.

**Evidence inspected.** `YM-S1a1-C001-v2`; Lüscher Proposition 1 and the OS shift construction.

**Finding.** If the infinite-volume OS time-shift is positive and the centered source images are dense in `Omega^perp`, SZZ's source-independent exponent supplies exactly the common `q` required by the parent lemma. Source-dependent finite prefactors disappear under nth roots.

**Strongest objection.** Do not infer operator positivity merely from self-adjointness. The candidate must either bind positivity of the infinite-volume one-step transfer operator or weaken explicitly to a two-step positive operator and separate the Hamiltonian interpretation.

**Vote.** `ALLOW_NARROW_CANDIDATE_WITH_POSITIVITY_OBLIGATION`.

## 3. Strong-coupling stochastic-analysis lead

**Background/role.** SZZ measure, functional inequalities, covariance estimate and parameter dependence.

**Evidence inspected.** SZZ Assumption 1.1, Theorem 1.2, Corollary 1.6 and Corollary 4.11.

**Finding.** Corollary 1.6 is broader than a Wilson-loop-only estimate. It covers all smooth cylinder functions with one exponent `c_N` depending on `K_S,N,d`; only finite prefactors depend on source support/norms. This is exactly the common-rate property that the previous nonuniform-rate hostile world showed to be load-bearing.

**Strongest objection.** Their term "mass gap" is exponential Euclidean clustering. The paper does not itself identify `c_N` with the physical Hamiltonian spectrum. That bridge must come entirely from the OS/transfer construction, not from terminology.

**Vote.** `ALLOW_COMPOSITION_CANDIDATE`.

## 4. Gauge-invariant source-algebra lead

**Background/role.** Gauge-invariant local observables, OS quotient/completion, source completeness.

**Evidence inspected.** Lüscher's definition of the physical Hilbert space as the null quotient/completion of gauge-invariant positive-time observables; SZZ definition of smooth cylinder functions and explicit inclusion of Wilson loops/functions thereof.

**Finding.** The source-density obligation can be made constructive rather than imported from a separate spin-network theorem. The OS Hilbert is defined as the completion of the positive-time local gauge-invariant algebra. Its images are dense by construction. Centering via `P_exc = I - |Omega><Omega|` maps a dense set to a dense set in `Omega^perp`. Gauge-invariant local polynomials/Wilson-loop functions form smooth cylinders, so a dense generating subclass lies inside the SZZ covariance class.

**Strongest objection.** The exact positive-time algebra and its smooth/polynomial generating subclass must be stated consistently with the pure-gauge infinite-volume measure; do not claim that every SZZ cylinder is physical or gauge invariant.

**Vote.** `SOURCE_DENSITY_REPAIR_ACCEPTED_IN_SCOPED_ALGEBRA`.

## 5. Adversarial gluing / normalization lead

**Background/role.** Cheapest counterexamples, interface mismatch, units and hidden assumptions.

**Hostile tests.** Retained hidden-state source counterexample; dense-but-nonuniform `q_k -> 1`; negative-beta sentinel; Langevin-generator-versus-physical-transfer sentinel; continuum-scaling sentinel.

**Finding.** For a fixed source of temporal width `m`, reflection plus an `n`-step forward translate gives support separation `n + O_F(1)`, so the nth-root rate is unchanged. If the OS transfer moment is nonnegative, SZZ's one-sided covariance upper bound suffices.

**Strongest objection.** The word "gap" is overloaded four ways: Langevin spectral gap, Euclidean clustering rate, fixed-a physical transfer gap, and continuum Clay mass gap. The candidate must name only the third and explicitly deny the fourth.

**Vote.** `ALLOW_ONLY_WITH_FOUR_GAP_TYPES_SEPARATED`.

## 6. Formal assurance / provenance lead

**Background/role.** Chronology, framework pin, hashes, authority boundary.

**Evidence inspected.** Current RAKL main `bd1a2768...`, merged v3 authority hardening PR #121, RAKL_math pin file, PR #79 parent artifacts.

**Finding.** Current framework semantics are stricter than the RAKL_math submodule pin (`15f1c3affe...`). The cycle may follow current-main rules for proposal/shadow research, but it cannot claim a clean exact-current-framework application integration until the submodule/pin is reviewed, synchronized, and the complete application suite passes. PR #121 also means caller-provided v3 authority flags are no longer acceptable substitutes for content-bound attestations.

**Chronology correction.** A preliminary `YM-S1A2_RESEARCH_MEMORY_REVIEW_20260811.json` was committed before this expert review. It must not receive strict `EXPERIENCE_MEMORY_REVIEW` chronology credit. Freeze a successor memory review after this file and bind only the successor in the pre-candidate trace. Preserve the preliminary bytes as negative/process history.

**Vote.** `ALLOW_CANDIDATE_AFTER_MEMORY_V2_AND_TRACE_ONLY / INTEGRATION_AUTHORITY_BLOCKED_ON_PIN_SYNC`.

## 7. Novelty / research-value lead

**Background/role.** Prior-art risk, explanatory value, route selection.

**Finding.** The expected fixed-a theorem is a composition of standard OS reconstruction/transfer positivity, SZZ's published covariance estimate, and the elementary parent spectral lemma. It should be classified provisionally as `RAKL_TRIVIAL` or otherwise zero-invention/compositional unless a bounded novelty search finds a genuinely new theorem coordinate. Its research value is route closure and exact localization of the remaining G5-G7 interfaces, not theorem novelty.

**Strongest objection.** A correct recombination can still be scientifically useful, but must not be marketed as a new Yang–Mills mass-gap theorem.

**Vote.** `NO_NOVELTY_CLAIM / ALLOW_ROUTE_CLOSURE_CANDIDATE`.

## Cell synthesis

### Consensus

The current best next action is not to invent another spectral lemma. The source packet already appears sufficient to propose one narrow composition:

`positive-beta SZZ strong-coupling infinite-volume measure`
`+ weak-limit reflection positivity`
`+ OS transfer identity and dense centered gauge-invariant source algebra`
`+ SZZ common c_N exponent`
`+ YM-S1a1-C001-v2`
`=> fixed-lattice-spacing infinite-volume physical transfer spectral gap`.

### Candidate blockers before proposal

1. Freeze a successor dual-memory review **after** this expert review because the preliminary memory file was chronologically early.
2. Freeze a hash-chained pre-candidate trace in the required order.
3. Candidate scope must state `beta >= 0` within the SZZ strong-coupling range, fixed `a`, and SZZ's `SU(N)/SO(N)` groups.
4. Candidate must keep `G5`, `G6`, `G7`, continuum existence and the Clay root open.
5. Integration/promotion claims remain blocked until the stale RAKL_math framework pin is separately synchronized and the full application suite passes.

### Recommendation

`NEXT_STEP = PROPOSE_SCOPED_COMPOSITION_ONLY_AFTER_MEMORY_V2_AND_TRACE`.

No member of this cell grants independent-review, novelty, formal-proof, framework-promotion, continuum, or root authority.