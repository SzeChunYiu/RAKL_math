# YM-S1a2c C001 R12 — reflection positivity passes to the SZZ strong-coupling thermodynamic limit

**Authority:** proposal/shadow verification only. **RAKL novelty class:** `compositional` (same-domain composition of a classical Wilson positivity theorem with weak convergence; no literature-novelty claim). **Root authority:** none.

## Exact scope

Fix `d=4`, `G=SU(N)`, and `0 < beta < 1/[16(d-1)] = 1/48`. Let `mu_{Lambda_L,N,beta}` be the periodic finite-volume Wilson plaquette measures of Shen–Zhu–Zhu (SZZ), and `mu^ym_{N,beta}` their unique thermodynamic limit from SZZ Theorem 1.2. Fix a standard lattice time reflection `theta` and restrict to bounded continuous **gauge-invariant** positive-time cylinder functions.

The statement below closes only the same-measure reflection-positivity witness in `F-YM-S1A2-OS-SZZ-SAME-THEORY-GLUING-UNBOUND`. It does not yet identify SZZ covariances with transfer moments or prove a physical spectral gap.

## Source-bound ingredients

1. SZZ define the finite-volume measure on periodic `Lambda_L` by
   `d mu = Z^{-1} exp(N beta Re sum_p Tr Q_p) prod_e d sigma_N(Q_e)`; see arXiv:2204.12737v1, (1.1)–(1.2), pp. 3–4. Their Theorem 1.2(2), p. 5, states that every tight limit is the same and the **whole sequence** converges to `mu^ym_{N,beta}` under the strong-coupling assumption. Remark 1.3 additionally says the same limit is obtained after changing periodic to Dirichlet or other boundary conditions.
2. Lüscher, *Commun. Math. Phys.* **54** (1977), 283–292, DOI `10.1007/BF01614090`, constructs the physical Hilbert space and transfer matrix for Wilson `SU(N)` lattice gauge theory. Proposition 1 proves the transfer matrix is selfadjoint, bounded, gauge invariant and strictly positive. Proposition 2 reconstructs the Euclidean expectations from the transfer formulation for the stated periodic gauge-field boundary data and explicitly says this proves Osterwalder–Schrader positivity of those Euclidean expectations. The pure-gauge Wilson factor is the needed sector here; we make no use of the fermion factor.

The coupling conventions differ by a positive normalization. Only the sign matters for the positivity kernel in this local binding, so the candidate is restricted to `beta>0`; no claim is made for negative `beta` allowed by SZZ's stochastic estimates.

## Lemma

Let `L_j -> infinity` be any cofinal subsequence of periodic lattice sizes compatible with the chosen time reflection (for example the parity class matching the finite-time reflection convention). Assume the finite-volume Wilson expectation on this subsequence obeys OS positivity on gauge-invariant positive-time cylinder functions, as in Lüscher's Wilson construction. Then `mu^ym_{N,beta}` is reflection positive on bounded continuous gauge-invariant positive-time cylinder functions:

`mu^ym_{N,beta}( overline(theta F) F ) >= 0`.

Moreover the same limiting measure is gauge invariant and reflection invariant on bounded continuous cylinder functions.

### Proof

Take a bounded continuous gauge-invariant positive-time cylinder `F`. It depends on finitely many links. Hence `theta F` and

`Phi_F(Q) = overline{(theta F)(Q)} F(Q)`

also depend on finitely many links and are bounded continuous functions on the compact product configuration space `Q=SU(N)^{E+}` used by SZZ.

For all sufficiently large reflection-compatible volumes, the support of `F` and its reflection embeds without ambiguity in the periodic finite lattice. Finite-volume Wilson physical/OS positivity gives

`int Phi_F d mu_{Lambda_{L_j},N,beta} >= 0`.

SZZ Theorem 1.2(2) gives weak convergence of the **whole** sequence of periodically extended measures to `mu^ym_{N,beta}`. In particular the selected cofinal subsequence has that same limit. Because `Phi_F` is bounded and continuous,

`int Phi_F d mu_{Lambda_{L_j},N,beta} -> int Phi_F d mu^ym_{N,beta}`.

A limit of nonnegative real numbers is nonnegative, proving reflection positivity for `F`.

Gauge invariance and reflection invariance pass by the same bounded-continuous-cylinder argument because each finite Wilson measure is invariant under finite-support gauge transformations and under the matched lattice reflection: for any bounded continuous cylinder `H`, `mu_L(H)=mu_L(H o g)=mu_L(H o theta)` for all large compatible volumes, and weak convergence gives the same identities at the limit. QED.

## Counterexample-first / DifferenceWitness audit

- **Continuity is load-bearing.** Weak convergence does not license passage of an arbitrary unbounded or discontinuous OS quadratic functional. The present cylinder class is safe because compact `SU(N)` and finite support make `Phi_F` bounded continuous.
- **Same action/sign is load-bearing.** A positivity theorem for a gauge-fixed action, negative plaquette coupling, or a different discretization would not glue to SZZ. This candidate uses only the positive-coupling Wilson plaquette sector.
- **Geometry is load-bearing.** The proof uses only a cofinal reflection-compatible periodic subsequence, and SZZ whole-sequence convergence ensures that selecting it cannot change the limit. It does not infer positivity from an unrelated thermodynamic state.
- **No spectral overpromotion.** Reflection positivity provides the OS positive form. It does not, by itself, prove that SZZ Corollary 1.6 covariance at support distance `d` equals `<psi_F,T^n psi_F>` for the reconstructed physical time-shift operator, nor that `d=n+O(1)` under the required source translation. Those remain separate gluing witnesses.
- **No continuum overpromotion.** All constants and statements here are at lattice spacing `a=1`. Nothing here is uniform as `a->0` in physical units.

## Expert-cell synthesis (same context, not independent review)

- **Constructive QFT/OS:** accepts the closed-cone weak-limit argument on the bounded cylinder algebra; blocks any claim beyond the OS form until the time-shift representation is bound.
- **Lattice transfer matrix:** accepts the Wilson `SU(N)`, positive-coupling match subject to the explicit reflection-compatible periodic finite-volume convention; fermion-specific factors are unused.
- **Weak-limit probability:** accepts the passage because SZZ use the compact product topology and whole-sequence weak convergence; the cofinal-subsequence move is therefore harmless.
- **Spectral theory:** classifies the result as a prerequisite, not a gap theorem. The hidden-state/common-rate issue remains governed by the dense-source lemma and a true transfer-moment identity.
- **RG/continuum:** records volume-uniform thermodynamic identification as locally handled, while lattice-spacing uniformity/physical normalization remain fully open.
- **Adversarial provenance/RAKL:** classifies the prior compound same-theory failure as partially resolved: witness `(same limiting measure is reflection positive)` now has a proposal/shadow proof; witness `(SZZ covariance = physical transfer moments with time-distance control)` remains open. No canonical obstruction/lesson promotion is authorized.

## Residual transformation

**Before:** `RES-YM-S1a2-SAME-MEASURE-RP + COVARIANCE-TRANSFER-MOMENT + TEMPORAL-DISTANCE + SOURCE-DENSITY + a/RG/CONTINUUM`.

**After this candidate, if source review accepts the finite-volume convention match:** `RES-YM-S1a2-COVARIANCE-TO-OS-TIME-SHIFT-MOMENT + TEMPORAL-SUPPORT-DISTANCE + (R11 conditional density witness) + a/RG/CONTINUUM`.

Local mathematical status: `PASS_PROPOSAL_SHADOW`. Local-to-global/gluing status: `PARTIAL_ONLY`; the load-bearing transfer-moment identification is still open.

## Next discriminator

For one centered smooth gauge-invariant positive-time cylinder `F`, construct the exact infinite-volume OS class `psi_F=[F]`, define the lattice time-shift operator on the same quotient, and prove the identity between the centered translated SZZ covariance and `<psi_F,T^n psi_F>` with a source-support offset bounded independently of `n`. Then verify that SZZ Corollary 1.6 converts the support distance to `n+O(1)` with its common exponent. Only after that witness and the R11 density lemma are simultaneously bound in this same measure may the abstract dense-source spectral-exclusion lemma be instantiated at fixed cutoff.
