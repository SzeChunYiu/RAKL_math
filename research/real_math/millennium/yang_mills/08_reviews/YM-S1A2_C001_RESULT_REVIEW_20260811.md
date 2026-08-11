# YM-S1a2-C001 same-context result review — 2026-08-11

**Authority:** `SAME_CONTEXT_INTERNAL_REVIEW / NOT_INDEPENDENT / NO_NOVELTY / ROOT_AUTHORITY_NONE`

The seven pre-candidate lenses re-read the scoped composition after proposal. The fixed-a **transfer-spectrum** core survives, but two target-facing statement repairs are required before treating the candidate as the preferred local result.

## R1 — beta=0 and ordinary logarithmic Hamiltonian endpoint

**Severity:** blocking for the unconditional Hamiltonian clause, not for transfer-spectrum exclusion.

V1 states `0 <= beta < 1/48` and then treats `H_a=-(1/a)log T` as an ordinary Hamiltonian on the infinite-volume reconstructed space. At `beta=0` the temporal transfer can collapse excited directions, so strict injectivity/ordinary logarithm is not source-bound by the cited finite positive-coupling construction. More generally, an infinite-volume positive transfer operator may acquire zero in its spectrum even if every finite-volume transfer matrix is strictly positive.

**Required repair.** Narrow the prospective Wilson-coupling statement to `0 < beta < 1/48`. State the unconditional result as the transfer-spectrum bound. State the Hamiltonian lower bound only when the reconstructed one-step transfer is independently known to be `exp(-aH_a)` with the required logarithmic functional calculus/injectivity. Do not interpret zero transfer spectrum as an ordinary finite Hamiltonian eigenvalue.

## R2 — one-step transfer positivity needs its own weak-limit handoff

**Severity:** major and load-bearing for use of the parent positive-operator lemma.

V1 correctly passes the OS norm form `mu(theta F F)>=0` to the SZZ limit, but then says the one-step transfer operator is positive without spelling out the analogous local limit. Self-adjointness alone is insufficient.

**Required repair.** For each local source `F`, use the finite positive transfer matrix to obtain the one-step form `<[F],T_L[F]> >=0`. By the reconstruction identity this is another bounded local Euclidean expectation. Pass that form through the same SZZ local weak limit. Density then extends nonnegativity from local source images to the infinite-volume one-step transfer operator. This gives operator positivity without assuming strong operator convergence of `T_L`.

## R3 — source class and common exponent

**Verdict:** pass.

SZZ Corollary 1.6 covers all smooth cylinder functions and uses one exponent `c_N` independent of source identity; only finite prefactors depend on supports/norms. The local gauge-invariant OS generating algebra is contained in that larger class, and orthogonal projection of its dense span is dense in `Omega^perp`. The old hidden-source and nonuniform-rate falsifiers are therefore actually discharged by named assumptions rather than ignored.

## R4 — support geometry

**Verdict:** pass at asymptotic level.

For each fixed finite source, reflection and n-step time translation change the nearest support distance by `n+O_F(1)`. The exact additive convention is irrelevant to the nth-root rate but should not be represented as an exact equality without a chosen reflection plane/source slab convention.

## R5 — scope and novelty

**Verdict:** pass only under narrow labels.

Even after repair this is a fixed-lattice strong-coupling `SU(N)` transfer-spectrum composition from published ingredients. It closes neither the strong-to-weak/RG bridge nor physical `a->0` scaling nor continuum spectral identification. No bounded novelty search or independent mathematical review has been performed. `PROVISIONAL_RAKL_TRIVIAL` remains the correct ancestry label and the Clay root remains open.

## R6 — framework/provenance

Current reusable-framework semantics are `RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`, including protected v3 authority receipts. The application repository remains pinned to older framework commit `15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`. This branch can preserve research/proposal evidence under current-main rules, but no exact-current-framework integration or promotion credit is available until a separate pin update is reviewed and the complete application suite passes.

## Cell disposition

`V1_TRANSFER_CORE_SUPPORTED / V1_HAMILTONIAN_SCOPE_REVISE / ONE_STEP_POSITIVITY_HANDOFF_MUST_BE_EXPLICIT / CREATE_V2_SUCCESSOR / NO_AUTHORITY_ESCALATION`.

Do not mutate V1. Preserve it as review history and create a V2 successor that contains the narrower beta scope, explicit one-step positivity limit, and conditional Hamiltonian clause.