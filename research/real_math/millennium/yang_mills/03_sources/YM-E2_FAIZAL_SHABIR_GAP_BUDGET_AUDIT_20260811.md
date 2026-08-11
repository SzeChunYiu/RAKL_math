# YM-E2 — Faizal–Shabir 2026 spectral-gap defect-budget audit

**Date:** 2026-08-11  
**Root:** `SzeChunYiu/RAKL_math#5`  
**Framework read first:** `SzeChunYiu/RAKL@decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8`  
**Application base:** `SzeChunYiu/RAKL_math@5d6bdc6f566921f51a375fdc2e8035123cf4830c`  
**Authority:** `RETROSPECTIVE_PRIMARY_SOURCE_ROUTE_DIAGNOSTIC / V3_SHADOW_EPISODE / NO_THEOREM_CANDIDATE / ROOT_AUTHORITY_NONE`

## Why this source was selected

Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang–Mills Theory With Mass Gap and Confinement*, Fortschritte der Physik 74(4), e70097 (2026), DOI `10.1002/prop.70097`; preprint `arXiv:2606.19362`.

The paper makes a direct full-scope constructive claim: reflection-positive lattice input, multiscale RG, continuum OS reconstruction, a positive spectral gap, confinement, universality, and weak-coupling/asymptotic-freedom compatibility. Because this directly intersects the Clay root rather than serving merely as an analogy, the cheapest high-information action is to audit one load-bearing quantitative implication before attempting a page-by-page global review.

## Chronology boundary

The source defect below was noticed during source reading **before** a fresh strict RAKL pre-candidate packet for this source-audit atom was frozen. It therefore receives no prospective/pre-candidate credit. Under RAKL v3 it is preserved as a retrospective TaskEpisode-style learning record and scoped failure diagnosis. It may change search priority but cannot mint theorem, proof, novelty, tool, gluing, or root authority.

## Exact source implication under audit

### Theorem 11.1

The source's spectral-gap theorem assumes an initial exponential-clustering scale with `m_* > 0` and an RG interlacing estimate

`T_(k+1) >= Pi_k T_k Pi_k - R_k`, with `R_k >= 0`, `||R_k|| <= epsilon_k`,

together with

`sum_k epsilon_k < infinity`.

It then concludes that the reconstructed continuum Hamiltonian has a strictly positive spectral gap, and in particular a lower bound proportional to the initial mass scale.

### Proposition 5.5

The source establishes a geometric defect estimate

`epsilon_k <= C theta^k`, `0 < theta < 1`,

hence `sum_k epsilon_k < infinity`.

### Corollary D.5

The appendix states that if

`Delta_(0,L) >= delta_0 > 0`,
`Delta_(k+1,L) >= Delta_(k,L) - epsilon_k`,
`epsilon_k >= 0`,
and `sum_k epsilon_k < infinity`,

then

`inf_L Delta_(n,L) >= delta_0 - sum_(k<n) epsilon_k >= delta_0 - sum_k epsilon_k =: delta_* > 0`.

The proof, however, explicitly invokes the stronger condition

`sum_k epsilon_k < delta_0`

and says this is guaranteed in the construction by defect summability with sufficiently large block factor.

## Cheapest falsifier

Pure summability does not imply the needed relative smallness.

Take

`delta_0 = 1`,
`epsilon_0 = 0.6`,
`epsilon_1 = 0.6`,
and `epsilon_k = 0` for `k >= 2`.

Then `epsilon_k >= 0` and `sum epsilon_k = 1.2 < infinity`, but

`delta_0 - sum epsilon_k = -0.2`.

Thus the abstract hypotheses stated in Corollary D.5 are insufficient to yield `delta_* > 0`. The same logical issue is visible in Theorem 11.1 if its positive-gap conclusion relies only on additive interlacing errors plus summability.

This does **not** show that the concrete Faizal–Shabir construction cannot satisfy the stronger inequality. It isolates the exact missing bridge: a quantitative proof that the concrete total defect budget is smaller than the initial gap.

## Bounded source search for the missing bridge

The bounded audit located Proposition 5.5's geometric estimate `epsilon_k <= C theta^k`, which gives

`sum epsilon_k <= C/(1-theta)`.

The source states that `C` and `theta` depend on the admissible coarse-graining scheme, including the finite-range decomposition, blocking factor, and collar decay. In the inspected theorem statements, however, no explicit inequality was located that binds

`C/(1-theta) < delta_0`

or otherwise proves the total error budget is smaller than the strong-coupling gap. The phrase “guaranteed ... with sufficiently large block factor” appears in the proof of Corollary D.5, but the relative-budget estimate itself is the new source obligation.

The correct follow-up is therefore not to declare the paper false. It is to require an exact source-bound constant audit.

## Expert cell

Six same-context roles were delegated against the same frozen source pages. These are not independent reviews.

1. **Constructive QFT / OS specialist.** Checked root relevance. Vote: `ACCEPT_ROUTE_RELEVANCE`; a scale-uniform positive transfer/OS gap is load-bearing for the claimed continuum mass gap, but this audit does not assess the rest of the OS construction.
2. **Operator / spectral specialist.** Re-derived the telescoping inequality. Vote: `ACCEPT_LOGICAL_GAP`; additive gap loss needs a positive residual budget, not merely a finite total loss.
3. **Constructive RG / FRD specialist.** Checked Proposition 5.5's role. Vote: `REVISE_SOURCE_BRIDGE`; geometric summability is useful, but the ratio of its total constant budget to the initial strong-coupling gap must be explicit.
4. **Adversarial mathematical-physics reviewer.** Supplied the finite summable countermodel above. Vote: `BLOCK_AS_STATED`; the stated abstract Corollary D.5 hypotheses do not imply its positive conclusion.
5. **Formal assurance / chronology reviewer.** Vote: `RETROSPECTIVE_ONLY`; preserve the observation without fabricating a pre-candidate trace or converting publication status into mathematical authority.
6. **RAKL v3 method-learning reviewer.** Vote: `PRESERVE_AS_GLUE_FAILURE`; this is a clean example of `local success != global solution`: summable local RG defects are not enough unless the gluing map preserves the root-critical positive-gap coordinate quantitatively.

Consensus:

`SOURCE_ROUTE_IMPORTANT / STATED_RELATIVE_BUDGET_INCOMPLETE / EXACT_REPAIR_OBLIGATION_OPEN / NO_ROOT_AUTHORITY`.

## Episode -> diagnosis -> obstruction/lesson

- **Observed episode:** a fresh full-solution source was audited at its gap-persistence interface.
- **Diagnosis:** the stated summability condition is weaker than the relative defect-budget inequality used in the proof.
- **Scoped obstruction:** `F-YM-E2-SUMMABLE-DEFECT-POSITIVE-GAP-BUDGET`.
- **Candidate lesson (shadow only):** whenever a positive root-critical quantity is transported through additive losses, RAKL should distinguish *summability* from *budget dominance* and require an explicit residual-margin certificate.

The lesson is not promoted to a reusable framework tool here.

## Local mathematics versus gluing

The local telescoping estimate is straightforward:

`Delta_n >= Delta_0 - sum_(k<n) epsilon_k`.

The open issue is the **gluing/transport margin**:

`Delta_0 - sum_k epsilon_k > 0`.

This is not a semantic detail. Positivity of the final root-critical coordinate depends on a quantitative margin that must survive all scales and relevant limits.

## Saturation vector

- `KNOWLEDGE`: reopened by a fresh 2026 root-claim source.
- `OPERATOR`: not flat; exact constant audit remains available.
- `EXPERIENCE_PATTERN`: reopened by the recurring surrogate/root-bridge pattern.
- `OBSTRUCTION`: reopened at the relative defect-budget inequality.
- `RELATION`: reopened by distinguishing `summable` from `small relative to initial margin`.
- `PATH`: reopened toward a quantitative `C, theta, delta_0` dependence audit.
- `META_METHOD`: reopened by v3 retrospective episode capture and gluing-failure typing.

## Next fresh atom

`YM-E2a — RELATIVE_DEFECT_BUDGET_CERTIFICATE`

Freeze a new strict pre-candidate packet **before** evaluating it. Exact question:

> In the concrete admissible Faizal–Shabir RG construction, can one prove from source-defined constants that the total transfer-gap defect budget is strictly smaller than the initial strong-coupling gap, uniformly in volume and along the continuum trajectory?

The minimum certificate must expose:

1. the exact strong-coupling lower bound `delta_0`;
2. exact `C` and `theta` dependence on block factor, coupling, FRD range and collar choices;
3. a proved inequality `C/(1-theta) < delta_0` or a sharper summation bound;
4. compatibility with the fixed-physical-time Hamiltonian conversion;
5. uniformity required for thermodynamic and continuum limits.

If the source supplies this, the route survives this audit and the next load-bearing bridge should be tested. If it does not, record `RELATIVE_DEFECT_BUDGET_UNPROVED` at source-route authority only.

## RAKL_METHOD_CASE_STUDY

**Method used.** Root-coordinate-first source audit: instead of reading hundreds of pages linearly, identify a theorem whose conclusion is necessary for the claimed root, compare stated hypotheses with proof-used hypotheses, then attack the cheapest implication.

**What worked.** A four-page targeted audit contracted a very large source claim into one quantitative inequality. Counterexample-first checking immediately separated “finite accumulated error” from “error small enough to preserve a positive margin.”

**What failed.** The source's local-to-global argument, as stated, compresses two distinct conditions—summability and relative smallness—into one. The process failure is primarily **bridge/gluing specification**, not a failure of the elementary telescoping calculation.

**v3 feature used.** Immutable retrospective episode semantics prevented us from pretending the source finding had been preregistered. Fibre bookkeeping separated selected prior failure memories from structurally different rejected ones. Saturation typing exposed a concrete reopened obstruction rather than labeling the route “stuck.”

**Framework-improvement hypothesis.** Add a proposal-only `MARGIN_PRESERVATION_AUDIT` to the problem-fibre/gluing layer: whenever a local-to-global edge transports a positive or nonzero root-critical coordinate through additive/multiplicative losses, require a machine-readable margin certificate of the form `initial_margin - total_loss > 0` (or the appropriate invariant analogue). Benchmark it first on this Yang–Mills source audit and on known safe/unsafe telescoping toy worlds.

No RAKL framework mutation is authorized by this single episode.
