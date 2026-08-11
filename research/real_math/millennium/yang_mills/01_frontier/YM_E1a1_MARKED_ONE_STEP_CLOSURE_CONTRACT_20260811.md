# YM-E1a1 marked one-step closure contract — 2026-08-11

**Authority:** `FROZEN_RESEARCH_CONTRACT / NOT_A_THEOREM / ROOT_AUTHORITY_NONE`

**Parent atom:** `YM-E1a1`  
**Framework authority:** `SzeChunYiu/RAKL@15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`  
**Application root:** `SzeChunYiu/RAKL_math#5`

## Purpose

The parent context packet authorizes candidate generation only after the one-step marked/source question is made operational. This contract fixes what a useful marked RG output must expose before any multiscale conclusion is allowed.

Let an exact finite-cutoff block transformation be written schematically as

\[
e^{-S'(V;J)}
=
\int K(V,U)\,e^{-S(U)}\,
\exp\!\left(\sum_{\alpha\in\mathcal A}J_\alpha O_\alpha(U)\right)dU,
\]

with \(J=0\) the unmarked theory. For each registered source direction \(\alpha\), define the exact normalized tangent

\[
D_\alpha(V)
=
-\partial_{J_\alpha}S'(V;J)\big|_{J=0},
\]

equivalently as the corresponding conditional expectation after subtracting any normalization term required by the chosen convention.

No claim is made here that Balaban's published unmarked RG already supplies this marked theorem.

## Frozen one-step outputs

A candidate marked space must return all five coordinates for every registered source direction.

1. **Exact derivative.** State the finite-cutoff \(D_\alpha(V)\) and justify differentiation under the block integral.
2. **Generated labels.** Give the set \(\Gamma(\alpha)\) of coarse gauge-invariant operator/geometry/representation labels needed to represent the tangent.
3. **Buffered support growth.** Bound the coarse support relative to a frozen reflection plane and positive-half-space buffer.
4. **Mixing plus typed remainder.** Exhibit
   \[
   D_\alpha(V)=\sum_{\beta\in\Gamma(\alpha)}
   M_{\alpha\beta}\,O'_\beta(V)+R_\alpha(V)
   \]
   with the meaning and provenance of every \(M_{\alpha\beta}\) and \(R_\alpha\) explicit.
5. **One-step marked norm loss.** In a declared marked norm \(\|\cdot\|_{\mathrm{mark}}\), register a bound such as
   \[
   \|M_\alpha\|_{\mathrm{mark}}+\|R_\alpha\|_{\mathrm{mark}}
   \le L(g,\ell,\text{geometry})\,\|O_\alpha\|_{\mathrm{mark}},
   \]
   recording all scale, coupling, support, representation and UV-depth dependencies. A one-step bound is not a multiscale summability theorem.

## Fail-closed result branches

- `FINITE_CLOSURE_LEAK`: a generated label lies outside the declared finite marked vocabulary.
- `REFLECTION_SUPPORT_LEAK`: support crosses the frozen reflection buffer or positivity cannot be transported under the proposed geometry.
- `NORM_LOSS`: the one-step constant already carries an uncontrolled scale/UV-depth dependence.
- `TRIVIAL_RESPONSE`: source tangents collapse so the proposed observable interface cannot witness non-triviality.
- `CONTROLLED_GRADED_CLOSURE`: exact finite closure fails but a graded/quasi-local space has explicit mixing, support and remainder budgets.
- `ONE_STEP_PASS_ONLY`: all five coordinates pass for one step; this authorizes a multiscale child problem, not a continuum theorem.

## First discriminator

The cheapest generated-label falsifier is deliberately local. For \(SU(N)\), \(N\ge 3\), integrate one shared link between two adjacent oppositely oriented plaquette factors. If a source mark \(\operatorname{Tr}(AU)\) interacting with \(\operatorname{ReTr}(U^\dagger B)\) produces the concatenated coordinate \(\operatorname{Tr}(AB)\), then a tiny scalar/single-contour marked vocabulary omitting that geometry is not exactly closed.

Candidate `YM-E1a1-C001` tests only this generated-label coordinate. It does **not** test the full Balaban weak-coupling block, a marked norm, reflection-positive support transport, continuum existence, OS reconstruction, correlation decay or a mass gap.

## Promotion boundary

A local failure may justify widening the marked representation. It does not prove marked RG impossible. A local success would likewise not prove multiscale uniformity. The next constructive atom after a finite-vocabulary leak must freeze a fresh context/memory/trace packet for a minimally widened graded/quasi-local marked space before proposing another candidate.
