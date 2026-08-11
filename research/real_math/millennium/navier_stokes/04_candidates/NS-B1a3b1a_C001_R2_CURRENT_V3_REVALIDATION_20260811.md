# NS-B1a3b1a-C001 R2 — current-v3 revalidation of the finite-I time-trace falsifier

Authority: `PROPOSAL_SHADOW_SCOPED_FALSIFIER / NO_ROOT_AUTHORITY`.

Framework subject: `SzeChunYiu/RAKL@787c7e00af2a5877ccb715bc807ec14f52974e9c` (`RAKL` method `3.0.0`, package `0.1.0`).
Application root: `RAKL_math#4`, status `OPEN_NO_SOLUTION_CERTIFICATE`.
Atom: `NS-B1a3b1a`, child of `NS-B1a3b1`.
Prospective R2 discriminator: official `PreActionFibreReceipt` hash `32334e7e308b49bdf56c9c52f20e750da35e3239d86709052cc532cc17d2504f`.

## Exact scoped question

The source-bound local Type-I bookkeeping uses, for each parabolic subcylinder `Q(z,r)`,

\[
 A=r^{-1}\operatorname*{ess\,sup}_t\int_{B_r}|u|^2,\qquad
 C=r^{-2}\int_{Q_r}|u|^3,\qquad
 D=r^{-2}\int_{Q_r}|p-[p]_{B_r}|^{3/2},\qquad
 E=r^{-1}\int_{Q_r}|\nabla u|^2.
\]

Albritton–Barker define `I` by the supremum of `A+C+D+E` over subcylinders and prove the suitable-weak-solution Type-I/finite-`I` ancient-solution equivalence. The present atom tests only whether the **numerical functional signature itself**, without using the Navier–Stokes equation, has a bounded map into the time-uniform vorticity inputs appearing in the selected Grujić v2 consumer: `L_t^∞ L_x^{3/2,∞}` amplitude and `L_t^∞ bmo_{1/|log r|}` direction.

Primary source anchors rechecked on 2026-08-11:
- Albritton–Barker, arXiv:1811.00502v2, Theorem 1.1 and equations (1.1)–(1.6).
- Z. Grujić, arXiv:2607.08866v2 (13 July 2026), Definition 2.1, equation (2), Theorem 4.1, Theorem 7.4.

## Hostile smooth divergence-free family

Choose `chi ∈ C_c^∞(B_1)` equal to one on `B_{3/4}` and `eta ∈ C_c^∞((-1,1))` with `eta(0)=1`. For integer `N≫1`, set

\[
 {\cal A}_N=(0,0,N^{-1}\chi(x)\cos(Nx_1)),\qquad
 v_N=\nabla\times{\cal A}_N,
\]
\[
 u_N(x,t)=\eta(N^2(t-t_0))v_N(x),\qquad p_N=0.
\]

The field is smooth, compactly supported and divergence free. On `B_{3/4}`,

\[
 v_N=(0,\sin(Nx_1),0),\qquad
 \omega_N=\nabla\times v_N=(0,0,N\cos(Nx_1)).
\]

The fixed cutoffs give `|v_N|≤C`, `|∇v_N|≤CN`, while the time support has length `O(N^-2)`.

## Every-radius scaling audit

For **any** parabolic subcylinder of radius `0<r≤1`, its intersection with the spatial support has volume at most `Cr^3` and with the temporal support has length at most `C min(r^2,N^-2)`. Hence, with constants depending only on the fixed cutoffs,

\[
 A(r)\lesssim r^2,\qquad
 C(r)\lesssim r\min(r^2,N^{-2}),\qquad
 D(r)=0,
\]
\[
 E(r)\lesssim N^2r^2\min(r^2,N^{-2}).
\]

The two hostile radius regimes close exactly:
- if `r≤N^-1`, then `E(r)≲N^2r^4≤N^-2`;
- if `r≥N^-1`, then `E(r)≲r^2≤1`.

Thus the numerical local `A+C+D+E` envelope is bounded independently of `N`. A redundant sweep over `N=8,…,2048` and 1200 logarithmically spaced radii in `[10^-6,1]` found no violation and maximum normalized `E=1`; this computation only checks the algebra and has no theorem authority.

## Consumer lower-bound audit

At `t=t_0`, on `B_{1/2}`, `\omega_N=(0,0,N cos(Nx_1))`. For all sufficiently large `N`, a fixed positive fraction of this ball has `|cos(Nx_1)|≥1/2`. Therefore

\[
 \|\omega_N(t_0)\|_{L^{3/2,\infty}(B_{1/2})}\gtrsim N.
\]

On the nonzero-vorticity set the normalized direction is `\xi_N=sgn(cos(Nx_1))e_3`. Choose a nodal plane that meets `B_{1/4}` and a ball of radius `rho_N=a/N` centered on it, with fixed small `a>0`. Reflection in the nodal plane swaps the two signs, so the ball mean is zero and the mean oscillation is exactly one. Grujić's norm is

\[
 \|f\|_{bmo_\phi}=\|f\|_\infty+
 \sup_{x,0<r<1/2}\phi(r)^{-1}\operatorname{MO}_{B_r(x)}(f),
 \quad \phi(r)=|\log r|^{-1}.
\]

Hence one admissible ball yields

\[
 \|\xi_N(t_0)\|_{bmo_{1/|\log r|}}\gtrsim |\log(a/N)|
 =\log N-O(1).
\]

The nodal planes have zero measure. Outside the vorticity support one may choose any fixed bounded convention for `xi`; this does not alter the above lower bound. It also does not solve the separate source-level zero-set binding problem for an actual NSE solution.

## Diagnosis, not overclaim

This family **does not solve Navier–Stokes**. In particular `p_N=0` is used only to instantiate the numerical `D` coordinate. Therefore it does not refute

`NSE + finite I => consumer signature`.

It refutes only the bare representation-level embedding from the numerical finite-`I` coordinates. The mechanism is a critical **parabolic time-trace defect**: spatial derivative amplitude `N` can be concentrated in a time window `N^-2`, so the spacetime quadratic derivative ledger remains bounded while an instantaneous vorticity trace diverges.

The next positive local route must therefore use genuinely equation-specific dynamics (smoothing, time coherence, rigidity, or a different consumer); static interpolation of the four numerical coordinates is saturated.

## Residuals kept separate

**Local mathematical/representation residual:** prove or falsify an NSE-specific upgrade from finite `I` to a suitable time-uniform vorticity phase/amplitude trace without derivative loss or circular regularity.

**Local-to-global/gluing residual:** even a local time-trace upgrade would not supply Grujić's global `L^{3/2,∞}`/far-field Biot–Savart inputs; a separate tail/tightness certificate is required.

**State-space/source residual:** Grujić Theorem 7.4 is a pre-first-singular-time conditional regularity result, not an ancient-solution Liouville theorem. The ancient/pre-singularity bridge remains open.

**Downstream-only items:** pressure localization, normalized-vorticity weak/strong limit binding, noncompact symmetries, backward uniqueness, and Type-II scenarios remain unresolved and are not manufactured by this falsifier.

Outcome: `PARTIAL_SUCCESS / BARE_FUNCTIONAL_PRODUCER_EMBEDDING_REVALIDATED_AS_FALSE / NSE_SPECIFIC_DYNAMIC_UPGRADE_OPEN`.

Novelty class for the scoped solved subproblem: `representation` (structural rank 0). Root remains `OPEN_NO_SOLUTION_CERTIFICATE`.
