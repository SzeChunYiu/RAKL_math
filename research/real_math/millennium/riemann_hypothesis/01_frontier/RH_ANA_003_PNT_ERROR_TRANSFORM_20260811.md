# RH-ANA-003 primary-source packet: arithmetic Li coefficients as a PNT-error transform

**Authority:** source-bound analytic reconstruction only. No RH theorem candidate and no root authority.

**Framework subject:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`  
**Application base:** `SzeChunYiu/RAKL_math@0fddc66a70a1f89b5aada81b63678fd66da589eb`  
**Atom:** `RH-ANA-003`

## Primary sources inspected

1. Jeffrey C. Lagarias, *Li Coefficients for Automorphic L-Functions*, arXiv:math/0404394v4, later Ann. Inst. Fourier 57 (2007), 1689–1740.
   - The introduction records the arithmetic decomposition
     \[
     \lambda_n=S_\infty(n)-S_f(n)+1.
     \]
   - For the trivial representation, §4 gives
     \[
     S_f(n)=\sum_{j=1}^n(-1)^{j-1}\binom{n}{j}\eta_{j-1},
     \]
     and
     \[
     \eta_j=\frac{(-1)^j}{j!}\lim_{N\to\infty}
     \left(
       \sum_{m=1}^{N}\frac{\Lambda(m)(\log m)^j}{m}
       -\frac{(\log N)^{j+1}}{j+1}
     \right).
     \]
   - This cycle uses these source formulas exactly. It does not import RH-conditional asymptotics as unconditional facts.

2. Daniel R. Johnston, *Zero-density estimates and the optimality of the error term in the prime number theorem*, arXiv:2411.13791.
   - Under a Vinogradov–Korobov type zero-free region, Johnston derives an essentially optimal unconditional magnitude estimate for
     \[
     E(x):=\psi(x)-x
     \]
     of the form
     \[
     \frac{|E(x)|}{x}\ll
     e^{-\omega(x)}
     \frac{(\log x)^9}{(\log\log x)^3},
     \]
     with \(\omega(x)\) on the familiar \((\log x)^{3/5}/(\log\log x)^{1/5}\) scale.

3. Chiara Bellotti, *A new zero-density estimate for \(\zeta(s)\) and the error term in the Prime Number Theorem*, arXiv:2508.02041.
   - Bellotti sharpens zero-density input near the zero-free boundary and obtains the optimal PNT error form \(E(x)\ll x e^{-\omega(x)}\) for the registered zero-free-region function.
   - This is admitted as current magnitude information only. It carries no signed/correlation information about \(E\) against the Li kernels below.

## Exact algebraic collapse of the finite-place term

Substitute Lagarias' definition of \(\eta_{j-1}\) into \(S_f(n)\). The two factors \((-1)^{j-1}\) cancel. Define
\[
K_n(t):=\sum_{j=1}^{n}\binom{n}{j}\frac{t^{j-1}}{(j-1)!}.
\]
By the defining finite expansion of associated Laguerre polynomials,
\[
K_n(t)=L_{n-1}^{(1)}(-t).
\]

The regularizing polynomial is
\[
\sum_{j=1}^n\binom{n}{j}\frac{(\log N)^j}{j!}
=L_n(-\log N)-1,
\]
and since
\[
\frac{d}{dt}L_n(-t)=L_{n-1}^{(1)}(-t)=K_n(t),
\]
it is also
\[
L_n(-\log N)-1
=\int_1^N K_n(\log x)\frac{dx}{x}.
\]

Therefore the finite-place term is exactly
\[
\boxed{
S_f(n)=
\lim_{N\to\infty}
\left[
\sum_{m\le N}\frac{\Lambda(m)}{m}K_n(\log m)
-
\int_1^N K_n(\log x)\frac{dx}{x}
\right].
}
\]

Equivalently, with
\[
\psi(x)=\sum_{m\le x}\Lambda(m),\qquad E(x)=\psi(x)-x,
\]
\[
\boxed{
S_f(n)=
\lim_{N\to\infty}
\int_{1^-}^{N}
\frac{K_n(\log x)}{x}\,dE(x).
}
\]

This is a re-expression of the registered arithmetic formula, not a novel theorem claim.

## Fixed-\(n\) PNT-error transform

For each fixed \(n\), an unconditional PNT error bound makes the upper integration-by-parts boundary vanish because \(K_n(\log x)\) is polynomial in \(\log x\). Using the lower-end convention \(E(1^-)=-1\) and \(K_n(0)=n\), define
\[
W_n(t):=K_n(t)-K_n'(t).
\]
Then
\[
\boxed{
S_f(n)
=
n+
\int_0^\infty
\frac{E(e^t)}{e^t}\,W_n(t)\,dt.
}
\]

Thus the exact all-index Li condition may be written as the one-sided family obligation
\[
\boxed{
\int_0^\infty
\frac{E(e^t)}{e^t}W_n(t)\,dt
\le
S_\infty(n)-n+1
\quad\text{for every }n\ge1.
}
\]

This localization is useful because it separates two information types:
- current PNT theorems primarily provide a **two-sided pointwise magnitude envelope** for \(E(e^t)/e^t\);
- Li positivity requires a **one-sided, family-uniform bound on a signed transform** whose kernel changes with \(n\).

No claim is made here that current PNT bounds cannot participate in a successful RH proof. The narrower diagnostic is that replacing \(E\) by \(|E|\) destroys sign/correlation information, so a triangle-inequality route must be quantitatively audited against the growing family \(W_n\) rather than assumed useful.

## Hostile envelope-control test

Let \(B(t)\ge0\) be any registered pointwise envelope with
\[
|E(e^t)|/e^t\le B(t).
\]
A proof step that uses **only** this symmetric envelope and the triangle inequality reduces the arithmetic residual to
\[
\left|
\int_0^\infty \frac{E(e^t)}{e^t}W_n(t)\,dt
\right|
\le
\int_0^\infty B(t)|W_n(t)|\,dt.
\]

The envelope itself contains no information about whether the true arithmetic error aligns or anti-aligns with \(W_n\). A hostile residual
\[
\varepsilon_{\rm host}(t)=B(t)\operatorname{sgn}W_n(t)
\]
is therefore a valid *method stress test* for envelope-only reasoning. It is **not** asserted to be a possible zeta PNT error. Its sole role is to check whether a proposed derivation accidentally obtains directional information from a symmetric magnitude hypothesis.

The next discriminator is quantitative and zeta-specific:
1. compute or bound the induced majorant family under the best current \(B\);
2. compare it with the exact archimedean threshold \(S_\infty(n)-n+1\);
3. if sign-blind domination is too loose, identify the weakest additional signed/correlation statistic of \(E\) that would change the bound;
4. verify that this added statistic is strictly weaker than RH before treating it as progress.

## Known-answer checks

The finite polynomial identity gives
\[
K_1(t)=1,\quad
K_2(t)=t+2,\quad
K_3(t)=\tfrac12t^2+3t+3,
\]
which matches \(L_{n-1}^{(1)}(-t)\) for \(n=1,2,3\).

These are algebraic indexing checks only. They do not validate any all-\(n\) inequality.

## Evidence boundary

- **Supported:** exact source formula, algebraic collapse into \(K_n\), fixed-\(n\) PNT boundary control, and localization of the residual as a signed PNT-error transform.
- **Not established:** any useful uniform-in-\(n\) upper bound, any sign/correlation theorem for the transform, any strict weakening of RH, any new theorem, or any RH progress certificate.
- **Root state:** `OPEN_NO_SOLUTION_CERTIFICATE`.
