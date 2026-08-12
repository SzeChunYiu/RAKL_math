# NS-B2a1a3 — one-scale logarithmic weighted bounds do not certify the moving-annulus tail

**Atom:** `NS-B2a1a3`  
**Parent:** `NS-B2a1a2`  
**Framework:** RAKL v3.0.0 @ `43897d3afaf0038385102d5acc64793c05ec40f0`  
**Frozen application base:** `21d22075fa250e4ded412fd292b7942b87503266`  
**Authority:** `SCOPED_ANALYTIC_ROUTE_PRUNING / PROPOSAL-SHADOW EXPERIENCE / NO ROOT AUTHORITY / NO LITERATURE-NOVELTY CLAIM`  
**Root:** `NS0 = OPEN_NO_SOLUTION_CERTIFICATE`

The pre-candidate packet for this atom was committed separately before this result. The high-level one-scale cutoff direction already existed before the public freeze, so this round claims **no strict context-first hypothesis-generation credit**. It may earn only scoped validation/route-pruning credit.

## 1. Exact source interface

The primary source is G. Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468v1 (28 Jun 2026). Under the logarithmic example

\[
f(r)=\log^{-\gamma}(e/r),\qquad \gamma>0,
\]

and the Euler scaling from (2.7), write

\[
L=\log(e/\lambda),\qquad
h=\log(e/(\lambda a)),\qquad
F_\lambda(a)=\frac{f(\lambda a)}{f(\lambda)}=\left(\frac{L}{h}\right)^\gamma.
\]

The useful local mesoscopic window isolated by the parent audit is

\[
h\to\infty,\qquad \frac{h}{L}\to0,
\]

so

\[
a=e^{L-h}\to\infty,\qquad \lambda a=e^{1-h}\to0,
\qquad F_\lambda(a)\to\infty.
\]

From Seregin's weighted estimate (2.9), the ordinary scale-normalized quantities on the same radius satisfy, schematically and with the exact powers inherited from the definitions,

\[
A(v^\lambda,a)\lesssim F^{-2},\qquad
E(v^\lambda,a)\lesssim F^{-1},\qquad
D(q^\lambda,a)\lesssim F^{-2}.
\tag{1}
\]

The compactness following (2.9) is stated for every **fixed** `a`; it is not a rate-uniform statement on `a=a(\lambda)\to\infty`. The scaled Navier-Stokes equation has viscosity `f(\lambda)\to0`, and its limit is Euler, so unit-viscosity rigidity/epsilon-regularity hypotheses are not transferable without a new check.

The parent atom `NS-B2a1a2` proved that the missing gluing coordinate is an **absolute uniform intermediate-annulus L2 tail modulus**. The present atom asks only whether standard one-scale uses of (1) can certify that missing coordinate.

## 2. Finite logarithmic gain cannot beat the mesoscopic radius

### Lemma (radius outruns every fixed algebraic log gain)

Let `L_k -> infinity` and let `h_k -> infinity` with `h_k/L_k -> 0`. Put

\[
a_k=e^{L_k-h_k},\quad
f_k=L_k^{-\gamma},\quad
F_k=(L_k/h_k)^\gamma,
\]

with fixed `gamma>0`. Then for every fixed `m>0` and every fixed finite real `alpha,beta`,

\[
a_k^m f_k^{\alpha}F_k^{-\beta}\longrightarrow\infty.
\tag{2}
\]

**Proof.** Taking logarithms,

\[
\log(a_k^m f_k^{\alpha}F_k^{-\beta})
=m(L_k-h_k)-\gamma(\alpha+\beta)\log L_k+\beta\gamma\log h_k.
\]

Because `h_k/L_k -> 0`, the first term is `m L_k(1-o(1))`. Since `h_k>=1` eventually and `h_k<L_k` eventually, all logarithmic terms are `O(log L_k)=o(L_k)`. Hence the displayed logarithm tends to `+infinity`, proving (2). QED.

A bounded numerical spot-check on `L_k=k^2`, `h_k=k` was used only as calibration; the proof is the preceding asymptotic argument.

## 3. Direct kinetic-tail certificate already fails at the bound level

The scale-normalized kinetic estimate in (1) yields only

\[
\sup_\tau\int_{B(a)}|v^\lambda|^2\,dy
\lesssim a F^{-2}.
\tag{3}
\]

By (2), the **control scale on the right-hand side diverges** throughout the mesoscopic window. This does **not** say that the actual kinetic mass diverges. It says that the weighted `A` bound, by itself, cannot certify the absolute moving-ball or intermediate-annulus L2 tightness required by `NS-B2a1a2`.

This is exactly the distinction exposed by the parent escaping-bump calibration: normalized smallness and absolute tightness are different coordinates.

## 4. Standard cubic and pressure absolute-value routes have the same obstruction

Let

\[
C(v,a)=a^{-2}\int_{Q(a)}|v|^3.
\]

The standard scale-invariant interpolation inequality gives

\[
C\lesssim A^{3/4}E^{3/4}+A^{3/2}.
\]

Using (1),

\[
C(v^\lambda,a)\lesssim F^{-9/4}+F^{-3}=O(F^{-9/4}).
\tag{4}
\]

For the pressure-velocity product, Hölder gives

\[
a^{-2}\int_{Q(a)}|q^\lambda||v^\lambda|
\le D^{2/3}C^{1/3}
=O(F^{-25/12}).
\tag{5}
\]

A one-scale cutoff has `|grad phi|=O(a^{-1})` and `|partial_t phi|+|Delta phi|=O(a^{-2})`. Restoring absolute dimensions therefore produces the familiar control scales

\[
aA=O(aF^{-2}),\qquad
aC=O(aF^{-9/4}),\qquad
aD^{2/3}C^{1/3}=O(aF^{-25/12}).
\tag{6}
\]

The scaled viscous cutoff terms carry additional fixed powers of `f(\lambda)`; those are still covered by (2). Thus every bound in the tested family that retains a positive power of `a` and only finitely many algebraic powers of `f` and `F` has a control scale that does not vanish; in fact it diverges.

Again, this is an **estimator insufficiency statement**. A diverging upper bound is not a lower bound. It does not prove that the true signed cubic flux, pressure work, or tail is nonzero.

## 5. Exact scope of the route pruning

The following inference family is pruned:

> source weighted `A/E/D` control + standard one-scale Hölder/Gagliardo-Nirenberg + absolute-value local-energy cutoff bounds -> the uniform moving-annulus absolute tail required by `NS-B2a1a2`.

The reason is structural: on `1 << h << L`, the observation radius is exponentially large in `L` while all gains generated by finite algebraic combinations of the logarithmic weights remain subexponential.

The following remain **open** and are not touched by this result:

- a genuinely multiscale shell telescoping or monotonicity argument in which geometric factors cancel across scales;
- a signed flux identity whose cancellation survives the limit;
- a pressure decomposition producing a qualitatively different scale dependence;
- a source-valid quantitative compactness/tightness theorem not reducible to the tested one-scale bounds;
- an alternative Euler/Liouville rigidity trigger that does not require this absolute tail;
- the orthogonal `NS-B2a1b` signed Euler-flux bypass;
- all Type-I and Type-II blow-up classes outside the exact source scenario.

## 6. Limit-passage and rigidity interface audit

**Weak/strong convergence.** The source gives strong convergence locally on each fixed cylinder and weak/weak-star control for gradients/energy. No step here diagonalizes that to `a_k -> infinity`.

**Pressure localization.** Equation (5) audits only the standard absolute Hölder route. It does not assert pressure convergence on moving shells and does not rule out pressure cancellation/decomposition.

**Far field / noncompact symmetry.** The obstruction is precisely at the far-field moving shell. Translation/scale escape remains a live failure mode until a PDE-specific tightness mechanism is proved.

**Backward uniqueness / unique continuation.** Not invoked. Any future rigidity step must verify its hypotheses on the actual limiting Euler/ancient state rather than importing a Navier-Stokes hypothesis through an equation change.

**Equation change.** The prelimit scaled viscosity is `f(lambda) -> 0`; the limit equation is Euler. A local prelimit lemma glues to a continuum rigidity theorem only if the state space, pressure, topology, far field, and equation-specific hypotheses match exactly.

## 7. Result and residual

**Scoped outcome:** `ONE_SCALE_CERTIFICATE_REFUTED_RADIUS_OUTRUNS_LOG_WEIGHT`.

**New reusable obstruction:** `O-NS-B2a1a3-RADIUS-VS-LOG-WEIGHT` — if a moving-domain absolute estimate retains a positive geometric power while source improvement consists only of finite algebraic powers of a logarithmic weight, the estimate cannot certify vanishing on the mesoscopic window.

**Residual:** `F-NS-B2a1a3-ONE-SCALE-ABSOLUTE-TAIL-CERTIFICATE` — the PDE-derived absolute tail remains unproved; the standard one-scale estimate family is insufficient.

**Next action:** reopen the `PATH/OBSTRUCTION/RELATION/EXPERIENCE_PATTERN` axes and test a genuinely scale-nonlocal or signed transformation: multiscale shell telescoping, pressure cancellation/decomposition, or the orthogonal signed-flux bypass. If no source-valid such transform survives a bounded search, only then consider LIFT under a cross-problem coverage receipt.

No regularity theorem, singular solution, Type-II exclusion beyond an already published source scenario, or Millennium root certificate follows.
