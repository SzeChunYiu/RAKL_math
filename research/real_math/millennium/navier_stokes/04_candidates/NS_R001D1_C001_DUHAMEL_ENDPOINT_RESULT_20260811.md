# NS-R001d1-C001 — unsigned Duhamel endpoint result

**Atom:** `NS-R001d1`
**Candidate:** `NS-R001d1-C001`
**Candidate commit:** `54974135e15027d58eae1dba474aec685b74e4f7`
**Frozen pre-candidate gate head:** `595abaa60190dbc63b335f0d1285d11995050e25`
**Framework re-read for this result:** `SzeChunYiu/RAKL@decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8`
**Application main inspected before result:** `SzeChunYiu/RAKL_math@5d6bdc6f566921f51a375fdc2e8035123cf4830c`
**Authority:** `SUPPORTED_PROOF_ARCHITECTURE_ENDPOINT_GAP / NO_NAVIER_STOKES_COUNTEREXAMPLE / NO_ROOT_AUTHORITY`

## Predeclared falsifier

The frozen candidate asks whether the scalar convolution
\[
J_t(g)=\int_0^t (t-s)^{-3/4}g(s)\,ds
\]
can obey
\[
J_t(g)\le K(t)\|g\|_{L^2(0,t)}
\]
with finite `K(t)` for every nonnegative `L^2` profile retained by the unsigned semigroup/energy reduction.

For fixed `t>0` and `0<epsilon<t`, use the registered near-diagonal pulse
\[
g_\epsilon(s)=\epsilon^{-1/2}\mathbf 1_{(t-\epsilon,t)}(s).
\]
Then
\[
\|g_\epsilon\|_2^2
=\epsilon^{-1}\int_{t-\epsilon}^t ds=1,
\]
while, with `r=t-s`,
\[
J_t(g_\epsilon)
=\epsilon^{-1/2}\int_0^\epsilon r^{-3/4}dr
=4\epsilon^{-1/4}
\longrightarrow\infty.
\]

Therefore no finite `K(t)` exists for the registered scalar `L^2_t -> pointwise` endpoint closure. The candidate hypothesis `H_endpoint` is refuted.

## Exact scope

This result does **not** refute Navier–Stokes regularity, the Duhamel formula, or any estimate exploiting information discarded by the scalar reduction. The pulse is a hostile profile in the information class retained after taking norms; it is not asserted to be the time profile of a Navier–Stokes trajectory.

The failure is specifically:

`F-NS-R001D1-C001-UNSIGNED-DUHAMEL-ENDPOINT`

> Leray energy gives a time-integrated `L^2_t L^6_x` control, but after the exact derivative heat kernel is reduced to an unsigned scalar convolution, near-diagonal temporal concentration defeats pointwise critical `L^3_x` closure.

Pressure/Leray cancellation, sign/coherence, local-energy structure, time-frequency localization, tent/Carleson geometry, frequency-local critical smallness, and projected-strain depletion remain live.

## Post-result exponent diagnostic

This calculation exposes a more general representation warning. Suppose both factors are taken only from the standard energy interpolation line
\[
u\in L_t^{p_i}L_x^{q_i},\qquad
\frac2{p_i}+\frac3{q_i}=\frac32.
\]
For a product in `L^r_x`, `1/r=1/q_1+1/q_2`, the derivative heat map into `L^3_x` has temporal singularity
\[
a=\frac3{2r}.
\]
The product time exponent satisfies `1/m=1/p_1+1/p_2`, hence exactly
\[
a+\frac1m=\frac32.
\]
A pointwise-in-time convolution Hölder closure would require `a+1/m<1`. Thus the global unsigned Lebesgue/energy architecture has a fixed one-half exponent deficit, independent of how the two energy interpolation exponents are chosen.

If one factor is already assumed in the target critical class `L^\infty_tL^3_x` and the other remains on the energy line, the same calculation gives
\[
a+\frac1m=\frac54,
\]
a fixed one-quarter deficit. If both factors are in `L^\infty_tL^3_x`, the ordinary scalar estimate reaches the logarithmic endpoint `a=1`.

These identities are post-result route diagnostics, not a newly preregistered theorem candidate. They explain why retrying global unsigned Hölder interpolation is low-information.

## Near-solved contrast: what successful critical closures add

Cheskidov--Eguchi (`arXiv:2503.11642`) prove a finite-energy global smoothness result only after adding frequency-local critical smallness: high frequencies are controlled in a local `BMO^-1` coordinate and low frequencies in `\dot B^{-1}_{\infty,\infty}`. Their nonlinear space includes a time-weighted `L^\infty_x` quantity and a local spacetime Carleson-type `L^2` quantity, together with frequency/time decomposition; it is not the scalar `L^2_tL^6_x` convolution tested here.

Barker--Prange (`arXiv:1812.09115`) likewise obtain localized smoothing from a scale-critical local `L^3` hypothesis rather than from energy alone. Miller (`arXiv:2407.02691`) supplies conditional strain/vorticity depletion coordinates, not the missing finite-energy bridge. Coiculescu--Palasek (`arXiv:2503.14699`) warn against equating membership in a large critical space with the small-data regime.

The common lesson is representation-level: successful critical bilinear control uses structure that the unsigned global Lebesgue reduction erases.

## Local-to-global/gluing residual

The local mathematical subproblem is now closed at its scoped level: the registered `H_endpoint` inequality is false.

The root-gluing problem is still open. Existing critical-space theorems do not glue to the Clay data class because the load-bearing critical smallness/coherence hypothesis has not been generated from arbitrary finite energy. The next bridge must explain **dynamic suppression of critical high-frequency replenishment or an equivalent cancellation-aware coordinate**, not merely positive-time heat smoothing.

## Next atom

Open proposal-only child:

`NS-R001d2 — DYNAMIC_HIGH_FREQUENCY_REPLENISHMENT`

Exact context question:

> Which critical time-frequency/Carleson or frequency-local quantity used by successful mild-solution closures is not controlled by Leray energy, and can exact Navier–Stokes evolution constrain the nonlinear replenishment of that quantity without assuming the small critical datum one is trying to generate?

The first action must be source/interface mapping and a fresh strict context packet, not theorem invention.

## Novelty boundary

The pulse calculation and exponent bookkeeping are elementary consequences of the frozen semigroup architecture. This cycle assigns the solved subproblem `RAKL_TRIVIAL` at proposal-only metrology: no new mathematical operator was required. This classification is an internal search-policy description, not a novelty claim about the literature.
