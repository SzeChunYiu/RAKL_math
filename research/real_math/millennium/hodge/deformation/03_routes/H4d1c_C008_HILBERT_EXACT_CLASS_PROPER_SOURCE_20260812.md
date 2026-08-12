# H4d1c-C008 — fixed-witness Hilbert incidence gives an exact-class proper local source

**Authority:** proposal/shadow, source-bound local variational certificate only. **Root:** `OPEN_NO_SOLUTION_CERTIFICATE`.

## Exact local setup

Let `f : X -> S` be a smooth projective complex algebraic family, let `s0 in S(C)`, and let `U subset S^an` be a sufficiently small contractible analytic neighbourhood of `s0`. Fix codimension `p`, a flat rational cohomology section `alpha` of `R^{2p} f_* Q|_U`, and a reduced irreducible local Hodge-locus branch `H subset U` through `s0` on which `alpha_s` is of type `(p,p)`. Assume only for this variational atom that the central class has an algebraic witness

`alpha_{s0} = sum_i q_i [Z_i]`, with `q_i in Q` and integral codimension-p subvarieties `Z_i subset X_{s0}`.

This central algebraicity is an input to the variational atom, not a conclusion about an arbitrary root instance.

## Certificate

Choose `N>0` clearing all denominators and write `m_i=N q_i in Z`. Fix a relative ample line bundle and the Hilbert polynomial `P_i` of each `Z_i`. For every occurrence `1 <= a <= |m_i|`, take a copy of the fixed-polynomial relative Hilbert space `Hilb^{P_i}(X/S)`. Form the finite fibre product

`P = product_{i,a} Hilb^{P_i}(X/S)` over `S`.

By Grothendieck's Hilbert construction in the form recorded by Stacks tag `0DPH`, every factor is proper over `S`, hence `P -> S` is proper. Let `w0` be the tuple which repeats `Z_i` exactly `|m_i|` times. The universal flat subschemes on the factors define on `X x_S P` the signed formal relative cycle

`Z_univ = sum_i sign(m_i) sum_{a=1}^{|m_i|} Z_{i,a}`.

After analytification and restriction over `U`, its fibre cohomology class is a locally constant section of the pulled-back integral local system. On the connected component `P0` through `w0`, this section equals `N alpha` because the two locally constant sections agree at `w0` and `U` is contractible. Therefore every point of `P0` parametrizes a signed rational algebraic cycle `(1/N) Z_univ,w` whose class is exactly `alpha` in the corresponding fibre.

Now bind the source to the chosen Hodge branch by

`W_H := (P0 x_U H)_red`.

The map `pi : W_H -> H` is proper: properness of the Hilbert product survives analytic restriction, passage to a closed connected component, and base change to `H`. Every point of `W_H` carries an algebraic signed-Q witness of the exact transported class `alpha_s`.

Hence, **for any fixed central algebraic witness and fixed local Hodge branch, exact signed-Q class binding plus proper/closed source projection is constructible by a finite product of fixed-polynomial relative Hilbert spaces.** No smoothness, dominance, or branch coverage follows from this construction alone.

## Interaction with C007

Merged C007 established a sufficient image certificate: for a proper map to an irreducible target, smoothness at one source point gives a nonempty open image; properness gives closed image; irreducibility forces full image. C008 supplies the previously separate `exact-class source + properness + branch binding` half for the canonical fixed-witness Hilbert source. The surviving local mathematical obstruction is therefore

`O-H4D1C-HILBERT-INCIDENCE-SMOOTHNESS-OR-DIRECT-DOMINANCE`:

> Prove that the exact-class Hilbert incidence `W_H -> H` is smooth at a useful point, or prove directly that its image contains a nonempty open/top-dimensional subset of `H`, without using tangent surjectivity at an unverified singular point as a substitute.

## Adversarial boundary audit

1. **Negative rational coefficients.** They do not require a Hilbert scheme of negative cycles. Clear denominators and parameterize each positive/negative integral component in a separate Hilbert factor; the sign is applied only in the formal cycle sum.
2. **Multiplicity.** Repeat a Hilbert factor `|m_i|` times. No unsupported nonreduced thickening claim is needed.
3. **Class drift.** The universal families are flat; their fibre fundamental classes are locally constant in the pulled-back cohomology local system. Contractibility of `U` fixes the comparison with `alpha`. This is a local statement only.
4. **Target-component leakage.** Base change to the chosen reduced irreducible branch `H` prevents using witnesses over a different Hodge component as branch-coverage evidence.
5. **Singular source.** `W_H` may be singular. C007 therefore remains active: tangent rank at a singular point is not an integrability certificate.
6. **Vertical source.** `W_H` may consist only of the central fibre or have image of smaller dimension. Properness closes the image; it does not make it large.
7. **Monodromy.** The certificate is frozen on contractible `U`. Extending it around nontrivial monodromy is a separate gluing/globalization problem.
8. **Formal versus actual families.** Relative Hilbert points are actual algebraic subschemes, so this atom does not need Artin effectivity merely to materialize these fixed-polynomial deformations. Higher-order/formal obstruction theory is still relevant to proving smoothness or constructing lifts.
9. **Initial algebraicity.** The certificate starts from a chosen algebraic `z0`; it does not construct `z0` for an arbitrary Hodge class and therefore cannot close the Hodge root.

## Analogue and disanalogy

Kloosterman's complete-intersection-on-hypersurface result is a positive structural analogue because its flag-Hilbert geometry genuinely maps a family of algebraic witnesses into a varying hypersurface/Hodge locus. The transfer is rejected beyond shape: his complete-intersection hypotheses give special incidence geometry not available for an arbitrary signed rational cycle. Cattani–Deligne–Kaplan supplies the Hodge-locus target geometry, not witness existence.

## Failure separation

No local mathematical falsifier defeated the exact-class/proper-source construction within the stated local contract. The cycle does, however, record a **meta-policy chronology failure**: the relative-Hilbert-product hypothesis appeared in private scratch before the durable v3 pre-action receipt. Consequently the result receives no prospective discovery credit. Verification/falsification after the receipt is retained as proposal/shadow evidence only.

Local mathematical residuals and local-to-global/gluing residuals are kept separate. Local: source smoothness/integrability or direct dominance. Gluing/global: monodromy, continuation across singular/degenerate loci, specialization, and any route from a special algebraic fibre to arbitrary root instances.
