# RH-ANA-003 — aggregate density/zero-free bridge audit

**Candidate:** `C-RH-ANA-003-ZD-EXCEPTION-BRIDGE`  
**Outcome:** `REFUTED_ROUTE_LOCAL / PARTIAL_SUCCESS_AS_OBSTRUCTION`  
**Root authority:** `NONE`

## Frozen claim under test

Current aggregate zero-density and zero-free inputs, with the standard zeta zero symmetries but without any additional pointwise exceptional-zero theorem, suffice *by themselves* to provide the missing all-index sign/tail bridge needed to turn the exact Bombieri–Lagarias/Li representation into `lambda_n >= 0` for every `n`.

This is deliberately narrower than the statement that zero-density information can never be useful inside a stronger zeta-specific proof.

## Counterexample-first bridge audit

Use a planted off-critical quartet closed under conjugation and the functional-equation reflection,

`Q_T = {3/4+iT, 3/4-iT, 1/4+iT, 1/4-iT}`,

with `T` arbitrarily large. This is a calibration of the inference form only; it is not asserted to be the zero set of the Riemann zeta function.

### Zero-free input does not extinguish the exception

Bellotti–Trudgian–Yang, arXiv:2603.21490, Theorem 1, proves zero-freeness only in the boundary region

`Re(s) > 1 - 1/(4.896 log |Im(s)|)` for `|Im(s)| >= 3`.

For sufficiently large `T`, the boundary is close to `1`, so a planted zero with real part `3/4` lies well outside the excluded region. The theorem therefore supplies no pointwise exclusion of this quartet.

### Zero-density input does not extinguish the exception

Guth–Maynard, arXiv:2405.20552v2, gives

`N(sigma,T) <= T^(30(1-sigma)/13 + o(1))`.

At `sigma=3/4` the displayed exponent is `15/26 > 0`. Hence this aggregate upper bound grows with `T`; by itself it cannot force `N(3/4,T)=0`. In particular, the logical content of the bound does not exclude a finite exceptional set such as one off-critical symmetric quartet.

### The exceptional quartet is Li-sensitive

For the left partner `rho_L=1/4+iT`,

`|1-1/rho_L|^2 = |rho_L-1|^2/|rho_L|^2 = (T^2+9/16)/(T^2+1/16) > 1`.

Thus the Li transform retains exponentially amplified sensitivity to such an off-line partner as the coefficient index grows. This is consistent with Voros, arXiv:math/0506326, which records the RH/non-RH large-`n` dichotomy: RH gives the tempered `n(A log n+B)` asymptotic, whereas failure of RH gives non-tempered oscillatory behavior. The earlier exact `RH-ANA-001` quartet calibration remains the regression witness that a single symmetric off-line defect can be invisible for a long finite prefix and then change sign.

## Result

The tested aggregate inputs do **not** contain the missing preservation theorem. They measure rarity or exclude a thin boundary near `Re(s)=1`, while the target is exception-free and all-index: one permitted off-line zero pair is enough to leave the Li sign bridge uncontrolled. Therefore the candidate implication is refuted as stated.

This does **not** refute zero-density, zero-free, mollifier, resonance, or explicit-formula methods as ingredients. It rules out treating their present aggregate conclusions alone as the root-critical bridge.

## Episode / diagnosis / obstruction separation

**Episode outcome.** The current zero-density and zero-free frontier was connected to the exact Li target and tested with the predeclared single-exception falsifier. The candidate failed; the cycle nevertheless reduced the route space.

**Diagnosis.** `GLUING + REPRESENTATION`: an aggregate exceptional-set representation discards the pointwise phase/amplitude information needed by the universal all-`n` Li sign target. The gap is a quantifier mismatch (`few` versus `none`) plus a representation mismatch (counting exceptions versus controlling each exceptional contribution in an oscillatory transform).

**Obstruction / lesson.** `O-RH-ANA-003-AGGREGATE-EXCEPTION-GAP`: any future density/mollifier-to-Li bridge must include an explicit exceptional-set **extinction or exact neutralization theorem** and must survive the planted-single-exception regression. Merely improving an exponent or a critical-line proportion does not close this atom.

## Residual after the audit

Search must now remain in an exceptional-zero-sensitive representation: either derive an exact zeta-specific prime/archimedean cancellation identity that controls each possible off-line contribution uniformly in `n`, or prove a genuinely weaker pointwise theorem that forces the exceptional set to vanish. The statement `N(sigma,T)=0` for every `sigma>1/2` and all heights is not a cheaper bridge; it is essentially the root zero-location requirement.

## Novelty and authority

Novelty class: `PROJECT_LOCAL_STRUCTURAL_OBSTRUCTION / NOT_A_NEW_MATHEMATICS_CLAIM`. No bounded literature novelty certificate was opened because no new theorem is claimed. Numerics, where mentioned, are calibration/falsification only.

Primary anchors: Guth–Maynard arXiv:2405.20552v2; Bellotti–Trudgian–Yang arXiv:2603.21490; Voros arXiv:math/0506326; Bombieri–Lagarias, JNT 77 (1999), DOI 10.1006/jnth.1999.2392.
