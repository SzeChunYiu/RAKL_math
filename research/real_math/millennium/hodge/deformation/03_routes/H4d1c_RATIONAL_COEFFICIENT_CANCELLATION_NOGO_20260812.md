# H4d1c-a rational-coefficient cancellation transfer audit

**Date:** 2026-08-12  
**Atom:** `H4d1c-a`  
**Parent:** `H4d1c-INDEPENDENT-HODGE-TO-WITNESS-TANGENT-SURJECTIVITY-MECHANISM`  
**Authority:** `SCOPED_INTERFACE_NOGO / PROPOSAL_SHADOW / NO_HODGE_THEOREM / NO_ROOT_AUTHORITY`

## Exact question

For the frozen smooth-projective/rational setup, write the chosen central witness as `z0 = sum_i q_i [Z_i]`, with fixed rational coefficients. H4d1c asks for independently checkable geometry forcing the coefficient-preserving witness projection to be first-order surjective onto the fixed Hodge branch. This subatom adversarially tests a natural transfer: apply a positive variational-Hodge/liftability mechanism separately to each selected component after using tangency of the **total** class `alpha`.

## Scoped no-go

Let `V` be the relevant first-order base tangent space. For each selected component let `h_i: V -> Q` denote its linearized Hodge-variation map after embedding the relevant Hodge-obstruction summands in a common vector space `Q`. Linearity of cohomology gives `h_alpha = sum_i q_i h_i` for `alpha = sum_i q_i [Z_i]`.

Total-class Hodge tangency gives only `v in ker(h_alpha) = ker(sum_i q_i h_i)`. A componentwise liftability theorem whose hypothesis is persistence of every component class would instead require `v in intersection_i ker(h_i)`. Always `intersection_i ker(h_i) subseteq ker(sum_i q_i h_i)`, but equality is not formal. The frozen countermodel is one-dimensional over `Q`: `h_1(v)=v`, `h_2(v)=-v`, `q_1=q_2=1`. At `v=1`, `h_alpha(v)=0` while both component conditions are nonzero.

Therefore the implication `total rational class is Hodge to first order => each selected component class is Hodge to first order` is invalid without an additional **joint no-cancellation condition**. Consequently a route that merely decomposes the rational signed witness and invokes positive componentwise deformation theorems cannot certify H4d1c from the total Hodge-branch condition alone.

This is an interface-level logical no-go. It does **not** assert that every abstract countermodel is realized by an actual smooth-projective variation, nor that a coupled geometric witness mechanism cannot exist.

## Repair envelope

A valid repair must add source-specific information that removes the kernel enlargement: a coupled witness object whose theorem is stated for the total class; an independently proved direct-sum/graded separation giving `ker(sum_i q_i h_i)=intersection_i ker(h_i)` on the active branch; or geometry proving actual simultaneous witness reachability directly. Codimension one is a positive disanalogy: after clearing denominators, divisor data can be packaged through Picard/line-bundle geometry, so one need not infer persistence of each chosen divisor component separately.

## Primary-source controls

- Cattani–Deligne–Kaplan, *On the Locus of Hodge Classes*, https://arxiv.org/abs/alg-geom/9402009 — Hodge-locus control is a base/cohomological condition, not a witness-lifting theorem.
- Nishinou, *Deformation of pairs and semiregularity*, https://arxiv.org/abs/2009.01651 — a positive source-bound theorem where semiregularity turns Hodge persistence for the relevant cycle into relative deformation.
- Kloosterman, *Variational Hodge conjecture for complete intersections on hypersurfaces in projective space*, https://arxiv.org/abs/2104.14845 — Theorem 1.1 uses explicit flag-Hilbert and Hodge-locus tangent/dimension geometry for one special cycle family; it is not a general componentwise transfer principle.
- Bloch–Esnault–Kerz, *Deformation of algebraic cycle classes in characteristic zero*, https://arxiv.org/abs/1310.1773 — formal rational cycle-class deformation is a distinct layer and does not remove this first-order component-cancellation issue.

The literature is used only as scope control. The no-go itself is the elementary linear countermodel above.

## Same-context expert cell

**VHS/Hodge specialist:** confirms linearity and the cancellation boundary; blocks componentwise inference without a splitting witness. **Algebraic-cycle/witness-moduli specialist:** confirms that coefficient-preserving multi-component bookkeeping requires simultaneous deformation over one base direction and does not itself supply the missing implication. **Deformation/obstruction specialist:** reuses H4d1b's complete-obstruction versus detector-only diagnosis; another one-sided detector is not a repair. **Adversarial verifier/foundations specialist:** executed the precommitted exact-rational countermodel and checked that it refutes only the logical transfer, not geometric realizability. These are same-context analytical passes and count as zero independent mathematical reviews.

## Local versus gluing diagnosis

This is a **local mathematical/representation-transfer failure**, at first order and before gluing. No local-to-global result was attempted. Higher Artin compatibility, algebraization, singular degeneration, monodromy/component switching, and global branch domination remain separately open.

## Outcome and residual

`PARTIAL_SUCCESS / COEFFICIENT_BOUNDARY_ROUTE_PRUNING`.

Componentwise positive analogues may only be reused after a joint no-cancellation or coupled-witness condition is proved. The next high-information atom is to test whether a selected special family supplies a **coupled** tangent-surjectivity mechanism for the total denominator-cleared cycle rather than separate component mechanisms.

Root rational Hodge Conjecture status remains `OPEN`.
