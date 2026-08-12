# NS-B2a1b1 — fixed-time signed-flux / asymptotic-density audit

**Authority:** proposal/shadow only.  **Root:** NS0 remains `OPEN_NO_SOLUTION_CERTIFICATE`.

## Frozen target

Work only in the Seregin 2026 Theorem 3.1 ancient-Euler state for the logarithmic case `F(a)=1`.  The source gives, uniformly in `a>0`,

\[
\sup_{-a^2<\tau<0}\frac1a\int_{B_a}|u|^2
+\frac1{a^2}\int_{Q(a)}|p|^{3/2}
+\frac1a\int_{Q(a)}|\nabla u|^2\le C,
\]

together with Euler and the one-sided local energy inequality (3.7).  No finite total energy, Onsager regularity, symmetry, moving-radius compactness, pressure sign, or energy equality is assumed.

Let `I=[t_1,t_2]` be a fixed compact interval in `(-∞,0)` and choose a smooth radial cutoff `χ_R(x)=χ(x/R)`, `0≤χ≤1`, `χ=1` on `B_1`, `χ=0` outside `B_2`, `|∇χ_R|≤C/R`.  For large `R`, `I×B_{2R}⊂Q(2R)`.

## Counterexample-first discriminator: sharp source envelope

The source bounds imply on the fixed interval `I`

\[
\sup_{t\in I}\|u(t)\|_{L^2(B_{2R})}^2\lesssim R,
\qquad
\int_I\!\int_{B_{2R}}|\nabla u|^2\lesssim R,
\qquad
\int_I\!\int_{B_{2R}}|p|^{3/2}\lesssim R^2.
\]

Local Sobolev on `B_{2R}` and time Hölder give

\[
\begin{aligned}
\int_I\!\int_{B_{2R}}|u|^3
&\lesssim
\sup_I\|u\|_2^{3/2}
\int_I\|u\|_6^{3/2}\,dt\\
&\lesssim_I
R^{3/4}
\Big(\int_I(\|\nabla u\|_2^2+R^{-2}\|u\|_2^2)dt\Big)^{3/4}
\lesssim_I R^{3/2}.
\end{aligned}
\]

Hence the convection contribution to the spatial-cutoff flux is

\[
\int_I\!\int |u|^3|\nabla\chi_R|\lesssim_I R^{1/2}.
\]

For pressure work, Hölder with exponents `3/2` and `3` gives

\[
\int_I\!\int |p|\,|u|\,|\nabla\chi_R|
\lesssim
R^{-1}(R^2)^{2/3}(R^{3/2})^{1/3}
\lesssim_I R^{5/6}.
\]

Therefore the full signed convection-plus-pressure boundary term obeys

\[
|\mathcal F_R(I)|\lesssim_I R^{5/6},
\qquad
\frac{|\mathcal F_R(I)|}{R}\lesssim_I R^{-1/6}\to0.
\]

The same estimate holds for a nonnegative dyadic shell test `χ_{2R}-χ_R`; this is obtained by applying the local-energy inequality directly to that shell test, **not** by subtracting two one-sided inequalities.  On dyadic radii the normalized error bound `R^{-1/6}` is geometrically summable.

## Consequence: a genuine large-radius Lyapunov observable

Approximate the time indicator of `[t_1,t_2]` by admissible nonnegative compact time cutoffs in (3.7).  For almost every admissible pair `t_1<t_2`,

\[
E_R(t_2)\le E_R(t_1)+\mathcal F_R([t_1,t_2]),
\qquad
E_R(t):=\int \chi_R|u(x,t)|^2\,dx.
\]

Divide by `R` and take `limsup_{R→∞}`.  The boundary term vanishes, so

\[
\Lambda_\chi(t):=\limsup_{R\to\infty}\frac{E_R(t)}R
\]

is finite and non-increasing forward in time (for the a.e.-time representative allowed by the source local-energy inequality):

\[
\Lambda_\chi(t_2)\le \Lambda_\chi(t_1).
\]

This is the retained local result of the cycle.  Pressure was not dropped; its worse fixed-time exponent `5/6` determines the rate.

## Hostile closure audit

The new monotone quantity does **not** close the Type-II exclusion:

1. Seregin's nontriviality condition (3.8) is a unit-scale spacetime norm.  It supplies no lower bound on the large-radius linear density `Λ_χ(t)`.
2. `Λ_χ(t)=0` is compatible with nonzero spatially localized or finite-energy configurations; therefore zero asymptotic linear density does not imply `u=0`.
3. Monotonicity gives no source-authorized terminal value at `t→0-` or `t→-∞` that would force the density to vanish.
4. The estimate is fixed-time-window.  It does not license replacing the common interval by an `R`-dependent parabolic interval and then claiming literal dyadic telescoping.
5. No pressure sign/coherence law was derived.  The calculation only proves sublinear magnitude on each fixed interval.

So the route is refined, not solved: **signed local-energy flux does yield a source-valid asymptotic-density Lyapunov law, but a local-nontriviality ↔ asymptotic-density bridge (or a terminal density condition) is missing.**

## Residual

New obstruction: `O-NS-B2a1b1-ASYMPTOTIC-DENSITY-LOCAL-NONTRIVIALITY-DISCONNECT`.

New failure signature: `F-NS-B2a1b1-LYAPUNOV-DENSITY-NO-RIGIDITY-BRIDGE`.

Next admissible atoms are either (i) prove a source-valid lower/upper bridge between the blowup nontriviality functional and `Λ_χ`, including pressure/time quantifiers, or (ii) search for an independent terminal/no-incoming-flux/BV-in-radius condition whose applicability to the exact Theorem-3.1 state can be proved.  The prior moving-radius compactness route remains orthogonal and open.

## Verification and falsifier status

- Scaling/units checked term by term; normalized pressure boundary exponent is `-1/6`, cubic exponent `-1/2`.
- One-sided-inequality logic checked: shell test is applied directly and remains nonnegative.
- Pressure/nonlocality retained explicitly.
- No derivative gain or circular bootstrap is used.
- Numerical work: none; all exponents are algebraic.
- Literature analogue (Onsager) is used only to motivate the need for a vanishing flux modulus; its regularity assumptions are not transferred.
- Same-context expert cell is internal role separation and receives `0/3` independent-review credit.
