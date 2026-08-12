# NS-B2a1a2 C001 — viscosity-normalized epsilon-regularity cost audit (R1)

Authority: **proposal/shadow research only**. This is a scoped estimate/interface result. It is not a Navier–Stokes regularity theorem, not a Type-II exclusion, and not root evidence.

## Exact discriminator

Starting only from Seregin arXiv:2606.29468v1 (1.7), (2.2), (2.7), (2.9), decide whether the weighted prelimit control can, after a lawful conversion from viscosity `nu=f(lambda)` to viscosity one, force one of the standard CKN quantities `A,E,C` below the universal epsilon threshold on a unit-parabolic cylinder. Pressure `D` is audited as an interface check even though Seregin's displayed `g0` criterion uses `A,E,C`.

Allowed outcome here: `DIRECT_CKN_BRIDGE_LICENSED`, `DIRECT_CKN_BRIDGE_ESTIMATE_INSUFFICIENT`, or `CANNOT_CHECK_NORMALIZATION_OR_SOURCE`.

## Source binding

Seregin defines `F_lambda(a)=f(lambda a)/f(lambda)` for `lambda a<=1`, with `f` increasing, `f(lambda)->0`, `f(1)=1`, and obtains

`M1 >= A_F(V,a)+E_F(V,a)+D_F(P,a)`

for the scaled fields `V=v^lambda`, `P=q^lambda`. Thus, writing `nu=f(lambda)`,

`A(V,a) <= M1/F^2`, `E(V,a) <= M1/F`, `D(P,a) <= M1/F^2`.

From (2.7), direct substitution into Navier–Stokes gives

`d_tau V + V.grad V - nu Delta V + grad P = 0`, `div V=0`.

This prelimit equation has viscosity `nu`; Theorem 3.1's limiting equation is Euler. A unit-viscosity epsilon-regularity theorem therefore cannot be silently applied either to `V` or to the Euler limit.

## All affine parabolic unit-viscosity normalizations

Take

`W(z,s)=c V(alpha z,beta s)`, `Pi(z,s)=c^2 P(alpha z,beta s)`.

Matching the convection and diffusion coefficients to one gives

`beta=c alpha`, `alpha^2=beta nu`, hence

`c=alpha/nu`, `beta=alpha^2/nu`.

So every such normalization is equivalent to this one-parameter family; the convenient representative `alpha=1` is

`W(z,s)=nu^{-1} V(z,s/nu)`, `Pi(z,s)=nu^{-2}P(z,s/nu)`.

This coefficient calculation is exact and removes the apparent freedom to choose an amplitude/time scaling that avoids the viscosity cost.

## Lawful target cylinder and aspect-ratio cost

A target unit-parabolic cylinder `Q_W(r)=B(r)x(-r^2,0)` maps to a source region with spatial radius `alpha r` and time depth `alpha^2 r^2/nu`. To fit inside `Q_V(a)=B(a)x(-a^2,0)` for `0<nu<=1`, it is necessary that

`r <= a sqrt(nu)/alpha`.

The largest lawful target cylinder therefore has `r=a sqrt(nu)/alpha`. This is the parabolic aspect-ratio loss. Using a smaller `r` only worsens the scale-normalized upper certificates below.

## Exact A/E/D transport

On `r=a sqrt(nu)/alpha`, direct change of variables and spatial containment give alpha-independent bounds:

`A(W,r) <= M1 nu^{-5/2} F^{-2}`,

`E(W,r) <= M1 nu^{-3/2} F^{-1}`,

`D(Pi,r) <= M1 nu^{-3} F^{-2}`.

The powers are invariant across the entire admissible `alpha` family. In particular, `alpha` is not an escape parameter.

For `C`, the standard local multiplicative estimate

`C(V,a) <= c [ A(V,a)^{3/4} E(V,a)^{3/4} + A(V,a)^{3/2} ]`

gives

`C(W,r) <= c M1^{3/2} nu^{-3}[F^{-9/4}+F^{-3}]`.

This is used only as a direct certificate audit, not as an assertion that the actual `C` is large.

## Counterexample-first optimization of the certificate

Because `lambda a<=1` and `f` is increasing with `f(1)=1`,

`F_lambda(a)=f(lambda a)/f(lambda) <= 1/nu`.

Therefore even the maximally favorable source-certified `F` leaves the **derived upper-bound expressions** with floors

- `A` certificate: `M1 nu^{-5/2}F^{-2} >= M1 nu^{-1/2}`;
- `E` certificate: `M1 nu^{-3/2}F^{-1} >= M1 nu^{-1/2}`;
- `D` certificate: `M1 nu^{-3}F^{-2} >= M1 nu^{-1}`;
- multiplicative `C` certificate: leading expression `~ M1^{3/2}nu^{-3}F^{-9/4} >= M1^{3/2}nu^{-3/4}` up to the fixed inequality constant.

As `nu->0`, these direct certificate bounds do not force CKN smallness. This statement is about what follows from the ledger and this normalization architecture; it does **not** imply lower bounds for the true `A,E,C,D`, and it does not exclude a different argument using cancellation, signed flux, moving-radius compactness, or additional structure.

## Logarithmic specialization

For Seregin's logarithmic example `f(lambda)=L^{-gamma}`, `L=ln(e/lambda)`, let `h=ln(e/(lambda a))`. Then

`nu=L^{-gamma}`, `F=(L/h)^gamma=nu^{-1}h^{-gamma}`.

Hence the direct normalized certificates become, in particular,

`E(W,r) <= M1 nu^{-1/2} h^gamma`,

`A(W,r) <= M1 nu^{-1/2} h^{2gamma}`,

and the leading multiplicative `C` certificate scales as `nu^{-3/4}h^{9gamma/4}`.

Thus the mesoscopic `F` gain cannot pay the unit-viscosity parabolic-aspect cost in this direct route. If `lambda a->0`, then `h->infinity`, making these certificate expressions worse; even the extremal source endpoint `h=O(1)` leaves the `nu^{-1/2}` A/E floor.

## Limit-passage and rigidity interface audit

This cycle does not change Seregin's fixed-cylinder convergence: the source gives local strong `L^{3 nu0}` convergence for `1<=nu0<10/9`, weak-* `L^{2,infinity}`, and weak gradient convergence on every fixed cylinder, while the limit solves Euler. The present obstruction occurs **before** any attempt to glue that local convergence to a unit-viscosity CKN theorem.

The following remain separate open gluing coordinates: moving-radius/rate-compatible compactness; pressure/far-field tail localization; noncompact translation/dilation leakage; producer ancestry of a moving incoming core; and any Euler-side rigidity or unique-continuation consumer. No backward-uniqueness hypothesis has been licensed across the Navier–Stokes-to-Euler equation change.

## Expert-cell disposition

Seven roles were used: partial-regularity analyst; Seregin source auditor; scaling/dimensional analyst; pressure analyst; concentration-compactness analyst; adversarial falsifier; RAKL metrology/authority analyst. Their scoped consensus is:

`DIRECT_CKN_BRIDGE_ESTIMATE_INSUFFICIENT`.

The smallest reusable obstruction is `O-NS-B2a1a2-F-GAIN-CANNOT-BEAT-NU-ASPECT-COST`: the weighted gain `F` is bounded by `nu^{-1}`, whereas lawful unit-viscosity/unit-parabolic normalization costs at least a residual `nu^{-1/2}` in the direct A/E certificate.

## Routing consequence

Flatten the direct `LIFT -> unit-viscosity CKN from (2.9) alone` family. Reopen orthogonal work on a proof that stays in the variable-viscosity/moving-radius coordinates, or on prelimit signed/no-incoming-flux control with the Hill translating-core construction retained only as a shadow falsifier. Do not reinterpret this route pruning as root progress.
