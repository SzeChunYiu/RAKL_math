# H4d1c-g — tangent surjectivity needs an integrability certificate

**Cycle:** `H4d1c-C007-GENERIC-RANK-COVERAGE-AUDIT`  
**Authority:** `PROPOSAL_SHADOW / SCOPED_ROUTE_RESULT / NO_HODGE_THEOREM / NO_ROOT_AUTHORITY`  
**Root scope preserved:** smooth projective complex varieties, rational `(p,p)` classes, rational algebraic cycles.

## Exact consumer question

Let `H` be one reduced irreducible local/algebraic Hodge-locus component for one locally marked rational class, and let

`pi : W -> H`

be a genuine algebraic-witness incidence whose points are intended to represent the exact transported signed rational class. C004 established that source tangent enlargement is not the consumer; C006 (open proposal/shadow) showed that surjectivity of `d pi` at the *selected* witness is not necessary for actual image coverage because ramification can kill the derivative. The present atom asks the converse operational question: **when is a surjective Zariski tangent map sufficient evidence for actual branch coverage?**

## Counterexample-first result: raw tangent surjectivity is not sufficient

Take the reduced irreducible cusp

`W = V(y^2 - x^3) subset A^2_C = H`

and let `pi:W -> H` be the closed immersion. At the origin, the defining equation has no linear term. Hence the Zariski tangent space of the cusp is all of `C^2`, so

`d pi_0 : T_0 W -> T_0 H`

is an isomorphism and in particular is surjective. Nevertheless `pi(W)` is the proper closed cusp, not all of `H`. The map is proper because a closed immersion is proper.

Thus even with:

- reduced irreducible source,
- smooth irreducible target,
- a proper morphism, and
- surjective Zariski tangent map at the chosen point,

**branch coverage does not follow when the source point is singular.** The first-order tangent space can contain infinitesimal directions that do not integrate into actual source motion in the corresponding target directions.

This is a local mathematical/representation failure, not a global gluing failure.

## Safe positive certificate

A stronger certificate is valid and operationally useful.

> Let `pi:W -> H` be a proper morphism of finite-type complex algebraic varieties. Assume `H` is irreducible. If there is a point `w in W` with `h=pi(w)` such that `pi` is smooth at `w`, then `pi(W)=H`.

Reason: smoothness is open on the source, so after shrinking to a Zariski-open neighborhood `U` of `w`, the restriction `pi|_U` is smooth. Smooth morphisms are universally open, hence `pi(U)` contains a nonempty Zariski-open subset of `H`. Proper morphisms have closed image. A closed subset of an irreducible space containing a nonempty open subset is the whole space.

For a morphism between complex manifolds near `w` and `h`—equivalently, when the selected source and target points are smooth and the local Jacobian criterion is verified—surjectivity of the differential gives the needed local submersion/smoothness certificate. **The load-bearing condition is not the numerical rank alone; it is rank plus local integrability/smoothness.**

Primary algebraic-geometry controls:

- Stacks Project, tag `056G`: a smooth morphism is universally open.
- Stacks Project, tag `01W6`: a proper morphism has closed image (in the stated separated setting).
- Stacks Project, tag `01W5`: a closed immersion is proper.
- Stacks Project, tag `01V9`: differential/smoothness criteria require more than an arbitrary tangent-space dimension statement; smoothness includes the relevant flatness/fibre conditions.

## Separate local-to-global/gluing boundary

Even when local openness is genuine, **properness/closed-image control is separately load-bearing for whole-component coverage**. The standard open immersion

`A^1_C -> P^1_C`

is a local isomorphism, hence has full-rank differential everywhere, but its image omits the point at infinity. Therefore the local mathematical certificate and the local-to-global image-closure certificate must be recorded as separate obligations.

Likewise, if the target is not bound to one irreducible component, full-rank motion into one component does not cover other components. Component binding is therefore a separate target-identity/gluing guard.

## Hodge-specific calibration and disanalogy

Kloosterman's complete-intersection-on-hypersurface setting has the correct positive shape. His flag Hilbert scheme parametrizes pairs `(Y,Z)` and is projective in the relevant construction; the projection to the hypersurface parameter space is proper and its image dimension is computed. The paper then proves that the relevant Hodge locus is smooth at the reference hypersurface and identifies the corresponding irreducible Hodge-locus component with the complete-intersection locus. This is exactly the kind of source-family geometry that prevents the cusp-style tangent-space false positive.

This remains a **special-family calibration only**. It does not supply a coupled signed-`Q` witness incidence for an arbitrary rational Hodge class and does not close initial algebraicity, source-family completeness, coefficient/category preservation, higher-order lifting, algebraization, monodromy, degeneration/specialization, or global continuation.

Primary Hodge sources:

- E. Cattani, P. Deligne, A. Kaplan, *On the Locus of Hodge Classes*, arXiv:alg-geom/9402009 — algebraicity of the locus where a fixed integral class remains Hodge in a smooth projective family.
- R. Kloosterman, *Variational Hodge conjecture for complete intersections on hypersurfaces in projective space*, arXiv:2104.14845 — Theorem 1.1 / Theorem 4.14 and Section 3 flag-Hilbert image geometry.

## Expert-cell synthesis

**VHS/Hodge-locus lead.** Work on one reduced irreducible locally marked Hodge component. General Hodge loci can be singular; a tangent-rank certificate should be sought over the smooth locus of the chosen component or replaced by direct image-dimension control.

**Hilbert/Chow incidence lead.** Hilbert/incidence tangent spaces are only first-order objects. Unless the incidence source is known smooth/unobstructed at the tested point, a large tangent map can be a singular tangent-cone artifact. Prefer actual image geometry when smoothness is unavailable.

**Local algebraic-geometry lead.** The cusp inclusion is the cheapest exact falsifier. The safe replacement is `smooth-at-one-point + proper image + irreducible target`, not raw tangent surjectivity.

**Cycle/coefficient lead.** None of this licenses splitting a signed rational total class into independently persistent components. Exact transported total-class binding remains mandatory.

**Deformation/formal lead.** The cusp failure is local integrability failure. It is distinct from the later all-Artin/algebraization obligations. Smoothness of `pi` at one point would supply local lifting for that incidence only; it does not create a general witness incidence.

**Adversarial verifier.** Dropping source smoothness is killed by the cusp; dropping properness is killed by `A^1 -> P^1`; dropping irreducible-component binding is killed by a component inclusion. The certificate survives only with those boundaries explicit or replaced by direct image geometry.

**RAKL/metrology lead.** C004 changed routing from source tangent size to consumer image; C006 shadow changed the question from selected-point necessity to a sufficiency/integrability audit. Open proposal records guided search only and receive no theorem authority.

## Outcome and next residual

**Outcome:** `PARTIAL_SUCCESS / VERIFIED_SCOPED_NONIMPLICATION + SAFE_SUFFICIENT_CERTIFICATE`.

New obstruction:

`O-H4D1C-SMOOTH-SOURCE-OR-DIRECT-IMAGE-CERTIFICATE`

A future general Hodge deformation route may use either:

1. a **smooth-source/smooth-morphism certificate** at some point of the exact-class witness incidence, together with properness and component binding; or
2. a **direct image certificate** (closed/proper image plus top dimension / dominance) that does not rely on singular-source tangent spaces.

The raw path `SURJECTIVE_ZARISKI_TANGENT_MAP_AT_UNVERIFIED_INCIDENCE_POINT => HODGE_BRANCH_COVERAGE` is flattened.

Root remains `OPEN_NO_SOLUTION_CERTIFICATE`. Same-context expert roles earn `0/3` independent-review credit.
