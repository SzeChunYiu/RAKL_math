# RH-ANA-003 result — finite-place density/radial sufficiency audit

**Result ID:** `RH-ANA-003-DENSITY-RADIAL-NO-GO`  
**Candidate:** `CAL-RH-ANA-003-DENSITY-RADIAL-OUTLIER`  
**Authority:** `SUPPORTED_GENERIC_LOGIC_CALIBRATION / ROUTE_PRUNING_ONLY`  
**Root authority:** `NONE`  
**Framework:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`

## Result

The frozen calibration survives its counterexample-first falsifiers.

> **Scoped no-go.** Aggregate zero-count or zero-density information that still permits one fixed functional-equation/conjugation-symmetric off-critical quartet cannot, by itself, imply an `O(sqrt(n) log n)` bound for the incomplete Li coefficient cut at height `sqrt(n)`.

This is a theorem about the stated generic symmetric-multiset inference form. It is **not** a theorem that every zero-density method is useless for zeta. A weighted density theorem, a zero-free theorem, or a direct prime-side cancellation theorem may contain additional horizontal/radial information that excludes the hostile quartet.

## Proof of the calibration

Let `Z0` lie on the critical line and satisfy `N_Z0(T)=O(T log T)`. For every `rho in Z0`,
\[
\left|1-\frac1\rho\right|=1,
\]
so each term
\[
1-\left(1-\frac1\rho\right)^n
\]
has magnitude at most `2`. Therefore
\[
\left|\Lambda_n(\sqrt n;Z_0)\right|
\le 2N_{Z_0}(\sqrt n)
=O(\sqrt n\log n).
\]

Now fix
\[
\rho_0=\beta+i\gamma,\qquad 0<\beta<\frac12,
\]
and add
\[
Q=\{\rho_0,\bar\rho_0,1-\rho_0,1-\bar\rho_0\}.
\]
Adding four points changes any ordinary counting asymptotic only by `O(1)`.

Set
\[
z=1-\frac1{\rho_0}=Re^{i\theta}.
\]
Direct algebra gives
\[
R^2
=
\frac{(\beta-1)^2+\gamma^2}{\beta^2+\gamma^2}
=
1+\frac{1-2\beta}{\beta^2+\gamma^2}>1.
\]
The four Li radial factors attached to the quartet are `z`, `bar(z)`, `z^{-1}` and `bar(z)^{-1}`. Hence its contribution is
\[
Q_n=4-2\operatorname{Re}(z^n+z^{-n})
=4-2(R^n+R^{-n})\cos(n\theta).
\]

There are infinitely many `n` for which `cos(n theta)` is at least a fixed positive constant. If `theta/(2 pi)` is rational this follows by periodicity; if it is irrational it follows from elementary Diophantine approximation of integer multiples of `theta/(2 pi)` to an integer. Along such a subsequence,
\[
Q_n=-\Omega(R^n).
\]
Once `n >= gamma^2`, the cutoff `sqrt(n)` contains the quartet. Therefore
\[
\Lambda_n(\sqrt n; Z_0\cup Q)
=
\Lambda_n(\sqrt n;Z_0)+Q_n,
\]
and the exponential quartet term dominates the `O(sqrt(n) log n)` critical-line background along an infinite subsequence. Thus the desired incomplete-Li bound fails while the aggregate counting law is unchanged up to `O(1)`.

## Exact hostile witness

The previous RH-ANA-001 calibration used `rho_0=1/4+100i`. For this point,
\[
\left|1-\frac1{\rho_0}\right|^2
=
\frac{160009}{160001}>1
\]
exactly. The deterministic numerical oracle in this cycle finds, for example, `n=539727`, where the quartet contribution is about `-1.445e6`, while `sqrt(n) log n` is about `9.697e3`. This numerical value is calibration only; the result above follows from the exact radius and infinite-subsequence argument.

## Source interpretation

Lagarias' Theorem 6.1 gives the exact source cut
\[
S_f(n,\pi)
=
\lambda_n(\sqrt n,\pi^\vee)+O_\pi(\sqrt n\log n),
\]
and states the small incomplete-Li estimate separately under RH. The present no-go explains why merely combining the standard zero count with that formula does not recover the RH-conditional bound: the count controls the number of powered terms, not the largest radial amplification.

Palojärvi's explicit `tau`-Li results independently reinforce the same structural distinction by connecting Li-type signs to zeros outside radial regions and treating low/high zero contributions separately.

## What was eliminated

The following method family is now a supported scoped failure:

```text
ordinary aggregate zero counting/density
+ no additional outlier/radial exclusion
=> uniform incomplete-Li finite-place control
```

It should not be retried under a new notation without a DifferenceWitness showing what additional horizontal/radial or arithmetic cancellation information has been added.

## What remains alive

Three materially different routes survive:

1. **weighted horizontal/radial control** that does not permit the hostile fixed quartet;
2. **direct prime-side cancellation** in the exact regularized arithmetic formula, which may exploit structure lost by zero-density abstraction;
3. **global Li-growth exclusion** in the Lagarias–Voros direction, provided the required unconditional growth estimate is not simply root-equivalent in disguise.

The first is selected as the next child because it is the smallest repair exposed directly by this falsifier. No candidate for that repair is proposed here.

## Authority boundary

The Riemann Hypothesis remains `OPEN_NO_SOLUTION_CERTIFICATE`. This calibration neither finds an off-critical zeta zero nor proves any new zero-free region. It prunes an inference family and sharpens the next exact obstruction.
