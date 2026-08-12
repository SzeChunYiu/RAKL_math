# NS-B1a4a — finite-I to one-slice self-similar-speed interface audit (R2)

Authority: proposal/shadow research evidence only. No theorem, candidate, root, or independent-review authority is claimed.

## Frozen question

Can the current Albritton–Barker finite-`I` Type-I/ancient lane be glued directly, without new estimates, to Pineau–Vicol Theorem 1.9 by treating the finite-`I` ledger as if it supplied the source theorem's one-time approximate-self-similarity carrier?

## Primary-source bindings

Albritton–Barker define the scale-invariant ledger on parabolic cylinders by `A` (local kinetic energy), `C` (space-time `L^3` velocity), `D` (space-time `L^(3/2)` pressure oscillation), and `E` (space-time `L^2` first velocity derivative), with `I=sup_Q(A+C+D+E)`. Their Theorem 1.1 identifies existence of a suitable weak Type-I singularity with existence of a nontrivial mild bounded ancient solution satisfying `I<∞`. The paper explicitly presents `I` as a weak Type-I notion and lists stronger Type-I quantities which imply it.

Pineau–Vicol Theorem 1.9 assumes instead, on `B_1 x [-1,0)`, three source carriers relevant here:

1. the pointwise Type-I bound `|u(x,t)| <= C_u/(sqrt(-t)+|x|)`;
2. an annular pressure bound `|p| <= C_p` on `1/2<|x|<3/4`;
3. at one sufficiently late time `t_bar`, smallness of the scaling-generator defect
   `sqrt(-t_bar)||(-t_bar)∂_t u - u/2 - (x·∇)u/2||_{L∞(B_1)} <= delta_0`.

In self-similar variables `U(y,s)=sqrt(-t)u(x,t)`, this is exactly smallness of `∂_s U(s_bar)`. Their Remark 1.11 allows a weaker Gaussian-weighted `L^1` smallness of `∂_s U`, but still requires a one-time self-similar-speed carrier.

## Counterexample-first carrier audit

With viscosity normalized to one, Navier–Stokes gives

`∂_t u = Δu - (u·∇)u - ∇p`.

Therefore

`∂_s U = sqrt(-t)[(-t)Δu - (-t)(u·∇)u - (-t)∇p - u/2 - (x·∇u)/2]`.

The finite-`I` ledger does **not, by definition**, contain the one-slice carriers appearing in this identity:

- `A` gives a local `L^2` time-slice velocity bound, not a one-slice derivative bound.
- `C` is a space-time `L^3` velocity quantity.
- `D` is a space-time `L^(3/2)` pressure-oscillation quantity, not a one-slice `∇p` or annular `L∞` bound.
- `E` is a space-time `L^2` bound on `∇u`, not a one-slice `Δu` bound.

Thus the direct estimate “finite `I` controls the Pineau–Vicol generator defect at some late time” has an explicit derivative/time-trace interface obligation. Scaling alone does not repair it: every term in the displayed generator is critical in similarity variables, so there is no small dimensional factor to exploit.

This is an interface diagnosis, **not** a proof that no dynamics-specific recurrence, smoothing, compactness-rigidity, or signed-cancellation theorem can generate the missing carrier.

## GLUE audit

The tempting chain

`finite I -> Albritton–Barker Type-I/ancient compactness -> Pineau–Vicol one-slice weighted rigidity -> regularity`

is not closed by the cited source statements.

The exact missing interfaces are:

1. **velocity carrier:** finite `I` is not source-bound to Pineau–Vicol's pointwise Type-I bound;
2. **pressure carrier:** `D` is not source-bound to the required annular `L∞` pressure bound;
3. **dynamical carrier:** local compactness / finite `I` is not source-bound to one-time small `∂_s U`.

The third item is the route-refining coordinate left by the previous signed/no-recrossing failure: a successful successor must manufacture a **self-similar-time speed/recurrence defect**, rather than merely another absolute local-energy budget.

## Outcome

`DIRECT_GLUE_UNLICENSED_SOURCE_INTERFACE`.

Local mathematical failure: `NONE` (no positive estimate was attempted after Gate C failed closed).

Local-to-global/gluing failure: `YES`.

Residual: `FINITE_I_TO_ONE_TIME_SELF_SIMILAR_SPEED_CARRIER_OPEN`, with subordinate carrier obligations `POINTWISE_TYPE_I_UPGRADE_OPEN` and `ANNULAR_PRESSURE_LINF_UPGRADE_OPEN`.

The root remains `OPEN_NO_SOLUTION_CERTIFICATE`.
