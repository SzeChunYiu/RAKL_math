# NS-B1a3-C001 — finite Type-I `I` is asymptotically max-decoupled under large spatial profile separation

**Atom:** `NS-B1a3`  
**Candidate/result ID:** `NS-B1a3-C001-I-PROFILE-MAX-DECOUPLING`  
**Authority:** `SCOPED_FUNCTIONAL_ROUTE_PRUNING / NO_NAVIER_STOKES_COUNTEREXAMPLE / NO_PROFILE_DECOMPOSITION_IMPOSSIBILITY / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`

## Question

The preceding `NS-B1a1` and `NS-B1a2` audits eliminated two possible scale-symmetry breakers: the standard finite-`I` local-energy ledger is scale-neutral, and finite kinetic energy does not quantize `L^3`-critical cores. The next candidate family in the DAG is a Kenig–Merle/Kenig–Koch/Gallagher–Koch–Planchon style critical-element route.

Those source methods operate in genuinely global scale-critical topologies and require control of defects of compactness. Before importing that machinery to the Albritton–Barker Type-I class, this audit asks the cheapest transfer question:

> Does the existing scalar Type-I functional `I` itself penalize two far-separated critical profiles more than one, or is profile multiplicity asymptotically free?

The calculation below is purely functional. The packets are smooth divergence-free test fields, not Navier–Stokes solutions. Pressure is set to zero. The result therefore tests the geometry of the `I` control only.

## Setup

Write, in the notation normalized in `NS-B1_TYPE_I_IMPLICATION_MATRIX_20260811.md`,

`S_Q(v,q) = A(Q)+C(Q)+D(Q)+E(Q)`

and

`I(v,q) = sup_Q S_Q(v,q)`,

where the scale-invariant factors are the Albritton–Barker ones:

- `A(Q_r) = r^-1 sup_t int_{B_r} |v|^2`,
- `C(Q_r) = r^-2 int_{Q_r} |v|^3`,
- `D(Q_r) = r^-2 int_{Q_r} |q|^(3/2)`,
- `E(Q_r) = r^-1 int_{Q_r} |grad v|^2`.

Let `v^(1),v^(2)` be nonzero smooth divergence-free vector fields compactly supported in space-time inside `B(0,R) x (-T,0)` for some fixed finite `R,T`. For `L>2R`, define the spatial translate

`T_L v^(2)(x,t) = v^(2)(x-L e_1,t)`

and

`v_L = v^(1) + T_L v^(2)`, `q_L=0`.

The two spatial supports are disjoint for large `L`.

## Proposition — max-decoupling

For the above fixed packets,

`lim_{L -> infinity} I(v_L,0) = max{ I(v^(1),0), I(v^(2),0) }`.

Thus the scalar finite-`I` control is asymptotically **max-decoupled**, not additive, under large spatial translation separation of fixed profiles.

### Proof

Set

`M_2 = sup_t ||v^(1)(t)||_2^2 + sup_t ||v^(2)(t)||_2^2`,

`M_3 = ||v^(1)||_{L^3_{x,t}}^3 + ||v^(2)||_{L^3_{x,t}}^3`,

and

`M_grad = ||grad v^(1)||_{L^2_{x,t}}^2 + ||grad v^(2)||_{L^2_{x,t}}^2`.

These are finite and independent of `L`.

Consider an arbitrary parabolic cylinder `Q=B(x_0,r) x (t_0-r^2,t_0)`.

**Case 1: the spatial ball meets at most one packet support.** Because the supports are disjoint, all integrands in `A,C,E` coincide on `Q` with those of the corresponding single packet, and `D=0`. Hence

`S_Q(v_L,0) <= max{ I(v^(1),0), I(v^(2),0) }`.

**Case 2: the spatial ball meets both packet supports.** The two support projections are separated by at least `L-2R`, so

`r >= (L-2R)/2`.

Using the fixed global packet integrals,

`A(Q) <= M_2/r <= 2 M_2/(L-2R)`,

`E(Q) <= M_grad/r <= 2 M_grad/(L-2R)`,

and

`C(Q) <= M_3/r^2 <= 4 M_3/(L-2R)^2`.

Since `q_L=0`, `D(Q)=0`. Therefore every cylinder seeing both profiles obeys

`S_Q(v_L,0) <= 2(M_2+M_grad)/(L-2R) + 4M_3/(L-2R)^2 = o(1)`.

Combining the two cases gives

`limsup_{L->infinity} I(v_L,0) <= max{I(v^(1),0),I(v^(2),0)}`.

For the reverse bound, fix `epsilon>0`. For each `j` choose a finite-radius cylinder `Q_j` with

`S_{Q_j}(v^(j),0) >= I(v^(j),0)-epsilon`.

For sufficiently large `L`, the translated other support is outside the spatial ball of `Q_j`; hence the same cylinder evaluated on `v_L` has the same score. Thus

`liminf_{L->infinity} I(v_L,0) >= max{I(v^(1),0),I(v^(2),0)}-epsilon`.

Letting `epsilon downarrow 0` proves the claim. `QED`.

## What the proposition says

The observation is stronger than the earlier statement that `I` is scale invariant. It identifies a separate defect relevant to critical-element transfer: **the scalar value of `I` carries no strict asymptotic price for duplicating a fixed profile far away in space.**

For two identical packets, the one-packet and two-packet configurations have the same limiting `I` value. Therefore `I` by itself does not provide an additive or strictly subadditive profile currency that can count spatial components or rule out dichotomy by scalar minimization alone.

This is exactly the transfer coordinate that differs from the standard critical-element examples. Kenig–Koch work with global `Hdot(1/2)` critical control, while Gallagher–Koch–Planchon use global critical Lebesgue/Besov profile decompositions and a minimal singular norm. Their results establish that concentration-compactness can work for Navier–Stokes in those source settings; they do **not** establish that finite Albritton–Barker `I` has the same defect-of-compactness geometry.

## What is pruned

The following proof shortcut is retired as a standalone route:

`finite I`

`=> minimize the scalar I value among nontrivial Type-I ancient objects`

`=> spatial dichotomy is automatically excluded`

`=> one-profile compact critical ancient element`.

The max-decoupling calculation blocks the middle implication as a consequence of the scalar `I` geometry alone.

## What is not pruned

This result does **not** show that:

- genuine finite-`I` ancient Navier–Stokes solutions can be superposed or spatially split;
- a critical-element construction with extra global topology is impossible;
- pressure/evolution cannot dynamically couple far-separated structures;
- a stability theorem cannot exclude nonlinear dichotomy;
- vorticity-direction coherence or geometric depletion fails;
- no-recrossing/persistence mechanisms fail;
- another source-valid Liouville trigger cannot close the Type-I branch.

The calibration sets `q=0` and deliberately removes the PDE. It therefore supplies no Navier–Stokes counterexample and no theorem about actual ancient solutions.

## Source comparison

- Albritton–Barker (`arXiv:1811.00502`) prove the Type-I singularity/finite-`I` ancient-solution equivalence and a Liouville theorem from a backward sequence bounded in global `L^3`; they explicitly note that boundedness of different Type-I quantities is not generally known to imply boundedness of the others.
- Kenig–Koch (`arXiv:0908.3349`) apply concentration compactness plus rigidity in global critical `Hdot(1/2)`.
- Gallagher–Koch–Planchon (`arXiv:1012.0145`) develop Navier–Stokes profile decomposition in critical Besov spaces and construct minimal-norm singular data under the hypothetical finite critical threshold.
- Barker–Prange (`arXiv:1812.09115`) prove local critical `L^3` concentration near a Type-I singularity at the parabolic scale; this gives at least one critical core, not an additive global profile currency.

The present result is a source-transfer calibration, not a novelty claim.

## Expert-cell interpretation

The PDE and concentration-compactness passes agree that a direct `I`-minimality route now lacks a necessary no-dichotomy ingredient. The vorticity/coherence pass continues to rank a dynamically inherited geometry coordinate at least as highly as searching for a new global critical norm. The adversarial pass confirms that the planted two-profile world attacks only scalar `I` geometry. Formal review keeps the result at route-pruning authority.

## Residual opened

The next strict atom should not ask for “more compactness” abstractly. It should isolate the missing **PDE-specific no-dichotomy coordinate**:

> What property of every finite-`I` Type-I ancient Navier–Stokes solution prevents large-translation profile splitting even though the scalar `I` value is max-decoupled, and how does that property activate a global-critical compactness theorem, a backward `L^3` sequence, or another source-valid Liouville theorem?

Candidate families remain: a genuinely global critical topology inherited from Type-I dynamics, nonlinear pressure/evolution no-splitting, vorticity-direction coherence/geometric depletion, and alternative Liouville triggers. Each requires a fresh context and a cheapest hostile falsifier before a theorem candidate.
