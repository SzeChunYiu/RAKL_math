# YM-S1a2h R19 — Wilson stable-manifold contraction/type audit

Authority: **PROPOSAL/SHADOW ONLY**. This packet records a primary-source-scoped incompatibility among displayed hypotheses and the resulting repair obligation. It is not a Yang–Mills counterexample, not a proof that no correct stable-manifold construction exists, not independent peer review, and not a root certificate.

## Exact atom

- Root: issue #5, `OPEN_NO_SOLUTION_CERTIFICATE`.
- Atom: `YM-S1a2h`.
- Issue: #301.
- Signature: `YM-S1a2h-WILSON-FULL-RG-CONTRACTION-VS-RELEVANT-SPECTRAL-SPLITTING-STABLE-GRAPH-CLOSURE`.
- Frozen pre-candidate fibre: `10_case_study/YM-S1a2h_PRE_CANDIDATE_FIBRE_MEMORY_20260812_R19.json`.
- Parent: #295 / draft PR #297.
- Residual entering R19: the relevant/marginal stable splitting and regulator-matched `Delta lambda` slaving used by the Wilson-2026 UVR3/UVR4 route were not source-bound.

## Framework boundary

Current RAKL main was read first at `9d61749c087994654515b2d087758f0ce0efaeb4`, method `3.0.0`, package `0.1.0`, constitution epoch `v3-authority-hardening-20260811`. Current `v3.py` and `method_specs.py` content identities remained `280bf143fc8910d5860aaa02fbe3817a6aacfb72` and `6342f2692b3fd85de3f274f9c6548c9736225691`. The current mathematical workflow requires context, dual-memory, obstruction-transformation review, and public trace before mathematical candidate generation. The connector runtime did not expose a canonical content-bound obstruction-transformation snapshot for this atom, so strict shortcut routing is `CANNOT_CHECK`; the post-freeze action is source acquisition plus falsification only, not proof invention.

## Primary source and verification boundary

Primary source inspected through author-uploaded indexed full text:

Jonathan J. Wilson, *Rigorous Construction of Four-Dimensional Yang–Mills Quantum Field Theory Via Gribov–Zwanziger Quantization and Renormalization Group Analysis: Measure-Theoretic Foundations, Spectral Properties, and the Mass Gap* (2026), including Sections 30.5–30.7 and 38.2–38.3. Relevant public records include SSRN abstract 6419219 and the author-uploaded ResearchGate full-text records DOI `10.13140/RG.2.2.10405.77282` / `10.13140/RG.2.2.22056.43527`.

Direct SSRN PDF retrieval returned HTTP 403 and direct ResearchGate page retrieval returned HTTP 429 during this cycle. No `application/pdf` view reference was obtained, so mandatory page screenshot verification could not be executed. Visual/page-level verification is therefore `CANNOT_CHECK`; the findings below are bounded to parsed indexed primary-author text. No missing formula is reconstructed from memory.

## D1 — displayed full-map contraction is incompatible with the displayed relevant-sector lower bound when the relevant sector is nonempty

Section 30.5 defines the global sequence state from the full pair `(c_k,K_k)` and derives a one-step difference bound

`delta_{k+1} <= LIP_k delta_k`,

with the displayed scalar Lipschitz envelope

`LIP_k := max{ ||Lin_k|| + 2 C_k r, kappa_k + 2 A_k r }`,

where `Lin_k` is the linearized coupling map. It then chooses parameters so `sup_k LIP_k <= L < 1` and concludes that the induced full RG map on the sequence space is a Banach contraction.

Section 30.6 immediately identifies the same linearized coupling maps on relevant/marginal coordinates and gives the displayed spectral classification

`||Lin_k|_rel|| >= lambda_rel > 1`,

with the irrelevant restriction bounded by a number below one. Section 30.7/Theorem 30.6 then simultaneously invokes both ingredients: it assumes the Section-30.5 full-map Lipschitz constants satisfy `sup_k LIP_k < 1`, states a codimension-`|A_rel|` stable manifold, and begins the proof by applying the same full induced map to the sequence space before separately “eliminating expanding directions (tuning).”

Under those displayed definitions, if the relevant sector is nonempty, the two quantitative hypotheses cannot hold simultaneously. Indeed,

`||Lin_k|| >= ||Lin_k|_rel|| >= lambda_rel > 1`,

and therefore, since the remaining Lipschitz-envelope terms are nonnegative,

`LIP_k >= ||Lin_k|| + 2 C_k r > 1`.

Hence `sup_k LIP_k < 1` is impossible for the same full forward map/norm while an included relevant block has the displayed norm lower bound `>1`.

This is stronger than the R18 “bounded is not contractive” hostile control: it is an internal incompatibility between the source's own displayed contraction envelope and its own displayed relevant-sector estimate, conditional only on a nonempty relevant sector in the theorem that subsequently tunes expanding directions.

### Cheap falsifier / repair certificate

This finding is withdrawn if primary detail shows that one of the apparently identical objects is actually different — for example:

1. the Section-30.5 contraction is a projected/reduced map with the relevant coordinates already solved out;
2. the sequence-space norm is on a graph/backward coordinate and `Lin_k` there is an inverse relevant block with norm `<1`;
3. the `LIP_k` entering the contraction omits the expanding relevant block after an explicitly defined projection; or
4. `A_rel` is empty in the exact theorem application and the later “expanding directions” language refers to a different coordinate system whose map is explicitly typed.

No such disambiguating definition was exposed in the bounded primary-source text acquired in this cycle.

## D2 — the displayed graph-transform proof does not yet repair D1

The source's Theorem 30.6 proof labels Step 1 “global contraction for the irrelevant coordinates,” but the displayed sequence norm and map still contain `(c,K)`, and the proof says the induced `R:X->X` is a strict contraction from the same `sup_k LIP_k<L<1` hypothesis. It then says that for each finite-dimensional relevant/marginal initial datum there is a unique full trajectory in the ball, before Step 2 separately eliminates expanding directions using projections `Pi_rel` and `Pi_irr`.

A legitimate stable-manifold proof can absolutely coexist with expanding relevant directions, but its contraction normally lives on a graph/Lyapunov–Perron space or uses inverse/backward evolution on the unstable/relevant block. The acquired source text did not expose an inverse relevant map, a lower conorm/invertibility estimate, a nonautonomous dichotomy estimate, or a graph-transform contraction constant that replaces the incompatible full-forward contraction hypothesis.

Therefore the correct status is not “stable manifold impossible”; it is `TYPED_HYPERBOLIC_GRAPH_TRANSFORM_UNBOUND_IN_ACQUIRED_PRIMARY_TEXT`.

## D3 — Section 38 reuses the same missing coordinate and adds a regulator-universality obligation

Section 38.5 again defines a graph space `g -> (lambda,K)`, asserts invariance of `||lambda_k|| <= c_lambda g_k^2`, and says the graph transform contracts because the finite-dimensional noncontracting directions are controlled by tuning while the remaining dependence enters through the irrelevant factor `rho<1`.

But the displayed `lambda` estimate uses only an operator bound on `A_k`; choosing `c_lambda` larger does not by itself turn an expanding/neutral linear relevant block into a contraction. R18 already isolated this issue. The new Section-30 finding shows exactly what a repair must type: the `lambda` coordinate must be solved/tuned through a backward/inverse or graph equation whose own contraction constants are explicit, not treated as part of the full forward contraction.

For regulator universality, Section 38.11 further states that the remaining `lambda` coordinates are “slaved” to `(g,K)` after proving decay for the latter. Even if each regulator has its own stable graph, universality still needs a regulator-matched estimate such as

`||h_R(g,K)-h_R'(g',K')|| <= L_g |g-g'| + L_K ||K-K'|| + eta(R,R')`,

with `eta -> 0` in the claimed regulator matching limit and constants uniform in the volume/lattice-spacing/RG range. No such acquired primary estimate closed this cycle.

## Expert-cell synthesis

1. **Rigorous lattice-gauge RG:** the full one-step envelope and the relevant-sector lower bound must be typed on distinct domains if both are to be true; the current displayed notation does not do that.
2. **Nonautonomous invariant-manifold theory:** relevant expansion is compatible with a stable manifold only after an explicit dichotomy/inverse/backward graph transform. A full forward contraction on the same coordinates is the wrong object.
3. **Banach-space functional analysis:** on the source's displayed norm, the full operator norm dominates the norm of every restriction; thus the inequality `||Lin_k|_rel||>1` forces the Section-30.5 envelope above one.
4. **Gauge/GZ representation:** any projection/elimination repair must preserve all GZ-compatible relevant/marginal counterterm coordinates and may not silently change the gauge-fixed theory.
5. **OS/continuum gluing:** even a repaired UV stable manifold would not supply reflection positivity, OS quotient/source identification, continuum nontriviality or a physical mass gap; those remain separate root dependencies.
6. **Adversarial mathematical physics:** a two-block linear control `R(x_rel,x_irr)=(2x_rel, x_irr/2)` makes the issue transparent: the irrelevant block contracts and a codimension-one stable manifold exists, but the full forward map is not a contraction. A correct proof must restrict/solve the expanding coordinate before invoking Banach contraction.
7. **RAKL v3 provenance/metrology:** all seven roles share the same evidence and earn `0/3` isolated review credit. Episode, diagnosis, failure and obstruction remain separate; no protected learning is promoted.

## Episode -> diagnosis -> failure/obstruction boundary

- Episode: `EP-YM-S1a2h-R19-20260812`.
- Diagnosis: `DG-YM-S1a2h-R19-FULL-CONTRACTION-HYPERBOLIC-TYPE-COLLISION-SHADOW`.
- Scoped source/proof failure: `FS-YM-S1a2h-FULL-FORWARD-CONTRACTION-VS-REL-LOWER-BOUND-R19-SHADOW`.
- Scoped source/gluing failure: `FS-YM-S1a2h-REGULATOR-STABLE-GRAPH-LIPSCHITZ-UNBOUND-R19-SHADOW`.
- Shadow obstruction: `O-YM-S1a2h-TYPED-HYPERBOLIC-GRAPH-TRANSFORM-AND-REGULATOR-SLAVING-R19-SHADOW`.
- Protected lesson: none.
- Research tool: none.
- Motif: none.

The first failure is a local displayed-hypothesis incompatibility. The second is a same-theory regulator-gluing insufficiency. Neither is a source-wide impossibility theorem.

## Outcome / residual

Outcome: `PARTIAL_SUCCESS_NEW_INTERNAL_STABLE_MANIFOLD_TYPE_INCOMPATIBILITY_AND_SHARPER_REPAIR_CONTRACT`.

Residual before:
`RES-YM-S1a2g-RELEVANT-STABLE-SPLITTING-AND-DELTA-LAMBDA-UNBOUND`.

Residual after:
`RES-YM-S1a2h-PROJECTED_OR_BACKWARD_RELEVANT-GRAPH-CONTRACTION-PLUS-REGULATOR-MATCHED-LAMBDA-SLAVING-AND-SAME-OS-SPECTRAL-TRANSPORT-UNBOUND`.

## Saturation / novelty boundary

Retained proposal/shadow semantic novelty is source-scoped only: one new exact relation/incompatibility, one sharpened obstruction coordinate, and one narrowed path. The underlying linear-algebra control is `RAKL_TRIVIAL`; no new mathematics is claimed. Protected novelty remains zero on all seven axes. Raw repository growth receives zero learning credit.

## Root boundary

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`. This cycle does not attempt formal proof verification, dependency/axiom closure, isolated recheck, bounded root novelty search or independent mathematical reviews. Even a successful repair of this atom would still leave gauge-invariant continuum existence/nontriviality, OS/reflection-positive same-theory reconstruction, regulator/volume/lattice-spacing limits, physical spectral normalization and the remaining root DAG open.
