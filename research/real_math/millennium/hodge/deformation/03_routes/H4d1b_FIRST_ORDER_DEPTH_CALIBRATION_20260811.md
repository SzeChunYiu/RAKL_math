# H4d1b formal-depth calibration

**Date:** 2026-08-11  
**Atom:** `H4d1b`  
**Candidate:** `H4d1b-C001-FIRST-ORDER-AS-FORMAL-CERTIFICATE`  
**Authority:** `SOURCE_BOUND_METHOD_CALIBRATION / FORMAL_COUNTEREXAMPLE / NO_HODGE_THEOREM / ROOT_AUTHORITY_NONE`

## Candidate under test

After H4d1a, the same-detector route can remain productive only if source-specific geometry proves direct first-order branch obstruction annihilation

`delta_1|_{T_{s0}T}=0`.

Under an exact witness-moduli tangent-obstruction interface, this says that each Hodge-branch tangent direction lifts with the chosen witness over dual numbers. The candidate tested here is deliberately stronger:

> **C001.** First-order branch liftability/tangent coverage by itself is sufficient to certify formal witness domination of the Hodge branch.

This is a method-authority claim, not a proposed theorem toward the Hodge conjecture. Its cheapest falsifier is to ask whether tangent surjectivity alone implies the small-extension lifting property required for formal smoothness.

## Formal hostile control

Let `k=C`, let

`T = Spec k[t]`

and let

`W = Spec k[t,u]/(u^2)`

with `q:W->T` induced by the inclusion `k[t] -> k[t,u]/(u^2)`.

At the origin `(t,u)=(0,0)`, the Zariski tangent space of `W` has coordinates `dt,du`, while the tangent space of `T` has coordinate `dt`. The differential

`dq : T_0 W -> T_0 T`

is therefore surjective.

So the first-order tangent test passes.

But `q` is not formally smooth. Consider the small extension

`A' = k[epsilon]/(epsilon^3) -> A = k[epsilon]/(epsilon^2)`.

Over the base point `t=0`, define an `A`-point of `W` by `u=epsilon`. This is valid because `epsilon^2=0` in `A`. Any lift to `A'` reducing to `u=epsilon` has the form

`u' = epsilon + a epsilon^2`.

Then

`(u')^2 = epsilon^2 != 0 mod epsilon^3`,

so the relation `u^2=0` cannot be satisfied. The required lift does not exist.

Hence tangent surjectivity at the point does **not** imply formal smoothness or all-small-extension liftability.

This is exactly the logical distinction required by the Stacks Project infinitesimal lifting criterion: formal smoothness is a lifting property for infinitesimal thickenings, and over a locally Noetherian finite-type base smoothness can be tested over all small extensions of Artinian local rings. It is not defined by one dual-number lift.

## Hodge-theoretic positive control

The correction does not make tangent calculations useless. In special variational-Hodge settings they combine with extra geometric hypotheses.

Kloosterman proves the variational Hodge conjecture for complete-intersection cycles on hypersurfaces. In the intersecting-linear-space comparison he explicitly uses that the geometric locus `NL([Pi_1],[Pi_2])` is smooth and contained in the Hodge locus; in that source-controlled setting equality of tangent spaces is sufficient for local equality of the loci. The extra smoothness/incidence structure is load-bearing.

Therefore the safe transfer is:

`first-order tangent agreement + independently proved smoothness/incidence hypotheses`

may close a special local comparison,

not

`first-order tangent agreement alone => formal witness domination`.

## Hodge-theoretic hostile control

The same Kloosterman Hodge-locus paper records classical nonreduced behavior. For `k=1`, `d>=5` and rational `lambda` outside `{0,1}`, the Hodge locus associated with `[Pi_1]+lambda[Pi_2]` is nonreduced, while its reduction equals the natural pair locus locally. The paper also records special higher-dimensional points where the combination Hodge locus is singular although the pair locus is smooth.

These examples are used only as a formal-depth warning: reduced support can erase genuine Hodge-scheme structure. They are **not** claimed to exhibit the stronger same-point pattern “tangent equality plus formal failure”; in the `k=1` nonreduced case the source detects excess tangent dimension already.

Thus the Hodge calibration and the elementary formal counterexample agree on the same methodological boundary: the target object for propagation must retain scheme/formal structure until reducedness/smoothness is separately proved.

## Expert-cell resolution

- **Hodge/VHS:** first-order Hodge compatibility remains base-side and must not erase Hodge-scheme thickness. `ACCEPT`.
- **Cycle/witness geometry:** `delta_1|T=0` remains a legitimate first-order checkpoint. `ACCEPT WITH SCOPE`.
- **Formal deformation:** C001 is refuted by the explicit small-extension counterexample. `REJECT C001`.
- **Adversarial Hodge-locus:** nonreduced Noether-Lefschetz loci validate scheme-depth as a live coordinate but do not overclaim same-point tangent equality. `ACCEPT`.
- **Method transfer:** retire linearized reachability as an all-order certificate; retain it only as a first-stage filter. `ACCEPT`.
- **Novelty/assurance:** the mathematical ingredients are established/elementary; authority is route-pruning, not new mathematics. `ACCEPT SCOPED RESULT`.

These are same-context roles, not independent reviewers.

## Verdict

**`FIRST_ORDER_CHECKPOINT_NOT_FORMAL_CERTIFICATE`.**

The candidate

`first-order branch liftability alone => formal witness domination`

is refuted in the general deformation-theoretic method class. Consequently, any future source-specific proof of

`delta_1|T=0`

may receive only **first-order/dual-number lifting authority** unless additional hypotheses independently establish the higher-order lifting contract.

This does not refute the possibility that a special Hodge family has enough smoothness, incidence geometry, semiregularity, derived obstruction control or another mechanism to upgrade first order to all orders. Such extra structure must be registered explicitly.

## Residual opened: H4d1c

The next propagation atom is scheme/formal rather than tangent-linear:

`H4d1c — all-order witness-incidence dominance over a Hodge branch`.

For a source-controlled witness/deformation object `q:W->T` through `(w0,s0)`, seek the weakest checkable condition that guarantees compatible witness lifts across every relevant small Artin extension. Candidate formulations include:

1. formal smoothness of the witness projection over the registered Hodge branch;
2. surjectivity of the chosen witness deformation functor over the branch on all Artin local test rings;
3. a completed-local-ring or obstruction-theory criterion that proves the same lifting property;
4. a source-specific theorem that proves the Hodge branch reduced/smooth and supplies enough incidence geometry to replace the abstract all-order test.

The H4d1c packet must keep separate:

`formal lifting != algebraization != global/monodromy continuation != root initial algebraicity`.

Before any H4d1c criterion is proposed, freeze a new context, current dual-memory review, expert cell and trace. The first hostile test should be a planted nilpotent/higher-order obstruction that passes the H4d1b tangent test.
