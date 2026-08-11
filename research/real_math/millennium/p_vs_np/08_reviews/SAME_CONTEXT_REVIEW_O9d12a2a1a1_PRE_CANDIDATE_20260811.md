# Same-context expert review — O9d12a2a1a1

**Scope:** pre-candidate review only.  
**Framework:** `SzeChunYiu/RAKL@bd1a2768f0f474ff44ffa25243241f94bfaf6466`.  
**Application base:** `SzeChunYiu/RAKL_math@4838969ecc18a091da79a059b58b8568634289b7`.  
**Context packet:** `O9d12a2a1a1_CONTEXT_FIBER_20260811.json`, `sha256:b955ea913e2aed2f6e67844c2d1b8412b4e75a0161de73681d70c6c66f9cd110`.  
**Authority:** role-separated same-context technical review. This is not independent peer review and grants no mathematical or framework authority.

## Review cell

### 1. Complexity-theory lead

**Background/role.** Boolean circuit complexity, Karchmer-Wigderson style communication formulations, source-level transference, and lower-bound barriers. Owns exact root-coordinate and theorem-scope checking.

**Evidence inspected.** Cavalar-Oliveira source-bound definitions as already frozen in the lane; C008, C009, C010, C016, C024, C025; current root contract and C025 DAG delta.

**Finding.** The active residual should not be phrased merely as “add higher-order closure state.” C008 proves that full noncanonical obligations can exceed the canonical subproblem, but C010 independently supplies an optimal all-disjoint two-pair cover for the same C008 instance. Thus C008 is evidence that canonical information is insufficient, not evidence that nonempty intersections or derived-intersection ancestry are essential.

**Strongest objection.** A new closure-depth invariant could be an artifact of one convenient optimal cover representation. If an equal-cardinality all-disjoint cover exists, the proposed state is not forced by the source object.

**Delegated discriminator.** Compare unrestricted full-cover optimum with the optimum when every selected pair is disjoint, holding the exact full semi-filter universe fixed.

**Vote:** `ACCEPT_NEXT_DISCRIMINATOR / BLOCK_HIGHER_ORDER_CANDIDATE_UNTIL_TESTED`.

### 2. Combinatorial-optimization / method-transfer lead

**Background/role.** Set cover, LP relaxations, integrality gaps, restricted admissible-set families, and transfer of optimization relaxations into communication/circuit complexity. Owns the method-transfer matrix and difference witnesses.

**Evidence inspected.** C024 fractional cover/dual packing, C025 integral G_NEQ repair, Karchmer-Kushilevitz-Nisan fractional-cover context, and Chlamtac-Friggstad-Georgiou lift-and-project warning.

**Finding.** The proposed restricted-vs-unrestricted comparison is source-native: the universe of obligations is unchanged and only the admissible pair family is restricted. A strict gap would establish a finite operational role for nonempty intersections without claiming an asymptotic lower bound. A null result is equally useful because it blocks a common but currently unsupported explanation of noncanonical hardness.

**Strongest objection.** `rho_disj` could become another auxiliary statistic with no root relevance. It should be used only as a discriminator for representation necessity, not as a lower-bound invariant unless a later theorem supplies a bounded fusion law and asymptotic bridge.

**Delegated discriminator.** Freeze a bounded exact graph universe and report both `rho` and `rho_disj`, including nulls. No hierarchy escalation until a strict gap is observed or a theorem rules the comparison out.

**Vote:** `ACCEPT_AS_FINITE_DISCRIMINATOR_ONLY`.

### 3. Adversarial representation/falsification lead

**Background/role.** Counterexample-first proof search, representation invariance, alternate-witness attacks, quotient/multiplexing/state-compression adversaries. Owns cheapest falsifiers.

**Evidence inspected.** C010 multiplexing, C013 quotient warning via current context, C016 finite-state compression, C023 scalar-collapse warning, and C025 first-order canonical collapse.

**Finding.** The cheapest falsifier is not to search for a complicated higher-order signature. First test whether non-disjoint pairs ever buy even one unit of exact cover cardinality on a frozen tiny universe. If no gap appears, that is not a theorem but materially lowers the priority of closure-ancestry representations.

**Strongest objection.** A search can accidentally be tuned after seeing exploratory output. The exact graph-size/complement-size boundary, pair restriction, evaluator implementation, output schema, and null interpretation must be frozen before evaluated output.

**Delegated discriminator.** Prospective search on all nontrivial `4 x 4` bipartite graphs with complement size at most `4`, using the exact existing semi-filter oracle semantics, reporting the first gap if any and aggregate count otherwise. This boundary is computationally bounded and distinct from the unregistered exploratory `3 x 3, |U|<=5` check.

**Vote:** `ACCEPT_IF_PREREGISTERED_BEFORE_RUN`.

### 4. Formal-methods / reproducibility lead

**Background/role.** Exact finite combinatorics, content binding, executable oracles, chronology, CI and proof-vs-computation boundaries. Owns implementation trust and receipt design.

**Evidence inspected.** Existing `full_cover_oracle.py`, C025 retrospective chronology audit, current RAKL v3 authority-hardening receipt, and current PNP exact-CI practice.

**Finding.** The existing oracle already exposes the exact Definition-20 predicate. The lowest-risk implementation is additive: factor the pair-mask enumeration so an optional `disjoint_only` restriction is mechanically identical except for rejecting `E & H != 0`; independently verify C008 returns `(rho,rho_disj)=(2,2)`; then run the frozen `4 x 4, |U|<=4` census. The result is finite computational calibration, not proof of an asymptotic statement.

**Strongest objection.** The v3 framework is now internally hardened, but this application result still cannot receive independent-review or theorem authority from the same session. The run receipt must bind exact base, evaluator bytes, preregistration bytes and output bytes.

**Delegated discriminator.** Add exact tests for restricted/original oracle agreement on C008 and for disjoint-pair validation. Freeze evaluator hash before running the census.

**Vote:** `ACCEPT_WITH_EXACT-BYTE_BINDING`.

### 5. Novelty / research-value lead

**Background/role.** Prior-art triage, significance calibration, rediscovery risk, and information-gain selection. Owns whether a result changes the research programme rather than merely adding another finite observation.

**Evidence inspected.** Current R004 route history and source anchors. No exhaustive novelty search was attempted because no novelty claim is requested for the restricted diagnostic.

**Finding.** The value of this cycle is route discrimination. A strict finite gap would justify a new child asking what invariant of non-disjoint intersections survives equivalent optimal covers. A null census would narrow the search away from naive “closure depth is the missing coordinate” narratives and toward richer obligation correlations not captured by pair overlap alone.

**Strongest objection.** Even a positive finite gap can be mathematically routine and may not scale. Do not advertise it as new circuit-complexity mathematics without a separate bounded novelty audit and asymptotic bridge.

**Delegated discriminator.** Treat the result as `RETROSPECTIVE/FINITE_CALIBRATION` or `SOURCE_BOUND_FINITE_DISCRIMINATOR`, never as root progress.

**Vote:** `ACCEPT_FOR_INFORMATION_GAIN / NO_NOVELTY_CLAIM`.

## Cell synthesis

All five lenses agree on one action before any higher-order closure candidate:

> Freeze and run an exact restricted-vs-unrestricted full-cover census that asks whether allowing nonempty intersections strictly reduces the number of pairs required to cover the same full semi-filter universe.

The registered prospective boundary is **all nontrivial `4 x 4` bipartite graphs with complement size `1..4`**. The evaluated output must be generated only after the preregistration/evaluator bytes are frozen. The earlier unregistered exploratory `3 x 3` check receives no prospective evidence credit.

### Decision branches

- **If a strict gap exists:** retain the smallest lexicographic witness as a finite calibration object; open a child atom asking for a representation-invariant characterization of the non-disjoint advantage and immediately attack it with C010/C016 compression.
- **If no strict gap exists in the frozen universe:** record a bounded null. Do not infer global eliminability of non-disjoint pairs. Lower the priority of closure-depth/ancestry candidates and broaden the next representation search to obligation correlations that are invariant under disjoint-cover replacement.
- **If the oracle or chronology fails:** classify the cycle as tooling/provenance failure, not mathematical evidence.

## Unresolved uncertainty

The cell does not know whether a strict finite gap exists outside the frozen tiny universe, whether any such gap scales, or whether it corresponds to a useful cyclic-intersection lower-bound invariant. Those are intentionally left open.
