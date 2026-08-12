# XM-PC-NS-001 C001 — exact enstrophy-sign result

**Authority:** proposal/shadow local verification only. **Root:** Navier–Stokes remains `OPEN_NO_SOLUTION_CERTIFICATE`. **Independent mathematical review:** `0/3`.

## Frozen candidate and chronology

This result consumes the already-passing pre-candidate gate `XM-PC-NS-001-PRE-CANDIDATE-GATE-20260812` and the subsequently committed candidate freeze `XM_PC_NS_001_C001_ENSTROPHY_FIELD_FREEZE_20260812.json` at commit `58948d71d63a79a9daba03333eedbd6d7e5adca7`. The candidate freeze contains no stretching coefficient, dissipation coefficient, derivative sign, or amplitude threshold.

Work on the periodic torus `T^3=(R/2πZ)^3` with viscosity `ν>0`. The frozen initial datum is `u_0=A v`, `A>0`, where

```text
v(x)=Σ_{j=1}^3 [a_j cos(k_j·x)+b_j sin(k_j·x)]

k1=( 3, 0, 0),  a1=( 0, 0, 1),  b1=( 0,-1, 0)
k2=( 0, 1, 1),  a2=( 0, 1,-1),  b2=( 1, 0, 0)
k3=(-3,-1,-1),  a3=(-1, 3, 0),  b3=( 1, 0,-3).
```

Each `k_j·a_j=k_j·b_j=0`, hence `div v=0`. The datum is a real trigonometric polynomial, so the standard local classical periodic Navier–Stokes solution exists for a nonzero time interval; only its exact derivative at `t=0` is used.

## Exact enstrophy identity

For `ω=curl u`, periodic integration by parts gives

`(1/2) d/dt ||ω||_2^2 = ∫_{T^3} ω_i ω_j ∂_j u_i dx - ν ||∇ω||_2^2`.

For `u=A v` at `t=0`, write

`I(v)=∫ (curl v)_i (curl v)_j ∂_j v_i dx`, `D(v)=∫ |∇ curl v|^2 dx`.

Then

`(1/2) d/dt ||ω||_2^2 |_{t=0} = A^3 I(v) - ν A^2 D(v)`.

## Exact Parseval audit

For one real mode `a cos(k·x)+b sin(k·x)`, the spatial mean of `|curl|^2` is `(|k×a|^2+|k×b|^2)/2`, and the spatial mean of `|∇curl|^2` is `|k|^2` times that number. The three frozen modes give:

```text
mode k1: mean |curl|^2 =   9, mean |∇curl|^2 =   81
mode k2: mean |curl|^2 =   3, mean |∇curl|^2 =    6
mode k3: mean |curl|^2 = 110, mean |∇curl|^2 = 1210
```

Therefore

`(2π)^(-3) ||curl v||_2^2 = 122`,

`(2π)^(-3) D(v) = 1297`.

## Exact cubic Fourier audit

Use the real-field Fourier convention `v(x)=Σ_k V_k e^{ik·x}`, with `V_k=(a_k-i b_k)/2` and `V_{-k}=conj(V_k)`. Then `Ω_k=i k×V_k`. The spatial mean of the stretching term is the finite resonant sum

`Σ_{p+q+r=0} (Ω_p·V_r)(Ω_q·i r)`.

For the frozen support `{±k1,±k2,±k3}`, the only nonzero ordered resonant contributions are

```text
 27i/2, -27i/4, -27i/2,  27i/4,
  3i/4,  -9i/4,  -3i/4,   9i/4,
     6i,    -15i,     -6i,     15i.
```

They cancel exactly. Hence

`I(v)=0`.

No floating-point sign decision is used; the calculation is finite Gaussian-rational Fourier algebra.

## Verdict

For every `A>0` and every `ν>0`,

`(1/2) d/dt ||ω||_2^2 |_{t=0} = -1297 ν A^2 (2π)^3 < 0`.

Thus the frozen candidate **does not falsify** bare enstrophy monotonicity. It is a candidate-specific null of the vortex-stretching integral, not evidence that enstrophy is globally monotone in 3D Navier–Stokes.

Outcome: `CANDIDATE_FAILURE_ZERO_STRETCHING_COEFFICIENT`.

Failure id: `F-XM-PC-NS-001-C001-TRIAD-STRETCHING-CANCELLATION`.

Diagnosis status: `OBSERVED_ONLY / CANDIDATE_SPECIFIC`; the exact resonant cancellation is established, but one failed field does not support a reusable obstruction or a blacklist of Fourier-triad falsifiers.

## Residual and next action

The parent obstruction `OBS-XM-PC-NS-ENSTROPHY-SIGN` remains open. The next admissible action is to reopen the PATH coordinate, incorporate this candidate-specific cancellation into failure memory, and only then freeze a second structurally distinct field or field family under a fresh trace continuation. A second field must not be repaired inside C001 after seeing this outcome.

The Poincaré→Navier–Stokes JUMP still has target authority `NONE`; no Ricci-flow monotonicity, surgery, noncollapse, or extinction theorem transfers from this candidate result. There is no local-to-global/gluing failure in C001 because the local falsifier itself did not fire.
