# NS-B1a3b-C001 — vorticity-direction transfer stability test

**Frozen candidate:** 2026-08-11T15:10:00Z  
**Authority:** `PROPOSAL_SHADOW_INTERFACE_TEST / NO_ROOT_AUTHORITY`  
**Pre-candidate trace:** `sha256:6560dd9a88cfb75241aee94843a96548b68026f0ba3db684473ccab92789273a`

## Candidate statement under test

> The convergence/control modes already registered in the Type-I local compactness package are, by themselves, strong enough to transport a normalized-vorticity-direction/coherence observable from approximating fields to the ancient limit.

This is deliberately narrower than a Navier–Stokes regularity theorem. Failure only proves that the **reported topology/data types alone** do not license the transfer. It does not prove that exact Navier–Stokes dynamics cannot supply an additional estimate.

## Falsifier A — local R3 topology calibration

Choose a fixed `chi in C_c^infty(R^3)` with `chi=1` on a nonempty ball. Define the vector potential

`A_n(x) = n^{-2} chi(x) (0, sin(n x_1), cos(n x_1))`

and the divergence-free field

`w_n = curl A_n`.

Frozen checks:

1. `div w_n = 0` identically and `w_n` is smooth compactly supported.
2. On every fixed domain containing `supp chi`, `||w_n||_L3 = O(n^{-1})`, hence `w_n -> 0` strongly in `L^3`.
3. `||grad w_n||_L2 = O(1)` because `grad w_n` contains at most two derivatives of `A_n`: the leading `n^2` phase factor exactly cancels `n^{-2}`.
4. On the core `chi=1`,
   `w_n=(0,n^{-1} sin(n x_1),n^{-1} cos(n x_1))`,
   `omega_n=curl w_n=(0,sin(n x_1),cos(n x_1))`,
   so `|omega_n|=1` and `xi_n=omega_n` rotates at frequency `n`.
5. For `x_1=0` and `y_1=pi/(2n)` inside the core, the directions are orthogonal while `|x-y|=pi/(2n)->0`. Thus the family is not equicontinuous, and every positive Hölder seminorm of `xi_n` grows at least like a constant times `n^alpha`.

If all five checks hold, strong local velocity convergence plus bounded first-derivative energy is not sufficient to transport direction coherence.

## Falsifier B — exact periodic Navier–Stokes calibration

On `T^3=(R/2piZ)^3`, fix amplitude `a>0` and define

`u_n(x,t) = (a/n) exp(-n^2 t) (0, sin(n x_1), cos(n x_1))`, `t>=0`, `p_n=constant`.

Frozen checks:

1. `div u_n=0`.
2. `(u_n·grad)u_n=0` because `u_1=0` and the field depends only on `x_1`.
3. `partial_t u_n - Delta u_n=0`; hence this is an exact smooth Navier–Stokes solution.
4. `omega_n=a exp(-n^2t)(0,sin(n x_1),cos(n x_1))`; wherever nonzero its direction rotates at frequency `n`.
5. At `t=0`, kinetic energy is `(2pi)^3 a^2/n^2` while `|omega_n|=a` everywhere and the direction Hölder seminorm grows like `n^alpha`.

This second calibration is **not** transferred as a theorem about the R3 Type-I ancient class: the periodic domain and forward-decaying shear-wave regime are material disanalogies. Its scoped role is to refute the idea that exact Navier–Stokes dynamics plus finite kinetic energy automatically produces a scale-uniform direction-coherence modulus.

## Pass/fail contract

- `FAIL_CANDIDATE / ROUTE_PRUNE` if both analytic calibrations pass. Residual: obtain a new source-valid strong-vorticity/orientation compactness, high-vorticity nondegeneracy, or direct coherence estimate from dangerous Type-I dynamics before using a direction criterion.
- `SURVIVES` if a listed analytic check fails or a load-bearing hypothesis in the stored Type-I interface already supplies the missing derivative/orientation stability.
- No outcome can change the root status or count as an independent mathematical review.
