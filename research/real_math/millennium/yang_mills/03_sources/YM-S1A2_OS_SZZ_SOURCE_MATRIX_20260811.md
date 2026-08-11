# YM-S1a2 primary-source matrix — OS reconstruction × SZZ common exponent

**Atom:** `YM-S1a2`  
**Frozen before candidate:** 2026-08-11T12:11:00+00:00  
**Framework authority inspected:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Application parent:** `RAKL_math@e76f8eed763bbe45d91a7b97ed671ed2573e11fa` (PR #79 head)  
**Authority:** `PRIMARY_SOURCE_PACKET / PRE_CANDIDATE / NO_THEOREM_AUTHORITY`

## Exact question

Can the common exponential covariance rate proved by Shen–Zhu–Zhu for the unique infinite-volume strong-coupling Wilson lattice Yang–Mills measure be inserted into the positive physical transfer-matrix spectral lemma from `YM-S1a1-C001-v2`, using the same gauge-invariant positive-time source family after Osterwalder–Schrader reconstruction?

The packet keeps fixed-cutoff strong-coupling transfer spectrum separate from RG transport (`G5`), physical lattice-spacing scaling (`G6`), continuum spectral identification (`G7`), continuum existence, and the Clay root.

## Source A — Shen, Zhu & Zhu (CMP 400, 2023; arXiv:2204.12737)

### Exact retained facts

1. Their finite-volume Wilson lattice Yang–Mills measure uses action `N beta Re sum_p Tr(Q_p)` on a periodic lattice and treats `G = SO(N)` or `SU(N)`.
2. Under Assumption 1.1 they prove that the infinite-volume Langevin invariant measure is unique and that the whole sequence of finite-volume Yang–Mills measures converges to it (Theorem 1.2).
3. `C^infty_cyl(Q)` is the class of smooth functions of finitely many edge variables.
4. Corollary 1.6 applies to **all** `f,g in C^infty_cyl(Q)` with disjoint edge supports and gives

   `Cov(f,g) <= c1 d(g) exp(-c_N d(Lambda_f,Lambda_g)) (|||f|||_infty |||g|||_infty + ||f||_2 ||g||_2)`

   where `c1` depends on source-support cardinalities, while the exponent `c_N` depends on `K_S, N, d`, not on the individual observables.
5. Their text explicitly notes that `f,g` may be Wilson loops or functions of arbitrary numbers of Wilson loops.
6. The same covariance estimate is first established for every tight limit (Corollary 4.11), then uniqueness identifies the limit used in Corollary 1.6.

### Load-bearing consequence for YM-S1a2

For a fixed local source and its Euclidean time translate, source-dependent prefactors are harmless under nth roots. If the edge-support distance grows as `n + O(1)`, the common SZZ exponent would supply one source-independent asymptotic ratio

`q = exp(-c_N) in (0,1)`

in lattice-time units. This is exactly the uniformity coordinate that the `YM-S1a1` hostile world F2 showed to be necessary.

### What this source does **not** by itself prove for this atom

- it does not state that its covariance is the matrix element of the physical OS transfer operator;
- it does not state that the chosen SZZ-controlled source vectors are dense/cyclic in the physical excited Hilbert space;
- its "mass gap" terminology is exponential Euclidean clustering and cannot be silently promoted to the Clay continuum spectral gap;
- its scope is fixed lattice spacing and explicit strong coupling;
- its group scope is `SO(N)` / `SU(N)`.

## Source B — Lüscher (CMP 54, 1977), DOI 10.1007/BF01614090

### Exact retained facts

1. Lüscher formulates OS physical positivity for gauge-invariant polynomials of positive-time fields.
2. Assuming this positivity, the physical Hilbert space is the span of positive-time observables with inner product given by reflected Euclidean expectation, followed by null quotient and completion.
3. He identifies `exp(-a H)` with the operator that shifts positive-time observables by one Euclidean lattice unit.
4. He gives an explicit Wilson-lattice transfer matrix and proves it is self-adjoint, bounded, gauge invariant, and strictly positive (Proposition 1), allowing `H = -(1/a) log T`.
5. His reconstruction theorem (Proposition 2) identifies the transfer-matrix Schwinger functions with the corresponding Euclidean expectations and recovers OS positivity.

### Load-bearing consequence for YM-S1a2

The positive-time gauge-invariant local polynomial algebra is dense **by construction** after the null quotient/completion. Centering those source vectors by subtracting their vacuum component gives a dense set in `Omega^perp`, because orthogonal projection of a dense set is dense in the projected subspace. These local polynomial/Wilson-loop observables are smooth cylinder functions and therefore lie inside the SZZ class.

The remaining difference is finite versus infinite volume. It must be repaired without assuming an unproved strong limit of finite-volume transfer matrices.

## Source C — Osterwalder & Seiler (Ann. Phys. 110, 1978), DOI 10.1016/0003-4916(78)90039-8

The source abstract explicitly states that physical positivity is verified for the lattice Schwinger functions, implying a positive self-adjoint transfer matrix; it also proves existence/analyticity of the strongly coupled infinite-volume lattice Yang–Mills limit and a Wilson confinement bound. For this packet we use it as an independent primary anchor for Wilson-lattice physical positivity and the strong-coupling infinite-volume setting. The exact local weak-limit step below is kept explicit rather than attributing an uninspected theorem statement to this paper.

## Source D — weak-limit preservation of local reflection positivity

This is a proposed elementary transfer step, not yet a candidate theorem at packet-freeze time.

Let `mu_L` be finite-volume Wilson measures that are reflection positive for a fixed reflection plane. For any fixed bounded continuous gauge-invariant positive-time cylinder `F`, the OS quadratic form is an expectation of the bounded continuous local cylinder observable

`h_F(Q) = overline{F(theta Q)} F(Q)`.

If `mu_L -> mu` locally/weakly and the chosen even-volume subsequence is large enough that the fixed source/reflection geometry does not meet the periodic seam, then

`mu(h_F) = lim_L mu_L(h_F) >= 0`.

Because SZZ Theorem 1.2 identifies every tight subsequential limit and the full sequence with the same `mu^ym_{N,beta}`, this would bind finite-volume Wilson reflection positivity to the exact SZZ infinite-volume measure for each fixed local source. Polarization then supplies the sesquilinear OS form.

**Unresolved at packet freeze:** verify the positive-coupling convention and the finite periodic reflection geometry used for the pure-gauge specialization; do not extend the statement to negative beta merely because SZZ allows `|beta|` in its stochastic estimates.

## Source-to-target matrix

| Target obligation | Source support | Status before candidate |
|---|---|---|
| exact infinite-volume Gibbs measure | SZZ Theorem 1.2 | `SOURCE_BOUND` |
| common source-independent exponent | SZZ Corollary 1.6 / 4.11 | `SOURCE_BOUND` |
| smooth local gauge-invariant sources included | SZZ definition of `C^infty_cyl`; Wilson loops explicitly noted | `SOURCE_BOUND` |
| positive-time source algebra dense after OS quotient/completion | Lüscher OS construction | `SOURCE_BOUND_AT_CONSTRUCTION_LEVEL` |
| centered source images dense in `Omega^perp` | bounded projection of a dense source set | `ELEMENTARY_TRANSFER_TO_CHECK` |
| finite-volume physical transfer positivity | Lüscher Proposition 1; Osterwalder–Seiler physical positivity | `SOURCE_BOUND` |
| exact Euclidean expectation ↔ transfer Schwinger function | Lüscher Proposition 2 / OS shift construction | `SOURCE_BOUND_FINITE_VOLUME` |
| reflection positivity of exact SZZ infinite-volume measure | finite RP + SZZ measure convergence | `ELEMENTARY_WEAK_LIMIT_TRANSFER_TO_CHECK` |
| support distance under n-step time translation | finite fixed source geometry | `ELEMENTARY_GEOMETRY_TO_CHECK` |
| common `q=exp(-c_N)` satisfies YM-S1a1-v2 | SZZ + OS identities + parent lemma | `COMPOSITION_TO_CHECK` |
| G5 RG transport | none here | `OPEN` |
| G6 dimensionful a-scaling | none here | `OPEN` |
| G7 continuum spectral identification | none here | `OPEN` |
| Clay root | none here | `OPEN` |

## Sign and scope control

The reflection-positive route is restricted prospectively to **positive Wilson coupling** `beta >= 0` inside the SZZ strong-coupling window. SZZ's stochastic estimates are stated using `|beta|`; this packet does not infer physical reflection positivity for negative beta. Any later theorem must state this narrower scope explicitly.

## Cheapest hostile tests

1. **Hidden-source regression:** if source density is dropped, the registered three-state world with an unseen `1/2` eigenmode defeats the full-gap inference.
2. **Nonuniform-rate regression:** dense sourcewise rates `q_k<1` with `q_k -> 1` have zero full gap; the SZZ exponent must be genuinely source-independent.
3. **Wrong-generator sentinel:** a Poincaré/log-Sobolev gap for the Langevin Markov generator cannot be substituted for the physical Euclidean-time transfer operator.
4. **Negative-beta sentinel:** do not import positive-transfer conclusions from the positive Wilson action into the entire `|beta|` range without a reflection-positive character-expansion proof.
5. **Continuum sentinel:** a fixed-a transfer gap is not a continuum mass gap unless the physical lower bound survives the `a -> 0` path.

## Pre-candidate assessment

The source audit materially sharpens the atom: the SZZ theorem already supplies a common exponent over a class broad enough to contain a dense OS generating algebra. The unresolved work is no longer "find a complete source family" in the abstract. It is to verify the finite-to-infinite reflection-positive handoff and then compose the exact OS moment identity with the SZZ bound under positive strong coupling. Candidate generation remains forbidden until the expert, memory and trace gates are frozen.