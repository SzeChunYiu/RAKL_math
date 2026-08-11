# NS-B1a4-C001 — pressure-zero local-energy recrossing calibration

**Authority:** proposal/shadow route diagnostic only.  
**Prospective target:** RAKL_math issue #173.  
**Pre-action branch head:** `cbe469d409ebcad783ea8f72904686e494136ec2`.  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`; independent mathematical reviews `0/3`.

## Exact question

Test whether the standard local-energy balance and pressure localization have an intrinsic one-sided temporal sign before spending effort on a finite-`I` pressure/no-recrossing theorem. This is deliberately narrower than the root-facing finite-`I` ancient claim.

## Exact smooth Navier–Stokes calibration

Normalize viscosity to `nu=1`. Put `s=1+t` and, for `t>-1`,

\[
f(y,t)=(4\pi s)^{-1/2}\exp\!\left(-\frac{(y-3)^2}{4s}\right),\qquad
u(x,t)=(f(x_2,t),0,0),\qquad p(x,t)=0.
\]

Then `div u=0`, because `f` is independent of `x_1`. Also

\[
(u\cdot\nabla)u=f\,\partial_1u=0,
\qquad
\partial_tu-\Delta u=(f_t-f_{yy},0,0)=0,
\]

because `f` is the one-dimensional heat kernel translated to `y=3`. Hence `(u,p)` is an exact smooth incompressible Navier–Stokes solution on `R^3 x (-1,infinity)`.

## Strict local energy increase with zero pressure

The squared profile is

\[
f(y,t)^2=(4\pi s)^{-1}\exp\!\left(-\frac{(y-3)^2}{2s}\right),
\]

so

\[
\partial_t f^2
=f^2\left[-\frac1s+\frac{(y-3)^2}{2s^2}\right]
=f^2\frac{(y-3)^2-2s}{2s^2}.
\]

For `|y|<=1` we have `|y-3|>=2`. Therefore, for `0<=t<1` (equivalently `1<=s<2`),

\[
(y-3)^2-2s\ge 4-2s>0.
\]

Let `phi` be any nonzero, nonnegative, smooth radial cutoff supported in `B_1`. Then

\[
E_\phi(t)=\frac12\int_{\mathbb R^3}|u(x,t)|^2\phi(x)\,dx
\]

satisfies

\[
E_\phi'(t)=\frac12\int \partial_t f(x_2,t)^2\,\phi(x)\,dx>0,
\qquad 0\le t<1.
\]

Thus localized kinetic energy can strictly increase for an exact smooth solution even though `p` vanishes identically.

For a radial cutoff, the convective cutoff flux also vanishes exactly:

\[
\int |u|^2u\cdot\nabla\phi\,dx
=\int f(x_2,t)^3\,\partial_1\phi(x)\,dx=0,
\]

by oddness in `x_1`. The pressure-work term is zero because `p=0`. The increase is therefore reconciled by viscous/cutoff boundary transport in the local energy equality, not by pressure or convection. This directly defeats any claim that pressure magnitude/nonlocality is the universal source of one-sided local-energy behavior.

## Hard DifferenceWitness: this is not a finite-I ancient counterexample

The solution is independent of `x_1,x_3`. It has infinite global kinetic energy. More specifically, at a fixed interior time, for large balls centered at the origin,

\[
\int_{B_r}|u|^2\,dx \sim c(t)r^2,
\]

because the `x_1,x_3` cross-section has area of order `r^2` across the fixed `x_2` heat profile. Consequently the Albritton–Barker scale quantity

\[
A(r)=r^{-1}\operatorname*{ess\,sup}_t\int_{B_r}|u|^2
\]

grows like `c(t) r`, so the global finite-`I` source contract fails already in `A`.

Therefore this calculation **does not refute** a theorem that derives no-recrossing from the full global finite-`I` ancient structure. It proves only that the generic smooth/local-suitable local-energy identity plus pressure localization carries no intrinsic local monotonicity of the required kind. A positive finite-`I` theorem must use a genuinely finite-`I`-specific global/trajectory mechanism or add a signed observable (for example a signed flux/correlation, a bounded-variation/Lyapunov defect, or a no-return quantity).

## Scaling, endpoints, pressure and circularity audit

- The observation interval `[0,1)` is strictly inside the smooth existence interval `(-1,infinity)`; no temporal-edge trace is used.
- The sign inequality is strict for every point in `B_1` and every `0<=t<1`; no limiting equality is used.
- Pressure is exactly zero, so harmonic/far-field pressure normalization cannot hide a sign contribution in this calibration.
- The nonlinear transport is exactly zero in the PDE and its radial-cutoff flux integrates to zero.
- No derivative estimate is bootstrapped from `A+C+D+E`; the calculation is an exact solution identity, so there is no derivative-loss or circular regularity step.
- Under Navier–Stokes parabolic scaling the local calibration can be rescaled, but its global `A` divergence persists as a source-family mismatch rather than becoming a finite-`I` example.

## Source boundary

Primary source used for the root-facing Type-I state space: Albritton–Barker, arXiv:1811.00502, which characterizes local Type-I singularities through nontrivial mild bounded ancient solutions with finite Type-I control and separately supplies an ancient `L^3`-sequence Liouville theorem. Current orthogonal rigidity analogue: Pineau–Vicol, arXiv:2607.09619v2 (revised 2026-08-06), whose local criterion uses additional Type-I/approximate-self-similarity structure rather than asserting monotonicity from the bare magnitude ledger.

## Scoped outcome

`EXISTING_LEDGER_SIGN_INSUFFICIENT_ROUTE_PRUNING`, with the qualification **generic local-balance sign only**.

Local mathematical failure:

`F-NS-B1a4-GENERIC-LEI-PRESSUREZERO-NO-MONOTONICITY`.

Separate gluing/source-state residual:

`G-NS-B1a4-LOCAL-SHEAR-TO-FINITE-I-ANCIENT`.

Reusable proposal/shadow obstruction:

`O-NS-B1a4-MAGNITUDE-LEDGER-MISSING-SIGNED-TEMPORAL-COORDINATE`.

The next discriminator is not another pressure-magnitude estimate. It is to test a **finite-I-specific** signed annular flux/trajectory quantity or bounded-variation/no-return defect whose total budget is invariant under scaling and whose sign survives moving centers, pressure localization and ancient-limit passage. If no such source-valid observable can be constructed, rotate to a different exact rigidity consumer rather than treating local pressure as a monotone surrogate.
