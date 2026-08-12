# NS-B2a1a2 — viscosity-normalized CKN bridge audit (R9)

**Authority:** proposal/shadow research only. Root #4 remains `OPEN_NO_SOLUTION_CERTIFICATE`. This note proves only an insufficiency of the direct estimate obtained from Seregin's weighted prelimit ledger; it does **not** prove that the actual solution lacks a small CKN scale.

## Source-bound setup

Primary source: G. Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468v1 (28 Jun 2026).

Relevant source surfaces were rechecked in parsed primary text and visually on the PDF:

- suitable weak Navier–Stokes and the displayed CKN regularity carrier `g0(v)=min{liminf A, liminf E, liminf C}` in (1.1);
- weighted `A_f,E_f,D_f` and `0<f<=1`, `f(lambda)->0`, `f(1)=1` in (1.7);
- `F_lambda(a)=f(lambda a)/f(lambda)` for `a lambda<=1` in (2.2);
- Euler scaling
  `w(y,tau)=v^lambda=lambda f(lambda)v(x,t)`, `pi=q^lambda=lambda^2 f(lambda)^2 q(x,t)`, `x=lambda y`, `t=lambda^2 f(lambda) tau` in (2.7);
- prelimit bound (2.9): for `0<a<1/lambda`,
  `A_{F_lambda}(w,a)+E_{F_lambda}(w,a)+D_{F_lambda}(pi,a) <= M1`;
- logarithmic `f(lambda)=log(e/lambda)^(-gamma)` in (2.10);
- Theorem 3.1, whose limit equation is Euler and whose displayed limit ledger is (3.5).

Write

`nu := f(lambda)` and `F := F_lambda(a)=f(lambda a)/nu`.

Direct substitution in the Navier–Stokes equation gives

`partial_tau w + w.grad w - nu Delta w + grad pi = 0`.

Thus the Seregin cylinder `Q(a)` has Euler-scaled spatial radius `a` and time depth `a^2`, but in original physical variables it corresponds to spatial radius `lambda a` and time depth `lambda^2 nu a^2`.

## Counterexample-first discriminator: restore the physical parabolic aspect ratio

A physical unit-viscosity parabolic cylinder `Q(r)` can fit inside that source cylinder only if

`r <= lambda a`, and `r^2 <= lambda^2 nu a^2`.

Because `0<nu<=1`, the maximal such radius is

`r_* = lambda a sqrt(nu)`.

Equivalently, if one first normalizes the `nu`-viscosity scaled equation to unit viscosity via `U(y,s)=nu^{-1}w(y,s/nu)` and `P(y,s)=nu^{-2}pi(y,s/nu)`, the largest standard parabolic subcylinder has radius `b=a sqrt(nu)`. This is the same coordinate calculation.

The weighted source ledger gives

`sup_{-a^2<tau<0} (1/a) int_{B(a)} |w|^2 <= M1/F^2`,

`(1/a) int_{Q(a)} |grad w|^2 <= M1/F`,

`(1/a^2) int_{Q(a)} |pi|^(3/2) <= M1/F^2`.

Transforming the physical CKN-scale quantities on `Q(r_*)`, using `B(a sqrt(nu)) subset B(a)`, gives exactly

`A(v,r_*) <= M1 / (nu^(5/2) F^2)`,

`E(v,r_*) <= M1 / (nu^(3/2) F)`,

`D(q,r_*) <= M1 / (nu^3 F^2)`.

The powers were independently checked both in original variables and through the unit-viscosity `(U,P)` normalization. A symbolic exponent check was used only as calibration; the displayed changes of variables are the proof.

### Why the source gain cannot pay this direct cost

Since the source assumes `f:(0,1]->(0,1]`, for every allowed `a lambda<=1`,

`F_lambda(a)=f(lambda a)/nu <= 1/nu`.

Therefore a direct source-certified `E`-smallness argument would require

`nu^(3/2) F_lambda(a) -> infinity`,

whereas source-validity forces

`nu^(3/2) F_lambda(a) <= sqrt(nu) -> 0`.

Likewise direct `A` smallness through this estimate would require `nu^(5/2)F^2 -> infinity`, but the source cap gives `nu^(5/2)F^2 <= sqrt(nu)->0`. The pressure carrier has `nu^3 F^2 <= nu ->0`. Even at the largest permitted gain `F≈nu^{-1}`, the resulting certified upper envelopes scale no better than

`A: O(M1 nu^{-1/2})`, `E: O(M1 nu^{-1/2})`, `D: O(M1 nu^{-1})`.

These are statements about the **strength of this estimate**, not lower bounds on the actual quantities.

For the logarithmic example, let `L=log(e/lambda)` and `h=log(e/(lambda a))`. Then `nu=L^{-gamma}` and `F=(L/h)^gamma`. On the predecessor's genuine mesoscopic window `1<<h<<L`, the direct physical-parabolic upper envelopes are

`A <= M1 L^(gamma/2) h^(2gamma)`,

`E <= M1 L^(gamma/2) h^gamma`,

`D <= M1 L^gamma h^(2gamma)`,

so the moving-radius gain that is strong in the Euler-scaled ledger is quantitatively overwhelmed by restoring the unit-viscosity parabolic aspect ratio.

## Optimality and scope of the covering step

For a desired physical radius `r=lambda b`, the corresponding Euler-scaled time depth is `b^2/nu`. A centered source cylinder `Q(c)` can cover both the spatial and temporal requirements only if `c>=b` and `c^2>=b^2/nu`; the minimal admissible source scale is `c=b/sqrt(nu)`. Hence the `sqrt(nu)` loss above is not an arbitrary choice of subradius within this direct centered-cylinder covering argument.

The ledger at the smaller spatial radius cannot simply be substituted, because it controls only the shorter terminal interval of length `c^2`; covering the required longer interval would need an additional time-uniform/local-energy propagation input not present in the bare `(2.9)` estimate. Such additional structure remains an open route rather than being silently assumed.

## Pressure / nonlocal / endpoint audit

- Pressure normalization is explicit: `pi=lambda^2 nu^2 q`; the `D` calculation carries the full `nu^{-3}` physical-parabolic penalty.
- No harmonic-pressure cancellation or annular pressure localization is used. Therefore this result does not prune a future signed pressure-flux mechanism.
- The source domain has `a<1/lambda`; the cap `F<=nu^{-1}` holds uniformly and can be approached but need not be attained at the strict endpoint.
- Constants are fixed through `M1`; no smallness of `M1` is assumed. The conclusion is asymptotic as `nu->0`.
- No derivative gain, bootstrap, or regularity assumption is used; there is no circular invocation of CKN.
- `r_* <= sqrt(nu) ->0` when `a<1/lambda`, so these are genuinely vanishing physical radii; failure is not caused by choosing a macroscopic CKN scale.

## Expert cell

1. **Partial-regularity analyst:** confirmed that the relevant direct target is a standard unit-viscosity parabolic scale and that source (1.1) makes small `A` or `E` a legitimate sufficient carrier; no root implication follows from estimate failure.
2. **Seregin source auditor:** confirmed selectors (1.1), (1.7), (2.2), (2.7), (2.9), (2.10), and Theorem 3.1; no moving-radius convergence rate or thin-time epsilon criterion is present on the inspected source surface.
3. **Scaling/dimensional analyst:** independently derived `r_*=lambda a sqrt(nu)` and the `nu^{-5/2}`, `nu^{-3/2}`, `nu^{-3}` penalties.
4. **Pressure/harmonic analyst:** confirmed `q`/`pi` normalization and that no pressure cancellation is being claimed.
5. **Concentration-compactness analyst:** kept the conclusion local: this prunes only the direct local CKN insertion; producer tightness/no-incoming-flux remains separate.
6. **Adversarial falsifier:** maximized the available gain using only `F<=nu^{-1}`; even the maximal source-certified gain cannot make the direct sufficient bounds small.
7. **RAKL authority/metrology analyst:** confirms the mathematical idea was noticed during source scoping before durable atom freeze, so strict prospective hypothesis-generation credit is denied; consequential verification is bound to #227 and remains proposal/shadow with `0/3` independent reviews.

Consensus: `DIRECT_CKN_BRIDGE_ESTIMATE_INSUFFICIENT / LOCAL_ESTIMATE_INTERFACE_FAILURE / ACTUAL_SMALL_SCALE_NOT_REFUTED / ROOT_AUTHORITY_NONE`.

## Episode -> diagnosis -> obstruction/lesson boundary

**Episode:** the frozen #227 discriminator tested whether the predecessor's mesoscopic `F_lambda` gain can be re-parabolized into a physical CKN smallness certificate.

**Diagnosis:** the Euler scaling shortens physical time by `nu`; restoring a unit-viscosity parabolic cylinder shrinks the admissible radius by `sqrt(nu)` and introduces stronger normalization costs than the source weight can pay.

**Reusable obstruction:** `O-NS-B2a1a2-VISCOSITY-NORMALIZATION-GAIN-DEFICIT` — under only (2.9), `F_lambda<=nu^{-1}` but the direct `E` bridge needs gain beyond `nu^{-3/2}` (and `A` beyond `nu^{-5/4}` in F-power terms).

**Candidate lesson:** `L-NS-B2a1a2-EULER-GAIN-DOES-NOT-PAY-PARABOLIC-COST` — before importing a parabolic epsilon criterion into an inviscid/Euler scaling, explicitly price the source cylinder's time-aspect and viscosity normalization; smallness in the Euler-scaled ledger is not itself a physical CKN certificate.

The lesson remains proposal/shadow. The next route should return to producer-specific no-incoming/tightness or a genuinely different carrier that does not silently demand the missing parabolic aspect ratio; any signed-flux route must still survive the translating-core falsifier from open PR #219.
