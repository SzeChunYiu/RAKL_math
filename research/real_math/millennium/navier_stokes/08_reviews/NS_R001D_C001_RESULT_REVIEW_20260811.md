# NS-R001d-C001 same-context result review

Authority: `ROLE_SEPARATED_SAME_CONTEXT_RESULT_REVIEW / NOT_INDEPENDENT_REVIEW / SCOPED_NEGATIVE_RESULT / NO_ROOT_AUTHORITY`.

The cell reviewed the exact Gaussian falsifier after execution. No role treats a route refutation as a Navier–Stokes regularity theorem.

## 1. PDE regularity lead — root and initial-data scope

**Background:** strong/mild Navier–Stokes solutions, energy class, conditional regularity criteria.

**Evidence inspected:** the frozen candidate, Gaussian falsifier, exact scaling exponents and Miller's conditional remainder criterion.

**Finding:** the result genuinely rules out a bound `Q(u)<=B(||u||_2^2)` on the full smooth rapidly decaying divergence-free initial-data class. Since each member is admissible as initial data, an energy-only snapshot theorem cannot be rescued by saying the fields are not admissible.

**Strongest objection:** the concentration family is not one Navier–Stokes trajectory and is not the Navier–Stokes solution symmetry.

**Delegation:** the next child must begin at positive time or integrate along actual solutions; do not repeat another static kinetic-energy bound with a renamed critical coordinate.

**Vote:** **ACCEPT SCOPED NO-GO / BLOCK DYNAMIC INFERENCE**.

## 2. Harmonic-analysis / projection lead — nonlocal binding

**Background:** orthogonal projections, strain constraint space, Calderón–Zygmund/nonlocal formulations.

**Evidence inspected:** `D=-Delta S`, the exact pairing `int F:D`, and the use of `R=P_st F`.

**Finding:** the argument does not replace the projected norm by the unprojected norm. Because `D` is in the strain space, self-adjoint orthogonal projection gives `<R,D>=<F,D>`. Cauchy–Schwarz then supplies a lower bound on `||R||` from the nonzero pairing.

**Strongest objection:** this lower bound says nothing about the detailed frequency or spatial distribution of `R`.

**Delegation:** if a dynamic child uses frequency-local cancellation, it must keep the projection and pressure/nonlocal structure explicit.

**Vote:** **ACCEPT PROJECTION-BOUND RESULT**.

## 3. Scaling / concentration lead — exponent audit

**Background:** critical PDE scaling and concentration compactness.

**Evidence inspected:** `u_lambda=lambda^(3/2)u(lambda x)` and exact Gaussian moments.

**Finding:** energy is invariant, `||D_lambda||_2^2` scales as `lambda^6`, and `<F_lambda,D_lambda>` scales as `lambda^(13/2)`, hence the rigorous lower bound on `Q` grows as `lambda^(1/2)`. This is the same structural warning as A1, now witnessed for Miller's projected remainder rather than a generic Serrin norm.

**Strongest objection:** the amplitude `lambda^(3/2)` is chosen to preserve energy, not to preserve the Navier–Stokes equation.

**Delegation:** explicitly treat the result as an initial-data family screen only.

**Vote:** **ACCEPT EXPONENT AUDIT**.

## 4. Dynamics / mechanism lead — surviving route

**Background:** viscous smoothing, nonlinear transport, enhanced-dissipation analogues, trajectory estimates.

**Evidence inspected:** the negative snapshot result and the retained passive-scalar structural analogy.

**Finding:** the failure increases the value of a dynamics-specific discriminator. A useful estimate would need to show that, for actual solutions at `t>0`, diffusion plus self-consistent advection/pressure changes the ratio or an integrated analogue in a way not available at `t=0` from energy alone.

**Strongest objection:** ordinary heat-semigroup smoothing by itself may produce time-weighted high-derivative bounds without yielding any scale-critical closing estimate for the nonlinear remainder.

**Delegation:** open `NS-R001d1` around the smallest positive-time/time-integrated statement that distinguishes mere parabolic smoothing from nonlinear depletion. First seek a hostile linear/perturbative calibration before a theorem candidate.

**Vote:** **ACCEPT DYNAMIC CHILD / REJECT STATIC RETRY**.

## 5. Formal/assurance lead — reproducibility and authority

**Background:** exact arithmetic, RAKL chronology, theorem-authority boundaries.

**Evidence inspected:** frozen context/memory/expert packet, pre-candidate trace, candidate commit preceding falsifier, exact `Fraction` Gaussian-moment regression and failure record.

**Finding:** the result can be reproduced without floating-point quadrature. The diagnosis should remain `SUPPORTED`: it is a verified counterexample to one registered route hypothesis, not a verified impossibility for all energy-based dynamics.

**Strongest objection:** no root claim, proof receipt, novelty certificate or independent review exists.

**Delegation:** append result/review/residual trace events and require exact-head application CI before merge.

**Vote:** **PASS SCOPED ASSURANCE / ROOT BLOCKED**.

## 6. Novelty / research-value lead — value of the negative result

**Background:** literature normalization and route-pruning value.

**Evidence inspected:** Miller's published/revised decomposition and the route-specific concentration calculation.

**Finding:** no novelty claim is warranted. The value is epistemic: it prevents the programme from spending further cycles trying to derive Miller-remainder snapshot control from kinetic energy alone and identifies a sharper dynamics-dependent residual.

**Strongest objection:** a simple scaling calibration may already be implicit to experts even if this exact Gaussian witness is not documented in the inspected source set.

**Delegation:** do not open a novelty lane for the calibration; invest the next cycle in the dynamic residual.

**Vote:** **RETAIN AS NEGATIVE RESEARCH TOOLING / NO NOVELTY AUTHORITY**.

## Cell synthesis

The group unanimously accepts the following bounded conclusion:

> **Static finite kinetic energy does not bound Miller's scale-invariant projected-remainder ratio over the full smooth rapidly decaying divergence-free initial-data class.**

The load-bearing new residual is not “find a better snapshot norm.” It is:

> **Can actual positive-time finite-energy Navier–Stokes evolution generate a scale-critical depletion or integrability property for the projected remainder that is absent at the initial snapshot?**

Open that as fresh child `NS-R001d1`; its first discriminator must separate generic heat smoothing from genuinely nonlinear advection/pressure depletion. The root remains open.
