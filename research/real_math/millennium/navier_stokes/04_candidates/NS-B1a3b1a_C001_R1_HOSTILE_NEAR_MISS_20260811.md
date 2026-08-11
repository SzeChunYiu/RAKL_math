# NS-B1a3b1a-C001 R1 — hostile near-miss for the finite-I producer signature

Authority: `PROPOSAL_SHADOW_SCOPED_FALSIFIER / NO_ROOT_AUTHORITY`.

## Claim under test

Test only the **bare functional embedding**

\[
\sup_{Q(z,r)\subset Q}\{A+C+D+E\}<\infty
\quad\Longrightarrow\quad
\sup_t\big(\|\omega(t)\|_{L^{3/2,\infty}}+
\|\xi(t)\|_{bmo_{1/|\log \rho|}}\big)<\infty,
\]

when the left side is treated as a numerical scale-functional signature. This is weaker than the actual Navier-Stokes producer question because the actual Albritton–Barker theorem assumes a suitable weak solution and may use equation-specific structure.

## Smooth divergence-free hostile family

Choose `chi in C_c^∞(B_1)` with `chi=1` on `B_{3/4}`, and choose `eta in C_c^∞((-1,1))` with `eta(0)=1`. For large integer `N`, set

\[
\mathcal A_N(x)=(0,0,N^{-1}\chi(x)\cos(Nx_1)),\qquad
v_N=\nabla\times\mathcal A_N,
\]
\[
u_N(x,t)=\eta(N^2(t-t_0))\,v_N(x),\qquad q_N=0.
\]

Then `u_N` is smooth, compactly supported in space, and divergence-free. On `B_{3/4}` one has exactly

\[
v_N=(0,\sin(Nx_1),0),\qquad
\nabla\times v_N=(0,0,N\cos(Nx_1)).
\]

The time support has length `O(N^{-2})`, while `|v_N|<=C` and `|\nabla v_N|<=C N`.

## Uniform numerical Type-I envelope

For any parabolic cylinder of radius `0<r<=1`, up to constants depending only on the fixed cutoffs,

\[
A(r)\lesssim r^2,
\]
\[
C(r)\lesssim r\,\min(r^2,N^{-2}),
\]
\[
D(r)=0,
\]
and
\[
E(r)\lesssim N^2r^2\min(r^2,N^{-2}).
\]

For `r<=N^{-1}`, the last quantity is at most `N^2r^4<=N^{-2}`. For `r>=N^{-1}`, it is at most `r^2<=1`. Hence the numerical `A+C+D+E` signature is bounded independently of `N`.

A scoped computational check over `N=8,...,256` and logarithmically spaced radii reproduced the envelope maximum `N^2 r^2 min(r^2,N^{-2})<=1`; this computation checks algebra only and is not proof of a Navier-Stokes statement.

## Peak-time consumer norms diverge

At `t=t_0`, inside `B_{1/2}`,

\[
\omega_N=(0,0,N\cos(Nx_1)).
\]

A fixed positive fraction of `B_{1/2}` has `|cos(Nx_1)|>=1/2`, uniformly for large `N`, so

\[
\|\omega_N(t_0)\|_{L^{3/2,\infty}(B_{1/2})}\gtrsim N.
\]

Away from the nodal planes, the normalized vorticity direction is

\[
\xi_N=\operatorname{sgn}(\cos(Nx_1))e_3.
\]

Take a ball of radius `rho_N~N^{-1}` centered on a nodal plane and contained in `B_{1/2}`. Positive and negative phases occupy comparable portions of this ball, so its mean oscillation is bounded below by a universal positive constant. Since the logarithmic BMO consumer multiplies this oscillation by `1/phi(rho_N)=|log rho_N|`,

\[
\|\xi_N(t_0)\|_{bmo_{1/|\log \rho|}(B_{1/2})}\gtrsim \log N-O(1).
\]

The arbitrary convention on the zero-vorticity planes does not affect these integral lower bounds because those planes have measure zero.

## Verified scoped conclusion

There is no bounded **norm-only** producer operator from the numerical finite-`I` `A/C/D/E` signature to the uniform time-slice vorticity amplitude and logarithmic-BMO direction signature. Parabolic spacetime first-derivative control can hide a high-frequency event in a time window of the matching `N^{-2}` width.

This does **not** prove that a suitable weak Navier-Stokes solution with finite `I` can exhibit the hostile family. The construction is intentionally not asserted to solve Navier-Stokes; `q_N=0` is only part of the numerical signature. Therefore the remaining positive route is sharply typed:

> establish an equation-specific upgrade from `NSE + finite I` to the needed time-slice phase/amplitude information, or use a different consumer.

## Interfaces that remain open

* **Limit passage:** strong local velocity `L^3` convergence does not permit differentiation to strong vorticity or normalized-direction convergence; derivative loss remains a live failure.
* **Pressure:** the hostile family supplies no NSE pressure localization theorem; the actual pressure decomposition/compactness hypotheses remain separate.
* **Far field/gluing:** even a local producer upgrade would not supply Grujić's global Lorentz/far-field inputs without a separate global-tail certificate.
* **Noncompact symmetries:** not used in this local norm falsifier; still live in actual blow-up compactness.
* **Backward uniqueness:** downstream; it cannot manufacture the missing phase/amplitude producer hypothesis.
* **State space:** Grujić's endgame is pre-singularity analyticity/escape-time, not an ancient Liouville theorem.
* **Type II:** untouched.

Outcome: `PARTIAL_SUCCESS / BARE_FUNCTIONAL_PRODUCER_EMBEDDING_REFUTED / NSE_SPECIFIC_UPGRADE_OPEN`.
