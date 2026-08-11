# NS-R001d same-context expert review

Authority: `ROLE_SEPARATED_SAME_CONTEXT_REVIEW / NOT_INDEPENDENT_REVIEW / PRE_CANDIDATE`.

The cell reviewed one frozen atom: whether Miller's projected advection-plus-quadratic remainder can become the missing critical-control coordinate **because of exact finite-energy Navier–Stokes evolution**, rather than because of a static energy inequality.

## 1. PDE regularity lead — criticality and root scope

Background: 3D Navier–Stokes regularity, Serrin criteria, energy methods, local well-posedness.

Finding: `Q=||R||_2/||-Delta S||_2` is dimensionless under the exact Navier–Stokes scaling, so it is a legitimate critical discriminator. Miller's theorem makes `Q` relevant near a hypothetical singular time, but it does not derive `Q<1` from finite energy.

Strongest objection: a new `Q` bound can merely rename the Millennium problem unless the bound is generated from the energy inequality plus an exact evolution mechanism.

Delegation: require the first action to falsify the weakest snapshot form before any theorem candidate.

Vote: **ACCEPT STATIC FALSIFIER / BLOCK THEOREM SEARCH**.

## 2. Harmonic-analysis / projection lead — nonlocality

Background: Calderón–Zygmund/Riesz transforms, Fourier projections, strain/vorticity formulations.

Finding: `P_st` is load-bearing. An unprojected norm estimate is not interchangeable with `||R||_2`. However, because `-Delta S` lies in the strain constraint space and `P_st` is the orthogonal projection, the pairing `<R,-Delta S>` can be tested exactly using the unprojected tensor inside `P_st`.

Strongest objection: a nonzero unprojected remainder alone would not prove `R != 0`; the test must use the strain-space pairing.

Delegation: construct a seed for which that exact pairing is nonzero and use Cauchy–Schwarz to obtain a projected lower bound.

Vote: **ACCEPT WITH PROJECTION BINDING**.

## 3. Adversarial scaling lead — cheapest counterexample family

Background: PDE scaling, concentration compactness, hostile examples.

Finding: the parent A1 failure suggests using `u_lambda(x)=lambda^(3/2)v(lambda x)`, which preserves `L2` kinetic energy but is deliberately not the Navier–Stokes solution scaling. If a smooth decaying seed has nonzero projected remainder, then `||R(u_lambda)||_2 / ||-Delta S(u_lambda)||_2` has exponent `+1/2`.

Strongest objection: the family is not one trajectory and cannot refute a positive-time dynamics theorem.

Delegation: state the scope as an initial-data snapshot no-go only.

Vote: **ACCEPT SCOPED SCREEN**.

## 4. Dynamics / mixing-transfer lead — enhanced dissipation analogy

Background: advection-diffusion, mixing, enhanced dissipation and trajectory estimates.

Finding: the passive-scalar analogy survives only after being narrowed. The useful lesson is not that advection is automatically regularizing, but that an energy-neutral transport term may matter through **time-dependent derivative redistribution**.

Strongest objection: prescribed shear is not self-consistent Navier–Stokes flow; strain also has quadratic source terms and nonlocal projection.

Delegation: if the static screen fails, reopen the next child around time-integrated or positive-time depletion, not another snapshot norm.

Vote: **ACCEPT ANALOGY AS PROPOSAL-ONLY**.

## 5. Formal/assurance lead — chronology and exact arithmetic

Background: RAKL mathematical gates, exact artifact identity, reproducible algebra.

Finding: NS-R001d is a new child atom and therefore needs a fresh context, memory review, expert event and hash chain. The proposed Gaussian seed permits exact rational polynomial/Gaussian moment checks, avoiding floating-point authority.

Strongest objection: do not backfill a theorem candidate before the new trace is complete.

Delegation: freeze E001–E007, then run only the registered falsifier and append result/residual events.

Vote: **PASS PRE-CANDIDATE PROCESS**.

## 6. Novelty / research-value lead — prior-art boundary

Background: source normalization, rediscovery risk, explanatory value.

Finding: Miller already supplies the remainder and the conditional criterion. The research value here is only the route-specific scope calibration: whether finite kinetic energy can statically control that criterion's dimensionless ratio.

Strongest objection: do not call the ratio, the enhanced-dissipation interpretation, or the scaling observation new mathematics without a bounded novelty review.

Delegation: authority after a successful screen is `SCOPED_ROUTE_FALSIFIER`, not theorem/novelty.

Vote: **ACCEPT CALIBRATION / NO NOVELTY CLAIM**.

## Cell synthesis

All six roles agree on the same next action: execute one exact **initial-data concentration falsifier** before any theorem candidate. The highest-value partition is:

- if fixed energy controls the snapshot ratio, a direct energy-to-Miller bridge remains live;
- if it does not, static control is pruned and the only live Miller-based route must use positive-time evolution, time integration, or additional critical information.

Unresolved: whether actual Navier–Stokes evolution supplies any such dynamic depletion.
