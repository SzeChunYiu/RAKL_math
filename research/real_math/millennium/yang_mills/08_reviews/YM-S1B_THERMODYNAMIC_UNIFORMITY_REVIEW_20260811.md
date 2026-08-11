# YM-S1b same-context expert review — thermodynamic uniformity

**Authority:** `SAME_CONTEXT_REVIEW_ONLY / SOURCE_AUDIT / NO_INDEPENDENT_REVIEW / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`

This review evaluates the source-bound refinement of `G3` only. All roles inspect the same frozen public evidence and therefore do not count as independent mathematical reviewers.

## Expert cell

### 1. Lattice Gibbs / infinite-volume specialist

**Background and role:** constructive statistical mechanics and lattice gauge Gibbs measures; owns finite-volume-to-infinite-volume interpretation and dependence of constants on the box.

**Evidence inspected:** Shen–Zhu–Zhu Assumption 1.1, Theorem 1.2 / infinite-volume uniqueness statements, Corollary 1.6, and the finite-volume covariance proof immediately before `L -> infinity`.

**Finding:** for the SZZ smooth-cylinder covariance theorem, the relevant finite-volume prefactor is explicitly independent of side length `L` before the limiting passage, and the theorem is ultimately stated on the unique infinite-volume measure. Generic box-size deterioration is therefore not the live obstruction for this source family.

**Strongest objection:** the prefactor still depends on support cardinalities, so `L`-uniformity must not be confused with uniformity over a source family whose support grows under coarse graining.

**Vote:** `ACCEPT_SCOPED_RECLASSIFICATION`.

### 2. Transfer-matrix / Osterwalder–Schrader specialist

**Background and role:** reflection positivity, transfer matrices, Euclidean reconstruction and spectral interpretation.

**Evidence inspected:** Osterwalder–Seiler physical positivity/positive self-adjoint transfer-matrix result; SZZ covariance theorem and its stochastic-generator setting.

**Finding:** thermodynamic Euclidean covariance control and physical transfer-spectrum control are separate obligations. The audit may narrow `G3`, but it must not infer a Hamiltonian gap from a Poincaré/log-Sobolev gap or from restricted Euclidean clustering without the pending `G4` OS/source-density bridge.

**Strongest objection:** the word “mass gap” in the SZZ corollary is a source terminology projection; the Clay root requires a physical continuum quantum theory and spectral gap. The repository must preserve that distinction.

**Vote:** `ACCEPT_WITH_AUTHORITY_BOUNDARY`.

### 3. RG / asymptotic-freedom specialist

**Background and role:** lattice renormalization group, weak/strong coupling regimes and continuum scaling.

**Evidence inspected:** SZZ explicit strong-coupling condition, the current `G5`/`G6` obligation definitions, and the constructive lane's recent marked-source leakage result.

**Finding:** an `L`-uniform strong-coupling theorem does not solve the actual route discontinuity from weak bare coupling to the strong-coupling regime. The more relevant uniformity question is whether source complexity, support and norms remain controlled under repeated blocking.

**Strongest objection:** a fixed-support cylinder theorem can become useless after many RG steps if the source basis proliferates or norms/prefactors grow faster than the exponential decay information can compensate.

**Vote:** `ACCEPT_AND_OPEN_SUPPORT_FAMILY_RESIDUAL`.

### 4. Boundary-condition / sector specialist

**Background and role:** thermodynamic limits, phase uniqueness, boundary conditions, superselection/flux sectors.

**Evidence inspected:** SZZ finite periodic-volume setup and the statement that alternative finite-volume boundary conditions lead to the same unique infinite-volume stochastic solution under the strong-coupling assumption.

**Finding:** this supports robustness of the stochastic infinite-volume limit, but it is not enough to certify uniform spectral estimates in every physical transfer-matrix sector. The matrix should retain a boundary/sector qualifier.

**Strongest objection:** uniqueness of one infinite-volume Gibbs/SDE object can coexist logically with unresolved sector-specific spectral questions.

**Vote:** `ACCEPT_SCOPED_ONLY`.

### 5. Adversarial falsification specialist

**Background and role:** counterexample-first review, hidden dependence auditing and implication-direction checks.

**Evidence inspected:** the exact dependence of `c1` and `c_N` in Corollary 1.6, the proof's `L`-independence statement, and current G3–G7 separation.

**Finding:** the easiest way to overclaim this source is to replace “independent of box side length for each fixed cylinder pair” by “uniform over all observables/scales.” Those are not equivalent. A future discriminator should explicitly grow source support/complexity across blocking steps and track the prefactor/norm loss.

**Strongest objection:** a common exponential exponent can be overwhelmed in a multiscale application if the family-dependent constants are uncontrolled as the family changes.

**Vote:** `ACCEPT_WITH_PLANTED_OVERCLAIM_BLOCK`.

### 6. Formal assurance / novelty specialist

**Background and role:** exact statement binding, provenance, research-control authority and rediscovery risk.

**Evidence inspected:** current RAKL mathematical-research gates, existing `YM-S1` obligation matrix, primary sources, and repository memory boundaries.

**Finding:** this is a source-scope correction, not new mathematics. It improves the proof-DAG search state by removing a falsely broad unresolved coordinate and replacing it with a sharper one. No candidate, proof, novelty or root authority is created.

**Strongest objection:** changing the G3 label without preserving its exact scope could silently turn a literature theorem into a stronger physical claim.

**Vote:** `ACCEPT_IF_SCOPE_IS_INLINE_IN_MATRIX`.

## Cell synthesis

The six roles agree on one bounded update:

- change the SZZ-specific thermodynamic-volume coordinate from generic `PARTIAL` to `SUPPORTED_INFINITE_VOLUME_STRONG_COUPLING_COVARIANCE`;
- keep physical transfer-spectrum, arbitrary-sector, weak-to-strong RG, lattice-spacing and continuum obligations open;
- open `YM-S1b1` as a future context atom for **source-family/support uniformity under RG**, not as a theorem candidate;
- do not disturb the active `YM-S1a1` chronology while PR #17's exact-head gate is still pending.

**Consensus authority:** `SOURCE_BOUND_ROUTE_REFINEMENT / SAME_CONTEXT_REVIEW_ONLY / NO_MATHEMATICAL_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`.
