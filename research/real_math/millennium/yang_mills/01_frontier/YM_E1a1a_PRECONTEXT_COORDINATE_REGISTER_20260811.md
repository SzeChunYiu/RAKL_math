# YM-E1a1a — pre-context coordinate register

**Authority:** `PRE_CONTEXT / NO_CANDIDATE / NO_THEOREM / ROOT_AUTHORITY_NONE`.

This register is a planning artifact, not a `MathContextFiber`. It exists so the next strict packet does not collapse several different failure surfaces into one vague “operator mixing” claim.

## Parent dependency

`YM-E1a1a` is the provisional child opened by active PR #32 after exact local calibration `YM-E1a1-C001`. Until PR #32 passes exact-head CI and is accepted, the child lineage is provisional. If the parent changes, this register must be reviewed before reuse.

## Atomic failure surfaces

| ID | Coordinate | Success shape for one weak block | Cheapest hostile falsifier | Why separate |
|---|---|---|---|---|
| M1 | mark vocabulary / geometry | generated marks lie in an explicitly graded loop/polymer/spin-network space | exhibit a generated contour/representation/multi-loop structure outside the registered grade | exact algebraic closure can fail even when norms stay finite |
| M2 | localization / polymer support | generated mark decomposes into localized polymers with explicit decay | construct a long-range connected marked term whose coefficient lacks the required support decay | locality is required for the Balaban induction, not merely formal expressibility |
| M3 | reflection buffer | support stays inside a quantified positive-half-space buffer after blocking | place an insertion at the minimal allowed distance and show one block crosses the reflection plane | fixed-cutoff reflection positivity is not invariant under arbitrary support enlargement |
| M4 | weak-coupling scaling | coefficients/norms expose acceptable powers of the running `g_k` | identify a generated factor with an inverse power or logarithmic loss that grows along the UV trajectory | finite one-step constants can still destroy asymptotic freedom bookkeeping |
| M5 | block-factor scaling | one-step loss has controlled `L` dependence compatible with iteration | show unavoidable growth faster than the irrelevant-dimensional gain | a bound independent of UV depth may still fail when `L` is iterated |
| M6 | mark degree | `r` source derivatives map to an explicit degree hierarchy with controlled combinatorics | show factorial/combinatorial growth not absorbed by the proposed weight | higher Schwinger functions require a hierarchy, not only first derivatives |
| M7 | large-field compatibility | marked data have a typed representation through the large-field/R operation | exhibit a large-field region where the mark is simply discarded or unbounded | small-field marked closure alone cannot yield full-measure observable control |
| M8 | non-triviality / separation | closure remains logically separate from whether limiting observables separate states | construct a closed but collapsing/trivial marked sector | existence of a stable algebra does not prove non-trivial continuum physics |

## Candidate norm coordinates to compare later

No norm is selected yet. A strict context should compare at least these families:

- exponential polymer/support weight `exp(mu |X|)` or an exact Balaban-compatible localization weight;
- contour/graph complexity weight depending on edge count, connected components and intersections;
- representation complexity weight tied to an explicit character/spin-network basis;
- source-degree factorial/exponential weights for repeated derivatives;
- reflection-distance penalty or hard buffer constraint;
- coupling-dependent weight chosen so irrelevant directions gain enough powers of the running weak coupling.

A proposed norm is acceptable only if its source assumptions match the actual one-step RG representation and if its one-step multiplier can be tested for multiscale summability. A norm invented merely to absorb the first counterexample is not evidence of closure.

## Role-separated delegation for the next strict packet

- **Balaban RG lead:** bind the exact block/background-field/localization variables and identify which inductive norm is inherited from the unmarked analysis.
- **Constructive QFT/OS lead:** define the positive-half-space source class and exact reflection buffer.
- **Gauge representation lead:** choose a gauge-invariant marked basis rich enough to express generated structures without silently fixing a gauge-dependent observable.
- **Multiscale analyst:** derive the required summability condition on one-step multipliers along the running coupling.
- **Adversarial lead:** construct M1–M7 hostile worlds before any positive closure claim.
- **Formal-methods lead:** insist on separate statements for exact decomposition, remainder bound, support bound and iteration criterion.
- **Novelty/frontier lead:** distinguish classical composite-operator/loop proliferation from any new nonperturbative estimate.

## Frozen next research decision

If parent PR #32 is accepted, the next cycle should freeze a fresh `MathContextFiber` around **M1–M7 as independent coordinates**, query both success and failure memory, and select the cheapest actual weak-coupling block calculation that can separate:

`FINITE/GRADED CONTROLLED CLOSURE` vs `LOCALIZATION LEAKAGE` vs `REFLECTION LEAKAGE` vs `UV-SCALING LOSS` vs `LARGE-FIELD INCOMPATIBILITY`.

No candidate may be generated from this register alone.
