# RAKL_METHOD_CASE_STUDY — P-vs-NP closure activation congruence

**Episode:** `episode-shadow::pnp-o9d12a2a1a1a-activation-congruence-20260811`  
**Authority:** proposal/shadow research-method evidence only.

## Method used

The cycle used a deliberately cheap sequence:

`source semantics -> coarse projection -> hostile counterexample -> refined projection -> congruence proof -> route pruning`

The target was not to invent a lower-bound invariant. It was to ask whether the extra apparent
state in the source-defined Theorem-24 closure carries independent witness-local information.

## What worked

- Returning to the exact source recurrence prevented a generic hierarchy from becoming the
  next default move.
- Counterexample-first testing immediately showed that "which rules fire at round zero" is
  too coarse.
- Refining to individual antecedent membership exposed a deterministic monotone recurrence.
- The congruence test killed an entire representation-level search branch before a candidate
  score or theorem was spent.
- Prior failures were used as routing constraints rather than blacklists: C025 warned about
  first-order collapse; XM004 warned that raw closure volume is unfaithful.

## What failed

The representation hypothesis failed, not the source mathematics.

`G_w(Lambda)` is richer as a raw family of subsets, but its **rule-activation computation**
for fixed `Lambda` is determined by the initial antecedent-membership projection plus the
fixed containment matrix. The extra raw state has no established bridge to the root
cover-complexity coordinate.

Failure category:

`REPRESENTATION -> ROOT_COORDINATE / GLUING_BRIDGE FAILURE`

not:

`MATHEMATICAL CONTRADICTION` or `P-vs-NP ROUTE IMPOSSIBILITY`.

## v3 features that helped

- **TaskEpisode discipline:** the result is stored as retrospective experience instead of
  being backfilled into a fake pre-candidate chronology.
- **Episode -> diagnosis -> lesson separation:** the observation (activation compresses),
  diagnosis (representation/root-coordinate mismatch), and advisory lesson (projection
  before score) are separate objects.
- **Failure-aware routing:** C025 and XM004 changed the action selected before any new
  candidate.
- **Vector saturation:** `RELATION` and `OBSTRUCTION` gained retained novelty while the
  current `PATH` was pruned; the system did not call the whole programme saturated.
- **Novelty metrology:** the root remains `UNRESOLVED`; the local task required a new
  representation coordinate but creates no mathematical novelty claim.

## v3 feature still missing

The current core `TaskEpisode` records `fibre_snapshot_hash`, `operator_ids`,
`action_trace`, observations, verification IDs, outcome, residual, evidence and cost.
That is enough to preserve an episode, but not enough for a longitudinal study of **how**
research decisions were made.

This run had to add application-local fields for:

- exact fibre items actually consulted;
- prior tools/failures that changed routing;
- retrieved-but-rejected items and rejection reasons;
- alternative operators/motifs considered;
- the explicit search-policy choice;
- mathematical-vs-retrieval-vs-representation-vs-verification failure category;
- gluing/bridge status;
- saturation-axis deltas;
- local structural-novelty class;
- next-action atomization.

Leaving these only inside free-text `action_trace` would make cross-agent method analysis
fragile and hard to benchmark.

## Framework improvement hypothesis

Add a proposal-only, content-bound `MethodTelemetry` object (or typed extension to
`TaskEpisode`) whose fields bind the actual fibre manifest, selected/rejected memory and
operator IDs, decision-policy metadata, failure-class taxonomy, gluing status, saturation
delta, novelty metrology and next-action pointer.

This should complement, not replace, framework issue #119:

- #119 asks **what search universe was covered** before no-match/completeness claims;
- this gap asks **what the agent actually used and rejected** after retrieval and why the
  resulting action was chosen.

### Expected benefit

Prospective telemetry should make it possible to measure repeat-failure rate, retrieval
misses, method-family fixation, representation churn, candidate spend per residual
contraction, and cross-domain strategy-motif transfer without reconstructing decisions from
prose.

### Possible regression

Overly detailed telemetry can increase prompt/log cost, encourage performative bookkeeping,
or freeze an impoverished taxonomy that misses genuinely new research behavior.

### Cheapest benchmark

On matched research atoms, compare:

1. current `TaskEpisode` + free-text trace; and
2. typed method telemetry.

Blind the downstream case-study evaluator to raw prose and ask it to reconstruct:

- which prior experience changed routing;
- which alternatives were rejected and why;
- the failure category;
- the saturation axes reopened;
- the next-action rationale.

The typed variant should improve reconstruction accuracy and cross-episode comparability
without increasing false authority or materially worsening task performance.
