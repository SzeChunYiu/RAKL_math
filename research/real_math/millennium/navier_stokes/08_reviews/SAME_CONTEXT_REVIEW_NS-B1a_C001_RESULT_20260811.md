# Same-context result review — NS-B1a-C001 pressure-tail calibration

**Authority:** role-separated same-context review only; **not independent mathematical review**.  
**Candidate:** `NS-B1a-C001`.  
**Result under review:** critical-Morrey control makes the absolute instantaneous far-field quadratic pressure contribution dyadically summable; the narrower raw pressure-divergence anti-replication mechanism is rejected.

## 1. PDE regularity / ancient-solution lead

**Background:** mild and suitable Navier–Stokes solutions, Type-I rescaling, critical regularity, ancient-solution Liouville routes.

**Delegation:** check whether the estimate composes with the parent Type-I route without silently creating the missing `L^3` trace.

**Finding:** the calculation is compatible with finite `I` through the `A` term, but it only localizes the distant quadratic pressure contribution. It does not create global `L^3` integrability, a backward bounded sequence, or triviality.

**Strongest objection:** do not rename pressure-tail summability as spatial tail tightness of velocity.

**Vote:** `ACCEPT_LOCAL_CALIBRATION / NO_LIOUVILLE_PROMOTION`.

## 2. Harmonic-analysis / pressure lead

**Background:** Calderón–Zygmund kernels, local pressure expansions, Morrey-type estimates.

**Delegation:** stress-test the dyadic estimate and the pressure representation boundary.

**Finding:** if `mu(B(x,r)) <= M r`, the sign-free far-field shell costs are `O(M 2^{-2k}R^{-2})`; the gradient-kernel shell costs are `O(M 2^{-3k}R^{-3})`. Both sums converge. This is stronger than relying on cancellation.

**Strongest objection:** the estimate concerns the far-field quadratic kernel only. It does not settle the local singular pressure, harmonic normalization, or time-integrated pressure work.

**Vote:** `PASS_SCOPED_KERNEL_ESTIMATE`.

## 3. Scaling / compactness lead

**Background:** critical scaling, translation/dilation noncompactness, concentration compactness.

**Delegation:** determine what structural coordinate has actually been eliminated.

**Finding:** pressure nonlocality alone does not prevent spatially remote critical mass through divergent instantaneous coupling; the critical Morrey growth is sparse enough that the `|z|^-3` kernel remains summable. Translation escape therefore remains possible at the level of this bound.

**Strongest objection:** this does not prove an actual finite-`I` Navier–Stokes orbit can realize the sparse-tail geometry.

**Vote:** `ROUTE_PRUNED / NONCOMPACTNESS_RESIDUAL_REMAINS`.

## 4. Adversarial falsification lead

**Background:** counterexample-first theorem design and mechanism falsification.

**Delegation:** ask whether the proposed anti-replication mechanism survives the worst legal shell growth.

**Finding:** it does not. Saturating `mu(B_r)~Mr` still gives geometric convergence. The pressure-gradient variant also converges, so adding one spatial derivative does not rescue raw divergence.

**Strongest objection:** a temporal accumulation of individually finite shell effects could still be decisive; this falsifier is intentionally instantaneous.

**Vote:** `FAIL_INSTANTANEOUS_PRESSURE_DIVERGENCE_MECHANISM`.

## 5. Formal-methods / assurance lead

**Background:** exact statement binding, proof-DAG scope, trace chronology and machine-auditable artifacts.

**Delegation:** verify the authority transition.

**Finding:** `NS-B1a` had a valid pre-candidate packet before `C001`; the result should append `CANDIDATE_PROPOSED -> FALSIFIER_RUN -> RESULT_RECORDED -> RESIDUAL_OPENED`. The failure record must target the mechanism family, not pressure generally.

**Strongest objection:** do not mark the failure as `VERIFIED_IMPOSSIBILITY`; alternative pressure-aware temporal or local mechanisms remain live.

**Vote:** `SUPPORTED_DIAGNOSIS_ONLY`.

## 6. Novelty / frontier lead

**Background:** neighboring-result search and source-bound claim control.

**Delegation:** assess whether the calculation is likely new and which current sources affect the next route.

**Finding:** Calderón–Zygmund/Morrey pressure localization is established territory; Bradshaw–Tsai gives a modern primary-source pressure-localization framework. Lei–Yang–Yuan gives a distinct bounded-mild backward-uniqueness route handling Calderón–Zygmund terms. Neither source supplies the missing finite-`I` to global-`L^3` bridge identified here.

**Strongest objection:** do not make a novelty claim from the specialized shell calculation.

**Vote:** `NO_NOVELTY_AUTHORITY / KEEP_SOURCES_AS_ROUTE_CONTEXT`.

## Cross-role discussion

The group considered four interpretations:

1. **Pressure solves the tail problem immediately.** Rejected: the far field is summable but no velocity-tail norm follows.
2. **Pressure is irrelevant.** Rejected: local, harmonic, temporal and coherent pressure effects remain untested.
3. **The whole Type-I route is dead.** Rejected: only one mechanism family was falsified.
4. **Move the atom from instantaneous pressure divergence to temporal pressure-aware shell flux.** Selected.

The selected move has the highest partition power because the current result proves that repeating more instantaneous far-field estimates in the same representation is unlikely to recover the missing global trace. A time-integrated shell balance can either produce a new summability mechanism or expose a second, sharper scale-accumulation failure.

## Consensus

`VERIFIED_LOCAL_CALIBRATION / INSTANTANEOUS_PRESSURE_DIVERGENCE_ROUTE_PRUNED / TEMPORAL_DYNAMICS_CHILD_OPENED / SAME_CONTEXT_ONLY / NO_NOVELTY / ROOT_AUTHORITY_NONE`

Next atom: `NS-B1a1`, with a fresh context/memory/review/trace packet required before candidate generation.
