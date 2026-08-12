# YM-S1a2e R15 — fixed-cutoff SZZ gap versus physical lattice-spacing scaling

Authority: **proposal/shadow source-and-gluing audit only**. No continuum theorem, no mass-gap theorem, no novelty claim, no root authority.

Prospective atom: #269, `YM-S1a2e-SZZ-STRONG-COUPLING-TO-CONTINUUM-PHYSICAL-MASS-SCALING`.

## Chronology / prior-observation boundary

The R15 fibre was frozen in Git before the exact parameter/regime test below. This runtime had already re-read the SZZ strong-coupling domain and Lüscher transfer-matrix discussion while checking concurrent R14 work; those observations receive zero strict R15 discovery credit. The differential R15 result is the exact post-freeze parameter matching and resulting G6 domain/gluing diagnosis.

## Primary-source binding

### 1. SZZ theory and theorem domain

Primary source: Hao Shen, Rongchan Zhu, Xiangchan Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, arXiv:2204.12737v1 / CMP 400 (2023).

- §1.1 fixes **unit lattice spacing**.
- Eq. (1.2) defines the Wilson weight through
  `S(Q) = N beta Re sum_{p in P^+} Tr(Q_p)`, where `P^+` contains one chosen orientation per plaquette.
- Assumption 1.1 / Eq. (1.3) gives, for `SU(N)`,
  `|beta| < 1/[16(d-1)]`.
- In `d=4` and on the positive-beta branch used by the fixed-cutoff OS lane, this is
  `0 < beta < 1/48`.

This is a theorem domain in a fixed small neighborhood of `beta=0`; SZZ themselves call beta the inverse coupling constant / beta*N the inverse-coupling-strength scaling.

### 2. Exact Wilson coefficient matching to Lüscher's bare coupling

Primary source: M. Lüscher, DESY 76/54 / CMP 54 (1977), *Construction of a Selfadjoint, Strictly Positive Transfer Matrix for Euclidean Lattice Gauge Theories*.

Lüscher Eq. (2) writes the pure-gauge plaquette contribution with coefficient

`(1/(2 g0^2)) sum_{n} sum_{mu != nu} Tr U_{mu nu}(n)`.

For every unoriented elementary plaquette, the ordered pair `(mu,nu)` and the reversed ordered pair `(nu,mu)` contribute a plaquette matrix and its inverse/conjugate under the trace. Pairing them gives

`Tr U_p + Tr U_p^* = 2 Re Tr U_p`.

Therefore Lüscher's coefficient per once-oriented plaquette is exactly

`(1/g0^2) Re Tr U_p`.

Matching the same Wilson weight to SZZ Eq. (1.2) gives the exact convention map

`N beta = 1/g0^2`, i.e. `beta = 1/(N g0^2)`.

No gauge fixing is used in this coefficient comparison; it is a comparison of the gauge-invariant Wilson plaquette action.

### 3. Consequence for the SZZ strong-coupling domain

For positive beta in `d=4`, substituting the exact map into the SZZ condition yields

`1/(N g0^2) < 1/48`, hence `g0^2 > 48/N`.

Thus for every fixed `N`, the microscopic bare coupling throughout the SZZ theorem domain is bounded **away from zero**.

Equivalently, any trajectory with `g0(a) -> 0` has `beta_SZZ(a) = 1/[N g0(a)^2] -> +infinity` and eventually exits `0 < beta < 1/48`.

### 4. Asymptotically-free cutoff-removal coordinate

Primary source: M. Lüscher and P. Weisz, *Two-loop relation between the bare lattice coupling and the MS coupling in pure SU(N) gauge theories*, arXiv:hep-lat/9502001 / Phys. Lett. B349 (1995).

They work with the standard four-dimensional hypercubic Wilson action of spacing `a`, bare gauge coupling `g0`, and `alpha0 = g0^2/(4 pi)`. Eq. (1.2) matches the renormalized coupling at momentum `s/a` to the bare lattice coupling,

`alpha_MS(s/a) = alpha0 + d1(s) alpha0^2 + d2(s) alpha0^3 + ...`,

and Appendix A gives the asymptotically-free beta function with positive universal `b0 = 11N/(48 pi^2)` in the convention `q d gbar/dq = -b0 gbar^3 - ...`.

**Scoped inference:** on the asymptotically-free Wilson cutoff-removal tail `a -> 0`, so that `q=s/a -> infinity` and the renormalized coupling tends to zero, the perturbative matching forces `alpha0 -> 0`, hence `g0(a) -> 0`. This is a perturbative/asymptotic-freedom coordinate, not by itself a constructive continuum-existence theorem.

### 5. Exact domain non-overlap

Combining §3 and §4 yields a strict parameter-domain separation for fixed `N`:

- SZZ strong-coupling theorem: `g0^2 > 48/N`;
- asymptotically-free microscopic cutoff-removal tail: `g0(a)^2 -> 0`.

Therefore the SZZ fixed-cutoff theorem **cannot be applied directly at the microscopic lattice spacing along the asymptotically-free continuum tail**. In SZZ's own parameter, the first lives at `beta < 1/48`, while the second has `beta(a) -> infinity` under the exact Wilson coefficient map.

This is a contextual-theory-gluing/domain obstruction, not an impossibility theorem for Yang–Mills and not a proof that a strong-coupling theorem is irrelevant to an RG construction. A valid repair could in principle start at weak microscopic coupling and prove that a same-theory RG flow reaches a strong effective-coupling regime at a coarser physical scale. But that requires an explicit theorem carrying the relevant gauge-invariant OS/spectral information through the flow.

## Physical mass scaling interface

Lüscher identifies the one-step transfer operator as `T_a = exp(-a H_a)`. Hence if a same-theory lattice spectral edge were `lambda_1(a) <= exp[-c(a)]`, its physical energy lower bound would be

`Delta_a >= c(a)/a`.

The current SZZ result supplies a positive lattice-distance exponent only inside its fixed strong-coupling theorem domain and is formulated at unit lattice spacing. The active fixed-cutoff draft work #256/#258 therefore has **zero direct `a -> 0` authority**. A continuum mass-gap bridge must control `c(a)/a` (or an equivalent renormalized Hamiltonian-gap quantity) on the actual cutoff-removal trajectory, with the same measure/OS source algebra and required limits.

A fixed strong-coupling value of `c_N` cannot be re-labelled as a continuum physical mass by merely restoring a symbol `a`; the corresponding fixed-beta microscopic family is not the asymptotically-free cutoff-removal tail established above.

## Bounded repair search

A bounded post-freeze primary-source search was made for a theorem transporting a strong-coupling lattice mass gap to the weak-coupling/asymptotically-free four-dimensional continuum theory with the same OS spectral data. No source satisfying the full #269 contract was located. Search results again exposed Balaban's ultraviolet-stability/RG program and strong-coupling lattice results, but not a primary theorem simultaneously binding the SZZ strong-coupling gap, the weak microscopic continuum trajectory, same OS Hilbert-space spectral data, and a uniform physical `c(a)/a` lower bound.

This search is not an exhaustive nonexistence claim. Missing theorem-level detail remains `BLOCKED/CANNOT_CHECK` rather than being reconstructed from memory.

## Gauge / regularization / limits audit

- **Gauge dependence:** the action match is gauge invariant; no gauge-fixed surrogate is used. Any later transport theorem must preserve gauge-invariant observables and the same physical OS quotient.
- **Regularization:** SZZ is fixed unit lattice spacing; Lüscher-Weisz explicitly exposes lattice spacing `a`. The audit does not identify these cutoffs without the parameter map.
- **Thermodynamic limit:** SZZ's strong-coupling infinite-volume measure is not in dispute here; the new residual is the cutoff-removal trajectory after infinite-volume/fixed-cutoff spectral work.
- **Limit interchange:** no interchange of infinite volume, RG scale, and `a -> 0` is assumed. A repair must state and prove its order/uniformity.
- **Uniformity:** fixed-cutoff source-independent exponential decay does not supply uniformity in `a`; `c(a)/a` is the relevant physical scaling coordinate.
- **Reflection positivity / OS:** fixed-cutoff RP/transfer work remains scoped dependency evidence only. Transport across RG/cutoff scales must type-check the same source algebra, quotient, physical time normalization, and continuum subsequence.

## Same-context expert cell findings

1. **Lattice renormalization / asymptotic freedom:** accepts the exact `N beta = g0^{-2}` match and the strict fixed-N domain non-overlap; treats the Lüscher-Weisz step as perturbative/asymptotic-freedom input, not a constructive existence theorem.
2. **Constructive RG:** rejects direct SZZ-to-continuum promotion; leaves open a weak-UV to strong-effective-IR RG route, but requires a same-theory transport theorem with regulator/scale/volume uniformity.
3. **OS / spectral theory:** requires the `T_a=e^{-aH_a}` normalization and a uniform physical bound on the actual trajectory; fixed lattice-unit `c_N` alone is insufficient.
4. **SZZ / probability:** confirms the theorem's small-beta strong-coupling domain and unit-spacing scope; no hidden `a`-trajectory theorem is supplied by the cited result.
5. **Gauge representation:** validates coefficient matching only after orientation double-counting is resolved; no gauge-switch is involved.
6. **Adversarial mathematical physics:** hostile control `g0(a)^2 -> 0` versus `g0^2 > 48/N` defeats direct microscopic application but does not defeat a separately proved RG transport mechanism.
7. **Provenance / metrology:** keeps the episode, diagnosis and obstruction distinct; credits zero strict discovery to pre-freeze observations; same-context review earns `0/3` independent-review credit.

## Scoped diagnosis

- Episode: `EP-YM-S1a2e-R15-20260812`.
- Diagnosis: `DG-YM-S1a2e-R15-STRONG-AF-DOMAIN-NONOVERLAP-SHADOW`.
- New proposal/shadow obstruction: `O-YM-S1a2e-MICROSCOPIC-STRONG-AF-DOMAIN-NONOVERLAP-R15-SHADOW`.
- New mathematical FailureExperience: **none** — no invalid mathematical candidate was executed; this is a source/domain gluing diagnosis.
- Lessons/tools/motifs promoted: **none**.

Residual after R15:

`RES-YM-S1a2e-WEAK-UV-TO-GAPPED-IR-SAME-OS-SPECTRAL-TRANSPORT-WITH-PHYSICAL-SCALING-UNBOUND`.

A successful successor must provide a primary same-theory theorem from the weak microscopic/asymptotically-free UV trajectory to a gapped IR scale (or an independent continuum gap construction), while preserving gauge invariance/RP/OS data and proving a positive physical gap with all volume, regulator, RG-scale and continuum uniformity explicit.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.
