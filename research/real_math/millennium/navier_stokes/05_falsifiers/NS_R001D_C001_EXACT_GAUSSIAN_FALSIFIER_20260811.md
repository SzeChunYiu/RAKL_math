# NS-R001d-C001 exact Gaussian falsifier

**Result authority:** `VERIFIED_EXACT_ROUTE_CALIBRATION_PENDING_EXACT_HEAD_CI / STATIC_SNAPSHOT_HYPOTHESIS_REFUTED / NO_NAVIER_STOKES_TRAJECTORY_COUNTEREXAMPLE / NO_NOVELTY / ROOT_AUTHORITY_NONE`.

## Frozen target

Candidate `NS-R001d-C001` tests only whether kinetic energy can uniformly bound Miller's scale-invariant projected-remainder ratio at a single smooth rapidly decaying divergence-free initial-data snapshot.

Let

`A(x,y,z) = (xy, yz, xz) exp(-r^2/2)`, `r^2=x^2+y^2+z^2`,

and set `v=curl A`. Explicitly,

- `v_1 = -y(xz-z^2+1) exp(-r^2/2)`,
- `v_2 = z(x^2-xy-1) exp(-r^2/2)`,
- `v_3 = x(y^2-yz-1) exp(-r^2/2)`.

Thus `v` is smooth, Schwartz, and divergence free.

For

- `S=(nabla v+nabla v^T)/2`,
- `omega=curl v`,
- `F=(v·nabla)S+S^2+(3/4)omega⊗omega`, and
- `D=-Delta S`,

exact polynomial-times-Gaussian integration gives

`int_R3 |v|^2 dx = (3/2) pi^(3/2)`,

`int_R3 |D|^2 dx = (3861/32) pi^(3/2)`,

and

`int_R3 F:D dx = (8/27)(2 pi/3)^(3/2) = (16 sqrt(6)/243) pi^(3/2) > 0`.

The application regression recomputes these coefficients from the vector potential using exact `Fraction` polynomial algebra and Gaussian moments; no floating-point quadrature is used.

## Projection binding

Miller's `P_st` is the orthogonal projection onto the strain constraint space. Since `S` is a strain tensor and the strain space is preserved by `-Delta`, `D=-Delta S` lies in that space. Hence, for `R=P_st F`,

`<R,D> = <P_st F,D> = <F,D>`.

Cauchy-Schwarz therefore yields

`Q(v) = ||R||_2/||D||_2 >= |<F,D>|/||D||_2^2`

and the exact positive lower bound

`Q(v) >= 512 sqrt(6) / 938223`.

This avoids the invalid substitution `||P_st F|| -> ||F||`.

## Fixed-energy concentration

For `lambda>0`, define

`v_lambda(x)=lambda^(3/2) v(lambda x)`.

This family preserves kinetic energy exactly:

`||v_lambda||_2^2 = ||v||_2^2 = (3/2) pi^(3/2)`.

It is deliberately **not** the Navier–Stokes solution scaling. It is used only to range over admissible smooth rapidly decaying divergence-free initial data at one snapshot.

The exact scaling exponents are:

- `S_lambda ~ lambda^(5/2)`,
- `D_lambda=-Delta S_lambda ~ lambda^(9/2)` pointwise, so `||D_lambda||_2^2 ~ lambda^6`,
- every term in `F_lambda` is pointwise `~lambda^5`, and
- `<F_lambda,D_lambda> ~ lambda^(13/2)`.

Thus

`Q(v_lambda) >= (512 sqrt(6)/938223) lambda^(1/2) -> infinity`.

## Falsifier result

The frozen hypothesis `H_snapshot` is refuted:

> There is no finite function of kinetic energy alone that uniformly bounds `Q(u)=||P_st((u·nabla)S+S^2+(3/4)omega⊗omega)||_2/||-Delta S||_2` over all smooth rapidly decaying divergence-free initial data.

This is stronger than merely showing that energy cannot force `Q<1`: at fixed kinetic energy the ratio is unbounded.

## Exact scope

This does **not** say that `Q(u(t))` becomes large along any one Navier–Stokes solution. It does not refute:

- a bound for every `t>0` with explicit time dependence;
- a time-integrated Miller remainder estimate;
- semigroup smoothing combined with nonlinear structure;
- frequency-local depletion;
- pressure/advection coherence;
- another exact trajectory invariant or monotonicity mechanism.

The correct residual is therefore dynamic: if Miller's decomposition contributes to a global-regularity route, the load-bearing estimate must use actual positive-time Navier–Stokes evolution or additional critical information, not static kinetic energy alone.
