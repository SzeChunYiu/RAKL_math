# H4d1c1 — formal effectivity over the completed Hodge branch

Authority: **proposal/shadow scoped transfer only**. This is not a proof of the rational Hodge conjecture, not a variational-Hodge theorem, and not independent review.

## Frozen atom

Let \(f:X\to S\) be smooth projective over a complex algebraic base, let \(s_0\in S\), and let a flat rational Hodge class \(\alpha\) already have one fixed finite signed rational algebraic witness on \(X_{s_0}\). Fix one algebraic irreducible local Hodge-locus branch \(T\) through \(s_0\). Write
\[
A=\widehat{\mathcal O}_{T,s_0},\qquad A_n=A/\mathfrak m^n,\qquad X_n=X_A\times_A A_n.
\]
After clearing denominators, freeze
\[
z_0=\frac1N\sum_{i=1}^r n_i[Z_{i,1}]
\]
with fixed integer coefficients and fixed component indexing.

The atom assumes, for each \(i\), a **compatible cartesian tower** of closed subschemes \(Z_{i,n}\hookrightarrow X_n\). It asks only whether this formal witness data is effective as an algebraic closed subscheme over \(\operatorname{Spec}A\).

## Scoped transfer lemma

**Lemma H4d1c1-C001 (formal closed-subscheme effectivity).**  
Assume \(A\) is Noetherian and complete, \(X_A\to\operatorname{Spec}A\) is separated and of finite type, and for every \(i\) the system \(Z_{i,n}\hookrightarrow X_n\) is compatible with cartesian transition squares and \(Z_{i,1}\) is proper over \(A_1\). Then for every \(i\) there is a closed subscheme \(Z_i\hookrightarrow X_A\), proper over \(A\), whose reduction to \(A_n\) is \(Z_{i,n}\) for every \(n\). Hence the fixed expression
\[
z_A=\frac1N\sum_i n_i[Z_i]
\]
is an algebraic signed rational cycle on \(X_A\) reducing to the prescribed formal component towers.

### Verification

This is a direct, componentwise application of the Stacks Project formulation of Grothendieck existence for closed subschemes, Lemma 30.28.1 (tag `0898`). Its hypotheses match the frozen representation: the completed local ring is Noetherian; the ambient base change is separated and finite type; compatibility is built into the tower; and each central projective cycle component is proper. Algebraicity of the Hodge-locus branch used to form the algebraic local ring is source-bound to Cattani–Deligne–Kaplan after denominator clearing of the rational class.

No new primitive theorem or operator is claimed. The solved subproblem is classified as **RAKL novelty class: TRANSFER** (with a representation refinement).

## Adversarial boundary audit

The theorem does **not** fire if lifts merely exist independently at each Artin order: a compatible inverse system is part of the hypothesis. It also does not certify that the algebraized closed subschemes are in the exact flat Hilbert/Chow witness category without an additional flatness argument; Stacks tag `0CTK` was inspected only as a separate flat-module effectivity boundary, not used to smuggle that conclusion in.

The theorem also does not prove that the resulting signed cycle has Gauss–Manin class \(\alpha\) unless the exact witness construction separately binds that class. Fixed coefficients alone do not solve class identity, component switching, or monodromy.

Most importantly, effectivity over \(\operatorname{Spec}\widehat{\mathcal O}_{T,s_0}\) is **not** descent to a Zariski or étale neighborhood of \(s_0\) in \(T\). Artin approximation is a separate interface. Therefore nearby pointwise variational algebraicity is not obtained in this atom.

## Residual split

The old undifferentiated `algebraization` residual separates into:

1. **local mathematical residual — compatible tower:** construct one all-order compatible exact-category witness tower for the fixed signed rational witness, while preserving the intended class and category;
2. **representation/category residual — flatness and class identity:** certify that the effective object lies in the exact Hilbert/Chow/cycle interface and continues to represent \(\alpha\);
3. **local-to-global/gluing residual — completion descent:** descend or spread the effective object from the completed local base to a genuine branch neighborhood with the required coefficient/category and component control;
4. **global residuals:** branch domination, monodromy/component switching, singular degeneration/specialization, global continuation, and root initial algebraicity.

Thus **formal closed-subscheme effectivity over the completion is conditionally closed**, while the difficult Hodge mathematics has not been solved; it has been localized more sharply.

## Routing consequence

The next high-information route should not spend an operator cycle reproving generic “algebraization” once a compatible proper closed-subscheme tower exists. Search should target the compatible higher-Artin tower first, and treat completion-to-neighborhood descent as a separate gluing atom. The first-order tangent/detector family remains saturated for this purpose by the H4d1a/H4d1b failure lineage.
