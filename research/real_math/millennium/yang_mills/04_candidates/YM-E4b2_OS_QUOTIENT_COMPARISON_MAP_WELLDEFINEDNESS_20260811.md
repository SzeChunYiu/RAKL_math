# YM-E4b2 — OS quotient comparison-map well-definedness before continuum gap transport

**Parent:** `YM-E4b`, RAKL_math issue #126  
**Root:** RAKL_math issue #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Atom signature:** `YM-E4b2-OS-QUOTIENT-COMPARISON-MAP-WELLDEFINEDNESS`  
**Framework freeze:** `SzeChunYiu/RAKL@2c7cec5bcb5c090be708926a685b3105dda6780e`, method `3.0.0`, package `0.1.0`  
**Application freeze:** `SzeChunYiu/RAKL_math@dc83b72201cb58844b2bdc76117e4dcb9190211d`  
**Pre-action receipt:** `YM-E4b2-PRE-ACTION-20260811T173237Z`, sha256 `373a73b788e92aaa05f95a273d8f3de653d5800af24064580ed047c3072c44ab`  
**Frozen fibre:** sha256 `ab6b9559b480796aaef4bc0ea316ee1e00cb6165b954c8027f3c8af3d880f427`  
**Authority:** `PROPOSAL_SHADOW / LOCAL_ELEMENTARY_LEMMA / SAME_CONTEXT_VERIFICATION_ONLY / NO_SOURCE_REPAIR_CERTIFICATE / NO_ROOT_AUTHORITY`.

## 1. Exact question and why it is prior to spectral transport

The predecessor `YM-E4b1` (draft PR #130) showed an abstract fixed-physical-time gap-transfer step: exact regulator-to-continuum isometries are not logically necessary if one already has actual bounded comparison maps, vacuum compatibility, strong semigroup intertwining, and a uniform physical excited-sector contraction. The present atom checks a logically prior typing obligation: whether the comparison-map rule itself descends through regulator-dependent Osterwalder–Schrader null quotients.

For positive-semidefinite OS forms `Q` and `Q_sigma`, a symbol such as

`U_sigma([F]) = [F_sigma]_sigma`

is not yet a map on the quotient unless the result is independent of the representative of `[F]`. Pointwise convergence of OS forms only gives asymptotic smallness of the regulated norm of a continuum-null representative; quotient descent requires exact null compatibility at each regulator where the map is asserted.

## 2. Quotient-descent lemma

Let `A` and `A_sigma` be complex vector spaces equipped with positive-semidefinite sesquilinear forms `Q` and `Q_sigma`. Let

`N = {F in A : Q(F,F)=0}` and `N_sigma = {G in A_sigma : Q_sigma(G,G)=0}`.

Let `R_sigma : A -> A_sigma` be linear. Consider the proposed rule

`U_sigma : A/N -> A_sigma/N_sigma`, `U_sigma([F]) := [R_sigma F]_sigma`.

**Lemma.** The rule is well-defined if and only if

`R_sigma(N) subseteq N_sigma`.  (NULL)

**Proof.** If `U_sigma` is well-defined and `F in N`, then `[F]=0` in `A/N`, hence `U_sigma([F])=0`; therefore `[R_sigma F]_sigma=0` and `R_sigma F in N_sigma`. Conversely, if `(NULL)` holds and `[F]=[G]`, then `F-G in N`; linearity gives `R_sigma(F-G) in N_sigma`, so `[R_sigma F]_sigma=[R_sigma G]_sigma`. QED.

There is a second, distinct completion obligation.

**Bounded-extension criterion.** Once quotient descent holds, `U_sigma` extends boundedly from `A/N` to the Hilbert completion `H` exactly when there is a finite constant `C_sigma` with

`Q_sigma(R_sigma F,R_sigma F) <= C_sigma^2 Q(F,F)` for every `F in A`.  (DOM_sigma)

A regulator-uniform bound `sup_sigma C_sigma < infinity` is what is needed for a uniform dense-core extension argument. Exact isometry is the special case `C_sigma=1` with equality of the forms; it is stronger than necessary.

## 3. Counterexample-first falsification: asymptotic isometry does not imply quotient descent

Take `A=R^2`, `R_n=I`,

`Q_infty((x,y),(x,y)) = x^2`,

and

`Q_n((x,y),(x,y)) = x^2 + y^2/n`.

Then `Q_n(u,v) -> Q_infty(u,v)` for every fixed pair `u,v`, so the forms are pointwise asymptotically isometric. But `N_infty=span(e_2)` while `N_n={0}`. Thus `[0]=[e_2]` in the continuum quotient, whereas `[0]_n != [e_2]_n` for every finite `n`. The rule `J_n[F]=[F]_n` is therefore not a function on `A/N_infty`.

The same example shows the exact logical distinction: `Q_n(e_2,e_2)=1/n -> 0` is insufficient; quotient descent requires `Q_n(e_2,e_2)=0` for every `n` on which `J_n` is defined.

An exact-rational computation was used only to calibrate this hostile control for several finite `n`; the proof is the two-line analytic calculation above. Computation carries no proof authority.

## 4. Source audit against arXiv:2606.19362v1

Primary source: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 June 2026).

### Main text section 8.2

On PDF page 89 (source text lines 6400–6411 in the retrieved primary PDF), the paper takes a continuum positive-time algebra, chooses lattice representatives `F_sigma`, declares `U_sigma([F])=[F]_sigma`, and then derives pointwise convergence of OS inner products, calling this an asymptotic isometry. The displayed convergence by itself does not establish `(NULL)` for a fixed `sigma`. Thus the main-text definition is under-typed unless an earlier exact null-space compatibility result is imported.

This is not a claim that no repair exists. It identifies the exact missing interface needed before the subsequent strong-semigroup calculation can be interpreted as an operator statement on quotient Hilbert spaces.

### Appendix D supplies a stronger sufficient hypothesis, but source binding remains open

A later Appendix-D formulation uses a common positive-time algebra `A+`, forms `Q_k`, null spaces `N_k`, and limit form `Q_infty`. On PDF page 544, equation (D.5) imposes

`sup_k Q_k(F,F) <= M Q_infty(F,F)` for every `F in A+`.

This condition is stronger than `(NULL)` and is exactly sufficient for both tasks relevant here:

1. if `F in N_infty`, then the right side is zero, hence `Q_k(F,F)=0` for every `k`, so `N_infty subseteq N_k` and `J_k[F]=[F]_k` descends exactly;
2. the same inequality gives `||J_k|| <= sqrt(M)`, hence the uniform bounded extension to the completed continuum Hilbert space.

Therefore Appendix D contains the right *shape* of repair. However, in the inspected primary-source surface it introduces (D.5) as an imposed uniform estimate said to hold under the constructive locality/clustering setting; this cycle did not locate a prior derivation establishing this domination inequality from the earlier RG/locality estimates with the same algebra, embeddings, regulator sequence, volume limit, and continuum subsequence. The paper's immediately following representative-independence explanation instead notes only that `Q_k(F-G,F-G) -> 0`; that convergence alone is not sufficient for exact consistency, although (D.5) would make the consistency statement valid for a stronger reason.

Accordingly, the source-facing residual is narrower than the generic `YM-E4b` objection: **prove/source-bind (D.5), or an equivalent exact null-inclusion plus uniform bounded-extension estimate, in the actual same-theory continuum construction.**

### Source-verification limitation

The primary arXiv PDF text was parsed directly and exact section/page locations were checked. Image screenshots of the relevant PDF pages were attempted repeatedly through the available PDF screenshot surface, but the retrieval backend returned a cache-miss error. This is recorded as a tooling/verification limitation, not a mathematical failure and not evidence against the source.

## 5. Same-context expert cell

These are role-separated checks sharing one research context; none counts as independent review.

- **Constructive QFT / OS reconstruction:** verified that the issue is quotient descent through null spaces, separate from the already-known positive-time semigroup/isometry defect. Verdict: `(NULL)` is the minimal exact representative-independence condition; source application remains blocked until the same OS family supplies it.
- **Functional analysis / varying Hilbert spaces:** checked the necessity/sufficiency proof and the bounded-extension criterion. Verdict: pointwise form convergence does not imply exact descent; (D.5) would supply both descent and a uniform operator bound.
- **Lattice gauge spectral theory:** checked that this atom is upstream of interpreting a transfer/semigroup bound as a continuum Hamiltonian gap. Verdict: no spectral promotion follows from a comparison map that has not been defined on the physical quotient.
- **RG / continuum limit:** checked the local-to-global interface. Verdict: the next source proof must retain volume/lattice-spacing uniformity and identify the same gauge-invariant continuum algebra/subsequence; generic locality or clustering language is not a substitute for the domination inequality.
- **Adversarial verifier:** supplied the two-dimensional positive-semidefinite hostile family and deletion test. Verdict: asymptotic isometry alone is falsified as a descent principle.
- **RAKL v3 assurance / metrology:** checked current v3 pre-action receipt semantics, selected/rejected memory, proposal-only authority, and chronology. Verdict: the discriminator was frozen before the formal lemma/counterexample test, but the quotient concern was noticed during source reading before the receipt, so the run claims prospective **test** binding only, not prospective hypothesis-generation/discovery credit.

## 6. Local result versus gluing result

**Local mathematical outcome:** `PARTIAL_SUCCESS`. The exact quotient-descent and bounded-extension conditions are isolated and proved. The finite-dimensional hostile family rules out using pointwise asymptotic isometry as a substitute.

**Local-to-global/source gluing:** `BLOCKED`. Appendix D's (D.5) is a sufficient repair hypothesis, but this cycle did not establish that the paper's earlier constructive estimates prove (D.5) on the same source algebra and along the same continuum trajectory. The known OS contraction-semigroup repair in #126, fixed-physical-time normalization in #92, source-family completeness in #109/PR #62, and uniform physical excited-sector contraction from PR #130 remain separate obligations.

No numerical evidence, confinement statement, finite-cutoff gap, or source-restricted decay estimate is promoted to a continuum Yang–Mills mass gap.

## 7. Novelty, saturation, and next discriminator

The solved local subproblem is classified, only for RAKL routing purposes, as **representation-class**: it clarifies which quotient-space representation makes cross-regulator comparison meaningful. Mathematically it is elementary/compositional and carries no theorem-novelty authority.

The high-information next discriminator is now precise: starting from the earlier constructive estimates actually proved in arXiv:2606.19362v1, derive or refute equation (D.5) with exact domains, regulator/volume/lattice-spacing quantifiers and the same continuum subsequence. If (D.5) cannot be derived, isolate the first missing estimate. If it can, bind it to the corrected OS contraction semigroups and then test the fixed-physical-time `INT` and `UGAP` obligations from `YM-E4b1`.

`RAKL_math#5` remains `OPEN_NO_SOLUTION_CERTIFICATE`. No proof-DAG closure, formal verification, independent review, barrier audit, or root promotion is claimed.
