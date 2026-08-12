# NS-B1a3b1b C001 — two-core critical-scaling morphology falsifier

Authority: `SCOPED_ANALYTIC_ROUTE_PRUNING / PROPOSAL_SHADOW / NO_NAVIER_STOKES_COUNTEREXAMPLE / ROOT_AUTHORITY_NONE`.

## Proposition — weak-`L^{3/2}` critical amplitude does not select a one-center critical-point source family

There exists a family of smooth compactly supported divergence-free vorticity fields `omega_r` on `R^3`, `r -> 0`, such that:

1. `sup_r ||omega_r||_{L^{3/2,infinity}} < infinity` (indeed the distribution quasi-norm is exactly independent of `r` up to the fixed two-copy factor);
2. for thresholds `lambda_r ~ r^-2`, the super-level set `{|omega_r| > lambda_r}` contains two components whose centers remain a fixed positive distance apart;
3. consequently there is no fixed constant `C` for which those super-level sets can all be contained in **any** one-center ball of radius `R_r <= C lambda_r^-1/2`.

Therefore a bare inference

`uniform weak-L^{3/2} vorticity amplitude (+ divergence-free smoothness) -> Grujic-v2 one-center critical-point morphology`

is false. This statement does **not** address the stronger implication `Navier-Stokes + finite I -> morphology`.

## Construction

Choose `chi in C_c^infinity(B_1)` with `chi=1` near the origin and define a compactly supported vector potential

`A(x) = (0,0,chi(x) x_2)`.

Let `omega_0 = curl A`. Then `div omega_0 = 0`, `omega_0` is smooth and compactly supported, and `omega_0=e_1` on a ball `B_rho(0)` for some `rho>0` after choosing the region where `chi=1` sufficiently small.

Fix `L>2` and the separated centers `a_+ = L e_1`, `a_- = -L e_1`. For sufficiently small `r>0`, define

`omega_r(x) = r^-2 [ omega_0((x-a_+)/r) + omega_0((x-a_-)/r) ]`.

The two supports are disjoint. Each field is smooth, compactly supported and divergence free.

## Exact weak-Lorentz scaling

Let

`mu_0(s) = |{y: |omega_0(y)| > s}|`

and `mu_r(lambda)=|{x:|omega_r(x)|>lambda}|`. Disjointness gives the exact distribution identity

`mu_r(lambda) = 2 r^3 mu_0(lambda r^2)`.

For `p=3/2`, the standard distribution-function weak-Lorentz quasi-norm is

`sup_{lambda>0} lambda mu(lambda)^(2/3)`.

Hence, with `s=lambda r^2`,

`lambda mu_r(lambda)^(2/3)`
` = lambda [2 r^3 mu_0(lambda r^2)]^(2/3)`
` = 2^(2/3) (lambda r^2) mu_0(lambda r^2)^(2/3)`
` = 2^(2/3) s mu_0(s)^(2/3)`.

Taking the supremum yields

`||omega_r||_{L^{3/2,infinity},dist} = 2^(2/3) ||omega_0||_{L^{3/2,infinity},dist}`,

independent of `r`. No numerical approximation is used.

## Exact one-center containment contradiction

Because `omega_0=e_1` on `B_rho(0)`, each `omega_r` has magnitude exactly `r^-2` on the two balls

`B_{rho r}(a_+)` and `B_{rho r}(a_-)`.

Set `lambda_r = (1/2) r^-2`. Then

`B_{rho r}(a_+) union B_{rho r}(a_-) subset { |omega_r| > lambda_r }`.

Any Euclidean ball containing this super-level set must contain both centers `a_+` and `a_-`, whose separation is `2L`. Therefore its radius is at least `L`.

By contrast, the Grujić Definition-2.1 profile supplies a scale bound of the form

`R_r <= C lambda_r^-1/2 = C sqrt(2) r`.

For any fixed `C`, choosing `r < L/(C sqrt(2))` gives `C sqrt(2) r < L`, contradicting the required containment. The contradiction holds for an arbitrary choice of ball center, so it is stronger than merely failing an origin-centered representation.

## Source interpretation

The primary consumer itself already distinguishes the coordinates: Grujić v2 Theorem 4.1 assumes conformity to the critical-point profile and says **in particular** that vorticity lies in the uniform weak-`L^{3/2}` class. The two-core family verifies why the implication cannot be reversed on amplitude information alone.

This closes only the **bare representation** subproblem: critical Lorentz amplitude does not encode source-family uniqueness/single-core morphology.

## Interfaces that remain open

### Local mathematical residual

`NSE + finite I -> one-center critical-point morphology` remains open. An equation-specific mechanism could in principle use singular-point recentering, minimality, no-dichotomy, persistence, unique-core selection, or additional Type-I information absent from the hostile family.

### Local-to-global / gluing residual

Even if one local core is selected after blow-up, a same-theory bridge must still control translating/dilating secondary profiles, far-field vorticity/strain, the global weak-Lorentz input, and the fact that the selected Grujić theorem is a pre-singularity criterion while the Albritton–Barker producer route naturally passes through an ancient solution. This is recorded separately from the local representation failure.

### Downstream hypotheses not manufactured here

- no log-BMO vorticity-direction certificate is produced;
- pressure localization is not checked by the non-solution family;
- backward uniqueness is not activated;
- no equation-preserving limit theorem is established;
- no Type-II scenario is affected.

## Same-context expert verdict

All six frozen roles accepted the narrow distribution-function calculation and arbitrary-center containment contradiction. The Type-I and concentration-compactness roles explicitly rejected the overclaim that this disproves a PDE-specific one-core selection theorem. The formal-assurance role assigns at most shadow novelty class `REPRESENTATION_NOVEL`; this is a route-diagnostic representation result, not a claim of mathematical novelty in the literature.

## Outcome

`PARTIAL_SUCCESS / REPRESENTATION_ROUTE_PRUNING`.

Residual before: the Grujić consumer was being tracked mainly through amplitude and direction inputs, leaving it unclear whether its critical-point morphology could be treated as shorthand for critical Lorentz amplitude.

Residual after: the one-center morphology is source-bound and independently necessary for that consumer; amplitude alone cannot supply it. Any continuation of this route must either produce an equation-specific one-core/no-dichotomy certificate from the finite-`I` class or choose a consumer whose source family is compatible with the actual ancient-limit class.
