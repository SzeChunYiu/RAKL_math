# NS-B1a3b-C001 — Vorticity-direction inheritance / derivative-loss interface audit

**Date:** 2026-08-11  
**Authority:** `SOURCE_BOUND_INTERFACE_ROUTE_PRUNING / TOPOLOGY_FALSIFIER_VERIFIED / PDE_INHERITANCE_OPEN / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`

## Executive finding

The vorticity-geometry family survives as a possible Navier–Stokes mechanism, but the **naive inheritance step is not licensed**.

The registered Albritton–Barker Type-I package produces a nontrivial mild bounded ancient solution in the finite-`I` class and, at the compactness stage already audited in `NS-B1a3`, strong local `L^3` convergence of velocity together with natural weak derivative control. Geometric regularity criteria consume substantially different objects: a modulus of the normalized vorticity direction, a critical projected-vorticity norm plus a controlled plane field, or another high-vorticity-set geometry quantity.

There is a one-derivative and normalization gap between those interfaces. An exact divergence-free oscillatory calibration shows that strong local velocity convergence plus bounded `L^2` gradient energy can coexist with arbitrarily rapid flipping of normalized vorticity direction. Hence

`finite-I compactness topology  =>  vorticity-direction coherence`

cannot be justified **by compactness topology alone**.

This does not prove that the Navier–Stokes equation cannot force additional geometric coherence. It localizes the next obligation: any positive geometry route must derive a new equation-specific, scale-matched geometric estimate before invoking a conditional regularity theorem.

## Exact counterexample-first topology calibration

Work on a fixed periodic box and define

`w_n(x) = (0, n^{-1} sin(n x_1), 0)`.

Then

`div w_n = 0`,

`||w_n||_{L^3} = O(n^{-1}) -> 0`,

and the only nonzero first derivative is

`partial_1 (w_n)_2 = cos(n x_1)`,

so `||grad w_n||_{L^2}` is independent of `n`. Moreover

`curl w_n = (0,0,cos(n x_1))`.

Away from the zero planes of `cos(n x_1)`, the normalized vorticity direction is exactly `+e_3` or `-e_3`. The signs alternate on spatial scale `O(n^{-1})`. For any fixed high-vorticity threshold `0<d<1`, points in the set `|curl w_n|>d` with opposite directions can be chosen at separation `O(n^{-1})`; their direction difference is `2`. Thus there is no modulus of continuity uniform in `n`.

This calibration is **not a Navier–Stokes solution** and is not a PDE counterexample. Its conclusion is narrower and exact: the producer topology consisting of strong velocity convergence plus the natural bounded/weak first-derivative control is insufficient, as a matter of functional analysis, to transport a modulus of normalized curl direction.

## Scaling and endpoint audit

Under the Navier–Stokes scaling

`u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`,

the vorticity scales as

`omega_lambda(x,t)=lambda^2 omega(lambda x,lambda^2 t)`.

Where `omega != 0`,

`xi_lambda(x,t)=omega_lambda/|omega_lambda|=xi(lambda x,lambda^2 t)`,

so the direction itself is dimensionless. But a spatial Hölder seminorm transforms as

`[xi_lambda]_{C^alpha}=lambda^alpha [xi]_{C^alpha}`.

Therefore “vorticity direction is regular” is not a single scale-invariant scalar statement. The precise modulus, high-vorticity subset, shrinking region, and time integrability in the consumer theorem must be bound before transfer.

The normalization endpoint is also non-removable: `xi` is undefined at `omega=0`, and the map `omega -> omega/|omega|` is unstable near zero. Source criteria avoid this by imposing geometry on high-vorticity subsets or by controlling a different projected-vorticity object. An inheritance theorem must preserve that set-valued interface rather than silently normalize everywhere.

## Primary-source consumer audit

### Constantin–Fefferman geometry

The whole-space Constantin–Fefferman route is a genuine geometric-depletion criterion. Barker–Prange's primary-source discussion records the condition schematically as

`|sin angle(omega(x+y,t),omega(x,t))| <= C |y|`

on a high-vorticity region and explains that it depletes the most singular vortex-stretching contribution. Their discussion explicitly distinguishes this from regularity criteria stated in scale-invariant quantities.

Therefore Constantin–Fefferman is a valid **mechanism analogue**, but it must not be relabeled as an automatically inherited critical norm.

### Miller anisotropic criterion

Miller's primary arXiv record states a scale-critical consumer: the vorticity projected to a varying plane must remain bounded in `L^4_t L^2_x`, while the gradient of the vector normal to that plane is bounded. Finite `I` supplies neither a preferred plane field nor the required bound. Choosing a plane from the vorticity direction would reintroduce the very directional-regularity problem under audit.

### Barker–Prange Type-I alignment

Barker–Prange prove a powerful near-solved analogue: in the half-space with no-slip boundary condition and the ODE Type-I rate, uniform continuity of vorticity direction on specified high-vorticity subsets of shrinking `O(sqrt(T-t))` regions yields regularity. Their proof uses scaled Morrey estimates, blow-up/compactness and persistence of singularities.

The transfer to `NS-B1a3b` is blocked for three independent reasons:

1. the source domain is the half-space with no-slip boundary, while the target is the whole space;
2. the source Type-I hypothesis is the ODE blow-up rate, while the active target class is the Albritton–Barker finite-`I` class;
3. most importantly, the alignment modulus is an **assumption**, not an output of Type-I compactness.

This theorem shows `Type-I + geometry` can close a blow-up contradiction in a nearby context. It does not prove `Type-I => geometry`.

### July 2026 logarithmic-depletion preprint

Grujic's July 2026 preprint studies critical-point singularities under weak-`L^{3/2}` vorticity concentration and a logarithmically weighted local BMO condition on vorticity direction, then derives depletion and subcritical gains. The direction and concentration conditions are again additional inputs. Because this is a fresh preprint and its target class carries extra hypotheses, it is retained only as proposal/shadow search guidance.

## Pressure and nonlocality audit

This route differs structurally from the earlier pressure-summability lane. Taking curl removes pressure exactly:

`partial_t omega + (u dot grad)omega - Delta omega = (omega dot grad)u`.

Thus `F-NS-B1a-C001-PRESSURE-SUMMABILITY` is **not** transferred as the active local obstruction.

Nonlocality nevertheless remains. The stretching term is governed by the velocity gradient; its strain component is a singular-integral/Biot–Savart transform of vorticity. Vorticity-direction coherence can cancel the singular kernel, but only after the geometric hypothesis has been established. Replacing “pressure is nonlocal” by “curl removes all nonlocal difficulty” would therefore be another interface error.

## Derivative loss and circular-bootstrap audit

A forbidden bootstrap would be:

`finite I -> weak control of grad u -> regular direction xi -> depleted stretching -> stronger grad u`.

The second arrow is precisely the missing step. Any estimate used there must be proved without assuming a derivative modulus or strong vorticity compactness equivalent to the desired conclusion.

The oscillatory calibration makes this circularity visible: bounded first-derivative energy does not control the normalized derivative field's direction. Equation-specific cancellation may still add information, but it must be an independently proved estimate.

## Failure classification

This cycle separates two failure types that must not be conflated.

**Local mathematical/representation interface failure**
- `F-NS-B1a3b-DERIVATIVE-LOSS-VORTICITY-DIRECTION` — the registered velocity compactness does not continuously produce a vorticity-direction modulus.
- `F-NS-B1a3b-NORMALIZATION-ZERO-INSTABILITY` — normalized vorticity is unstable/undefined at zeros; high-vorticity-set structure must be preserved explicitly.
- `F-NS-B1a3b-GEOMETRY-NOT-INHERITED-BY-TOPOLOGY` — conditional geometry inputs are not outputs of the current finite-`I` compactness topology.
- `F-NS-B1a3b-DOMAIN-TYPEI-DIFFERENCE-WITNESS` — half-space ODE-Type-I alignment cannot be silently transferred to whole-space finite `I`.

**Local-to-global/gluing status**
- No new local-to-global gluing failure was discovered in this child.
- The earlier `F-NS-B1a3-LOCAL-GLOBAL-INTERFACE-MISMATCH` remains separately open for critical compactness/rigidity.
- `NS-B1a3b` fails earlier, at a local representation/inheritance interface.

The normalized reusable obstruction is

`O-NS-B1a3b-GEOMETRY-INHERITANCE-INTERFACE`:

> Before applying a vorticity-geometry consumer theorem to a finite-`I` blow-up limit, produce a source-matched, scale-correct equation-specific estimate that controls its geometric input uniformly through the rescaled sequence and survives normalization/high-vorticity-set passage.

## Episode -> diagnosis -> obstruction/lesson separation

**Episode:** the frozen `NS-B1a3b-C001` attempt tested a predeclared topology-and-source discriminator.

**Diagnosis:** the failure of direct transfer is caused by derivative loss plus normalization instability, with separate domain/Type-I DifferenceWitness failures for the closest analogue.

**Reusable obstruction/lesson:** only the scoped producer/consumer interface above is retained. The episode itself does not prove that Navier–Stokes dynamics can never create vorticity alignment.

The repeated process pattern links this cycle to `NS-B1a3`: twice, a known consumer theorem was initially attractive, and twice the high-information action was to compare the producer output type against the consumer input type before theorem invocation. The mathematical obstructions differ — global critical tail tightness in `B1a3`, derivative/normalization geometry in `B1a3b` — so they remain separate failure records.

## Outcome and residual

**Outcome:** `PARTIAL_SUCCESS / SOURCE_BOUND_GEOMETRIC_INHERITANCE_ROUTE_PRUNING`.

**Solved subproblem:** the compactness-topology-only inheritance claim is falsified by an exact divergence-free calibration and source-signature audit.

**RAKL novelty classification:** `TRANSFER_NOVEL`, structural rank `0`, for this solved route-pruning subproblem: the cycle reuses the pre-existing producer/consumer interface audit pattern under an explicit DifferenceWitness in a new vorticity representation; no new framework operator or ontology was invented.

**Residual before:** broad vorticity-direction/geometric-depletion route after critical compactness failed.

**Residual after:** geometry remains live only through a new equation-specific estimate. Candidate successor questions are:
- derive from finite-`I` dynamics a uniform scale-matched high-vorticity geometric functional that survives blow-up;
- identify a different vorticity/strain quantity whose compactness is actually controlled at the existing derivative level;
- or pivot to the orthogonal pressure-temporal/no-recrossing lane rather than assuming geometry.

**Root status:** `OPEN_NO_SOLUTION_CERTIFICATE`.

No Type-I exclusion, Type-II result, global regularity proof, independent review, or root promotion is created by this audit.

## Primary-source anchors

- Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502 / J. Math. Fluid Mech. 21 (2019), 43.
- Peter Constantin and Charles Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier-Stokes Equations*, Indiana Univ. Math. J. 42 (1993), 775–789.
- Tobias Barker and Christophe Prange, *Scale-invariant estimates and vorticity alignment for Navier-Stokes in the half-space with no-slip boundary conditions*, arXiv:1906.08225.
- Evan Miller, *A locally anisotropic regularity criterion for the Navier–Stokes equation in terms of vorticity*, arXiv:2002.02152 / Proc. Amer. Math. Soc. Ser. B 8 (2021).
- Zoran Grujic, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866v2 (13 July 2026); preprint, proposal/shadow search use only.
