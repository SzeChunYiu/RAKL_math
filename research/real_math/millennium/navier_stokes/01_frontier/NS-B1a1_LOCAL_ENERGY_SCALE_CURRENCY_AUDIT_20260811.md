# NS-B1a1 local-energy scale-currency discriminator

**Status:** `EXACT_SCALING_ROUTE_DIAGNOSTIC / ABSOLUTE_SHELL_SUMMATION_REJECTED / NO_NAVIER_STOKES_THEOREM / ROOT_AUTHORITY_NONE`

## 1. Exact question

Let `(v,q)` be a suitable/local-energy solution on a parabolic cylinder `Q_R=B_R x (t_0-R^2,t_0)` and let

- `A(R)=ess sup_t R^-1 ∫_{B_R}|v|^2`,
- `C(R)=R^-2 ∫_{Q_R}|v|^3`,
- `D(R)=R^-2 ∫_{Q_R}|q-[q]_{B_R}(t)|^(3/2)`,
- `E(R)=R^-1 ∫_{Q_R}|∇v|^2`.

These are the Albritton–Barker critical quantities. Take a nonnegative parabolic cutoff `phi_R` with support in `Q_R`, equal to one on a fixed smaller cylinder, and

`|∂_t phi_R|+|Δ phi_R| <= c R^-2`, `|∇phi_R| <= c R^-1`.

The local-energy inequality has the schematic form

`energy + 2*dissipation <= T_2 + T_3 + T_p`

with cutoff quadratic term `T_2`, cubic transport `T_3`, and pressure work `T_p`. The natural localized kinetic-energy scale is `R`. The discriminator asks whether `R^-1 |T_j|` carries any strict scale decay.

## 2. Exact homogeneity calculation

### Quadratic cutoff term

Using `sup_t ∫_{B_R}|v|^2 <= R A(R)` and a time interval of length `R^2`,

`|T_2| <= c R^-2 ∫_{Q_R}|v|^2
          <= c R^-2 * R^2 * R A(R)
          = c R A(R)`.

Therefore

`R^-1 |T_2| <= c A(R)`.

### Cubic transport

`|T_3| <= c R^-1 ∫_{Q_R}|v|^3
          = c R^-1 * R^2 C(R)
          = c R C(R)`,

so

`R^-1 |T_3| <= c C(R)`.

### Pressure-velocity work

A spatially constant pressure gauge contributes zero because `div v=0`, so use `q-[q]_{B_R}(t)`. Hölder gives

`∫_{Q_R}|q-[q]_{B_R}||v|
 <= (R^2 D(R))^(2/3) (R^2 C(R))^(1/3)
 = R^2 D(R)^(2/3) C(R)^(1/3)`.

Hence

`|T_p| <= c R D(R)^(2/3) C(R)^(1/3)`

and

`R^-1 |T_p| <= c D(R)^(2/3) C(R)^(1/3)`.

The localized endpoint kinetic energy and dissipation are themselves of natural size `R A(R)` and `R E(R)`.

Thus under finite Type-I control `A+C+D+E <= I` on every admissible cylinder,

`R^-1 (|T_2|+|T_3|+|T_p|) <= C_* [A+C+D^(2/3)C^(1/3)] <= C_*(I+I)`,

with **no positive power of `R`**.

## 3. Negative discriminator

For a dyadic chain `R_n=2^-n R_0`, the standard absolute estimate yields at best

`sum_{n=0}^{N} R_n^-1 |T(R_n)| <= C(I) (N+1)`.

It therefore does not produce a finite total charge as `N→∞`. This does not say the local-energy inequality is useless; it says that **absolute termwise shell accounting is a critical local balance, not a terminal multiscale budget**.

Annular support does not repair the conclusion automatically. Unnormalized physical annuli can be disjoint, but the critical normalization changes with `R`, while nested core content can be reused at each scale. Cubic transport and pressure work also have no favorable sign. A successful summation requires an additional theorem identifying a signed increment, an injective/disjoint charge, a strict decrement of a bounded potential, or a no-recrossing coordinate.

## 4. Exact residual theorem now needed

The next theorem-level object must have one of the following exact forms; none is presently claimed.

**Scale potential form.** There exist a bounded-below functional `Phi` on certified Type-I descendant states, `theta in (0,1)` and `delta>0` such that every dynamically realized strict descendant satisfies

`Phi(theta R) <= Phi(R)-delta`

after all translation/center changes and pressure gauges are accounted for.

**Summable increment form.** There are nonnegative increments `J_n`, derivable from the equation, such that `sum_n J_n < infinity` from a source-valid finite budget, while every certified singular descendant forces `J_n >= delta>0`. The second clause must be an annular-renewal/no-core-recycling theorem, not an epsilon-regularity lower bound on a nested core.

**Compactness/rigidity form.** From a hypothetical Type-I singularity, rescale to a non-trivial mild bounded ancient `(U,P)` with finite `I`; prove an additional compactness/tightness property strong enough either to:
1. produce times `t_k→-infinity` with `sup_k ||U(t_k)||_3<infinity`, then use Albritton–Barker Theorem 1.2; or
2. meet the exact hypotheses of another Liouville/backward-uniqueness theorem and force `U=0`.

## 5. Blow-up limit audit

The current source-valid limit passage needs:

- uniform scale-invariant local velocity/pressure bounds on compact rescaled cylinders;
- subsequential `v_k -> U` **strongly in `L^3_loc`** and `q_k ⇀ P` weakly in `L^(3/2)_loc`;
- persistence of singularity/non-triviality rather than relying on a merely weak velocity limit;
- local pressure decomposition into a Calderón–Zygmund part plus a harmonic piece, with pressure gauge normalized locally;
- a separate far-field/tightness argument, because local compactness does not transport global `L^3`, exterior decay, or a canonical pressure normalization;
- explicit handling of translations/dilations and moving centers to prevent profile leakage.

Albritton–Barker's compactness lemma supplies the local strong/weak convergence under the stated local bounds, and their persistence proposition shows how singularity is retained. Their pressure argument explicitly separates a local Calderón–Zygmund component from a harmonic component. These facts do **not** supply the missing far-field theorem.

## 6. Backward uniqueness and decay audit

Backward uniqueness remains a possible terminal rigidity mechanism, but it cannot be invoked from finite `I` by name alone. The finite-I/local-energy packet presently does not generate:

- global `L^3` control,
- terminal-time vorticity vanishing,
- exterior vanishing/decay at the terminal slice,
- or the exact global weighted hypotheses required by a selected backward-uniqueness theorem.

Lei–Yang–Yuan's whole-space bounded-mild backward-uniqueness result is therefore a downstream bridge to audit after a terminal/global hypothesis is produced; it is not a scale-currency theorem.

## 7. Adversarial controls and normalized failure

- **Noncompact symmetry:** moving centers/dilations can prevent one fixed annular charge from following the profile.
- **Profile leakage:** weak/local convergence can lose the far field; strong `L^3_loc` preserves local nontriviality but not global tightness.
- **Core recycling:** the same nested critical core can be counted at every scale.
- **Uncontrolled far field:** neither local compactness nor `I<∞` gives global `L^3`.
- **Unique-continuation hypothesis failure:** a rigidity theorem cannot be used before its terminal/global assumptions are manufactured.
- **Local-to-global depletion gap:** vorticity alignment/geometric depletion remains local unless integrated into a scale/global estimate.
- **DSS hostile calibration:** scale recurrence is structurally compatible with suitable/local-energy formulations in known forward DSS constructions; this is a warning against deriving strict scale decay from the inequality alone, not a blow-up counterexample.

Normalized failure:

`F-NS-B1a1-ABSOLUTE-LOCAL-ENERGY-SCALE-CURRENCY`

> The canonical absolute local-energy contributions are scale-critical after the natural `R` normalization; finite Type-I control gives an `O(I)` bound per realized scale but no finite total budget across an infinite dyadic descent.

Scope excludes signed cancellations, telescoping identities, monotonicity formulas, frequency-local transfer, almost-periodic/minimal-element compactness, and distinct unique-continuation bridges.

## 8. Route decision

The first discriminator is **negative**. Do not spend a candidate on sharper absolute shell constants. The next atom should target the smallest missing coordinate:

`NS-B1a1a — INCREMENT_OR_NO_RECYCLING`

Produce a source-valid signed/telescoping/no-recrossing quantity, or an annular-renewal theorem that prevents nested-core reuse, with translation/dilation and pressure localization built into the statement. If no such coordinate survives hostile DSS/moving-center/profile-leakage controls, rotate to a compactness/rigidity representation rather than assume a terminal scale.
