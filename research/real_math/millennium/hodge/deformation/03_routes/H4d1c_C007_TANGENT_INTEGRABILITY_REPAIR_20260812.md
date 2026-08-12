# H4d1c C007 — tangent surjectivity needs integrability

**Authority:** scoped proposal/shadow mathematics; no Hodge theorem or root authority.
**Current application base:** `451d9506d365f06eb314323523ba123edd3ffb32`.
**Current RAKL authority/pin:** `5dc0627f039e8f3e1cdcb7e05cd7603860afc554`.

## Merged predecessor and distinct question

C006 is merged and credited as
`MATH-HODGE-C006-RAMIFICATION-POINTWISE-DIFFERENTIAL-NONIMPLICATION`.
It proves that full nonlinear image does **not** force surjectivity of the
differential at an arbitrary selected point: ramification can make the
differential under-report the image.

C007 asks the converse proxy question.  Does a surjective Zariski tangent map
at a selected incidence point force actual image coverage?  The answer is also
no when the source point is singular.

## One scoped mathematical unit

Let

`W = V(y^2-x^3) subset A^2_C = H`

and let `pi:W->H` be the closed immersion.  The cusp is reduced and
irreducible, `H` is smooth and irreducible, and `pi` is proper.  At the origin,
the defining equation has no linear term:

`d(y^2-x^3)_0 = 0`.

Consequently the Zariski tangent space `T_0W` is the full ambient plane, and
the tangent map `d pi_0:T_0W->T_0H` is an isomorphism.  Nevertheless `pi(W)` is
the proper closed cusp rather than all of `H`.

Thus surjective pointwise Zariski tangent rank at a singular source can be a
false positive for image coverage.  Excess tangent directions need not
integrate into actual source motion.

This is exactly one mathematical unit.  The sufficient certificate below is
the repair boundary attached to that unit, not a second credit item.

## Attached sufficient certificate

Let `pi:W->H` be a proper morphism of finite-type complex algebraic varieties,
with `H` irreducible.  If `pi` is smooth at some `w in W`, then `pi(W)=H`.

Indeed, smoothness persists on an open source neighborhood `U` of `w`, and a
smooth morphism is universally open (Stacks Project, tag `056G`).  Hence
`pi(U)` contains a nonempty open subset of `H`.  The image of a proper morphism
is closed (tag `01W6`).  A closed subset of irreducible `H` containing a
nonempty open subset equals `H`.  Tag `01W5` also confirms that the cusp closed
immersion is proper, so properness alone does not remove the local false
positive.

Without properness, local openness need not cover a whole component: the open
immersion `A^1_C -> P^1_C` is a local isomorphism but omits infinity.

## Hodge applicability remains open

The cusp is not an actual Hodge-incidence.  Reusing the certificate in the
rational Hodge program requires a genuine exact-class, coupled signed-rational
witness incidence, a point at which its projection is smooth, proper/closed
image control, and binding to one irreducible Hodge-locus component.  This
packet supplies none of initial algebraicity, source-family completeness,
higher-Artin lifting, algebraization, monodromy, degeneration, or global
continuation.

Root state remains `OPEN_NO_SOLUTION_CERTIFICATE`; same-context review has zero
independent-review authority; Git, CI, schemas, hashes, and chronology have
zero mathematical credit.
