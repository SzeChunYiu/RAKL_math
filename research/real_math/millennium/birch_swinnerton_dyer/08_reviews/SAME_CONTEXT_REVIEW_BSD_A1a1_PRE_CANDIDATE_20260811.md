# Same-context expert review — BSD-A1a1 theta-order comparison

**Atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**Authority:** `SAME_CONTEXT_REVIEW_ONLY / PRE_CANDIDATE / NOT_INDEPENDENT`

This cell reviews the source-level implication graph exposed by `BSD-A1a`. It does not propose a theorem or claim BSD progress beyond a sharper obstruction.

## 1. Analytic / automorphic lead

**Background:** modular L-functions, Rankin–Selberg products, functional equations, central derivatives.

**Finding:** exact analytic rank two is a statement about the order of `L(E,s)` in the complex variable `s` at `s=1`. Castella–Hsieh Theorem 2.3 instead defines `Theta_{f/K}(T)` on the anticyclotomic character direction `T`, with specializations `T=zeta-1` tied to central Rankin–Selberg values. The source itself deduces only positive `T`-order from central vanishing.

**Strongest objection:** a notation-level identification `ord_s=2 => ord_T=2` conflates two deformation directions.

**Vote:** `ACCEPT_CHILD_ATOM`; search for an exact leading-term comparison, not another restatement of interpolation.

## 2. Iwasawa / p-adic L-function lead

**Background:** anticyclotomic Iwasawa theory, theta elements, p-adic L-functions, derived heights.

**Finding:** the factorization and explicit-reciprocity machinery downstream of `Theta_{f/K}` is strong: the triple-product p-adic L-function and localized big diagonal-cycle class both carry the theta factor under explicit hypotheses. But these identities consume the theta function; they do not make complex `s`-order determine `T`-order.

**Strongest objection:** an Iwasawa main conjecture may recover theta order through a Selmer characteristic ideal, but that can import arithmetic rank information independent of the bare complex-rank-two premise. Logical strength must be audited before reuse.

**Vote:** `ACCEPT_CHILD_ATOM`; distinguish a genuinely analytic comparison theorem from a Selmer-mediated conditional bridge.

## 3. Arithmetic-geometry lead

**Background:** Mordell–Weil groups, Selmer groups, Tate–Shafarevich groups, heights.

**Finding:** Castella–Hsieh Theorem B assumes `rank_Z E(Q)>0` in addition to `ord_T Theta=2` to force generalized-Kato nonvanishing. That hypothesis is downstream of the desired analytic-to-arithmetic bridge and must not be used to manufacture it.

**Strongest objection:** even a successful theta-order comparison would leave a separate localization/positive-rank residual before the generalized-Kato route becomes noncircular.

**Vote:** `ACCEPT_CHILD_ATOM`; keep `BSD-A1a2-LOCALIZATION-BRIDGE` separate and downstream.

## 4. Adversarial falsification lead

**Background:** counterexample-first proof auditing, representation mismatch, logical-strength tests.

**Cheapest calibration:** for a generic two-variable function, order along one direction need not equal order along another; e.g. `F(s,T)=(s-1)^2+T^4` has order two along the `s` axis at `T=0` but order four along the `T` axis at `s=1`. This is not an arithmetic counterexample. It falsifies only the inference form that equal base-point vanishing plus shared notation determines directional order.

**Target-specific falsifier:** inspect the exact interpolation theorem. At the trivial character it yields vanishing and, in the source's own argument, `ord_T Theta>0`; it does not state `ord_T Theta=2`.

**Vote:** `PASS_REPRESENTATION_MISMATCH_DIAGNOSIS`; reject interpolation-only candidate generation.

## 5. Formal-assurance lead

**Background:** statement binding, dependency DAGs, proof obligations, checker trust.

**Required future candidate contract:** specify `E`, admissible `p`, `K`, and auxiliary character data; state the exact complex premise, exact theta element, exact `T` coordinate, and the theorem that preserves the first nonzero coefficient across the `s -> T` representation change. Any use of Selmer dimension, positive rational rank, Sha finiteness, or a main conjecture must remain an explicit premise.

**Strongest objection:** a statement that merely proves `Theta(0)=0` or `ord_T Theta>0` is strictly weaker than the required child conclusion.

**Vote:** `PASS_PRE_CANDIDATE_ONLY`.

## 6. Novelty / research-value lead

**Background:** source equivalence, prior-art and theorem-strength auditing.

**Finding:** no new theorem is claimed. The research value is the decomposition of the earlier coarse `complex L'' -> kappa` bridge into two independently testable residuals: exact theta-order transfer and localization/positive-rank transfer. The inspected primary sources already contain the p-adic interpolation, factorization, reciprocity and derived-height machinery; the live question is the missing cross-direction exact-order comparison without root-strength arithmetic input.

**Vote:** `NO_NOVELTY_CLAIM`; proceed with source search for a noncircular `s`-to-`T` leading-term theorem.

## Cell decision

**Selected modes:** `REFLECTIVE_RESTRUCTURE + CONTRASTIVE_DISCRIMINATION + EFFECTUAL_PROBE`.

**Selected next action:** search primary literature for a theorem that identifies the exact anticyclotomic `T`-adic leading order or leading coefficient from complex analytic rank two under explicit admissibility hypotheses. Classify every candidate theorem as:

1. `ANALYTIC_INPUT_ONLY`;
2. `USES_LOCALIZATION_OR_POSITIVE_RANK`;
3. `USES_SELMER_DIMENSION`;
4. `USES_IWASAWA_MAIN_CONJECTURE`;
5. `USES_BSD_OR_EQUIVALENT_STRENGTH`.

Only class (1), or a rigorously weaker noncircular variant, may support the desired root bridge. No mathematical candidate is authorized merely by this review.
