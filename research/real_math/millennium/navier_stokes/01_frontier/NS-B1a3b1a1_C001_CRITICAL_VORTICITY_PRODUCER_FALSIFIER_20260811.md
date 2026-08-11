# NS-B1a3b1a1-C001 — exact Navier–Stokes derivative-trace producer falsifier

**Authority:** `SOURCE_BOUND_EXACT_NS_ROUTE_PRUNING / PROPOSAL_SHADOW / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`

## Exact scoped result

There is no universal same-slab estimate of the form

\[
\sup_{0<t<1}\|\omega(t)\|_{L^{3/2,\infty}(\mathbb R^3)}
\le F(M)
\]

for all smooth whole-space Navier–Stokes solutions whose scale-critical velocity/finite-`I` ledger is bounded by the same number `M`, if no additional frequency, derivative, temporal-history, singular-profile, or geometric hypothesis is supplied.

More concretely, one can construct a sequence of smooth rapidly decaying divergence-free initial data `u_{0,N}` such that:

1. `||u_{0,N}||_{L^3}` is uniformly smaller than the Kato small-data threshold;
2. the resulting exact global smooth Navier–Stokes solutions have a uniform critical velocity bound and therefore a uniform Albritton–Barker finite-`I` bound on the forward slab;
3. nevertheless
   \[
   \sup_{0<t<1}\|\omega_N(t)\|_{L^{3/2,\infty}}\to\infty.
   \]

This prunes only the universal producer edge
`finite I / same-slab critical velocity control -> global critical vorticity amplitude`.
It is not a singular solution, not a counterexample to regularity, and not a proof that extra first-singular-time structure cannot control the vorticity endpoint.

## Exact construction

Fix a nonzero cutoff `eta in C_c^\infty(R^3)` equal to one on
\[
Q=[0,2\pi]\times[-1,1]\times[-1,1].
\]
For integer `N>=1` and a fixed small amplitude `a>0`, set the vector potential
\[
A_N(x)=\left(0,0,\frac{a}{N}\eta(x)\sin(Nx_1)\right)
\]
and
\[
u_{0,N}=\nabla\times A_N.
\]
Then, exactly,
\[
(u_{0,N})_1=\frac aN(\partial_2\eta)\sin(Nx_1),
\]
\[
(u_{0,N})_2=-a\eta\cos(Nx_1)-\frac aN(\partial_1\eta)\sin(Nx_1),
\qquad (u_{0,N})_3=0,
\]
and `div u_{0,N}=0`.

Hence for all `N>=1`,
\[
\|u_{0,N}\|_{L^3}\le
a\Big(\|\eta\|_{L^3}+\|\partial_1\eta\|_{L^3}+\|\partial_2\eta\|_{L^3}\Big)
=:aC_\eta.
\]
Choose `a` so that `a C_eta` is below the small-data threshold in Kato's critical `L^3` theory. The resulting solution is global; the fixed-point estimate gives a critical `L^\infty_tL^3_x` bound depending only on this smallness, hence independent of `N`.

## Vorticity endpoint lower bound

The vorticity is `omega_{0,N}=curl u_{0,N}`. Its third component is
\[
(\omega_{0,N})_3
=aN\eta\sin(Nx_1)-2a(\partial_1\eta)\cos(Nx_1)
-\frac aN(\partial_{11}\eta+\partial_{22}\eta)\sin(Nx_1).
\]
On `Q`, where `eta=1` and its derivatives vanish,
\[
\omega_{0,N}(x)=(0,0,aN\sin(Nx_1)).
\]

For
\[
S_N=\{x\in Q:|\sin(Nx_1)|\ge 1/2\},
\]
integer periodicity gives
\[
|S_N|=\frac{16\pi}{3}.
\]
Using the distribution-function definition of weak `L^{3/2}`,
\[
\|\omega_{0,N}\|_{L^{3/2,\infty}}
\ge \frac{aN}{2}|S_N|^{2/3}
=\frac{aN}{2}\left(\frac{16\pi}{3}\right)^{2/3}.
\]
Thus the critical vorticity norm grows linearly with `N` even though the critical velocity norm stays uniformly small.

Because each datum is smooth and compactly supported, its global small-data solution is classical and converges to its datum in sufficiently high Sobolev norms as `t downarrow 0`. For each fixed `N` there is therefore a positive `t_N<1` for which the vorticity remains arbitrarily close to `omega_{0,N}` uniformly on `Q`. Shrinking the threshold if needed gives
\[
\|\omega_N(t_N)\|_{L^{3/2,\infty}}\ge c_\eta aN.
\]
No uniform-in-`N` lower bound on `t_N` is asserted or needed: the target statement is a supremum over the forward slab.

## Why the finite-I ledger stays uniform

Albritton–Barker define the Type-I ledger from the scale-invariant local quantities `A,C,D,E`. Their weak-Serrin-to-Type-I result explicitly lists `sup_t ||v(t)||_{L^{3,\infty}}` as sufficient for finite `I`. Here the stronger uniform `L^\infty_tL^3_x` bound holds.

The scaling can also be checked directly. Uniform `L^3` control gives, on any parabolic ball of radius `r`,
\[
r^{-1}\int_{B_r}|u|^2\lesssim \|u\|_3^2,\qquad
r^{-2}\int_{t-r^2}^t\int_{B_r}|u|^3\lesssim \|u\|_{L^\infty_tL^3_x}^3.
\]
With `p=R_iR_j(u_i u_j)`, Calderon–Zygmund boundedness gives a uniform global `L^{3/2}` pressure bound and therefore the corresponding `D` estimate after subtraction of a spatial mean. The local energy inequality then controls `E` from the same scale-invariant data. The constants depend on the fixed small critical velocity bound, not on `N`.

This is exactly the interface stressed by the counterexample: the integrated one-derivative term inside `I` does not furnish an `L^\infty_t` endpoint trace of that derivative.

## Scaling, pressure, endpoint and circularity audit

- **Scaling:** `L^3` velocity and `L^{3/2,\infty}` vorticity are both critical under Navier–Stokes scaling, so dimensional mismatch does not explain the failure. The missing information is derivative/frequency trace control.
- **Units:** the construction keeps velocity amplitude `O(a)` while placing frequency `N` in a fixed physical region; vorticity amplitude is therefore `O(aN)`.
- **Endpoint:** finite `I` contains spacetime `L^2` gradient information, not a uniform-time global weak-`L^{3/2}` curl trace. The example concentrates derivative size into a rapidly dissipating temporal layer.
- **Pressure:** pressure is controlled by the critical velocity through Riesz transforms for the finite-`I` certificate. Taking curl removes pressure from the vorticity equation, so pressure is not the local obstruction here.
- **Nonlocality:** strain remains a nonlocal singular-integral transform of vorticity. Nothing in this calibration supplies Grujic's phase/far-field hypotheses.
- **Derivative loss:** this is the active obstruction: zero-order critical velocity control does not control a one-derivative critical time trace.
- **Circular bootstrap:** a proof may not assume a frequency envelope, vorticity trace, or geometric depletion equivalent to the missing consumer input in order to claim that finite `I` generated it.

## Analogue and DifferenceWitness audit

The closest solved analogue is Kato's exact whole-space small-critical-data theory. It is used only to ensure the calibration family consists of genuine Navier–Stokes solutions, not arbitrary divergence-free fields.

The closest consumer is Grujic v2, whose Theorem 4.1 assumes uniformly near a first possible singular time both global `L^{3/2,\infty}` vorticity and global log-weighted BMO direction, in addition to the critical-point profile. Those are extra inputs.

The transfer is intentionally one-sided. The calibration family is globally regular and its large vorticity is inherited from high-frequency initial data. A first-singular-time route may possess additional one-sided history, profile localization, no-recrossing, or frequency information. Therefore the result does **not** establish
`finite I near a singular time can never imply vorticity endpoint control`.
It establishes only that such a theorem cannot be a consequence of the finite-`I`/critical-velocity ledger alone.

## Same-context expert cell

- `EX-NS-PDE-SCALING`: verified divergence-free construction, critical `L^3` uniformity, source-matched small-data solution and finite-`I` scope.
- `EX-NS-HARMONIC-VORTICITY`: verified the curl formula, exact positive-measure weak-Lorentz lower bound, and identified the obstruction as derivative time-trace rather than pressure.
- `EX-NS-COMPACTNESS`: accepted the route pruning only with the explicit first-singular-time/history DifferenceWitness; rejected extrapolation to singular profiles.
- `EX-RAKL-ADVERSARIAL`: rejected root or Type-I promotion and required local producer failure to remain separate from global/far-field and pre-singularity/ancient gluing.

These are same-context roles and count as `0/3` genuinely isolated mathematical reviews.

## Failure separation

**Local mathematical producer failure**
`F-NS-B1a3b1a1-FINITE-I-NO-CRITICAL-VORTICITY-TRACE`:
the finite-`I` / same-slab critical-velocity ledger does not universally control the global uniform-time critical vorticity amplitude.

**Local-to-global/gluing failures, unchanged and separate**
`F-NS-B1a3-UNCONTROLLED-FAR-FIELD` and
`F-NS-B1a3-LOCAL-GLOBAL-INTERFACE-MISMATCH` remain open. This cycle does not repair them.

**Source/state-space DifferenceWitness, unchanged**
Grujic's consumer is a first-singular-time pre-singularity theorem; the ancient-limit and producer interfaces remain separate.

## Episode -> diagnosis -> obstruction/lesson

**Episode:** test an exact Navier–Stokes high-frequency family under a frozen finite-`I` versus critical-vorticity discriminator.

**Diagnosis:** the universal producer fails because finite `I` controls an integrated derivative ledger but not a global `L^\infty_t` critical derivative trace. Scale compatibility alone does not repair this.

**Reusable obstruction/lesson:** a downstream consumer requiring a critical derivative endpoint cannot be advertised as generated by a zero-order critical producer merely because both quantities are scale invariant. Require an explicit frequency/history/trace mechanism and test it independently.

The solved route-pruning subproblem is classified `compositional`, structural rank `0`: it composes Kato small-data existence/control, the Albritton–Barker finite-`I` implication, and an explicit oscillatory vector-potential construction. It is not a novelty claim about the Navier–Stokes root problem.

## Outcome and next action

**Outcome:** `PARTIAL_SUCCESS / EXACT_NS_UNIVERSAL_AMPLITUDE_PRODUCER_PRUNED / PROFILE_HISTORY_ROUTES_OPEN`.

The Grujic producer route should receive no further budget from interpolation or finite-`I` bookkeeping alone. A successor must name genuinely new structure: for example a frequency-envelope monotonicity, positive-distance parabolic smoothing bound with singular-time-compatible constants, no-recrossing/persistence mechanism, or a source-matched singular-profile theorem. Otherwise rotate to the orthogonal pressure-temporal/no-recrossing child.

**Root status:** `OPEN_NO_SOLUTION_CERTIFICATE`.

## Primary-source provenance

- Tosio Kato, *Strong L^p-Solutions of the Navier-Stokes Equation in R^m, with Applications to Weak Solutions*, Math. Z. 187 (1984), 471–480, DOI `10.1007/BF01174182`; digitized primary text: `https://gdz.sub.uni-goettingen.de/fulltext/PPN266833020_0187/00000479`.
- Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:`1811.00502v2`, J. Math. Fluid Mech. 21 (2019), 43.
- Zoran Grujic, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:`2607.08866v2`, 13 July 2026.
- RAKL framework subject: `34e0e24844dfb322eae3a5c639adc12713065f54`, method `3.0.0`.
- RAKL_math base: `47f56df0492339097a651d40b6c7289c4e2d4034`.
