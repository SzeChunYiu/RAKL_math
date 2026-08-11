# NS-B1a2-C001 hostile audit — compactness and self-similar-time drift

**Authority:** `ROUTE_PRUNING / LOGICAL_AND_SOURCE_INTERFACE_AUDIT / NO_NEW_NAVIER_STOKES_THEOREM / ROOT_AUTHORITY_NONE`  
**Atom:** `NS-B1a2`  
**Frozen pre-candidate trace:** `NS-B1a2-PRE-20260811`  
**Current framework inspected before execution:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`

## Registered question

Can finite Type-I local scale-invariant control plus compactness/minimality of a renormalized ancient orbit force one sufficiently late self-similar time at which the scaling-generator drift is small enough to activate a source-valid near-self-similarity regularity criterion?

The audit deliberately tests only the **compactness/averaging bridge**. It does not assume or prove that every finite-`I` ancient Navier–Stokes orbit is precompact.

## Source interface

Pineau–Vicol v2, arXiv:2607.09619v2, Theorem 1.9 gives a local regularity criterion for a smooth solution on `B_1 x [-1,0)` under three load-bearing inputs:

1. the pointwise Type-I velocity bound `|u(x,t)| <= C_u/(sqrt(-t)+|x|)`;
2. a uniform pressure bound on the fixed annulus `1/2<|x|<3/4`;
3. at one sufficiently late time, smallness of the scaling generator.

In self-similar variables `U(y,s)=sqrt(-t)u(x,t)`, `s=-log(-t)`, the third condition is exactly smallness of `partial_s U` on an expanding ball. Remark 1.11 permits a weaker Gaussian-weighted `L^1` smallness condition for `partial_s U`.

This gives a precise downstream discriminator. It does **not** say that finite Albritton–Barker `I` supplies any of the three inputs.

## Falsifier 1 — compactness does not imply small instantaneous drift

The abstract trajectory `z(s)=(cos s,sin s)` in `R^2` has compact range, but

`|z'(s)|=1`

for every `s`.

Therefore the functional implication

`precompact orbit -> exists s_n -> infinity with ||z'(s_n)|| -> 0`

is false without an additional dynamical assumption.

This is a logical/dynamical counterexample only. It is not a Navier–Stokes solution and creates no PDE theorem.

The consequence for `NS-B1a2` is exact: even if a future concentration-compactness argument produced precompactness of the finite-`I` renormalized orbit (possibly modulo symmetries), **precompactness alone cannot activate Pineau–Vicol's one-slice generator-smallness criterion**.

## Falsifier 2 — small average vector increment does not imply small drift norm

For any sufficiently regular Banach-valued trajectory,

`(1/T) integral_S^(S+T) partial_s U ds = (U(S+T)-U(S))/T`.

If the trajectory is bounded, the norm of the left-hand **vector average** can become small as `T` grows. But this does not imply

`(1/T) integral_S^(S+T) ||partial_s U|| ds -> 0`

and does not supply a time with small `||partial_s U||`.

The circle control is again decisive: over every complete period the vector average of `z'` is exactly zero while `|z'|=1` identically.

Thus a long-time endpoint estimate or recurrence identity cannot be silently upgraded into the norm smallness required by the regularity criterion.

## Falsifier 3 — averaging the nonlinear equation does not produce a stationary Leray profile

For a non-rotated self-similar-time solution,

`partial_s U + (1/2)U + (1/2)(y·grad)U - Delta U + (U·grad)U + grad P = 0`.

Write `U=Ubar+U'`, where `Ubar` is a time average and `overline(U')=0`. Averaging over a finite interval yields an endpoint term plus

`div overline(U tensor U) = div(Ubar tensor Ubar) + div overline(U' tensor U')`.

The second term is a Reynolds/fluctuation stress. It is not controlled merely because the endpoint increment divided by the averaging time is small. Therefore the time-averaged profile does not solve the stationary Leray equation unless one separately controls the fluctuations.

This blocks the shortcut

`bounded recurrent self-similar-time orbit -> average -> stationary profile -> apply fixed-profile Liouville theorem`.

## Calibration 4 — the simplest fixed Gaussian energy is not an automatic Lyapunov function

For a smooth sufficiently Gaussian-integrable calibration profile, multiply the non-rotated self-similar-time equation by `rho U`, with `rho(y)=exp(-|y|^2/4)`, and integrate. The drift and Gaussian integration-by-parts terms cancel so that

`(1/2) d/ds integral rho |U|^2 + integral rho |grad U|^2 + (1/2) integral rho |U|^2 = -(1/4) integral rho |U|^2 (U·y) -(1/2) integral rho P (U·y)`.

The convection and pressure terms have no fixed sign at this level. This calculation is a **route calibration**, not a claim that no more sophisticated adjoint or vorticity-weighted monotone quantity exists. Pineau–Vicol's successful weighted estimates use more structured weights and source-specific arguments.

The only conclusion licensed here is that the most naive fixed Gaussian velocity energy cannot simply be declared a Lyapunov budget for a general renormalized orbit.

## Source-valid structural near-miss — periodic self-similar-time profiles

Pineau–Vicol write DSS/RDSS solutions as profiles periodic in self-similar time. Their RDSS theorem excludes specified parameter regimes when the self-similar period is sufficiently small (with additional rotation restrictions), and their discussion treats these solutions as breather-like scenarios.

This reinforces the logical audit: recurrence/periodicity is a genuine orbit class. It is not the same object as a fixed point, and converting it into near-stationarity requires quantitative structure such as a small period or another controlled defect.

## Disposition

The following route is rejected:

`finite-I -> (hypothetical) precompact renormalized orbit -> compactness/long-time averaging alone -> one-slice small ||partial_s U|| -> Pineau-Vicol regularity`.

The rejection is scoped to the words **compactness/long-time averaging alone**.

The following routes remain open:

- derive a finite total-variation or finite-dissipation quantity in self-similar time;
- construct a genuine Lyapunov/monotone defect under the exact finite-`I` class;
- prove a no-recurrence/no-breather statement under inherited hypotheses;
- obtain direct smallness of the scaling generator from a source-valid PDE estimate;
- control a modulation parameter so that quotient-orbit drift becomes small;
- bypass generator smallness with the Albritton–Barker global-`L^3` sequence trigger or another exact Liouville theorem.

Separately, Pineau–Vicol's pointwise Type-I and annular-pressure hypotheses remain unresolved at finite `I`; these interface questions overlap the already-open `NS-B1b1` source/transfer audit and should not be duplicated here.

## New residual

`NS-B1a3`: identify the weakest **sign-controlled or finite-variation self-similar-time defect** inherited from the finite-`I` Type-I ancient class that can force `liminf` one-slice drift smallness, or prove that the selected candidate defect is not controlled. Keep the pointwise-Type-I/annular-pressure transfer as a separately linked interface obligation.

No candidate theorem is proposed by this audit.
