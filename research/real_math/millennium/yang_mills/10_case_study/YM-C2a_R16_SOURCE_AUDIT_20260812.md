# YM-C2a R16 — MRS fixed-IR UV construction source audit

**Authority:** proposal/shadow only. No theorem-falsity claim, no lesson, no protected obstruction, no independent-review credit, no root authority.

**Frozen atom:** `YM-C2a-MRS-UV-REMOVED-IR-CUTOFF-OS-POSITIVITY-IR-REMOVAL-SAME-THEORY` (issue #276). The pre-action receipt was committed before the detailed primary-source audit. Abstract/bibliographic discovery of MRS 1993 is explicitly retrospective and receives no prospective-discovery credit.

## Primary source and exact scope

Primary text: Jacques Magnen, Vincent Rivasseau, Roland Sénéor, *Construction of YM4 with an infrared cutoff*, Communications in Mathematical Physics 155 (1993), 325–383, DOI `10.1007/BF02097397`. The author TeX is archived as mp_arc `92-38`; an author-uploaded scan of the published paper was also inspected.

The paper states a theorem that, for its fixed infrared regulator and regularized axial-gauge construction, the ultraviolet limit of the Schwinger functions (moments of its bare measure) exists and satisfies the infrared-cutoff-adapted Slavnov identities. This is useful UV-side constructive information.

The same primary source also places four exact verification boundaries on that statement:

1. **Proof completeness.** In the introduction the authors say they do not give all convergence proofs in detail; immediately after the theorem-form statement they say a detailed self-contained proof is not supplied and would require a much longer write-up. Under the root contract this means the paper cannot by itself serve as a closed proof certificate; omitted arguments/dependencies have to be source-bound and audited.
2. **Infrared removal.** The source explicitly says it does not try to remove the infrared cutoff. It associates that regime with large coupling and confinement/nonperturbative effects outside the constructive methods developed there. Section II again fixes an IR cutoff and says it is never lifted.
3. **OS positivity.** The source says the complete Osterwalder–Schrader axiom set is not studied and presents OS positivity as something the authors think could be obtained with additional lattice-first/momentum-slicing work. It is therefore a proposed repair coordinate, not a proved property of the continuum Schwinger family in this paper.
4. **Physical gauge-invariant observables.** The axial gauge is explicitly non-Euclidean invariant, hence its gauge-fixed correlation functions are not Euclidean invariant. The source says gauge-invariant Euclidean-covariant physical observables involve composite-operator renormalization and that those constructions are not provided.

The source also does not investigate large gauge transformations or non-trivial topological effects. Its explicit field-theory construction is for pure `SU(2)` in the trivial topological sector. An exact search of the author TeX found no `mass gap` theorem; more decisively, the source itself stops before IR removal/confinement and before OS reconstruction.

## DifferenceWitness against the official root

| Cell | MRS 1993 | Root-facing requirement |
|---|---|---|
| UV regulator | removed (`rho -> infinity`) in stated Schwinger theorem | continuum UV removal with closed proof/dependency audit |
| IR regulator / volume | fixed; explicitly not lifted | infinite-volume / IR-removed state with uniform estimates |
| gauge group/topology | `SU(2)`, trivial topological sector | every compact simple gauge group; no silent sector restriction |
| gauge representation | regularized axial gauge + background-dependent small-field gauges | gauge-invariant physical observable/source algebra on same theory |
| Euclidean covariance | axial-gauge correlations explicitly not Euclidean invariant | Euclidean/OS axioms on physical source family |
| OS positivity | proposed as additional work | proved RP/OS positivity and reconstruction |
| gauge identities | cutoff-adapted infinitesimal Slavnov identities | full root-facing physical/gauge-invariant state binding |
| physical composites | acknowledged but not constructed | renormalized gauge-invariant observables on same continuum state |
| mass gap | not supplied | positive physical Hamiltonian spectral gap |
| proof closure | detailed convergence proof omitted in source | closed proof DAG + dependency/axiom/verifier audits |

## Expert-cell findings

- **Constructive gauge QFT / renormalization:** retain MRS as a high-value UV architecture and theorem statement, but root verification must source-bind the omitted convergence arguments.
- **OS reconstruction:** axial positivity is not OS reflection positivity; the source itself marks OS positivity as additional work.
- **Rigorous RG / infrared:** the exact bridge needed after R15 begins where MRS stops: fixed IR cutoff must be removed with estimates uniform enough to preserve the same state.
- **Gauge / Slavnov:** the nonperturbative Slavnov identities are valuable but are cutoff-adapted and infinitesimal; they do not by themselves construct the gauge-invariant physical source algebra.
- **Functional analysis / Schwinger distributions:** the gauge-fixed Schwinger family is not yet the Euclidean-covariant physical observable family required for OS reconstruction.
- **Spectral / mass gap:** without IR removal + RP/OS + physical-source binding, no physical Hamiltonian gap can be inferred from this source.
- **Adversarial provenance / metrology:** classify this as source applicability/proof-completeness and contextual-theory-gluing evidence, not a proof that the MRS theorem is false.

All roles shared the same evidence context, so independent mathematical review credit remains `0/3`.

## Residual

`RES-YM-C2a-SELF-CONTAINED-UV-PROOF-DEPENDENCY-CLOSURE-PLUS-GAUGE-INVARIANT-OS-POSITIVITY-PLUS-UNIFORM-IR-REMOVAL-AND-PHYSICAL-GAP-SAME-THEORY`

The next admissible source search is not another fixed-cutoff SZZ calculation and not a reconstruction from remembered constructive-QFT lore. It is a later primary theorem (or closed chain of primary theorems) that actually supplies the omitted UV convergence dependencies and/or carries a same-theory MRS/Balaban-type UV construction through IR removal to an OS-positive gauge-invariant state with physical spectral control.

## Provenance

- Frozen base: `9e36dd83874bfc9f8ef94a2ce2708769cc25861e`
- Pre-action commit: `ae1b7514bd40e251199941e10ede03ebbf35baef`
- RAKL main used at freeze/audit: `43897d3afaf0038385102d5acc64793c05ec40f0`
- RAKL method: `3.0.0`; package: `0.1.0`; constitution epoch: `v3-authority-hardening-20260811`
- Visual verification: five published-PDF screenshot attempts; one success. The successful page is journal p.327 and visibly contains the IR non-removal, OS-as-future-work statement, UV theorem formulation, and detailed-proof disclaimer. The other four screenshot attempts failed with backend cache misses; parsed author TeX / PDF text remained available.
