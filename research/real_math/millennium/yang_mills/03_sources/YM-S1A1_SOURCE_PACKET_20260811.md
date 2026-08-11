# YM-S1a1 primary-source packet — 2026-08-11

**Atom:** `YM-S1a1` — dense-source common-rate spectral exclusion at fixed lattice cutoff/infinite volume.

**Authority:** `SOURCE_BOUND_PRE_CANDIDATE_CONTEXT / NO_MATHEMATICAL_CANDIDATE_YET / ROOT_AUTHORITY_NONE`.

## Exact research question

The previous exact calibration showed that exponential decay for a restricted source family can miss a lower transfer-matrix excitation. This child asks whether the repair can be made precise:

> Under the same reflection-positive lattice theory, can a source class that is dense/cyclic in the physical excited-state Hilbert space and has one common exponential Euclidean-time decay exponent force a lower bound on the full transfer-matrix/Hamiltonian gap?

The answer is not assumed. This packet freezes the source facts needed to decide what candidate is legal to formulate.

## Primary sources and exact scope

### Osterwalder–Seiler 1978

K. Osterwalder and E. Seiler, *Gauge field theories on a lattice*, Annals of Physics 110 (1978), 440–471, DOI `10.1016/0003-4916(78)90039-8`.

The paper verifies physical positivity for the lattice Schwinger functions, which implies a positive self-adjoint transfer matrix, and establishes strong-coupling infinite-volume/confinement results. This is the operator bridge source. It does **not** by itself supply a quantitative full spectral gap uniform toward the four-dimensional continuum limit.

### Shen–Zhu–Zhu 2022/2023

H. Shen, R. Zhu, X. Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, arXiv:`2204.12737`, Commun. Math. Phys. 400 (2023).

Under their explicit strong-coupling Assumption 1.1, Corollary 1.6 bounds covariance of disjoint-support smooth cylinder functions by a finite source/support prefactor times `exp(-c_N d(Lambda_f,Lambda_g))`. The exponent `c_N` depends on the strong-coupling/model parameters, while the prefactor can depend on the functions/support sizes. The theorem is directly in infinite volume.

Load-bearing limitation: their Poincaré/log-Sobolev gap is for the stochastic Langevin generator. The present atom may use the **Euclidean covariance decay statement**, but may not identify the Langevin generator with the physical transfer-matrix Hamiltonian.

### Baez 1994

J. C. Baez, *Spin Network States in Gauge Theory*, arXiv:`gr-qc/9411007`.

For a compact connected Lie group, Baez constructs spin-network spanning vectors and an orthonormal spin-network basis associated to a fixed graph. This supports a kinematic completeness coordinate for gauge-invariant finite-graph functions.

Load-bearing limitation: this Hilbert-space construction is not automatically the exact infinite-volume Osterwalder–Schrader physical Hilbert space of the SZZ Gibbs measure.

### Burgio et al. 1999

G. Burgio, R. De Pietri, H. A. Morales-Tecotl, L. F. Urrutia, J. D. Vergara, *The basis of the physical Hilbert space of lattice gauge theories*, arXiv:`hep-lat/9906036`.

The paper constructs an orthonormal basis of the physical gauge-invariant Hilbert space of Hamiltonian lattice gauge theories using compact-group harmonic analysis.

Load-bearing limitation: fixed-lattice Hamiltonian basis completeness supplies no common decay rate and is not, without an explicit identification, density in the exact infinite-volume OS reconstruction used by this atom.

## Source synthesis

The sources expose a potentially composable chain but do not yet prove it:

`reflection positivity -> positive transfer matrix`
+
`gauge-invariant local source completeness/density`
+
`one common Euclidean-time covariance exponent`
`=>? full transfer spectral exclusion`.

The candidate-generation step is permitted to propose only the abstract implication after the fresh context/memory/trace gates pass. Applying it to SZZ requires separate proofs of temporal support-distance scaling, covariance-to-transfer-moment identity, and density of the controlled gauge-invariant smooth-cylinder source states.

## Explicit non-claims

- No continuum Yang–Mills existence theorem.
- No weak-coupling/strong-coupling interpolation.
- No claim that the SZZ Langevin spectral gap equals the quantum Hamiltonian mass gap.
- No claim that a fixed-lattice spin-network basis automatically supplies OS cyclicity.
- No novelty claim for the spectral-theorem implication.
