# YM-E4b retrospective source audit — OS semigroup and continuum Hilbert-space identification

**Date:** 2026-08-11  
**Framework inspected before mathematical work:** `SzeChunYiu/RAKL@fe47a12c4bad8253658baaf37e1300cab15d0823`, RAKL Method `3.0` / release `v3.0.0`  
**RAKL_math freeze base:** `f54becbed3b74d0fdb2002a2e5a49326cf0294dd`  
**Root:** `RAKL_math#5`, `OPEN_NO_SOLUTION_CERTIFICATE`  
**Prospective repair atom opened after the observations:** `YM-E4b`, issue #126  
**Authority:** `RETROSPECTIVE_PRIMARY_SOURCE_PROOF_AUDIT / PROPOSAL_SHADOW_EVIDENCE / NO_YANG_MILLS_THEOREM / ROOT_AUTHORITY_NONE`

## 1. Scope and chronology

This cycle audits one load-bearing constructive-continuum chain in:

- Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:`2606.19362v1`, 9 June 2026; DOI `10.1002/prop.70097`.

The audited interfaces are main-text Theorems 8.2–8.5 and Appendix E, especially Theorem E.1, Proposition E.2 and Theorem E.4. The observations below were made before a fresh strict prospective repair context was frozen. They are therefore permanently **retrospective**. Issue #126 freezes only the repair question that follows from them; no candidate chronology is backfilled.

The source PDF was accessed as primary text. The runtime-required visual PDF screenshot checks were attempted on three relevant pages but failed with a cache-miss tooling error. The textual theorem/proof content was nevertheless available from the primary PDF parser. This tooling failure is recorded rather than silently treated as successful visual verification.

## 2. Why this interface is root-critical

The Clay-strength root requires a single nontrivial continuum theory and a positive physical Hamiltonian gap. A regulated lattice/Euclidean clustering estimate cannot carry root authority merely because each cutoff theory has a positive transfer operator. The proof must identify the physical OS Hilbert spaces and their semigroups across the regulator/continuum limit strongly enough to transport the vacuum sector and exclude spectrum in a fixed positive interval in the **same continuum reconstructed theory**.

This is distinct from the already-stored source-family obstruction #109. Even a complete dense family with a common decay rate cannot certify a continuum gap unless its vectors and the semigroup live in the same continuum OS space reached by the regulator limit.

## 3. Finding A — Appendix E.1 uses an unproved OS isometry identity

Theorem E.1 defines the OS sesquilinear form in the standard shape

`Gamma(F,G) = S(Theta F G)`

and defines positive-time translations by `U(t)[F]=[tau_t F]`. The proof then asserts

`Gamma(tau_t F, tau_t G) = Gamma(F,G)`

by Euclidean invariance and concludes that `U(t)` is an isometry.

That displayed inference does not follow from Euclidean invariance. Reflection and positive-time translation satisfy the structural relation

`Theta tau_t = tau_{-t} Theta`.

Consequently

`Gamma(tau_t F,tau_t G) = S(tau_{-t} Theta F · tau_t G)`.

A common Euclidean translation can move both factors, but it does not remove their relative separation; it turns the OS form into one with an additional positive separation. This is exactly the mechanism by which nontrivial Euclidean time evolution loses norm and becomes a contraction rather than a general isometry.

The main text itself earlier describes the reflected positive-time evolution as a **contraction**. Thus Appendix E.1's displayed isometry route is not only unproved by the written algebra but also mismatched with the nontrivial semigroup behavior required later for decay and spectral separation.

**Disposition:** the written proof of E.1 is defective at this step. This is not an impossibility theorem. Standard Osterwalder–Schrader reconstruction supplies a contraction-semigroup paradigm, so a repair may exist if all quotient, continuity and gauge-invariant source hypotheses are supplied for the exact theory.

Primary analogues checked:

- K. Osterwalder and R. Schrader, *Axioms for Euclidean Green's functions*, Commun. Math. Phys. 31 (1973), DOI `10.1007/BF01645738`.
- K. Osterwalder and R. Schrader, *Axioms for Euclidean Green's functions II*, Commun. Math. Phys. 42 (1975), DOI `10.1007/BF01608978`.
- K. Osterwalder and E. Seiler, *Gauge field theories on a lattice*, Ann. Phys. 110 (1978), DOI `10.1016/0003-4916(78)90039-8`.

These are structural analogues and source constraints, not plug-in repairs to the 2026 proof.

## 4. Finding B — Proposition E.2 assumes exact cross-cutoff isometries and uses an invalid finite-net weak-to-strong upgrade

Proposition E.2 first places regulated and continuum vectors into a common comparison by assuming canonical **isometric identifications** from the regulator-dependent OS construction. The written strong-convergence step then proceeds from convergence of matrix elements plus uniform boundedness by choosing a finite `delta`-net of the unit sphere of the continuum Hilbert space.

For an infinite-dimensional Hilbert space, the unit sphere is not totally bounded. Therefore there is no finite `delta`-net for `delta<1`. The displayed compactness step cannot justify uniform control on the full unit sphere.

There is also a general functional-analysis separation between weak and strong convergence. As a cheap hostile control on `ell^2`, let

`v_n=(e_1+e_n)/sqrt(2)`,  `P_n=|v_n><v_n|`.

The `P_n` are positive self-adjoint contractions. Their matrix elements converge to those of `(1/2)P_{e_1}`, but

`P_n e_1 - (1/2)e_1 = (1/2)e_n`,

so the convergence is not strong on `e_1`. This is deliberately only a **generic operator hostile control**, not a counterexample to a correctly formulated semigroup convergence theorem.

For self-adjoint contraction semigroups a stronger argument may be recoverable, for example by combining convergence at `t` and `2t` with a legitimate identification structure, or through a varying-Hilbert-space Mosco/generalized-resolvent theorem. The present source must prove such hypotheses rather than relying on a nonexistent finite net.

## 5. Finding C — Section 8 moves from asymptotic isometry to exact isometry without a bound interface

The main text initially defines regulated source maps from a dense continuum source domain and derives convergence of their inner products. It explicitly characterizes the maps as **asymptotic isometries**. That is the natural form of information one might expect before quotient/completion and regulator limits are fully controlled.

Theorem 8.4 then uses exact isometric identification maps `U_sigma : H -> H_sigma` to extend a resolvent-convergence statement from the dense domain to the full Hilbert space. Theorem 8.5 subsequently writes the identification direction oppositely, from the regulated space toward the continuum space. The source therefore needs one precise typed comparison structure with fixed domains/codomains and an explicit theorem connecting its asymptotic inner-product information to the convergence mode used later.

This is a **local-to-global/gluing failure**, not merely a local algebraic typo. Regulator-dependent OS Hilbert spaces are quotient/completion objects whose null spaces can depend on the Schwinger functional and regulator. Equality of source labels or asymptotic equality of their inner products does not by itself create a canonical exact isometry of the completed quotient spaces.

The relevant structural analogue is:

- K. Kuwae and T. Shioya, *Convergence of spectral structures: a functional analytic theory and its applications to spectral geometry*, Commun. Anal. Geom. 11 (2003), DOI `10.4310/CAG.2003.v11.n4.a1`.

That work develops spectral/semigroup/resolvent convergence on **varying Hilbert spaces** once a suitable convergence structure is specified. It is an applicability template, not an automatic repair: the OS quotient/gauge structure and all required hypotheses still have to be mapped explicitly.

## 6. Finding D — Theorem E.4 has a vacuum endpoint projection error

Theorem E.4's source-family spectral argument aims to exclude positive spectrum below `m`. For a centered source vector it is consistent to seek zero spectral measure in `(0,m)`. The proof's final vacuum line, however, says that because `Omega` is the zero-energy eigenvector,

`E([0,m)) Omega = 0`.

This is backwards. Since `0 in [0,m)`, spectral calculus gives

`E([0,m)) Omega = Omega`.

A corrected global gap statement should preserve the vacuum projection at zero and exclude spectrum in `(0,m)` on `Omega^perp`. This is a local endpoint/projection defect and appears readily repairable. It is therefore recorded separately from the more structural continuum-identification obstruction.

## 7. Bound-memory review and routing effect

### Selected prior experience

- root #5: exact existence+gap contract and non-promotion boundary;
- #109 / `F-YM-S1A-RESTRICTED-SOURCE-HIDDEN-STATE`: fixed-source decay cannot certify a full gap;
- PR #62 / `YM-S1a1-C001`: dense-common-rate spectral exclusion in an abstract fixed Hilbert space;
- #88: same-theory OS Hilbert/source binding is already a recognized gluing obligation;
- PR #97: prior Faizal–Shabir source-proof audit, useful as source/chronology precedent.

The initial pre-memory direction in this run was to test whether continuum source-family completeness might fail. Retrieval of #109 and #88 showed that this obstruction family was already stored. That **changed the selected action**: the cycle rotated to the regulator-to-continuum OS semigroup/Hilbert-space identification chain instead of minting a duplicate hidden-source obstruction.

### Retrieved but rejected for this atom

- `YM-E1a1a0`: Bałaban primary-source acquisition blocker; different and already saturated route.
- #92: variable-lattice versus fixed-physical-time gap normalization; distinct scale-coordinate defect.
- #93: weak-coupling quadratic recurrence; distinct local RG proof defect.
- #69: bare-coupling escape; distinct RG trajectory defect.

### Memory miss

Repository searches for the exact E.1/E.2/8.4 isometry and finite-net interface did not surface an existing stored audit. The varying-Hilbert-space convergence analogue was therefore retrieved externally after the source mismatch was isolated. This supports only **repository-local non-duplication**, not a literature-wide novelty claim.

## 8. Same-context expert cell

These are role-separated analytical passes in one context, **not independent review**.

| Lens | Delegated audit | Finding / vote |
|---|---|---|
| Constructive QFT / OS reconstruction | reflection/translation algebra, OS quotient, time evolution | E.1's isometry equality is not supplied by Euclidean invariance; a correct contraction construction is required. **BLOCK written route / REPAIR POSSIBLE** |
| Functional analysis / spectral convergence | weak/strong semigroup and resolvent convergence on varying spaces | E.2's finite-net step is invalid; 8.4 needs a valid varying-space comparison theorem. **BLOCK current strong-convergence proof** |
| Gauge-theory physical-state algebra | gauge-invariant quotient/null spaces and source mapping | source-label correspondence does not establish exact isometry of changing physical quotients. #109 remains a separate density/common-rate obligation. **BLOCK gluing** |
| RG / continuum-limit analysis | regulator and volume limits, uniformity, physical spectral identification | even a positive regulated gap has no continuum authority until the same-theory semigroup/Hilbert limit is proved with uniform estimates. **BLOCK root transfer** |
| Adversarial verification | finite-net, weak/strong, endpoint and hidden-space controls | all cheap controls falsify the unsupported intermediate statements at their literal scope; none proves the desired theorem impossible. **ACCEPT scoped diagnosis** |
| RAKL v3 assurance / metrology | chronology, memory routing, authority and telemetry | observations are retrospective; #126 freezes only the repair question. No lesson/theorem/novelty promotion. **ACCEPT shadow evidence** |

## 9. Episode -> diagnosis -> obstruction/lesson separation

- **Episode:** `YM-E4b-EP-FS-OS-CONTINUUM-AUDIT-20260811T1643Z`, a primary-source proof/gluing audit guided by dual success/failure memory.
- **Diagnosis:** three local written proof defects (E.1 isometry, E.2 finite-net weak-to-strong step, E.4 endpoint projection) plus one structural gluing mismatch (asymptotic/exact cross-cutoff Hilbert identification).
- **Prospective obstruction:** issue #126 asks for the correct OS contraction and varying-Hilbert convergence bridge. It is proposal-only.
- **Lesson:** **none promoted or minted**. One source audit does not authorize a reusable method lesson.

## 10. Failure lattice and residual

### Local mathematical/source-proof failures

1. `E1_OS_ISOMETRY_IDENTITY_UNJUSTIFIED`.
2. `E2_INFINITE_SPHERE_FINITE_NET_INVALID`.
3. `E4_VACUUM_ENDPOINT_PROJECTION_ERROR`.

### Local-to-global/gluing failures

1. `ASYMPTOTIC_TO_EXACT_OS_IDENTIFICATION_UNBOUND`.
2. `VARYING_HILBERT_STRONG_CONVERGENCE_UNBOUND`.
3. `GAUGE_NULL_QUOTIENT_COMPATIBILITY_UNBOUND`.
4. `VOLUME_REGULATOR_UNIFORMITY_AND_LIMIT_INTERCHANGE_OPEN`.
5. `SAME_THEORY_CONTINUUM_GAP_TRANSPORT_OPEN`.

These two layers are kept separate: repairing E.1/E.2/E.4 locally would **not** by itself prove the continuum gluing obligations.

## 11. Prospective next action under #126

Do not generate a continuum Yang–Mills theorem candidate from this audit. The next admissible action is to construct or source-bind a precise comparison diagram

`(H_sigma, T_sigma(t), Omega_sigma)  --J_sigma-->  (H, T(t), Omega)`

or an equivalent varying-space convergence structure, with exact quotient/null-space compatibility, then prove the semigroup/resolvent convergence needed to transport a uniform positive spectral exclusion. Only after that bridge closes may it compose with #109's dense-source/common-rate obligation.

Any missing primary detail in that comparison structure blocks rather than being reconstructed from memory.

## 12. Root disposition

`OPEN_NO_SOLUTION_CERTIFICATE`.

No existence theorem, continuum mass-gap theorem, novelty certificate, independent review, or root promotion is produced by this cycle.