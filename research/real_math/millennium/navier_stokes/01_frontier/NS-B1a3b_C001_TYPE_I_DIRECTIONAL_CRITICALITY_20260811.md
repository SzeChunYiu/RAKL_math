# NS-B1a3b-C001 — Type-I directional-criticality classification

Authority: `SOURCE_DERIVED_CLASSIFICATION / PROPOSAL_SHADOW / NO_ROOT_AUTHORITY`.

## Result

For a hypothetical whole-space Type-I mild blow-up at `t=0`, define `omega=curl u`, `zeta=omega/|omega|` on the nonzero-vorticity set, and `Omega_d(t)={x:|omega(x,t)|>d}`. Giga–Miura Corollary 2.6 gives, for every fixed `d>0`,

`integral_{-1}^0 ||grad zeta||_{L^infinity(Omega_d(t))}^2 dt < infinity  =>  no blow-up at t=0`.

Therefore, by direct contrapositive, any Type-I blow-up in this class must satisfy the quantified geometric pathology

`for every d>0: integral_{-1}^0 ||grad zeta||_{L^infinity(Omega_d(t))}^2 dt = infinity`.

This is an exact **necessary blow-up-classification condition**, not a new regularity theorem and not a proof that Type-I blow-up exists. Giga–Miura explicitly state that their `L_t^2 L_x^infinity` condition is scaling invariant. Under `u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`, one has `omega_lambda=lambda^2 omega`, `zeta_lambda(x,t)=zeta(lambda x,lambda^2t)`, `grad zeta_lambda=lambda grad zeta`, and the threshold covaries as `d -> d/lambda^2`; the time Jacobian cancels the squared gradient factor. Thus finiteness is invariant as an existential high-vorticity-threshold property, and the contrapositive divergence is the appropriate critical residual.

A second exact classification edge follows from Giga–Miura Theorem 1.1: a Type-I blow-up must fail uniform-in-time spatial uniform continuity of the vorticity direction on `Omega_d(t)` for every fixed `d>0`. It is not enough that one modulus deteriorates; no single modulus `eta`, independent of time, may satisfy the theorem's `(CA)` hypothesis at any fixed high-vorticity threshold.

## Exact limit-passage interface

The source proof chooses times `t_k -> 0` with `M_k=||u(t_k)||_infinity` attaining the running maximum, centers `x_k` with nearly maximal velocity, `lambda_k=M_k^{-1}`, and

`u_k(x,t)=lambda_k u(x_k+lambda_k x,t_k+lambda_k^2 t)`.

Then `|u_k|<=1`, `|u_k(0,0)|->1`, and whole-space bounded-mild parabolic regularity supplies uniform space/time derivative bounds on compact backward intervals. A subsequence of `u_k` and `omega_k` converges locally uniformly on `R^3 x (-infinity,0]`; the limit is a bounded ancient mild solution, with mildness passed through weak-star convergence of `u_k tensor u_k` in `L^infinity`.

**Weak/strong convergence audit.** Direction is never passed through weak convergence. On a compact `K` contained in `{omega!=0}`, local-uniform vorticity convergence gives a positive lower bound for `|omega_k|` for all large `k`, so `zeta_k` is well-defined and converges locally uniformly. This is the exact strong convergence needed for the geometric interface.

**High-vorticity threshold audit.** Since `omega_k=lambda_k^2 omega` and `lambda_k=M_k^{-1}`, a positive lower bound `|omega_k|>delta` on `K` implies the corresponding original vorticity eventually exceeds any fixed `d`; in the source notation `delta>M_k^{-2}d`. Thus the continuous-alignment hypothesis is legitimately available on the points used in the limit passage.

**Nontriviality audit.** Velocity normalization alone does not certify nonzero vorticity. Giga–Miura Proposition 2.1 supplies the missing step: if the ancient limiting vorticity vanished, bounded harmonicity and mildness would make the limiting velocity a nonzero space-time constant; the inherited Type-I bound tends to zero as backward time tends to `-infinity`, contradiction. Hence the limit vorticity is nontrivial.

## Exact rigidity interface

Continuous alignment, or the source's weaker `(CA')`, collapses the spatial variation of the limiting direction on every compact subset of `{omega!=0}`. Thus at each time the limiting vorticity has one spatial direction. At an arbitrary time slice, rotate coordinates so `omega=(0,0,omega_3)`. Then `(curl omega)_3=0`, so `-Delta u_3=0`; boundedness makes `u_3` spatially constant. The equations `omega_1=omega_2=0` force the horizontal velocity to be independent of `x_3`. Mild-solution uniqueness propagates this two-dimensional structure forward from the arbitrary time slice. The limit then obeys the bounded ancient 2D vorticity equation

`partial_t omega_3 - Delta omega_3 + u·grad omega_3 = 0`.

Giga–Miura Lemma 2.3 applies a translated compactness argument plus the strong maximum principle and harmonic Liouville theorem to force `omega_3=0`, contradicting Proposition 2.1. This is the rigidity contradiction.

## Interface audit against the requested failure modes

- **Pressure localization:** no local pressure decomposition is consumed by this whole-space theorem. The source works in the bounded mild class, where pressure normalization is bound through the mild formulation. This does not prove a new pressure-tail estimate.
- **Far field:** the theorem explicitly allows infinite-energy bounded mild solutions; no decay or global `L^3` tightness is an input. Hence the far-field loss that blocked `NS-B1a3-C001` is non-load-bearing for this route.
- **Noncompact symmetries:** translations `x_k` and dilations `lambda_k` are fixed by maximum normalization; only local-uniform compactness is used. No claim of global profile tightness is made.
- **Vorticity zeros:** direction statements are restricted to compact subsets of `{omega!=0}`. No extension of `zeta` through zeros is assumed.
- **Backward uniqueness:** not used. Therefore no Escauriaza–Seregin–Sverak terminal/exterior/coefficient hypotheses are imported.
- **Equation changes:** 3D Navier–Stokes is not replaced by a stationary Leray equation. The only reduction is an exact consequence of constant limiting vorticity direction, yielding a 2D Navier–Stokes/vorticity system to which a bounded-ancient Liouville theorem applies.
- **Local energy:** the global whole-space theorem does not require the local-energy compactness machinery used by the source's separate local criterion. The existing Clay route may still carry local energy, but it is not a hidden input here.

## What is *not* inherited

The registered finite-`I` Type-I class supplies the blow-up/ancient object, but this cycle found no source-valid implication

`finite I  =>  integral ||grad zeta||_infinity^2 dt < infinity`

or `finite I => uniform continuous alignment`.

Absence of such an implication is recorded as an **open inheritance residual**, not as a refuted theorem. The strongest valid use of the Giga–Miura criterion is therefore classification by contrapositive: any surviving Type-I singularity must live in the directional-critical divergence / loss-of-uniform-continuity class.

## Relation to prior geometry calibration

`NS-R001b` showed that local positive-eigenframe strain/vorticity alignment alone can coexist with concentration or with exact infinite-energy Navier–Stokes growth. That property is not Giga–Miura's nonlocal vorticity-direction coherence and does not falsify this criterion. The current result therefore reopens the geometry lane at a strictly different coordinate: **critical directional oscillation on high-vorticity sets**.

## Residual and nonpromotion

The child contracts from “find some geometric depletion property” to the exact residual:

`NS-B1a3b1`: determine whether the registered finite-`I` Type-I dynamics enforce any quantitative deficit below the Giga–Miura critical divergence class, or else characterize compatible directional-oscillation scenarios without assuming a singular solution exists.

A natural adversarial next target is a self-similar-scale angular cascade in which `grad zeta` has order `(-t)^(-1/2)` on high-vorticity sets, producing logarithmic divergence of the critical integral while remaining consistent with the Type-I velocity scale. Constructing such a field or formal model would be calibration only unless it is an exact Navier–Stokes trajectory.

Root remains `OPEN_NO_SOLUTION_CERTIFICATE`. Type-II `NS-B2` is untouched. This cycle neither proves nor disproves Type-I singularities and creates no root certificate.
