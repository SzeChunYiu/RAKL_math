# H4d1d — unrestricted proper domination is target-equivalent at class level

**Date:** 2026-08-11  
**Atom:** `H4d1d`  
**Result:** `H4d1d-C001-UNRESTRICTED-DOMINATION-TARGET-EQUIVALENCE`  
**Authority:** `SCOPED_VERIFICATION / ROUTE_PRUNING / REPRESENTATION_CORRECTION / NO_HODGE_THEOREM / NO_ROOT_AUTHORITY`

## Chronology boundary

The candidate equivalence was noticed before the v3 pre-action receipt. It therefore receives **no prospective discovery credit**. Receipt `1a7c804e24a4a9f11c13722bb2cee7648fb1e6bec8ccae5807c4f852f6d6f04c` prospectively freezes only the subsequent verification discriminator and its three allowed branches. This distinction is intentional: retrospective experience may guide search, but it is not rewritten as prospective discovery.

## Frozen local statement

Let `f:X→S` be smooth projective over `C`. Work on one irreducible **reduced algebraic fixed-class branch** `T` of the Hodge locus on which the rational flat class `α` is globally specified. The deformation lane already assumes an algebraic witness at the central point. Full Hodge-scheme nilpotents, higher Artin lifting, algebraization beyond the Hilbert parameter spaces used below, global monodromy, singular degeneration, and root initial algebraicity are outside this atom.

For class-level witnesses, compare:

- **(A) Pointwise variational algebraicity:** for every `t∈T(C)`, the class `α_t` is represented by some finite rational algebraic cycle on `X_t`.
- **(B) Unrestricted proper domination:** there exist one finite tuple of Hilbert polynomials, one finite rational coefficient vector, and one irreducible component `W` of the corresponding exact-class relative Hilbert-product stratum such that `W→T` is proper and surjective.

The word **unrestricted** is essential: all finite Hilbert-polynomial tuples, all finite rational coefficient vectors, and all their components are allowed. No requirement is imposed that `W` contain the originally selected central witness `z0`.

## Verification of (B) ⇒ (A)

This direction is immediate once the words `exact-class` and `surjective` are enforced. A point `w∈W_t` is a finite tuple of subschemes in `X_t`; the fixed rational coefficient vector gives a rational algebraic cycle, and the exact-class condition says its Betti class is `α_t`. Surjectivity supplies such a point over every `t`.

The falsifier here is coefficient/category drift: a dominating Hilbert component whose universal cycle does not carry the exact rational class does **not** establish (A).

## Verification of (A) ⇒ (B)

Fix a relatively ample line bundle. Any rational cycle witnessing `α_t` is a finite rational linear combination of irreducible codimension-`p` subvarieties. Such a witness therefore determines finite discrete data

`D = (r; P_1,…,P_r; q_1,…,q_r)`

with Hilbert polynomials `P_i` and rational coefficients `q_i`. The set of all such finite data is countable.

For fixed `D`, form

`H_D = ∏_T Hilb^{P_i}_{X/T}`.

By Stacks Project Tag `0DPH`, each fixed-polynomial relative Hilbert space is proper over `T` under the projective hypotheses, hence so is the finite product. The universal flat subschemes determine a signed relative cycle; Stacks Tags `0H4Z` and `0H56` are the cycle-family controls. After clearing the denominator of the fixed coefficient vector, its Betti cycle class is locally constant in the pulled-back Gauss–Manin local system. Consequently the locus `H_D^α` on which that class equals the corresponding multiple of `α` is a union of connected components. It remains proper over `T`.

Let `Z_D` be the image of `H_D^α→T`. Properness makes `Z_D` Zariski closed. If (A) holds, every complex point of `T` belongs to some `Z_D`, so

`T(C) = ⋃_D Z_D(C)`

with only countably many `D`.

An irreducible finite-type variety over the uncountable field `C` is not a countable union of proper closed subvarieties. A short induction proof is available: reduce by Noether normalization to affine space; in dimension one proper closed subsets are finite, and in higher dimension choose a fibre of a coordinate projection outside the countable union of exceptional parameter sets and apply induction. Therefore some `Z_D` equals `T`.

For that fixed `D`, `H_D^α` has finitely many irreducible components. Their proper images are closed and their union is `T`; irreducibility of `T` forces one component `W` to have image `T`. This is (B).

## Source bindings and limits

- Cattani–Deligne–Kaplan, arXiv:`alg-geom/9402009`, is used only for the algebraicity control on fixed integral Hodge loci after denominator clearing. It does not supply algebraic-cycle witnesses.
- Stacks Project Tag `0DPH` is used for properness of fixed-Hilbert-polynomial relative Hilbert spaces.
- Stacks Project Tags `0H4Z`/`0H56` are used for relative-cycle bookkeeping from flat Hilbert families.
- Dan arXiv:`1404.7519` and Kloosterman arXiv:`2104.14845` remain special-family positive controls and are **not** used to generalize a domination theorem.

The argument is deliberately local/fixed-class. If the class is not globally single-valued on the chosen algebraic branch, a cover/monodromy interface must be frozen separately; this cycle does not erase that gluing problem.

## Adversarial boundary: pointed versus class-level domination

The equivalence does **not** survive addition of a pointed-witness condition. Pointwise algebraicity of `α_t` does not imply that the one originally selected witness `z0` lies on a component dominating `T`; different fibres may require different components or representatives. This is exactly the selected-witness/class-level distinction left open by H4d1c.

Thus there are two different research targets:

1. **Unpointed unrestricted class-level domination:** under the frozen hypotheses, target-equivalent to pointwise variational algebraicity and therefore not an independent mechanism.
2. **Pointed or independently generated restricted-family domination:** genuinely stronger search information, but it requires source-specific geometry and may fail even when the class remains algebraic.

The second target is the only noncircular direction worth allocating theorem-invention budget to here.

## Outcome

The predeclared branch selected is:

`TARGET_EQUIVALENT_UNDER_FROZEN_HYPOTHESES`.

This is a **representation/search-target pruning result**, not a new Hodge theorem. It removes the unrestricted version of H4d1d as an independent mechanism. The next atom should ask for a bounded witness family generated for reasons external to the desired pointwise conclusion — for example through a specified correspondence/Lefschetz mechanism, a cycle-moduli construction with a pointed central witness, a normal-function construction that actually lifts to cycles, or a degeneration/specialization mechanism with explicit monodromy and coefficient control.

## Local versus gluing failure ledger

Local mathematical failure: no failure of the Hodge conjecture was found. The local failure is **representation-level**: the unrestricted domination target merely re-encodes the desired pointwise conclusion.

Local-to-global/gluing failures were not tested and remain separate: monodromy of `α`, component switching outside the fixed branch, algebraization of any non-Hilbert formal/analytic lift, singular degeneration/specialization, and global continuation across Hodge-locus components.
