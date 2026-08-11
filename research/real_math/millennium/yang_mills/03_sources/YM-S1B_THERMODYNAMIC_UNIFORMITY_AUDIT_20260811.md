# YM-S1b — thermodynamic-uniformity source audit — 2026-08-11

**Authority:** `SOURCE_BOUND_CONTEXT_REFINEMENT / NO_MATHEMATICAL_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`

**Parent lane:** `YM-S1` spectral/lattice-RG gap transport.  
**Audited obligation:** `G3 — thermodynamic uniformity`.  
**Framework authority:** current `SzeChunYiu/RAKL` main observed at `15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`; application pin matches that commit.

## Object and question

The original `G3` question was intentionally broad:

> Does a lower bound or clustering estimate survive the spatial thermodynamic limit `L -> infinity` with constants that do not deteriorate with the finite-volume side length?

This audit does **not** ask whether a physical Hamiltonian mass gap has been proved. It asks a narrower source question: for the Shen–Zhu–Zhu strong-coupling Euclidean covariance theorem already present in the spectral lane, is ordinary finite-volume `L`-dependence still an unresolved obstruction?

## Primary-source evidence

### Shen–Zhu–Zhu, 2022/2023

Hao Shen, Rongchan Zhu, Xiangchan Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, arXiv:2204.12737; Commun. Math. Phys. 400 (2023), DOI `10.1007/s00220-022-04609-1`.

Under Assumption 1.1, including

`|beta| < 1 / (16(d-1))` for `SU(N)`,

the paper proves convergence of the finite-volume Yang–Mills measures to a unique invariant measure on the whole lattice. Its Corollary 1.6 is stated directly for the infinite-volume measure `mu^ym_{N,beta}` and gives, for disjoint-support smooth cylinder functions `f,g`, a covariance estimate of the form

`Cov(f,g) <= c1 d(g) exp(-c_N d(Lambda_f,Lambda_g)) * source_norms`,

where `c1` depends on the finite support cardinalities and `c_N` depends on the strong-coupling/model parameters (`K_S`, `N`, `d`).

The proof immediately before the `L -> infinity` passage states that its finite-volume constant `c1` depends on `|Lambda_f|, |Lambda_g|` and is **independent of `L`**. It then lets `L -> infinity` to obtain the stated result.

The same paper also proves uniqueness for the infinite-volume stochastic dynamics and notes that finite-volume approximations with other boundary conditions lead to the same unique infinite-volume SDE solution. This strengthens the thermodynamic-limit picture but is not, by itself, a theorem about every physical transfer-matrix boundary/sector construction.

### Osterwalder–Seiler, 1978

K. Osterwalder and E. Seiler, *Gauge field theories on a lattice*, Ann. Phys. 110 (1978), 440–471, DOI `10.1016/0003-4916(78)90039-8`.

They verify physical positivity for lattice Schwinger functions, obtaining a positive self-adjoint transfer matrix, and prove existence/analyticity of the infinite-volume limit in a strong-coupling regime together with Wilson confinement bounds. Shen–Zhu–Zhu explicitly describe the earlier cluster expansion as uniform in volume.

This source does not turn the SZZ stochastic functional-inequality gap into the physical Hamiltonian spectral gap, nor does it supply continuum-limit gap transport.

## Audit result

For the **specific SZZ strong-coupling smooth-cylinder covariance family**, plain thermodynamic-volume deterioration is no longer accurately described as merely `PARTIAL`:

`G3-SZZ = SUPPORTED_INFINITE_VOLUME_STRONG_COUPLING_COVARIANCE`

The source already supplies an infinite-volume covariance theorem and an `L`-independent finite-volume prefactor before the limiting passage. Therefore the spectral lane should not spend its next cycle trying to re-prove generic `L`-uniformity for this exact source family.

This does **not** promote the global `G3` obligation to a physical transfer-gap theorem. The result is scoped to the stated strong-coupling Euclidean covariance setting.

## What remains unresolved

The audit moves the high-information boundary rather than closing the Yang–Mills route:

1. **Source/OS binding (`G4`)** — the controlled smooth-cylinder class must be placed in the same reconstructed physical Hilbert space and shown dense/cyclic enough to exclude hidden low-energy states.
2. **Observable-family growth** — `c1` depends on support sizes. If RG blocking makes the relevant source family grow in support/complexity, ordinary `L`-independence does not give a uniform multiscale estimate. This is a more precise uniformity residual than box volume alone.
3. **RG transport (`G5`)** — the theorem lives at explicit strong coupling. No source here supplies a rigorous comparison carrying a gap-sensitive quantity from the asymptotically-free weak bare-coupling trajectory into this regime.
4. **Physical-unit scaling (`G6`)** — no `a -> 0` lower bound on `-a^{-1} log(lambda_1/lambda_0)` follows from the lattice-unit covariance exponent.
5. **Continuum spectral identification (`G7`)** — no continuum OS/Hamiltonian spectral-convergence theorem is supplied.
6. **Boundary/sector scope** — uniqueness of the infinite-volume stochastic solution is not automatically uniform control of every gauge-theory transfer-matrix sector or every boundary implementation relevant to a spectral theorem.

## Refined residual

The most useful successor to generic `YM-S1b` is therefore not “does the box-size limit exist?” but:

> **`YM-S1b1 — source-family/support uniformity`:** along a proposed RG/coarse-graining transport, can the source/support-dependent prefactors and norms be controlled uniformly enough that the common exponential rate remains informative for the growing family needed for spectral completeness?

This child is a context/measurement refinement only. Any mathematical candidate for `YM-S1b1` requires a fresh MathContextFiber, analogue/method-transfer matrix, same-context expert review, dual-memory review and hash-chained pre-candidate trace.

## Route decision

Keep `YM-S1a1` as the active spectral candidate lane once its separate exact-head pre-candidate CI passes. Reclassify ordinary thermodynamic `L`-uniformity for the SZZ covariance theorem as source-supported, and redirect future `G3` work toward **support-family/RG uniformity** rather than repeating finite-box convergence analysis.
