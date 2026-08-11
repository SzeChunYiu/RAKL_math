# YM-E4b2 — OS null-quotient comparison and finite-chart repair

**Atom:** `YM-E4b2`  
**Signature:** `YM-E4b2-OS-NULL-QUOTIENT-COMPARISON-MAP-CHART-REPAIR`  
**Parent:** `YM-E4b` / issue #126; follows proposal/shadow `YM-E4b1` / PR #130.  
**Framework source of truth at freeze:** `SzeChunYiu/RAKL@787c7e00af2a5877ccb715bc807ec14f52974e9c`, method `3.0.0`, software package `0.1.0`.  
**Application base:** `SzeChunYiu/RAKL_math@dc83b72201cb58844b2bdc76117e4dcb9190211d`.  
**Pre-action receipt commit:** `da2a115675f80867df81f3359f469f277447f027`.  
**Frozen fibre:** `sha256:b1766988c34811ab3faa0d99d70799dd6bdbdcb3d043bbafde5c38c2587801ee`.  
**Authority:** `PROPOSAL_SHADOW / LOCAL_REPRESENTATION_LEMMA / SAME_CONTEXT_REVIEW_ONLY / NO_CONTINUUM_YM_THEOREM / ROOT_AUTHORITY_NONE`.

## 1. Chronology boundary

The source-local observation that the raw rule `U_sigma([F])=[F_sigma]_sigma` needs a quotient-well-definedness check was noticed while auditing the primary source and therefore predates the durable pre-action receipt. It is **retrospective motivating evidence** and receives no prospective-discovery credit.

The action frozen prospectively at commit `da2a115...` was narrower: first falsify the inference that asymptotic OS-form convergence alone makes the representative rule a quotient map; then, if it fails, test a finite-dimensional section/Gram-chart repair and isolate the remaining source/gluing obligations. The result below is the outcome of that prospectively frozen repair test.

## 2. Exact primary-source interface

Primary source: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 June 2026).

Section 8.2, pp. 88–90, makes the following source-level moves:

1. It fixes a countable positive-time gauge-invariant cylinder algebra `A_+`, chooses for each `F in A_+` a regulator approximation `F_sigma`, lets `D` be the span of continuum OS classes `[F]`, and defines `U_sigma([F])=[F_sigma]_sigma`.
2. Equation (8.15) establishes only asymptotic preservation of inner products: `(U_sigma phi,U_sigma psi)_sigma -> (phi,psi)` on `D`.
3. Theorem 8.3, equations (8.16)–(8.26), then derives fixed-time strong semigroup convergence by expanding a norm into Schwinger-function matrix elements at times `0,t,2t`.
4. Theorem 8.4 subsequently calls `U_sigma:H->H_sigma` *isometric identification maps*, a stronger property than the asymptotic relation in (8.15).

This cycle does not treat the preprint's claim as established merely because it is stated. It audits the exact interface used by the proof.

## 3. Local obstruction: a representative rule descends to the quotient only under null-space compatibility

Let `V_0,V_sigma` be complex vector spaces with positive-semidefinite sesquilinear forms `q_0,q_sigma`. Let

`N_0={v in V_0:q_0(v,v)=0}` and `N_sigma={w in V_sigma:q_sigma(w,w)=0}`,

and let `pi_0:V_0->V_0/N_0`, `pi_sigma:V_sigma->V_sigma/N_sigma` be quotient maps. Let `R_sigma:V_0->V_sigma` be linear.

### Lemma 3.1 — exact quotient criterion

The formula

`J_sigma(pi_0 v) := pi_sigma(R_sigma v)`

defines a linear map `V_0/N_0 -> V_sigma/N_sigma` **if and only if**

`R_sigma(N_0) subseteq N_sigma`.

**Proof.** If `J_sigma` is well defined and `n in N_0`, then `pi_0 n=pi_0 0`, hence `pi_sigma(R_sigma n)=pi_sigma(0)` and therefore `R_sigma n in N_sigma`. Conversely, if `R_sigma(N_0) subseteq N_sigma` and `pi_0 v=pi_0 w`, then `v-w in N_0`, so `R_sigma(v-w) in N_sigma`, which gives `pi_sigma(R_sigma v)=pi_sigma(R_sigma w)`. Linearity is inherited from `R_sigma`. QED.

Thus convergence of forms is not, by itself, the criterion needed to define the quotient map.

### Hostile control 3.2 — asymptotic form convergence does not imply exact null-space compatibility

Take `V_0=V_epsilon=R^2`,

`q_0((x,y),(x,y))=x^2`,

`q_epsilon((x,y),(x,y))=x^2+epsilon y^2`, `epsilon>0`,

and `R_epsilon=id`. Then `q_epsilon(v,w)->q_0(v,w)` for every fixed pair, so all finite collections of inner products converge. But

`N_0=span(e_2)`, whereas `N_epsilon={0}`.

Hence `[0]_0=[e_2]_0` but `[0]_epsilon != [e_2]_epsilon`. The raw rule `[v]_0 -> [v]_epsilon` is not well defined for any `epsilon>0`, even though `||[e_2]_epsilon||=sqrt(epsilon)->0`.

This falsifies only the inference

`asymptotic OS-form preservation => representative rule is an exact quotient map at every regulator`.

It does **not** show that the source cannot choose a different comparison structure, nor that its actual gauge-theory null spaces necessarily realize this hostile model.

## 4. Prospectively tested repair: finite-dimensional quotient-safe source charts

The previous obstruction is avoided if the comparison is defined on continuum Hilbert-space coordinates rather than by an equivalence-class representative rule.

Let `H` be the continuum OS Hilbert space, `D subset H` a source domain, and for each regulator let `H_sigma` be the regulated OS Hilbert space. Let `E subset D` be finite dimensional. Choose a **fixed linear section/representative chart**

`s_E:E -> V_0`, with `pi_0 s_E = id_E`.

For each regulator let `R_sigma` approximate source representatives and define

`J_{sigma,E} phi := pi_sigma R_sigma s_E(phi)`.

Because `s_E` is a single-valued map whose input is already the continuum Hilbert vector `phi`, `J_{sigma,E}` is a genuine linear map on `E`; it does not require `R_sigma(N_0) subseteq N_sigma`.

### Lemma 4.1 — finite-chart asymptotic isometry from Gram convergence

Let `e_1,...,e_m` be an orthonormal basis of `E`. Assume

`<J_{sigma,E}e_i,J_{sigma,E}e_j>_{H_sigma} -> delta_ij`

for all `i,j`. Then

`sup_{||phi||_H=1, phi in E} | ||J_{sigma,E}phi||^2 - 1 | -> 0`.

Consequently, for every `0<eta<1`, for all sufficiently small regulator,

`(1-eta)||phi||^2 <= ||J_{sigma,E}phi||^2 <= (1+eta)||phi||^2`

for every `phi in E`; in particular `J_{sigma,E}` is injective on `E`.

**Proof.** In the chosen basis the regulated inner product is represented by the Hermitian Gram matrix `G_sigma` with entries above. Entrywise convergence to the identity is equivalent to operator-norm convergence in fixed finite dimension. For `phi=sum_i c_i e_i`,

`||J_{sigma,E}phi||^2=c^*G_sigma c`.

Hence the unit-sphere error is bounded by `||G_sigma-I||_op`, which tends to zero. QED.

This is the precise limited sense in which equation (8.15)-type information can supply a quotient-safe asymptotic identification without exact cross-cutoff isometry: first fix a finite continuum chart/section, then use its finite Gram matrix.

### Lemma 4.2 — fixed-time finite-chart strong semigroup intertwining

Let `T(t)` on `H` and `T_sigma(t)` on `H_sigma` be self-adjoint contraction semigroups. Fix `t>=0` and finite-dimensional `E subset D`. Assume `E_t:=E+T(t)E` is contained in the source domain and is equipped with one fixed section/chart as above, giving `J_{sigma,E_t}`. Assume for every `u,v in E_t` and `s in {0,t,2t}`,

`<J_{sigma,E_t}u, T_sigma(s)J_{sigma,E_t}v> -> <u,T(s)v>`.

Then for every `phi in E`,

`||T_sigma(t)J_{sigma,E_t}phi - J_{sigma,E_t}T(t)phi|| -> 0`.

**Proof.** Write `J_sigma=J_{sigma,E_t}`. By self-adjointness and the semigroup property,

`||T_sigma(t)J_sigma phi - J_sigma T(t)phi||^2`

`= <J_sigma phi,T_sigma(2t)J_sigma phi>`

`  + <J_sigma T(t)phi,J_sigma T(t)phi>`

`  - 2 Re <J_sigma phi,T_sigma(t)J_sigma T(t)phi>`.

The three assumed matrix-element limits are respectively

`<phi,T(2t)phi>`, `||T(t)phi||^2`, and `<phi,T(t)T(t)phi>=<phi,T(2t)phi>`.

Since `T(t)` is self-adjoint, `<phi,T(2t)phi>=||T(t)phi||^2`; the limiting combination is zero. QED.

This is a finite-chart version of the norm-expansion idea used in the source's equations (8.19)–(8.26), but it does not require an ill-defined raw quotient map or an exact cross-cutoff Hilbert isometry.

## 5. What this does and does not repair in the source route

### Local representation result

The raw source definition `U_sigma([F])=[F_sigma]_sigma` needs an additional exact condition or a choice mechanism. A sufficient exact condition is null-space preservation `R_sigma(N_0) subseteq N_sigma`. Without it, asymptotic inner-product preservation does not make the formula representative-independent.

The finite-chart construction gives a bounded alternative: choose continuum Hilbert coordinates first, fix a section on each finite chart, and build regulator maps from those coordinates. Gram convergence supplies uniform asymptotic norm control on each fixed chart, and the three-time matrix-element interface supplies fixed-time strong semigroup intertwining there.

### Global/source-binding residuals — still open

This cycle does **not** establish any of the following:

1. that the actual Faizal–Shabir regulator approximation preserves continuum OS null spaces exactly;
2. that the preprint supplies a canonical or compatible family of sections on nested dense source charts;
3. that `T(t)D subset D`, or an adequate approximation/core statement, holds for the exact source domain and all physical times used;
4. that lattice-time translations used for `F_sigma o tau_t` are defined with the required fixed-physical-time normalization for arbitrary `t` and regulator;
5. that finite-chart convergence extends uniformly to the whole continuum physical OS Hilbert space;
6. vacuum compatibility `VAC` and a volume/lattice-spacing-uniform excited-sector contraction `UGAP` from `YM-E4b1`;
7. gauge-invariant physical-state/null-space compatibility under gauge fixing, blocking, and removal of the regulator;
8. source-family density/common-rate in the same reconstructed theory (`#109`, PR #62, `#88`);
9. finite/infinite-volume and continuum limit interchange, nontriviality, RG transport, or existence of the required continuum Yang–Mills theory.

The failure at item 1 is **local representation/quotient failure**. Items 2–9 are **local-to-global/source/gluing obligations** and are recorded separately rather than collapsed into the local lemma.

## 6. Same-context expert cell

These are role-separated internal passes, not independent review.

1. **Constructive QFT / OS reconstruction.** The OS Hilbert space is a quotient by null vectors before completion. Therefore a representative-defined cross-regulator map must be checked for descent to that quotient. The finite-chart section is a legitimate local repair, but source-domain/time-translation compatibility remains unproved.
2. **Functional analysis / varying Hilbert spaces.** Lemma 3.1 is the exact quotient criterion. The `R^2` model is a decisive counterexample to replacing exact null inclusion by asymptotic norm-zero. Lemma 4.1 is finite-dimensional Gram-matrix perturbation; Lemma 4.2 is a direct semigroup norm identity. No global varying-Hilbert theorem is imported.
3. **Gauge-theory physical-state specialist.** The repair is abstract. It does not prove that gauge-equivalent or OS-null continuum sources have regulator approximants compatible with the gauge-invariant physical quotient. This remains a same-theory binding obligation.
4. **RG / continuum-limit specialist.** Fixed-chart convergence is not regulator/volume-uniform control over an expanding dense family. No exchange of `sigma->0`, volume, RG depth, or long Euclidean time is justified here.
5. **Adversarial verifier.** The collapsing-null-space model kills the raw inference. Removing finite-dimensionality from Lemma 4.1 also removes the automatic upgrade from entrywise Gram convergence to uniform norm control; removing the time-`t` cross matrix element from Lemma 4.2 leaves the strong-intertwining conclusion unsupported.
6. **RAKL v3 assurance/metrology.** The motivating source diagnosis is retrospective; the chart-repair test is prospectively bound by `da2a115...`. No same-context pass counts as an isolated mathematical review, and no local result is promoted beyond proposal/shadow authority.

## 7. Episode -> diagnosis -> obstruction/lesson separation

- **Episode:** `YM-E4b2-EP-OS-NULL-QUOTIENT-CHART-REPAIR-20260811T1745Z` — one bounded research attempt using the frozen fibre, hostile control, chart repair, and six-role review.
- **Diagnosis:** `DX-YM-E4b2-REPRESENTATIVE-MAP-NOT-QUOTIENT-WELLDEFINED` — equation (8.15)-type asymptotic form convergence does not itself prove that the representative rule descends to the continuum OS quotient.
- **Scoped failure:** `F-YM-E4b2-ASYMPTOTIC-FORM-NOT-EXACT-NULL-PRESERVATION` — the implication from asymptotic form convergence to exact quotient-map well-definedness is false.
- **Proposal obstruction:** `O-YM-E4b2-NULL-SPACE-OR-SECTION-COMPATIBILITY` — source-facing repair must prove exact null preservation or provide a compatible quotient-safe comparison chart/section structure, then separately satisfy the global `AI/VAC/INT/UGAP` gluing interface.
- **Lesson:** none promoted. A candidate lesson, kept shadow-only, is that varying-Hilbert comparison maps defined through representatives require an explicit null-space descent certificate or a chart that is defined on quotient coordinates from the outset.

## 8. Saturation and route effect

The saturated Bałaban-source family `YM-E1a1a0` is not revisited. The current obstruction reopens the `OBSTRUCTION`, `RELATION`, `PATH`, `EXPERIENCE_PATTERN`, and `META_METHOD` axes at proposal/shadow level: the prior `YM-E4b1` episode changed routing from global gap-transfer algebra to the exact quotient-map interface; the hostile control narrows the source repair; and the finite-chart route gives a concrete next discriminator. `OPERATOR` remains flattened because no new protected operator is created. `KNOWLEDGE` is treated conservatively as unretained because no protected promotion gate runs in this cycle.

**Shadow solved-subproblem novelty class:** `representation` — the local repair changes the representation of cross-regulator comparison from representative classes to finite continuum Hilbert charts. This classification carries no novelty authority.

## 9. Next action

Prospectively freeze a source-binding child that tests one exact finite chart of gauge-invariant positive-time cylinder classes in the actual construction: specify the section, regulator approximation, allowed physical time `tau`, and prove the three matrix-element limits needed by Lemma 4.2 with exact page/equation anchors. Then test nested-chart compatibility and only afterward attempt the `AI/VAC/INT/UGAP` global extension from `YM-E4b1`.

Root status remains `OPEN_NO_SOLUTION_CERTIFICATE`. No root gate is weakened or approached by assertion.