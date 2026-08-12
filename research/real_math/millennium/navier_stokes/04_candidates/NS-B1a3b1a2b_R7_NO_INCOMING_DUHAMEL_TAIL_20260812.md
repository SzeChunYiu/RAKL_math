# NS-B1a3b1a2b R7 — temporal no-incoming Duhamel tail versus spatial packet summability

**Authority:** proposal/shadow mathematical evidence only. Strict current-v3 causal discovery credit is fail-closed by the pre-candidate chronology receipt; no Clay-root, theorem-novelty, or independent-review authority is claimed.

**Cycle:** `NS-B1a3b1a2b-R7-NO-INCOMING-DUHAMEL-20260812`  
**Frozen application base:** `bc55996ef611c93fcc85162f5a2dfe5450cef8b1`  
**Framework source of truth:** `SzeChunYiu/RAKL@5dc0627f039e8f3e1cdcb7e05cd7603860afc554`, method `3.0.0`.  
**Framework execution pin on branch:** synchronized to the same SHA before result materialization.

## Scoped outcome

`REMOTE_PAST_LINEAR_ANCESTRY_ELIMINATED__ABSOLUTE_DUHAMEL_TIME_TAIL_OBTAINED__SPATIAL_PACKET_SUMMABILITY_STILL_OPEN`

The R6 successor asked whether an actual finite-Type-I ancient Navier–Stokes solution has a same-theory "no incoming" mechanism strong enough to replace the representation-only packet objection. There is a useful partial answer.

Let `u` be a bounded ancient mild solution on `R^3 x (-infinity,0)` and define the critical kinetic Morrey coordinate

`A_* = sup_{x in R^3, s<0, R>0} R^(-1) int_{B(x,R)} |u(y,s)|^2 dy`.

In the Albritton–Barker finite-Type-I class this coordinate is bounded by the registered `A` part of `I=A+C+D+E` (up to the convention already frozen in the parent application state). Put `M=||u||_infinity`.

Then the exact mild/Stokes representation and the critical Morrey bound imply two large-time estimates:

`|| e^{T Delta} u(t-T) ||_infinity <= C A_*^(1/2) T^(-1/2),`

and, writing `K_tau` for the kernel of `e^{tau Delta} P div`,

`|| K_tau * (u tensor u)(t-tau) ||_infinity <= C A_* tau^(-3/2)`.

Near `tau=0`, boundedness instead gives the standard estimate

`|| K_tau * (u tensor u) ||_infinity <= C M^2 tau^(-1/2)`.

Hence the nonlinear mild integral is absolutely integrable in `L^infinity` over `(0,infinity)`, the remote-past heat term vanishes as `T->infinity`, and for every fixed ancient time `t`

`u(t) = - int_0^infinity e^{tau Delta} P div (u tensor u)(t-tau) d tau`

with the quantitative tail

`|| int_T^infinity e^{tau Delta} P div (u tensor u)(t-tau) d tau ||_infinity <= C A_* T^(-1/2)`.

Thus **temporal incoming linear ancestry is not the missing obstruction** inside this finite-critical-Morrey ancient mild class. But the estimate is translation-uniform and does not give an `l^1` spatial packet count, a one-center tail, orbit compactness, or a radius-free vorticity distribution bound. The R6 `O(R)` high-vorticity packet-capacity obstruction therefore survives in a narrower form: the missing ingredient is specifically **spatial summability/recentering/coercivity after temporal ancestry has been removed**.

## 1. Primary same-equation representation

Koch–Nadirashvili–Seregin–Sverak, arXiv:0709.3599, Section 3, write the divergence-form Stokes solution using the Helmholtz projection and the kernel `K_ijk`; in dimension three their kernel bound is

`|K_ijk(x,t)| <= C (|x|^2+t)^(-2)`.

Section 4 substitutes the Navier–Stokes forcing `f_jk=-u_j u_k`, and Section 6 defines an ancient mild solution through arbitrarily remote initial times. Splitting a mild interval at any intermediate time therefore gives, for `T>0` with `t-T` inside one such ancient mild interval,

`u(t) = e^{T Delta}u(t-T) - int_0^T K_tau*(u tensor u)(t-tau) d tau`.

The projected formula retains pressure/nonlocality through `P`; it does not assume `p=0`.

## 2. Heat ancestry shell estimate

Fix `x,t,T` and decompose space into `B(x,sqrt(T))` and dyadic annuli with radius `R_k ~ 2^k sqrt(T)`.

From the critical kinetic Morrey coordinate,

`int_{B(x,R)} |u(y,t-T)|^2 dy <= A_* R`.

By Cauchy-Schwarz,

`int_{B(x,R)} |u(y,t-T)| dy <= C R^(3/2) (A_* R)^(1/2) = C A_*^(1/2) R^2`.

The heat kernel on the `k`th annulus is bounded by

`C T^(-3/2) exp(-c 4^k)`,

so that annulus contributes at most

`C A_*^(1/2) T^(-1/2) 2^(2k) exp(-c 4^k)`.

The dyadic series is absolutely summable, yielding

`||e^{T Delta}u(t-T)||_infinity <= C A_*^(1/2) T^(-1/2)`.

This is scale-correct: `A_*` is invariant under Navier–Stokes scaling and `T^(-1/2)` has velocity scaling.

## 3. Oseen nonlinear tail shell estimate

For fixed `tau>0`, the same source gives

`|K_tau(z)| <= C (|z|^2+tau)^(-2)`.

On a dyadic annulus `|z| ~ 2^k sqrt(tau)` this is

`<= C tau^(-2) 2^(-4k)`.

The Morrey bound applied to `u tensor u` gives

`int_{B(x,R)} |u(y,t-tau)|^2 dy <= A_* R`.

Therefore the `k`th shell contributes at most

`C tau^(-2) 2^(-4k) A_* 2^k sqrt(tau)
 = C A_* tau^(-3/2) 2^(-3k)`,

and the shell sum is absolutely convergent:

`||K_tau*(u tensor u)(t-tau)||_infinity <= C A_* tau^(-3/2)`.

This is integrable for `tau>=1`. For `0<tau<=1`, scaling of the same kernel gives `||K_tau||_1 <= C tau^(-1/2)`, so boundedness of `u` yields

`||K_tau*(u tensor u)||_infinity <= C M^2 tau^(-1/2)`,

which is integrable at zero.

Consequently

`int_0^infinity ||K_tau*(u tensor u)(t-tau)||_infinity d tau < infinity`.

Letting `T->infinity` in the ancient mild formula is therefore licensed in `L^infinity`, and the large-time tail is `O(A_* T^(-1/2))`.

## 4. Small-critical-Morrey calibration

The two regimes also give a useful consistency calibration. Split the infinite Duhamel integral at `tau_0=A_*/M^2` when `M,A_*>0`. Then

`M <= C M^2 tau_0^(1/2) + C A_* tau_0^(-1/2)
   <= C' M A_*^(1/2)`.

Thus sufficiently small `A_*` forces `M=0`. This is recorded only as a scoped calibration/consequence of the same estimates, with **no novelty claim** and no use as a root certificate.

## 5. Summation-compatibility audit: time closes, space does not

Current RAKL `SummationCompatibilityWitness` is used twice.

1. `SW-NS-B1a3b1a2b-R7-TEMPORAL-DUHAMEL` records absolute convergence of the dyadic kernel shells and the small/large-time Duhamel decomposition. Finite grouping and time-block regrouping are licensed for this **temporal representation**.
2. `SW-NS-B1a3b1a2b-R7-SPATIAL-LORENTZ` fail-closes the attempted transport from that temporal convergence to a global spatial packet/Lorentz sum: no radius-free block-tail theorem or equivalence proof is available. The unresolved `R->infinity` spatial consumer is not the same infinite object as the convergent `tau->infinity` time tail.

This is exactly why the new same-theory no-incoming result does not erase the R6 packet-capacity obstruction.

## 6. Adversarial audit

**Scaling and units.** `A_*` is critical. Both `A_*^(1/2)T^(-1/2)` and `A_*T^(-1/2)` have velocity units after fixing the dimensionless normalization of `A_*`; the kernel estimate has the correct `length^-4` Stokes-divergence scaling in 3D.

**Endpoint.** The `T->infinity` limit is taken only after the exact ancient mild restart identity. No finite-left-endpoint smoothing is reused.

**Pressure/nonlocality.** The Helmholtz projection is present in `K_tau`; pressure is not set to zero. This result does not claim control of local pressure-work or harmonic pressure tails needed by other local-energy routes.

**Derivative loss.** None. The argument is at the velocity/Duhamel level and does not infer a derivative from a critical norm.

**Circular bootstrap.** No epsilon-regularity or desired global Lorentz condition is used. Bounded ancient mildness and finite `A_*` are the only producer inputs for the new time-tail statement.

**Parasitic solutions.** A nonzero spatially constant velocity has `A_* = infinity`, so it is outside this finite-critical-Morrey producer. No contradiction with the mild ancient definition is created.

**Spatial compactness.** The estimates are uniform under translation. They do not distinguish one packet from infinitely many widely separated packets so long as only the critical local mass law is inspected. The prior ambient packet train remains representation-only; no non-solution model is used as same-theory refutation here.

## 7. Episode -> diagnosis -> obstruction/lesson

**Episode.** Source-bind the ancient mild restart and projected Stokes kernel; perform the critical-Morrey heat and Oseen shell sums; pass to the infinite-past Duhamel representation; then run the current v3 summation-compatibility discriminator against the global Lorentz consumer.

**Diagnosis.** Finite critical kinetic Morrey control plus ancient mildness does provide a quantitative temporal no-incoming mechanism: the remote linear ancestry and nonlinear Duhamel tail both decay as `T^(-1/2)`. The remaining R6 failure is not temporal ancestry but spatial noncompact multiplicity.

**Failure.** `temporal absolute Duhamel convergence => spatial radius-free packet/Lorentz summability` is not licensed.

**Obstruction.** A next route must add a same-theory spatial coordinate—recentring/orbit compactness, a source-inherited one-center tail, signed/coherent pressure-local-energy cancellation, quantitative profile-count control, or another coercive spatial invariant—that is not already contained in the translation-uniform `A_*` shell estimate.

**Candidate lesson.** When an ancient evolution supplies an absolutely convergent remote-past representation, audit the accumulation variable before calling it "no incoming": convergence in time closes only temporal ancestry; it does not transfer to a different spatial infinite decomposition without an explicit compatibility/tail theorem.

## 8. Residual and next atom

Residual before R7:

`finite-I ancient NSE must supply a no-incoming/tail/profile-count mechanism contracting O(R) high-vorticity capacity`.

Residual after R7:

`temporal no-incoming is source-derived and no longer the generic missing coordinate; the open bridge is spatial summability/recentering/coercivity from the actual NSE ancestry to a radius-free critical-vorticity state`.

A strict successor should therefore test a **spatially coercive same-theory consequence** of the infinite-past Duhamel identity, not strengthen local smoothing and not repeat a temporal tail estimate. Candidate families include orbit compactness modulo translation, a one-center tail inherited from blow-up ancestry, or a signed local-energy/pressure flux quantity whose spatial block sum has an explicit current-v3 summation witness.

The Clay root remains `OPEN_NO_SOLUTION_CERTIFICATE`; proof DAG remains open; genuinely isolated mathematical review remains `0/3`.
