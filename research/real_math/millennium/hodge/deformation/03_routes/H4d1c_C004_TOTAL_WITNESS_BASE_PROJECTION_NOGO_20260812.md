# H4d1c-d total-witness projection-faithfulness audit

**Date:** 2026-08-12  
**Atom:** `H4d1c-d`  
**Parent residual:** `H4d1c-INDEPENDENT-HODGE-TO-WITNESS-TANGENT-SURJECTIVITY-MECHANISM`  
**Authority:** `SCOPED_INTERFACE_NOGO / PROPOSAL_SHADOW / NO_HODGE_THEOREM / NO_ROOT_AUTHORITY`

## Exact question

Current-main H4d1 fixes the root-aligned local interface as a witness/incidence projection `pi_alpha : W_alpha -> T`, where `T` is a Hodge-locus branch in the **base of the varying smooth-projective family**. The first-order H4d1c target is therefore `im(d pi_alpha) = T_s0 T`, not merely largeness of `T_w W_alpha`.

Open proposal/shadow PR #250 (`H4d1c-C003`) gives a useful solved-class DifferenceWitness inside a fixed `P^2`: the total conic parameter space has the tangent `z^2 mod <xy>` that is absent from the product-of-lines factorization. This cycle adversarially tests whether that internal tangent escape, by itself, certifies any additional Hodge-base reachability.

## Scoped linear no-go

Let `j : W_fix -> W_tot` be a local map from a fixed-factor witness representation into a total-witness representation and let `pi_tot : W_tot -> T` be the root-aligned projection to the Hodge branch. Write `pi_fix = pi_tot o j`. At the chosen point set `A = im(dj) subset B = T_w W_tot`, and `p = d pi_tot : B -> H`, where `H = T_s T`.

A strict source-space enlargement `A proper_subset B` does **not** imply a strict target-image enlargement `p(A) proper_subset p(B)`. The cheapest exact countermodel is

- `B = span(e1,e2)`,
- `A = span(e1)`,
- `H = span(v1,v2)`,
- `p(e1)=v1`,
- `p(e2)=0`.

Then `A proper_subset B`, but `p(A)=p(B)=span(v1)`, and the required Hodge direction `v2` is still unreachable. The extra total-witness tangent can be vertical for the projection.

Hence any claimed H4d1c gain from a larger total-witness tangent space needs an additional **nonverticality / image-coverage certificate**. Source tangent dimension or source tangent strict inclusion alone is not congruent for the root-critical quantity `im(d pi_alpha)`.

The exact transfer condition is visible on the quotients. For `A subseteq B`, the inclusion `p(A) subseteq p(B)` is strict exactly when the induced map

`bar p : B/A -> H/p(A)`

is nonzero. Full first-order branch coverage is the separate condition `p(B)=H`, equivalently every required `h in H` has some witness tangent `b in B` with `p(b)=h`. Thus a successor must prove a nonzero quotient image for a strict gain, and surjectivity for full branch coverage; neither follows from `A proper_subset B`.

## Compatibility with the Hodge failure atlas

Current main records `FM-HODGE-REPRESENTATION-EQUIVALENCE-NOT-REDUCTION`: renaming a fixed first-order lifting obligation by an equivalent same-detector condition does not reduce it. This result preserves rather than replaces that warning. The present failure has a distinct scoped form: enlarging a source representation does not establish progress in the target image unless the new quotient direction survives the consumer projection. Representation equivalence is not reduction, and representation enlargement is not target-image gain. Neither statement covers higher-order lifting, other detectors, or the root conjecture.

## Audit of the C003 conic control

The C003 family `C_t = V(xy+t z^2)` varies the conic while the ambient variety is fixed as `P^2`. Against the H4d1 interface, there is no nontrivial ambient Hodge-deformation base in that control; if it is mapped to a base at all, the root-aligned base is a point. Thus the exhibited `z^2` direction is an **internal witness-deformation direction**, not evidence that the image of a witness-incidence projection onto a nontrivial Hodge branch has enlarged.

This does not invalidate C003. It still proves the fixed-component fibre-product no-go is representation-local: a total witness can have deformations absent from a fixed factorization. What is pruned here is the stronger inference `INTERNAL_TANGENT_ESCAPE => HODGE_BRANCH_REACHABILITY_GAIN`.

The C003 path reopening must therefore be typed as `TOTAL_WITNESS_REPRESENTATION_AVAILABLE`; H4d1c branch reachability remains open until an actual base projection is controlled.

## Positive source-family control

Kloosterman's complete-intersection-on-hypersurface setting has the right root-aligned shape. The source uses a flag Hilbert scheme of pairs `(Y,Z)` and projects it to the parameter space of hypersurfaces `Y`; the theorem controls the Hodge locus by a locus reached by such pair deformations in the stated special family. That is qualitatively stronger than enlarging the tangent space of `Z` while keeping `Y` fixed, because it controls the **image in the ambient-deformation base**.

This source is a positive calibration only. It is special-family geometry and does not transfer to arbitrary rational Hodge classes.

Primary scope controls consulted:

- R. Kloosterman, *Variational Hodge conjecture for complete intersections on hypersurfaces in projective space*, arXiv:2104.14845.
- T. Nishinou, *Deformation of pairs and semiregularity*, arXiv:2009.01651.
- H. Movasati, *On a Hodge locus*, arXiv:2211.11405.
- K. Liu and Y. Shen, *Sections of Hodge bundles II: deformation of (p,p)-classes and applications to Kähler geometry*, arXiv:2602.13951.

The linear no-go above is proved directly and does not depend on those papers.

## Expert-cell findings

**Hodge/VHS lead.** The consumer is a base tangent direction on a Hodge branch. Internal witness deformations are relevant only through their projection to that base.

**Hilbert/Chow deformation lead.** A larger total-witness tangent space is a real representation gain, but vertical directions can be killed by `d pi`.

**Flag-incidence lead.** Kloosterman is the correct positive template because the flag object projects to the varying hypersurface base and the source controls the image locus there.

**Obstruction/formal lead.** Even a first-order image-surjectivity result leaves higher Artin lifting, formal compatibility and algebraization separate.

**Coefficient/category lead.** A useful future total-witness incidence must retain the exact signed rational class equation; replacing it by one effective cycle is not licensed.

**Adversarial/RAKL lead.** The two-dimensional linear countermodel falsifies the overstrong transfer at negligible mathematical cost. Same-context role separation earns no independent-review credit.

## Result and residual

**Outcome:** `PARTIAL_SUCCESS / VERIFIED_SCOPED_NONIMPLICATION`.

New scoped obstruction: `O-H4D1C-TOTAL-WITNESS-NONVERTICAL-HODGE-BRANCH-COVERAGE`.

The smallest next atom is to freeze a genuinely varying source-family incidence `pi:W_tot->T` and prove, from source geometry rather than tangent dimension alone, that every required Hodge-branch direction has a nonvertical witness lift. Kloosterman supplies a solved special-family calibration. A general route must separately preserve rational coefficients/category, then face higher Artin order, algebraization, monodromy/component switching, singular degeneration/specialization, global continuation, and the root initial-algebraicity gap.

This cycle records a **local-to-base projection/gluing failure**, not a local failure of the conic tangent computation and not a global-continuation failure.
