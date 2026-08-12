# XM022 — dense-source common-rate spectral exclusion

**Cycle:** `XM022-HODGE-YM-POSTNULL-SPECTRAL-COVERAGE-20260812`  
**Atom:** `XM022-YM-POSTNULL-DENSE-SOURCE-SPECTRAL-EXCLUSION`  
**Authority:** scoped abstract mathematical lemma, same-context verification only; no Yang–Mills theorem, no novelty claim, no root authority.

## Lemma

Let `H` be a Hilbert space and let `T` be a bounded positive self-adjoint operator with `0 <= T <= I`. Fix `q0` with `0 < q0 < 1`. Let `D subset H` be dense. Assume that for every `v in D` there is a finite constant `C_v` such that

`0 <= <v,T^n v> <= C_v q0^n`

for every integer `n >= 0`.

Then the spectral projection `1_(q0,1](T)` is zero. Consequently `sigma(T) subset [0,q0]` and `||T|| <= q0`.

### Proof

Let `mu_v` be the positive spectral measure of `T` associated to `v`. Then

`<v,T^n v> = integral_[0,1] lambda^n d mu_v(lambda)`.

Fix `v in D`. If `mu_v((q0,1]) > 0`, then because

`(q0,1] = union_{k>=1} [q0 + 1/k,1]`

after discarding empty terms, there is some `epsilon > 0` with
`mu_v([q0+epsilon,1]) > 0`. Therefore

`<v,T^n v> >= (q0+epsilon)^n mu_v([q0+epsilon,1])`.

Dividing by `q0^n` makes the right-hand side grow like
`(1+epsilon/q0)^n`, contradicting the finite bound `C_v`. Hence
`mu_v((q0,1])=0` for every `v in D`.

Writing `P=1_(q0,1](T)`, positivity of the spectral measure gives
`||P v||^2=<v,Pv>=0` for every `v in D`. Since `P` is bounded and `D`
is dense, `P=0`. Because `T` is positive, no spectral point exceeds
`q0`, so `||T||<=q0`. QED.

## Transfer-matrix corollary

If, on a fixed-cutoff reconstructed excited Hilbert space, `T=e^{-a H_exc}`
for `a>0` and a positive self-adjoint Hamiltonian `H_exc`, then the lemma
with `q0=e^{-a m0}` implies `inf sigma(H_exc) >= m0`.

This corollary is conditional on the exact same-theory identifications:
the controlled Euclidean source must map to the displayed Hilbert vector,
the measured correlation must equal the positive transfer moment, and the
post-null source image must be dense in the excited space. It says nothing
about uniformity as `a -> 0` or the continuum Clay mass gap.

## DifferenceWitness: density is essential

Let `H=span(v1,v2)`, choose `0<q0<r<1`, and define

`T v1=(q0/2) v1`, `T v2=r v2`.

For the non-dense source subspace `D=span(v1)`, every source obeys
`<v,T^n v> <= ||v||^2 q0^n`, yet `T` has the hidden slower mode `r>q0`.
Thus source-family decay does not identify the full gap without
post-null density/cyclicity.

## DifferenceWitness: a common rate is essential, but a uniform prefactor is not

Let `H=ell^2(N)`, `T e_j=r_j e_j` with `0<r_j<1` and `r_j -> 1`, and
let `D=c_00` be the finitely supported vectors. Then `D` is dense. For
each fixed `v in D`, with `q_v=max{r_j: v_j != 0}<1`,

`<v,T^n v> <= ||v||^2 q_v^n`.

Every fixed source therefore has an exponential rate, but there is no
common `q0<1` and `||T||=1`, so no positive global gap follows.

In contrast, the lemma allows the prefactor `C_v` to depend arbitrarily
on `v`: once the rate `q0` is common and the source image is dense, the
spectral projection argument excludes hidden slower modes without a
uniform bound on `C_v`.

## Target-side interpretation

This falsifies an over-strong import of the earlier pointwise-to-diagonal
uniformity warning into the positive transfer-moment setting. At a fixed
lattice cutoff, **if** a Yang–Mills source family is dense after the OS
null quotient and **if** its same-theory correlations are exactly positive
transfer moments with one common exponential rate, source-dependent finite
prefactors are not an additional abstract obstruction to spectral
exclusion.

The current Yang–Mills application residual is therefore sharper, not
closed:

1. bind SZZ-style decay to exact same-theory OS transfer moments for the
   controlled source class;
2. prove post-null quotient density/cyclicity of that class in the
   relevant excited Hilbert space;
3. identify the reconstructed spectral exclusion with the physical
   fixed-cutoff excitation sector;
4. separately prove lattice-spacing/RG/continuum transport.

Shen–Zhu–Zhu's strong-coupling result establishes exponential decay for a
large class of lattice observables, but this artifact does not infer the
missing OS moment or density interfaces from that statement. Lüscher's
positive transfer-matrix construction is fixed-lattice input, not a
continuum mass-gap theorem.

## Source / provenance boundary

- Hao Shen, Rongchan Zhu, Xiangchan Zhu, arXiv:2204.12737.
- Martin Lüscher, DESY-76-054 / DOI 10.1007/BF01614090.
- Konrad Osterwalder and Robert Schrader, CMP 31 (1973), DOI 10.1007/BF01645738.
- Konrad Osterwalder and Robert Schrader, CMP 42 (1975), DOI 10.1007/BF01608978.
- Application source result: `MATH-HODGE-C004-PROJECTION-KERNEL-NONIMPLICATION`.
- Same-domain warning: `FM-YM-SAME-THEORY-INTERFACE-AND-DENSITY`.

No primary source above is claimed to contain this repository-local
cross-problem formulation, and no literature novelty search is promoted
from this cycle.
