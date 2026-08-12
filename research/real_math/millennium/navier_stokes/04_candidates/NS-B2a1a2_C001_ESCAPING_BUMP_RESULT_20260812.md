# NS-B2a1a2-C001 — an escaping divergence-free bump falsifies the bare moving-radius transfer

**Atom:** `NS-B2a1a2`  
**Candidate:** `NS-B2a1a2-C001-ESCAPING-BUMP`  
**Candidate statement hash:** `sha256:fc4885b3625d49423a68a683e7f1d89fe223cf704f54479250723aa4169672e9`  
**Authority:** `SCOPED_ANALYTIC_ROUTE_PRUNING / FUNCTIONAL_CALIBRATION / NO_NAVIER_STOKES_OR_EULER_COUNTEREXAMPLE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`  
**Root:** `NS0 = OPEN_NO_SOLUTION_CERTIFICATE`

This round earns mathematical credit only for the explicit construction and the
sharp tail condition below. Software, schema, hash, chronology, and CI work earn
zero mathematical credit.

## 1. Exact failed move reconstructed

The parent logarithmic audit established, for

\[
L_k=\log(e/\lambda_k),\qquad h_k=\log(e/(\lambda_k a_k)),
\qquad F_k=(L_k/h_k)^\gamma,
\]

that the only useful local mesoscopic regime is

\[
1\ll h_k\ll L_k,\qquad a_k\to\infty,\qquad
\lambda_k a_k\to0,\qquad F_k\to\infty.
\]

The source's compactness is on each **fixed** ball/cylinder, whereas the gain is
on the **moving** ball of radius \(a_k\). The failed proof move is

\[
v_k\to v\text{ strongly on every fixed compact}
\quad+\quad A(v_k,a_k)\to0
\quad\Longrightarrow\quad
\int_{B(a_k)}|v_k-v|^2\to0.
\]

Here

\[
A(w,a)=\frac1a\sup_t\int_{B(a)}|w(x,t)|^2\,dx.
\]

The implication confuses scale-normalized smallness with absolute tightness.

## 2. Explicit smooth divergence-free counterexample

Fix \(\gamma>0\). Choose nonzero
\(\psi\in C_c^\infty(B(0,1);\mathbb R^3)\) with
\(\nabla\cdot\psi=0\) and normalize \(\|\psi\|_2=1\). Such a field is obtained,
for example, as the curl of a nonzero compactly supported smooth vector
potential.

Set

\[
L_k=k^2,\qquad h_k=k,\qquad
\lambda_k=e^{1-L_k},\qquad a_k=e^{L_k-h_k},\qquad
F_k=(L_k/h_k)^\gamma=k^\gamma,
\]

and let \(x_k=(a_k/2,0,0)\). Define the time-independent calibration field

\[
v_k(x,t)=c_k\psi(x-x_k),\qquad
c_k=\frac{\sqrt{a_k}}{F_k}.
\]

Every \(v_k\) is smooth and divergence-free. It is **not** asserted to solve
Navier--Stokes or Euler.

The scale identities are exact:

\[
\frac{h_k}{L_k}=\frac1k\to0,
\qquad \lambda_k a_k=e^{1-h_k}=e^{1-k}\to0,
\qquad F_k=k^\gamma\to\infty.
\]

For any fixed \(R<\infty\),

\[
\operatorname{supp}v_k\subset B(x_k,1),\qquad |x_k|-1=a_k/2-1>R
\]

eventually. Hence \(v_k=0\) on \(B(R)\) eventually, so \(v_k\to0\) strongly
in every local space, including \(L^2(B(R)\times I)\) on each fixed finite time
interval.

Also \(B(x_k,1)\subset B(a_k)\) eventually because \(a_k/2+1<a_k\). Therefore

\[
\int_{B(a_k)}|v_k|^2\,dx=c_k^2\|\psi\|_2^2
=\frac{a_k}{F_k^2}
=\frac{e^{k^2-k}}{k^{2\gamma}}\longrightarrow\infty,
\]

while

\[
A(v_k,a_k)=\frac1{a_k}\int_{B(a_k)}|v_k|^2\,dx
=F_k^{-2}=k^{-2\gamma}\longrightarrow0.
\]

Thus fixed-radius strong convergence and moving-scale normalized energy
smallness coexist with divergent absolute mass inside the moving ball. This is
an explicit counterexample to the **bare functional transfer**.

## 3. Sharp transfer condition

The exact missing coordinate is uniform intermediate-annulus tightness.

### Lemma

Let \(a_k\to\infty\), let \(v_k,v\in L^2_{\mathrm{loc}}(\mathbb R^3)\), and
assume \(v_k\to v\) strongly in \(L^2(B(R))\) for every fixed \(R\). Then

\[
\int_{B(a_k)}|v_k-v|^2\,dx\to0
\]

if and only if

\[
\lim_{R\to\infty}\limsup_{k\to\infty}
\int_{B(a_k)\setminus B(R)}|v_k-v|^2\,dx=0.
\tag{T}
\]

The convention is harmless for the finitely many \(k\) with \(a_k\le R\).

### Proof

For fixed \(R\) and all sufficiently large \(k\), \(R<a_k\), and the disjoint
decomposition gives

\[
\int_{B(a_k)}|v_k-v|^2
=\int_{B(R)}|v_k-v|^2
+\int_{B(a_k)\setminus B(R)}|v_k-v|^2.
\tag{1}
\]

If (T) holds, take \(\limsup_k\) in (1). The first term vanishes by fixed-ball
strong convergence, and then \(R\to\infty\) makes the second term vanish.

Conversely, if the moving-ball integral tends to zero, nonnegativity and
\(B(a_k)\setminus B(R)\subset B(a_k)\) imply, for every fixed \(R\),

\[
0\le\limsup_k\int_{B(a_k)\setminus B(R)}|v_k-v|^2
\le\limsup_k\int_{B(a_k)}|v_k-v|^2=0.
\]

Thus (T) follows. \(\square\)

For the constructed sequence \(v=0\). For every fixed \(R\), its support lies
in \(B(a_k)\setminus B(R)\) eventually, so the annular integral equals
\(a_k/F_k^2\to\infty\). The exact repair condition fails maximally.

## 4. Mathematical lesson and strict scope

The mathematical lesson is:

> Fixed-radius compactness transfers a moving-scale kinetic quantity only when
> a scale-aligned tail modulus such as (T), or equivalently quantitative
> convergence on compatible radii, is supplied. Scale-normalized smallness alone
> cannot substitute for this modulus because mass may escape into an annulus that
> every fixed compact eventually misses.

This result closes the **abstract compactness implication** negatively and gives
its sharp repair condition. It does not establish that Seregin's actual
vanishing-viscosity sequence exhibits escape, nor that it satisfies (T). It says
nothing decisive about pressure, signed flux, temporal PDE structure, or a
different rate-compatible compactness theorem.

## 5. Residual

`NS-B2a1a3` remains open:

> Establish or refute a **PDE-derived** scale-aligned intermediate-annulus
> tightness/rate modulus for the logarithmic mesoscopic window, including
> pressure and vanishing-viscosity compatibility; alternatively pursue the
> orthogonal signed prelimit flux/telescoping bypass `NS-B2a1b`.

No regularity theorem, singular solution, blow-up exclusion, or solution
certificate follows.
