# YM-S1a2 primary-source binding audit — 2026-08-11

**Atom:** `YM-S1a2` — bind Shen–Zhu–Zhu (SZZ) infinite-volume Euclidean covariance decay to the same Osterwalder–Schrader (OS) physical transfer Hilbert space.  
**Parent:** `YM-S1a1` abstract dense-source common-rate spectral exclusion.  
**Framework inspected:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`.  
**Application base:** `SzeChunYiu/RAKL_math@6557b1b25fa839fe71aba8047c958d5da892edd8`.  
**Authority:** `PRIMARY_SOURCE_AUDIT / PRE_CANDIDATE / PROPOSAL_ONLY / ROOT_AUTHORITY_NONE`.

This audit is a source-binding operation required by issue #88. It deliberately stops before a new mathematical candidate. The existing `YM-S1a1` abstract lemma is preserved at its actual local authority; no fixed-cutoff Yang–Mills gap, continuum gap, novelty, or root claim is promoted here.

## Exact discriminator

The parent source packet had three open interfaces:

1. **same-theory OS binding** — the SZZ infinite-volume Gibbs measure must inherit the reflection-positive Euclidean structure needed for the physical transfer construction;
2. **controlled-source density** — the smooth gauge-invariant cylinder functions to which the SZZ common exponent applies must generate a dense source sector in the same OS physical excited Hilbert space;
3. **time-translation geometry** — translating a fixed positive-time source by `n` lattice steps must produce the exact OS moment/covariance and support distance `n+O_F(1)` required by nth-root asymptotics.

The cheapest high-information action is to determine how much of these interfaces is already source-bound before proposing another lemma.

## Primary sources inspected

### 1. Shen–Zhu–Zhu, arXiv:2204.12737

H. Shen, R. Zhu, X. Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, arXiv:2204.12737; Commun. Math. Phys. 400 (2023).

Primary PDF: `https://arxiv.org/pdf/2204.12737` (retrieved 2026-08-11).

Source-bound facts used in this audit:

- Their finite-volume lattice Yang–Mills measure is the Wilson plaquette measure on `G^{E^+_Λ}` for `G=SO(N)` or `SU(N)`, with Haar product base measure and action `N beta Re sum_p Tr(Q_p)` (paper equations (1.1)–(1.2)).
- Under Assumption 1.1, Theorem 1.2 states that the whole sequence of finite-volume Yang–Mills measures converges to one unique infinite-volume measure `mu^ym_{N,beta}`.
- They define `C^infty_cyl(Q)` as smooth functions of finitely many edge variables (equation (1.8)).
- Corollary 1.6 applies to arbitrary disjoint-support `f,g in C^infty_cyl(Q)` and bounds their covariance by a finite source/support-dependent prefactor times one exponential `exp(-c_N d(Lambda_f,Lambda_g))`; the exponent `c_N` is common at fixed `N,d,beta` in the stated strong-coupling regime.
- The paper explicitly describes Osterwalder–Seiler 1978 as earlier work on the same lattice Yang–Mills class at strong coupling and distinguishes its own stochastic/Langevin machinery from the Euclidean covariance statement.

**Boundary:** SZZ's Poincaré/log-Sobolev spectral gap is a gap for the Langevin/Markov generator. It is not identified here with the physical transfer Hamiltonian. Only their Euclidean Gibbs measure and covariance theorem are admissible inputs to `YM-S1a2`.

### 2. Lüscher 1977

M. Lüscher, *Construction of a selfadjoint, strictly positive transfer matrix for euclidean lattice gauge theories*, DESY 76/61 (1977), later Commun. Math. Phys. 54, 283–292.

Primary PDF: `https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf?version=1` (retrieved 2026-08-11).

Source-bound facts used in this audit:

- Lüscher states OS positivity for gauge-invariant positive-time observables and constructs the physical Hilbert space by quotienting null vectors and completing the positive-time observable space.
- In that construction the one-step positive Euclidean-time shift is identified with `T=e^{-aH}`; positivity of `T` is separately established for Wilson lattice gauge theory.
- He also constructs the canonical time-zero gauge Hilbert space as an `L^2` space over compact-group link variables at finite spatial volume.

This is strong evidence that **positive-time observable density is structural to the OS construction**, rather than an independent spin-network theorem. It does not by itself establish that SZZ's particular smooth infinite-volume cylinder subclass is dense after the OS quotient.

### 3. Osterwalder–Seiler 1978

K. Osterwalder, E. Seiler, *Gauge field theories on a lattice*, Ann. Phys. 110 (1978), 440–471, DOI `10.1016/0003-4916(78)90039-8`.

The primary publisher abstract states physical positivity for lattice gauge Schwinger functions, implication of a positive self-adjoint transfer matrix, and strong-coupling infinite-volume/analyticity/confinement results.

**Boundary:** this audit does not infer that every infinite-volume measure built by a later method is automatically the identical OS reconstruction without checking the finite-volume measure identity and passage of the positivity inequality.

## Source-bound narrowing

### A. Same finite-volume model is substantially bound

SZZ define the standard Wilson plaquette Gibbs measure. Their own introduction identifies Osterwalder–Seiler as the closely related earlier strong-coupling treatment of lattice Yang–Mills. This removes the most severe possibility that the covariance theorem concerns an unrelated Euclidean model.

What is still missing is a **written infinite-volume OS inheritance proof** for the exact SZZ limit. The natural route is short but remains a candidate obligation rather than a source fact: for every fixed local positive-time gauge-invariant observable `F`, finite-volume reflection positivity gives a nonnegative number `mu_L(theta(F) F)`; local weak convergence to `mu^ym` should then pass this inequality to the limit. The exact reflection plane, boundary convention and locality needed for this passage must be fixed before proof credit.

### B. The density problem is narrower than a generic basis-completeness problem

Lüscher's physical OS Hilbert space is, by construction, the completion of positive-time gauge-invariant observables modulo the null space. Therefore the issue is **not** to find an external basis of the entire physical Hilbert space from scratch.

The exact remaining question is whether the **gauge-invariant smooth cylinder subalgebra controlled by SZZ** is dense in that OS completion. A plausible approximation route is exposed but not yet promoted:

1. finite-coordinate cylinder functions generate the product configuration sigma-algebra;
2. on each finite compact-group coordinate set, smooth functions are dense in the relevant finite-dimensional `L^2` marginal;
3. gauge averaging preserves gauge invariance and smoothness;
4. if the OS seminorm is controlled by the Euclidean `L^2(mu^ym)` norm through Cauchy–Schwarz plus reflection invariance, `L^2` approximation would imply OS-norm approximation;
5. subtracting the vacuum expectation would target the vacuum-orthogonal sector.

Every arrow in this route must be checked in the exact infinite-volume gauge-invariant positive-time algebra. Until then this is a **repair route**, not a theorem candidate.

### C. SZZ supplies the right common-rate shape

Corollary 1.6 is stronger than a finite list of correlator decays for the purpose of the abstract `YM-S1a1` lemma: at fixed strong-coupling parameters, its exponent is common across the smooth cylinder source class, while the prefactor may depend on the source supports/norms. For a fixed source translated by `n` time steps, any finite source-dependent prefactor disappears under `n`th roots.

The unresolved geometric obligation is exact: show the support distance between a fixed source and its positive-time translate is `n+O_F(1)` under the SZZ edge-support metric and that the centered covariance is exactly the transfer moment `<[F],T^n[F]>` (possibly after one fixed offset convention). This is expected to be elementary once the same-theory OS construction is bound, but it remains unproved here.

## Three residual sub-obligations

The source audit contracts the issue #88 residual to:

- **S1a2-RP:** prove finite-volume Wilson reflection positivity passes to the unique SZZ infinite-volume measure for the exact positive-time local gauge-invariant algebra and yields the one-step OS shift `T` on the reconstructed Hilbert space;
- **S1a2-DENSE:** prove gauge-invariant `C^infty_cyl` positive-time sources are dense modulo nulls in the same OS Hilbert space, and centered sources are dense in the excited/vacuum-orthogonal sector;
- **S1a2-TIME:** prove `Cov_mu(F, tau_n F)=<[F],T^n[F]>` with the registered centering/offset convention and `d(Lambda_F,Lambda_{tau_n F})=n+O_F(1)` for fixed finite source support.

If all three close, the already-supported abstract dense-source lemma becomes applicable only to the fixed-cutoff, infinite-volume, strong-coupling theory. G5 RG transport, G6 physical `a` scaling, G7 continuum spectral identification, continuum existence/nontriviality, and the Clay root remain open.

## Same-context expert cell

These are role-separated analytical passes in one context, **not independent review**.

1. **Constructive lattice gauge / OS lead.** The finite-volume model identity is now sufficiently specific to justify attacking positivity inheritance directly. Strongest objection: boundary/reflection conventions can invalidate an informal limit argument. Vote: `REVISE -> freeze S1a2-RP exact contract before proof`.
2. **Transfer-spectrum lead.** The parent `YM-S1a1` spectral theorem no longer needs modification. The bottleneck has moved entirely to source/Hilbert applicability. Strongest objection: density in an ambient `L^2` space is not automatically density in the OS quotient without a norm comparison. Vote: `ACCEPT residual rotation`.
3. **Stochastic/SZZ lead.** Corollary 1.6 has the required source-independent exponent shape and is directly infinite-volume. Strongest objection: no use of the Langevin generator gap is permitted as physical-Hamiltonian evidence. Vote: `ACCEPT Euclidean covariance input only`.
4. **Adversarial mathematical-physics lead.** The proposed smooth-cylinder density route could fail if gauge averaging/reflection support, null-space behavior, or the OS seminorm comparison is mishandled. Cheapest hostile tests: a source crossing the reflection plane; a sequence convergent in ordinary `L^2` but not shown OS-Cauchy; a noncentered source dominated by vacuum. Vote: `BLOCK candidate until exact algebra/norm contract is frozen`.
5. **Formal-assurance lead.** Issue #88 exists, but no fresh `YM-S1a2` context/memory/trace chain has yet been frozen on current RAKL. This source audit may be retained as pre-candidate evidence; candidate generation remains forbidden. Vote: `BLOCK CANDIDATE_PROPOSED`.
6. **Novelty/metrology lead.** If the three interfaces close by standard OS/L2 approximation and lattice geometry, the result is likely compositional/`RAKL_TRIVIAL` relative to the now-registered ingredients rather than a novel primitive. Scientific value would be exact gluing closure, not novelty. Vote: `DO NOT CLAIM NOVELTY`.

## Decision

`SOURCE_BRIDGE_NARROWED / CANDIDATE_GENERATION_BLOCKED`.

The next admissible action is to freeze a fresh `YM-S1a2` MathContextFiber and dual-memory/trace packet around **S1a2-RP + S1a2-DENSE + S1a2-TIME**, then select the cheapest one of those interfaces for a candidate proof. This audit does not backfill that chronology.

## RAKL method-case observation

This cycle is evidence that the RAKL gluing discipline changed the research unit from “prove another mass-gap lemma” to “bind three exact applicability interfaces for an already-valid local lemma.” The important outcome is residual localization rather than theorem production. Because a pre-memory counterfactual preference was not frozen before this run, no causal credit is assigned to RAKL for that decision in the metrology receipt.
