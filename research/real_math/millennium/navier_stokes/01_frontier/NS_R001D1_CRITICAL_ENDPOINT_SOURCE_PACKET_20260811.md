# NS-R001d1 source packet — critical semigroup endpoint calibration

## Authority and root boundary

- Framework authority read for this cycle: `SzeChunYiu/RAKL@15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`.
- Application `main` observed at cycle start: `SzeChunYiu/RAKL_math@02cf72656e9da055ae9c3af173ca2207e03b3872`.
- Persistent Navier–Stokes control issue: `RAKL_math#4`.
- Exact root pursued: Clay statement (A), global smooth finite-energy unforced 3D incompressible Navier–Stokes on `R^3` for every smooth rapidly decaying divergence-free datum.
- Root status remains `OPEN_NO_SOLUTION_CERTIFICATE`.
- Parent `NS-R001d-C001` rejected only a static kinetic-energy bound for Miller's projected strain-remainder ratio. This child asks what ordinary positive-time parabolic evolution by itself can supply before invoking nonlinear depletion.

## Primary-source anchors

1. Charles L. Fefferman, *Existence and Smoothness of the Navier–Stokes Equation*, official Clay Mathematics Institute Millennium problem description.
2. Tosio Kato, *Strong L^p-Solutions of the Navier-Stokes Equation in R^m*, Math. Z. 187 (1984), 471–480, DOI `10.1007/BF01174182`.
3. L. Escauriaza, G. A. Seregin, V. Šverák, *L_{3,∞}-solutions of Navier–Stokes equations and backward uniqueness*, Russian Math. Surveys 58 (2003), 211–250, DOI `10.1070/RM2003v058n02ABEH000609`.
4. Herbert Koch and Daniel Tataru, *Well-posedness for the Navier–Stokes equations*, Adv. Math. 157 (2001), 22–35.
5. Tobias Barker and Christophe Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, arXiv:2003.06717.
6. Alexey Cheskidov and Taichi Eguchi, *Global well-posedness of the Navier–Stokes equations for small initial data in frequency localized Koch-Tataru's space*, arXiv:2503.11642.

These anchors establish surrounding solution spaces and conditional criteria. They do not supply an energy-to-critical global estimate.

## Exact baseline estimate

For a smooth mild solution on `R^3`,

`u(t)=e^{ν(t-s)Δ}u(s)-∫_s^t e^{ν(t-τ)Δ} P ∇·(u⊗u)(τ)dτ`.

For `q>2`, the heat-gradient estimate followed by the order-zero Leray projector gives

`||e^{νρΔ}P∇·F||_q <= C_q (νρ)^(-α(q)) ||F||_{q/2}`,

where `α(q)=1/2+3/(2q)`. Hence

`||B(u,u)(t)||_q <= C_q ν^(-α(q)) ∫_s^t (t-τ)^(-α(q)) ||u(τ)||_q^2 dτ`.

The spatial Navier–Stokes scaling exponent is `σ(q)=1-3/q`, so exactly

`α(q)=1-σ(q)/2`.

Thus `q>3` is subcritical/stronger with `α<1`; `q=3` is critical with `α=1`; and `2<q<3` is supercritical/weaker with `α>1`. At `q=3`, a bare substitution `||u(τ)||_3 <= M` leaves the logarithmically divergent integral `M^2∫(t-τ)^(-1)dτ`. This diagnoses that estimate, not Kato's critical local theory, which uses a finer solution space.

## Units, constants, pressure and nonlocality

Take `[x]=L`, `[t]=T`, `[u]=L/T`, `[ν]=L^2/T`. Then `||u||_q` has units `L^(1+3/q)/T`, `||u⊗u||_{q/2}` has `L^(2+6/q)/T^2`, and because `2α=1+3/q`, `(νρ)^(-α)` has units `L^(-1-3/q)`; after integration in time the units match `||u||_q` exactly. `C_q` depends on `q`, dimension three, and heat/Leray normalization; the displayed powers of `ν` are exact.

At `q=3`, `u⊗u∈L^{3/2}` and the Leray projector is bounded on that strong `L^p` range, so the projector changes constants rather than the exponent in this baseline absolute estimate. This does not make pressure irrelevant: absolute norms discard cancellations, and pressure-coherent/frequency-local mechanisms remain live.

## Generic heat-smoothing stress test

The linear heat semigroup gives `||e^{νtΔ}f||_3 <= C(νt)^(-1/4)||f||_2`. For `f_λ(x)=λ^(3/2)f(λx)`, kinetic energy is fixed. At `t_λ=τ/λ^2`, heat scaling gives

`||e^{νt_λΔ}f_λ||_3 = λ^(1/2)||e^{ντΔ}f||_3`.

Therefore ordinary viscosity alone does not produce a time-uniform critical `L^3` bound from kinetic energy across concentration scales. These are linear heat trajectories, not nonlinear Navier–Stokes trajectories.

## Candidate boundary

The first candidate may test only finite energy + ordinary heat smoothing + the standard absolute `L^{q/2}->L^q` mild bilinear estimate + a bare `L_t^∞L_x^3` bootstrap. A negative result may not be generalized to refined Kato spaces, Koch–Tataru/Carleson norms, frequency-local smallness, pressure cancellation, geometry, epsilon-regularity, concentration compactness, or any genuinely nonlinear trajectory mechanism.
