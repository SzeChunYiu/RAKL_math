# YM-E4b R1 — same-context expert-cell review

**Atom:** `YM-E4b`  
**Candidate:** `YM-E4b-C001-A/B`  
**Fibre:** `sha256:56093cb6547bca98774743a05caa0143aee2255359e3805cb44ba8a3ed5d7832`  
**Review authority:** `SAME_CONTEXT_ROLE_SEPARATION_ONLY / NOT_INDEPENDENT_REVIEW / ROOT_AUTHORITY_NONE`

All seven roles saw the same frozen issue/fibre and primary-source packet. Their role separation broadens attack coverage but does not count toward the three isolated mathematical reviews required for root closure.

## Shared finding packet

The cell reviewed three propositions separately:

1. `P1`: Appendix E's proof-level claim that the OS positive-time shift is an isometry is incompatible with a nonzero positive Hamiltonian spectrum.
2. `P2`: the dense-domain `t/2t` polarization argument is a valid local route from asymptotic embeddings + semigroup matrix elements to strong convergence, under explicit domain/map hypotheses.
3. `P3`: this local repair does not supply the changing-Hilbert-space identification, OS-null-space compatibility, global/resolvent extension, or continuum physical-gap transport required by the root.

## Role discussions and delegated checks

### 1. Constructive QFT / OS reconstruction

**Background:** reflection positivity, OS quotient construction, Euclidean time translation, Hamiltonian reconstruction.

**Check:** re-derived the OS norm under positive translation. Common translation of both positive-time arguments does not in general preserve their distance from the reflection plane. The source theorem itself asks for a contraction semigroup; the proof's stronger isometry sentence is therefore not needed and is incompatible with nontrivial excitations by `YM-E4b-C001-A`.

**Disposition:** `P1 ACCEPT`, `P2 ACCEPT CONDITIONALLY`, `P3 ACCEPT`. Requires any repair to preserve the OS null-space quotient and semigroup action, not merely Euclidean covariance before quotienting.

### 2. Functional analysis / spectral convergence

**Background:** self-adjoint contraction semigroups, resolvents, strong/weak operator convergence, varying Hilbert spaces.

**Check:** independently expanded `||T_n(t)J_n phi-J_nT(t)phi||^2` and verified that the three terms converge from asymptotic norm preservation and matrix elements at `t,2t`. The finite-delta-net argument in Appendix E.2 cannot be used on an infinite-dimensional unit sphere. Generic weak convergence plus boundedness is insufficient.

**Disposition:** `P1 ACCEPT`, `P2 ACCEPT`, `P3 ACCEPT`. Recommends a Kuwae–Shioya-type changing-space convergence structure as an analogue, not an automatic theorem import.

### 3. Gauge-theory physical-state / source algebra

**Background:** gauge-invariant observables, physical quotient spaces, regulator-dependent null vectors and sectors.

**Check:** focused on whether `[F]_sigma` and `[F]` can be called canonically the same vector. Their norms are defined by different OS forms; null spaces may change with the regulator. An exact isometry requires a theorem, not notation. Source-family completeness under `#109` is logically separate from this map problem.

**Disposition:** `P2 ACCEPT AS LOCAL`, `P3 STRONGLY ACCEPT`. No claim of physical-gap transport until gauge quotient and map direction/domain are source-bound.

### 4. Constructive RG / continuum-limit analysis

**Background:** lattice spacing, thermodynamic limits, RG trajectories, uniform estimates and physical units.

**Check:** the local semigroup lemma is regulator-indexed and dimensionless. It does not establish uniformity in volume, lattice spacing, bare coupling or regulator family. A continuum mass gap also requires that the spectral coordinate be the same physical Hamiltonian coordinate along the limit.

**Disposition:** `P2 ACCEPT`, root implication `REJECT`. Remaining failure is gluing/uniformity, not the local operator lemma.

### 5. Adversarial mathematical verifier

**Background:** hostile models, domain/quantifier attacks, proof-assumption auditing.

**Checks:**
- `T(t)` isometry + self-adjoint positive semigroup => `H=0`.
- no finite `delta`-net of the infinite-dimensional unit sphere for `delta<1`.
- matrix elements alone do not force norm convergence.
- `J_sigma T(t)phi` is not licensed unless `T(t)phi` belongs to the map domain or an extension/coherent approximation is proved.
- a fixed countable cylinder subalgebra claimed for all real `t` needs an explicit stability/core construction.

**Disposition:** local lemma survives; source-to-continuum gluing remains blocked.

### 6. Primary-source / provenance auditor

**Background:** exact source selectors, dependency and scope discipline.

**Check:** source-local selectors were bound to pp.89–92 and pp.203–206 of arXiv:`2606.19362v1`. The current source contains both the valid polarization pattern and the later exact-isometry/common-space assumptions. The Kuwae–Shioya reference is used only for the existence of a changing-Hilbert-space framework. No unavailable theorem detail is reconstructed.

**Tooling note:** screenshot rendering was attempted twice and failed with cache-miss. Parsed PDF text remained available; no figure/image interpretation is used.

**Disposition:** evidence sufficient for the narrow local claims; no broader source verdict.

### 7. RAKL v3 assurance / metrology

**Background:** immutable episodes, failure diagnosis, gluing, saturation vector, authority boundaries.

**Check:** preserved `episode -> observation -> diagnosis -> existing obstruction`, not `one failed source proof -> global impossibility`. The local mathematical repair is separated from the still-open gluing residual. Prior memory changed routing away from source-completeness duplication and saturated Bałaban metadata retrieval, but no matched no-memory counterfactual identifies causal lift.

**Disposition:** retain internal semantic novelty only on `KNOWLEDGE=1`, `RELATION=1`, `PATH=1`; all other axes zero. No lesson/tool/obstruction/motif promotion.

## Cell synthesis

Consensus is unanimous on the narrow status:

`PARTIAL_LOCAL_RESULT / SOURCE_PROOF_PATH_REPAIRED_LOCALLY / CHANGING_HILBERT_GLUING_BLOCKED / ROOT_OPEN`.

The strongest surviving objection is representation-level: the argument needs a typed regulator-to-continuum identification/convergence witness compatible with the actual OS quotient, semigroup, gauge-invariant physical sector, vacuum and continuum spectral coordinate. A formal changing-space theorem cannot be applied until those target hypotheses are source-bound.

No role grants independent-review credit.
