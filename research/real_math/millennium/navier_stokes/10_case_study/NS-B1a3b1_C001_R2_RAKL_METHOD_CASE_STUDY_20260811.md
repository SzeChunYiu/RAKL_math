# RAKL_METHOD_CASE_STUDY — NS-B1a3b1-C001 R2

**Cycle:** `NS-B1a3b1-C001-R2`  
**Authority:** `PROPOSAL_SHADOW_CASE_STUDY / NO_ROOT_AUTHORITY`

## Atom and actual fibre

The active atom was the exact child from issue #122: decide whether the `bmo_{1/|log r|}` vorticity-direction input in Grujic v2 is stable under the Navier–Stokes blow-up zoom, and distinguish that representation question from the producer-side finite-`I` geometry problem.

The frozen fibre actually consulted: Clay root/success contract; Albritton–Barker finite-`I` ancient producer; arXiv:2607.08866v2 as the exact current consumer; merged episode `EP-NS-B1a3b-C001-20260811`; failures `F-NS-B1a3b-DERIVATIVE-LOSS-VORTICITY-DIRECTION`, `F-NS-B1a3b-NORMALIZATION-ZERO-INSTABILITY`, `F-NS-B1a3b-GEOMETRY-NOT-INHERITED-BY-TOPOLOGY`, `F-NS-B1a3-UNCONTROLLED-FAR-FIELD`, and `F-NS-B1a3-LOCAL-GLOBAL-INTERFACE-MISMATCH`; scoped tool `T-XM-ROOT-BRIDGE-STABILITY-AUDIT`; and `PRE-ACTION-FIBRE-RECEIPT-v1`. The earlier partial B1a3b1 branch at `82d29134` was read as experience but rejected for prospective gate credit because its framework/application subjects were stale.

## Methods/operators and decision policy

Selected operators were `OP-NS-LOGBMO-ZOOM-IDENTITY` and `OP-NS-GRUJIC-SOURCE-SIGNATURE-AUDIT`. The first used exact change of variables in the weighted mean-oscillation norm; the second bound Definition 2.1, the `bmo_phi` definition, Theorem 4.1 including its near/far-field proof, and Theorem 7.4 to the producer/consumer interface. A direct finite-`I`-to-geometry derivation was deliberately deferred.

The pre-memory preference was to continue the geometry lane by trying to push a direction regularity condition through the finite-`I` blow-up passage. Prior B1a3b/B1a3 experience changed routing: first test whether the consumer representation itself survives zoom and whether its exact global/state-space inputs match the producer. Barker–Prange and Miller were retrieved but rejected as different consumers; scalar energy-shell failures were retrieved but rejected as a saturated representation family; pending PR #60 was rejected for canonical authority because it remains an open draft.

## Falsifier and verification

The counterexample-first discriminator was exact: if some `0<r<=1` enlarged the source's global `bmo_{1/|log rho|}` norm under `f(y)=f(x0+r y)`, the representation candidate failed. It did not. Mean oscillation transforms exactly from radius `rho` to `r rho`, and `|log rho|/|log(r rho)|<=1`; the `L^infinity` term is unchanged. The critical global `L^{3/2,infinity}` vorticity norm is also invariant under Navier–Stokes zoom.

Source verification then showed that scale compatibility is not enough. Grujic v2 consumes global uniform-in-time weak-Lorentz vorticity, a global small-radius BMO phase norm, critical-point profile assumptions, and far-field Biot–Savart information. Its Theorem 7.4 is a first-singular-time forward-analyticity/escape-time theorem, not an ancient Liouville theorem. A source-text search did not locate an explicit convention for `xi` on the zero-vorticity set, so that endpoint is retained as `CANNOT_CHECK` applicability, not promoted to a criticism of the source.

## Outcome, diagnosis, and retained lesson

Outcome: `PARTIAL_SUCCESS / REPRESENTATION_BRIDGE_VERIFIED / PRODUCER_AND_GLUING_OPEN`.

Episode, diagnosis, and lesson remain separate. The episode records what was tried and observed. The diagnosis rejects scale-loss and supports producer-input absence plus global/state-space interface mismatch. The candidate lesson is: when an exact conditional consumer is non-expansive under the blow-up representation, remove scale-loss from the residual and move search upstream to producer generation; audit global/far-field and time/state-space gluing independently.

The solved subproblem is classified `representation`, structural rank `0`. It is a useful exact transport identity, not a claim of new Navier–Stokes mathematics.

## Failure taxonomy and saturation

No local mathematical failure occurred in the zoom lemma. The remaining failures are separated as producer/representation input absence, local-to-global gluing (global Lorentz/far-field), source state-space mismatch (pre-singularity versus ancient), and a source-applicability warning (zero-vorticity phase convention). These are not merged into one generic “geometry failed” record.

Retained semantic novelty this round: `KNOWLEDGE=1`, `OPERATOR=0`, `EXPERIENCE_PATTERN=0`, `OBSTRUCTION=1`, `RELATION=1`, `PATH=1`, `META_METHOD=0`. The reopened axes are KNOWLEDGE, OBSTRUCTION, RELATION, and PATH. OPERATOR, EXPERIENCE_PATTERN, and META_METHOD are locally flat for this round only; no global saturation claim is made.

## What v3 helped and what was missing

Useful v3 features were the frozen MathContextFiber, dual success/failure memory, explicit rejected retrievals, ProblemFibre-style co-retrieval, pre-action receipt, immutable TaskEpisode shadow, episode-to-diagnosis-to-lesson separation, scoped failure lattice, hash-chained trace, and seven-axis saturation accounting. The strongest practical effect was routing: prior failure experience prevented a duplicate topology attack and redirected the cycle to the exact representation/source boundary.

A tooling limitation remained: this connector-only environment could inspect current RAKL source but could not import or execute the repository package because the container has no network access and the GitHub connector exposes files rather than a mounted checkout. Therefore no canonical `RAKLV3State` was materialized and `state_fingerprint(...)` is `CANNOT_MEASURE`; the cycle used proposal/shadow records matching the current v3 surfaces and independently recomputed canonical content hashes.

## Framework-improvement hypothesis

A general hypothesis, not yet an established defect: a pre-action binding helper could explicitly reject a receipt/fibre whose framework or application subject is no longer current when a run resumes after concurrent main movement. This cycle had to reject a stale prior partial branch manually. Before opening a framework issue, the existing runtime should be exhaustively checked for an equivalent freshness/rebinding surface; no framework defect is claimed here without that audit.

## Next action

Open `NS-B1a3b1a`: counterexample-first test whether finite-`I` dynamics on the original pre-singularity solution can produce the required global uniform phase/amplitude certificate without importing derivative regularity, global tail tightness, or the desired geometry. Keep the orthogonal pressure-temporal/no-recrossing lane and Type-II classification separate.
