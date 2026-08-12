# NS-B1a3b1a2a R6 — ancient smoothing versus global critical-vorticity gluing

**Authority:** proposal/shadow Verified Discovery only. No Clay-root authority, no literature-novelty claim, and no independent-review credit.

**Cycle:** `NS-B1a3b1a2a-R6-ANCIENT-SMOOTHING-GLOBAL-LORENTZ-20260812`

**Frozen application base:** `3871283cfe5040801b174e25b045e05ee0228cc2`

**Framework read before mathematics:** `SzeChunYiu/RAKL@8274f51b3c56145b4300435cea0d401c47313756`, method `3.0.0`.

## Scoped outcome

`ANCIENT_LOCAL_SMOOTHING_BOUND / GLOBAL_LORENTZ_GLUE_OPEN_QUANTIFIED_LINEAR_CAPACITY`

The temporal-edge obstruction is removed in the actual bounded ancient mild class: a bounded ancient mild Navier–Stokes solution has uniform-in-time pointwise bounds on every spatial/time derivative with the scale-forced powers of its global velocity bound. However, combining this smoothing with the finite-`I` dissipation ledger gives only a **linear-in-radius high-vorticity packet-capacity bound**. That is not a radius-free global weak-`L^{3/2}` vorticity estimate. A purely functional gluing step from bounded ancient smoothing plus the `A+C+D+E` bookkeeping to the global Lorentz consumer is therefore insufficient; an equation-specific tail/profile-multiplicity/no-incoming mechanism is still required.

This does **not** show that an actual finite-`I` ancient Navier–Stokes solution can realize the hostile packet arrangement below. It separates the local smoothing theorem from the unresolved global gluing theorem.

## 1. Source-bound local smoothing consequence

Let `u` be a bounded ancient mild solution on `R^3 x (-infinity,0)` and set

`M = ||u||_{L^infinity(R^3 x (-infinity,0))}`.

Koch–Nadirashvili–Seregin–Sverak define an ancient mild solution by the existence of times `T_j -> -infinity` such that, on each `R^3 x (T_j,0)`, `u` is a mild Cauchy solution with initial value `u(.,T_j)`. Their Section 4 gives the mild identity `u=U+B(u,u)` and Proposition 4.1: for a bounded mild solution launched from `u_0 in L^infinity`, for every nonnegative `k,l`,

`||(t)^(k/2+l) nabla^k partial_t^l u||_infinity <= C(k,l)||u_0||_infinity`

on a time interval of length at least `epsilon(k,l)||u_0||_infinity^(-2)`.

For any target time `t_0<0`, choose an ancient mild interval beginning before `t_0-delta`. Split the mild formula at an interior time `s=t_0-delta`; the heat semigroup identity and uniqueness make the restriction on `[s,t_0]` the mild Cauchy solution launched from `u(s)`. Since `||u(s)||_infinity<=M`, choose

`delta = c_{k,l} M^(-2)`

with `0<c_{k,l}<epsilon(k,l)` (the case `M=0` is trivial). Proposition 4.1 then gives, uniformly in `t_0`,

`||nabla^k partial_t^l u(t_0)||_infinity <= C_{k,l} M^(k+2l+1)`.

Thus in particular

`||omega||_infinity <= C M^2`,

`||nabla omega||_infinity <= C M^3`,

`||partial_t omega||_infinity <= C M^4`.

The powers are exactly compatible with Navier–Stokes scaling `u_lambda=lambda u(lambda x,lambda^2 t)`, `omega_lambda=lambda^2 omega(lambda x,lambda^2 t)`. No pressure estimate is needed for this mild-semigroup smoothing step; the Helmholtz projection is already built into the mild formulation.

**Primary source:** G. Koch, N. Nadirashvili, G. Seregin, V. Sverak, arXiv:0709.3599, especially Section 4 Proposition 4.1 and Section 6 ancient-mild definition/Lemma 6.1.

## 2. What finite `I` then says about a fixed-time high-vorticity set

Albritton–Barker define, for every parabolic ball `Q(z,R)`,

`E(Q)=R^(-1) int_Q |nabla u|^2`

and `I=sup_Q(A+C+D+E)`. Hence finite `I` implies

`int_{t-R^2}^t int_{B(x,R)} |omega|^2 <= C I R`,

using `|omega|^2 <= C|nabla u|^2`.

Fix a time `t`, threshold `lambda>0`, and write

`S_lambda(t)={x: |omega(x,t)|>=lambda}`.

Let `K_t=||partial_t omega||_infinity`. The local smoothing result makes `K_t<=C M^4`. For

`delta = min(R^2, lambda/(2K_t))`

(with the obvious interpretation if `K_t=0`), temporal Lipschitz continuity gives

`|omega(x,s)| >= lambda/2`

for every `x in S_lambda(t)` and every `s in [t-delta,t]`. Therefore

`(lambda^2/4) delta |S_lambda(t) cap B(x,R)|`

` <= int_{t-delta}^t int_{B(x,R)} |omega|^2`

` <= C I R`,

so

`|S_lambda(t) cap B(x,R)| <= C I R / (lambda^2 min(R^2,lambda/K_t))`.

For each fixed `lambda>0`, once `R^2 >= lambda/(2K_t)`, this becomes

`|S_lambda(t) cap B(x,R)| <= C I K_t R lambda^(-3)`

and hence, using ancient smoothing,

`|S_lambda(t) cap B(x,R)| <= C I M^4 R lambda^(-3)`.

This is a genuine equation/source-class consequence: ancientness removes the temporal-edge derivative spike and converts the spacetime `E` ledger into a fixed-time **packing-capacity law**. But the law permits `O(R)` high-vorticity volume as the observation radius grows. It does not imply that `|S_lambda(t)|` is finite on all of `R^3`.

A global weak-`L^{3/2}` bound would require a radius-free distribution estimate of the form

`|S_lambda(t)| <= C lambda^(-3/2)`

(up to the standard equivalent Lorentz normalization). The currently derived bound has both an unbounded radius factor and a much weaker threshold exponent. No limit `R->infinity` is licensed.

## 3. Counterexample-first representation stress test

The linear radius factor is not an artifact of a loose counting step at the level of the registered norm ledger.

Choose a nonzero smooth compactly supported divergence-free velocity packet `v_*` supported in `B(0,r_*)`, with vorticity `w_*=curl v_*`. Choose `a>0` such that the set

`E_*={x:|w_*(x)|>=a}`

has positive measure. Pick `L>4r_*`, centers `x_n=(Ln,0,0)`, and a smooth time bump `eta in C_c^infinity((-2,-1))` equal to one at some `t_*`. Define the locally finite smooth field

`V(x,t)=eta(t) sum_{n in Z} v_*(x-x_n)`, `P=0`.

The supports are disjoint, so `V` and all its derivatives are uniformly bounded. For a spatial ball of radius `R`, the number of intersected packets is `O(1+R)`. Consequently, by direct counting:

- `A(Q)=R^(-1) esssup int_{B_R}|V|^2` is uniformly bounded;
- `C(Q)=R^(-2) int_Q |V|^3` is uniformly bounded (for large `R`, the fixed time-support of `eta` makes it `O(R^(-1))`);
- `E(Q)=R^(-1) int_Q |nabla V|^2` is uniformly bounded;
- the bookkeeping expression `D(Q)` is zero for the chosen `P=0`.

For small radii these quantities are controlled by smooth boundedness and parabolic volume; for large radii they are controlled by the `O(R)` packet count and the compact time support.

Yet at `t=t_*`,

`{|curl V|>=a}`

contains the disjoint union of `E_*+x_n` over infinitely many `n`, so it has infinite measure and `curl V(t_*)` is not in global weak-`L^{3/2}`.

**Hard DifferenceWitness:** `(V,P)` is not asserted to solve Navier–Stokes, satisfy the suitable local-energy inequality, or be an Albritton–Barker blow-up limit. It therefore falsifies only a representation-level inference from the magnitude ledger plus smooth local derivative control to global Lorentz amplitude. An equation-specific theorem using pressure/local-energy dynamics, ancestry, tail compactness, or profile rigidity remains open.

## 4. Pressure, nonlocality, endpoint, derivative-loss and circularity audit

- **Scaling:** the local derivative powers `M^(k+2l+1)` are scale-correct. The global Lorentz norm `L^{3/2,infinity}` of vorticity is critical, while the linear-radius capacity is explicitly non-global.
- **Units:** `K_t R lambda^(-3)` has spatial-volume units, as required for the distribution measure.
- **Pressure/nonlocality:** pressure is absent only from the mild local-smoothing proof. The finite-`I` global gluing problem still contains `D` and harmonic/far-field pressure coordinates; none is declared controlled by the smoothing lemma.
- **Endpoint:** the ancient restart uses a fixed positive interior time depth `c M^(-2)` and therefore avoids the finite-left-endpoint separator from R4. It does not use a terminal value at `t=0`.
- **Derivative loss:** the smoothing estimate supplies `partial_t omega` through one spatial plus one time derivative of `u`, with scale power `M^4`; no unregistered derivative estimate is assumed.
- **Circular bootstrap:** no regularity criterion is used to prove the local smoothing bound; it is the standard bounded-mild smoothing result. The global Lorentz step is explicitly left open rather than inferred from its desired conclusion.
- **Source-family completeness:** finite `I` is not replaced by global `L^3`, finite total enstrophy, tail tightness, compact orbit, one-center morphology, or vorticity-direction regularity.
- **Consumer completeness:** even a future global `L^{3/2,infinity}` amplitude bound would not by itself supply Grujic-v2's critical-point profile or log-weighted BMO direction hypotheses.

## 5. Episode -> diagnosis -> obstruction/lesson separation

- **Episode:** source-bind ancient mild restart; derive scale-correct uniform derivative bounds; combine `partial_t omega` persistence with finite `E`; run a linearly replicated smooth packet near-miss.
- **Diagnosis:** genuine ancientness repairs the temporal-edge derivative obstruction, but the repaired producer exposes a spatial multiplicity/tail obstruction: finite `I` permits only a linear-radius capacity estimate.
- **Failure:** the gluing inference `ancient local smoothing + finite-I magnitude ledger => global weak-L^{3/2} vorticity amplitude` is not licensed by the currently registered estimates.
- **Obstruction:** a source-valid tail/profile-count/no-incoming or other equation-specific mechanism must contract the `O(R)` packet capacity to a radius-free global distribution bound.
- **Candidate lesson:** after a local regularizer succeeds, immediately compute the induced large-radius capacity of the target superlevel set; do not confuse bounded local regularity with global critical-state identification.

## 6. Next strict atom

`NS-B1a3b1a2b`: determine whether the **actual finite-`I` ancient Navier–Stokes dynamics** supply a sublinear-to-finite packet-count/tail-tightness mechanism beyond the magnitude ledger. Search first for a source-valid no-incoming-energy/profile-compactness/recentering theorem or an equation-specific pressure/local-energy cancellation that turns the linear capacity above into a radius-free distribution bound. If no such bridge is source-valid, rotate away from the Grujic-amplitude producer rather than strengthening local smoothing again.

The Clay root remains `OPEN_NO_SOLUTION_CERTIFICATE`; proof DAG remains open and genuinely isolated mathematical review remains `0/3`.
