# H4d1c tangent-codimension squeeze calibration

**Date:** 2026-08-11  
**Atom:** `H4d1c`  
**Authority:** `SOURCE_BOUND_FIRST_ORDER_ROUTE_CALIBRATION / PROPOSAL_SHADOW / NO_HODGE_THEOREM / NO_ROOT_AUTHORITY`

## Exact frozen target

Keep the rational Hodge scope unchanged. Fix the already-algebraic finite signed rational witness `w0`, the branch-bound witness space `pi_alpha: W_alpha -> T`, and the fixed irreducible local Hodge branch `T` through `s0`. H4d1b normalized complete first-order obstruction vanishing to surjectivity of

`d pi_alpha|w0 : T_w0 W_alpha -> T_s0 T`.

H4d1c asks for independent source geometry that proves this surjectivity without assuming liftability or replacing it by detector vanishing.

## Same-context expert cell

1. **VHS/Hodge-locus specialist.** Owns the tangent space `T_s0 T`, Hodge-locus equations, smoothness and branch identification. Rejects any inference from Hodge equations to a cycle-moduli tangent map without an explicit bridge.
2. **Cycle/Hilbert-Chow specialist.** Owns `W_alpha`, the exact signed rational witness bookkeeping, the derivative `d pi_alpha`, vertical witness deformations and incidence equations.
3. **Semiregularity/deformation specialist.** Checks that no complete-obstruction statement is being renamed and that detector-only vanishing is not credited as reachability.
4. **Degeneration/monodromy specialist.** Keeps singular degeneration, specialization, component switching and higher-order monodromy outside this first-order certificate unless separately frozen.
5. **Adversarial special-family specialist.** Uses hypersurface examples to falsify expected-dimension heuristics and transfer by analogy without a DifferenceWitness.
6. **Formal/novelty auditor.** Separates an elementary rank squeeze from source-specific mathematics, same-context review from independent review, and local first-order success from all gluing obligations.

All six roles are same-context analytical lenses, not independent reviewers.

## Operator tried: exact tangent-codimension squeeze

Let `S_amb` denote the ambient local base parameter space containing `T`. Branch binding gives

`im(d pi_alpha|w0) subseteq T_s0 T subseteq T_s0 S_amb`.

Let `c_H = codim(T_s0 T, T_s0 S_amb)` and `c_W = codim(im(d pi_alpha|w0), T_s0 S_amb)`.

Because the witness tangent image is contained in the Hodge tangent,

`c_W >= c_H`.

Therefore any **independent source calculation** establishing the opposite inequality `c_W <= c_H` forces `c_W = c_H`, hence

`im(d pi_alpha|w0) = T_s0 T`.

Equivalently, H4d1c first-order surjectivity is certified by four separately checkable coordinates:

- **C1 branch binding:** the chosen witness family really maps into the same Hodge branch `T` for the same rational class;
- **C2 Hodge tangent:** compute or bound the exact tangent codimension `c_H` for that branch;
- **C3 witness incidence rank:** compute `d pi_alpha` in the exact witness category and prove `c_W <= c_H` independently of the desired liftability;
- **C4 category fidelity:** the moving objects represent the same finite signed rational class, rather than a different integral/effective witness or a cohomological surrogate.

No smoothness of the scheme-theoretic image of `pi_alpha` is needed for this first-order linear-algebra implication. Smoothness becomes relevant only when a source uses local dimensions or reducedness to infer the derivative rank.

This squeeze is not a new theorem; it is a representation-level certificate exposing the exact source-specific inequality that must carry mathematical content.

## Primary-source calibration and falsification

- **Kloosterman, arXiv:2104.14845.** Positive special-family control. The paper proves the variational Hodge conjecture for complete-intersection cycles on hypersurfaces and uses flag-Hilbert/Hodge-locus geometry. This supports the method family `incidence geometry + tangent comparison`, but only in the stated hypersurface/complete-intersection setting.
- **Nishinou, arXiv:2009.01651.** Positive semiregular codimension-one control. Relative deformation is tied to Hodge persistence under the paper's semiregularity hypotheses. It is a solved-category analogue, not a general H4d1c transfer.
- **Kloosterman, arXiv:2312.12363.** Adversarial dimension control. The paper gives counterexamples to a conjecture about dimensions of Hodge loci for linear combinations of linear subvarieties in several cubic/quartic hypersurface regimes. Consequently, expected-dimension formulas inferred from special cycle combinatorics are not acceptable substitutes for C2/C3; the actual tangent/rank calculation must be source-bound.
- **Liu--Shen, arXiv:2602.13951 (2026-02-15).** Current base-side control. The paper gives intrinsic Hodge-locus descriptions and a Beltrami-differential criterion for the variational Hodge conjecture. For H4d1c it can inform C2, but without a same-theory map from those equations to `d pi_alpha(T_w0 W_alpha)` it does not supply C3.
- **Movasati, arXiv:1902.00831.** Hostile calibration only. The paper studies rigid selected-cycle configurations with finite-order Hodge-locus computations and conjectural underlying cycles in some cases. Computation may falsify a proposed dimension/rank formula but is not proof of C3 or witness existence.

Freshness checked against the current arXiv records during this cycle. No inspected source supplies a general smooth-projective source-independent C3 inequality in the exact rational signed witness category.

## Counterexample-first discriminator

A proposed source mechanism is rejected before theorem invention if any of the following occurs:

1. `c_W <= c_H` is obtained by assuming `d pi_alpha` is onto, first-order liftability, or an equivalent complete-obstruction vanishing statement;
2. only a Hodge/semiregularity detector vanishes, with no derivative-rank conclusion;
3. an expected dimension is substituted for an actual tangent-space/rank computation at a singular or nonreduced point;
4. the witness family changes coefficient/category (effective/integral versus finite signed rational) without an explicit equivalence witness;
5. a hypersurface/complete-intersection formula is transferred to an arbitrary smooth-projective family without a DifferenceWitness covering the deformation complex, incidence equations and Hodge tangent calculation.

## Episode -> diagnosis -> reusable obstruction/lesson

**Episode result:** the codimension-squeeze operator succeeds as a first-order *certificate normal form* but does not solve H4d1c generally.

**Diagnosis:** after H4d1b removed obstruction-language renaming, the remaining first-order mathematical content is exactly a source-specific lower bound on witness-incidence derivative rank matching the independently computed Hodge tangent dimension. Base-side Hodge equations and expected dimensions do not supply that lower bound.

**Reusable obstruction:** `H4d1c1-EXACT-WITNESS-INCIDENCE-RANK-BOUND`: produce, in a nontrivial source family and exact rational witness category, an independently proved rank/codimension bound C3 strong enough to meet C2. Keep this distinct from local-to-global obligations.

**Candidate lesson:** when a geometric lifting route has already been normalized to tangent surjectivity, search for a two-sided rank/codimension squeeze with independently sourced bounds; reject expected dimension and detector vanishing as substitutes. This remains proposal/shadow until protected validation.

## Local versus gluing status

**Local mathematical residual:** C3 is open in general; C2 may itself be difficult or singular. The certificate does not prove a moving witness exists for arbitrary Hodge classes.

**Local-to-global/gluing residuals, separately OPEN:** higher Artin order; formal compatibility; algebraization of formal/analytic lifts; preservation of rational signed coefficients/category; branch/component switching; monodromy; singular degeneration and specialization; global continuation; and the root's initial algebraicity obligation.

## Saturation audit

Seven axes in this Hodge lane are tracked as `DETECTOR_FAITHFULNESS`, `BRANCH_REACHABILITY`, `WITNESS_LIFTING`, `ALGEBRAIZATION`, `COEFFICIENT_CATEGORY`, `MONODROMY_DEGENERATION`, `LOCAL_TO_GLOBAL_GLUING`.

- `DETECTOR_FAITHFULNESS`: flattened by H4d1a for the same-detector nonzero-envelope idea.
- `BRANCH_REACHABILITY`: **reopened/refined** as exact derivative-rank C3 rather than obstruction-language vanishing.
- `WITNESS_LIFTING`: open beyond first order.
- `ALGEBRAIZATION`: open.
- `COEFFICIENT_CATEGORY`: open.
- `MONODROMY_DEGENERATION`: open.
- `LOCAL_TO_GLOBAL_GLUING`: open.

## Verdict

`PARTIAL_SUCCESS / REPRESENTATION_AND_PATH_REFINEMENT`.

The cycle does not close H4d1c. It replaces a broad search for “geometry forcing surjectivity” by a falsifiable four-coordinate certificate whose only non-tautological local burden is an exact source-specific incidence-rank bound. The next cycle should attack `H4d1c1` in a source family where both Hodge tangent equations and cycle-incidence linearization are explicitly available, with Kloosterman 2023 used as an adversarial check against expected-dimension shortcuts.
