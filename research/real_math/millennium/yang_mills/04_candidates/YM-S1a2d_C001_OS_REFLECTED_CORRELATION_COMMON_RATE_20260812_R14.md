# YM-S1a2d-C001 R14 — Same-theory reflected-correlation common-rate envelope

**Authority:** `PROPOSAL_SHADOW_LOCAL_COMPOSITION / SAME_CONTEXT_CHECKED / NO_OPERATOR_REALIZATION / NO_PHYSICAL_GAP / NO_ROOT_AUTHORITY`  
**Root:** #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Atom:** #253 (`YM-S1a2d-SZZ-OS-TIME-SHIFT-MOMENT-SUPPORT-GROWTH`)  
**Frozen fibre:** `sha256:a5d653721edaffb1358834e5c4d6f6f0bf848328ff9ffa5e86e1e9db1358bf79`  
**Scope:** `d=4`, `G=SU(N)`, fixed unit lattice spacing, exact SZZ strong-coupling infinite-volume Wilson measure, `0 < beta < 1/48`.

## Exact local question

The already-registered abstract candidate `YM-S1A1-C001-V2` says that a positive self-adjoint contraction has no excited spectrum above a common transfer ratio `q<1` if a dense excited source family has common nth-root moment rate at most `q`. The remaining target-facing question is not that spectral lemma. It is whether the exact SZZ strong-coupling Euclidean correlations can be typed as the required same-theory nonnegative time-shift forms with a common exponential rate.

This cycle closes only the **Euclidean reflected-correlation + temporal support** coordinate. It deliberately leaves the existence/well-definedness of the exact infinite-volume one-step OS operator on the null quotient open.

## Primary-source packet and exact provenance

### SZZ

H. Shen, R. Zhu, X. Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, arXiv:2204.12737 / Commun. Math. Phys. 400 (2023).

The current arXiv HTML surface inspected on 2026-08-12 renders a manuscript date `March 22, 2026`; the linked PDF surface is explicitly `arXiv:2204.12737v1`, dated April 2022. The theorem selectors used below were checked on that linked v1 PDF. **No unverified 2026-text delta is silently imported.**

Relevant v1 PDF selectors:

- (1.1)–(1.3): periodic Wilson measure and the `SU(N)` strong-coupling condition `|beta|<1/[16(d-1)]`;
- Theorem 1.2: whole finite-volume sequence converges to the unique infinite-volume measure `mu^ym_{N,beta}`;
- (1.8): `C^infty_cyl(Q)` consists of real-valued smooth functions of finitely many edge variables;
- Corollary 1.6 / Corollary 4.11: for disjoint finite edge supports,
  `Cov_mu(f,g) <= c_1 dim(g) exp(-c_N d(Lambda_f,Lambda_g)) (|||f|||_inf |||g|||_inf + ||f||_2 ||g||_2)`,
  where the exponent `c_N>0` depends on the strong-coupling constant, `N`, and `d`, while the finite prefactor may depend on source support sizes;
- the proof of Corollary 4.11 states the finite-volume constant is independent of volume before passing to the infinite-volume limit.

The displayed SZZ inequality is **one-sided**, not an absolute-value estimate. That sign distinction is retained below.

### Wilson reflection/transfer positivity

M. Lüscher, *Construction of a Selfadjoint, Strictly Positive Transfer Matrix for Euclidean Lattice Gauge Theories*, Commun. Math. Phys. 54 (1977), DOI `10.1007/BF01614090`.

Relevant primary selectors: OS positivity (4); the identification of the positive-time one-step shift with `e^{-aH}`; the explicit warning that in a lattice theory an additional argument beyond one OS reflection is needed for `T>0`; Proposition 1 (self-adjoint, bounded, strictly positive finite-volume transfer matrix); and Proposition 2 (finite-volume Euclidean expectations equal transfer-matrix Schwinger functions for the compatible periodic gauge geometry).

P. Menotti and A. Pelissetto, *General Proof of Osterwalder-Schrader Positivity for the Wilson Action*, Commun. Math. Phys. 113 (1987), DOI `10.1007/BF01221251`.

The abstract and Section 2 state that the Wilson action has reflection positivity for gauge-invariant observables at **all Euclidean time separations**. The paper explicitly notes that positivity with respect to both link-cutting and site-containing reflection planes is needed for a positive-definite one-step transfer matrix. Its pure-gauge specialization is the present Wilson gauge sector.

The same finite Wilson action/coupling and compatible cofinal periodic geometry were independently audited in proposal/shadow R13 / PR #240. This R14 record reuses that exact-action match as routing evidence; PR #240 remains unmerged and authority-inert.

## Proposition — nonnegative reflected SZZ correlations with one common rate

Let `mu=mu^ym_{N,beta}` be the SZZ infinite-volume Wilson measure in `d=4`, `G=SU(N)`, `0<beta<1/48`.

Fix one of the standard lattice time reflections used by the Wilson reflection-positivity construction. Write its time-coordinate action as

`theta_kappa(t)=kappa-t`,

with `kappa` fixed by the chosen site/link convention. Let `Theta` be the corresponding antilinear reflection on observables and `tau_n` the positive Euclidean-time translation by `n` lattice units.

Let `F` be a **real-valued**, smooth, gauge-invariant finite-edge cylinder supported in the admissible positive-time region and centered under the exact infinite-volume measure:

`mu(F)=0`.

Then there are finite source-dependent constants `n_F` and `C_F` and one source-independent exponent `c_N>0` from SZZ such that, for every integer `n>=n_F`,

`0 <= mu((Theta F)(tau_n F)) = Cov_mu(Theta F,tau_n F) <= C_F exp(-c_N n)`.

Consequently,

`limsup_{n->infinity} mu((Theta F)(tau_n F))^(1/n) <= exp(-c_N) < 1`.

This is a statement about exact same-theory **Euclidean reflected forms**. It is not yet a statement about powers of an infinite-volume physical transfer operator.

## Proof

### 1. Same-theory nonnegativity survives the infinite-volume limit

Use the reflection-compatible cofinal periodic Wilson volumes from the exact-action match audited in R13: for positive coupling the SZZ gauge weight is the Wilson gauge weight under the identification `g_0^{-2}=N beta`.

For the fixed source `F` and fixed separation `n`, choose the cofinal volumes large enough that `F`, `Theta F`, and `tau_n F` do not meet a periodic wrap seam. Menotti–Pelissetto's all-separation Wilson reflection positivity (equivalently, Lüscher's strictly positive finite-volume transfer matrix plus reconstruction on the matching Wilson theory) gives the finite-volume reflected correlation nonnegativity for this gauge-invariant source and separation.

The integrand `(Theta F)(tau_n F)` is a bounded continuous cylinder on the common compact product configuration space used by SZZ. SZZ Theorem 1.2 gives weak convergence of the whole finite-volume sequence, hence of the cofinal reflection-compatible subsequence. Passing to the limit yields

`mu((Theta F)(tau_n F)) >= 0`.

This step uses finite-volume physical/reflection positivity only as a sign certificate for the exact limiting Euclidean form. It does **not** construct an infinite-volume transfer operator.

### 2. Centering makes the form an exact covariance

Translation invariance of the exact Wilson limit gives

`mu(tau_n F)=mu(F)=0`.

Reflection invariance gives `mu(Theta F)=0` for real centered `F`. Therefore

`mu((Theta F)(tau_n F)) = Cov_mu(Theta F,tau_n F)`.

Gauge averaging/centering do not change finite-coordinate smoothness, so both arguments remain inside the SZZ cylinder class.

### 3. Temporal translation forces affine support separation

Let `Lambda_F` be the finite SZZ edge support of `F`, and let `V_F` be the finite set of lattice vertices incident to those edges. Reflection may reverse edge orientation, but it sends the vertex time coordinate by `t -> kappa-t`. Translation sends it by `t -> t+n`.

Define the finite geometric constant

`A_F = max{|x_0+y_0-kappa| : x,y in V_F}`.

For any vertex of a reflected support edge and any vertex of a translated support edge, the absolute time-coordinate difference is at least

`n-A_F`.

SZZ's edge-support distance is the nearest lattice-vertex distance, which is bounded below by absolute separation in the time coordinate. Hence

`d(theta Lambda_F, tau_n Lambda_F) >= n-A_F`.

For all `n>A_F` the two edge supports are disjoint, so the hypothesis of SZZ Corollary 1.6 applies. This is the exact support-distance/time conversion that was previously missing from the compound gluing residual.

### 4. The SZZ common exponent yields a common nth-root rate

Apply SZZ Corollary 1.6 to the real smooth cylinders `Theta F` and `tau_n F`. The support sizes are fixed in `n`; translation leaves all source norms unchanged, and reflection changes them at most by a fixed source-dependent factor (indeed the Wilson lattice symmetries preserve the underlying bi-invariant edge geometry). Absorb every finite source quantity and `exp(c_N A_F)` into one constant `C_F`.

The one-sided SZZ inequality gives

`Cov_mu(Theta F,tau_n F) <= C_F exp(-c_N n)`.

Step 1 supplies the missing lower sign, so no absolute-value strengthening of the SZZ theorem has been assumed. Combining gives the claimed two-sided envelope. Taking nth roots removes the source-dependent prefactor and yields the common rate `q=exp(-c_N)<1`.

`QED` at proposal/shadow local-composition authority.

## Real versus complex source family

SZZ defines `C^infty` as real-valued smooth functions. This candidate therefore proves the envelope first for real gauge-invariant cylinders. The complex linear span of real and imaginary parts of smooth complex cylinders is the same complex cylinder span, so this restriction is compatible with the separate proposal/shadow source-density lemma in PR #225. **That density result remains unmerged and is not promoted here.**

## Why this still does not instantiate the spectral lemma

The implication

`nonnegative Euclidean reflected forms with common e^{-c_N n} envelope`

`=> positive self-adjoint contraction T on the exact infinite-volume OS quotient with these forms equal to <psi,T^n psi>`

has **not** been proved in this cycle.

The exact remaining operator/gluing obligations are:

1. show that the one-step positive-time translation descends to the null quotient of the exact `mu` OS form;
2. prove on that quotient that the induced operator is bounded/self-adjoint and positive (or bind a primary theorem whose exact hypotheses give those properties for this same infinite-volume Wilson measure);
3. prove the exact moment identity for powers of that operator, not merely for the Euclidean forms before quotienting;
4. combine with a source-density result carrying valid authority in the **same** OS Hilbert space.

Lüscher explicitly warns that one-reflection OS positivity alone does not prove one-step transfer positivity on a lattice. Menotti–Pelissetto explain why link and site reflections are both load-bearing. The sign result above therefore narrows, rather than bypasses, the operator-realization problem.

## Counterexample-first / hostile controls

### H1 — one-sided decay without positivity

A sequence `b_n=-1` satisfies `b_n <= C q^n` for every positive `C` and `0<q<1` once `n` is large enough, but it cannot be a nonnegative spectral moment. Therefore the sign certificate is load-bearing when using SZZ's displayed one-sided covariance inequality.

### H2 — nonnegative exponentially decaying forms without a typed operator

Merely declaring numbers `b_n=q^n` does not construct a Hilbert-space operator, prove null-space invariance of a time shift, or identify a physical Hamiltonian. The exact Euclidean envelope is not itself an operator-realization certificate.

### H3 — sourcewise prefactors are harmless, sourcewise exponents are not

The existing `YM-S1A1-C001-V2` counterexample with dense eigenvectors whose rates approach `1` remains active: source-dependent prefactors disappear under nth roots, whereas source-dependent exponents approaching `1` can hide a zero gap. SZZ supplies the needed common exponent `c_N` at this fixed strong-coupling theory.

### H4 — fixed lattice units are not physical continuum units

Even if an exact fixed-cutoff transfer operator were later bound and gave a lattice Hamiltonian gap `c_N/a`, no Clay-level conclusion follows unless one proves the required regulator/RG/continuum statement along an asymptotically-free continuum trajectory. This cycle supplies no lower bound uniform in lattice spacing in physical units.

## Seven-role same-context expert synthesis

1. **Constructive lattice gauge / OS:** accepts the weak-limit sign passage only on exact matched Wilson measures and keeps the null-quotient shift problem open.
2. **Transfer-matrix:** confirms Lüscher's extra lattice positivity warning and Menotti–Pelissetto's site/link distinction; rejects deriving an infinite-volume one-step operator from R13's single RP coordinate alone.
3. **Spectral/operator:** confirms the common nth-root rate is the correct input shape for `YM-S1A1-C001-V2`, but refuses spectral handoff without an actual positive self-adjoint contraction on the same quotient.
4. **Stochastic/correlation:** verifies SZZ's source class is real smooth finite-edge cylinders, the displayed covariance bound is one-sided, `c_N` is common, and source-support prefactors are finite.
5. **Lattice geometry:** verifies the reflection-convention-robust bound `d(theta Lambda_F,tau_n Lambda_F)>=n-A_F` and eventual disjointness.
6. **RG/continuum:** classifies the result as fixed-cutoff only; strong/weak interpolation, lattice-spacing uniformity and continuum spectral identification remain open.
7. **Adversarial provenance / RAKL v3:** records the arXiv HTML/PDF version mismatch, proposal/shadow authority, prior-memory routing effect, SEARCH→JUMP→GLUE status and `0/3` independent-review credit.

All roles share the same context and are not independent mathematical reviews.

## Episode -> diagnosis -> reusable obstruction/lesson separation

**Episode:** `EP-YM-S1a2d-R14-20260812` — exact-source composition and falsification cycle on #253.

**Diagnosis:** `DG-YM-S1a2d-R14-EUCLIDEAN-FORM-DECAY-PASS-OPERATOR-REALIZATION-BLOCKED` — same-theory nonnegative reflected forms and the affine support-distance conversion close locally; the next load-bearing failure is operator realization on the exact OS quotient.

**Existing obstruction narrowed, not replaced:** `F-YM-S1A2-OS-SZZ-SAME-THEORY-GLUING-UNBOUND` remains active. Its sign/support coordinate is partially discharged; null-quotient time-shift realization, source completeness with authority, and continuum gluing remain open.

**New obstruction:** none minted.  
**New reusable lesson:** none promoted.  
**Failure category:** `GLUING / OPERATOR-REALIZATION`, not local covariance mathematics.  
**Novelty class:** `COMPOSITIONAL` — exact source results plus elementary lattice geometry; no new operator, representation or ontology.

## Saturation update

- `KNOWLEDGE`: `REOPENED` — exact same-theory nonnegative common-rate form packet retained at shadow level.
- `OPERATOR`: `REOPENED` — the previously compound residual is now concentrated on null-quotient shift/operator realization.
- `EXPERIENCE_PATTERN`: `FLAT` — no new protected reusable pattern.
- `OBSTRUCTION`: `FLATTENED` — no new obstruction; an existing compound obstruction is narrower.
- `RELATION`: `REOPENED` — SZZ support-distance decay is now exactly related to reflected temporal separation.
- `PATH`: `REOPENED` — a conditional path to `YM-S1A1-C001-V2` is shorter but still blocked.
- `META_METHOD`: `FLAT` — no method-authority change.

## Residual

**Before:** `RES-YM-S1a2-POST-RP-COVARIANCE-TO-TRANSFER-MOMENTS-PLUS-SOURCE-COMPLETENESS-AND-PHYSICAL-GAP-UNBOUND`.

**After:** `RES-YM-S1a2d-INFINITE-VOLUME-OS-NULL-QUOTIENT-ONE-STEP-TRANSFER-REALIZATION-PLUS-DENSITY-AUTHORITY-AND-CONTINUUM-UNBOUND`.

No finite-lattice, infinite-volume, or continuum Hamiltonian gap is promoted by this file. Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.