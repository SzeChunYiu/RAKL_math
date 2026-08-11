# RAKL_METHOD_CASE_STUDY — NS-B2a Type-II Euler-limit cycle

**Case-study authority:** proposal-only meta-evidence.  
**Framework inspected:** current `SzeChunYiu/RAKL@decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8`.

## Research method used

The cycle followed this observable operator sequence:

1. **fresh framework/source refresh** — read current RAKL v3 semantics and current RAKL_math state;
2. **source-bound equation classification** — identify that Seregin's limiting equation is Euler rather than Navier-Stokes;
3. **problem-fibre retrieval** — retrieve the merged pressure-summability failure, a pending structurally similar Type-I shell failure, and prior Euler-scaling sources;
4. **rejection before transfer** — reject Navier-Stokes backward uniqueness as a wrong-equation closure and reject the pending PR as authority;
5. **DifferenceWitness** — transfer only the abstract critical-scale diagnostic, not the Type-I theorem/object;
6. **negative-first scaling discriminator** — compute the homogeneity of every canonical absolute cutoff term before inventing a rigidity theorem;
7. **residual sharpening** — separate local control from the far-field/gluing interface and open a smaller child.

This sequence reduced a vague “find an Euler Liouville theorem” search into the more specific interface problem “produce tail/sign information that is absent from the critical absolute bounds.”

## What worked

- **Equation-type classification prevented an invalid method transfer.** Had the cycle treated the limit as Navier-Stokes, backward uniqueness would have been a false downstream premise.
- **Failure retrieval reduced duplicate work.** The merged pressure-summability result immediately removed raw pressure divergence from consideration.
- **Contrastive retrieval was useful even without authority transfer.** Pending PR #54 suggested the correct hostile question—whether normalization leaves only `O(1)` per scale—but the present Euler result was independently re-derived.
- **Negative-first analysis gave high epistemic contraction.** A short scaling audit pruned an entire naive absolute-flux route before theorem invention.
- **v3 local-to-global language clarified the actual gap.** Seregin's local section is not the missing theorem; the missing object is the tail/gluing certificate.

## What failed

### Mathematical / representation failure

The representation
`absolute local-energy cutoff magnitude`
as a proxy for
`no incoming energy at infinity`
is not contracting in the `F=1` class. Critical homogeneity leaves only an `O(1)` normalized estimate.

### Process / chronology failure

The useful discriminator was recognized before a fresh strict `NS-B2a` pre-action context/fibre was frozen. The result therefore cannot receive prospective candidate credit. This is not an isolated pattern in the application history: prior Navier-Stokes chronology repairs and other retrospective route audits show that valuable observations can precede the formal freeze.

### Retrieval boundary

The pending Type-I PR #54 was relevant but noncanonical. A retrieval system that does not distinguish `relevant` from `authority-bearing` could silently contaminate the new episode.

## v3 features used

- `TaskEpisode` semantics: preserve the actual cycle as an immutable outcome-linked episode.
- problem-conditioned fibre: explicitly record selected, rejected, and noncanonical retrieved items.
- episode -> diagnosis -> obstruction separation: project only an `OBSERVED_ONLY` failure.
- local-section/gluing distinction: classify tail inheritance and Euler rigidity as separate global interfaces.
- vector saturation: record retained novelty and reopened axes rather than calling the whole route exhausted.
- branching residual: open a new child rather than rewriting the failed route into a successful story.

## Saturation interpretation

This cycle does **not** establish bounded saturation of the Type-II programme.

- `KNOWLEDGE`: reopened by the fresh 2026 Seregin source/interface.
- `OPERATOR`: no new mathematical operator retained.
- `EXPERIENCE_PATTERN`: retained novelty because the critical-absolute-bound failure recurs across a mathematically disanalogous Euler limit.
- `OBSTRUCTION`: reopened and sharpened to tail/no-incoming-flux inheritance.
- `RELATION`: retained a new relation between Type-I and Type-II critical-balance failures without theorem transfer.
- `PATH`: one path pruned; signed/tail/compactness paths remain open.
- `META_METHOD`: reopened by the chronology-capture defect.

## Novelty class

No new Navier-Stokes theorem is claimed. At the research-process level, the result is best classified as **TRANSFER/REPRESENTATION diagnostic**: a known critical-scaling idea is transferred across a DifferenceWitness to a new Euler-limit interface, where it rejects a representation of the missing root coordinate. This classification grants no mathematical novelty authority.

## Concrete framework-improvement hypothesis

### Hypothesis: automatic pre-action fibre receipt

**Target:** RAKL v3 driver/runtime around `compile_state_fibre()` / `record_task_episode()`.

**Problem observed:** a consequential discriminator can be executed before the agent freezes the exact retrieval universe, action choice and context. The later TaskEpisode is honest but retrospective; repeated chronology repairs waste effort and create authority risk.

**Proposed mechanism:** before any consequential operator executes, automatically persist a content-bound `PRE_ACTION_FIBRE_RECEIPT` containing:

- current problem atom/context identity;
- exact fibre snapshot hash;
- selected and rejected retrieval IDs with authority;
- chosen operator/action;
- predeclared discriminator/falsifier;
- current framework/application subject identities.

The post-action TaskEpisode must reference that receipt. If absent, the episode is automatically `RETROSPECTIVE_ONLY` and cannot satisfy prospective promotion gates.

**Expected benefit:** prevents backfilled preregistration, makes method telemetry comparable across agents, and separates “good idea discovered retrospectively” from “prospectively tested method.”

**Regression risk:** excessive ceremony/latency for cheap exploratory source checks, and false confidence if the receipt captures an incomplete retrieval universe.

**Cheapest discriminating benchmark:** on a matched set of source-audit/research atoms, compare agents with versus without automatic pre-action receipts. Measure (i) chronology violations, (ii) duplicated/repeated failures, (iii) retrieval omissions discovered post hoc, (iv) epistemic contraction per cycle, and (v) overhead. Promotion must remain disabled during the benchmark.

**Current status:** framework-improvement hypothesis only. This case study does not mutate RAKL or self-promote the proposal.
