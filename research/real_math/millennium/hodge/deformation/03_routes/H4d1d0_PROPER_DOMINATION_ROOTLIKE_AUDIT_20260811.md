# H4d1d0 proper-domination root-like audit

**Atom:** `H4d1d0`  
**Root:** rational Hodge Conjecture, exact smooth-projective complex / rational-coefficient scope  
**Authority:** `PROPOSAL_SHADOW_REPRESENTATION_AUDIT / NO_NEW_HODGE_THEOREM / ROOT_AUTHORITY_NONE`  
**Pre-action receipt:** `734888108cce58b020ce31249cda538cfc727d732ac319319c892d7719d6542f` frozen in commit `0106e9186e19cca49728e39e94db74528dcd5418` before the source-bound verification.

## Question

Pending PR #119 opened `H4d1d-REDUCED-BRANCH-PROPER-WITNESS-DOMINATION`: for an irreducible reduced Hodge branch `T_red`, seek an exact rational signed-cycle incidence component proper over the branch and dominating it. `H4d1d0` asks a prior discriminator:

> Is “some proper exact witness component dominates `T_red`” actually a weaker geometric bridge than pointwise variational algebraicity on `T_red`, or is it only another representation of that same class-level obligation?

The atom also separates that class-level question from the stronger selected-witness question: whether a component containing the fixed central witness `z0` dominates.

## Exact scoped lemma

Let `T` be an irreducible finite-type complex algebraic variety. Suppose there is a countable family of proper finite-type morphisms

`pi_i : W_i -> T`, `i in N`,

with exact witness semantics: every point of `W_i` represents an allowed signed rational algebraic cycle in the corresponding fibre whose cohomology class is the prescribed flat class `alpha`; and the family is complete for the allowed witness category in the sense that every pointwise algebraic witness belongs to some `W_i`.

Define:

- **A:** for every `t in T(C)`, `alpha_t` has an allowed algebraic-cycle witness;
- **B:** for some `i`, `pi_i(W_i)=T`.

Then **A iff B**.

### Proof

`B => A` is immediate from the exact witness semantics. For `A => B`, properness makes each image `Z_i := pi_i(W_i)` Zariski closed. Pointwise coverage gives

`T(C) = union_i Z_i(C)`.

An irreducible finite-type variety over the uncountable field `C` cannot be a countable union of proper Zariski-closed subsets, so some `Z_i=T`.

For completeness, the uncountability step can be proved elementarily. By Noether normalization reduce to affine space. If `A^n_C` were covered by countably many proper closed sets, choose a nonzero polynomial vanishing on each. Choose the first coordinate outside the countable union of finite bad sets on which any one of those polynomials specializes identically to zero; then induct on `n`. The resulting point avoids every closed set.

This is standard algebraic geometry assembled for route diagnosis; it is not claimed as new mathematics.

## Why the witness family is naturally countable, and the exact boundary

For a projective family `X_T -> T`, a rational cycle can be denominator-cleared and written as a finite signed integral sum `sum_j a_j [Z_j]`. Record the denominator, the finite integer coefficient tuple, and the Hilbert polynomials of the integral subvarieties. There are only countably many such discrete data. For each fixed tuple, use the fibre product over `T` of the corresponding relative fixed-Hilbert-polynomial spaces. Stacks Project Tag `0DPH` states that the fixed-Hilbert-polynomial relative Hilbert space is proper over the base when the ambient morphism is proper of finite presentation with a relatively ample line bundle.

The important guard is **exact class binding**. A Hilbert polynomial does not by itself say `sum_j a_j cl(Z_j)=N alpha`. The countable family used by the lemma must be restricted to components/pieces where the prescribed cohomology class is actually bound under the pulled-back local system. This audit does not silently promote that class-binding step to a theorem; it is part of the typed parameterization assumption.

Cattani–Deligne–Kaplan (`arXiv:alg-geom/9402009`, 1994; JAMS 1995) supplies the separate fact that the locus where a fixed integral class remains Hodge is algebraic in a smooth projective algebraic family. It does not supply algebraic-cycle witnesses.

## Selected-witness falsifier

Class-level domination does **not** imply persistence of the chosen central witness.

Take `T=A^1_C`. Let `W_dom=T` map by the identity and let `W_vert={0}` map to `0`. Choose the distinguished central point `z0` in `W_vert`. Every point of `T` has a witness through `W_dom`, and a component dominates `T`, but the component containing `z0` has image `{0}`.

Therefore the statements

1. some exact witness component dominates `T`, and
2. a component containing the selected central witness `z0` dominates `T`

must not be conflated. The first is class-level and, under the countable proper parameterization, equivalent to pointwise algebraicity. The second adds a genuine transport/connectivity requirement and needs independent source geometry.

## Positive controls and disanalogies

Ananyo Dan (`arXiv:1404.7519`) proves a variational-Hodge result for complete-intersection cycles on projective hypersurfaces and explicitly relates the corresponding Hodge locus to a flag-Hilbert image in that special source family. Remke Kloosterman (`arXiv:2104.14845`) gives another proof for complete-intersection cycles. These are positive controls showing that source-specific incidence geometry can establish the equivalent class-level statement without assuming it.

They are not literal transfers to arbitrary rational Hodge classes: the complete-intersection equations, tangent/dimension identities, and source geometry are absent in the general root problem. Dan's work on nonreduced Noether–Lefschetz components (`arXiv:1407.8491`) also reinforces the prior H4d1c warning that reduced support and full Hodge-locus scheme structure must be typed separately.

## Episode -> diagnosis -> obstruction/lesson

- **Episode:** `H4d1d0-C001-PROPER-COVER-EQUIVALENCE` records the executed countable-cover discriminator and selected-component hostile control.
- **Diagnosis:** `D-H4D1D0-DOMINATION-IS-CLASSLEVEL-REFORMULATION` says the pending “some component dominates” bridge is noncontracting at class level under the frozen parameterization assumptions.
- **Failure experience:** `F-H4D1D0-SOME-COMPONENT-DOMINATION-NONCONTRACTING` is a scoped route warning, not a blacklist of incidence methods.
- **Lesson:** `L-H4D1D0-TYPE-SOME-VS-SELECTED-COMPONENT` requires future moduli routes to distinguish some-component, selected-component, and bounded/canonically replaceable component claims.
- **Successor obstruction:** `H4d1e-SELECTED-OR-BOUNDED-COMPONENT-TRANSPORT` asks for independent source geometry forcing a component through `z0`, or a canonically controlled bounded replacement family, to dominate a dense open without assuming pointwise branch algebraicity.

## Local mathematics versus gluing

The local mathematical result is only the scoped representation equivalence plus the selected-component nonimplication. The local mathematical **failure** is that no general source-specific selector/transport theorem was found.

The separate **gluing failures** remain: monodromy may permute witness components; extension across singular branch points and degenerations is open; local domination does not automatically globalize across the Hodge locus; and the root initial-algebraicity problem is completely untouched because this deformation lane begins with an algebraic central witness.

## Root status

`OPEN_NO_SOLUTION_CERTIFICATE`.

No proof, novelty, independent-review, or root-promotion gate is invoked by this route audit. The result is a `representation`-class RAKL subproblem resolution of structural rank `0`: it removes a noncontracting formulation from the search path and sharpens the next obstruction, but it is not new mathematics.
