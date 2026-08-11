# YM-E1a1a — actual weak-block source contract

**Status:** `SOURCE_BOUND_CONTRACT / CANDIDATE_BLOCKED / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`.

## Why this contract exists

The strict `YM-E1a1a` pre-candidate packet passed exact-head application CI and became canonical at `RAKL_math` merge `d8e4b392c1d21b5a2bc832fc47a038b37490afa3`. Its registered next action is not “try a plausible block”: it is to freeze **one actual weak-coupling Balaban-style block** and only then generate the narrowest closure-or-leakage candidate.

A fresh primary-source audit exposed a load-bearing source-identity omission in the canonical packet. The packet binds Balaban's background-field, four-dimensional small-field, cluster-expansion and large-field papers, but its source anchors do not bind the dedicated paper

- T. Bałaban, *Averaging operations for lattice gauge theories*, Commun. Math. Phys. **98** (1985), 17–51, DOI `10.1007/BF01211042`.

The primary record states that renormalization-group transformations are defined through averaging operations, that this paper studies such operations for lattice gauge fields and gauge transformations, and that it characterizes classes of configurations on which the operations are regular, including analytic regularity. This is therefore part of the exact transformation identity, not optional background reading.

The currently accessible primary record is abstract/metadata level; it does **not** expose enough of the nonlinear averaging definition, path/block conventions, regularity domain and gauge-covariance hypotheses to instantiate the actual block without reconstruction from memory or secondary exposition. Such reconstruction is disallowed for a candidate whose point is to test the actual Balaban block.

## Primary-source stack and exact authority boundary

1. **Gauge-field averaging identity.** Bałaban 1985, DOI `10.1007/BF01211042`. Authority presently extracted: role of averaging operations for lattice gauge fields/gauge transformations and existence of regular/analytic configuration classes. Missing: exact formula, block/path conventions and theorem hypotheses.
2. **Gaussian/propagator precursor.** Bałaban 1984 I, DOI `10.1007/BF01215753`, treats the Gaussian vector-field theory used as a precursor for more complicated non-Abelian RG. Bałaban 1984 II, DOI `10.1007/BF01240221`, extends the operator results across restrictions/scales and RG transformations of different orders. These do not supply a marked non-Abelian source theorem.
3. **Background-field propagator.** Bałaban 1985, DOI `10.1007/BF01240355`, proves regularity and decay for RG propagators depending on an external background gauge field. This is a localization ingredient, not the missing gauge-field averaging definition and not a marked observable estimate.
4. **Background-field variational problem.** Bałaban 1985, DOI `10.1007/BF01229381`, remains the source for the coarse-variable-constrained background field.
5. **Actual 4D small-field effective-action step.** Bałaban 1987, DOI `10.1007/BF01215223`, remains the source for the four-dimensional small-field RG/effective-action and running-coupling step.
6. **Cluster induction and large fields.** DOI `10.1007/BF01239022`, `10.1007/BF01257412`, `10.1007/BF01238433` remain required for polymer localization/iteration and the `R`-operation boundary.

No line above is promoted to an observable-closure, reflection-positivity-preservation, continuum-limit or mass-gap theorem.

## Frozen actual-block contract schema

A future `YM-E1a1a-C001` is **not admissible** until one primary-text extraction fills every field below with exact definitions or theorem references. `UNKNOWN` is a blocking value; post-result completion is forbidden.

| Field | Required binding | Current state |
|---|---|---|
| `B0_TRANSFORMATION_ID` | exact Balaban one-step transformation and source papers | `PARTIAL` |
| `B1_FINE_COARSE_GEOMETRY` | fine/coarse lattices, block factor `L`, orientation/path conventions | `UNKNOWN` |
| `B2_GAUGE_AVERAGING_MAP` | exact nonlinear gauge-field averaging map and gauge-transformation covariance | `UNKNOWN` |
| `B3_REGULARITY_DOMAIN` | small/regular-field domain on which averaging/background construction is defined/analytic | `UNKNOWN` |
| `B4_BACKGROUND_FIELD_BINDING` | exact coarse constraint/minimizer/gauge-fixing relation used by the 4D step | `PARTIAL` |
| `B5_ONE_STEP_DENSITY` | exact one-step finite-cutoff integral/effective-density object to differentiate | `PARTIAL` |
| `B6_SOURCE_MARK` | one gauge-invariant source, support, representation/geometry grade and normalization fixed before differentiation | `UNKNOWN` |
| `B7_REFLECTION_BUFFER` | reflection plane, positive-half-space algebra and deterministic support enlargement budget under the block | `UNKNOWN` |
| `B8_MARKED_DECOMPOSITION` | registered generated-label basis plus typed remainder, fixed before result inspection | `UNKNOWN` |
| `B9_MARKED_NORM` | weighted polymer/geometry/source-degree norm with explicit `g_k` and `L` dependence | `UNKNOWN` |
| `B10_LARGE_FIELD_INTERFACE` | whether/how the chosen mark passes through the large-field `R` operation | `UNKNOWN` |
| `B11_NONTRIVIALITY_WITNESS` | finite-cutoff separating/nonzero response check; no continuum inference | `UNKNOWN` |

### Candidate acceptance gate

Candidate generation is enabled only if `B0`–`B11` have no `UNKNOWN`, every exact mathematical definition is primary-source bound, and the already-frozen context/memory/expert/trace packet remains current. If filling these fields materially changes the `MathContextFiber`, method-transfer matrix or solved-analogue set, a fresh context/memory/review/trace packet is required before the candidate.

## New lower-dimensional contrastive control

A current primary result sharpens what a genuine continuum bridge should look like without transferring its proof to four dimensions:

- N. V. Dang and E. Nohra, *The Yang--Mills measure on compact surfaces as a universal scaling limit of lattice gauge models*, arXiv:`2602.08591` (2026), constructs the two-dimensional Yang–Mills measure as a random distributional one-form on compact surfaces and proves a lattice scaling-limit universality theorem for a broad class including Wilson, Manton and Villain actions, together with convergence of correlation functions and Segal amplitudes.

**Transferable question only:** can the 4D program eventually state regulator independence and observable convergence at an equally explicit topology/observable level?

**Non-transfer:** the 2D construction does not supply the 4D asymptotically-free non-Abelian RG estimates, reflection-positive marked transport, ultraviolet-depth uniformity, OS reconstruction or a four-dimensional spectral mass gap.

Because this 2026 solved analogue was not named in the frozen `YM-E1a1a` context, it must be included in a context supplement/refreeze if it is used to shape `C001` rather than merely as a contrastive calibration.

## Same-context source/contract cell

Seven role-separated passes were rerun on this source identity question.

1. **Constructive QFT / OS:** blocks candidate generation; reflection support cannot be audited until the exact block geometry and averaging support are fixed.
2. **Balaban RG:** identifies DOI `10.1007/BF01211042` as part of the transformation identity and rejects substituting the local Haar toy or a generic block map.
3. **Gauge representation / operator mixing:** requires the source mark and output grade to be frozen only after the actual averaging/background map is exact, otherwise “leakage” has no stable meaning.
4. **Multiscale norms:** rejects any finite one-step constant that omits `g_k`, `L`, support and source-degree dependence; the primary norm conventions must be extracted before a bounded-tangent claim.
5. **Adversarial mathematical physics:** strongest falsifier is now source-level: if the actual averaging map has nonlocal/path or gauge-fixing dependencies incompatible with the proposed reflection buffer, the planned marked state fails before analytic estimates begin.
6. **Formal assurance:** distinguishes a machine-passed pre-candidate packet from an instantiated mathematical candidate contract; the former does not authorize invention of missing definitions.
7. **Novelty/frontier:** no novelty claim; identifying a missing primary source binding is a research-control correction, not a new Yang–Mills theorem.

Consensus: `BLOCK_CANDIDATE_UNTIL_PRIMARY_BLOCK_INSTANTIATED`.

## Breakthrough-learning use

Only `CONTRASTIVE_DISCRIMINATION` and `FIXATION_RESET` are used: the 2D continuum universality theorem is a contrastive solved model, and the failure to bind the exact averaging source resets fixation on “operator mixing” as the first analytic difficulty. Neither mode has theorem authority.

## Result and residual

**Result:** `YM-E1a1a` remains the correct child, but the smallest obstruction is now earlier than marked operator mixing: the exact weak-block object has not yet been source-instantiated. A candidate generated now would be testing an invented surrogate rather than the registered method.

**Residual `YM-E1a1a0`:** obtain/extract the primary full-text averaging definition and hypotheses, bind them to the 1987 4D step/background field, freeze one positive-half-space source and marked norm, then rerun the candidate-currentness gate.

No `FailureExperience` is minted from this episode because no mathematical candidate was run or falsified. In particular this is **not** evidence of gauge redundancy, nonperturbative impossibility, loss of uniform estimates, continuum-limit noncommutation, positivity/reconstruction failure or decay-to-gap failure. It is a typed **source/context coverage block** whose scope is only `YM-E1a1a` candidate instantiation.

**Authority:** `PRIMARY_SOURCE_COVERAGE_CORRECTION / ACTUAL_BLOCK_CONTRACT_NOT_INSTANTIATED / CANDIDATE_BLOCKED / NO_THEOREM / NO_NOVELTY / ROOT_AUTHORITY_NONE`.
