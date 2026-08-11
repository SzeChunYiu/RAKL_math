# YM-S1c1 — bare-coupling escape audit of arXiv:2606.19362v1

**Root:** RAKL_math issue #5  
**Control issue:** #69  
**Framework authority inspected first:** `SzeChunYiu/RAKL@decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8`  
**Application base:** `SzeChunYiu/RAKL_math@5d6bdc6f566921f51a375fdc2e8035123cf4830c`  
**Chronology:** retrospective source audit; the discriminator was observed before this packet was frozen.  
**Authority:** `SOURCE_BOUND_RETROSPECTIVE_ROUTE_DIAGNOSTIC / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`

## Exact question

Does the weak-coupling entry argument in Faizal–Shabir, arXiv:2606.19362v1, actually produce the Wilson bare-coupling escape required by the paper's own continuum/asymptotic-freedom claim, or does it only tune into a small RG ball near a fixed finite bare coupling?

This audit is deliberately narrower than reviewing the 593-page construction as a whole.

## Root contract binding

The live Yang–Mills root contract requires a nontrivial four-dimensional continuum QFT, physical Hilbert-space identification, a positive Hamiltonian gap in physical units, limit uniformity, and ultraviolet/asymptotic-freedom compatibility. Fixed-cutoff transfer positivity or strong-coupling clustering is explicitly insufficient by itself.

## Fibre actually consulted

- Root contract: `00_problem_contract/ROOT_CONTRACT.md`.
- PR #46: ordinary box-size uniformity for the Shen–Zhu–Zhu strong-coupling cylinder family is not the active G3 bottleneck; changing source-family/support control remains open.
- PR #62: the abstract dense-source/common-rate implication closes only a fixed-cutoff logical sub-bridge; target binding, RG transport, physical scaling and continuum identification remain open.
- Primary sources: Lüscher 1977; Osterwalder–Seiler 1978; Shen–Zhu–Zhu 2022/2023; Faizal–Shabir arXiv:2606.19362v1.
- RAKL v3: immutable TaskEpisode semantics, problem-fibre/gluing interfaces and vector saturation.

Selected operations: `PRIMARY_SOURCE_COLLISION_AUDIT`, `ROOT_BRIDGE_STABILITY_AUDIT`, `CONTRASTIVE_DISCRIMINATION`, `GLUING_INTERFACE_AUDIT`.

Rejected low-information actions: another generic finite-volume-uniformity pass; another fixed-cutoff spectral lemma; numerical glueball calibration.

## Source-internal discriminator

The source uses `beta` as the inverse Wilson bare coupling and treats small `beta` as strong coupling. In its weak-coupling section it states that the desired continuum trajectory has `beta(a) -> infinity`.

Theorem 5.4 instead fixes a compact interval `I`, chooses a fixed reference `beta_* in int(I)`, and derives

`delta_K = (2 C0 / c0) rho^K`, with `0 < rho < 1`,

followed by

`beta_K in (beta_* - delta_K, beta_* + delta_K)`.

Hence, under the theorem's stated fixed-reference construction,

`|beta_K - beta_*| <= delta_K -> 0`,

so

`beta_K -> beta_* < infinity`.

The appendix repeats the same structure: fix `beta_*` in a compact interval where the FRD expansion is valid and choose `beta_K` near it.

This is incompatible with using that theorem *by itself* to establish the separately asserted Wilson bare-coupling escape `beta(a) -> infinity`.

## Scope of the result

Verdict:

`TRANSFER_BLOCKED_SCOPED / BARE_COUPLING_ESCAPE_NOT_ESTABLISHED_BY_THEOREM_5_4`

This does **not** show that no asymptotically-free trajectory exists. It does **not** refute the fixed-cutoff strong-coupling gap theorem. It does **not** invalidate classical transfer-matrix positivity. It does **not** prove the full paper wrong.

It says only that the source's displayed Theorem 5.4 argument, with a fixed `beta_*` and shrinking `delta_K`, does not establish the bare-coupling asymptotic that the later continuum identification requires.

A repair would need, for example, a separately proved moving reference `beta_*(K)` or moving interval `I_K` with `beta_*(K)->infinity`, together with estimates uniform on that moving domain and compatibility with the gap/clustering/OS interlacing machinery. None of those may be supplied by simply relabeling the decay of an operational renormalized coupling.

## Gluing diagnosis

Local sections retained:

1. fixed-cutoff OS/transfer positivity;
2. strong-coupling exponential clustering / fixed-cutoff gap mechanisms;
3. abstract dense-source spectral visibility lemma.

Missing interface:

`strong-coupling/fixed-beta RG control -> Wilson bare trajectory beta(a)->infinity -> scale-uniform physical gap -> continuum OS Hamiltonian`.

The local pieces therefore do not currently glue into the root certificate.

## Six-role same-context expert cell

1. **Constructive lattice gauge/RG analyst — ACCEPT scoped obstruction.** The source itself separates small-`beta` strong coupling from the claimed `beta(a)->infinity` weak-coupling trajectory.
2. **Rigorous RG/dynamical-systems analyst — ACCEPT.** A point constrained to an `O(rho^K)` neighborhood of one fixed finite reference converges to that reference; a moving-domain theorem would be a different hypothesis.
3. **OS/transfer-spectrum analyst — ACCEPT WITH SCOPE.** Fixed-cutoff spectral conclusions remain logically separate and are not downgraded by this audit.
4. **Asymptotic-freedom analyst — ACCEPT.** Decay of a defined renormalized observable at increasing effective scale is not identical to proving the required Wilson bare parameter escapes to weak coupling along `a->0`.
5. **Adversarial source auditor — ACCEPT SOURCE-BOUNDED.** A full-text search found later claims that Theorem 5.4 provides the AF bare trajectory, but no displayed repair of the fixed-reference asymptotic in the audited chain.
6. **RAKL v3 assurance/meta-method analyst — ACCEPT AS RETROSPECTIVE EPISODE ONLY.** The finding predates the frozen packet and cannot receive prospective candidate authority.

These are same-context AI roles, not independent peer review.

## Competing diagnoses

- **D1 (selected only as observed route failure):** Theorem 5.4 proves entry near a fixed finite bare coupling, not the claimed `beta(a)->infinity` trajectory.
- **D2:** The intended reference/compact interval was meant to move with `K` or `a`, but the necessary uniform estimates and asymptotic relation were omitted from the stated proof.
- **D3:** A different convention for the bare parameter is intended in the weak-coupling appendix. This would require an explicit coordinate conversion consistent with the earlier Wilson action and does not follow from the current notation.
- **D4:** Another theorem elsewhere can repair the trajectory. If found, it must be source-bound and audited rather than inferred.

Only the observed inconsistency is recorded; no global impossibility diagnosis is promoted.

## Next prospective atom

`YM-S1c1a — MOVING-BARE-COUPLING-TRAJECTORY`

Before candidate generation, freeze a fresh context-first packet asking:

> Can one construct `a -> beta(a)` with `beta(a)->infinity` and a scale map `K(a)->infinity` such that the exact RG estimates, reflection positivity, source-family control, gap step-scaling and physical-unit lower bound remain uniform along the moving trajectory?

The cheapest hostile test is to reject any proof whose tuning theorem keeps `beta(a)` inside one fixed compact set, or proves only `g_R(mu)->0` at fixed bare `beta` without a source-bound relation to the Wilson bare trajectory.

Root remains `OPEN_NO_SOLUTION_CERTIFICATE`.
