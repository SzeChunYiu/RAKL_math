# NS-B2a1a1 — logarithmic prelimit scale-window / compactness interface audit

**Authority:** `PROPOSAL_SHADOW_ONLY`  
**Root:** `NS0 = OPEN_NO_SOLUTION_CERTIFICATE`  
**Frozen atom:** RAKL_math issue #214  
**Primary source:** Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468v1 (28 Jun 2026), especially (1.7), (2.2), (2.7), (2.9), the compactness statement immediately after (2.9), (2.10), and Theorem 3.1.

This is a source-interface verification result, not a new regularity theorem and not a claim of literature novelty.

## 1. Exact source normalization

For the logarithmic example
\[
f(\lambda)=\{\log(e/\lambda)\}^{-\gamma},\qquad \gamma>0,
\]
set
\[
L_\lambda:=\log(e/\lambda),\qquad
h_\lambda(a):=\log\frac{e}{\lambda a}=L_\lambda-\log a.
\]
Seregin's admissibility condition \(a\lambda\le 1\) gives \(h_\lambda(a)\ge 1\). From (2.2),
\[
F_\lambda(a)=\frac{f(\lambda a)}{f(\lambda)}
=\left(\frac{L_\lambda}{h_\lambda(a)}\right)^\gamma.
\]

Hence, for any admissible sequence \(a_\lambda\ge1\),
\[
F_\lambda(a_\lambda)\to\infty
\quad\Longleftrightarrow\quad
\frac{h_\lambda(a_\lambda)}{L_\lambda}\to0
\quad\Longleftrightarrow\quad
\frac{\log a_\lambda}{L_\lambda}\to1.
\]

This immediately separates fixed or polynomially interior radii from the only scale-breaking window. For \(a_\lambda=\lambda^{-\theta}\) with fixed \(0\le\theta<1\),
\[
h_\lambda=(1-\theta)L_\lambda+\theta,\qquad
F_\lambda(a_\lambda)\to(1-\theta)^{-\gamma}<\infty.
\]
So no asymptotic \(F_\lambda\)-gain exists at any fixed-power interior exponent bounded away from \(1\).

## 2. A genuine local mesoscopic window exists

The physical radius corresponding to scaled radius \(a_\lambda\) is \(r_\lambda=\lambda a_\lambda\), and
\[
h_\lambda(a_\lambda)=\log(e/r_\lambda).
\]
Therefore both
\[
r_\lambda\to0
\quad\text{and}\quad
F_\lambda(a_\lambda)\to\infty
\]
hold exactly in the nonempty regime
\[
1\ll h_\lambda\ll L_\lambda.
\]
For example, \(h_\lambda=\sqrt{L_\lambda}\) gives
\[
a_\lambda=e^{L_\lambda-\sqrt{L_\lambda}}\to\infty,\quad
r_\lambda=e^{1-\sqrt{L_\lambda}}\to0,\quad
F_\lambda(a_\lambda)=L_\lambda^{\gamma/2}\to\infty.
\]

Thus the logarithmic weight does contain genuine scale-breaking information before the limit, but only on moving radii that go to infinity in the Euler-scaled variables while remaining local in the original variables.

## 3. What (2.9) really yields there

Using the source definitions,
\[
A_{F_\lambda}(v^\lambda,a)=F_\lambda(a)^2 A(v^\lambda,a),\quad
E_{F_\lambda}(v^\lambda,a)=F_\lambda(a)E(v^\lambda,a),\quad
D_{F_\lambda}(q^\lambda,a)=F_\lambda(a)^2 D(q^\lambda,a).
\]
Therefore (2.9) implies, for every admissible \(a\),
\[
A(v^\lambda,a)\le M_1F_\lambda(a)^{-2},\quad
E(v^\lambda,a)\le M_1F_\lambda(a)^{-1},\quad
D(q^\lambda,a)\le M_1F_\lambda(a)^{-2}.
\]
Along any mesoscopic window \(1\ll h_\lambda\ll L_\lambda\), these three **scale-normalized** quantities tend to zero.

This is not absolute tail tightness. For example,
\[
\int_{B(a_\lambda)}|v^\lambda|^2
\le M_1\,\frac{a_\lambda}{F_\lambda(a_\lambda)^2}
= M_1 e^{L_\lambda-h_\lambda}
\left(\frac{h_\lambda}{L_\lambda}\right)^{2\gamma}.
\]
When \(h_\lambda=o(L_\lambda)\), the right-hand side grows rather than tending to zero. Thus the source bound supplies dimensionless smallness at the moving scale, but it does not by itself supply finite total energy, absolute mass tightness, or a vanishing unsigned global-cutoff budget. The same warning is stronger for the unnormalized pressure integral.

## 4. Hostile compactness test: the gain and the convergence live on different scale regimes

Immediately after (2.9), the source extracts a subsequence with strong/weak convergence on \(Q(a)\) **for every fixed \(a>0\)**. In the logarithmic example, for every fixed \(a\),
\[
F_\lambda(a)\to F(a)=1.
\]
So the fixed-radius limit retains the bounded \(F=1\) class, but the \(F_\lambda\to\infty\) gain has disappeared.

A diagonal compactness slogan does not close this gap. To exploit the gain one needs \(a_k\to\infty\) with
\[
\log a_k/L_{\lambda_k}\to1.
\]
Convergence on each fixed \(Q(R)\) gives no quantitative rate that guarantees convergence on a radius \(R=a_k\) tied this tightly to \(\lambda_k\). Choosing \(k\) much larger to ensure convergence on a prescribed \(R\) can itself force \(L_{\lambda_k}\gg\log R\), collapsing \(F_{\lambda_k}(R)\) back toward \(1\). A rate-compatible moving-radius compactness theorem (or a different signed identity avoiding strong convergence on that radius) is therefore an additional missing bridge, not a consequence stated in the source.

This is a local-to-global/gluing failure. The local source estimates remain valid.

## 5. Hostile epsilon-regularity test: viscosity degenerates

The Euler scaling (2.7) is not the unit-viscosity Navier-Stokes scaling. Direct substitution gives
\[
\partial_\tau v^\lambda+v^\lambda\!\cdot\nabla v^\lambda
-f(\lambda)\Delta v^\lambda+\nabla q^\lambda=0,
\qquad \nabla\cdot v^\lambda=0.
\]
For the logarithmic example \(f(\lambda)=L_\lambda^{-\gamma}\to0\).

Consequently the small scale-normalized \(A,E,D\) values on the mesoscopic radii cannot be fed silently into a unit-viscosity Caffarelli--Kohn--Nirenberg/epsilon-regularity criterion with a uniform threshold. Any such step would require a separately sourced theorem uniform as viscosity tends to zero. No such theorem is part of this atom or of the cited source. This prevents a false shortcut from “moving-scale normalized smallness” to regularity of the original singular core.

## 6. Pressure / flux / endpoint audit

- **Pressure:** (2.9) gives normalized \(D\)-smallness on the moving scale, not absolute pressure-work tail control. Harmonic/nonlocal pressure and far-field interfaces remain open.
- **Signed flux:** no sign, telescoping, no-incoming-flux, or BV-in-radius identity was derived here. `NS-B2a1b` remains separate.
- **Domain endpoint:** all calculations retain \(a\lambda\le1\); the useful local mesoscopic regime even has \(\lambda a\to0\).
- **Units/scaling:** \(A,E,D\) are dimensionless under ordinary parabolic normalization; the \(F_\lambda\) factors are dimensionless. No dimensional mismatch was found.
- **Root:** no global regularity conclusion follows.

## 7. Scoped outcome

`MESOSCOPIC_WINDOW_IDENTIFIED_COMPACTNESS_GAP_PERSISTS`.

The generic residual
`F-NS-B2a1-DOUBLE-LIMIT-TAIL-INHERITANCE`
is sharpened to:

> In the logarithmic \(F=1\) regime, the only source-native \(F_\lambda\)-smallness occurs on radii with \(1\ll \log(e/(\lambda a))\ll\log(e/\lambda)\). Those radii move to infinity in scaled variables, while the cited compactness is fixed-radius and supplies no rate compatible with that movement. The resulting smallness is scale-normalized, not absolute tail tightness, and the scaled equation has viscosity \(f(\lambda)\to0\).

**Next strict atom:** establish either (i) a source-valid, rate-compatible mesoscopic compactness/tightness statement on such radii, or (ii) a signed prelimit flux/telescoping identity that can pass to the Euler limit without requiring strong convergence on a moving radius. No theorem authority is attached to this routing proposal.
