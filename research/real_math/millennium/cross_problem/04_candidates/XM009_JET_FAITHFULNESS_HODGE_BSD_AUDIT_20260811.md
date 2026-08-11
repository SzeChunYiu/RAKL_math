# XM009 — jet-faithfulness before transporting exact vanishing order

**Application base:** `RAKL_math@812addd25a7f34d3c6272143e21d5d7db34539aa`  
**Current semantic framework inspected first:** `RAKL@3299072b410ac9136548dfd103e846fc7656c31e` (`method_version=3.0.0`)  
**Application execution pin at base:** `RAKL@787c7e00af2a5877ccb715bc807ec14f52974e9c`  
**Active fibre snapshot:** `sha256:e7a7470e3737aeb020ab7724fd127a4c0384ba75c070093eb08358ddbedbb004`  
**Authority:** `PROPOSAL_SHADOW / SEARCH_CONTROL_ONLY / ELEMENTARY_LOCAL_ALGEBRA_CALIBRATION / NO_MILLENNIUM_THEOREM / NO_ROOT_AUTHORITY / NO_FRAMEWORK_PROMOTION`

## Research question

The current BSD lane has normalized its missing local bridge to the exact cell

`NUMBER_FIELD + WEIGHT_TWO_ELLIPTIC_CURVE + COMPLEX_S_DERIVATIVE_ORDER_TWO + ROOT_FAITHFUL_ARITHMETIC_OUTPUT`.

Current primary-source neighbors include genuinely higher-order formulas, but in distinct coordinates/categories: function-field higher complex derivatives, higher-cycle/weight formulas, and second derivatives of p-adic/Hida-family L-functions. The question for this cycle is narrower than BSD:

> What exact local algebra must a comparison carry before a second derivative/order statement in one parameter can be used as evidence for exact order two in another parameter?

The source experience is Hodge `H4d1b`: first-order tangent lift can be valid while formal/higher-order lift fails. That failure changed routing from “another higher derivative formula” to “audit the truncation/coordinate map itself”.

## Same-context expert cell

These role-separated passes shared the same evidence and do **not** count as independent mathematical review.

1. **Hodge deformation lead** — audits first-order versus higher-Artin/formal depth and the scope of Nishinou/Kloosterman positive controls.
2. **BSD arithmetic-geometry lead** — keeps the target at exact complex `s`-order two and rejects p-adic/Hida or function-field derivative coordinates without a comparison theorem.
3. **Local algebra/analytic-germ lead** — proves the formal-power-series order calculation and identifies the exact coordinate-change condition.
4. **Adversarial transfer lead** — constructs coordinate changes and small perturbations that destroy the target order.
5. **Primary-source/provenance lead** — separates what the cited papers actually state from structural analogy.
6. **RAKL memory/routing lead** — checks prior cross-problem tools/failures and rejects saturated transfers.
7. **Metrology lead** — counts only retained semantic search-control structure and writes `CANNOT_MEASURE` for unfrozen denominators.
8. **Authority/verification lead** — separates elementary lemma verification, application CI, same-context review, and root authority.

Consensus: retain an exact *jet-faithfulness discriminator* as proposal/shadow search control; do not promote a reusable tool or BSD theorem.

## Source atom and source evidence

**Source atom:** Hodge `H4d1b`, especially the recorded failure `F-H4D1B-FIRST-ORDER-NOT-FORMAL`.

The application hostile control from PR #100 exhibits a morphism with a surjective first-order tangent map but a dual-number point that cannot lift one order further. This is a local warning about truncation depth, not a Hodge theorem.

Primary-source positive controls remain strictly scoped:

- Nishinou, arXiv:2009.01651, proves relative deformation under semiregularity exactly when the divisor class remains Hodge in his setting.
- Kloosterman, arXiv:2104.14845, proves the variational Hodge conjecture for complete-intersection cycles in the stated hypersurface setting.
- Hu–Sun–Yang–Zuo, arXiv:2606.05794, in a disanalogous non-abelian Noether–Lefschetz setting, use a sequence of higher-order obstruction classes and show that their vanishing forces lifting to arbitrary finite order.

These sources support only the methodological distinction between a first-order checkpoint and controlled higher-order lifting. They do not transfer Hodge geometry into BSD.

## Target atom

**Target atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`, current R4 subtarget `COMPLEX_S_DERIVATIVE_ORDER_TWO`.

Current BSD R4 already separates three meanings of “higher Gross–Zagier”. In particular:

- Ishikawa, arXiv:1409.8584, gives a second-derivative formula for a two-variable **p-adic/Hida-family** L-function.
- Castella–Hsieh, arXiv:1809.09066, relate the leading term of an anticyclotomic p-adic L-function to derived p-adic heights/regulators under their hypotheses.
- Castella, arXiv:2204.09608 and arXiv:2312.01481, gives rank-two generalized-Kato/Selmer results with stated arithmetic hypotheses.
- Fornea, arXiv:2603.28327, constructs plectic Heegner classes with p-adic/Galois-cohomological structure.
- Bieker, arXiv:2607.07531, is a current function-field higher-Gross–Zagier analogue and remains a DifferenceWitness control, not number-field elliptic-curve evidence.

The target remains the **complex** local parameter `z=s-1`; a second derivative in a different deformation parameter is not the requested coordinate.

## Transfer contract

### Common abstraction

Both source and target ask whether information at one truncation/coordinate can support a conclusion living at a stricter truncation/coordinate.

The proposed principle is:

`JET_FAITHFULNESS_BEFORE_ORDER_TRANSFER`

> Before transporting exact vanishing order `r` across a representation or parameter change, require an exact source-bound germ comparison that preserves the relevant `r`-jet filtration; derivative labels or small approximation alone are not enough.

### Enabling assumptions

A safe one-variable comparison has the form

`g(U) = u(U) f(phi(U))`

in a field-valued formal/analytic local ring, where:

1. `f(0)=0` and the target order is measured at the same distinguished point;
2. `u(0) != 0` is a unit;
3. `phi(0)=0`;
4. the coordinate map is exact and source-bound, not inferred from terminology;
5. for order preservation, `phi` has a nonzero linear coefficient, equivalently `ord_U phi = 1`;
6. the compared functions/objects are proved to satisfy the germ identity, not merely analogous interpolation statements.

### Elementary local-algebra lemma

Let

`f(T)=a_r T^r + O(T^(r+1))`, `a_r != 0`,

and

`phi(U)=b_m U^m + O(U^(m+1))`, `b_m != 0`.

Then

`ord_U(f(phi(U))) = r*m`.

The leading term is `a_r b_m^r U^(rm)` and cannot be cancelled by higher terms. Multiplication by a unit `u(U)` does not change order.

Therefore an exact local coordinate substitution preserves **all** vanishing orders iff `ord_U phi=1` (equivalently the linear coefficient is nonzero).

For the order-two target, if

`f(T)=a_1 T + a_2 T^2 + ...` and `phi(U)=b_1 U+b_2 U^2+...`,

then

`[U] f(phi(U)) = a_1 b_1`,
`[U^2] f(phi(U)) = a_1 b_2 + a_2 b_1^2`.

Thus exact order two requires the lower jet to vanish exactly (`a_1=0`), the coordinate map to be first-order invertible (`b_1 != 0`), and the second target coefficient to be nonzero. “Second derivative” by name does not establish any of these cross-coordinate identities.

### Cheapest falsifiers

1. **Small-perturbation falsifier.** `f(T)=T^2` but `g_e(T)=T^2+eT` has order `1` for every `e != 0`, even as `e -> 0`. Arbitrarily small coefficient error does not preserve exact order.
2. **Ramified-coordinate falsifier.** `f(T)=T^2`, `phi(U)=U^2`, so `f(phi(U))=U^4`. A genuine exact relation can still change order if the parameter map is ramified.
3. **Positive control.** `phi(U)=cU+O(U^2)` with `c != 0`, and multiplication by a unit, preserves order exactly.

These are local-algebra calibrations only; they do not say that any particular BSD source admits or fails such a comparison.

### DifferenceWitness

```text
Hodge source:
first-order tangent / dual-number lift
    versus
higher-Artin or formal witness lift.

BSD target:
higher derivative/order in a p-adic, Hida, plectic, or function-field coordinate
    versus
exact complex s-order at s=1.
```

Non-transferable coordinates include Hodge incidence geometry, obstruction complexes, complex `s`, p-adic weight/Hida variables, anticyclotomic augmentation parameters, Shtuka/Frobenius geometry, and Selmer/regulator objects. Only the truncation/coordinate-faithfulness audit transfers.

## Falsifier result against the current BSD source neighborhood

The bounded source neighborhood contains target-near higher-order objects, but no consulted primary source supplies, in the frozen target scope, an exact germ identity

`g(U)=unit * L(E,1+phi(U))`

with a source-bound `phi` having nonzero linear term and with `g`'s order/leading coefficient identified with a root-faithful arithmetic output.

Therefore the p-adic/Hida “second derivative” route remains **not admissible as a substitute for complex-s order two solely by derivative count**.

This does not prove that no comparison theorem exists. Coverage completeness is `CANNOT_MEASURE`. It sharpens the residual from a terminology mismatch to an explicit comparison obligation.

**Outcome:** `PARTIAL_SUCCESS_ROUTE_REFINEMENT / JET_COMPARISON_OBLIGATION_EXPOSED`.

**Failure class:** `REPRESENTATION + BRIDGE_GLUING` for the proposed cross-coordinate substitution. The elementary local-algebra lemma itself succeeds. No local BSD mathematical theorem failed.

## Episode -> diagnosis -> lesson/obstruction separation

### Episode

Hodge truncation-depth failure and BSD higher-derivative ontology were retrieved. The action tested whether an exact order-preservation criterion can be stated and falsified before another target-near source is accepted.

### Diagnosis

`REPRESENTATION / BRIDGE_GLUING`.

The current target-near literature spans genuinely distinct local parameters and mathematical categories. The bottleneck is not the phrase “higher derivative”; it is the missing exact germ/jet comparison to the complex `s` coordinate.

### Proposal lesson

`PL-XM009-JET-FAITHFULNESS-BEFORE-ORDER-TRANSFER`:

> Exact multiplicity/order is transported only through a proved order-faithful local comparison (unit factor plus unramified parameter map in the one-variable calibration); approximation, derivative count, or shared lineage is insufficient.

Authority: `PROPOSAL_SHADOW_ONLY`.

### Observed obstruction signature

`F-XM009-BSD-CROSS-COORDINATE-JET-COMPARISON-MISSING`.

Status: `OBSERVED_ONLY / SEARCH_CONTROL_SCOPE`. It is not a literature-wide nonexistence claim and not a BSD obstruction theorem.

### Positive motif

`M-XM009-TRUNCATION-DEPTH-FIRST`:

> When a target asks for an exact kth-order property, audit the kth-jet transport map before searching by semantic labels such as “higher”, “second derivative”, or “deformation”.

## Prior experience that changed routing

Selected:

- `F-H4D1B-FIRST-ORDER-NOT-FORMAL`: changed the active question from source-name matching to truncation-depth faithfulness.
- `D-BSD-A1A1-HIGHER-GZ-ONTOLOGY-MISMATCH-R4`: supplied the target's already-normalized coordinate distinction.
- `T-XM-ROOT-BRIDGE-STABILITY-AUDIT`: retained only as a scoped audit operation—make the root-critical coordinate explicit and test its preservation.
- XM008 interface-preservation pattern: used as a search-control analogy, not theorem authority.

Retrieved but rejected/deferred:

- XM006 pointwise-to-diagonal uniformity: useful warning but its quantifier/uniformity defect is not the present coordinate-jet defect.
- XM007 state-projection congruence: already exercised; no new projection collision is needed here.
- P-vs-NP free-union quotient warnings: invariance/quotient failure is structurally different.
- Navier–Stokes local/global tail failures: gluing discipline is relevant, but they do not identify the parameter-map obligation.
- Yang–Mills hidden-state/source-family warning -> RH: rejected earlier as duplicative of RH's own universal-exception falsifier.

Missed relevant experience in a bound universe: `CANNOT_MEASURE` because no exhaustive relevance-labelled cross-Millennium retrieval universe was frozen for this cycle.

## Seven-axis saturation audit

```text
KNOWLEDGE          OPEN
OPERATOR           FLAT
EXPERIENCE_PATTERN REOPENED
OBSTRUCTION        FLAT
RELATION           REOPENED
PATH               REOPENED
META_METHOD        FLAT
```

Conservative retained semantic search-control vector:

```text
KNOWLEDGE          0
OPERATOR           0
EXPERIENCE_PATTERN 1
OBSTRUCTION        0
RELATION           1
PATH               1
META_METHOD        0
```

No mathematical novelty is claimed. If the scoped abstract subproblem is classified at all, the defensible RAKL novelty class is `representation/transfer`, structural rank `0`.

## Local versus global/gluing boundary

The local algebra criterion is closed in the stated one-variable formal-power-series calibration. The BSD target is **not** locally solved: no exact complex-s-to-arithmetic germ comparison has been supplied. Even if such a local comparison is found, the lane must separately glue the arithmetic carrier to Mordell–Weil rank/regulator and Sha/Tamagawa/torsion contributions under the exact root contract.

No local success is counted as global BSD progress.

## Framework observer note

Current RAKL main contains first-class `method_telemetry`, `episode_admission`, and `artifact_contract_coverage` surfaces that directly address earlier cross-lane process failures (#182 and #134). The application execution pin is older than current semantic main, so this cycle uses current semantics for proposal/shadow recording but does not claim execution of newer framework code inside the pinned application suite.

Recent application hash/chronology repairs are therefore retained as tooling/provenance evidence, but **no new framework issue is opened**: the strongest generic artifact-contract hypothesis is already represented in the now-implemented framework surface, and this cycle has not prospectively demonstrated a current-main regression.

## Next action

In BSD, any future source whose value proposition is “second/higher derivative” in a non-complex-s coordinate should first be screened for a source-bound jet-faithfulness witness. If no such map is part of the theorem, reject it as a direct solution to the complex-order bridge while retaining it as an analogue. If a map is found, verify unramifiedness/unit factors and exact lower-jet vanishing before auditing downstream arithmetic gluing.

No Millennium root status changes.
