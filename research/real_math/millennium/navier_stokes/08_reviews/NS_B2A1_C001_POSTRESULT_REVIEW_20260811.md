# NS-B2a1-C001 post-result same-context audit

**Reviewed artifact:** `01_frontier/NS-B2a1_C001_LOCAL_TO_TAIL_QUANTIFIER_AUDIT_20260811.md`  
**Blob:** `23cb332d429b07bfbfc1f060c5a0337933b0e24b`  
**Authority of this review:** same-context adversarial review only; not independent peer review.

## Domain/PDE pass

The calibration is correctly separated from the PDE claim. Seregin's paper records fixed-cylinder compactness under the Euler scaling and Theorem 3.1 yields a nontrivial ancient Euler limit with local scale-weighted bounds. The constructed `W_k` sequence is not asserted to satisfy the Euler or Navier–Stokes equations. Therefore the result may prune only the inference from local compactness/boundedness to a global tail handoff.

**Strongest objection:** source nontriviality could invalidate a pure escape example.  
**Resolution:** the construction retains the fixed nonzero core `w_0`; local convergence is to a nonzero limit while a second packet escapes.  
**Vote:** `ACCEPT_SCOPED_RESULT`.

## Concentration-compactness / formal analysis pass

For each fixed compact set, the translated compact support is eventually disjoint, so convergence is actually exact on the compact set for all sufficiently large `k`. For each sufficiently large `R`, a later packet can be placed fully outside `B(R)`, giving a uniform positive lower bound on `sup_k` tail mass. This proves the noncommutation of fixed-radius convergence with uniform tail tightness.

**Strongest objection:** bounded local norms might fail uniformly as the translated packet crosses a centered ball.  
**Resolution:** smooth compact supports and compact time support give bounded small-scale contributions; when the translated support first enters a centered ball, the radius is comparable to `|x_k|`, while the packet norm is fixed, so scale normalization cannot blow up. This boundedness is a calibration property only, not a claim of the full Seregin (3.5)+(3.7) class.  
**Vote:** `ACCEPT`.

## Pressure/far-field pass

The velocity counterexample already suffices to refute a velocity-tail inference. The manuscript correctly refuses to extend the calibration automatically to pressure and explicitly leaves global pressure normalization/decomposition as a separate residual.

**Vote:** `ACCEPT_WITH_PRESSURE_RESIDUAL`.

## Euler-rigidity pass

The result does not claim a Liouville theorem and does not reject a genuinely local Euler rigidity theorem. It correctly states that a global-tail-based rigidity theorem needs a separately inherited tail/recentering/signed-flux hypothesis.

**Vote:** `ACCEPT / RIGIDITY_STILL_BLOCKED`.

## Vorticity/geometric-depletion pass

Translation covariance means analogous centered-local vorticity observations can also miss an escaping packet. No vorticity theorem is inferred.

**Vote:** `ACCEPT_SCOPE`.

## Adversarial pass

The two-packet version is materially stronger than the pending XM005 pure-moving-core calibration because the local limit remains nontrivial. It is materially different from pending PR #72 because it attacks the order-of-limits / tail-inheritance interface rather than scale homogeneity of absolute cutoff terms.

**Vote:** `NON_DUPLICATIVE / ACCEPT`.

## Formal assurance / novelty pass

The required strict chronology passed: context, memory, same-context expert review and the seven-event hash-chained pre-candidate trace were frozen before `NS-B2a1-C001` was written. No external novelty claim is warranted or made. The exact source wording should remain conservative: the paper explicitly lists fixed-`Q(a)` subsequence convergence in its scaling argument and then invokes the same compactness machinery for the later Euler-limit theorem; the calibration needs only that local topology, not a stronger global convergence claim.

**Vote:** `PROCESS_CLEAN / NO_ROOT_AUTHORITY`.

## Consensus

`SUPPORTED_SCOPED_COMPACTNESS_OBSTRUCTION / LOCAL_CONVERGENCE_ALONE_DOES_NOT_TRANSFER_UNIFORM_TAIL_TIGHTNESS / ACTUAL_PDE_MAY_SUPPLY_ADDITIONAL_STRUCTURE / NEXT_ATOM_PRELIMIT_UNIFORM_TAIL_OR_RECENTERING / ROOT_AUTHORITY_NONE`.

No reviewer in this same-context cell supports promotion to an Euler theorem, Navier–Stokes theorem or Clay-root claim.
