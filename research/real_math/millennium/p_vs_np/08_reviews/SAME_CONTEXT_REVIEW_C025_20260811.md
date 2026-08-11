# Same-context review — C025 joint binary-signature gate

**Atom:** `O9d12a2a1a`  
**Candidate:** `C025`  
**Receipt:** `sha256:fcbdcdcb6a182705253b1cd0779316814c9791ceef549fc3f848023023a476eb`  
**Review status:** `ROLE_SEPARATED_SAME_CONTEXT / NOT_INDEPENDENT_REVIEW`  
**Timestamp:** `2026-08-11T08:14:07Z`

## Review boundary

These are analytical roles in the same research context. They are not external experts and do not provide independent peer review. The review asks only whether the frozen candidate, executable receipt, proof draft, failure diagnosis, memory deltas, and claim scope agree.

## 1. Complexity-theory lens

**Finding:** The local statement is correctly isolated. On the diagonal complement of `G_NEQ`, being above `(u,v)` forces both diagonal singleton generators into the semi-filter. A complementary cut separating `u,v` therefore places two members of the semi-filter on disjoint sides, so it covers the semi-filter. A signature collision leaves the canonical semi-filter uncovered.

**Vote:** `ACCEPT_EXACT_LOCAL_REPRESENTATION`.

**Boundary:** The proof does not normalize arbitrary full-cover pairs on another graph and has no direct P-versus-NP implication.

## 2. Counterexample-first computational lens

**Finding:** The receipt is bound to the preregistration and executable hashes and is canonically self-hashing. The oracle:

- exhaustively finds the predicted minima for `N=2,3,4`;
- enumerates all `4,18,166` semi-filters for those universes and checks `5,73,273` ordered cut families, respectively;
- reports zero mismatches between the source preservation definition and signature injectivity;
- checks constructive and low-order cases at powers of two and immediately above them through `N=17`.

**Vote:** `PASS_REGRESSION_EVIDENCE`.

**Boundary:** Finite enumeration is regression evidence, not proof. The all-`N` statement relies on the displayed elementary proof.

## 3. Formal-methods lens

**Finding:** Object, quantifiers, normalization, and direction of implication are explicit. The collision direction has an explicit canonical semi-filter witness rather than relying on absence of separation alone. Candidate and evaluator chronology is preserved by preregistration commit `03a4cb9a0bce32374d79210d8b712670c11626a7` before the evaluated receipt.

**Vote:** `ACCEPT_PROOF_DRAFT_SCOPE`.

**Blocking remainder:** No theorem-prover artifact, dependency audit, isolated checker, or novelty certificate exists. Do not promote to a machine-proven or new-mathematics claim.

## 4. Barrier and hostile-route lens

**Finding:** The repair passes the old C024 failure benchmark: simultaneous integrality raises the normalized `G_NEQ` value from the fractional upper value `2` to `ceil(log2 N)`. But the same first-order state representation has only `2^k` cardinality states. A pigeonhole-only lower-bound argument on `M` traces is exhausted at `ceil(log2 M)`.

**Vote:** `REJECT_AS_SUPERLOG_PRIMARY_ROUTE_WITHIN_FROZEN_SCOPE`.

**Scope correction:** The pre-candidate next-step prose asked whether every polynomial-trace binary-signature certificate is universally logarithmically capped. C025 does **not** establish that overbroad statement. The frozen candidate correctly narrowed the falsifier to cardinality-only first-order state counting. Realizability-sensitive constraints and higher-order closure signatures remain open.

## 5. Failure-diagnosis lens

**Observed result:** exact local calibration success coexists with a logarithmic first-order capacity ceiling.

**Competing diagnoses retained:** failure to restore joint correlation; target-specific specialness of `G_NEQ`; too-low-order witness state; or stronger realizability constraints not represented by raw cardinality.

**Bounded diagnosis:** joint correlation is restored on the registered benchmark, so that diagnosis is rejected locally. The state-count ceiling supports retiring only cardinality-only first-order capacity as the super-log route. It does not diagnose higher-order successors.

**Vote:** `SUPPORTED_BOUNDED_DIAGNOSIS`.

## 6. Research-memory and metacognition lens

**Success retained:** `T-PNP-JOINT-SIGNATURE-CALIBRATION` records the exact preconditions, guaranteed effects, non-guarantees, known failure, and validation obligations for reusing the calibration.

**Failure retained:** `F-C025-FIRST-ORDER-CAPACITY-CEILING` keeps the exact context, candidate, observed result, competing diagnoses, bounded selected diagnosis, scope, evidence, lattice relations, and next discriminator.

**Method lesson candidate:** after repairing a parent representation failure, run both the old-failure regression and a separate capacity/expressivity audit before expensive target search.

**Transport limit:** C023-C025 are one P-vs-NP lineage. This is not independent cross-problem recurrence and cannot authorize a RAKL framework delta. The proposal needs a frozen meta-evaluator, planted fail world, structural cannot-check world, and fresh assurance outside this lineage.

**Vote:** `RETAIN_PROPOSAL_ONLY_METHOD_LESSON`.

## Blocking-concern table

| Concern | Disposition |
|---|---|
| Candidate proposed only after strict context/memory/trace gate | Resolved and commit-bound |
| Evaluator thresholds frozen before output | Resolved in preregistration |
| Full-semi-filter coverage reduced to signatures only by assertion | Resolved by proof plus exact source-definition enumeration for `N<=4` |
| Finite checks presented as proof | Resolved by explicit authority boundary |
| Overbroad universal binary-signature no-go | Resolved by narrowing to cardinality-only first-order capacity |
| Higher-order closure state silently blacklisted | Resolved; recorded `NOT_TESTED` and reopened |
| Same-context review called independent | Resolved; explicitly prohibited |
| P-versus-NP implication inferred | Resolved; root status remains open |

## Verdict

`ACCEPT_SCOPED_CALIBRATION / RETAIN_SUCCESS_TOOL / RETAIN_SCOPED_FAILURE / REJECT_FIRST_ORDER_CARDINALITY_ROUTE / OPEN_HIGHER_ORDER_CHILD / ROOT_AUTHORITY_NONE`.

No independent review has occurred. No Millennium problem is claimed solved.
