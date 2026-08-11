# NS-B1a-C001 — critical-Morrey pressure-tail localization

**Atom:** `NS-B1a` — dynamics-specific Type-I trace/tail bridge  
**Candidate:** `NS-B1a-C001`  
**Authority:** `SOURCE_BOUND_DERIVED_CALIBRATION / VERIFIED_LOCAL_ANALYTIC_STEP_IF_RECHECKED / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`  
**Targeted mechanism:** raw instantaneous far-field pressure divergence as an anti-replication mechanism.

## Why this candidate is allowed now

The strict `NS-B1a` context, analogy/method-transfer review, six-role same-context expert review, dual-memory review and seven-event pre-candidate trace were frozen before this candidate. The migrated application regression reconstructs those artifacts and passes `plan_math_research`.

The application submodule is pinned to `RAKL@7853ec0c4ff8f862359835bca1af1d934bfbd887`. At candidate time, current framework main is `RAKL@55d4cb0a83f271d3263fbe48f99b173119c732d2`. The intervening framework-repository commits implement the framework/application split; the comparison contains no changes to the mathematical-research runtime, context/memory/trace schemas, or pre-candidate gate used by this atom. This is a freshness audit, not theorem evidence.

## Source boundary

Load-bearing sources:

- Albritton–Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502: Type-I ancient class, the scale-invariant quantities `A,C,D,E`, and the backward-`L^3`-sequence Liouville trigger.
- Bradshaw–Tsai, *On the local pressure expansion for the Navier-Stokes equations*, arXiv:2001.11526: pressure localization for whole-space distributional/mild solutions and the need to treat pressure with the correct local/far-field representation.
- Lei–Yang–Yuan, *Backward Uniqueness for 3D Navier-Stokes Equations with Non-trivial Final Data and Applications*, arXiv:2311.02429: a distinct bounded-mild backward-uniqueness route involving Calderón–Zygmund terms. It is an alternative downstream route, not used to prove the estimate below.

No novelty claim is made. The estimate below is a standard dyadic Calderón–Zygmund/Morrey calculation specialized as a route discriminator.

## Frozen question

The parent calibration showed that local Type-I functionals can remain bounded on an arbitrary divergence-free sparse bump train while every time slice has infinite global `L^3`. That example is not a Navier–Stokes solution.

The first dynamics-specific question was therefore:

> Could the nonlocal pressure coupling itself prohibit infinitely replicated distant packets because their instantaneous pressure contribution necessarily diverges?

This candidate tests that mechanism before attempting a universal Type-I-to-`L^3` theorem.

## Exact local statement

Fix a time `t` and define the energy measure

\[
\mu_t(E)=\int_E |v(y,t)|^2\,dy.
\]

Assume the scale-critical Morrey growth

\[
M_t:=\sup_{x\in\mathbb R^3,\ r>0}
\frac{1}{r}\mu_t(B(x,r)) \le M <\infty.
\]

Let `K_ij(z)` denote the Hessian kernel of the Newtonian potential, so away from the origin

\[
|K(z)|\le c_0 |z|^{-3},
\qquad
|\nabla K(z)|\le c_1 |z|^{-4}.
\]

For `R>0`, consider only the absolute far-field quadratic stress contribution

\[
P_{>R}(x,t)
:=
\int_{|y-x|>R}
K_{ij}(x-y)v_i(y,t)v_j(y,t)\,dy .
\]

Then

\[
|P_{>R}(x,t)|
\le \frac{8}{3} c_0 M R^{-2}.
\]

Likewise, for the first kernel derivative,

\[
\int_{|y-x|>R}
|\nabla K(x-y)|\,|v(y,t)|^2\,dy
\le \frac{16}{7} c_1 M R^{-3}.
\]

For a finite-`I` ancient solution, the `A` component of the registered Type-I quantity supplies this Morrey energy bound on the relevant time slices, with `M` controlled by `I`.

## Derivation

Partition the far field into dyadic shells

\[
S_k=\{2^kR<|y-x|\le 2^{k+1}R\},\qquad k\ge0.
\]

On `S_k`,

\[
|K(x-y)|\le c_0(2^kR)^{-3}.
\]

The Morrey bound gives

\[
\mu_t(S_k)
\le
\mu_t(B(x,2^{k+1}R))
\le
M\,2^{k+1}R.
\]

Therefore

\[
\begin{aligned}
\int_{S_k}|K(x-y)|\,|v(y,t)|^2\,dy
&\le
c_0(2^kR)^{-3}M\,2^{k+1}R\\
&=
2c_0M\,2^{-2k}R^{-2}.
\end{aligned}
\]

Summing,

\[
\sum_{k\ge0}2^{-2k}=\frac{4}{3},
\]

hence

\[
|P_{>R}(x,t)|
\le
\frac{8}{3}c_0MR^{-2}.
\]

For `|\nabla K(z)|\le c_1|z|^{-4}` the same calculation yields shell cost

\[
2c_1M\,2^{-3k}R^{-3},
\]

and

\[
\sum_{k\ge0}2^{-3k}=\frac{8}{7},
\]

giving the stated `16/7` bound.

No cancellation, compact support, finite packet count, global `L^3`, or orbit compactness is used.

## Scaling audit

The quantity

\[
\sup_{x,r} r^{-1}\int_{B(x,r)}|v|^2
\]

is invariant under the Navier–Stokes scaling. The pressure-tail bound scales like `R^{-2}`, matching pressure, and the kernel-gradient bound scales like `R^{-3}`. No dimensional mismatch is introduced.

## Falsifier result

The attempted mechanism was:

> infinitely replicated distant critical packets should force divergent instantaneous nonlocal pressure, thereby ruling out the sparse-tail scenario.

The worst-case sign-free dyadic sum **converges geometrically** under the exact critical Morrey energy growth already available from `A`.

Therefore the proposed *raw pressure-divergence anti-replication mechanism* fails inside this registered scope.

This does **not** construct a Navier–Stokes sparse-tail solution. It only shows that the available Type-I Morrey energy bound is already strong enough to make the distant quadratic pressure stress absolutely summable, so mere nonlocality/divergence cannot be the missing bridge.

## What remains live

Pressure is not globally discarded. The calculation leaves open:

- local/singular and harmonic parts of the pressure representation;
- pressure–velocity sign/coherence effects;
- time-integrated pressure work in the local-energy inequality;
- transport of critical mass between shells;
- diffusion/advection constraints on long-lived packet replication;
- backward uniqueness or unique-continuation mechanisms;
- minimality/almost-periodicity if independently derived.

The result therefore shifts the active obstruction from **instantaneous spatial accumulation** to **temporal/coherent dynamics**.

## Next child atom

`NS-B1a1` — **pressure-aware temporal shell-flux anti-replication**:

> For a mild bounded ancient Navier–Stokes solution with finite `I`, does the time-integrated local-energy balance across expanding dyadic shells yield any scale-decaying, telescoping, or otherwise summable quantity that prevents persistent replicated critical mass without assuming global `L^3`, compact support, fixed/DSS orbit structure, or a pre-existing critical-element theorem?

The first pre-candidate audit for `NS-B1a1` must explicitly test the hostile possibility that the available local-energy bounds charge `O(1)` per dyadic scale, in which case summing infinitely many shells still fails.

## Non-promotion boundary

This result is not:

- `I<∞ -> L^3` along a backward sequence;
- a Liouville theorem;
- exclusion of Type-I blow-up;
- exclusion of Type-II blow-up;
- a Clay solution;
- a novelty certificate.

It is a bounded route-pruning calculation and a sharper residual.
