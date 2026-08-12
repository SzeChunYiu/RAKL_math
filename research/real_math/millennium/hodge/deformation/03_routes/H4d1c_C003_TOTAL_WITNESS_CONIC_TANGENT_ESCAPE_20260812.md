# H4d1c-c total-witness tangent-escape calibration

**Date:** 2026-08-12  
**Atom:** `H4d1c-c`  
**Parent residual:** `H4d1c-INDEPENDENT-HODGE-TO-WITNESS-TANGENT-SURJECTIVITY-MECHANISM`  
**Authority:** `SCOPED_SOLVED-CLASS_CALIBRATION / PROPOSAL_SHADOW / NO_HODGE_THEOREM / NO_ROOT_AUTHORITY`

## Exact question

After the H4d1c-b fixed-component fibre-product non-expansion result, test the smallest adversarial positive control for the remaining escape hatch: can a **genuinely total witness representation** have first-order directions that are absent from the fixed-component factorization?

The control is deliberately confined to divisors on `P^2_C`, where all degree-two divisors are algebraic and have class `2H`. It is therefore a representation/deformation calibration, not progress on initial algebraicity of higher-codimension Hodge classes.

## Frozen comparison

Let `W=H^0(P^2,O(1))=<x,y,z>`. The fixed-component representation of reducible conics is

`mu : P(W) x P(W) -> P(Sym^2 W),   ([l_1],[l_2]) |-> [l_1 l_2]`.

Freeze the central conic

`C_0 = V(xy) = L_x union L_y`

at `([x],[y])`. The full total-witness parameter space of conics is `P(Sym^2 W) ~= P^5`.

The precommitted falsifier was: if `d mu` is surjective at `([x],[y])`, then this control does **not** exhibit an escape from fixed-component tangent reachability.

## Exact tangent computation

The projective tangent target at `[xy]` is

`T_[xy] P(Sym^2 W) = Sym^2 W / <xy>`,

with basis represented by

`x^2, xz, y^2, yz, z^2`.

A tangent vector to the first factor at `[x]` can be represented by `a in <y,z>`, and one to the second factor at `[y]` by `b in <x,z>`. Differentiating multiplication gives

`d mu_(x,y)(a,b) = a y + x b  mod <xy>`.

Hence

`im(d mu_(x,y)) = <y^2, yz, x^2, xz>`

and has dimension `4`, whereas the total conic tangent space has dimension `5`. The class `z^2 mod <xy>` is not in the fixed-factor image.

The missing tangent integrates to the explicit algebraic family

`C_t = V(xy + t z^2)`.

For `t != 0`, `C_t` is smooth: the partial derivatives are `y`, `x`, and `2tz`, which have no common projective zero. Equivalently, the symmetric matrix of `xy+t z^2` has determinant `-t/4`, nonzero for `t != 0`.

Therefore a total-witness representation can strictly enlarge the first-order deformation image relative to the fixed-component factorization. The previous H4d1c-b non-expansion lemma is **representation-local**: it prunes bookkeeping fibre products of fixed selected components, not changing-decomposition total-witness geometry.

## What this does and does not establish

This is a solved codimension-one control. Since every `C_t` is a degree-two divisor, its cohomology class is `2H` and remains an algebraic `(1,1)` class. The control therefore demonstrates a real geometric DifferenceWitness between two witness representations: fixed factorization cannot reach `z^2`, while the total linear-system representation does.

It does **not** transfer this tangent enlargement to codimension `p>1`. In higher codimension there is generally no complete-linear-system analogue for cycles; Hodge-locus tangency is nontrivial; Hilbert/Chow branches can be obstructed; signed rational coefficient semantics and rational equivalence require separate treatment; and tangent reachability does not imply higher-Artin lifting, algebraization, monodromy control, singular-degeneration compatibility, or global continuation.

## Primary-source scope controls

- Cattani–Deligne–Kaplan, *On the Locus of Hodge Classes*, arXiv:`alg-geom/9402009`: controls the base locus where a fixed Hodge class remains Hodge; it is not a general witness-lifting theorem.
- Nishinou, *Deformation of pairs and semiregularity*, arXiv:`2009.01651`: gives a positive relative-deformation result for semiregular divisor maps, a source-bound positive control rather than a general higher-codimension transfer.
- Kloosterman, *Variational Hodge conjecture for complete intersections on hypersurfaces in projective space*, arXiv:`2104.14845`: provides a special higher-codimension source family where explicit incidence/flag-Hilbert geometry supports a variational Hodge result.
- Bloch–Esnault–Kerz, *Deformation of algebraic cycle classes in characteristic zero*, arXiv:`1310.1773`: concerns a distinct formal deformation problem for rational cycle classes and does not collapse the first-order witness-representation issue.
- Movasati, *On a Hodge locus*, arXiv:`2211.11405`: explicitly studies situations where Hodge deformation space can be larger than algebraic-cycle deformation space, reinforcing the need to prove witness reachability rather than infer it from Hodge tangency.
- Liu–Shen, *Sections of Hodge bundles II: deformation of (p,p)-classes and applications to Kähler geometry*, arXiv:`2602.13951` (2026): current Hodge-bundle/Hodge-locus context; used only for scope awareness, not as an algebraic witness-lifting theorem.

The tangent-rank and smoothing statements above are proved directly in this packet and do not rely on those sources.

## Same-context expert cell

**Algebraic-geometry/Hilbert–Chow specialist.** Verified the source and target tangent dimensions, differentiated the multiplication map, and interpreted `z^2` as a changing-decomposition direction.

**VHS/Hodge-locus specialist.** Confirmed the positive control is codimension one, where degree fixes the divisor class, and blocked any inference that a higher-codimension Hodge-locus tangent is automatically represented by a total witness family.

**Deformation/obstruction specialist.** Confirmed that the explicit one-parameter family integrates the chosen first-order direction in this solved control, while higher Artin compatibility and algebraization remain independent in the actual H4d1c target.

**Adversarial proof auditor.** Executed the falsifier: the `5 x 4` differential matrix has rank `4`; adjoining the `z^2` column raises rank to `5`; smoothness for `t != 0` follows from the gradient or determinant test. No hidden smoothness assumption on the reducible central conic was used.

**RAKL v3/metrology auditor.** Classified this as proposal/shadow evidence only, assigned zero independent-review credit, separated the episode from its diagnosis/obstruction/lesson, and prohibited raw repository growth from being counted as learning.

These are same-context analytical roles and count as **zero genuinely isolated mathematical reviews**.

## Local versus gluing diagnosis

No local mathematical failure occurred in the codimension-one calibration: the tangent escape is proved. No local-to-global theorem was attempted. The unresolved transfer to a higher-codimension Hodge branch is a **representation/transfer residual before gluing**, not a gluing failure. Higher-order/formal/algebraic/global interfaces remain separate residual coordinates.

## Outcome

`PARTIAL_SUCCESS / SOLVED_CLASS_REPRESENTATION_ESCAPE_CALIBRATION`.

The H4d1c-b fixed-component route stays pruned, but the broader total-witness path is now demonstrably nonempty in a solved control. The next atom must be source-specific and higher-dimensional: identify a genuine total cycle/incidence/correspondence representation whose tangent projection reaches an **actual higher-codimension Hodge-locus branch**, with an explicit DifferenceWitness from fixed-component bookkeeping and exact rational coefficient/category semantics.

Root rational Hodge Conjecture status remains `OPEN_NO_SOLUTION_CERTIFICATE`.