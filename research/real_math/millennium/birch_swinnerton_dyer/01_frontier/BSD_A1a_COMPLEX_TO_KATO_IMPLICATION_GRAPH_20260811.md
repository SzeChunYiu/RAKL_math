# BSD-A1a source-level implication graph — complex analytic rank two to generalized Kato nonvanishing

**Status:** source-bound research-control audit; no theorem candidate and no root authority.

**Framework authority inspected:** `SzeChunYiu/RAKL@55d4cb0a83f271d3263fbe48f99b173119c732d2`.  
**Application root:** `SzeChunYiu/RAKL_math#7`.

## Question

For an elliptic curve `E/Q` with exact complex analytic rank two, where is the first currently unclosed noncircular arrow toward a nonzero generalized Kato class?

The root premise is

`ord_{s=1} L(E,s) = 2`.

The desired intermediate conclusion is, for explicitly admissible auxiliary data,

`kappa_p(E) != 0`.

## Expert-cell decomposition

The analytic/automorphic, Iwasawa, arithmetic-geometry, adversarial, formal-assurance, and novelty lenses agree that the earlier compressed arrow must be expanded as follows.

### A0. Exact complex root input

`ord_{s=1} L(E,s)=2`.

This is an order in the **complex spectral variable `s`**. It does not contain a `p`-adic character coordinate.

### A1. Auxiliary-data admissibility

Castella–Hsieh work with a good ordinary `p>3`, an imaginary quadratic field `K` in which `p` splits, residual/level hypotheses, and suitable ring-class/CM auxiliary data. Their Remark 1.8 records conditions under which infinitely many choices give

`L(E,ad^0(g),1)=L(E^K,1) L(E/K,chi,1) != 0`.

**Authority:** proved under the stated source hypotheses; this solves an auxiliary-selection problem in those families, not the BSD bridge itself.

### A2. Anticyclotomic theta interpolation

Castella–Hsieh Theorem 2.3 defines an anticyclotomic theta element `Theta_{f/K,chi}(T)` with `T` determined by a topological generator of `Gamma_infinity`. For finite-order anticyclotomic characters `epsilon_zeta`, its specialization satisfies an interpolation formula of the form

`Theta(zeta-1)^2 = explicit_nonzero/local_factors * L(f/K tensor chi epsilon_zeta,1) / period`.

Thus the `T` direction varies **anticyclotomic character**, while the BSD root order varies **complex `s`**.

At the trivial character, central vanishing implies `Theta(0)=0`. In Section 5.3 the authors explicitly conclude only

`r = ord_T Theta_{f/K} > 0`

from `L(E/K,1)=0` and interpolation.

**Authority:** theorem-level interpolation; **insufficient for exact order two**.

### A3. Live missing bridge

Wanted:

`ord_{s=1} L(E,s)=2`
`+ admissible auxiliary data`
`=> ord_T Theta_{f/K}=2`.

No such implication is supplied by Theorem 2.3. Exact vanishing order is directional: value interpolation at the base point does not identify the first nonzero `T` coefficient from the first nonzero complex `s` derivative.

A generic calibration such as

`F(s,T)=(s-1)^2+T^4`

has order two along `s` at `T=0` and order four along `T` at `s=1`. This is **not** an arithmetic model or counterexample; it only proves that an additional comparison identity is logically necessary.

**Residual opened:** `BSD-A1a1-THETA-ORDER-COMPARISON`.

### A4. Triple-product factorization

Castella–Hsieh Proposition 2.5 factors the relevant triple-product `p`-adic L-function as

`unit * Theta_{f/K}(T) * nonzero auxiliary central-value factor * congruence factor`

under explicit hypotheses.

**Authority:** proved factorization. Once auxiliary factors are nonzero, theta order is the load-bearing anticyclotomic order. This arrow does not determine theta order from complex analytic rank.

### A5. Explicit reciprocity / localized big class

Their Coleman-map/explicit-reciprocity formula identifies the localization of the big diagonal-cycle class with

`Theta_{f/K}(T) * explicit nonzero factors`.

**Authority:** proved under source hypotheses. This transports theta information into a cohomological localization; it still consumes rather than derives the theta leading order.

### A6. Derived-height leading term

Theorem 5.3 sets `r=ord_J Theta_{f/K}`, places the generalized Kato class in the `r`th derived Selmer filtration, and relates its derived `p`-adic height to the leading theta term.

**Authority:** proved conditional on the setup. It is a leading-term theorem **after `r` is defined**, not a complex-`s` to `T` order comparison.

### A7. Generalized-Kato nonvanishing criterion

Theorem B proves, under Theorem A hypotheses and the additional arithmetic assumption

`rank_Z E(Q) > 0`,

that

`ord_T Theta_{f/K}=2 => kappa != 0`.

This exposes a second independent residual:

`BSD-A1a2-LOCALIZATION-POSITIVE-RANK-BRIDGE`.

Using `rank E(Q)>0` to prove the root analytic-rank-to-rational-rank direction would be circular. Castella's later non-CM formulation likewise shows that the converse Selmer-to-Kato direction is controlled by nonzero localization.

## Cross-Millennium memory review

The scoped tool `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` is applicable only as a diagnostic. Its Yang–Mills source concerned cutoff normalization, not arithmetic. The DifferenceWitness is:

- **source:** finite-scale dimensionless gap vs continuum physical gap;
- **target:** complex `s`-order vs anticyclotomic `T`-order;
- **shared abstraction:** a valid surrogate coordinate does not automatically preserve a root-critical coordinate through a representation change;
- **material difference:** no continuum limit or spectral-gap mechanism transfers;
- **target falsifier:** the exact interpolation theorem itself yields only positive `T`-order, not exact order two.

The related failure `F-XM001-POINTWISE-GAP-COLLAPSE` is therefore a warning about bridge sufficiency, not evidence against any BSD theorem.

## Result of this cycle

The earlier child `BSD-A1a-KATO-NONVANISHING-BRIDGE` is now decomposed into two non-equivalent residuals:

1. **`BSD-A1a1-THETA-ORDER-COMPARISON`** — find a noncircular theorem comparing exact complex `s`-order two with exact anticyclotomic `T`-order two.
2. **`BSD-A1a2-LOCALIZATION-POSITIVE-RANK-BRIDGE`** — eliminate or justify the positive-rational-rank/localization input needed downstream for Kato nonvanishing.

The first is selected because it is analytically upstream and does not immediately restate a positive Mordell–Weil-rank conclusion.

## Source boundary

Primary sources inspected for this audit:

- Andrew Wiles, Clay Mathematics Institute official BSD problem description.
- Francesc Castella and Ming-Lun Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum of Mathematics, Sigma 10 (2022), e12, DOI `10.1017/fms.2021.85`, especially Theorem 2.3, Proposition 2.5, Theorem B, Theorem 5.3 and the Appendix.
- Francesc Castella, *Nonvanishing of generalised Kato classes and Iwasawa main conjectures*, arXiv:`2312.01481`.

No claim is made that this source set proves absence of every possible comparison theorem. The next search is explicitly a bounded primary-literature search for that theorem family.
