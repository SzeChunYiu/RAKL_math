# YM-S1A1-C001 — Dense common-rate spectral exclusion

**Atom:** `YM-S1a1`  
**Candidate:** `YM-S1A1-C001`  
**Framework authority inspected for this run:** `SzeChunYiu/RAKL@b4be08e0df4b099f6d5eb1dce191c85063e71c21`  
**Application base:** `SzeChunYiu/RAKL_math@39bdd688bfd7cfc4a6f2d1e4201397c52e0975a7`  
**Root state:** `OPEN_NO_SOLUTION_CERTIFICATE`  
**Authority of this artifact:** abstract fixed-cutoff operator lemma only; it is not a Yang–Mills mass-gap theorem.

## Bound pre-candidate packet

Candidate generation is bound to the already-frozen `YM-S1a1` packet:

- `01_frontier/YM-S1A1_CONTEXT_FIBER_20260811.json`
- `03_sources/YM-S1A1_SOURCE_PACKET_20260811.md`
- `07_memory/YM-S1A1_RESEARCH_TOOL_INVENTORY_20260811.json`
- `07_memory/YM-S1A1_FAILURE_EXPERIENCE_LATTICE_20260811.json`
- `07_memory/YM-S1A1_RESEARCH_MEMORY_REVIEW_20260811.json`
- `08_reviews/YM-S1A1_PRE_CANDIDATE_REVIEW_20260811.md`
- `09_trace/YM-S1A1_PRE_CANDIDATE_TRACE_20260811.json`

The pre-candidate trace ends at event hash
`sha256:7c93020929cde30bcc7ed92a5300f7e938064655cc24033ce0fe602c12b1edaf`.

## Exact statement

Let `H_0` be a Hilbert space and let `T:H_0 -> H_0` be a positive self-adjoint contraction. Let `D` be a dense subset of `H_0`. Suppose that there is one number `q in [0,1)` such that for every nonzero `psi in D`,
\[
 \limsup_{n\to\infty} \langle \psi,T^n\psi\rangle^{1/n}\le q.
\]
Then
\[
 \|T\|\le q,
 \qquad
 \sigma(T)\subset[0,q].
\]

Consequently, if in a separately established physical transfer-matrix representation on the excited space one has
`T = exp(-a_t H)` with `a_t>0`, then for `q in (0,1)` the same fixed-cutoff representation has
\[
 \inf \sigma(H)\ge -a_t^{-1}\log q.
\]
This consequence is conditional on the transfer/Hamiltonian identification; this lemma does not establish that identification for Yang–Mills.

## Proof

Let `E_T` denote the projection-valued spectral measure of `T`. Positivity and contractivity give
`support(E_T) subset [0,1]`.

Fix any `r>q`. Assume for contradiction that
\[
 P_r:=E_T((r,1])
\]
is nonzero. Since `D` is dense, `D` cannot be contained in the closed subspace `ker P_r`; otherwise
`H_0 = closure(D) subset ker P_r`, forcing `P_r=0`. Hence there is a nonzero `psi in D` with `P_r psi != 0`.

Let
\[
 \mu_\psi(B)=\langle\psi,E_T(B)\psi\rangle.
\]
Then
\[
 \mu_\psi((r,1])=\|P_r\psi\|^2>0.
\]
By the spectral theorem and positivity,
\[
 \langle\psi,T^n\psi\rangle
 =\int_{[0,1]}\lambda^n\,d\mu_\psi(\lambda)
 \ge r^n\mu_\psi((r,1]).
\]
Taking nth roots and then `liminf`,
\[
 \liminf_{n\to\infty}
 \langle\psi,T^n\psi\rangle^{1/n}
 \ge r,
\]
because the positive constant `mu_psi((r,1])` has nth root tending to one. This contradicts the common-rate hypothesis
`limsup <= q < r`.

Thus `E_T((r,1])=0` for every `r>q`. If the spectrum contained any `lambda>q`, choosing `r` with
`q<r<lambda` would contradict the support property of the spectral measure. Therefore
`sigma(T) subset [0,q]`. Since `T` is positive self-adjoint,
`||T|| = sup sigma(T) <= q`. QED.

## Quantifier and endpoint audit

1. `D` need not be a linear subspace; density alone is used.
2. The same `q` must work for every nonzero source in `D`. Source-dependent rates are insufficient.
3. Source-dependent finite prefactors do not alter the nth-root exponent.
4. The endpoint `q` is allowed in the spectrum; the conclusion is `<=q`, not `<q`.
5. For `q=0`, the abstract conclusion is `T=0` on `H_0`. No finite physical-energy interpretation is asserted from the logarithmic formula.
6. Positivity is used to avoid cancellation in the moment integral. The statement is not transferred to a merely self-adjoint contraction with negative spectrum without reformulation.

## Planted known-answer worlds

### Failure world: old hidden source

Take `H_0=R^2`, `T=diag(1/2,1/4)`, and the tested family
`D=span{e_2}`. Every tested nonzero vector has nth-root moment rate `1/4`, yet `||T||=1/2`.
This does **not** contradict the lemma: `D` is not dense. It reproduces
`F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE` and verifies the DifferenceWitness.

### Success world: spanning/dense source family

For the same `T`, take `D=Q^2`, viewed as a dense subset of `R^2`. Vectors with nonzero first coordinate have rate `1/2`; vectors supported on `e_2` have rate `1/4`. Therefore the smallest common admissible rate is `q=1/2`, exactly `||T||`.

### Endpoint world

For `T=diag(q,q/2)` with `0<q<1` and dense `D`, the common rate can equal `q`; the conclusion permits the spectral endpoint `q`.

## Six-role result review

The result was checked through six complementary roles, each working against the same frozen context.

1. **Transfer-matrix / lattice-gauge specialist:** checked that the lemma is stated only on an already-constructed physical excited Hilbert space and does not manufacture reflection positivity, a transfer matrix, gauge projection, or the `T=e^{-a_tH}` normalization.
2. **Operator / spectral-theory specialist:** owned the projection-valued-measure proof and checked the density argument, endpoint `q`, and the equivalence `||T||=sup sigma(T)` for positive self-adjoint `T`.
3. **Strong-coupling / cluster-expansion specialist:** checked that only a common asymptotic exponent is consumed; support/source-dependent finite prefactors are deliberately not promoted to uniform constants.
4. **RG / asymptotic-freedom specialist:** checked that the lemma has no coupling interpolation, no lattice-spacing uniformity, and no continuum extrapolation authority.
5. **OS / constructive-QFT specialist:** checked that Euclidean covariance-to-transfer-moment identification, null-space quotienting, centering, time translation, and same-theory source density remain separate open target hypotheses.
6. **Formal / adversarial assurance specialist:** checked the planted hidden-mode failure, spanning success world, endpoint case, `q=0`, and quantifier order.

The cell found no defect in the abstract implication. This is same-context assurance, not an independent root review.

## Exact scope update

This closes only the **abstract logical sub-bridge** inside `G4`:

> if a Yang–Mills construction supplies a positive self-adjoint excited transfer operator, a dense controlled source family in that same reconstructed Hilbert space, and one common nth-root transfer-moment rate, then hidden slower spectral modes are excluded.

It does **not** establish any of those Yang–Mills-specific hypotheses.

Open residuals remain:

- **G4-target binding:** prove that the controlled Euclidean gauge-invariant source class maps, in the same OS-reconstructed theory, to a dense/cyclic subset of the excited Hilbert space and that the covariance bound is exactly a transfer-moment bound after all quotients/centerings.
- **G3/source-family uniformity:** control support/complexity growth for the source family needed under blocking.
- **G5:** transport quantitative control from the rigorous strong-coupling regime toward the continuum/asymptotically-free trajectory without an uncontrolled phase/coupling barrier.
- **G6:** obtain a physical lower bound `-a_t^{-1} log q(a)` that remains positive uniformly as lattice spacing tends to zero.
- **G7:** identify the limiting continuum physical spectrum and show the bound survives reconstruction/continuum extrapolation.
- Continuum Yang–Mills existence and the Clay root remain open.

## Candidate verdict

`SUPPORTED_ABSTRACT_LEMMA / TARGET_BINDING_OPEN`

No root promotion is permitted.
