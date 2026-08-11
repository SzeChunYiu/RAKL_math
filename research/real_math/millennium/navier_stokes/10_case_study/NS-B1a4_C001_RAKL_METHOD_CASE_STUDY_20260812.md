# RAKL_METHOD_CASE_STUDY — NS-B1a4-C001

**Cycle:** `EP-NS-B1a4-C001-SIGNED-FLUX-20260812`  
**Framework:** `SzeChunYiu/RAKL@2f722d42db240538e1bdec146aebc7e9d5eeb8a6`; method `3.0.0`, package `0.1.0`  
**Application base:** `SzeChunYiu/RAKL_math@a7301f0f0e2cab2750ac6e923efe18b5750b5af6`  
**Authority:** proposal/shadow only; no root promotion.

## Atom / problem signature

`NS-B1a4`: determine whether the currently registered unsigned finite-`I` local-energy magnitudes `A+C+D+E`, standard suitable local-energy inequality, and pressure localization themselves contain enough signed information to support a one-sided fixed-region local-energy/no-recrossing law.

The exact Clay root remains open. Type-II is out of scope. The finite-`I` ancient/global rigidity interface is not silently inherited.

## Actual fibre consulted

Selected prior failures:
- `F-NS-B1a-C001-PRESSURE-SUMMABILITY`;
- `F-NS-B1a1-SCALE-NEUTRAL-LOCAL-ENERGY-LEDGER`;
- `F-NS-B1a3-LOCAL-GLOBAL-INTERFACE-MISMATCH`.

Retrieved but rejected:
- `F-NS-B1a3b-DERIVATIVE-LOSS-VORTICITY-DIRECTION` — vorticity derivative/topology issue, not energy-flux sign;
- `F-NS-B1a3b-NORMALIZATION-ZERO-INSTABILITY` — normalization-specific;
- `F-NS-B1a3b1-GLOBAL-CONSUMER-SIGNATURE-MISMATCH` — general gluing warning already represented more directly by `F-NS-B1a3-LOCAL-GLOBAL-INTERFACE-MISMATCH`.

Success-derived tool inventory: empty in the inspected Navier–Stokes application snapshot.  
Promoted motifs: none found.  
Cross-Millennium memory: not queried because same-problem scoped failures directly matched the residual; no applicability gain justified transfer risk.  
Missed relevant experience: `CANNOT_MEASURE` because there is no closed recall oracle.

## Expert cell

Seven same-context roles were frozen before verification: Type-I/ancient PDE; local energy/pressure; scaling/concentration compactness; rigidity/backward uniqueness; adversarial exact-solution construction; formal assurance/verifier trust; novelty/source boundary.

Consensus: run the issue-#173 pressure-free shear discriminator and keep the global finite-`I` DifferenceWitness explicit.

Preserved disagreement: the fixed-region falsifier does not rule out moving/profile-adapted regions, a new signed flux/correlation observable, almost-periodicity/minimality, or a stronger global trajectory theorem.

This expert cell is not independent peer review.

## Methods / operators / motifs tried

Applied method families:
1. counterexample-first exact-NSE calibration;
2. structural analogy from global energy dissipation to local energy, with boundary-flux disanalogy;
3. method-transfer audit from Albritton–Barker finite-`I` local-energy machinery;
4. pressure-mechanism audit conditioned on prior pressure-summability experience;
5. producer/consumer interface separation for local sign versus global ancient rigidity;
6. exact DifferenceWitness scope audit.

Unpromoted operator labels used in the TaskEpisode:
- `agent:counterexample-first`;
- `agent:exact-NSE-calibration`;
- `agent:DifferenceWitness-scope-audit`;
- `agent:local-vs-global-failure-separation`.

No promoted StrategyMotif was used.

## Decision policy

The chosen policy was the cheapest high-information discriminator: verify the preregistered exact `p=0` shear before inventing another signed-flux lemma.

The selected prior experiences changed *bounded routing* by blocking three familiar retries: raw far-field pressure divergence, absolute scale-budget summation, and local-to-global gluing by assumption. A causal counterfactual relative to a frozen pre-memory preference cannot be measured because the harness did not freeze such a preference.

## Falsifier / verification

The exact family

`u=(eps exp(k x_2+k^2 t),0,0)`, `p=0`

satisfies `div u=0`, `(u·grad)u=0`, and `partial_t u=Delta u`. For every fixed ball,

`E_R(t)=(1/2)∫_{B_R}|u|^2`,  
`dE_R/dt=2k^2 E_R>0`.

Verification performed:
- exact PDE algebra;
- local kinetic-energy derivative;
- pressure-zero check;
- local suitable/equality scope;
- global target DifferenceWitness;
- local-versus-global failure separation.

A small deterministic regression test is added only as a calibration/consistency check. Computation is not proof.

## Outcome / residual

Outcome: `EXISTING_LEDGER_SIGN_INSUFFICIENT_ROUTE_PRUNING`.

Solved subproblem: the existing local unsigned magnitude representation plus standard local-energy identity and pressure localization does not force nonpositive fixed-region local kinetic-energy derivative.

Residual: a live no-recrossing route must add a source-valid signed/correlated flux or trajectory coordinate, or a stronger global finite-`I` theorem that supplies orientation. `NS-B1a4a` records that successor interface. Global ancient-state gluing and Type-II remain open.

## Failure classification

Primary failure: `LOCAL_MATHEMATICAL_REPRESENTATION`.

New failure ID: `F-NS-B1a4-UNSIGNED-LOCAL-ENERGY-NO-SIGN`.

No new local-to-global impossibility was claimed. The preexisting gluing failure remains separately active.

Repeated-process links:
- pressure magnitude/nonlocality was already non-discriminating under `F-NS-B1a-C001-PRESSURE-SUMMABILITY`;
- absolute scale bookkeeping was already non-discriminating under `F-NS-B1a1-SCALE-NEUTRAL-LOCAL-ENERGY-LEDGER`.

The present residual refines the missing coordinate to signed orientation/correlation rather than reusing either failure verbatim.

## Seven saturation axes

- `KNOWLEDGE`: flattened for the narrow question “does the existing fixed-region ledger itself carry the sign?”; not flattened for finite-`I` dynamics generally.
- `OPERATOR`: reopened — need a signed/correlation/trajectory operator rather than another magnitude estimator.
- `EXPERIENCE_PATTERN`: flattened — reused the existing counterexample-first/interface-audit pattern; no new pattern retained.
- `OBSTRUCTION`: reopened and classified — `O-NS-B1a4-SIGNED-FLUX-COORDINATE`.
- `RELATION`: reopened — relation between pressure-free boundary influx and prior scale-neutral/pressure-summability failures is now explicit.
- `PATH`: reopened — `NS-B1a4a` is the source-valid signed-coordinate successor, but this path idea already existed prospectively, so retained PATH novelty is zero.
- `META_METHOD`: flattened — no new search-governance rule was required.

## RAKL novelty class

Internal class: `REPRESENTATION`, structural rank 0. The useful result is that the current magnitude representation erases the orientation needed by the proposed sign argument. This is not an external mathematical novelty certificate.

## What worked

RAKL v3 helped by forcing:
- exact context and DifferenceWitness before verification;
- dual memory retrieval so pressure/shell failures changed the test chosen;
- explicit separation of local mathematical failure from global gluing;
- proposal/shadow TaskEpisode evidence;
- residual-driven reopening of only the operator/relation/path axes.

## What failed

The mathematical route failed at the representation/sign interface: localized energy can increase even with `p=0`, so the available magnitude ledger does not supply one-sidedness.

There was no retrieval failure that changed the conclusion, no source contradiction, no verifier failure, and no tooling failure affecting the mathematics. Literature completeness remains unproved; the source search is bounded routing evidence only.

## v3 feature helped / missing

Helpful: immutable episode-style record, explicit failure lattice, DifferenceWitness discipline, and seven-axis saturation language prevented this calibration from being overpromoted into a finite-`I` theorem.

Potentially missing: a first-class `candidate_origin` / chronology field distinguishing `PREEXISTING_PROSPECTIVE_CANDIDATE` from a candidate genuinely generated after the v3 pre-candidate gate. The current cycle can record this in prose/TaskEpisode, but a typed field would improve attribution and prevent accidental discovery-credit inflation.

## Framework-improvement hypothesis

Add a typed `candidate_origin` plus `origin_evidence_pointer` to mathematical TaskEpisode/trace schemas, and make metrology count strict RAKL-mediated candidate generation only when the origin is `POST_GATE_GENERATED`. This would improve Paper-5 attribution without changing theorem authority.
