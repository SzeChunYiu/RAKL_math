# NS-R001d-C001 — fixed-energy snapshot remainder-ratio screen

**Authority at proposal:** `STRICT_RAKL_CANDIDATE / ROUTE_HYPOTHESIS / NO_THEOREM_AUTHORITY / NO_NOVELTY_AUTHORITY / ROOT_AUTHORITY_NONE`.

**Parent atom:** `NS-R001d`.

**Frozen before proposal:** context packet `sha256:b846a739651692306c82255b1e7f76cd13347b4c00bc3f61e2ea28d3c7bb711f`, dual-memory review `sha256:71063a2b8249886ddd05fbf7e160f15a27c6c9e9abb93d8d3b43e9bacf08b9da`, and pre-candidate trace through `NS-R001d-E007`.

## Exact route hypothesis

Let `u` range over smooth rapidly decaying divergence-free vector fields on `R^3`, viewed only as admissible Navier–Stokes initial data. Put

- `S = (nabla u + nabla u^T)/2`,
- `omega = curl u`,
- `F = (u·nabla)S + S^2 + (3/4) omega⊗omega`,
- `R = P_st F`, with `P_st` the orthogonal projection onto the strain constraint space,
- `D = -Delta S`, and
- `Q(u) = ||R||_2 / ||D||_2` when `D != 0`.

The weakest static bridge worth testing is:

> **H_snapshot:** there exists a finite function `B(E)` such that every smooth rapidly decaying divergence-free initial datum with `||u||_2^2 = E` satisfies `Q(u) <= B(E)`.

This is deliberately weaker than a bound `Q<1`. If even finite energy cannot bound `Q` at one snapshot, then no direct energy-only route to Miller's perturbative regime can work on the full Clay initial-data class.

## Frozen falsifier

Use the Gaussian vector potential

`A(x,y,z) = (xy, yz, xz) exp(-(x^2+y^2+z^2)/2)`

and set `v = curl A`. This is smooth, Schwartz and divergence free. Compute exactly:

1. `E0 = int |v|^2`;
2. `D0^2 = int |-Delta S(v)|^2`;
3. the strain-space pairing `J0 = int F(v):(-Delta S(v))`.

Because `D=-Delta S` lies in the strain space and `P_st` is an orthogonal projection,

`<R,D> = <P_st F,D> = <F,D>`.

Thus any exact `J0 != 0` gives the rigorous lower bound

`Q(v) >= |J0| / ||D||_2^2 > 0`

without replacing the nonlocal projected norm by an unprojected surrogate.

Then form the fixed-energy concentration family

`v_lambda(x) = lambda^(3/2) v(lambda x)`.

This is **not** the Navier–Stokes solution scaling and is not asserted to be one trajectory. It is a family of admissible initial data with identical kinetic energy. Under this concentration,

- `S_lambda` scales pointwise as `lambda^(5/2)`,
- `D_lambda=-Delta S_lambda` scales pointwise as `lambda^(9/2)`, hence `||D_lambda||_2^2` as `lambda^6`,
- every term in `F_lambda` scales pointwise as `lambda^5`, and
- `<F_lambda,D_lambda>` scales as `lambda^(13/2)`.

Therefore a nonzero seed pairing forces

`Q(v_lambda) >= c lambda^(1/2)`.

## Result branches frozen before execution

- **If `J0 = 0`:** this seed is nondiscriminating. Do not infer snapshot control; choose another exact divergence-free seed under the same frozen candidate.
- **If `J0 != 0`:** `H_snapshot` is refuted: fixed kinetic energy does not uniformly bound `Q` on the smooth rapidly decaying divergence-free initial-data class.
- **If exact projection binding cannot be justified:** result is `CANNOT_CHECK`; do not use an unprojected norm as a replacement.

## Scope boundary

A negative result is only a **static energy-to-critical-coordinate no-go**. It does not refute any estimate that starts at positive time, integrates over time, uses actual Navier–Stokes semigroup smoothing, frequency transfer, pressure coherence, or another trajectory property. It is not a singular solution and cannot close the Clay problem.
