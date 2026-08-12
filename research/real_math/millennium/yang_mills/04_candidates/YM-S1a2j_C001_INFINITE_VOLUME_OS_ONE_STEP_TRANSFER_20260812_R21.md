# YM-S1a2j-C001 R21 — Infinite-volume OS one-step positive transfer contraction

**Authority:** `PROPOSAL_SHADOW_LOCAL_COMPOSITION / SAME_CONTEXT_CHECKED / NO_PROTECTED_AUTHORITY / NO_CONTINUUM_GAP / NO_ROOT_AUTHORITY`  
**Root:** #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Atom:** #330 (`YM-S1a2j-SZZ-INFINITE-VOLUME-OS-ONE-STEP-TRANSFER-REALIZATION`)  
**Frozen pre-source object:** Git commit `3ce9a54d1ebf678924d7cd3305ca99b1a9854c5c`, blob `42c8bfedf1943b21e9d612ba76d92936f2eb871e`. The literal SHA-256 of the frozen fibre file bytes is `07607acbbec64b99ec8f4f10e366d2e8c61dae4faa10b9e31bf65a0313a52249`; the self-declared hash field inside that file was not actually computed and is invalid. This metrology defect is corrected append-only in the R21 case-study packet and does not backfill chronology.

## Exact local statement

Let `mu = mu^ym_{N,beta}` be the Shen–Zhu–Zhu infinite-volume Wilson measure for `d=4`, `G=SU(N)` and `0<beta<1/48`. Let `A_+` be the bounded gauge-invariant finite-edge cylinder algebra supported strictly on the positive-time side of a site reflection `theta_0`. Assume the two exact reflection-positive inputs inherited from the matching finite Wilson measures:

1. **site reflection positivity:** `mu((Theta_0 F) F) >= 0` for `F in A_+`;
2. **adjacent link reflection positivity:** for the link plane at time `-1/2`, `mu((Theta_{-1/2} F) F) >= 0` for `F in A_+`.

The finite Wilson action has precisely the site/link positivity distinction emphasized by the primary transfer literature. Menotti–Pelissetto describe their theorem as extending Osterwalder–Seiler positivity to site-containing planes and state positivity for gauge-invariant observables at all Euclidean time separations. For each fixed cylinder the two finite-volume inequalities pass to `mu` along reflection-compatible periodic subsequences because SZZ Theorem 1.2 proves convergence of the whole finite-volume Wilson sequence to one infinite-volume measure.

Define the OS form

`<F,G>_OS := mu((Theta_0 F) G)`

on `A_+`, quotient its null space `N`, and complete to `H_OS`. Let `tau` be translation by one lattice unit in the positive Euclidean-time direction.

**Proposition.** The rule

`T_0 [F] := [tau F]`

is well defined on `A_+/N`, is symmetric and contractive there, and extends uniquely to a bounded self-adjoint contraction `T` on `H_OS`. Adjacent link reflection positivity makes `T >= 0`. For all `F,G in A_+` and integers `n>=0`,

`<[F], T^n [G]>_OS = mu((Theta_0 F) (tau_n G))`.

Thus the exact SZZ infinite-volume Euclidean reflected forms can be typed as powers of a **same-theory positive self-adjoint one-step transfer contraction** without taking an operator limit of finite-volume transfer matrices.

This proposition does **not** prove strict positivity/injectivity of `T`, does not by itself construct a finite-valued Hamiltonian logarithm on every vector, and does not address lattice-spacing-uniform or continuum Yang–Mills.

## Primary-source binding

### Shen–Zhu–Zhu

H. Shen, R. Zhu, X. Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, arXiv:2204.12737v1 / Commun. Math. Phys. 400 (2023).

Checked selectors:

- (1.1)–(1.3): periodic finite-volume Wilson measure, and for `SU(N)` the strong-coupling condition `|beta|<1/[16(d-1)]`, hence `|beta|<1/48` in `d=4`;
- Theorem 1.2: every tight limit is the same and the whole finite-volume sequence converges to `mu^ym_{N,beta}`;
- Corollary 1.6: exponential covariance decay for disjoint smooth finite-edge cylinders with one exponent `c_N>0`; source-dependent quantities are finite prefactors;
- finite periodic measures are translation invariant, and whole-sequence convergence transports this to the limiting cylinder expectations.

### Lüscher

M. Lüscher, *Construction of a Selfadjoint, Strictly Positive Transfer Matrix for Euclidean Lattice Gauge Theories*, Commun. Math. Phys. 54 (1977), DOI `10.1007/BF01614090`.

Checked primary PDF selectors:

- Eq. (4) and Eq. (5): OS positivity and the null-quotient Hilbert construction;
- immediately after Eq. (5): on the lattice an additional argument beyond a single OS reflection is required to make the one-step shift positive;
- Proposition 1: the finite-volume canonical transfer matrix is self-adjoint, bounded and strictly positive;
- Proposition 2: finite-volume Euclidean expectations reconstruct as transfer-matrix Schwinger functions; the `M->infinity` discussion identifies the corresponding finite-spatial-volume Hilbert descriptions.

The present proof does **not** infer an infinite-volume operator by taking a limit of Lüscher's finite-volume canonical `T`. It instead constructs the shift directly on the exact limiting OS quotient.

### Osterwalder–Seiler / Menotti–Pelissetto

K. Osterwalder, E. Seiler, *Gauge field theories on a lattice*, Ann. Phys. 110 (1978), DOI `10.1016/0003-4916(78)90039-8`. The primary publisher abstract states that physical positivity for lattice gauge approximations implies a positive self-adjoint transfer matrix and separately states existence/analyticity of the strong-coupling infinite-volume limit.

P. Menotti, A. Pelissetto, *General Proof of Osterwalder-Schrader Positivity for the Wilson Action*, Commun. Math. Phys. 113 (1987), DOI `10.1007/BF01221251`. The primary Springer abstract states that the Osterwalder–Seiler proof is extended to planes containing sites and that the resulting positivity holds for gauge-invariant `F` at all Euclidean time separations.

These sources are used only to bind the finite-Wilson site/link positivity inputs. The infinite-volume operator conclusion below is a local composition proved explicitly.

## Proof

### 1. The one-step shift descends through the exact OS null space

Site RP makes `<.,.>_OS` positive semidefinite, hence its Cauchy–Schwarz inequality holds before quotienting. If `F in N`, then

`<F,H>_OS = 0`

for every `H in A_+`. Since positive translation preserves `A_+`, `tau_2 F in A_+`. Using `Theta_0 tau = tau^{-1} Theta_0` and translation invariance,

`||[tau F]||_OS^2`
`= mu((Theta_0 tau F)(tau F))`
`= mu((Theta_0 F)(tau_2 F))`
`= <F,tau_2 F>_OS = 0`.

Therefore `T_0[F]=[tau F]` is independent of the representative.

### 2. The descended shift is symmetric

For `F,G in A_+`,

`<T_0[F],[G]>_OS`
`= mu((Theta_0 tau F)G)`
`= mu((Theta_0 F)(tau G))`
`= <[F],T_0[G]>_OS`,

where the middle equality again uses `Theta_0 tau=tau^{-1}Theta_0` and translation invariance. Thus `T_0` is symmetric on the dense quotient domain.

### 3. Site RP plus bounded cylinders forces contractivity

Fix `F` and write

`b_k := ||T_0^k[F]||_OS^2 = mu((Theta_0 F)(tau_{2k}F))`, `k>=0`.

Cauchy–Schwarz for the OS form applied to `tau_{k-1}F` and `tau_{k+1}F` gives, for `k>=1`,

`b_k^2 <= b_{k-1} b_{k+1}`.

Hence the nonnegative sequence `(b_k)` is log-convex. It is also uniformly bounded because `F` is a bounded cylinder and `mu` is a probability measure:

`0 <= b_k <= ||F||_infty^2`.

If `b_0=0`, Step 1 already gives `b_1=0`. If `b_0>0` and `b_1>b_0`, log-convexity implies the positive ratios `b_k/b_{k-1}` are nondecreasing, so every later ratio is at least `b_1/b_0>1`; then `b_k` grows exponentially, contradicting the uniform bound. Therefore

`b_1 <= b_0`,

or `||T_0[F]||_OS <= ||[F]||_OS`.

So `T_0` extends uniquely to a bounded contraction `T` on `H_OS`. Its extension is symmetric on the whole Hilbert space and therefore self-adjoint.

### 4. The second reflection is exactly what excludes negative transfer spectrum

Let `theta_{-1/2}` be the adjacent link reflection. With the standard lattice translation/reflection convention,

`Theta_{-1/2} = tau^{-1} Theta_0`.

Therefore, by translation invariance,

`<[F],T[F]>_OS`
`= mu((Theta_0 F)(tau F))`
`= mu((Theta_{-1/2}F)F)`.

Adjacent link RP makes this nonnegative for every `F in A_+`; continuity extends the inequality to all of `H_OS`. Hence `T>=0`.

This step is logically separate from site RP. It is precisely the extra lattice positivity input that Lüscher warns is needed beyond the single site-reflection quotient construction.

### 5. Exact same-theory moment identity

On the dense cylinder quotient, induction gives `T_0^n[F]=[tau_n F]`. Thus

`<[F],T^n[G]>_OS = mu((Theta_0F)(tau_n G))`

for every `n>=0`. No finite-volume operator convergence, state matching, or external Hilbert-space identification is used.

`QED` at proposal/shadow local-composition authority.

## Counterexample-first controls

### H1 — site RP alone does not imply positive one-step transfer

The scalar moment sequence `a_n=(-1)^n` has Hankel matrices `[a_{i+j}]=v v^*` with `v_i=(-1)^i`, hence the site-reflection/Hankel positivity pattern is satisfied, while the represented one-step operator is `T=-1`. The adjacent link form has `a_1=-1` and fails positivity. This validates the separate site/link gate.

### H2 — RP without boundedness need not give a contraction

The scalar sequence `a_n=2^n` also has rank-one positive Hankel matrices, but its norms grow. The bounded-cylinder/probability-measure envelope is therefore load-bearing in Step 3.

### H3 — positive contraction is not strict positivity

A positive contraction can have nontrivial kernel. Weak limits of strictly positive finite-volume operators need not retain a uniform lower spectral bound. This cycle does not infer injectivity of the exact infinite-volume `T`, and therefore does not silently identify `T=e^{-H}` with an everywhere finite Hamiltonian logarithm.

### H4 — fixed lattice transfer gap is not the Clay mass gap

Even after combining this operator lemma with a common exponential Euclidean rate and a dense centered source class, the result is only a gap in the spectrum of the **unit-lattice transfer contraction** away from its vacuum eigenvalue. It supplies no lattice-spacing-uniform physical lower bound, no asymptotically-free trajectory, no continuum OS state, and no continuum Hamiltonian identification.

## Conditional spectral handoff

For `Omega=[1]`, translation gives `T Omega=Omega`. Smooth centered gauge-invariant positive-time cylinders are the natural excited source family. On this family, the previously audited SZZ Corollary 1.6 plus reflected-support time separation supplies

`0 <= <[F],T^n[F]> <= C_F exp(-c_N n)`

for all sufficiently large `n`, with one source-independent `c_N>0`. If their images are dense in `Omega^perp` in this same `H_OS` (an elementary OS/L2 density coordinate, previously recorded only at proposal/shadow level), the standard spectral-measure argument excludes `spec(T|Omega^perp)` from `(exp(-c_N),1]`.

R21 therefore makes the **operator-realization coordinate locally available**, but does not promote the density packet or the resulting fixed-cutoff spectral exclusion to protected authority in this file. No continuum inference follows even if that local handoff is separately closed.

## Seven-role same-context expert synthesis

1. **Constructive lattice gauge / OS lead** — background in reflection-positive Euclidean lattice gauge measures; verified the null quotient, finite-to-infinite RP passage, and kept site/link planes distinct.
2. **Transfer-matrix lead** — background in Wilson/Lüscher canonical transfer matrices; accepted the direct quotient construction and rejected any finite-volume-operator-limit shortcut.
3. **Functional-analysis / spectral lead** — background in positive operators and moment problems; verified null descent, symmetry, the bounded-log-convex contraction lemma, and the positivity handoff.
4. **Strong-coupling correlation lead** — background in SZZ functional inequalities; verified the exact strong-coupling range and common-exponent covariance input while keeping source prefactors source-dependent.
5. **Thermodynamic-limit lead** — background in Gibbs weak limits; checked that whole-sequence SZZ convergence lets fixed bounded cylinder RP inequalities pass through compatible periodic subsequences.
6. **RG / continuum lead** — background in lattice-spacing scaling and asymptotic freedom; blocked every attempted promotion from unit-lattice transfer spectrum to a physical continuum mass.
7. **Adversarial provenance / RAKL-v3 lead** — background in proof gates and telemetry; caught the uncomputed self-declared fibre hash, preserved the Git-frozen pre-source object, and downgraded the hash field by append-only correction rather than rewriting history.

All seven roles share one context and count as **same-context expert review only**, not independent mathematical review. Independent review credit remains `0/3`.

## Episode -> diagnosis -> obstruction/lesson

- **Episode:** `EP-YM-S1a2j-R21-20260812` — direct infinite-volume OS shift construction/falsification cycle.
- **Diagnosis:** `DG-YM-S1a2j-R21-ONE-STEP-TRANSFER-LOCAL-PASS-HAMILTONIAN-CONTINUUM-OPEN` — the exact null-quotient one-step positive contraction is locally constructible from site/link RP, translation invariance and bounded cylinders; strict positivity and continuum transport are separate.
- **Existing obstruction narrowed:** `F-YM-S1A2-OS-SZZ-SAME-THEORY-GLUING-UNBOUND` loses its one-step positive-operator-realization coordinate at proposal/shadow level. Same-Hilbert-space density authority, strict/physical Hamiltonian identification if required, lattice-spacing normalization, RG/continuum gluing remain open.
- **New obstruction:** none promoted. A shadow residual `RES-YM-S1a2j-STRICT-TRANSFER-HAMILTONIAN-PLUS-CONTINUUM` is recorded, not admitted to protected memory.
- **Reusable lesson:** none promoted. A proposal-only lesson candidate is that site RP + bounded time-translates controls the contraction, whereas adjacent link RP controls the sign of the one-step spectrum; the two roles should not be conflated.
- **Novelty class:** `COMPOSITIONAL` (exact OS algebra + bounded log-convexity + primary site/link source binding). No new Yang–Mills operator formalism or ontology is claimed.

## Saturation / residual

`KNOWLEDGE=REOPENED`, `OPERATOR=REOPENED`, `EXPERIENCE_PATTERN=FLAT`, `OBSTRUCTION=FLATTENED`, `RELATION=REOPENED`, `PATH=REOPENED`, `META_METHOD=REOPENED` only in the telemetry sense that current v3 epistemic-sufficiency routing was newly used; no protected meta-method novelty is retained.

**Residual before:** `RES-YM-S1a2d-INFINITE-VOLUME-OS-NULL-QUOTIENT-ONE-STEP-TRANSFER-REALIZATION-PLUS-DENSITY-AUTHORITY-AND-CONTINUUM-UNBOUND`.

**Residual after:** `RES-YM-S1a2j-SAME-HILBERT-DENSE-DECAY-HANDOFF-PLUS-STRICT-HAMILTONIAN-IF-REQUIRED-PLUS-A-UNIFORM-RG-CONTINUUM-UNBOUND`.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.
