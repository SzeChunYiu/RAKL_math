# YM-S1c1 — bare-coupling escape audit of arXiv:2606.19362v1

**Root:** RAKL_math issue #5  
**Control issue:** #69  
**Framework authority inspected first:** `SzeChunYiu/RAKL@decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8`  
**Application base:** `SzeChunYiu/RAKL_math@49edbefcb3bd4bab24b154ac509ed933e8d817dc`  
**Chronology:** retrospective source audit; the discriminator was observed before this packet was frozen.  
**Authority:** `SOURCE_BOUND_RETROSPECTIVE_ROUTE_DIAGNOSTIC / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`

## Exact question

Does the weak-coupling entry argument in Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 June 2026), actually produce the Wilson bare-coupling trajectory needed by its continuum/asymptotic-freedom identification, or does its displayed tuning theorem only enter a small RG ball near a fixed finite bare coupling?

This audit is narrower than a review of the full paper.

## Root-contract and live-route binding

The live Yang–Mills root contract requires a nontrivial four-dimensional continuum QFT, OS/Wightman-strength reconstruction, the physical Hilbert space, a positive Hamiltonian gap in physical units, limit uniformity, and ultraviolet/asymptotic-freedom compatibility. Fixed-cutoff transfer positivity, strong-coupling clustering, a stochastic/Langevin gap, or a restricted correlation estimate cannot close the root by themselves.

The active spectral lane already contains two relevant local sections:

- PR #46 source-audits Shen–Zhu–Zhu and moves the ordinary box-volume question to the sharper support/source-family uniformity residual;
- PR #62 proves the abstract positive-self-adjoint dense-source/common-rate spectral exclusion lemma, while keeping same-theory OS binding, RG transport, physical lattice-spacing scaling and continuum spectral identification open.

Therefore another fixed-cutoff lemma is lower information than auditing a new primary source that directly claims the missing G5–G7 bridge.

## Fibre actually consulted

Selected knowledge / memory:

- Yang–Mills root contract and G5–G7 continuum obligations;
- Lüscher 1977 fixed-cutoff positive transfer-matrix result;
- Osterwalder–Seiler 1978 fixed-cutoff reflection-positive lattice framework;
- Shen–Zhu–Zhu arXiv:2204.12737 strong-coupling infinite-volume clustering;
- PR #46 `SUPPORT_FAMILY_UNIFORMITY_OPEN`;
- PR #62 `TARGET_BINDING_OPEN` and the old restricted-source hidden-state warning;
- Faizal–Shabir arXiv:2606.19362v1.

Selected operations:

`PRIMARY_SOURCE_COLLISION_AUDIT`, `ROOT_BRIDGE_STABILITY_AUDIT`, `CONTRASTIVE_DISCRIMINATION`, `GLUING_INTERFACE_AUDIT`.

Retrieved but rejected as lower information:

- another generic finite-volume-uniformity pass;
- another fixed-cutoff spectral lemma;
- numerical glueball calibration.

## Primary-source discriminator

The source uses `beta` as the inverse microscopic Wilson bare coupling and treats sufficiently small `beta` as its strong-coupling regime. Its weak-coupling discussion later calls `beta(a)` a bare-coupling trajectory and claims entry into an asymptotically-free continuum flow.

The displayed entry theorem is local in a fixed bare-coupling domain. In the proof of Theorem 5.4 the source assumes a compact interval `I` of `beta` values, fixes one reference `beta_* in int(I)`, and obtains constants `c0,C0` and `0<rho<1` such that

`|g_K(beta_*)| <= C0 rho^K`.

It then sets

`delta_K = (2 C0 / c0) rho^K`

and chooses a zero `beta_K` satisfying

`beta_K in (beta_* - delta_K, beta_* + delta_K)`.

For the fixed reference used in the proof,

`|beta_K - beta_*| <= delta_K -> 0`,

therefore

`beta_K -> beta_* < infinity`.

Appendix A.9 again fixes `beta_*` in a compact interval of bare couplings where the FRD expansion is valid, and later says the bare-coupling interval is restricted to a compact set to retain uniform FRD bounds.

By contrast, the downstream weak-coupling section calls `beta(a)` an asymptotically-free bare-coupling trajectory supplied by Theorem 5.4 and proves decay of an operational renormalized quantity `g_R(mu)` by taking further RG steps after entry into the contraction ball.

The latter conclusion is a statement about the operational renormalized coordinate after entry. It does not, from the displayed fixed-reference tuning alone, supply an escaping Wilson bare parameter as `a -> 0`.

## Result

`TRANSFER_BLOCKED_SCOPED / FIXED_REFERENCE_ENTRY_DOES_NOT_ESTABLISH_BARE_COUPLING_ESCAPE`

The audited Theorem 5.4 proof establishes, at most from the displayed fixed-reference argument, entry into the contraction ball using couplings approaching one finite `beta_*`. It does **not by that argument alone** establish a moving Wilson bare-coupling trajectory escaping every fixed compact interval.

This result does **not** show that no asymptotically-free trajectory exists. It does **not** refute the fixed-cutoff strong-coupling gap result. It does **not** invalidate classical reflection positivity or transfer-matrix results. It is not a global verdict on the 593-page preprint.

A source-valid repair would need a separately proved moving reference/domain—e.g. `beta_*(K)` or `I_K` escaping to weak coupling—with estimates uniform on that moving domain, or another theorem that explicitly binds the Wilson bare parameter to the continuum scale while preserving all downstream RG, gap, source-family and OS hypotheses.

## Gluing diagnosis

Retained local sections:

1. fixed-cutoff OS/transfer positivity;
2. strong-coupling fixed-cutoff/infinite-volume clustering mechanisms;
3. abstract dense-source spectral exclusion at fixed cutoff.

Open interface:

`fixed-domain RG control -> genuine Wilson bare trajectory -> scale-uniform physical gap -> continuum OS Hamiltonian`.

The local sections therefore cannot yet glue to the root certificate through this audited source theorem.

## Six-role same-context expert cell

1. **Constructive lattice gauge/RG analyst — ACCEPT scoped obstruction.** The same source distinguishes its small-`beta` strong-coupling regime from the later weak-coupling/continuum discussion.
2. **Rigorous dynamical-systems/RG analyst — ACCEPT.** A sequence constrained to an `O(rho^K)` neighborhood of one fixed finite reference converges to that reference; a moving-domain result requires extra hypotheses.
3. **OS/transfer-spectrum analyst — ACCEPT WITH SCOPE.** Fixed-cutoff spectral statements are separate local sections and are not downgraded by this audit.
4. **Asymptotic-freedom/renormalization analyst — ACCEPT.** Decay of a renormalized observable after entry does not itself identify the required microscopic Wilson bare trajectory.
5. **Adversarial source auditor — ACCEPT SOURCE-BOUNDED.** Full-text inspection finds downstream language attributing asymptotically-free bare trajectories to Theorem 5.4, but the audited fixed-reference construction does not display the missing escape theorem.
6. **RAKL v3 assurance/meta-method analyst — ACCEPT AS RETROSPECTIVE EXPERIENCE ONLY.** The discriminator predates the frozen YM-S1c1 packet and receives zero prospective candidate/promotion credit.

These are role-separated same-context AI reviews, not independent peer review.

## Competing diagnoses retained without promotion

- a moving `beta_*(K)` was intended but the needed uniform estimates are absent from the audited displayed proof;
- another bare-coupling coordinate was intended but no explicit conversion to the Wilson `beta` used in the paper has been bound;
- another theorem elsewhere in the source or literature may repair the bridge.

No impossibility diagnosis is promoted.

## Prospective child

`YM-S1c1a — MOVING-BARE-COUPLING-TRAJECTORY`

Before candidate generation, freeze a fresh context-first packet asking whether one can source or prove a trajectory `a -> beta(a)` and scale map `K(a)` such that the required weak-coupling asymptotic and all RG/gap/source/OS estimates are uniform along that moving trajectory.

The cheapest hostile test must reject any candidate whose bare coupling remains in one fixed compact set, or which silently replaces the Wilson bare parameter by a renormalized coordinate without a proved map between them.

Root remains `OPEN_NO_SOLUTION_CERTIFICATE`.
