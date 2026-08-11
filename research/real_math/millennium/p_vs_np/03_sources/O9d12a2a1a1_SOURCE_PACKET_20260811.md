# O9d12a2a1a1 source packet — noncanonical closure / fixed-point re-representation

**Atom:** `O9d12a2a1a1`  
**Authority:** source-bound pre-candidate context only; no theorem candidate, novelty claim, or root authority.

## Why this source refresh exists

C025 repaired C024's lost simultaneous consistency on the canonical `G_NEQ` calibration, but the surviving state was still only original-generator separation. C009 already caps that canonical representation at logarithmic scale. The child therefore needs a representation that can contain **arbitrary noncanonical subsets produced recursively by several fusion choices** before another invariant is proposed.

## Primary target source

### Cavalar–Oliveira (2025)

Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ACM Transactions on Computation Theory 17(2), 2025; arXiv:2503.14117; DOI 10.1145/3718746.

Source-bound facts used here:

- Section 3.1, Definition 18: a semi-filter over `U` is nonempty, upward closed, and excludes `empty`.
- Definition 19: being above a target witness forces the corresponding generator traces `B intersect U` into the semi-filter.
- Definition 20: preservation of `(E,H)` is exactly the conditional closure law `E,H in F => E intersect H in F`.
- Definition 21: cover complexity is the minimum number of pairs for which no semi-filter above any target witness preserves the entire family.
- Section 2.5 defines cyclic discrete complexity as monotone fixed-point evaluation.
- The source's Fusion Problem `Pi_R` is an explicit binary-rule closure process: `(a,b,c)` fires when `a,b` are present and adds `c`; the paper realizes a fixed rule system with a cyclic monotone circuit containing one fan-in-two AND gate per rule.
- The paper's exact characterization of cover complexity via cyclic intersection complexity makes fixed-point language source-internal, not an imported metaphor.

**Research use:** these definitions motivate an exact least-closure interface over subset propositions. They do **not** by themselves supply a super-logarithmic lower bound or a useful quotient of the closure state.

## Solved analogue: Horn implication propagation

William F. Dowling and Jean H. Gallier, *Linear-time algorithms for testing the satisfiability of propositional Horn formulae*, Journal of Logic Programming 1(3):267–284, 1984, DOI 10.1016/0743-1066(84)90014-1.

The paper formulates propositional Horn satisfiability as a monotone data-flow/pebbling-style propagation problem and gives linear-time algorithms in the size of an **explicitly listed** Horn formula.

**Transfer retained:** least-fixed-point / forward-propagation semantics for facts and binary antecedent rules.

**Transfer blocked:** our proposition universe contains one possible variable per subset of `U`, and upward implications are implicit and exponentially numerous. No Horn-SAT runtime theorem is imported as an efficient graph-cover algorithm. A later 1990 note corrected one top-down algorithmic variant; this research uses only the fixed-point semantic analogy, not that implementation.

## Near analogue: stronger global consistency

Rahul Jain and Hartmut Klauck, *The Partition Bound for Classical Communication Complexity and Query Complexity*, CCC 2010; arXiv:0910.4266.

Their partition bound is an LP lower bound that can dominate simpler rectangle/corruption and discrepancy-style bounds in randomized communication complexity.

**Transfer retained:** global consistency can carry information missed by local relaxations.

**Transfer blocked:** randomized communication complexity is a different model; no partition-bound inequality is transferred to deterministic cover complexity.

## Adversarial hierarchy warning

Eden Chlamtac, Zachary Friggstad, and Konstantinos Georgiou, *Understanding Set Cover: Sub-exponential Time Approximations and Lift-and-Project Methods*, arXiv:1204.5489 (2012).

Their set-cover analysis shows that strong generic lift-and-project consistency does not automatically eliminate logarithmic integrality gaps.

**Research use:** do not respond to C024/C025 by mechanically increasing hierarchy order. Any higher-order coordinate must be witnessed by the semi-filter closure law and survive target-domain falsifiers.

## Exact proposed representation obligation

For a target witness `a`, define the seed family provisionally as

`S_a = {U} union {B intersect U : B in generators and a in B}`.

For a selected pair family `Lambda`, consider the **least** family of subsets of `U` containing `S_a` and closed under:

1. upward closure: `S -> T` whenever `S subseteq T subseteq U`;
2. selected fusion rules: `E,H -> E intersect H` for `(E,H) in Lambda`.

The first post-gate obligation is to prove or refute:

> a semi-filter above `a` preserving `Lambda` exists **iff** this least closure does not contain `empty`.

If exact, cover complexity can be re-read as the minimum number of selected binary fusion rules that force `empty` into every target-witness closure.

This is deliberately a **representation/calibration candidate**, not a claimed lower bound. The next hostile controls are C008, canonical `G_NEQ`, and C010 block repetition. C021 remains the explicit-target ceiling.

## Novelty boundary

No novelty claim is made for Horn logic, closure operators, fixed-point propagation, cyclic fusion, or the elementary equivalence obligation. The research value being tested is whether this exact state representation exposes a **noncanonical, recursively generated coordinate** that survives the already-recorded P-vs-NP failure families.
