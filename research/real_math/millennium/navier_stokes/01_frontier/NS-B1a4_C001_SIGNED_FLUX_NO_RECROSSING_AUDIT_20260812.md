# NS-B1a4-C001 — signed-flux / no-recrossing local-energy discriminator

**Date:** 2026-08-12 (Europe/Stockholm; verification at 2026-08-11T22:51:53Z)  
**Authority:** `EXISTING_LEDGER_SIGN_INSUFFICIENT_ROUTE_PRUNING / EXACT_NSE_LOCAL_CALIBRATION / GLOBAL_FINITE_I_THEOREM_OPEN / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`  
**Framework pin:** `SzeChunYiu/RAKL@2f722d42db240538e1bdec146aebc7e9d5eeb8a6`, method `3.0.0`  
**Application base:** `SzeChunYiu/RAKL_math@a7301f0f0e2cab2750ac6e923efe18b5750b5af6`  
**Frozen context:** `sha256:4f4201800bdb64d85704ed43c5acb44bb0a3edc4772df2a0477f4ad989c0f83a`

## Executive finding

The existing unsigned finite-`I` magnitude ledger plus the standard local-energy identity and pressure localization does **not by itself supply the sign** needed for a fixed-region kinetic-energy monotonicity/no-recrossing argument.

An exact smooth pressure-free 3D Navier–Stokes shear has strictly increasing kinetic energy in every fixed ball. Therefore pressure cannot be the universal source of the missing sign, and the viscous dissipation term does not by itself make localized energy nonincreasing because boundary diffusion/transport terms remain. This prunes only the inference architecture

`unsigned local magnitude control + standard local-energy identity + pressure localization -> one-sided fixed-region local-energy sign`.

It does **not** refute a stronger theorem using global finite `I`, an ancient-state constraint, moving/profile-adapted regions, a new signed flux/correlation observable, almost-periodicity/minimality, or another dynamics-specific trajectory input.

## Exact pressure-free calibration

Fix `eps>0` and `k>0`, and define on `R^3 x R`

`u(x,t) = (eps exp(k x_2 + k^2 t), 0, 0)`,  
`p(x,t) = 0`.

Write `f(x_2,t)=eps exp(k x_2+k^2 t)`. Then

`div u = partial_1 f = 0`,

because `f` is independent of `x_1`. Also

`(u dot grad)u = f partial_1 u = 0`,

while

`partial_t u = k^2 u`,  
`Delta u = partial_2^2 u = k^2 u`.

Hence

`partial_t u + (u dot grad)u = Delta u - grad p`

exactly, with viscosity normalized to one.

This is therefore an exact smooth 3D incompressible Navier–Stokes solution, not merely a heat-flow proxy.

## Local kinetic energy increases

For a fixed ball `B_R`, define

`E_R(t) = (1/2) integral_{B_R} |u(x,t)|^2 dx`.

Because the spatial integral is finite on every bounded ball,

`E_R(t) = (eps^2/2) exp(2 k^2 t) integral_{B_R} exp(2 k x_2) dx`.

Therefore

`dE_R/dt = 2 k^2 E_R(t) > 0`.

Thus fixed-ball local kinetic energy can increase even when `p=0`.

For this shear the advective energy flux has zero net contribution through a centered ball by the `x_1 -> -x_1` symmetry, while diffusion imports enough energy through the spatial boundary to exceed local viscous dissipation. Equivalently, the smooth local-energy identity has a signed dissipation term but no universal sign after localization because the cutoff/boundary terms remain.

## Relation to the finite-I ledger

On every compact parabolic cylinder, the local quantities of the Albritton–Barker suitable-solution ledger are finite; here `D=0` because pressure vanishes. Smoothness gives the local-energy equality, hence also the suitable local-energy inequality.

What fails is **global target membership**, not local PDE validity:

- `u` grows exponentially as `x_2 -> +infinity`;
- it is not globally finite-energy;
- it is not bounded on all of `R^3`;
- it is not a nontrivial mild bounded ancient solution with global finite Albritton–Barker `I`.

This DifferenceWitness is mandatory. The calibration cannot falsify

`global finite I + ancient Navier-Stokes dynamics -> signed/no-recrossing property`.

It falsifies only the weaker claim that the *already available local unsigned magnitudes, local energy identity, and pressure localization* contain enough information by themselves to orient the local flux.

## Pressure audit

The prior experience `F-NS-B1a-C001-PRESSURE-SUMMABILITY` already pruned raw instantaneous far-field pressure divergence as the anti-replication mechanism. The present exact `p=0` calibration makes a different point: even eliminating pressure altogether does not make localized kinetic energy one-sided.

Therefore the pressure-temporal lane, if continued, must involve a genuinely signed pressure-velocity/flux correlation or another trajectory structure; pressure magnitude/localization alone is insufficient.

## Local-versus-global failure separation

### Local mathematical / representation failure

`F-NS-B1a4-UNSIGNED-LOCAL-ENERGY-NO-SIGN`:

The producer data `A,C,D,E` are unsigned magnitudes. Together with the standard local-energy identity they do not force nonpositive fixed-region local-energy derivative. Exact pressure-free NSE dynamics exhibit positive derivative.

This is a local representation/inference failure.

### Local-to-global / gluing status

No new global-gluing impossibility is proved. The prior

`F-NS-B1a3-LOCAL-GLOBAL-INTERFACE-MISMATCH`

remains separately active: even a valid local signed lemma would still need to glue to the same finite-`I` ancient state, control far field/noncompact symmetries, and deliver the exact input of a named rigidity theorem.

Backward uniqueness, stationary Leray-profile Liouville theorems, and self-similar equation reductions are not invoked in this calibration.

## Episode -> diagnosis -> obstruction/lesson

**Episode:** `EP-NS-B1a4-C001-SIGNED-FLUX-20260812` executes the issue-#173 pressure-free exact-NSE falsifier against the local/magnitude-only sign inference.

**Diagnosis:** the missing coordinate is not pressure magnitude but orientation/correlation of localized energy transfer. Dissipation has a sign; localization reintroduces boundary flux whose sign is not encoded in `A,C,D,E`.

**Reusable obstruction:** `O-NS-B1a4-SIGNED-FLUX-COORDINATE` — before claiming no-recrossing from finite-`I` local energy, identify a source-valid signed/correlated trajectory observable and prove that it survives the Type-I rescaling/limit and same-theory global assembly.

**Lesson proposal:** `L-NS-B1a4-MAGNITUDE-LEDGER-DOES-NOT-ORIENT-FLUX` remains proposal-only until separately consolidated/validated.

## Prior experience routing

Selected and action-changing in the bounded routing sense:

- `F-NS-B1a-C001-PRESSURE-SUMMABILITY`: prevented retrying raw pressure-tail divergence.
- `F-NS-B1a1-SCALE-NEUTRAL-LOCAL-ENERGY-LEDGER`: prevented another absolute shell-budget summation.
- `F-NS-B1a3-LOCAL-GLOBAL-INTERFACE-MISMATCH`: forced local sign failure and global gluing to remain separate.

Retrieved but rejected for this atom:

- `F-NS-B1a3b-DERIVATIVE-LOSS-VORTICITY-DIRECTION`;
- `F-NS-B1a3b-NORMALIZATION-ZERO-INSTABILITY`;
- `F-NS-B1a3b1-GLOBAL-CONSUMER-SIGNATURE-MISMATCH`.

They are either vorticity-representation-specific or duplicate a more direct local-to-global warning.

No promoted Navier–Stokes success tool and no promoted StrategyMotif were available in the inspected application inventory.

## Outcome and residual

**Outcome:** `PARTIAL_SUCCESS / EXISTING_LEDGER_SIGN_INSUFFICIENT_ROUTE_PRUNING`.

**Solved subproblem:** fixed-region local-energy nonincrease cannot be inferred from local unsigned finite-I-type magnitude control, the standard local-energy identity, and pressure localization alone.

**RAKL novelty class:** `REPRESENTATION` (internal/scoped, structural rank 0). The retained result identifies a sign coordinate erased by the magnitude-ledger representation. This is not an external literature novelty claim.

**Residual before:** broad pressure-aware temporal cancellation/no-recrossing route.

**Residual after:** any live successor must add at least one of:
1. a signed scale-to-scale flux/correlation observable with a source-valid evolution law;
2. a profile/moving-region trajectory coordinate whose recrossings are quantifiably controlled;
3. a global finite-`I`/ancient-state theorem that supplies orientation unavailable to local ledger data;
4. an orthogonal Type-I mechanism. Type-II remains separately open.

**Root status:** `OPEN_NO_SOLUTION_CERTIFICATE`.

## Source provenance

- Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502v2, J. Math. Fluid Mech. 21 (2019), 43.
- Pineau and Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations*, arXiv:2607.09619v2 (2026), retained only as a stronger-hypothesis near-solved analogue.
- `SzeChunYiu/RAKL_math` issue #173, prospective scope/falsifier provenance.

A bounded 2026 literature search found no direct source match for the desired finite-`I` signed no-recrossing implication. That search result is routing evidence only, not a completeness or novelty certificate.
