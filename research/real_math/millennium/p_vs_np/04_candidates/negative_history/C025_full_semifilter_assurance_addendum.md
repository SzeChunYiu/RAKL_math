# C025 assurance addendum — normalized full-semi-filter regression and capacity scope

**Synthesis role:** This is an assurance addendum to `C025_joint_signature_canonical_scope.md`, not a second candidate and not a competing failure/tool identity. The negative-history framing and C009-based route pruning remain canonical.

**Atom:** `O9d12a2a1a`
**Prior-selected case-plan artifact:** `sha256:39378a50357fd3807d1ee9bcfbdec79e7cf4e5f379d256cfc28d3bf0cb2ce286`
**Machine receipt:** `sha256:fcbdcdcb6a182705253b1cd0779316814c9791ceef549fc3f848023023a476eb`
**Authority:** `ASSURANCE_ADDENDUM / RETROSPECTIVE_EXECUTABLE_ASSURANCE / PROOF_DRAFT / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`

The case plan, predictions and falsifiers were committed before the recorded
output, but the evaluator file and its content hash were absent from that
commit.  Moreover, the registration commit `03a4cb9` and result commit
`1bfad13` lie on divergent descendants of `f479e00`.  The exact counts below
are reproducible, but this execution is **not** strict preregistered-evaluator
evidence.  The machine-readable chronology audit preserves that failure.

## Registered object and scope

Let `G_NEQ` have label set `[N]`, `N>=2`, and diagonal complement universe

\[
U=\{e_u=(u,u):u\in[N]\}.
\]

C025 studies only a simultaneously selected family of normalized complementary cut pairs

\[
p_j=(E_{S_j},H_{S_j}),\qquad
E_{S_j}=\{e_u:u\in S_j\},\quad H_{S_j}=U\setminus E_{S_j}.
\]

The source justification for replacing arbitrary pairs by such partitions is retained only for the `G_NEQ` canonical family, exactly as the canonical C025 negative-history artifact states. This addendum asks a conditional assurance question: **once a normalized partition family is fixed on `G_NEQ`, does signature injectivity also agree with the source preservation definition over every full semi-filter above each unequal edge?** It does not extend the normalization step to arbitrary full semi-filters, arbitrary graphs, or arbitrary semi-filter geometries. It also does not test higher-order tuple/intersection/closure state.

## Proposition C025-L1 — exact joint-signature criterion on `G_NEQ`

Associate to every label the shared joint binary signature

\[
\sigma(u)=(1_{u\in S_1},\ldots,1_{u\in S_k})\in\{0,1\}^k.
\]

The normalized family covers every semi-filter above every unequal edge if and only if `u -> sigma(u)` is injective.

### Forward coverage from unequal signatures

Let `F` be any semi-filter above `(u,v)` with `u!=v`. By the definition of being above that edge, `F` contains the diagonal singleton traces `{e_u}` and `{e_v}`. If coordinate `j` separates `u` and `v`, assume without loss of generality that `u in S_j` and `v notin S_j`. Upward closure gives

\[
E_{S_j}\in F,\qquad H_{S_j}\in F.
\]

But their intersection is empty, and a semi-filter does not contain the empty set. Thus `F` fails to preserve `p_j`. One separating coordinate therefore covers every semi-filter above that unequal edge.

### Collision witness

If `sigma(u)=sigma(v)`, then every cut places `u,v` on the same side. Consider the canonical semi-filter

\[
F_{u,v}=\{W\subseteq U:e_u\in W\text{ or }e_v\in W\}.
\]

For every selected complementary pair, exactly one side contains both `e_u,e_v` and the other contains neither. Therefore the premise that both pair members lie in `F_{u,v}` is false, so `F_{u,v}` preserves that pair. The whole family fails to cover this semi-filter. Hence coverage of all unequal-edge semi-filters is equivalent to injectivity.

## Corollary C025-C1 — exact logarithmic calibration

There are at most `2^k` binary signatures, so injectivity requires

\[
N\le 2^k,\qquad k\ge\lceil\log_2 N\rceil.
\]

Conversely, assign each label its ordinary distinct binary encoding of length `ceil(log2 N)` and take one cut for each bit. This realizes an injective family, so

\[
\boxed{k_{\min}=\lceil\log_2 N\rceil.}
\]

This joint integral representation therefore repairs C024's loss on `G_NEQ`: it recovers the exact logarithmic normalized-cut calibration instead of the fractional value at most `2`.

## Capacity falsifier and its exact boundary

The same proof shows why this repair is not a primary super-logarithmic route by itself. A **cardinality-only** argument using `k` binary coordinates on `M` distinguished first-order traces has only `2^k` joint states. Its pigeonhole separation lower bound is exhausted at `ceil(log2 M)`. When `M` is polynomial in graph side size, that particular argument is only `O(log N)`.

This is not a theorem that all generator-signature lifts have logarithmic cover complexity. Realizability constraints could make coordinates weaker, and higher-order closure state could contain information not representable by labels in a binary codebook. Those possibilities are outside C025.

## Retrospectively reproducible counterexample-first result

The exact result executable, first repository-visible with the output:

- exhaustively enumerated ordered cut families for `2<=N<=4` and found minima `1,2,2`, matching `ceil(log2 N)`;
- checked direct cut separation against signature inequality for every enumerated family in that range;
- constructed exact covering codebooks for `N=2,3,4,5,8,9,16,17`;
- confirmed that `k=ceil(log2 N)-1` has capacity strictly below `N` in every registered case.

These computations are regression evidence for the representation and receipt. The all-`N` statement above rests on the elementary injectivity/counting proof, not on finite enumeration.

## Result and residual

**Accepted narrowly:** joint binary signatures restore simultaneous integral consistency on normalized `G_NEQ` and recover `ceil(log2 N)`.

**Rejected narrowly:** cardinality-only first-order signature capacity is not pursued as the super-log primary invariant. The canonical route-level reason remains C009: state certified only as canonical/original-generator separation is already in a universally logarithmically capped lane.

**Identity reconciliation:** the retained failure is `F-C025-FIRST-ORDER-CANONICAL-COLLAPSE` and the retained tool is `T-PNP-GNEQ-JOINT-SIGNATURE-CALIBRATION`. The assurance result does not mint the parallel provisional capacity-ceiling failure/tool names.

**Still open:** define a higher-order semi-filter closure coordinate with an exact legal per-fusion accounting law and a target-applicable capacity analysis. This requires a fresh child context before another candidate is generated.

No claim about `P=NP` or `P!=NP` follows.
