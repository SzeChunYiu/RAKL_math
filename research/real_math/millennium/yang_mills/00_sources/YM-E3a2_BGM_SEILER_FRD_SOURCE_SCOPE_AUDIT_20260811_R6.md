# YM-E3a2 — cited FRD source-scope audit (R6)

**Authority:** `PROPOSAL_SHADOW_SOURCE_AUDIT / NO_THEOREM_PROMOTION / ROOT_AUTHORITY_NONE`  
**Root:** `RAKL_math#5`, still `OPEN_NO_SOLUTION_CERTIFICATE`  
**Active atom:** `YM-E3a2` / `YM-E3a2-SAME-THEORY-FRD-RHO-C-STRICT-RADIUS-ENTRY`  
**Frozen fibre:** `../10_case_study/YM-E3a2_FIBRE_RECEIPT_20260811_R6.json`, hash `96828be2fb2a681ba91d790adb48ec1a1cb2dc0ba2e6c61de86e869f7cbddc1e`.

This audit asks only whether the references explicitly cited at Faizal–Shabir Appendix A.9/A.40–A.43 source-bind the **same non-Abelian Yang–Mills** diameter-weighted polymer RG map with the quantitative hypotheses needed by the already-proved local invariant-ball lemma in draft PR #157. It is not a literature-wide nonexistence claim.

## 1. Claiming-source interface

Primary source: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1, 9 June 2026, Appendix A, PDF pp. 589–590.

At A.40–A.43 the paper says that, “by standard FRD renormalization (cf. [3, 11]),” the one-step map on a diameter-weighted polymer Banach algebra has

`Phi' = L Phi + Q(Phi,Phi)`, `||L|| <= rho < 1`, and `||Q(Phi,Phi)|| <= C ||Phi||^2` for `||Phi|| <= r`, with the bounds asserted uniform in scale. The same appendix identifies [3] as Brydges–Guadagni–Mitter (2004) and [11] as Seiler (1982).

The exact local recurrence repair in draft PR #157 is deliberately not re-proved here. It requires a strict invariant radius `r_*` with `C r_* < 1-rho` and an independently valid entry theorem into that radius. The present question is whether the cited external sources actually provide the typed Yang–Mills hypotheses to which that lemma may be glued.

## 2. Reference [3]: Brydges–Guadagni–Mitter does not itself close the Yang–Mills nonlinear-map interface

Primary source: D. C. Brydges, G. Guadagni, P. K. Mitter, *Finite Range Decomposition of Gaussian Processes*, arXiv:math-ph/0303013v3 / J. Stat. Phys. 115 (2004) 415–449.

The paper’s abstract and Theorem 1.1 prove a finite-range, positive-semidefinite decomposition for the lattice Gaussian covariance `(a-Delta)^(-1)` and related fractional Laplacian covariances, including scale limits and uniform Sobolev-type bounds for the covariance pieces. Its introduction and Section 4 explain how those covariance decompositions generate RG transformations by integrating independent **Gaussian** fluctuation fields, e.g. the generic transformation `z_{n+1}(phi)=int dmu_{Gamma_n}(zeta) z_n(zeta+phi_{L^-1})`.

That is a genuine and relevant structural ingredient, but it is not the same mathematical object as the Appendix-A claim that a non-Abelian Yang–Mills polymer interaction admits a bilinear nonlinear map with a scale-uniform strict contraction on the stated diameter-weighted norm. A bounded full-text audit of the 27-page primary paper finds no occurrence of “Yang-Mills” or “polymer norm”; the only textual hit for “contraction” is a random-walk/Feller semigroup contraction, not a theorem of the required nonlinear RG form. The theorem statement itself is about covariance functions, not a gauge-field polymer Banach map.

### DifferenceWitness for transfer from [3]

The transfer is therefore **not licensed** without a separate theorem closing at least these differences:

- Gaussian covariance decomposition versus a non-Abelian gauge-field/polymer interaction map;
- generic functional integration versus an exact `L+Q` decomposition on the same Yang–Mills Banach norm;
- no source-bound same-action/gauge-group/background-field domain;
- no source-bound scale/volume/regulator-uniform `rho,C,r` for the Yang–Mills map;
- no source-bound gauge covariance/reflection-positivity compatibility for that nonlinear map;
- no source-bound noncircular tuning into a prescribed strict `r_* < min(r,(1-rho)/C)`.

**Scoped conclusion for [3]:** `FRD_COVARIANCE_INGREDIENT_CONFIRMED / SAME_THEORY_YM_NONLINEAR_CONTRACTION_NOT_ESTABLISHED_BY_THIS_SOURCE`.

This does **not** say that BGM cannot be used as an ingredient in a longer construction; it says only that citing BGM alone does not bind A.41–A.43 at the strength required by `YM-E3a2`.

## 3. Reference [11]: exact theorem detail remains unavailable, so it cannot be reconstructed from memory

Faizal–Shabir [11] is Erhard Seiler, *Gauge Theories as a Problem of Constructive Quantum Field Theory and Statistical Mechanics*, Lecture Notes in Physics 159, Springer, 1982. The current official Springer surface confirms the book, author, date, and chapter ranges (lattice gauge theories pp. 3–98; continuum gauge quantum field theories pp. 99–181), but exposes only subscription-preview metadata in this run.

No exact theorem/page was acquired that supplies the Appendix-A diameter-weighted polymer map, scale-uniform `rho,C,r`, the gauge/reflection-positivity compatibility, or the strict-radius entry theorem. Because primary mathematical detail is missing, its applicability is recorded as `BLOCKED/UNKNOWN`; no theorem is reconstructed from title, age, subject metadata, or memory.

The chronology is only a disanalogy signal, not a proof: Seiler (1982) predates the BGM finite-range-decomposition paper (2004), so the book cannot literally be evidence for the later BGM theorem as such. It may contain older cluster/block-spin/gauge estimates that are relevant, but exact source detail is required before any transfer.

## 4. Expert-cell synthesis

1. **Constructive RG/polymer norms:** BGM supplies a covariance decomposition and a generic Gaussian integration transform; that does not type-check the claimed Yang–Mills `L+Q` contraction constants.
2. **Non-Abelian lattice gauge / gauge covariance:** the missing bridge must live on the same gauge field/configuration space and preserve the gauge and reflection-positive interfaces used downstream.
3. **Nonlinear dynamics:** draft PR #157 already resolves the scalar recurrence after strict invariant-ball entry; repeating that proof has zero information gain. The unknown is now the source-specific domain/constants/entry map.
4. **Constructive continuum QFT / OS reconstruction:** even a valid weak-coupling RG contraction would close only a local/source-gluing atom, not the existence, nontriviality, OS reconstruction, continuum limit, or physical-gap obligations.
5. **Primary-source/adversarial audit:** [3] is positively identified as an ingredient rather than a closing theorem; [11] remains unknown because theorem-level content was not obtained. Missing detail is not backfilled.
6. **RAKL v3 assurance/metrology:** this cycle records a source-applicability relation and route narrowing, not a new reusable obstruction or protected lesson; same-context expert agreement gives zero independent-review credit.

## 5. Episode → diagnosis → obstruction/lesson separation

- **Episode:** bounded audit of the exact source pair cited for A.40–A.43.
- **Diagnosis:** the citation interface is under-typed. BGM verifies the FRD covariance ingredient but not the same Yang–Mills nonlinear contraction theorem; Seiler theorem detail remains unavailable.
- **Existing obstruction:** `RAKL_math#159/YM-E3a2` remains open and is narrowed to a source/genealogy/gluing problem rather than a scalar-recurrence problem.
- **New obstruction:** none promoted.
- **Reusable lesson:** none minted; the evidence is source-scoped.

Local mathematical failure this cycle: **none new**.  
Local source-proof/source-binding failure: **A.41–A.43 are not externally bound by [3] at the required type; [11] remains UNKNOWN**.  
Local-to-global/gluing failure: **the repaired recurrence cannot yet be attached to a same-theory Yang–Mills FRD map, and all later OS/continuum/spectral/root interfaces remain separate**.

## 6. Residual and next discriminator

`YM-E3a2` remains `BLOCKED`, but the search space is narrower. Do not spend another cycle treating BGM Theorem 1.1 as if it were the missing nonlinear Yang–Mills theorem. The next primary-source action is to acquire theorem-level content from Seiler relevant to the exact polymer/block-spin estimates **or** trace the citation genealogy to a primary constructive gauge-RG source that explicitly proves the same non-Abelian map with its norm, constants, gauge/RP compatibility, and uniformity. Any such source remains an analogue until its DifferenceWitness is closed against the exact Faizal–Shabir objects.

Downstream issues #69, #73/#92, #109, #126/#133, continuum existence/nontriviality, physical spectral identification, and all root gates remain open and independent.
