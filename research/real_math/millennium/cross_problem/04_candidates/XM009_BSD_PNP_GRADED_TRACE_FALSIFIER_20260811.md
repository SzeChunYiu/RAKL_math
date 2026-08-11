# XM009 — BSD → P-vs-NP graded-trace transfer falsifier

**Authority:** proposal/shadow cross-problem research control only. This is not a theorem about BSD, not a P-vs-NP lower bound, not a reusable-tool promotion, and not root authority.

## Frozen transfer

- **Source atom:** `BSD-S001c1a-COMPLEX-UPPER-BOUND` (open RAKL_math PR #44; pending/search-priority evidence only).
- **Target atom:** `O9d12a2a1a1e` (successor proposed by open RAKL_math PR #128 after the zero-cost shattering audit).
- **Common abstraction:** an absolute/cumulative scalar can be saturated or inflated by degree-zero nuisance/free structure. A quotient, filtration, or associated-graded representation is useful only if a root-relevant positive-degree layer remains nondegenerate.
- **Enabling assumptions:** the P-vs-NP construction families are filtered monotonically by counted intersections; zero intersections permit arbitrary free unions; the candidate observable depends only on traces on one fixed row.
- **Disanalogies:** BSD augmentation ideals have algebraic graded pieces and multiplication; P-vs-NP set-construction families need not. Extra augmentation zeros can coexist with informative leading graded data, while a fixed-row trace filtration can already be complete at degree zero.
- **Predicted principle:** before adopting a quotient/graded invariant to remove nuisance structure, check both nuisance invariance and positive-degree target sensitivity.
- **Cheapest falsifier:** compute the degree-zero fixed-row trace family. If it is already the full power set, monotonicity makes every cumulative fixed-row trace layer identical.
- **DifferenceWitness:** the source representation has potentially informative higher augmentation layers; the target fixed-row trace representation can have no nontrivial higher layer at all.

## Exact target-side calculation

Fix `N >= 2`. In the graph discrete space `G_{N,N}`, write

- `R_i = {(i,j): 1 <= j <= N}` for rows,
- `C_j = {(i,j): 1 <= i <= N}` for columns,
- `A = R_1`.

Let `F_t` denote all sets constructible using at most `t` counted pairwise intersections and arbitrary free unions of the generators. Thus `F_0` is the free-union closure and `F_0 ⊆ F_t`. Define the cumulative fixed-row trace family

`T_t(A) = {X ∩ A : X ∈ F_t}`.

For any `S ⊆ A`, let `J_S = {j : (1,j) ∈ S}` and set

`X_S = ⋃_{j∈J_S} C_j`.

This uses no counted intersection, so `X_S ∈ F_0`. Moreover

`X_S ∩ R_1 = {(1,j): j∈J_S} = S`.

Hence every subset of `A` occurs already at degree zero:

`T_0(A) = P(A)`.

Because `F_0 ⊆ F_t`, we have `T_0(A) ⊆ T_t(A)`. But every trace is a subset of `A`, so `T_t(A) ⊆ P(A)`. Therefore

**`T_t(A) = P(A)` for every `t >= 0`.**

Consequently, for every `t`,

- `log_2 |T_t(A)| = N`,
- `VCdim(T_t(A)) = N`,
- `log_2|T_t(A)| - log_2|T_0(A)| = 0`, and
- `VCdim(T_t(A)) - VCdim(T_0(A)) = 0`.

More generally, any cumulative coordinate that is a function only of the complete set-valued family `T_t(A)` is constant along this filtration. Subtracting or quotienting the free baseline does not rescue this particular fixed-row observation: its positive-degree associated information is identically degenerate.

## What the falsifier does and does not establish

The transfer is **falsified in its naive target representation**. The BSD intuition “pass from a polluted absolute order to a leading graded object” does not automatically produce a useful P-vs-NP fixed-row trace potential. The decisive disanalogy is not terminology but nondegeneracy: the target trace filtration is already saturated at degree zero.

This does **not** rule out incremental or conditional potentials in general. It leaves open observables that change the observation locus or preserve coupling information, including joint traces across several rows, target-relative incidence/correlation data, noncumulative conditional signatures, or global/shared-rule coordinates. Any successor must still prove a legal per-intersection marginal law and an explicit super-logarithmic hard-instance value.

The local set-theoretic calculation is closed. Global P-vs-NP gluing is not attempted and remains open.

## Primary-source provenance

1. **Akshay Cavalar and Igor Carboni Oliveira**, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033 (18 March 2025). The report defines the `N x N` graph discrete space using row/column generators and the intersection-count model used here. The source is used only to bind the target operation semantics; the power-set trace calculation above is elementary and reproduced in full.
2. **Kazuto Ota**, *Kato's Euler system and the Mazur–Tate refined conjecture of BSD type*, arXiv:1509.00682. The paper defines the augmentation ideal, records extra-zero phenomena for Mazur–Tate elements, and places the leading coefficient in an augmentation quotient. Those facts calibrate only the source-side representation motif; no arithmetic statement is transferred into the P-vs-NP calculation.

## Expert-cell dispositions

- **Complexity theory:** accepts the zero-cost trace proof and the narrow flattening conclusion; rejects extrapolation to joint/global observables.
- **Arithmetic/Iwasawa:** accepts the augmentation-filtration motif as a source calibration; rejects any literal transfer of BSD algebra.
- **Structural transfer:** marks the DifferenceWitness decisive and classifies the transfer as a useful negative transfer.
- **Adversarial falsification:** confirms that monotonicity plus `T_0(A)=P(A)` is sufficient; no enumeration or asymptotic assumption is needed.
- **Formal assurance:** gives no protected/gate credit to proposal artifacts and no independent-review credit to the expert cell.
- **Metrology:** counts no retained semantic novelty absent a protected retention gate; route-pruning observations are recorded separately.
- **Source provenance:** primary sources support only the scoped operation/representation claims stated above.

## Outcome

`PARTIAL_SUCCESS_ROUTE_PRUNING / NEGATIVE_TRANSFER_FALSIFIED`

Residual after the cycle:

`FIXED_ROW_CUMULATIVE_TRACE_COORDINATE_FLATTENED + JOINT_OR_GLOBAL_TARGET_SENSITIVE_COORDINATE_OPEN + LEGAL_ONE_INTERSECTION_MARGINAL_BOUND_OPEN + EXPLICIT_HARD_GRAPH_SUPERLOG_VALUE_OPEN`.
