# YM-S1a2 C001 R11 — conditional density of smooth gauge-invariant cylinder sources after the OS quotient

**Authority:** proposal/shadow only. **Novelty class:** `RAKL_TRIVIAL` (direct/compositional functional analysis; no research-novelty claim). **Root authority:** none.

## Scope

This candidate attacks only witness (iv) in `F-YM-S1A2-OS-SZZ-SAME-THEORY-GLUING-UNBOUND`: source density after the Osterwalder–Schrader null quotient. It is deliberately conditional on a **single same measure** carrying the Euclidean, gauge, and reflection-positive structures. It does **not** establish that the Shen–Zhu–Zhu infinite-volume measure is the same reflection-positive physical measure, does not identify its covariance with a transfer-matrix moment, and does not address lattice-spacing/RG/continuum transport.

## Conditional local lemma

Let `G` be a compact Lie group and let the positive-time edge set `E_+` be countable. Put `Q_+=G^{E_+}` with its product Borel sigma algebra. Let `mu` be a Borel probability measure on the full reflected lattice configuration space and `mu_+` its positive-time marginal. Assume:

1. `mu` is invariant under the compact product gauge group acting on edge variables and invariant under the Euclidean time reflection `theta`;
2. reflection positivity holds on the positive-time algebra, so
   `(<[F],[H]>_OS := mu(conj(theta F) H))`
   is positive semidefinite and its quotient-completion is `H_OS`;
3. the gauge-invariant physical sector is obtained by the corresponding gauge-invariant positive-time subspace; and
4. `Omega=[1]` is normalized.

Then the quotient images of centered, smooth, gauge-invariant positive-time cylinder functions have dense linear span in `Omega^perp` inside the gauge-invariant OS Hilbert sector.

### Proof

**Step 1 — cylinder density in `L^2(mu_+)`.** `Q_+` is compact metrizable because it is a countable product of compact metrizable spaces. The algebra of continuous finite-coordinate cylinder functions contains constants and separates points, so Stone–Weierstrass makes it uniformly dense in `C(Q_+)`. Continuous functions are dense in `L^2(mu_+)` for a Borel probability measure on a compact metric space. On each finite coordinate block `G^n`, smooth functions are uniformly dense in continuous functions. Hence smooth positive-time cylinder functions are dense in `L^2(mu_+)`.

**Step 2 — gauge-invariant density.** Let `K` be the compact product gauge group. Haar averaging defines the `L^2(mu_+)` contraction `P` onto the gauge-invariant subspace because `mu` is gauge invariant. If `F` depends on finitely many edges, the action on `F` depends only on gauge variables at finitely many incident vertices; therefore `PF` is still a finite-coordinate cylinder function, and compact-group integration preserves smoothness on its finite `G^n` coordinate block. For any gauge-invariant `H` and smooth cylinders `F_j -> H` in `L^2`,

`||P F_j-H||_2 = ||P(F_j-H)||_2 <= ||F_j-H||_2 -> 0`.

Thus smooth gauge-invariant positive-time cylinders are dense in the gauge-invariant `L^2(mu_+)` sector.

**Step 3 — the OS quotient map is `L^2`-continuous.** For any positive-time `F`, reflection positivity makes the OS square norm nonnegative, while Cauchy–Schwarz and reflection invariance give

`||[F]||_OS^2 = mu(conj(theta F) F) <= ||theta F||_{L^2(mu)} ||F||_{L^2(mu)} = ||F||_{L^2(mu)}^2`.

For positive-time functions the full-measure `L^2(mu)` norm equals the marginal `L^2(mu_+)` norm. Therefore `L^2` approximation by smooth gauge-invariant cylinders implies OS-norm approximation after the null quotient.

**Step 4 — centering is dense in the excited sector.** Since `theta 1=1`,

`<Omega,[F]>_OS = mu(F)`.

Let `psi in Omega^perp` and choose smooth gauge-invariant cylinders `F_j` whose quotient vectors converge to `psi`. Then `mu(F_j)=<Omega,[F_j]>_OS -> <Omega,psi>_OS=0`. Hence

`[F_j-mu(F_j)] -> psi`,

and every approximant is centered, smooth, gauge invariant, positive-time, and cylindrical. This proves dense span in `Omega^perp`. QED.

## Counterexample-first controls and assumption audit

The proof is not a cross-context density transfer. If the `L^2` approximation is taken with respect to one measure while the OS form comes from another, Step 3 gives no bridge. If reflection invariance is absent, `||theta F||_2=||F||_2` is unavailable. If gauge invariance of `mu` is absent, Haar averaging need not be an `L^2(mu)` contraction/projection onto the desired sector. If the controlled source family were merely a finite collection, density could fail exactly as in the hidden-state calibration underlying `YM-S1a1`. These are load-bearing hypotheses, not cosmetic regularity assumptions.

A fixed-graph spin-network completeness theorem is therefore unnecessary for this coordinate and was rejected as an avoidable transfer: direct compact-product density plus the OS norm inequality remains in the same prospective theory. This does **not** make the local lemma self-applying to SZZ; the same-measure/reflection-positive identification remains open.

## Binding to the SZZ source family

Shen–Zhu–Zhu define `C_cyl^infty(Q)` as functions of finitely many edge variables through a smooth function on `G^n` (their (1.8)). Their Corollary 1.6 gives exponential covariance decay for disjoint-support `f,g` in that class, with a common exponential constant `c_N` depending on the strong-coupling parameters while finite source/support factors remain in the prefactor. Thus the regularity class required by this density lemma is not narrower than the paper's stated smooth-cylinder class. This is only a source-family compatibility observation: the paper's Euclidean covariance statement is not, by itself, a physical Hamiltonian spectral-gap theorem.

## Expert-cell synthesis (same-context, not independent review)

- **Constructive QFT / OS reconstruction:** Step 3 is the decisive topology bridge; same-measure reflection invariance/positivity must be source-bound before application.
- **Spectral/operator theory:** `YM-S1a1_C001_V2` needs dense span in `Omega^perp`; cyclicity is stronger than necessary for that local spectral-support exclusion lemma.
- **Lattice gauge theory:** compact gauge averaging preserves finite support and smoothness; gauge invariance of the measure is essential.
- **SZZ / stochastic lattice YM:** the stated smooth-cylinder source class is broad and Cor. 1.6 has one exponential distance exponent, but its stochastic/Langevin machinery is not the physical transfer Hamiltonian.
- **Adversarial barrier audit:** density alone leaves the exact covariance-to-transfer-moment identity, time-support geometry, physical transfer identification, and all `a -> 0` obligations open.
- **Formal/metrology:** this closes at most one conditional local coordinate; no root, theorem-authority, formal-proof, or isolated-review promotion is permitted.

## Residual / gluing ledger

**Local mathematical coordinate:** conditional source density after OS quotient — `CLOSED_IF_ASSUMPTIONS_BOUND`.

**Local-to-global / same-theory gluing remains OPEN:**

1. prove that the exact infinite-volume measure used for the SZZ decay estimate is the same reflection-positive measure entering the OS reconstruction;
2. prove for centered positive-time gauge-invariant sources the exact translated covariance identity `Cov(F,tau_n F)=<psi_F,T^{n+c_F}psi_F>` (or the precisely correct boundary-offset variant) for the physical positive transfer matrix;
3. prove support distance under translation is `n+O(1)` in the chosen time direction so the SZZ common exponent becomes a common transfer ratio;
4. preserve the same theory/operator/source algebra under any thermodynamic and regulator limits used next;
5. obtain lattice-spacing-uniform physical normalization and continuum spectral identification. A fixed-lattice decay rate is not the Clay mass gap.

## Primary provenance

- H. Shen, R. Zhu, X. Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, arXiv:2204.12737; `C_cyl^infty` at (1.8), Corollary 1.6 for exponential covariance decay. Source rechecked 2026-08-12, including visual PDF inspection of pages containing (1.8) and Corollary 1.6.
- K. Osterwalder and E. Seiler, *Gauge field theories on a lattice*, Annals of Physics 110 (1978), DOI 10.1016/0003-4916(78)90039-8. Used only as historical/structural OS-transfer provenance here; no uninspected theorem text is imported into the proof above.
- A. Jaffe and E. Witten, *Quantum Yang-Mills Theory*, Clay Millennium problem description, for root scope.

**Outcome:** local conditional lemma proved; same-theory OS/SZZ/transfer gluing still open; root remains `OPEN_NO_SOLUTION_CERTIFICATE`.