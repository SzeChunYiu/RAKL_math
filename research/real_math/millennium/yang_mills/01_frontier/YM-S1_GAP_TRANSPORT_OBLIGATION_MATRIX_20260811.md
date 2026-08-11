# YM-S1 gap-transport obligation matrix — 2026-08-11

**Authority:** `PRE_CANDIDATE_CALIBRATION / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`

This matrix decomposes the phrase "prove a lattice mass gap and take the continuum limit" into separately falsifiable obligations. It is a research-control object, not a theorem.

| ID | Obligation | Exact question | Closest source support | Current state | Cheapest falsifier / discriminator |
|---|---|---|---|---|---|
| `G1` | Physical transfer matrix | Is there a positive self-adjoint transfer matrix on the correct gauge-invariant physical Hilbert space, with the Euclidean time step and normalization bound? | Osterwalder–Seiler 1978 | `SUPPORTED_FIXED_CUTOFF` | Exhibit a proposed observable/evolution object that lives in a Markov/Langevin space or gauge-fixed auxiliary space rather than the reconstructed physical transfer-matrix space. |
| `G2` | Fixed-cutoff gap/correlation estimate | What exact dimensionless decay exponent or eigenvalue-ratio bound is proved at fixed `a`, and for which observables/states? | Shen–Zhu–Zhu 2023; strong-coupling literature | `SUPPORTED_STRONG_COUPLING_ONLY` | Check whether the estimate is only a functional-inequality gap for a stochastic generator or only a restricted correlation family. |
| `G3` | Thermodynamic / source-family uniformity | Does the relevant decay/gap-sensitive estimate survive `L -> infinity`, and do its support/source-dependent constants remain controlled for the changing observable family needed by later RG/spectral steps? | SZZ Cor. 1.6 is already infinite-volume at explicit strong coupling; its finite-volume proof has an `L`-independent prefactor for each fixed cylinder pair | `SUPPORTED_INFINITE_VOLUME_STRONG_COUPLING_COVARIANCE / SUPPORT_FAMILY_UNIFORMITY_OPEN` | First verify `L`-independence for the exact source theorem; then grow source support/complexity along a blocking sequence and test whether prefactors/norm losses erase the common exponential-rate information. |
| `G4` | Source-family spectral visibility | Does the controlled gauge-invariant observable family detect every physical excitation below the proposed gap? | No source in the current packet closes this for the root theory | `OPEN / ACTIVE_YM-S1a1` | Construct a positive finite-dimensional transfer matrix with a hidden low-energy state orthogonal to the tested source family while the tested correlator decays faster. If possible, restricted-source clustering cannot imply the full gap without a cyclicity/density hypothesis. |
| `G5` | RG/coarse-graining transport | Is there a rigorous comparison law that transports the chosen gap-sensitive quantity across blocking steps from weak bare coupling toward an infrared regime? | Balaban RG supplies UV multiscale control, not this gap law | `OPEN` | Show that the candidate quantity has no monotone/comparison law under one exact blocking step, or that the constants leave the controlled Banach/regime. |
| `G6` | Physical-unit scaling | With `T_a = exp(-a H_a)` (when that normalization is proved), does `-a^{-1} log(lambda_1/lambda_0)` stay bounded below by a finite positive constant rather than merely having a lattice-unit bound? | Dimensional identity once transfer matrix is bound | `OPEN` | A bound on the one-step exponent that is not quantified in `a`, or that vanishes faster than `a`, fails to certify a physical gap. |
| `G7` | Continuum spectral identification | Do lattice Schwinger functions/transfer objects converge strongly enough, with OS/Wightman reconstruction, to identify the limiting Hamiltonian spectrum and preserve the lower bound? | Osterwalder–Schrader reconstruction gives the target framework; Yang–Mills continuum construction remains open | `OPEN / ROOT-COUPLED` | Produce a sequence with finite-cutoff gaps but weak/sectorwise convergence that loses the gap or changes the Hilbert space; any proof lacking a spectral-convergence theorem remains incomplete. |

## Same-context expert partition

The cell separates four first-order child atoms instead of treating `YM-S1` as one proof request:

- `YM-S1a — spectral visibility`: minimum cyclicity/density/completeness condition on gauge-invariant sources needed for clustering to exclude hidden low-energy states (`G4`). Its strict successor `YM-S1a1` is the active spectral bridge lane.
- `YM-S1b — thermodynamic uniformity audit`: ordinary box-size uniformity for the SZZ strong-coupling smooth-cylinder covariance theorem is now source-supported. The refined unresolved child is `YM-S1b1 — source-family/support uniformity`, tracking support-dependent prefactors/norms as the observable family changes across RG/spectral use (`G3`).
- `YM-S1c — RG transport`: a gap-sensitive quantity with an exact comparison law across controlled gauge-theory RG steps (`G5`).
- `YM-S1d — continuum physical scaling`: correct `a`-scaling plus spectral convergence/reconstruction (`G6` + `G7`).

## Current discriminator ordering

`YM-S1a1` remains the active spectral candidate lane and is governed by its own fresh strict pre-candidate packet and exact-head CI. The `YM-S1b` source audit does not create a candidate and does not alter that chronology.

The new G3 audit removes a lower-information repeat task: for the exact SZZ strong-coupling cylinder theorem, re-proving generic finite-box convergence is not the next bottleneck. The residual worth testing is whether the **changing source family** required by completeness/RG can retain useful uniform control when support, labels and norms grow.

## Explicit non-inferences

- `G2` does not imply `G4`.
- SZZ `L`-uniform/infinite-volume covariance control does not imply uniformity over a growing RG source family.
- `G3` does not imply `G6`.
- Wilson area law does not imply `G4` or `G7`.
- A Langevin/Poincaré/log-Sobolev gap does not imply `G1`.
- Balaban-style UV stability does not imply `G5`.
- Passing `G1`–`G6` at fixed regulator does not imply `G7`.
- None of `G1`–`G7` alone proves continuum existence or the Clay root.
