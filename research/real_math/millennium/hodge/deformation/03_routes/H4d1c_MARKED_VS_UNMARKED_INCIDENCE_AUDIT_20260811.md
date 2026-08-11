# H4d1c — marked witness versus class-constrained unmarked incidence

**Date:** 2026-08-11  
**Atom:** `H4d1c`  
**Authority:** `PROPOSAL_SHADOW_ROUTE_REPRESENTATION / NO_HODGE_THEOREM / ROOT_AUTHORITY_NONE`  
**Frozen fibre:** `sha256:b3cd5b334cfe24a8cd95081b4828802b362e3e11d9505b09bd11c0b15de080c7`

## Question

H4d1b normalized a complete first-order obstruction target to the condition that the projection from the **chosen marked witness** have surjective differential onto the fixed Hodge-branch tangent. This cycle asks whether that marked condition is actually required by the rational Hodge root, or is only one sufficient representation of local algebraicity.

## Adversarial separation lemma

For a morphism `pi:W -> T`, equality of the image germ with `T` does not imply surjectivity of `d pi_w0` at a specified point `w0`.

The cheapest counterexample is `pi:A^1_C -> A^1_C`, `x |-> x^2`. Its image is all of `A^1_C`, but `d pi_0=0`. A second counterexample separates witness identity: take a disjoint union of a rigid point over `0` and another component dominating `T`. Nearby fibres have witnesses even though the chosen point does not move.

Therefore these are distinct interfaces:

1. `MARKED_POINTED_DOMINATION`: the specified witness `z0` lies on a branch whose differential (and, at higher order, formal map) dominates the Hodge branch.
2. `CLASS_CONSTRAINED_UNMARKED_DOMINATION`: for each nearby point of the Hodge branch there exists *some* algebraic witness in a coefficient-safe incidence object whose class is exactly the transported rational class.

The second condition can be enough for the root's local algebraicity arrow. It does **not** prove that `z0` deforms.

## Primary-source controls

### Kloosterman: complete intersections in projective hypersurfaces

Kloosterman, *Variational Hodge conjecture for complete intersections on hypersurfaces in projective space*, arXiv:2104.14845v2.

Proposition 3.2 computes the dimension of the **image** `L=Im(pi)` of the flag-Hilbert projection. Its proof studies the tangent space to the fibre at `(Y,Z)`, bounds it by `H^0(N_{Z/Y})`, and constructs the expected-dimensional family in the fibre. Theorem 4.14 then identifies the relevant irreducible Hodge-locus component with the locus of hypersurfaces containing a complete intersection of the fixed multidegree and proves the Hodge locus smooth at `Y`.

Source: https://arxiv.org/pdf/2104.14845

What may be transferred safely: a special-family **unpointed geometric image/class-existence mechanism**. What is not transferred merely from Theorem 4.14's statement: a general theorem that the originally marked `Z` has surjective projection differential in every smooth-projective family. A marked transfer needs the pointwise flag-Hilbert smoothness/rank argument stated and checked separately.

### Bruzzo–Montoya: toric deformation of pairs

The version of record, Bruzzo–Montoya, *Deformation of pairs and Noether–Lefschetz loci in toric varieties*, European Journal of Mathematics 9 (2023), article 108, Theorem 5.4, proves under Macaulay-type and degree hypotheses that the class deforms algebraically iff it remains of Hodge type, and identifies the local Noether–Lefschetz locus with an irreducible component of the projection of a suitable flag Hilbert scheme.

Source: https://link.springer.com/article/10.1007/s40879-023-00702-4  
ArXiv provenance: https://arxiv.org/abs/2203.00664

This is again a source-bound positive control for class-existence/incidence geometry, not a general marked-witness theorem.

## Expert-cell synthesis

- **VHS/Hodge-locus geometer:** accepted the split. The base-side target is the exact branch for the transported rational class, not the whole geometric image locus when several Hodge classes/components meet.
- **Flag-Hilbert/cycle-moduli geometer:** required separate typing of a marked point and an unmarked projected component; image dimension alone cannot certify the marked differential.
- **Deformation-obstruction specialist:** H4d1b remains correct for the marked representation. Its equivalence does not show that the marked representation is necessary for class algebraicity.
- **Adversarial verifier:** `x^2` and the disjoint-component example falsify the forbidden marked<-unmarked implication. Higher-order/nonreduced regressions remain open.

These are same-context analytical passes, not independent mathematical review.

## Outcome

`PARTIAL_SUCCESS / REPRESENTATION_SPLIT_AND_ROUTE_REOPENING`.

The marked H4d1c target is retained as a sufficient route but is no longer the only local propagation representation. A parallel unmarked route is admissible **only** when the incidence object is constrained to realize the same transported rational class. For a general finite signed rational witness this requires explicit coefficient/category bookkeeping; “same Hilbert polynomial”, “same multidegree”, or “some algebraic cycle exists” is not by itself enough.

This is a representation/compositional research result, not a Hodge theorem.

## Residuals and gluing boundary

Open two children rather than silently conflating them:

- `H4d1c-M`: source-specific `MARKED_POINTED_DOMINATION` for the chosen witness.
- `H4d1c-U`: construct a `CLASS_CONSTRAINED_UNMARKED_INCIDENCE` for the exact rational class and prove its image contains the relevant Hodge-branch germ.

Either child, if successful, still needs a separately frozen higher-Artin/formal test where relevant, algebraization if the output is only formal, coefficient preservation, and global/monodromy continuation. Singular degeneration remains separate. No local result is glued to the global Hodge root in this cycle.

## Saturation / novelty

The previously saturated detector/complete-obstruction family stays flattened. `RELATION`, `PATH`, and `OBSTRUCTION` reopen because the propagation DAG now has two typed local edges. No new primitive operator was invented.

RAKL novelty class: `representation` (defensible only for the route normalization); theorem novelty: none.

## Framework-improvement hypothesis

Candidate only: add an incidence-typing guard to `mathematical_context_translation` and `contextual_theory_gluing`: `UNPOINTED_IMAGE`/projected-Hilbert evidence must not close a `MARKED_POINTED_DOMINATION` edge without pointwise rank/smoothness evidence. Conversely, a class-constrained unmarked existence edge should be representable without forcing a chosen witness to deform.
