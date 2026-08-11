# XM004 — P-vs-NP closure-volume cheap-target calibration

**Atom:** `XM-REPRESENTATION-COST-004`  
**Target lane:** P-versus-NP `O9d12a2a1a1` (active pre-candidate PR #49)  
**Framework read first:** `SzeChunYiu/RAKL@a151d5612709ea0f95c3ea232630f246f722739a`  
**Application base:** `SzeChunYiu/RAKL_math@d7f75d6aeb6b04a9586b5e684875460ab42ae0f8`  
**Authority:** `SUPPORTED_RETROSPECTIVE_ROUTE_DIAGNOSTIC / NO_MATHEMATICAL_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`

## Chronology boundary

The source-derived discriminator below was noticed **before** this XM004 packet was frozen. It is therefore permanently ineligible for strict context-first candidate authority and does not count as the prospective retrieval rehearsal left open by XM003. Under current RAKL v3 semantics it is preserved as an outcome-linked retrospective learning episode and scoped failure record; it may change search priority, not theorem authority.

## Cross-problem action chosen

The cycle selected one action with high expected epistemic contraction: transfer only the verified-local **root-bridge stability audit operation** from XM001 to the source-native closure representation being opened in P-vs-NP PR #49, and attack the cheapest representation-to-root-cost inference before any closure invariant is proposed.

The source mathematics is not transferred. The common abstraction is narrower:

> an exact representation can be locally rich while a root-critical cost coordinate remains zero unless the representation feature being measured is actually charged by the bridge to that cost.

The frozen mapping and DifferenceWitness are in `07_memory/XM004_TRANSFER_MAPPING_20260811.json`. The current-main tool remains only `VERIFIED_LOCAL`; pending PR #30/#50 promotions are not treated as canonical authority.

## Primary source

Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033 (2025), especially Section 2.2.4, Theorem 22, Theorem 24, and Claim 27.

The relevant source facts are exact:

1. On `Gamma=[N] x [N]`, the generator family `R_{N,N}` contains **every combinatorial rectangle** `U x V`, with arbitrary `U,V subseteq [N]`. The paper states `D_intersection(G | R_{N,N})=0` for every graph.
2. In the example immediately before the proof of Theorem 22, the authors state that for every nontrivial graph `G`, `rho(G,R_{N,N})=0`: any semi-filter above an edge would have to contain the empty set.
3. Theorem 24 constructs, for a fixed integral pair family `Lambda`, the minimal family `G_w subseteq P(U)` forced into any preserving semi-filter above `w`: generator traces seed the family together with **all supersets**, and `E_i,H_i in G_w` propagates `E_i intersect H_i`, again together with all supersets. Claim 27 identifies `emptyset in G_w` exactly with `w in A`.

Primary source: https://eccc.weizmann.ac.il/report/2025/033/

## Exact cheapest falsifier

Let `A=G` be any nontrivial graph in `[N] x [N]`, let `U=A^c`, and choose the all-rectangle generator family `B=R_{N,N}`.

Fix any `a=(i,j) in A`. Because `R_{N,N}` contains every rectangle, the singleton

`B_a={i} x {j}={a}`

is itself a generator. It contains `a`, so the Theorem-24 base rule inserts its trace

`B_a intersect U = emptyset`

into `G_a`. The same base rule includes every superset of that trace inside `U`. Every subset of `U` is a superset of the empty set, hence

`G_a = P(U)`

already at the base/upward-closure stage, before any pair-preservation propagation is needed. Therefore

`|G_a| = 2^{|U|}`,

which is the **maximum possible raw closure cardinality**, while the exact source example gives

`rho(G,R_{N,N}) = 0`.

So the inference

`large (even maximal) raw source-native closure volume => positive/large cover complexity`

is false.

This is an exact consequence of the source definitions and source-stated zero-cover regime. It is not a new theorem claim and is not presented as novelty.

## What was falsified — and what was not

The scoped failure is `F-XM004-PNP-UPWARD-CLOSURE-VOLUME-INFLATION`.

It rejects raw cardinality/volume, entropy, or a monotone score that assigns hardness merely because many subsets are present in `G_w`. The mechanism is newly useful for the failure portrait: **generator-basis/upward-closure inflation**. A representation can acquire enormous state mass for free from the generator vocabulary and closure convention, independently of pair/fusion cost.

It does **not** reject the source-native closure representation itself. In particular, Theorem 24's productive propagation is indexed by the `t=|Lambda|` cover pairs: a productive step introduces one of the pair intersections `E_i intersect H_i`, and the proof bounds the number of such productive rounds in terms of `t`. A future seed-quotiented coordinate that charges first productive pair-index activation, ancestry, or another explicitly `|Lambda|`-budgeted feature remains open.

That residual must still survive PR #49's existing C010 multiplexing, C021 cheap-target, C023 scalar-collapse, C024 correlation, and C025 projection controls. Different closure states alone do not imply different cover complexity.

## Dual experience query

Both success and failure memory were queried.

- `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` was selected at its current-main `VERIFIED_LOCAL` authority, with target-specific validation supplied by the rectangle-generator falsifier.
- `T-PNP-FRACTIONAL-SEMIFILTER-PACKING` was retrieved but not selected: its guarantee is a sound LP-dual lower-bound certificate, whereas this episode tests closure representation volume.
- `F-XM001-POINTWISE-GAP-COLLAPSE` is a cross-problem warning about losing a root-critical coordinate; its Yang–Mills normalization mechanism is explicitly disanalogous.
- `F-C024-FRACTIONAL-INTEGRALITY-GAP` is a target-local warning about losing correlation/integrality, but it is not the same mechanism as free upward-closure inflation.
- PR #49's bound C010/C021/C023/C025 hostile controls remain active and are not superseded.

The post-result timing is recorded in `XM004_RETROSPECTIVE_MEMORY_QUERY_20260811.json`; it receives no pre-candidate gate credit.

## Six-role expert cell

1. **Circuit/fusion complexity lead** checked the implication directions of Theorems 22 and 24. Verdict: accept the zero-cover calibration; reject any reading that reverses Theorem 24 into a lower bound.
2. **Combinatorics/closure-systems lead** checked the base/upward rule. Verdict: the singleton rectangle forces `emptyset` and hence the full powerset exactly; raw closure mass is contaminated before propagation.
3. **Cross-domain transfer lead** compared XM001/Yang–Mills, BSD/Hodge reuse, and the P-vs-NP target. Verdict: transfer only the audit operation; the mechanism is a new finite representation-cost disanalogy.
4. **Adversarial falsification lead** asked whether the example merely uses a degenerate illegal target. Verdict: no—the all-rectangle family is an explicit source-defined discrete space and Theorem 22's own example states its zero cover complexity; nevertheless the conclusion must remain scoped to raw volume.
5. **Formal-assurance/chronology lead** observed that the discriminator predated the XM004 freeze. Verdict: record it as retrospective calibration/TaskEpisode; do not create a fake pre-candidate trace or claim prospective retrieval success.
6. **Novelty/research-value lead** treated the mathematical consequence as source-derived rather than novel. Its value is programmatic: it removes a tempting entire score family before candidate generation and identifies the minimally safer residual representation.

Consensus: **reject raw closure volume; retain seed-normalized pair-budgeted ancestry as an open representation question; do not change any Millennium root status.**

## Breakthrough-learning proposal and falsifiable benchmark

Use `CONTRASTIVE_DISCRIMINATION` plus a bounded `FIXATION_RESET`, proposal-only. Benchmark the next closure representation on two controls before target evaluation:

- hostile zero-cost control: `B=R_{N,N}`, where generator/upward closure may be enormous but the score must not invent positive cover cost;
- positive calibration: a source instance such as the existing `G_NEQ` lineage where integral cover complexity is nonzero and known exactly.

A candidate representation passes this search-policy benchmark only if it explicitly quotients/freezes the generator-seeded closure and charges a feature with a source-bound relation to pair/fusion work; it must then survive multiplexing and scalar-collapse controls. Passing this benchmark creates zero theorem authority.

## Program effect

PR #49 currently asks for a candidate-free `ClosureStateInterfaceAudit` before invariant generation. XM004 supplies a decisive first hostile case for that audit and narrows the useful search substrate:

`raw G_w state mass` -> **rejected**

`seed-quotiented, pair-indexed productive activation/ancestry` -> **still open, requires fresh prospective testing**

No P-versus-NP, RH, Navier–Stokes, Yang–Mills, Hodge, or BSD root certificate changes.