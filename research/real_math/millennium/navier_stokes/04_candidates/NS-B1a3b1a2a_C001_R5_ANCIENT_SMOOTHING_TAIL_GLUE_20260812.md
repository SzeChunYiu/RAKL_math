# NS-B1a3b1a2a R5 — ancient smoothing versus global critical-vorticity gluing

**Authority:** proposal/shadow only. **Root:** `OPEN_NO_SOLUTION_CERTIFICATE`. **Independent mathematical review:** `0/3`. This record advances only the scoped discriminator frozen in RAKL_math issue #221. It is not a Type-I exclusion, a Navier–Stokes regularity theorem, or a Clay certificate.

## Exact source-bound state

Let `u` be a nontrivial whole-space 3D incompressible mild bounded ancient Navier–Stokes solution on `R^3 x (-infinity,0)` in the Albritton–Barker Type-I source class, with

`M := ||u||_{L^infinity(R^3 x (-infinity,0))} < infinity`

and finite

`I := sup_Q (A(Q)+C(Q)+D(Q)+E(Q)) < infinity`,

where in particular `E(Q(z,R)) = R^{-1} integral_{Q(z,R)} |grad u|^2`.

Primary provenance:

- Koch–Nadirashvili–Seregin–Sverak, arXiv:0709.3599, especially the mild formulation, Proposition 4.1 bounded-data smoothing, and the Section 6 definition of bounded ancient mild solutions: https://arxiv.org/abs/0709.3599
- Albritton–Barker, arXiv:1811.00502v2, Theorem 1.1 and definitions (1.1)–(1.5) of `A,C,D,E,I`: https://arxiv.org/abs/1811.00502v2
- Grujic, arXiv:2607.08866v2, Definition 2.1 and Theorem 4.1 for the selected critical-point geometric-depletion consumer: https://arxiv.org/abs/2607.08866v2

## Proposition A — genuine ancientness closes the local derivative interface

For every pair of nonnegative integers `(k,l)` there is a source-dependent constant `C_{k,l}` such that

`|| grad^k partial_t^l u(t) ||_infinity <= C_{k,l} M^{k+2l+1}`

for every `t<0`. In particular,

`||omega(t)||_infinity <= C M^2`,

`||grad omega(t)||_infinity <= C M^3`,

and

`||partial_t omega(t)||_infinity <= C M^4`.

### Verification

If `M=0`, the assertion is trivial. Assume `M>0`. The ancient-mild definition in Koch et al. supplies times `T_j -> -infinity` such that on each `(T_j,0)` the solution is the mild Cauchy solution from `u(T_j)`. Fix `t_0<0`. Choose a source-admissible smoothing depth

`delta = theta_{k,l} M^{-2}`

with `theta_{k,l}>0` small enough for Proposition 4.1, and choose `j` so that `T_j < t_0-delta`. The mild Duhamel formula and the heat/Stokes semigroup property allow the same solution on `(T_j,0)` to be restarted from the intermediate time `s=t_0-delta`; this does not add a pressure hypothesis. Since `||u(s)||_infinity <= M`, Proposition 4.1 applied to the restarted problem gives

`delta^{k/2+l} ||grad^k partial_t^l u(t_0)||_infinity <= C_{k,l} M`.

Substituting `delta ~ M^{-2}` yields `M^{k+2l+1}`. For vorticity, use `omega=curl u` and the corresponding derivative orders. The bound is dimensionally consistent with Navier–Stokes scaling.

**Scoped outcome:** `ANCIENT_LOCAL_SMOOTHING_BOUND`.

## Direct global-glue probe — persistent superlevel packing

The remaining producer question is global: whether the local derivative bounds plus finite `I` force a uniform-in-time global weak-`L^{3/2}` bound for vorticity.

Fix `t<0` and a threshold `a>0`. For `a` above a constant multiple of `M^2`, Proposition A makes the superlevel set empty. For `0<a<=c M^2`, let

`S_{2a}(t) := {x : |omega(x,t)| > 2a}`.

At any `x in S_{2a}(t)`, Proposition A implies persistence on a short space-time cylinder. Taking

`r = c_1 a M^{-3}`, `tau = c_2 a M^{-4}`

with sufficiently small universal/source constants gives

`|omega(y,s)| >= a`

for `y in B_r(x)` and `s in [t-tau,t]`, because spatial and temporal variation are bounded by `C M^3 r + C M^4 tau`.

Fix a center `x_0` and an observation radius `R >= max(r,sqrt(tau))`. A maximal disjoint collection of radius-`r/2` balls centered in `S_{2a}(t) cap B_R(x_0)` has cardinality `N`; the corresponding persistence cylinders are spatially disjoint and lie inside a constant-factor enlargement of `Q((x_0,t),R)`. Since `|curl u|^2 <= C |grad u|^2` and finite `I` gives a radius-linear spacetime dissipation budget,

`N * c a^2 r^3 tau <= C I R`.

Vitali covering then yields the source-valid direct estimate

`|S_{2a}(t) cap B_R(x_0)| <= C I R /(a^2 tau) <= C I M^4 R a^{-3}`.

The units are correct: the right side has spatial-volume dimension. This is a **local Morrey-style superlevel-growth certificate**, not a global Lorentz bound.

## Exact obstruction

The direct bridge retains an uncancelled factor of the observation radius `R` and an `a^{-3}` distribution exponent. Sending `R -> infinity` therefore does not produce a finite global distribution function, much less the `a^{-3/2}` scaling needed for a uniform weak-`L^{3/2}` vorticity bound. This verifies only that the natural route

`ancient L-infinity smoothing + finite-I E ledger + persistent-superlevel packing`

is insufficient by itself to discharge the global Lorentz consumer coordinate. It does **not** prove that an exact finite-`I` ancient Navier–Stokes solution cannot satisfy the global Lorentz bound; an equation-specific tail/no-dichotomy mechanism may still do so.

**Scoped outcome:** `ANCIENT_LOCAL_SMOOTHING_BOUND / GLOBAL_LORENTZ_GLUE_OPEN`.

## Interface audit

- **Weak/strong convergence:** no new compactness limit is used in this R5 proposition. The Albritton–Barker source-class relation is input provenance, not re-proved here.
- **Pressure localization:** Proposition A uses the pressure-free mild formulation; the packing probe uses the `E` component only. No pressure estimate closes the spatial tail. Pressure/harmonic far-field control remains downstream for any suitable-solution gluing or rigidity step.
- **Far field / noncompact symmetries:** translation multiplicity and spatial tail remain live. Ancientness removes the finite-left-endpoint temporal-edge separator but does not compactify space.
- **Dilation:** the derivative exponents are exactly scale-covariant. No dimensional history parameter is mistaken for a critical invariant.
- **Grujic-v2 consumer completeness:** global weak-`L^{3/2}` amplitude is only one consumer coordinate. The selected v2 route also requires the registered critical-point profile / one-center concentration morphology and logarithmically weighted BMO control of vorticity direction. Proposition A produces neither.
- **Backward uniqueness:** not invoked; terminal/global hypotheses have not been produced.
- **Equation changes:** none. No Euler or stationary-Leray theorem is imported. Type II remains a separate sibling lane.
- **Numerics:** none used.

## DifferenceWitnesses and negative history

The fixed-finite-history R4 shadow separator cannot refute Proposition A: every finite history interval can be parabolically renormalized, whereas an ancient solution has no finite left endpoint. Conversely, Proposition A does not repair the previously recorded local-to-global critical-state-space failure: bounded derivatives are local amplitude information and do not supply global tail tightness, profile-count control, or the exact global critical orbit compactness used by critical-element methods. Cross-problem/root-bridge experience is retained only as routing analogy; no cross-Millennium theorem is transferred.

## Next atomic residual

`NS-B1a3b1a2a1`: **equation-specific ancient tail/no-dichotomy discriminator**. Freeze before work an exact question asking whether the finite-`I` ancient NSE dynamics supply a radius-uniform vorticity distribution/tightness certificate, a backward-sequence global critical bound, or a one-center/no-multiplicity mechanism that improves the radius-dependent estimate above. Counterexample-first probes must remain exact NSE; non-solution blob arrays can calibrate representation only.

Root authority remains `NONE`.
