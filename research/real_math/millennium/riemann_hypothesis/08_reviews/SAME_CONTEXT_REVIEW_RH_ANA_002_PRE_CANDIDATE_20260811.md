# SAME-CONTEXT REVIEW — RH-ANA-002 pre-candidate packet

**Atom:** `RH-ANA-002 — LI_NORM_IDENTITY_DEFECT`  
**Root:** Riemann Hypothesis  
**Review authority:** `SAME_CONTEXT_ROLE_SEPARATION_ONLY / NOT_INDEPENDENT_REVIEW`  
**Candidate state:** none  
**Root authority:** none

The cell reviewed the same frozen source/context packet from seven deliberately different technical roles. Votes concern **research-control adequacy**, not RH truth.

## 1. Analytic number theory / explicit-formula lead

**Background:** zeta/L-functions, explicit formulae, prime sums, zero-sum regularization, analytic continuation.

**Evidence inspected:** Li 1997; Bombieri–Lagarias 1999; Suzuki equations (1.3), (1.9), Proposition 2.1; the `RH-ANA-001` finite-prefix no-go.

**Strongest objection:** moving from zeros to the arithmetic formula can hide rather than remove the all-`n` obstruction. The binomial weights amplify cancellations, and a finite prime truncation has exactly the same logical weakness as a finite Li prefix unless a uniform remainder theorem is frozen first.

**Attempted falsifier:** ask whether any termwise-positive reading of the Bombieri–Lagarias/Suzuki arithmetic formula survives the explicit alternating/binomial structure. It does not: the source formula is not a manifest positive prime sum.

**Delegated next step:** in the faithfulness matrix, mark every truncation/tail operation and identify the first bound whose constant/range grows with `n`.

**Residual uncertainty:** a more global prime-side transform may reorganize the cancellation usefully, but no such theorem is yet registered.

**Vote:** `ACCEPT_PRE_CANDIDATE / BLOCK_TERM_SCRAPING_CANDIDATE`.

## 2. Li / Weil criterion specialist

**Background:** Li coefficients, Weil quadratic functional, equivalent positivity criteria, zero symmetries.

**Evidence inspected:** Li criterion, Bombieri–Lagarias Li/Weil identity, Lagarias generalized Li coefficients.

**Strongest objection:** `lambda_n=P_n` for all `n` is already an RH-equivalent statement. Calling `D_n=P_n-lambda_n` a “defect” can create an illusion of localization if one immediately asks to prove `D_n=0`.

**Attempted falsifier:** replace “prove RH” by “prove the norm identity for every n.” No reduction in logical strength occurs. The packet correctly classifies this as a forbidden root relabeling.

**Delegated next step:** require every proposed `D_n` subidentity to state exactly why it is strictly weaker or independently falsifiable before it can become a candidate.

**Residual uncertainty:** there may be a useful one-sided or averaged defect identity that is weaker than all-`n` equality; current sources do not establish one.

**Vote:** `ACCEPT_PRE_CANDIDATE / BLOCK_ROOT_RELABELING`.

## 3. Harmonic analysis / model-space lead

**Background:** Hardy/model spaces, de Branges spaces, Hilbert-space norm identities, Parseval-type arguments.

**Evidence inspected:** Suzuki Theorem 1.1 and Propositions 2.1–2.2; the paper's distinction between unconditional `L2` membership and RH-dependent model-space structure.

**Strongest objection:** positivity of an `L2` norm is mathematically trivial once `G_n` exists. The load-bearing theorem is faithfulness. Model-space orthogonality or basis expansions used under RH cannot be silently pulled into the unconditional side.

**Attempted falsifier:** isolate the weakest unconditional statement: `G_n|R` is bounded, real-analytic and in `L2`. This gives `P_n>=0` but no sign information about `lambda_n` without the identity.

**Delegated next step:** dependency-label the proof of the norm identity line by line and identify the first step that uses RH/model-space structure.

**Residual uncertainty:** Suzuki's unconditional Proposition 2.1 may permit an exact defect expression before the conditional model-space step, but this must be derived source-faithfully.

**Vote:** `ACCEPT_PRE_CANDIDATE / SELECT_IDENTITY_DEPENDENCY_AUDIT`.

## 4. Asymptotic complex-analysis lead

**Background:** entire functions, zero sums, asymptotic analysis, Li coefficient growth.

**Evidence inspected:** Lagarias `math/0404394`; Voros `math/0506326`.

**Strongest objection:** the growth-class route could be a more efficient all-index representation, but a sufficiently strong unconditional global bound may already encode almost all of RH. “Tempered” needs an exact quantitative definition and implication boundary.

**Attempted falsifier:** use only the RH-conditional `n(A log n+B)` asymptotic as the desired bound. This is circular and therefore rejected.

**Delegated next step:** after the norm-faithfulness audit, compare the strongest unconditional known Li growth estimates against the weakest bound that excludes the non-tempered off-line contribution.

**Residual uncertainty:** this may expose a genuinely smaller analytic target, but it is not yet established to be lower-cost than the norm defect.

**Vote:** `ACCEPT_PRE_CANDIDATE / HOLD_GROWTH_ROUTE_AS_ALTERNATIVE`.

## 5. Adversarial falsification / root-bridge lead

**Background:** counterexamples, surrogate-vs-target failures, finite-to-infinite and representation-faithfulness audits.

**Evidence inspected:** `F-RH-ANA-001-FINITE-LI-PREFIX`, `T-RH-LI-PREFIX-QUARTET-CALIBRATION`, `T-XM-ROOT-BRIDGE-STABILITY-AUDIT`, `F-XM001-POINTWISE-GAP-COLLAPSE`.

**Strongest objection:** the phrase “positive norm representation” is precisely the kind of surrogate-success narrative that can conceal the missing root bridge.

**DifferenceWitness:** XM001 concerned a dimensionless finite-cutoff gap whose physical normalization vanished. RH-ANA-002 concerns an exact analytic identity between `P_n` and `lambda_n`. The source counterexample does not transfer; only the audit protocol transfers.

**Cheapest target falsifier:** Suzuki already provides it at the logical level: `P_n` exists and is nonnegative unconditionally, while the all-`n` identity is stated as RH-equivalent. Therefore surrogate positivity alone has zero root authority.

**Delegated next step:** refuse any future positive surrogate unless its faithfulness map is frozen first and has a hostile failure world.

**Residual uncertainty:** a strictly weaker faithfulness lemma may exist.

**Vote:** `ACCEPT_PRE_CANDIDATE / SELECT_ROOT_BRIDGE_AUDIT_TOOL`.

## 6. Formal methods / assurance lead

**Background:** statement binding, artifact hashes, dependency audit, chronology, proof-authority boundaries.

**Evidence inspected:** current RAKL mathematical-research workflow, current schemas/runtime gate, RAKL_math repository contract, RH issue #3.

**Strongest objection:** a new `D_n` formula would be a mathematical candidate if it asserts a nontrivial identity not already source-proved. It must not appear before the strict packet passes.

**Attempted falsifier:** inspect this packet for a hidden theorem claim. `D_n` is defined only as bookkeeping, and the next action is a source dependency matrix; no sign, vanishing, recurrence, or new identity for `D_n` is asserted.

**Delegated next step:** run `audit_math_context_fiber`, `audit_research_memory_review`, `audit_pre_candidate_trace`, and `plan_math_research`; require exact-head application CI before using the packet to authorize candidate generation.

**Residual uncertainty:** repository CI execution is external to this role; queued/missing checks cannot be treated as green.

**Vote:** `ACCEPT_PRE_CANDIDATE / NO_CANDIDATE_AUTHORITY_YET`.

## 7. Novelty / frontier / research-policy lead

**Background:** current literature scan, novelty boundaries, route saturation, exploration/exploitation.

**Evidence inspected:** peer-reviewed/source-primary Li/Weil/model-space literature plus current 2026 arXiv/frontier scan.

**Strongest objection:** positivity and operator formulations of RH are heavily populated; another “RH iff positive object” equivalence is low-value unless it identifies a provably cheaper bridge. Recent proof claims and working papers must not be treated as resolved mathematics.

**Attempted falsifier:** search for a source already giving unconditional `lambda_n=P_n` or an unconditional positive arithmetic decomposition. Suzuki states the norm identity as necessary and sufficient for RH; the current primary sources inspected do not close the bridge.

**Delegated next step:** keep the mode `REFLECTIVE_RESTRUCTURE + CONTRASTIVE_DISCRIMINATION + EFFECTUAL_PROBE`; do not trigger unconstrained recombination yet.

**Residual uncertainty:** a recent source outside the inspected query boundary may contain a relevant partial identity; bounded novelty/frontier search must continue if a candidate later emerges.

**Vote:** `ACCEPT_PRE_CANDIDATE / RESEARCH_VALUE_IN_LOCALIZATION_NOT_NEW_EQUIVALENCE`.

## Cell synthesis

The seven roles agree on the following:

1. `RH-ANA-002` is a legitimate child because it adds a structural coordinate absent from the finite-prefix atom: **faithfulness of a positive surrogate to the exact Li target**.
2. The strongest source-bound fact is the separation in Suzuki between unconditional `G_n in L2` and the RH-equivalent all-`n` norm identity.
3. The cross-Millennium root-bridge stability tool transfers only as a diagnostic procedure, with an explicit DifferenceWitness.
4. No theorem/inequality/recurrence/defect formula should be invented yet.
5. The next action is the `LI_NORM_FAITHFULNESS_MATRIX`: label source steps `UNCONDITIONAL`, `RH_CONDITIONAL`, `RH_EQUIVALENT`, or `UNKNOWN`, then test whether the unconditional layer exposes any strictly weaker exact sub-obligation.
6. If the result is `NO_STRICTLY_WEAKER_BRIDGE_FOUND`, that is useful negative search information and should trigger representation rotation rather than another norm-positivity reformulation.

**Final cell vote:** `PASS_TO_MACHINE_PRE_CANDIDATE_GATE / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`.

This same-context expert cell is not independent mathematical review.
