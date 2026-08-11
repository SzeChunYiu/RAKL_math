# YM-E1a1 source packet — marked one-step RG closure — 2026-08-11

**Authority:** `PRIMARY_SOURCE_CONTEXT / PRE_CANDIDATE_ONLY / ROOT_AUTHORITY_NONE`

**Framework authority inspected:** `SzeChunYiu/RAKL@55d4cb0a83f271d3263fbe48f99b173119c732d2`.
**Application root:** `SzeChunYiu/RAKL_math#5`.

This packet supports only the child atom `YM-E1a1`. It does not assert that a marked Balaban RG theorem already exists.

## S0 — official Yang–Mills target

Arthur Jaffe and Edward Witten, *Quantum Yang–Mills Theory*, Clay Mathematics Institute.

- https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf
- Retained use: the root requires a non-trivial 4D quantum Yang–Mills theory with axiomatic strength at least comparable to the stated Wightman/OS framework and a positive mass gap.
- Boundary: fixed-cutoff lattice control, an ultraviolet stability estimate, or a finite source family does not close the root.

## S1 — fixed-cutoff reflection positivity

K. Osterwalder and E. Seiler, *Gauge field theories on a lattice*, Annals of Physics **110** (1978), 440–471.

- DOI: https://doi.org/10.1016/0003-4916(78)90039-8
- The paper rigorously verifies physical positivity for lattice Schwinger functions, yielding a positive self-adjoint transfer matrix, and proves strong-coupling infinite-volume results.
- Retained use: a positive-half-space gauge-invariant source family can be calibrated against exact reflected quadratic forms at fixed cutoff.
- Boundary: the theorem does not say that an arbitrary RG blocking/source-mixing map preserves support or positivity, nor does it remove the cutoff in the weak-coupling 4D continuum regime.

## S2 — Balaban one-step/multiscale RG backbone

T. Balaban, *Renormalization group approach to lattice gauge field theories I*, Commun. Math. Phys. **109** (1987), 249–301.

- DOI: https://doi.org/10.1007/BF01215223

T. Balaban, *Renormalization group approach to lattice gauge field theories II*, Commun. Math. Phys. **116** (1988), 1–22.

- DOI: https://doi.org/10.1007/BF01239022

T. Balaban, *Convergent renormalization expansions for lattice gauge theories*, Commun. Math. Phys. **119** (1988), 243–285.

- DOI: https://doi.org/10.1007/BF01217741

Retained use: these works provide the same-problem exact multiscale setting—localized effective densities, cluster expansions, coupling renormalization and large-field control—against which the marked/source tangent question should be posed.

Critical boundary: in the source set inspected for this cycle, no theorem was identified that upgrades the unmarked Balaban RG to a separating family of gauge-invariant source insertions with the exact support, operator-mixing and ultraviolet-depth-uniform derivative bounds required by `YM-E1a1`. Absence from this bounded source check is not an impossibility theorem.

## S3 — loop renormalization makes geometry part of the mark

R. A. Brandt, F. Neri and M.-a. Sato, *Renormalization of loop functions for all loops*, Phys. Rev. D **24** (1981), 879.

- DOI: https://doi.org/10.1103/PhysRevD.24.879
- Retained use: Wilson-loop renormalization has geometry-sensitive structure, including cusp/intersection effects. A marked RG state therefore cannot assume that “one Wilson-loop coefficient” is a closed scalar coordinate under refinement/blocking.
- Boundary: this is perturbative loop renormalization, not a nonperturbative 4D marked-RG theorem.

## S4 — constructive gauge analogue with uniform regulator control

D. Brydges, J. Fröhlich and E. Seiler, *On the construction of quantized gauge fields. I. General results*, Annals of Physics **121** (1979), 227–284.

- DOI: https://doi.org/10.1016/0003-4916(79)90098-8
- Retained use: gauge invariance and Osterwalder–Schrader positivity can coexist with regulator-uniform constructive estimates in gauge/Higgs settings.
- Boundary: the detailed continuum constructions are lower-dimensional/superrenormalizable or matter-assisted; the 4D pure non-Abelian critical problem has different ultraviolet and gauge-fixing structure.

## S5 — 4D pure SU(2) ultraviolet construction with fixed IR cutoff

J. Magnen, V. Rivasseau and R. Sénéor, *Construction of YM4 with an infrared cutoff*, Commun. Math. Phys. **155** (1993), 325–383.

- DOI: https://doi.org/10.1007/BF02097397
- The work constructs Schwinger functions for pure SU(2) Yang–Mills with a fixed infrared cutoff and no ultraviolet cutoff in a regularized axial gauge, with nonperturbative control of counterterms restoring gauge invariance and Slavnov identities.
- Retained use: it is a contrastive same-dimension example showing that observable/source information and gauge-identity bookkeeping can be first-class parts of an ultraviolet construction.
- Boundary: SU(2), fixed IR cutoff, trivial topological sector and axial-gauge representation do not supply the Clay theory or the Balaban marked-step closure.

## Source-bound conclusion

The smallest source-supported question is not “does the continuum theory exist?” but:

> after one exact gauge RG blocking step, what is the image of a finite gauge-invariant source tangent, and can that image be represented in a reflection-compatible marked space with explicitly bounded mixing, support growth and norm loss?

The source record supports asking and falsifying that question. It does not supply its positive answer.
