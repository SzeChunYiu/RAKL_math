# H4d1b first-order obstruction/liftability representation audit

**Date:** 2026-08-11  
**Atom:** `H4d1b`  
**Authority:** `SOURCE_BOUND_FORMAL_ROUTE_NORMALIZATION / NO_HODGE_THEOREM / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`

## Frozen question

The parent H4d1 calibration fixes a smooth projective complex family `f:X→S`, a flat rational class `α`, an already algebraic finite signed rational witness `z0`, and one irreducible local Hodge-locus branch `T` through `s0`. The witness interface is branch-bound as `π_α:W_α→T`. After H4d1a's same-detector no-go, H4d1b proposed proving directly that the first-order branch obstruction vanishes on `T` without assuming the desired lift or full semiregularity.

The pre-action receipt froze the following adversarial discriminator before this audit: test whether direct first-order vanishing is actually equivalent to first-order witness reachability/tangent surjectivity, and reject any claim that silently swaps a complete obstruction theory for a mere detector.

## Scoped formal lemma

Let `w0∈W_α` lie over `s0∈T`, and let `δ_{1,T}: T_{s0}T → Ob_1` be the first-order obstruction assignment for lifting the chosen witness over the first-order base deformation represented by `v∈T_{s0}T`.

Assume first that this is a **complete first-order obstruction theory** for the registered lifting problem: `δ_{1,T}(v)=0` if and only if the corresponding first-order lift of `w0` exists. A first-order lift is precisely a tangent vector `\tilde v∈T_{w0}W_α` mapping to `v`. Therefore

`ker(δ_{1,T}) = im(dπ_α|_{w0})`.

Consequently,

`δ_{1,T}|_{T_{s0}T}=0  ⇔  dπ_α|_{w0}:T_{w0}W_α→T_{s0}T is surjective`.

Because `π_α` is already branch-bound to `T`, the reverse containment is built into the interface. Thus the H4d1b condition is exactly first-order witness reachability along the chosen Hodge branch, expressed in the obstruction representation.

This is not a new theorem in deformation theory. It is the exact meaning of a complete obstruction assignment plus the definition of the tangent map.

## Detector-only fork

If `δ_{1,T}` is only a **non-complete detector**—its vanishing is necessary but not sufficient for a lift—then only `im(dπ_α|_{w0}) ⊆ ker(δ_{1,T})` is justified. In that fork, proving `δ_{1,T}|_T=0` does **not** close the witness-lifting arrow.

Hence H4d1b has a two-way normalization: complete obstruction map → direct vanishing restates tangent surjectivity; detector-only map → direct vanishing is insufficient for witness lifting. Either way, a useful successor must add an independently checkable geometric mechanism that proves actual first-order reachability/surjectivity, rather than crediting the vanishing statement itself as a reduction.

## Primary-source controls

The Stacks Project's definition of an obstruction theory requires the obstruction element to vanish exactly when a lift exists for the deformation situation. This is the completeness fork used above; no stronger property is imported.

Nishinou's *Deformation of pairs and semiregularity* is a positive conditional control: for the paper's semiregular codimension-one map setting, relative deformation occurs if and only if the cycle class remains Hodge. The source therefore supplies an actual liftability theorem in its category, not merely an untyped detector-vanishing slogan.

Kloosterman's *Variational Hodge conjecture for complete intersections on hypersurfaces in projective space* is the strongest selected special-family control for the normalized target. Theorem 1.1 states that the Hodge locus is smooth at the hypersurface and is contained in the locus of hypersurfaces containing a complete intersection of the fixed multidegree. The proof explicitly uses a flag Hilbert scheme, computes the dimension of its image, and compares it with the tangent space of the Hodge locus. This is exactly the kind of independent geometry H4d1c must seek; it is not a general smooth-projective theorem.

Source anchors:
- https://stacks.math.columbia.edu/tag/07YG
- https://arxiv.org/abs/2009.01651
- https://arxiv.org/abs/2104.14845

## Expert-cell post-discriminator synthesis

- **VHS/Hodge-locus:** accept only the branch-bound statement; tangent equality says nothing about nilpotent/higher-order Hodge-locus structure.
- **Cycle/witness-moduli:** for the chosen rational witness, `W_α` remains local coefficient-preserving bookkeeping; surjectivity concerns that exact category, not all rational cycles.
- **Semiregularity/derived obstruction:** accept the complete-vs-detector fork; a different obstruction object is a fresh representation, not a repair by terminology.
- **Degeneration/monodromy:** no progress is credited on singular degeneration, specialization, monodromy, algebraization or global continuation.
- **Adversarial formal methods:** the cheapest counterexample to overclaiming is a non-complete detector; the cheapest counterexample to globalizing tangent surjectivity is singular/nonreduced higher-order structure.
- **Novelty/metrology:** classify the solved subproblem as `RAKL_TRIVIAL`, structural rank `0`; retained value is route normalization and an experience pattern, not theorem novelty.

These passes are same-context analytical review only.

## Verdict

`PARTIAL_SUCCESS / REPRESENTATION_EQUIVALENCE_ROUTE_PRUNING`.

H4d1b does not supply an independent first-order route. Its direct-vanishing target either restates first-order witness liftability (complete obstruction theory) or is too weak to imply liftability (detector-only theory).

This materially narrows the deformation program without changing the status of the rational Hodge conjecture.

## Residual opened: H4d1c

Open `H4d1c-INDEPENDENT-HODGE-TO-WITNESS-TANGENT-SURJECTIVITY-MECHANISM`.

The next first-order atom must seek a **source-specific, independently checkable geometric condition** that forces `dπ_α(T_{w0}W_α) = T_{s0}T` for the exact chosen witness branch without assuming first-order liftability. Priority controls are Kloosterman-style flag-Hilbert dimension/smoothness versus Hodge-tangent codimension calculations; Lefschetz/correspondence structures that produce actual moving witnesses with exact coefficient/category checks; normal-function or infinitesimal-invariant arguments only if they output witness reachability rather than another detector; and degeneration/specialization only under a separately frozen singular/monodromy interface.

Any first-order success still opens a fresh higher-Artin-order child. Formal lifting, algebraization, coefficient preservation, monodromy/global continuation and root initial algebraicity remain separate obligations.

## Framework-improvement hypothesis

Candidate only: mathematical route representations should type an obstruction surface as `COMPLETE_OBSTRUCTION` (zero iff lift) versus `DETECTOR_ONLY` (vanishing only necessary, or otherwise one-sided). Before granting route-reduction credit to “prove the obstruction vanishes,” a generic normalization check should ask whether the statement is already equivalent to the target liftability by completeness. This episode is one application case and does not authorize a framework change or ResearchTool.
