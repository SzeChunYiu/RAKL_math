# NS-B2a1b1-C001 — logarithmic \(F_\lambda\)-gain versus geometric cutoff debt

**Authority:** `FINITE_POWER_F_GAIN_CANNOT_PAY_POSITIVE_RADIUS_DEBT / SCOPED_ESTIMATE_ROUTE_PRUNING / NO_NS_THEOREM / ROOT_AUTHORITY_NONE`  
**Root:** `NS0 = OPEN_NO_SOLUTION_CERTIFICATE`  
**Frozen atom:** RAKL_math issue #234  
**Framework source of truth:** `SzeChunYiu/RAKL@43897d3afaf0038385102d5acc64793c05ec40f0`, method `3.0.0`  
**Application base:** `SzeChunYiu/RAKL_math@597b7d98b514af33808d5f32be2cd5c906cfe036`  
**Frozen fibre:** `sha256:d76b820a4f1c065eb174b0d3d82aea816b0e650b990044244d428b9a58663bf6`

Primary source: Gregory Seregin, *On potential Type II blowups for the Navier–Stokes equations*, arXiv:2606.29468v1 (28 Jun 2026), especially (1.7), (2.2), (2.7), (2.9), (2.10), and Theorem 3.1.

## Executive finding

The logarithmic prelimit gain in Seregin's Euler scaling cannot compensate any **fixed positive power** of the moving scaled radius by taking only a **fixed finite algebraic power** of \(F_\lambda\).

Write
\[
L=\log(e/\lambda),\qquad
h=\log\frac{e}{\lambda a}=L-\log a,\qquad
F_\lambda(a)=\left(\frac{L}{h}\right)^\gamma ,
\]
with \(a\lambda\le1\), hence \(1\le h\le L\). If \(F_\lambda(a_\lambda)\to\infty\), then \(h_\lambda/L_\lambda\to0\), so \(\log a_\lambda=L_\lambda-h_\lambda\sim L_\lambda\). Meanwhile \(F_\lambda\le L_\lambda^\gamma\). Consequently for every fixed \(\alpha,\beta>0\),
\[
\frac{a_\lambda^\beta}{F_\lambda(a_\lambda)^\alpha}\longrightarrow\infty.
\]

This kills a whole estimate architecture: any standard absolute cutoff remainder certified only as
\[
O\!\left(a^\beta F_\lambda^{-\alpha}\right),\qquad \beta>0,\ \alpha<\infty,
\]
cannot be made to vanish by entering the logarithmic mesoscopic \(F_\lambda\)-gain window.

The result does **not** show that the actual signed flux is nonzero. A cancellation/telescoping identity, a scale-neutral/debt-free formulation, or stronger source information can still succeed.

## 1. Exact source normalization

Seregin defines
\[
A_f(v,r)=\sup_{-r^2<t<0}\frac{f(r)^2}{r}\int_{B(r)}|v|^2,\quad
E_f(v,r)=\frac{f(r)}{r}\int_{Q(r)}|\nabla v|^2,
\]
and
\[
D_f(q,r)=\frac{f(r)^2}{r^2}\int_{Q(r)}|q|^{3/2},
\]
with a uniform bound in (1.7). Under the Euler scaling (2.7), (2.2) gives
\[
F_\lambda(a)=\frac{f(\lambda a)}{f(\lambda)}
\]
and (2.9) gives a uniform prelimit bound on \(A_{F_\lambda}+E_{F_\lambda}+D_{F_\lambda}\).

For the logarithmic example (2.10),
\[
f(\lambda)=\{\log(e/\lambda)\}^{-\gamma},
\]
so exactly
\[
F_\lambda(a)=\left(\frac{L}{h}\right)^\gamma,\qquad
L=\log(e/\lambda),\quad h=L-\log a.
\]

The prior atom `NS-B2a1a1` established that a genuinely local divergent-gain window is
\[
1\ll h_\lambda\ll L_\lambda,
\]
equivalently \(a_\lambda\to\infty\), \(\lambda a_\lambda\to0\), and \(F_\lambda(a_\lambda)\to\infty\). The present atom asks whether that gain can pay the geometric powers produced by cutoff estimates.

## 2. Finite-power compensation lemma

**Lemma.** Let \(\gamma,\alpha,\beta>0\) be fixed. For any admissible sequence \(\lambda\downarrow0\), \(a_\lambda\ge1\), \(\lambda a_\lambda\le1\), if
\[
F_\lambda(a_\lambda)=\left(\frac{L_\lambda}{h_\lambda}\right)^\gamma\to\infty,
\]
then
\[
a_\lambda^\beta F_\lambda(a_\lambda)^{-\alpha}\to\infty.
\]

**Proof.** Since \(F_\lambda\to\infty\),
\[
\frac{h_\lambda}{L_\lambda}\to0.
\]
Hence eventually \(h_\lambda\le L_\lambda/2\), and
\[
\log a_\lambda=L_\lambda-h_\lambda\ge \frac{L_\lambda}{2}.
\]
Because \(h_\lambda\ge1\),
\[
F_\lambda(a_\lambda)=\left(\frac{L_\lambda}{h_\lambda}\right)^\gamma
\le L_\lambda^\gamma.
\]
Therefore
\[
\log\!\left(a_\lambda^\beta F_\lambda^{-\alpha}\right)
=\beta(L_\lambda-h_\lambda)-\alpha\gamma\log(L_\lambda/h_\lambda)
\ge \frac{\beta}{2}L_\lambda-\alpha\gamma\log L_\lambda
\to\infty.
\]
Exponentiating proves the claim. \(\square\)

The same proof covers the stricter local mesoscopic regime \(1\ll h_\lambda\ll L_\lambda\). The physical locality requirement \(h_\lambda\to\infty\) does not help the compensation problem.

### DifferenceWitness

The lemma concerns **fixed** \(\alpha,\beta\). It does not rule out a source mechanism that changes the radius exponent to \(\beta\le0\), produces super-algebraic gain, yields an exponent \(\alpha=\alpha(\lambda)\to\infty\), or gives an exact signed cancellation instead of an absolute estimate.

## 3. What the weighted ledger gives before cutoffs

Suppressing constants depending only on the source bound \(M_1\), (2.9) yields
\[
S_a:=\sup_t\int_{B(a)}|v^\lambda|^2
\lesssim aF_\lambda^{-2},
\]
\[
G_a:=\int_{Q(a)}|\nabla v^\lambda|^2
\lesssim aF_\lambda^{-1},
\]
and
\[
P_a:=\int_{Q(a)}|q^\lambda|^{3/2}
\lesssim a^2F_\lambda^{-2}.
\]

These are exact consequences of the weighted definitions. They expose why normalized smallness need not be enough: the absolute integrals carry positive powers of \(a\).

## 4. Full-parabolic local-energy cutoff audit

For a standard spatial cutoff at radius \(a\),
\[
|\nabla\phi_a|\lesssim a^{-1},\qquad
|\Delta\phi_a|\lesssim a^{-2},
\]
and for a parabolic time cutoff,
\[
|\partial_\tau\phi_a|\lesssim a^{-2}.
\]

The usual local interpolation inequality gives, at the level needed here,
\[
C(v^\lambda,a)\lesssim A(v^\lambda,a)^{3/4}E(v^\lambda,a)^{3/4}
+A(v^\lambda,a)^{3/2}.
\]
Since
\[
A\lesssim F_\lambda^{-2},\qquad E\lesssim F_\lambda^{-1},
\]
we obtain
\[
\int_{Q(a)}|v^\lambda|^3
\lesssim a^2\left(F_\lambda^{-9/4}+F_\lambda^{-3}\right).
\]

Hence the absolute cubic cutoff term is bounded by
\[
a^{-1}\int_{Q(a)}|v^\lambda|^3
\lesssim
aF_\lambda^{-9/4}+aF_\lambda^{-3}.
\]
Both terms have positive radius debt \(\beta=1\).

For pressure work, Hölder with the source \(D\)-bound gives
\[
a^{-1}\int_{Q(a)}|q^\lambda||v^\lambda|
\lesssim
a^{-1}P_a^{2/3}
\left(\int_{Q(a)}|v^\lambda|^3\right)^{1/3},
\]
whose leading bounds are
\[
\lesssim aF_\lambda^{-25/12}+aF_\lambda^{-7/3}.
\]
Again \(\beta=1\).

The quadratic cutoff terms satisfy
\[
a^{-2}\int_{Q(a)}|v^\lambda|^2
\le a^{-2}\,a^2S_a
\lesssim aF_\lambda^{-2}.
\]
Thus the usual full-parabolic time/Laplacian magnitude bounds also pay \(\beta=1\).

By the lemma, **none** of these certified bounds vanishes along a divergent logarithmic \(F_\lambda\)-gain window solely because \(F_\lambda\to\infty\). This is a failure of the magnitude-estimate route, not a lower bound on the actual terms.

## 5. Fixed-time intervals do not remove all positive debt

A possible escape is to restrict to a fixed time interval \(I\) of length \(T\), independent of \(a\), once \(a^2>T\). This helps some quadratic terms but does not eliminate all positive radius debt.

On \(I\times B(a)\), the ball Gagliardo–Nirenberg inequality and Hölder in time give
\[
\int_I\int_{B(a)}|v^\lambda|^3
\lesssim
S_a^{3/4}G_a^{3/4}T^{1/4}
+a^{-3/2}S_a^{3/2}T.
\]
Using the source bounds,
\[
\int_I\int_{B(a)}|v^\lambda|^3
\lesssim
a^{3/2}F_\lambda^{-9/4}T^{1/4}
+F_\lambda^{-3}T.
\]
Therefore
\[
a^{-1}\int_I\int_{B(a)}|v^\lambda|^3
\lesssim
a^{1/2}F_\lambda^{-9/4}T^{1/4}
+a^{-1}F_\lambda^{-3}T.
\]
The second term is debt-free/decaying in \(a\), but the first has \(\beta=1/2>0\), so the logarithmic gain still cannot certify its vanishing.

Using only the source pressure bound over the containing \(Q(a)\),
\[
a^{-1}\int_I\int_{B(a)}|q^\lambda||v^\lambda|
\]
is bounded by a sum whose leading radius powers include
\[
a^{5/6}F_\lambda^{-25/12}T^{1/12}
\quad\text{and}\quad
a^{1/3}F_\lambda^{-7/3}T^{1/3}.
\]
Both retain positive geometric debt.

The fixed-time Laplacian term does improve:
\[
a^{-2}\int_I\int_{B(a)}|v^\lambda|^2
\lesssim T\,a^{-1}F_\lambda^{-2}.
\]
But one improved term is not enough; cubic and pressure work remain obstructed at the magnitude-only level.

Therefore the answer to the frozen check “does fixed time remove all positive radius debt?” is **no** under the source-native weighted ledger and standard absolute interpolation.

## 6. Local mathematical failure versus gluing failure

### Local mathematical / estimate failure

`F-NS-B2a1b1-FINITE-F-POWER-GEOMETRIC-DEBT`:

> In the logarithmic Type-II prelimit window, every divergent \(F_\lambda\)-gain is at most polylogarithmic in \(1/\lambda\), while the corresponding moving scaled radius has \(\log a\sim\log(1/\lambda)\). Hence fixed finite powers of \(F_\lambda\) cannot compensate any positive fixed radius power in an absolute cutoff estimate. Standard cubic and pressure-work magnitude estimates retain such positive powers, even on fixed time intervals.

### Local-to-global / gluing status

No new gluing impossibility is proved. The existing failures
`F-NS-B2a1a1-LOG-GAIN-MOVING-RADIUS-COMPACTNESS-MISMATCH`,
`F-NS-B2a1a2-FIXED-TO-MOVING-RADIUS-ESCAPE`, and
`F-NS-B2a1-DOUBLE-LIMIT-TAIL-INHERITANCE-SHARPENED`
remain separately active.

Even a successful signed prelimit identity would still need:
1. a uniform subsequence/source-family statement;
2. pressure normalization compatible with the same identity;
3. protection against moving-center/profile leakage;
4. a valid passage through the vanishing-viscosity limit;
5. a same-theory Euler rigidity consumer.

Navier–Stokes backward uniqueness is not imported after the limit equation becomes Euler.

## 7. Episode -> diagnosis -> obstruction/lesson

**Episode:** `EP-NS-B2a1b1-C001-20260812` tested the issue-#234 asymptotic falsifier and standard cutoff exponents.

**Diagnosis:** the missing coordinate is not “more \(F\)-power.” It is elimination of geometric radius debt, or an exact sign/cancellation coordinate that avoids absolute-value estimates.

**Reusable obstruction proposal:** `O-NS-B2a1b1-LOG-GAIN-CANNOT-PAY-GEOMETRIC-DEBT`.

**Lesson proposal:** `L-NS-B2a1b1-DEBT-FREE-OR-SIGNED-CANCELLATION` — require \(\beta\le0\) at the certified estimate level before expecting logarithmic \(F\)-gain to close the cutoff, unless a genuine signed identity bypasses the magnitude bound.

These remain proposal/shadow search guidance only.

## 8. Expert-cell synthesis

Seven same-context roles separately audited source binding, asymptotics, local energy, pressure, compactness/gluing, hostile falsification, and RAKL authority/metrology. All agreed on the scoped route-pruning outcome. This earns **0/3 independent mathematical reviews**.

## 9. Outcome and next atom

**Outcome:** `PARTIAL_SUCCESS / FINITE_POWER_F_GAIN_CANNOT_PAY_POSITIVE_RADIUS_DEBT`.

**Solved subproblem:** the logarithmic moving-radius gain cannot make any fixed positive-radius-power absolute cutoff estimate vanish through a fixed finite \(F_\lambda\)-power, and standard cubic/pressure magnitude estimates do retain positive radius debt even after restricting to fixed time intervals.

**RAKL novelty class:** `COMPOSITIONAL` for this scoped internal result. No external literature-novelty claim is made.

**Residual before:** broad signed prelimit flux/telescoping bypass.

**Residual after:** restrict the live bypass to one of:
- an exact signed annular flux/telescoping identity whose boundary terms cancel rather than being estimated absolutely;
- a scale-neutral functional with no positive \(a\)-debt;
- a source-native correlation/transport quantity with super-algebraic gain;
- a PDE-scale-aligned tightness theorem from the sibling compactness route.

A useful successor atom is:

`NS-B2a1b2`: identify the exact local-energy/pressure flux combination on nested annuli whose **signed** telescoping survives the Euler scaling, and test it against translating-core/moving-center adversaries before attempting the \(\lambda\to0\) limit.

**Root status:** `OPEN_NO_SOLUTION_CERTIFICATE`. Type-I and other Type-II scenarios remain open. No protected promotion gate is attempted.
