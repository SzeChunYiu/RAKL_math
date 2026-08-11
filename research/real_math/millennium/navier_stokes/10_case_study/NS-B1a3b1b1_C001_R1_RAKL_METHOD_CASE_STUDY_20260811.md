# RAKL_METHOD_CASE_STUDY — NS-B1a3b1b1 C001 R1

Authority: `PROPOSAL_SHADOW_CASE_STUDY / NO_THEOREM_OR_ROOT_AUTHORITY`.

## Atom / problem signature

`NS-B1a3b1b1`: determine whether the one-center high-vorticity containment used by Grujić v2 is genuinely required by the localized commutator/De Giorgi consumer, or whether a uniformly bounded finite-center cover preserves the relevant restricted weak-Lorentz QoI.

## Actual fibre consulted

- CURRENT RAKL `main` at `f224d91d9fbd2844a89921ca4a30b77a7954ecd2`: version manifest, `method_specs.py`, and `ARCHITECTURE.md` v3 substrate/context-lift rules.
- RAKL_math canonical `main` at `47f56df0492339097a651d40b6c7289c4e2d4034` plus stacked parent PR #149 head `e0bcf0fd99a5587d303a9fd407f89d5505b1beb4`.
- Prior morphology episode/failure/obstruction from `NS-B1a3b1b` and the profile-leakage/local-global failures from `NS-B1a3`.
- PR #131 was retrieved as saturation evidence but rejected as theorem authority because it remains open/noncanonical.
- Primary literature: Grujić arXiv:2607.08866v2 Definition 2.1, Theorem 4.1 and equations (23)-(25); Albritton–Barker arXiv:1811.00502v2; Barker arXiv:2111.14776v2 as a finite-singular-point structural analogue with an explicit DifferenceWitness.

Fibre snapshot hash: `sha256:a9825cb4c0cef189694a6257e4366fb4959f3d5cba3b9200afa802b20c569f4a`.

## Research method and decision policy

The cycle used `experience-conditioned route rotation -> source-signature type check -> typed context-lift review -> counterexample-first multiplicity falsifier -> scoped proof validation`. The previous two-core morphology episode changed the **priority** of search: rather than immediately attempt the much harder PDE theorem “finite I selects a unique core,” the cycle audited the exact downstream quantity consumed by equations (23)-(25). No causal counterfactual is claimed because no pre-memory ranking was prospectively frozen.

## Operators / motifs tried

1. `CL-NS-B1a3b1b1-GRUJIC-FINITE-CENTER-R1`: one-ball to bounded-finite-union context lift.
2. Distribution-function union estimate in weak `L^{3/2}`.
3. Translation-covariance audit of the localized Calderón–Zygmund/BMO proof.
4. Counterexample harness for multiplicity: disjoint equal profiles reject an `N`-independent union constant.
5. `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` reused only as a producer/consumer type-check operation.
6. Strategy motif: `relax-consumer-before-strengthening-producer`.

## What worked

The source audit exposed that the one-center morphology is used at the relevant energy interface to obtain smallness of the restricted stretching norm on `A_lambda`. The localized commutator estimate is translation-covariant, so it applies with the same global-norm constant on each translated small ball. Summing distribution functions over at most `N0` balls gives the explicit weak-Lorentz loss `N0^(2/3)`. Because `R <= C lambda^-1/2`, this yields `O(N0^(2/3)/log lambda)`, which still vanishes for fixed `N0` and therefore retains viscous absorption in equations (24)-(25). This narrows the consumer morphology requirement from unique center to bounded multiplicity at the scoped interface.

## What failed / remained open

The cycle did **not** produce an equation-specific map from Albritton–Barker finite `I` to a bounded-multiplicity shrinking cover. It also did not produce the consumer's global vorticity weak-`L^{3/2}` or vorticity-direction log-BMO assumptions, nor close the ancient-solution/pre-singularity state-space bridge. These are **local-to-global / producer-gluing failures**, not failures of the finite-union analytic lemma. Type II is untouched.

The finite-singular-point theorem of Barker 2111.14776 was **rejected as a direct transfer**: its global velocity `L^{3,infinity}` hypothesis, terminal singular-point conclusion, state variable, and missing log-BMO direction output differ materially from the active producer/consumer interface.

## Failure category

- local mathematics: `NONE_FOR_SCOPED_LEMMA`;
- representation: previous one-center representation was unnecessarily rigid for this QoI; successfully relaxed;
- retrieval: no blocking failure observed;
- decomposition: successful narrowing to the exact restricted-norm consumer;
- verification: analytic distribution proof + source-level interface audit completed; repository/CI is artifact assurance only;
- local-to-global/gluing: `OPEN`, including bounded-cover production, global Lorentz/direction production, far-field/state-space interfaces;
- source: no source currently selected proves the producer obligations;
- tooling/meta-policy: no framework defect identified in this cycle.

## Episode -> diagnosis -> obstruction / lesson separation

- Episode: `EP-NS-B1a3b1b1-C001-R1-20260811` stores the immutable attempt/outcome evidence.
- Diagnosis: `D-NS-B1a3b1b1-ONE-CENTER-IS-STRONGER-THAN-LOCAL-CONSUMER-NEEDS` explains why the prior obstruction was over-specific at this interface.
- Reusable obstruction: `O-NS-B1a3b1b1-BOUNDED-MULTIPLICITY-COVER-PRODUCER` records the remaining producer boundary.
- Candidate lesson: `L-NS-B1a3b1b1-RELAX-CONSUMER-BEFORE-PROVING-UNIQUE-CORE` is proposal/shadow and requires applicability/DifferenceWitness checks on reuse.

No derived memory replaces the episode evidence.

## Seven saturation axes

- `KNOWLEDGE`: REOPENED — exact source-use of morphology in equation (25) retained.
- `OPERATOR`: REOPENED — finite-union context-lift operator retained.
- `EXPERIENCE_PATTERN`: REOPENED — a prior multi-core failure redirected to consumer relaxation.
- `OBSTRUCTION`: REOPENED/NARROWED — unique-core producer obstruction replaced by bounded-multiplicity cover producer obstruction at this interface.
- `RELATION`: REOPENED — one-center and finite-center contexts are related by quantified QoI preservation.
- `PATH`: REOPENED — bounded-multiplicity Type-I concentration route becomes a new child path.
- `META_METHOD`: FLATTENED — no RAKL method change proposed.

## Novelty class

`REPRESENTATION_NOVEL_SHADOW`, meaning a retained RAKL case-study representation/context-lift result. This is **not** a claim of novelty in the mathematical literature.

## RAKL v3 feature impact

The most useful v3 feature was the typed **context-lift review** combined with immutable TaskEpisode evidence and separate obstruction/lesson memory. It prevented the system from treating the previous failure of unique-center inference as a reason to abandon the entire conditional-regularity consumer. Experience altered search priority only; source/proof evidence supplied the scoped authority.

## Framework-improvement hypothesis

No framework defect is warranted from this cycle. A possible future benchmark question, not a proposed framework change, is whether `ContextLiftRecord` telemetry should expose a canonical quantitative `loss_function` field (here `N^(2/3)`) so Paper 5 can compare how often context lifts preserve a QoI with controlled degradation. This remains a hypothesis only; no RAKL issue is opened because the current proposal/shadow record can encode the loss without weakening gates.

## Next action

Search current primary literature for equation-specific Type-I concentration results that can produce a **uniformly bounded multiplicity** of `O(lambda^-1/2)` high-vorticity cores under assumptions genuinely available from the finite-`I` producer. Every candidate must carry a DifferenceWitness. If no compatible producer exists after bounded search, rotate to a consumer whose source family tolerates multi-profile ancient limits. Root remains `OPEN_NO_SOLUTION_CERTIFICATE`, with independent mathematical review `0/3`.
