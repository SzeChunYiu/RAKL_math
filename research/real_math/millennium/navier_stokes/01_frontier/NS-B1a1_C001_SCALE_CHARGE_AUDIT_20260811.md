# NS-B1a1-C001 — scale-neutrality audit of the standard local-energy ledger

**Atom:** `NS-B1a1`  
**Authority:** `ROUTE_PRUNING_CALIBRATION / PROPOSAL_SHADOW / NO_NEW_NAVIER_STOKES_THEOREM / ROOT_AUTHORITY_NONE`  
**Pre-candidate context:** `sha256:2dd3659dd73036559e41fddd35b599fc1945933730d99ad2dc60d98ba28b67ce`  
**Pre-candidate memory:** `sha256:5331f53e7f396aa43912f76867cde26b0f71256a06005b8ae9229a2ee2cf8a74`  
**Pre-candidate final event:** `sha256:e8a3bd92bc35ff207610dc53ab146e3e9f9961c0cdc3c399b7423d009349b9d4`

## Registered hostile question

Assume `(v,q)` is in the registered mild bounded ancient Type-I class and on `Q(2R)` each dimensionless Albritton–Barker quantity satisfies `A(2R), C(2R), D(2R), E(2R) <= M`. Does the *standard* local-energy inequality with a cutoff from `Q(2R)` to `Q(R)` itself generate a scale-decaying, summable, or monotone charge that could make infinitely many dyadic descendants impossible?

The candidate is falsified if the source-valid estimate alone produces a positive power of `R` in the **dimensionless** descendant charge, a nonzero telescoping defect, a no-recrossing statement, or a genuinely disjoint nonsummable expenditure.

## Scaling bookkeeping

Use a standard nonnegative cutoff `phi_R` supported in `Q(2R)`, equal to one on `Q(R)`, with `|grad phi_R| <= c_phi R^-1` and `|partial_t phi_R| + |Delta phi_R| <= c_phi R^-2`.

The definitions give, up to the exact factor from using radius `2R`, `sup_t integral_{B(2R)} |v|^2 <= 2 M R`, `integral_{Q(2R)} |v|^3 <= 4 M R^2`, `integral_{Q(2R)} |q-[q]_{B(2R)}(t)|^(3/2) <= 4 M R^2`, and `integral_{Q(2R)} |grad v|^2 <= 2 M R`. The time length of `Q(2R)` is `4R^2`, hence `integral_{Q(2R)} |v|^2 <= 8 M R^3`.

Every standard right-hand contribution therefore has physical size `R` times a bounded dimensionless expression.

### Linear cutoff term
`integral |v|^2 (|partial_t phi_R|+|Delta phi_R|) <= 8 c_phi M R`.

### Convective cutoff term
`integral |v|^3 |grad phi_R| <= 4 c_phi M R`.

### Pressure-work cutoff term
A time-dependent spatial pressure mean may be subtracted because `div v=0` and the cutoff is spatially compact. Hölder gives

`R^-1 integral |q-[q]| |v| <= R^-1 (integral |q-[q]|^(3/2))^(2/3) (integral |v|^3)^(1/3) <= 4 M R`

up to the cutoff constant. In normalized variables the structural form is proportional to `D(2R)^(2/3) C(2R)^(1/3)`, not a positive power of `R`.

Thus the standard local-energy estimate has the scale-correct form

`A(R) + E(R) <= C_phi [ A(2R) + C(2R) + D(2R)^(2/3) C(2R)^(1/3) ]`

up to conventional constants and harmless variants of the local-energy functional. Under `I<=M`, the right side is `O_M(1)`.

## Result of the hostile check

The preregistered scale-decay prediction **does not appear**. Standard finite-`I` local-energy bookkeeping is scale-neutral after dividing by the natural physical energy scale `R`.

This blocks only the naive inference `bounded local-energy ledger at each scale => summable/well-founded descendant charge`. It does **not** prove that actual Navier–Stokes flux lacks cancellation, sign, temporal coherence, telescoping, or another stronger structure.

## Why finite physical currency does not stop infinite descent

If radii are `R_j=2^-j R_0`, then even a positive physical cost comparable to `R_j` or `R_j^2` has finite total: `sum_j R_j = 2 R_0` and `sum_j R_j^2 = (4/3) R_0^2`. Therefore a bounded total physical energy/flux budget is compatible with infinitely many smaller scales unless each descendant spends a **non-summable normalized amount**, satisfies a no-recrossing rule, or belongs to disjoint regions/events carrying a fixed lower cost.

The same warning applies to epsilon-regularity thresholds. Failure of a dimensionless smallness criterion at every nested singular scale does not make the corresponding physical integrals disjoint, and the scale-weighted lower bounds can shrink geometrically.

## Structural near-miss: forward DSS

Forward discretely self-similar suitable weak Navier–Stokes solutions are known in source-bounded settings and satisfy the classical local-energy inequality. They are not backward Type-I ancient counterexamples and are not in the target class merely by analogy. They serve only as a hostile near-miss showing that `local-energy inequality + scale invariance` does not syntactically force a Lyapunov decrease or forbid scale repetition.

## Local-to-global / gluing diagnosis

This is a **gluing failure**, not a local mathematical failure. The source-valid finite-`I` bounds and local-energy inequality remain intact. What fails is the bridge assembling bounded scale-local ledgers into a root-useful terminal/summable charge. The broken assumption is that `O(1)` dimensionless control per scale can be treated as if it limits the number of descendants.

The surviving residual is to find information not present in the absolute standard ledger: a bounded-below dimensionless monotone defect with strict drop, a no-recrossing/persistence theorem, sign/coherence cancellation, genuinely disjoint positive expenditure, compactness/minimality plus rigidity, or another source-valid Liouville trigger.

A useful next child is therefore `NS-B1a2`: identify whether any source-valid dynamics-specific defect quantity changes monotonically under nested Type-I blow-up rescaling, or prove a no-recrossing statement for a carefully chosen critical threshold.

## Authority and novelty

The Clay root remains `OPEN_NO_SOLUTION_CERTIFICATE`; Type-I and Type-II exclusion remain open. This is a scoped inference/route-pruning calibration. For the solved *subproblem*, the defensible RAKL novelty class is `TRANSFER_NOVEL`, structural rank `0`, because the operation reuses `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` with a target-specific DifferenceWitness and introduces no new primitive research operator. No mathematical novelty claim is made for the local-energy estimate itself.