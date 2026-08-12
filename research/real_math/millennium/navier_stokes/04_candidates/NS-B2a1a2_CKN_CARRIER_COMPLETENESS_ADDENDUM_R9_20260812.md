# NS-B2a1a2 — CKN carrier completeness addendum (R9)

**Authority:** proposal/shadow only. This addendum sharpens the direct-estimate result; it does not turn failure of a sufficient upper bound into a lower bound on the actual solution.

The source-side regularity display (Seregin arXiv:2606.29468v1, (1.1)) allows the standard dimensionless velocity carriers `A`, `E`, or `C`. The main R9 audit already priced `A` and `E` under the exact Euler-scale-to-physical-parabolic coordinate map. For completeness, this addendum audits the standard `C` carrier and corrects the asymptotic wording of the maximal-gain stress test.

Write `nu=f(lambda)`, `F=F_lambda(a)` and `w=v^lambda`. On the maximal physical parabolic subcylinder `r_*=lambda a sqrt(nu)`, direct change of variables gives

`C(v,r_*) <= nu^(-3) C(w,a)`,

where enlargement from the smaller spatial ball to `B(a)` is harmless for this upper estimate. Standard local Sobolev interpolation on the source cylinder gives, with a universal constant `c`,

`C(w,a) <= c [ A(w,a)^(3/4) E(w,a)^(3/4) + A(w,a)^(3/2) ]`.

Using the source ledger `A(w,a)<=M1/F^2`, `E(w,a)<=M1/F` therefore yields

`C(v,r_*) <= c M1^(3/2) [ nu^(-3) F^(-9/4) + nu^(-3) F^(-3) ]`.

The useful-gain regime has `F>=1`; if `F<1` the displayed source upper bounds are only weaker. Since the source also gives `F<=nu^(-1)`, the **smallest right-hand side permitted by this direct interpolation estimate** is asymptotically no smaller than the maximal-gain substitution

`c M1^(3/2) [ nu^(-3/4) + 1 ]`,

which does not approach the CKN epsilon threshold as `nu->0` and in fact has a divergent first term. Hence the ordinary `C` interpolation route does not rescue the direct ledger-to-CKN bridge.

Likewise, the precise maximal-gain reading for the main R9 `A,E,D` estimates is: because `F<=nu^(-1)`, their right-hand sides are bounded **from below as candidate upper envelopes** by scales `M1 nu^(-1/2)`, `M1 nu^(-1/2)`, and `M1 nu^(-1)` respectively. This is not a lower bound on the actual physical `A,E,D`; it means only that the inequalities available from the bare weighted ledger cannot furnish a vanishing sufficient upper bound.

For Seregin's logarithmic example, `nu=L^(-gamma)` and `F=(L/h)^gamma`, so the first standard interpolation term becomes

`c M1^(3/2) L^(3gamma/4) h^(9gamma/4)`,

while the second is `c M1^(3/2) h^(3gamma)`. On the mesoscopic window `1<<h<<L`, neither produces epsilon smallness. Together with the main audit, all three velocity carriers explicitly named in the source's displayed `g0=min{liminf A,liminf E,liminf C}` interface fail to receive a vanishing bound from the **bare direct centered-cylinder transformation**.

This remains scoped. A different theorem using equation-specific cancellation, pressure structure, time-uniform propagation, a non-centered/modulo-symmetry carrier, or producer-side tightness is outside this addendum and remains open. No root or impossibility authority is claimed.
