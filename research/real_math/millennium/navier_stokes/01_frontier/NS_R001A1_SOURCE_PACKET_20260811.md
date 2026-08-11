# NS-R001a1 primary-source packet — averaging-stable partial-regularity barrier

**Atom:** `NS-R001a1`  
**Authority:** source-bound context only; no theorem candidate or root authority.  
**Frozen context:** `sha256:f357574cb08e88f75b276cddaa5997e4d471bc19a384bec2a02b9207933d377f`

## Primary sources

### Tao — averaged Navier–Stokes blowup

Terence Tao, *Finite time blowup for an averaged three-dimensional Navier-Stokes equation*, JAMS 29 (2016), arXiv:1402.0290, DOI 10.1090/jams/838.

Load-bearing facts used here:

1. The true projected Navier–Stokes nonlinearity has the cancellation `⟨B(u,u),u⟩=0`, giving the energy identity.
2. Tao constructs an averaged operator `\tilde B`, built from rotations/dilations/order-zero Fourier multipliers, that retains the cancellation and essentially the harmonic-analysis upper-bound strength of `B`.
3. The averaged equation admits finite-time blowup.
4. Therefore a positive regularity proof must use finer structure not shared by the averaged operator; energy cancellation plus generic harmonic-analysis estimates are insufficient.
5. Tao explicitly identifies the differential vorticity formulation of true Navier–Stokes as an example of structure not automatically shared by a generic averaged equation.

Primary URL: https://arxiv.org/abs/1402.0290

### Coiculescu — partial regularity and blowup in one amenable model class

Matei P. Coiculescu, *Partial Regularity and Blowup for an Averaged Three-Dimensional Navier-Stokes Equation*, arXiv:2307.15986v4.

Load-bearing facts used here:

1. Definition 1 introduces an **amenable** bilinear-operator class with: energy cancellation, pseudodifferential structure, broad `L^p`-type upper bounds (including endpoint integrability cases stated there), and a discrete scaling property.
2. Theorem 1.3 / 2.1: for `3/4 < alpha < 5/4`, a smooth solution for an amenable operator, if it first blows up at `T`, is smooth at `T` away from a closed set of Hausdorff dimension at most `5-4 alpha`.
3. Theorem 1.2: for every `3/4 < alpha < 5/4`, there exists an averaged amenable operator with Schwartz divergence-free data whose equation blows up in finite time; at the first blowup time its singular set still has Hausdorff dimension at most `5-4 alpha`.
4. At classical Navier–Stokes dissipation `alpha=1`, the source therefore supplies an averaged blowup equation in the same amenable class while retaining a partial-regularity conclusion with singular-set dimension at most `1`.
5. The paper's partial-regularity proof is Fourier/wavelet based. Its introduction explicitly distinguishes this from the suitable-local-energy Caffarelli–Kohn–Nirenberg techniques and says those techniques were not transferred in that work.

Primary URL: https://arxiv.org/abs/2307.15986

## Exact transfer boundary

The source-supported no-go is deliberately narrow:

> A global-regularity proof architecture whose decisive hypotheses and deductions are invariant across Coiculescu's amenable class — energy cancellation, the registered pseudodifferential/`L^p` bounds, discrete scaling, and the associated wavelet partial-regularity machinery — cannot be sufficient, because the same class contains a finite-time blowup equation at `alpha=1`.

This does **not** establish that CKN suitable-local-energy structure, the exact pressure Poisson identity, the differential vorticity equation, helicity structure, or any other true-Navier–Stokes-specific identity is shared by the averaged countermodel. Those are residual discriminators to audit, not assumptions of this no-go.

## Parameter check

`alpha=1` satisfies `3/4 < 1 < 5/4`, and `5-4 alpha = 1`. No endpoint extrapolation is used.
