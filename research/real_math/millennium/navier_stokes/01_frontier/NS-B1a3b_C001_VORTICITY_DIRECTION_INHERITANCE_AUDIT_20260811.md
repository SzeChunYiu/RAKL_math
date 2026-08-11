# NS-B1a3b-C001 — finite `I` does not functionally control vorticity-direction coherence

**Atom:** `NS-B1a3b`  
**Candidate:** `NS-B1a3b-C001-FINITE-I-TO-DIRECTION-COHERENCE`  
**Authority:** `SCOPED_FUNCTIONAL_ROUTE_PRUNING / PROPOSAL_SHADOW / NOT_A_NAVIER_STOKES_COUNTEREXAMPLE / ROOT_AUTHORITY_NONE`  
**Frozen context:** `sha256:ed24b30e6c8b6e6682584c516ca1f2e2e0b30ecc1fca2f738d808c176e7d59e4`  
**Frozen fibre:** `sha256:633eff45bbd8592b80bcb0b260030be2dd609c1472f4e974d432fec21583ebe1`  
**Pre-candidate final event:** `sha256:e2eb8dd0b7a358505d557011c859fffb7fcbaa030768b8a3a1d391fce49ede64`

## Exact scoped question

Can the finite Albritton–Barker information class, viewed only through the scale-invariant local functionals `A+C+D+E`, force a quantitative spatial coherence bound on the normalized vorticity direction `xi=omega/|omega|` strong enough to supply either:

1. a common modulus of continuity on a fixed high-vorticity region, as in the Type-I Giga–Miura criterion; or
2. a uniform local `bmo_{phi}` bound with `phi(r)=1/|log r|`, the direction coordinate used by Grujic `arXiv:2607.08866v2` in its narrower critical-point singularity setting?

A negative answer here prunes only a **finite-I-only a priori estimate**. It does not rule out a Navier–Stokes-dynamics theorem that creates direction coherence.

## Hostile family

Fix smooth cutoffs `psi in C_c^infty(R^3)` and `chi in C_c^infty(R)` with

- `psi = 1` on `B_2` and `supp psi subset B_3`;
- `chi = 1` on a nonempty interval `J subset (-1,0)` and has fixed compact time support.

For integers `N >= 1`, define the vector potential

`A_N(x) = N^{-2} psi(x) (0, cos(N x_1), sin(N x_1))`

and the spacetime packet

`v_N(x,t) = chi(t) curl A_N(x),   q_N(x,t)=0`.

Then `v_N` is smooth, compactly supported, and divergence free identically because it is a curl.

On `B_2 x J`, where both cutoffs are constant,

`v_N = (0, -N^{-1} cos(Nx_1), -N^{-1} sin(Nx_1))`

and therefore

`omega_N = curl v_N = (0, cos(Nx_1), sin(Nx_1))`.

Hence `|omega_N|=1` on this core and

`xi_N = omega_N/|omega_N| = (0, cos(Nx_1), sin(Nx_1))`.

There is no normalization singularity in the tested region.

## Uniform finite-`I` functional ledger

The fixed cutoffs give constants independent of `N` such that

`||v_N||_infinity <= C/N`,  
`||grad v_N||_infinity <= C`.

For any parabolic cylinder `Q_r=B_r(x_0) x (t_0-r^2,t_0)`, fixed spatial and temporal support imply

`A_N(r) <= C N^{-2} r^{-1} min(r^3,1)`,  
`C_N(r) <= C N^{-3} r^{-2} min(r^3,1) min(r^2,1)`,  
`E_N(r) <= C r^{-1} min(r^3,1) min(r^2,1)`,  
`D_N(r)=0`.

Thus for `r<=1` the right sides are respectively `O(N^{-2}r^2)`, `O(N^{-3}r^3)`, and `O(r^4)`; for `r>=1` they are `O(N^{-2}r^{-1})`, `O(N^{-3}r^{-2})`, and `O(r^{-1})`. Therefore

`sup_N sup_{Q_r} [A_N(r)+C_N(r)+D_N(r)+E_N(r)] < infinity`.

The construction has a uniformly bounded finite-`I` **functional** ledger.

This estimate uses no Navier–Stokes evolution equation. In particular `q_N=0` is an auxiliary functional coordinate, not the pressure determined by `v_N` through the NSE.

## Uniform-continuity obstruction

Take, at any `t in J`,

`x_N=(0,0,0)`,  
`y_N=(pi/(2N),0,0)`.

For all sufficiently large `N`, both points lie in `B_2`, `|omega_N|=1`, and

`|x_N-y_N| = pi/(2N) -> 0`

while

`|xi_N(x_N)-xi_N(y_N)| = sqrt(2)`.

Consequently no modulus `eta`, depending only on a uniform finite-`I` bound, can satisfy the Giga–Miura type direction estimate for this information class: it would require `eta(pi/(2N)) >= sqrt(2)` for all large `N`, contradicting `eta(r)->0`.

## Log-weighted BMO obstruction

Let `r_N=pi/N`, with `N` large enough that `r_N<1/2` and `B_{r_N}(0) subset B_2`. On this ball the average of `xi_N` is

`m_N = (0, 3/pi^2, 0)`.

Indeed the cross-sectional weight of the ball at coordinate `x_1` is proportional to `r_N^2-x_1^2`; after `s=Nx_1`,

`average(cos(Nx_1)) = [integral_{-pi}^{pi} cos(s)(pi^2-s^2) ds] / [integral_{-pi}^{pi}(pi^2-s^2) ds] = 3/pi^2`,

and symmetry gives zero sine average.

Since `|xi_N|=1`,

`average |xi_N-m_N|^2 = 1-|m_N|^2 = 1-9/pi^4`.

Also `|xi_N-m_N|<2`, so

`average |xi_N-m_N| >= (1-9/pi^4)/2 =: c_0 > 0`.

For `phi(r)=1/|log r|`, the weighted mean-oscillation term at this one ball is at least

`c_0 / phi(r_N) = c_0 |log(pi/N)| -> infinity`.

Therefore a uniform finite-`I` bound does not give a uniform `bmo_{1/|log r|}` norm of vorticity direction, even on a core where vorticity has fixed nonzero magnitude.

## Diagnosis: derivative/normalization information is missing

The construction identifies the local structural cause rather than merely registering failure. Finite `I` controls a first-derivative velocity energy quantity `grad u` in a scale-invariant spacetime ledger. Direction coherence differentiates

`xi = omega/|omega|`,  `omega=curl u`,

so schematically

`grad xi = (I - xi tensor xi) grad omega / |omega|`.

This carries one additional spatial derivative of `u` and a division by `|omega|`. In the hostile family `|grad v_N|=O(1)` but `|grad xi_N|~N` on the nonzero-vorticity core. No contradiction with finite `I` occurs.

**Scoped diagnosis:** `FINITE_I_DIRECTION_COHERENCE_DERIVATIVE_GAP`.

This is a local functional/a-priori-estimate failure, not a local-to-global gluing failure.

## Separate transfer/gluing failure for the 2026 weighted-BMO route

Grujic `arXiv:2607.08866v2` does not state its weighted-BMO mechanism for every finite-`I` Type-I ancient solution. It assumes a critical-point concentration profile with vorticity scaling like `|x|^{-2}` / `L^{3/2,infinity}` and corresponding high-vorticity superlevel localization, together with the time-uniform weighted-BMO direction hypothesis.

Thus the direct transfer

`finite-I Type-I ancient limit -> Grujic critical-point weighted-BMO trigger`

has **two independent missing interfaces**:

1. the direction-coherence inheritance, for which the finite-I-only functional shortcut is falsified above;
2. the critical-point concentration/scenario inheritance, not supplied by the current finite-I source contract.

This second item is a **transfer/gluing interface failure**, separate from the local derivative-gap failure.

## Source calibration

- Albritton–Barker, `arXiv:1811.00502`: Type-I singularities and finite-`I` mild bounded ancient solutions; source of the active finite-`I` lane.
- Giga–Miura, *Comm. Math. Phys.* 303 (2011), DOI `10.1007/s00220-011-1197-x`, HUPSM 956, Theorem 1.1: a Type-I mild solution does not blow up if a common modulus controls vorticity-direction differences on the region `|omega|>d`.
- Z. Grujic, `arXiv:2607.08866v2` (2026-07-13), Definition 2.1 and Theorem 4.1: critical-point concentration plus `xi in L^infinity_t bmo_{1/|log r|}` produces logarithmic localized stretching depletion. This is a recent preprint and is used here only as a source-bound transfer target, not as independent theorem authority for the Clay root.

## Outcome and residual

**Outcome:** `PARTIAL_SUCCESS / ROUTE_PRUNING`.

Pruned:

`finite I alone -> quantitative vorticity-direction modulus / weighted-BMO control`.

Still live:

`Navier–Stokes dynamics + Type-I structure -> equation-specific direction coherence/depletion`.

The smallest next atom is therefore not “estimate `xi` from `I` more sharply.” It is:

`NS-B1a3b1`: identify a dynamics-specific evolution, high-vorticity-set, vortex-line, or stretching-commutator quantity whose control can be proved from the actual ancient NSE and which supplies a theorem-matched geometric depletion condition without a derivative-loss/circular bootstrap.

Pressure/nonlocality must re-enter at that stage because the present hostile family deliberately does not satisfy the NSE pressure relation.

## Nonpromotion and novelty class

This is not a Navier–Stokes solution family, not a counterexample to any cited regularity theorem, not Type-I exclusion, and not root evidence. Same-context review is not independent review.

For the solved route-pruning subproblem, the defensible RAKL novelty class is `REPRESENTATION_NOVEL` at proposal/shadow scope: the rotating vector-potential hostile representation exposes a derivative-gap interface. This classification is not a mathematical novelty claim and does not count as retained semantic learning until a protected retention gate says so.
