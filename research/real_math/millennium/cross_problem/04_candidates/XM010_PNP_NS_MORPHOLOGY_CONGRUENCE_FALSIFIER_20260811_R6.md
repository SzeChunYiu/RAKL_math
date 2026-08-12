# XM010 — PNP projection congruence -> Navier–Stokes morphology falsifier

**Cycle:** `XM010-PNP-NS-MORPHOLOGY-CONGRUENCE-20260811-R6`  
**Authority:** `PROPOSAL_SHADOW_ROUTE_DIAGNOSTIC / NO_NAVIER_STOKES_THEOREM / NO_ROOT_AUTHORITY`  
**Framework read before execution:** `SzeChunYiu/RAKL@eeca4ea13ad7e2b2bc2fd4d7420ad05a81f654ca`, method `3.0.0`.  
**RAKL_math base:** `47f56df0492339097a651d40b6c7289c4e2d4034`.  
**Prospective execution freeze:** commit `edd223bbecca120b3590dba7966ff88ae4bfd53c`, after durable target contract `RAKL_math#145`.  
**Chronology guard:** the two-core idea itself predates the durable issue and receives no prospective hypothesis-generation credit. Only this exact execution/mapping is prospectively frozen.

## 1. Source and target

The source operation is the P-vs-NP projection-congruence diagnostic: a coarse state representation is not sufficient for a downstream outcome if two states have the same projection but different downstream outcomes. Only that research-control operation transfers; no P-vs-NP mathematics transfers.

The target is `NS-B1a3b1b`. Grujić, arXiv:2607.08866v2, Definition 2.1 treats a one-center critical point profile of the form `omega = Phi |x|^{-2}` with bounded shape factor; the source states as a structural consequence that sufficiently high vorticity superlevel sets fit inside one ball with radius bounded by `C lambda^{-1/2}`. Albritton–Barker, arXiv:1811.00502, supplies the separate finite-`I` Type-I/ancient state space. This cycle asks a strictly weaker representation question first:

> Does the critical weak-`L^{3/2}` vorticity-amplitude coordinate, even together with smoothness, compact support, and divergence-freeness, determine the required one-center high-threshold morphology?

If not, an equation-specific producer theorem must carry additional geometry/rigidity; amplitude alone cannot be the faithful state.

## 2. Exact hostile family

Choose `psi in C_c^infty(B(0,1))` with nonzero horizontal gradient and set

`W = curl(0,0,psi) = (partial_2 psi, -partial_1 psi, 0)`.

Then `W` is nonzero, smooth, compactly supported in `B(0,1)`, and divergence-free. Fix `z0` with

`m := |W(z0)| > 0`.

Let

`p = 3/2`, `c = 2^{-2/3}`, and `0 < epsilon < 1`.

Define a one-core and a separated two-core field by

`omega_1,epsilon(x) = epsilon^{-2} W(x/epsilon)`,

`omega_2,epsilon(x) = c epsilon^{-2} [ W((x-e_1)/epsilon) + W((x+e_1)/epsilon) ]`.

For `epsilon<1` the two supports are disjoint.

These fields are smooth, compactly supported and divergence-free. They are **not asserted to solve Navier–Stokes**.

## 3. Exact weak-`L^{3/2}` equality

Use the Lorentz weak norm in its distribution/rearrangement form

`||f||_{L^{p,infinity}} = sup_{t>0} t mu_f(t)^{1/p}`,

where `mu_f(t)=|{x: |f(x)|>t}|`.

For the critical scaling `f_epsilon(x)=epsilon^{-2} f(x/epsilon)` in dimension three and `p=3/2`,

`mu_{f_epsilon}(t)=epsilon^3 mu_f(t epsilon^2)`.

Hence

`||f_epsilon||_{L^{3/2,infinity}} = ||f||_{L^{3/2,infinity}}`.

Therefore

`|| |omega_1,epsilon| ||_{L^{3/2,infinity}} = || |W| ||_{L^{3/2,infinity}} =: M`.

For two disjoint identical copies scaled by `c`, the distribution function satisfies

`mu_2(t) = 2 mu_1(t/c)`.

Thus

`|| |omega_2,epsilon| ||_{L^{3/2,infinity}}
 = c 2^{1/p} M
 = 2^{-2/3} 2^{2/3} M
 = M`.

So the one-core and two-core fields have **exactly the same critical weak-`L^{3/2}` amplitude norm**, not merely comparable norms.

## 4. Same projection, different one-center morphology

Fix the common threshold

`lambda_epsilon = (c m/2) epsilon^{-2}`

and the fixed constant

`C_0 = sqrt(c m/2)`.

Then

`C_0 lambda_epsilon^{-1/2} = epsilon`.

For the one-core field, its entire support is contained in `B(0,epsilon)`, hence its `lambda_epsilon`-superlevel set is also contained in the one ball

`B(0, C_0 lambda_epsilon^{-1/2})`.

For the two-core field, the points

`p_+ = e_1 + epsilon z0`,

`p_- = -e_1 + epsilon z0`

satisfy

`|omega_2,epsilon(p_+)| = |omega_2,epsilon(p_-)| = c epsilon^{-2} m > lambda_epsilon`.

Their separation is exactly

`|p_+ - p_-| = 2`.

Any Euclidean ball containing both therefore has radius at least `1`, whereas the registered one-center radius at the same threshold and same fixed `C_0` is `epsilon<1`. Hence the two-core superlevel set cannot fit in any ball of radius `C_0 lambda_epsilon^{-1/2}`.

Define the coarse projection

`pi(omega) = (smooth, compactly-supported, divergence-free, || |omega| ||_{L^{3/2,infinity}})`

and the downstream outcome

`Q_{C_0,lambda_epsilon}(omega) = 1` iff the `lambda_epsilon`-superlevel set is contained in one ball of radius `C_0 lambda_epsilon^{-1/2}`.

Then

`pi(omega_1,epsilon) = pi(omega_2,epsilon)`

but

`Q(omega_1,epsilon)=1`, `Q(omega_2,epsilon)=0`.

This is the registered **DifferenceWitness**. The weak-`L^{3/2}` amplitude projection is not a congruence for the one-center morphology outcome on this hostile smooth divergence-free class.

A stronger family-level statement also follows: the two-core amplitude norm remains fixed as `epsilon -> 0`, while for any fixed candidate containment constant `C`, the permitted radius `C lambda_epsilon^{-1/2}` is `O(epsilon)` and eventually below `1`; the two macroscopic cores remain distance `2` apart. Thus no fixed one-center constant can be inferred from the amplitude bound alone on this class.

## 5. What this does and does not close

**Closed only as a representation-level route diagnostic:** a critical weak-`L^{3/2}` amplitude signature, even on smooth compactly supported divergence-free fields, cannot by itself encode Grujić's one-center high-vorticity morphology.

**Still open and kept separate:**

- `LOCAL_MATH / NSE_SPECIFIC`: whether the Navier–Stokes equation plus finite `I` supplies an equation-specific one-center/recentering/rigidity theorem;
- `LOCAL_REPRESENTATION`: the separate log-BMO vorticity-direction coordinate;
- `LOCAL_TO_GLOBAL_GLUE`: global Lorentz/far-field/tail compatibility;
- `STATE_SPACE_GLUE`: pre-singularity Grujić conditions versus ancient-solution Liouville state space;
- `NONCOMPACT_SYMMETRY`: whether a valid blow-up recentering theorem rules out persistent multiple-core leakage;
- `TYPE_II`: untouched.

The hostile fields cannot refute `NSE + finite I -> morphology` because they are not NSE solutions. That exact DifferenceWitness is the principal disanalogy from the target theorem question.

## 6. Same-context expert cell

Seven same-context roles reviewed the result; none receives independent-review credit.

1. **Representation/congruence analyst:** verifies that equal projected state plus different registered outcome is exactly the transferred operation and that only the operation, not PNP content, moved across problems.
2. **Navier–Stokes Type-I analyst:** accepts only the representation-level no-go; rejects any statement that finite `I` plus NSE has been falsified.
3. **Lorentz/scaling analyst:** checks the `epsilon^{-2}` critical scaling and the disjoint-copy factor `2^{-2/3}` giving exact norm equality.
4. **Vorticity-morphology analyst:** checks the two superlevel points, distance-two radius lower bound, and the one-center `lambda^{-1/2}` scale.
5. **Adversarial falsification analyst:** tests overreach; requires explicit separation of amplitude, direction, far-field, recentering and state-space obligations.
6. **Primary-source/provenance analyst:** limits the consumer claim to the current cited Grujić v2 structural consequence and the producer state space to Albritton–Barker.
7. **RAKL v3 assurance/metrology analyst:** requires proposal/shadow TaskEpisode storage, episode -> diagnosis -> obstruction/lesson separation, zero protected novelty counts absent a retention gate, and no root/promotion authority.

Consensus: `PARTIAL_SUCCESS_ROUTE_PRUNING / REPRESENTATION_CONGRUENCE_FAIL`. Independent mathematical review count: `0/3`.

## 7. Verification boundary

The norm equality and radius contradiction above are analytic. A finite distribution-function calibration was also run as a regression of the copy/scaling arithmetic; it is calibration only and carries no proof authority. No formal verifier, dependency/axiom audit, isolated recheck, novelty certificate, or root proof DAG is supplied.

**Next action:** search only for an equation-specific finite-`I` -> one-center morphology/recentering theorem or a source-native geometric coordinate that survives the hostile two-core regression. Do not spend another cycle treating critical amplitude alone as a faithful morphology carrier.