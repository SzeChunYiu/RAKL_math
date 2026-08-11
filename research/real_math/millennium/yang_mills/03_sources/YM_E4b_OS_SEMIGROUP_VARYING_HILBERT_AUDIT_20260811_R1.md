# YM-E4b R1 — OS semigroup / varying-Hilbert-space repair audit

**Date:** 2026-08-11  
**Atom:** `YM-E4b`  
**Local candidate:** `YM-E4b-C001`  
**Authority:** `PRIMARY_SOURCE_BOUND_LOCAL_OPERATOR_REPAIR / PROPOSAL_SHADOW / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`

## Exact scope and chronology

The prospective repair atom was already frozen in `RAKL_math#126` before this cycle. That issue asks for a correct OS contraction semigroup and a valid regulator-to-continuum changing-Hilbert-space identification/convergence structure. This cycle does not backfill a new strict pre-candidate packet. The richer fibre snapshot is an after-the-fact cycle record; the only prospective credit comes from the pre-existing issue.

Primary source: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:`2606.19362v1` (9 June 2026), 593 pp., `https://arxiv.org/pdf/2606.19362`.

Exact selectors used:

- PDF p.89, Eq. (8.15) and Theorem 8.3 setup: `U_sigma : D -> H_sigma` is defined only on a dense cylinder-source domain and is called an **asymptotic isometry**.
- PDF pp.90–91, Eqs. (8.18)–(8.26): the source expands the norm difference and uses semigroup matrix elements at `t` and `2t` to derive strong convergence on the dense domain.
- PDF p.91, Theorem 8.4: the source changes the interface to exact isometric maps `U_sigma : H -> H_sigma` said to be furnished by OS reconstruction.
- PDF pp.203–204, Theorem E.1: the theorem statement correctly asks for self-adjoint contractions, while the proof asserts `Gamma(tau_t F,tau_t G)=Gamma(F,G)` and concludes positive-time translation is an isometry.
- PDF pp.204–206, Proposition E.2: it assumes canonical cross-cutoff isometries/common core and uses a finite `delta`-net of the full unit sphere to turn matrix-element convergence into strong convergence.

The web PDF screenshot renderer was invoked twice on these pages but returned a cache-miss error. The source's parsed PDF text exposed exact page/line selectors, so no image-dependent claim is made. This is recorded as a tooling failure, not a mathematical/source failure.

## Finding 1 — the Appendix E isometry conclusion would trivialize the Hamiltonian

Theorem E.1 states the correct target object: a strongly continuous semigroup of self-adjoint contractions `T(t)=exp(-tH)` with `H>=0`. Its proof then claims the positive-time shift is an isometry.

That stronger conclusion is incompatible with any nonzero positive spectrum.

### Lemma `YM-E4b-C001-A`

Let `H>=0` be self-adjoint and let `T(t)=exp(-tH)`. If for some `t>0`, `T(t)` is an isometry on the whole Hilbert space, then `H=0`.

**Proof.** Isometry gives `T(t)^*T(t)=I`. Since `T(t)` is self-adjoint, `exp(-2tH)=I`. By the spectral theorem, `exp(-2t lambda)=1` on the support of every spectral measure. For `lambda>=0` and `t>0` this forces `lambda=0`. Hence the spectral measure of `H` is supported at zero and `H=0`. QED.

Thus the Appendix E proof cannot use global isometry if it also aims at a nontrivial theory with positive-energy excitations. The needed OS object is the contraction semigroup already stated in the theorem and elsewhere in the paper.

**Novelty boundary:** issue `#126` had already recorded qualitatively that the isometry argument is wrong. The lemma above is a compositional exact consequence/verification of that stored diagnosis, not a new obstruction class.

## Finding 2 — a valid dense-domain strong-convergence repair exists without exact isometries

The main-text proof of Theorem 8.3 contains the right local functional-analytic mechanism. It can be stated independently of the source's later exact-isometry assumption.

### Lemma `YM-E4b-C001-B` — asymptotic-embedding semigroup polarization

Let `H` and `H_n` be Hilbert spaces. Let `D` be a dense linear subspace of `H`, and for a fixed `t>=0` assume `T(t)D subset D`, where `T(s)` is a self-adjoint contraction semigroup on `H`. Let `T_n(s)` be self-adjoint contraction semigroups on `H_n`, and let linear maps `J_n:D->H_n` satisfy:

1. **asymptotic inner-product preservation:**  
   `<J_n x,J_n y>_n -> <x,y>` for all `x,y in D`;
2. **semigroup matrix-element convergence:**  
   `<J_n x,T_n(s)J_n y>_n -> <x,T(s)y>` for all `x,y in D` and `s` needed below (in particular `s=t,2t`).

Then for every `phi in D`,
`||T_n(t)J_n phi - J_n T(t)phi||_n -> 0`.

**Proof.** Expand `d_n=T_n(t)J_n phi-J_nT(t)phi`. By self-adjointness and the semigroup law, `||T_n(t)J_n phi||^2 = <J_n phi,T_n(2t)J_n phi>`, which converges to `<phi,T(2t)phi>=||T(t)phi||^2`. Asymptotic inner-product preservation gives `||J_nT(t)phi||^2 -> ||T(t)phi||^2`. Finally, matrix-element convergence with `x=T(t)phi`, `y=phi` gives `<J_nT(t)phi,T_n(t)J_nphi> -> <T(t)phi,T(t)phi>`. Substitution into `||d_n||^2` gives a limit of zero. QED.

This is precisely the extra norm information absent from generic weak-operator convergence. It avoids the finite-net argument in Appendix E.2 and does not require exact cross-cutoff isometries.

The source's Eqs. (8.18)–(8.26) instantiate this pattern formally through Schwinger-function limits at `t` and `2t`.

## Finding 3 — the root-facing problem is now a representation/gluing obligation, not this local lemma

The local lemma does **not** establish the Faizal–Shabir continuum gap bridge. The following interfaces remain unproved in the audited source segment:

1. `J_sigma` is initially defined on the dense continuum cylinder domain by selected regulator approximants. To write `J_sigma T(t)phi`, one must show the selected approximation system is translation-compatible or otherwise define the map on the translated vector.
2. The statement that a fixed countable cylinder subalgebra gives a domain stable under every real `t>=0` needs an explicit construction or a time-dependent/core formulation.
3. Theorem 8.4 replaces asymptotic embeddings on `D` by exact isometries on all of `H`; the preceding argument does not furnish that upgrade.
4. Regulator-dependent OS null spaces/quotients can change. A valid changing-space convergence structure must give exact domains, codomains, null-space compatibility and map direction.
5. Resolvent convergence must be formulated on the actual varying spaces rather than by silently treating all vectors as living in one common Hilbert space.
6. Gap transport additionally needs the vacuum projections and positive spectral exclusion to refer to the same reconstructed physical Hamiltonian, with volume/lattice-spacing/regulator uniformity and gauge-invariant physical-sector compatibility.

Kuwae–Shioya's changing-Hilbert-space spectral-structure framework (Comm. Anal. Geom. 11 (2003), 599–673, DOI `10.4310/CAG.2003.v11.n4.a1`) is a structural analogue: it explicitly treats convergence across different Hilbert spaces and spectral structures. It is **not** imported as a Yang–Mills theorem. The Yang–Mills OS quotients, gauge constraints, approximation maps, forms and uniform estimates must be mapped to its hypotheses (or to another valid changing-space framework) explicitly.

## Local versus global status

- **Local mathematical result:** `YM-E4b-C001-A/B` passes the same-context source/functional-analysis/adversarial checks. The first is an elementary spectral-theorem consequence; the second is a standard polarization/semigroup argument.
- **Local source diagnosis:** Appendix E's isometry and finite-net routes are invalid as written.
- **Local-to-global/gluing status:** `BLOCKED`. A changing-Hilbert-space OS identification certificate is still missing.
- **Source-family completeness:** remains a separate obligation under `RAKL_math#109`; this cycle does not duplicate it.
- **Existence / nontriviality / RG / gauge / limit uniformity:** untouched except for sharpening the OS continuum identification interface.
- **Root:** `OPEN_NO_SOLUTION_CERTIFICATE`.

## Episode -> diagnosis -> obstruction/lesson

- **Episode:** inspect the exact E4b source interface and attempt the cheapest repair.
- **Observation:** one source proof path uses isometry/finite-net steps that do not hold; a different main-text polarization path has a valid local core.
- **Diagnosis:** the immediate mathematical repair is available, but the source lacks a licensed representation/identification map that glues the local semigroup argument across regulator-dependent OS spaces.
- **Reusable obstruction:** no new promoted obstruction. The gluing class was already frozen by `#126`; the broader local-to-root preservation pattern is already under `SzeChunYiu/RAKL#124`.
- **Reusable lesson/tool:** none promoted. A proposal-only framework hypothesis is recorded in the method case study.
