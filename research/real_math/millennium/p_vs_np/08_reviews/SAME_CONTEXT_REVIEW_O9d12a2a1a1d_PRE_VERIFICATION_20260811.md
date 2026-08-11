# Same-context expert cell — O9d12a2a1a1d pre-verification

Authority: `SAME_CONTEXT_INTERNAL_REVIEW / NO_INDEPENDENT_REVIEW_CREDIT`  
Framework: `SzeChunYiu/RAKL@9027cc6beab7e935d714bbdf8e902b89b50caaa8`

The cell reviewed the frozen source/context/memory packet before executing the normal-form verification. These are role-separated passes over the same evidence, not independent peer review.

- **Fusion/cyclic-complexity specialist.** The exact object is the Section 2.5 least-fixed-point syntactic sequence, and the counted resource is intersection gates only. Recommendation: reason pointwise or via the OR-only dependency graph; do not replace least-fixed-point semantics by an acyclic circuit model.
- **Order/semilattice specialist.** In an OR-only subsystem with external sources fixed, the least fixed point at a node should equal the union of all external sources that can reach it through OR-only paths. Recommendation: prove this reachability statement first, then substitute it into counted intersection inputs.
- **Adversarial falsification specialist.** Highest-risk cases are OR SCCs that both receive and return a counted-intersection output, and two counted gates mutually coupled through OR paths. Predeclare these as hostile worlds; one mismatching finite example refutes the representation claim.
- **Complexity-transfer specialist.** Even if exact, the normal form gives no nontrivial lower bound by itself. It only narrows admissible lower-bound coordinates to the `k` counted meet nodes plus their free-union reachability environment.
- **Formal/verifier-trust specialist.** The candidate was conceived before the v3 pre-action receipt is materialized. Therefore discovery chronology is retrospective; only the upcoming verification action can be prospectively bound. No proof-assistant or independent checker is available in this cycle.
- **Novelty/research-value specialist.** A join-elimination normal form is plausibly standard as monotone fixed-point graph simplification. Do not claim literature novelty. If it survives, classify only as `representation` in shadow metadata.
- **Gluing specialist.** Keep local and root residuals separate. Local success closes only OR-node elimination. The root-facing residual remains a quotient-respecting `Phi`, a universal `Phi<=f(k)` theorem, an explicit super-log target, and the registered circuit/root bridges.

**Cell decision:** execute the bounded hostile-world verification and a direct proof of OR-reachability elimination. Do not open scalar invariant search in this cycle.
