# NS-B1a3b1a1 R3 — exact-NSE high-frequency producer audit

**Authority:** proposal/shadow route-pruning only. This note does not prove a Navier–Stokes singularity, exclude Type I or Type II blow-up, or change the Clay root state. Root remains `OPEN_NO_SOLUTION_CERTIFICATE`; independent mathematical review credit is `0/3`.

## Exact atom

Issue `#148 / NS-B1a3b1a1` asks whether the same-slab Albritton–Barker scale-critical velocity ledger (finite `I`, with the usual `A+C+D+E` coordinates) can, **inside exact whole-space Navier–Stokes dynamics**, force a uniform-in-time global vorticity amplitude bound
\[
\sup_t\|\omega(t)\|_{L^{3/2,\infty}(\mathbb R^3)}<\infty
\]
with a bound depending only on that producer ledger.

The current Grujić v2 consumer genuinely requires the amplitude coordinate separately: Theorem 4.1 assumes, uniformly on a pre-singularity interval, `omega in L^\infty_t L^{3/2,\infty}_x` in addition to the log-weighted BMO direction hypothesis and the critical concentration profile. This cycle tests only production of the amplitude coordinate.

## Scoped result

### Proposition (same-slab finite-I does not control critical vorticity amplitude)

There is a constant `M<infinity` and a sequence of smooth global solutions `(u^N,p^N)` of the unforced incompressible three-dimensional Navier–Stokes equations on `R^3 x [0,infinity)` such that:

1. the standard scale-invariant local ledger is uniformly bounded on every backward parabolic cylinder contained in the positive-time half-space,
   \[
   \sup_N\sup_{z,r}\{A_N(z,r)+C_N(z,r)+D_N(z,r)+E_N(z,r)\}\le M;
   \]
2. there are positive times `t_N -> 0` for which
   \[
   \|\omega^N(t_N)\|_{L^{3/2,\infty}(\mathbb R^3)}\to\infty.
   \]

Consequently, **no universal producer map from this same-slab finite-I ledger alone to a uniform critical-vorticity-amplitude bound can hold**, even after restricting to exact smooth Navier–Stokes solutions.

This is deliberately weaker than a first-singular-time or ancient-solution statement. The hostile family is globally regular and concentrates derivative information at the initial temporal edge.

## Construction

Choose `chi in C_c^\infty(R^3)` with `chi=1` on the cube `Q=[-1,1]^3`. Fix a small amplitude `a>0`, to be chosen below the Kato small-data threshold after multiplication by a cutoff-dependent constant. For integer `N>=1`, set the vector potential
\[
A_N(x)=\left(0,0,\frac aN\chi(x)\sin(Nx_1)\right),
\qquad u_0^N=\nabla\times A_N.
\]
Then `div u_0^N=0` identically and
\[
u_{0,1}^N=\frac aN(\partial_2\chi)\sin(Nx_1),\qquad
u_{0,2}^N=-a\chi\cos(Nx_1)-\frac aN(\partial_1\chi)\sin(Nx_1),\qquad
u_{0,3}^N=0.
\]
Hence
\[
\sup_N\|u_0^N\|_{L^3}\le C_\chi a.
\]
Choose `a` so that `C_chi a` lies below the small-data `L^3` threshold. Kato's critical `L^m` theory (with `m=3`) then gives a unique global strong/mild solution for every `N`, with a uniform contraction bound
\[
\sup_N\sup_{t\ge0}\|u^N(t)\|_{L^3}\le M_3
\]
for a constant `M_3` depending on the chosen small-data ball, not on `N`.

The data are smooth and compactly supported. Classical high-regularity local theory therefore identifies the Kato solution with a classical solution near `t=0` and gives `C^1` convergence to the initial datum for each fixed `N`.

## Positive-time weak-Lorentz lower bound

On `Q`, where `chi=1`,
\[
u_0^N=(0,-a\cos(Nx_1),0),\qquad
\omega_0^N=\nabla\times u_0^N=(0,0,aN\sin(Nx_1)).
\]
For all sufficiently large `N`, the set
\[
E_N=\{x\in Q:|\sin(Nx_1)|\ge 3/4\}
\]
has measure bounded below by an absolute positive constant `c_Q`; this follows by counting complete periods in `[-1,1]`, with only `O(N^{-1})` endpoint loss. Thus
\[
|\omega_0^N|\ge \frac{3aN}{4}\quad\hbox{on }E_N.
\]

For each fixed `N`, `u^N(t)->u_0^N` in `C^1` as `t downarrow 0`. Select
\[
0<t_N< N^{-4}
\]
small enough that
\[
\|\omega^N(t_N)-\omega_0^N\|_{L^\infty(Q)}\le \frac{aN}{4}.
\]
Then `|\omega^N(t_N)|>=aN/2` on `E_N`. Using the distribution-function characterization
\[
\|f\|_{L^{3/2,\infty}}
=\sup_{\lambda>0}\lambda\,|\{|f|>\lambda\}|^{2/3},
\]
we obtain
\[
\|\omega^N(t_N)\|_{L^{3/2,\infty}}
\ge \frac{aN}{2}\,c_Q^{2/3}\longrightarrow\infty.
\]
The `N^{-4}` cap is optional mathematically but makes `t_N->0` explicit.

## Uniform finite-I audit

Use the standard lane coordinates
\[
A(z,r)=r^{-1}\operatorname*{ess\,sup}_{s\in(t-r^2,t)}
\int_{B_r(x)}|u(s)|^2,
\]
\[
C(z,r)=r^{-2}\int_{Q_r(z)}|u|^3,\qquad
D(z,r)=r^{-2}\int_{Q_r(z)}|p-(p)_{B_r}(s)|^{3/2},
\]
\[
E(z,r)=r^{-1}\int_{Q_r(z)}|\nabla u|^2.
\]

Let `M_3=sup_t ||u(t)||_3`, uniformly bounded for the family.

* `A`: Hölder on `B_r` gives
  \[
  r^{-1}\int_{B_r}|u|^2\le C\|u\|_3^2\le C M_3^2.
  \]
* `C`: the time interval has length `r^2`, hence `C(z,r)<=M_3^3`.
* `D`: with the whole-space pressure normalization
  `p=R_iR_j(u_i u_j)`, Calderón–Zygmund boundedness gives
  `||p(s)||_{3/2}<=C M_3^2`. Subtracting a ball mean costs only a universal factor, so `D(z,r)<=C M_3^3`.
* `E`: apply the local energy equality/inequality with a spatial cutoff on `B_{2r}` and a temporal cutoff supported in an interval of length at most `4r^2`. If that enlarged interval meets `t=0`, use the initial energy term; its localized contribution is bounded by `Cr M_3^2`. The cutoff derivative/Laplacian terms are bounded by `Cr M_3^2`, while the cubic and pressure fluxes are bounded by `Cr M_3^3`. After division by `r`,
  \[
  E(z,r)\le C(M_3^2+M_3^3).
  \]
  No derivative norm of the initial data enters this estimate.

Therefore `I=A+C+D+E` is uniformly bounded independently of `N`. The large vorticity comes from derivative-scale information that the same-slab critical velocity ledger does not encode.

## Falsifier audit

1. **Pure scaling rejected.** Navier–Stokes scaling preserves both `||u||_3` and `||omega||_{3/2,\infty}`; dilation alone cannot produce the separator.
2. **Exact equation retained.** Unlike PR #131's non-solution burst, every member here is an exact smooth Navier–Stokes solution.
3. **Positive time retained.** The lower bound is evaluated at `t_N>0`, not only on initial data.
4. **Pressure/nonlocality audited.** Global pressure is controlled in `L^{3/2}` by the uniform global `L^3` velocity norm; the pressure flux enters the `E` estimate explicitly.
5. **No circular smoothing bootstrap.** The only high-derivative fact used is fixed-`N` classical trace continuity to place the initial high-frequency amplitude at some positive `t_N`; the uniform producer bound itself is derived without a derivative estimate.
6. **Endpoint scope explicit.** The construction exploits arbitrarily short forward history. It does not show that a long one-sided history, ancient boundedness, first-singular-time normalization, profile compactness, or additional geometric hypotheses fail to produce amplitude control.

## Local mathematical failure versus gluing failure

**Local mathematical producer failure:**  
`FINITE_I_SAME_SLAB -> UNIFORM_GLOBAL_VORTICITY_L3_2_INFINITY` is false as a universal implication on exact smooth whole-space NSE solutions. The obstruction is derivative/time-edge blindness of the producer signature.

**Separate local-to-global / state-space gluing residuals:**  
The result does not enter the Albritton–Barker singular/ancient source family. It does not control or refute: first-singular-time persistence, long backward history, ancient compactness, global far-field tightness under blow-up recentering, Grujić critical-point morphology, vorticity-direction log-BMO, pressure normalization under limiting sequences, or backward-uniqueness hypotheses. These remain separate obligations.

## Episode -> diagnosis -> obstruction / lesson

**Episode:** execute the prospectively frozen issue-#148 discriminator using an exact small-data high-frequency NSE family.

**Diagnosis:** the equation does not repair the derivative loss on arbitrarily short forward time intervals; critical `L^3`/finite-I velocity control is compatible with unbounded positive-time critical vorticity amplitude across a family.

**Scoped obstruction:** `O-NS-B1a3b1a1-SAME-SLAB-DERIVATIVE-AMPLITUDE-PRODUCER` — any positive producer theorem for the actual Type-I/ancient route must use an extra coordinate not present in same-slab finite-I alone, such as a quantified backward-history/smoothing window, frequency envelope, compactness/tightness condition, or a directly inherited vorticity bound.

**Candidate reusable lesson (not promoted):** `L-NS-B1a3b1a1-TEMPORAL-EDGE-CAN-HIDE-CRITICAL-DERIVATIVES` — before asking a derivative-level consumer to follow from a scale-critical velocity ledger, adversarially test smooth exact solutions with bounded critical velocity and arbitrarily high initial frequency; if the desired estimate is uniform up to the temporal edge, it needs an additional history/frequency hypothesis.

## Novelty / saturation

Shadow classification of the solved subproblem: **representation**. It separates two critical coordinates inside the exact PDE class; it is not a literature-novelty certificate.

This round reopens `KNOWLEDGE`, `EXPERIENCE_PATTERN`, `OBSTRUCTION`, `RELATION`, and `PATH` locally; `OPERATOR` and `META_METHOD` remain flat. No claim of global saturation is made.

## Next atom

Do **not** retry another same-slab finite-I-to-amplitude inequality. The next admissible producer question is narrower:

> `NS-B1a3b1a2 — HISTORY-SEPARATED AMPLITUDE PRODUCER`: in the actual Albritton–Barker Type-I blow-up/ancient class, does a quantified positive backward-history window plus finite `I` suppress the temporal-edge high-frequency separator strongly enough to yield a global weak-`L^{3/2}` vorticity amplitude bound, or can an exact ancient/long-history adversary still defeat it?

That child must bind the history length under rescaling, weak/strong compactness, pressure localization, far-field tightness, and the exact pre-singularity/ancient state-space interface before any Grujić gluing.

## Primary-source provenance

1. Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502v2; J. Math. Fluid Mech. 21 (2019), 43. Current arXiv record checked 2026-08-11; v2 dated 2019-11-18. Used only for the Type-I/ancient source-family boundary and the backward-sequence `L^3` Liouville context.
2. Tosio Kato, *Strong L^p-solutions of the Navier-Stokes equation in R^m, with applications to weak solutions*, Math. Z. 187 (1984), 471–480, DOI 10.1007/BF01174182. Primary full-text introduction checked 2026-08-11: local strong `L^m` solutions, global for sufficiently small `L^m` data. Used for the exact global small-`L^3` NSE family.
3. Zoran Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866v2, revised 2026-07-13. Current arXiv HTML checked 2026-08-11. Definition 2.1 fixes the critical concentration profile; Theorem 4.1 assumes uniform `L^{3/2,\infty}` vorticity plus log-weighted BMO direction on the pre-singularity interval. Used only to bind the consumer coordinate.

No numerical experiment is used as proof.
