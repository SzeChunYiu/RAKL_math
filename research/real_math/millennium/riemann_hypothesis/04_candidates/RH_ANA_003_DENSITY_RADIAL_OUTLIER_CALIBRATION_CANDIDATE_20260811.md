# RH-ANA-003 candidate calibration — aggregate counting does not control Li radial outliers

**Candidate ID:** `CAL-RH-ANA-003-DENSITY-RADIAL-OUTLIER`  
**Atom:** `RH-ANA-003`  
**Candidate frozen:** 2026-08-11T12:19:00+00:00  
**Authority sought:** `KNOWN_ANSWER_LOGIC_CALIBRATION_ONLY`  
**Root authority sought:** `NONE`

## Frozen statement

Let `Z0` be a multiset of points on the critical line `Re(rho)=1/2`, closed under complex conjugation, whose counting function satisfies
\[
N_{Z_0}(T)=O(T\log T).
\]
Fix one off-critical point
\[
\rho_0=\beta+i\gamma,\qquad 0<\beta<1/2,\quad \gamma\ne0,
\]
and adjoin the symmetry quartet
\[
Q=\{\rho_0,\overline{\rho_0},1-\rho_0,1-\overline{\rho_0}\}.
\]
Put `Z=Z0 union Q`.

For
\[
\Lambda_n(T;Z)
=
\sum_{\rho\in Z,\;|\Im\rho|\le T}
\left[1-\left(1-\frac1\rho\right)^n\right],
\]
the aggregate count remains
\[
N_Z(T)=N_{Z_0}(T)+O(1)=O(T\log T),
\]
but, once `T=sqrt(n)` contains `Q`, the quartet contribution is exponentially large along an infinite subsequence of `n`. Consequently
\[
\Lambda_n(\sqrt n;Z)\ne O(\sqrt n\log n).
\]

Therefore an aggregate zero-count or zero-density premise that still permits a fixed symmetry-compatible off-line quartet is **not by itself** sufficient to imply the RH-compatible incomplete-Li bound.

## Intended proof skeleton

Define
\[
z=1-\frac1{\rho_0}.
\]
Then
\[
|z|^2
=
1+\frac{1-2\beta}{\beta^2+\gamma^2}>1.
\]
The quartet contribution equals
\[
4-2\Re(z^n+z^{-n}).
\]
Writing `z=R e^{i theta}` with `R>1`, there are infinitely many positive integers `n` for which `cos(n theta)` is bounded below by a fixed positive constant (periodicity if `theta/2pi` is rational; elementary Diophantine approximation otherwise). Along that subsequence the quartet term has magnitude comparable to `R^n`.

For every point of `Z0`, the corresponding Li radial factor has modulus one, so each summand has magnitude at most two. Since only `O(sqrt(n) log n)` points of `Z0` enter the cutoff, their total contribution is `O(sqrt(n) log n)`. The exponential quartet term therefore dominates along the selected subsequence.

## Counterexample-first falsifier

Try to invalidate the statement by one of:

1. showing quartet symmetry cancels the exponential term for every `n`;
2. showing the fixed quartet necessarily changes an `O(T log T)` count premise by more than its allowed error;
3. showing the on-line reference contribution can be exponentially large despite unit radial factors and `O(T log T)` count;
4. finding a hidden assumption that makes the construction ineligible for the claimed *logic-calibration* scope.

Any such failure rejects this candidate. Success only prunes aggregate-count/density inference forms that permit the outlier; it does not apply to weighted density or direct arithmetic cancellation theorems unless their hypotheses also admit the construction.
