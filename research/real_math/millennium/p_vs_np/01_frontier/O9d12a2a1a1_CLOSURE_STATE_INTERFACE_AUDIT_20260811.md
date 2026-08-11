# O9d12a2a1a1 — ClosureStateInterfaceAudit: normalized `G_NEQ` is a one-step signature system

**Date:** 2026-08-11  
**Authority:** `SOURCE_BOUND_INTERFACE_ROUTE_PRUNING / EXACT_LOCAL_LEMMA / COMPUTATION_IS_NOT_PROOF / SAME_CONTEXT_REVIEW_ONLY / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`  
**Candidate status:** none. This executes the pre-registered candidate-free interface audit from `O9d12a2a1a1`; it does not propose a lower-bound invariant.

## Executive finding

The requested DifferenceWitness cannot be obtained **inside the only scope in which C025-level signatures are source-defined**.

For the `G_NEQ` canonical specialization after Claim 41 / Lemmas 42–43 normalization, every pair is a partition `(E_i,H_i)=(E_i,U\E_i)`. In the source-defined Theorem 24 closure, the only possible derived intersection is therefore

\[
E_i\cap H_i=\varnothing.
\]

For an edge `e=(u,v)`, the pair is propagation-active at the base stage exactly when the C025 signatures of `d_u` and `d_v` differ in coordinate `i`. Hence the whole nontrivial derived-activation interface is the coordinatewise XOR of the two C025 signatures. If any coordinate fires, upward closure of `emptyset` immediately yields all of `P(U)`; if none fires, propagation is already at a fixed point.

So the source-general closure `G_w(Lambda)` **is genuinely richer in general**, but that richness degenerates under the C025 normalization used to define the comparison. The prior packet's proposed transfer—"use derived intersections absent from C025 signatures as the discriminator"—does not survive its first source-exact interface check.

The correct action is re-atomization, not a candidate.

## Source binding

Primary source: Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033 / ACM TOCT 17(2), 2025.

The audit uses only the following source facts:

1. In Theorem 24, with `U=A^c`, the minimal family `G_w` starts from every generator trace `B_U=B∩U` for generators containing `w`, together with all supersets.
2. If both `E_i` and `H_i` are present, propagation adds `E_i∩H_i` and all supersets.
3. In the `G_NEQ` example, `U=bar(G_NEQ)` is the diagonal; for `e=(u,v)` the two canonical generator traces are the singleton diagonal points `d_u` and `d_v`.
4. Claim 41 characterizes coverage of the canonical filter by separation of those two singleton traces.
5. Lemmas 42–43 justify, **only for that canonical `G_NEQ` calibration**, replacing a covering pair by a complementary partition.

The source uses `G_w` in an upper construction (Theorem 24); no lower-bound monotonicity is transferred here.

## Exact local lemma

### O9d12a2a1a1-L1 — partition-closure collapse

Let

\[
U=\{d_1,\ldots,d_N\}=\overline{G_{\rm NEQ}},
\qquad
\Lambda=\{(E_i,H_i)\}_{i=1}^k,
\qquad
H_i=U\setminus E_i.
\]

For an edge `e=(u,v)` with `u != v`, define the C025 signature

\[
\sigma_\Lambda(x)_i=\mathbf 1[d_x\in E_i].
\]

Then the source Theorem-24 closure above `e` has base state

\[
G_e^{(0)}
=
\{S\subseteq U:\ d_u\in S\ \text{or}\ d_v\in S\}.
\]

For every coordinate `i`,

\[
E_i,H_i\in G_e^{(0)}
\quad\Longleftrightarrow\quad
\sigma_\Lambda(u)_i\ne \sigma_\Lambda(v)_i.
\]

Consequently,

\[
G_e(\Lambda)=
\begin{cases}
\mathcal P(U),&\sigma_\Lambda(u)\ne\sigma_\Lambda(v),\\
G_e^{(0)},&\sigma_\Lambda(u)=\sigma_\Lambda(v).
\end{cases}
\]

In particular, the first-stage derived-activation vector is exactly

\[
a_i(e)=
\sigma_\Lambda(u)_i\oplus\sigma_\Lambda(v)_i.
\]

### Proof

Only row `u` and column `v` among the row/column generators contain the edge `e`; their traces on the diagonal complement are `{d_u}` and `{d_v}`. The Theorem-24 base rule and upward closure therefore give exactly the displayed `G_e^(0)`.

For a normalized partition pair, `E_i` belongs to the base state iff it contains at least one of `d_u,d_v`; the same holds for `H_i`. Since the two sides are complementary, both belong to the base state iff the two diagonal points lie on opposite sides, which is exactly the XOR condition.

If a pair fires, its intersection is empty. The source propagation rule then adds every superset of the empty set, i.e. all of `P(U)`. If no pair fires at the base stage, no propagation rule can add anything, because every possible consequent is the empty set and none of its antecedent pairs is present. This proves the formula.

This is a direct specialization of the source rules plus the C025 normalization, not a new circuit lower-bound theorem.

## Counterexample-first DifferenceWitness audit

The frozen criterion asked for source-exact cases with identical C025-level generator-signature information but different derived closure activation.

There are two natural exact readings, and both fail.

**Reading A — valid C025 covering family.** C025 already proves that a normalized family covering every canonical `G_NEQ` filter has an injective signature map. Distinct diagonal witnesses therefore cannot share the same complete C025 signature inside a valid calibration. Moreover the signature matrix determines every partition side exactly: `E_i={d_u : sigma(u)_i=1}`. There is no hidden normalized pair information for the closure to recover.

**Reading B — relax coverage and permit signature collisions.** The lemma above still applies. Two edge states with the same ordered pair of C025 signatures have the same derived-activation XOR vector. Their raw base closures may differ because the generator identities `{d_u},{d_v}` differ, but that is original-generator identity, not a new derived-intersection coordinate. Counting such raw differences would therefore violate the DifferenceWitness intent.

Thus `NO_DERIVED_DIFFERENCEWITNESS_WITHIN_NORMALIZED_GNEQ`.

## Executable falsifier

`05_falsification/closure_state_interface_gneq.py` exhaustively checks every ordered partition family with `0 <= k <= 2` for `2 <= N <= 5`.

The exact finite regression covers:

- `1,424` partition families;
- `24,896` ordered unequal-edge states;
- `7,740` same-signature edge groups.

It verifies, for every case, that base pair activation equals signature XOR and that the terminal closure is either the unchanged base closure or all of `P(U)` exactly as the lemma predicts. It also deliberately finds cases where raw base states differ under the same pair-level signature information while derived activation stays identical, guarding against the false proxy "raw closure difference = higher-order information".

This computation is a regression against transcription/case mistakes only. The proof above carries the local mathematical authority.

## Method-transfer matrix update

| Method / representation | Transfer into this interface | Result | DifferenceWitness / disanalogy |
|---|---|---|---|
| Theorem-24 source closure | exact | retained as source semantics | general nonempty intersections disappear after C025 partition normalization |
| C025 joint signatures | exact on normalized `G_NEQ` | sufficient statistic for derived activation | activation is coordinatewise XOR |
| Horn / data-flow analogy | exact but degenerate | one-step dependency language only | no nonempty derived fact can be chained in the normalized calibration |
| generic hierarchy strengthening | not licensed | rejected | no source-specific missing coordinate has been identified |
| upper-first screening | retained | no target evaluation yet | route already fails before a hard-target claim is reached |

The structural analogy therefore reverses from "possibly deep Horn closure" to "one-step Horn-to-bottom" in the C025 specialization. This is precisely the disanalogy that the interface audit was meant to detect.

## Same-context expert-cell disposition

The six roles are documented separately in `08_reviews/SAME_CONTEXT_REVIEW_O9d12a2a1a1_INTERFACE_AUDIT_20260811.md`. Their shared conclusion is:

- fusion/source specialist: **ACCEPT L1 / BLOCK transfer to a lower-bound invariant**;
- closure specialist: **ACCEPT one-step collapse / reject raw state-size proxy**;
- communication/set-cover specialist: **DifferenceWitness gate FAILS in exact C025 scope**;
- adversarial specialist: **stop before C010/C021/C023 target controls because there is no discriminator to stress-test**;
- formal-assurance specialist: **retain computation as regression only; no candidate or proof promotion**;
- novelty/value specialist: **no novelty claim; material value is route correction and preserved negative history**.

These are same-context roles, not independent reviews.

## Hostile-control disposition

The ordered hostile-control pipeline stops at its first prerequisite:

- `F-C025-FIRST-ORDER-CANONICAL-COLLAPSE`: **TRIGGERED / strengthened at the closure interface**. The normalized closure is exactly first-order signature separation.
- `F-C024-FRACTIONAL-INTEGRALITY-GAP`: **INHERITED**. C025's integral joint state remains the calibration repair; this audit adds no further integrality coordinate.
- `F-C010-MULTIPLEXING`: **NOT_REACHED_NO_DIFFERENCEWITNESS**. There is no new closure discriminator whose reuse stability can be tested.
- `F-C021-CHEAP-ADJACENCY`: **NOT_REACHED_NO_TARGET**.
- `F-C023-SCALAR-COLLAPSE`: **NOT_APPLICABLE_NO_SCORE**.

Stopping here is deliberate: running later controls on a nonexistent discriminator would create false evidence.

## Failure-memory delta

New scoped failure:

`F-O9D12A2A1A1-PARTITION-CLOSURE-COLLAPSE`

> The source-general `G_w(Lambda)` closure loses its higher-order intersection coordinate when compared inside the normalized `G_NEQ` C025 scope, because every normalized consequent `E_i∩H_i` is empty and propagation is exactly signature XOR.

This does **not** say source-general closure is weak, that all closure-derived objects are logarithmically bounded, or that no noncanonical cover invariant exists.

## Metacognitive / breakthrough-learning control

The effectual probe produced high information at low cost: it falsified the exact transfer premise before a candidate was spent. Proposal-only modes for the next step are:

- `CONTRASTIVE_DISCRIMINATION`: keep "source-general closure" distinct from "C025-normalized closure";
- `FIXATION_RESET`: do not escalate the same normalized binary-signature vocabulary;
- `INCUBATION_CONTEXT_ROTATION`: open a fresh source-general interface atom before defining a score.

`META_METHOD_BASIS_AUDIT` is **not** promoted from this result alone: the new source-native basis has only received one exact interface falsification, even though older route families are saturated.

No cross-Millennium memory was imported: the obstruction was resolved by exact local source semantics, so there was no applicability/DifferenceWitness justification for a transfer.

## Residual / next atom

Open `O9d12a2a1a1a` as `OPEN_CONTEXT_REQUIRED` with the narrower target:

> Define a source-general, explicitly scoped first-order projection outside the C025 partition specialization, and determine whether any fixed `(A,B,Lambda)` admits a genuine later closure-activation distinction after that projection. If the projection is already a congruence for the closure recurrence, record the no-go instead of inventing a hierarchy.

A fresh `MathContextFiber`, method-transfer matrix, expert cell, dual-memory review and pre-candidate trace are required before any candidate in that child.

## Root status

`OPEN_NO_SOLUTION_CERTIFICATE`.

No super-logarithmic full-cover lower bound, circuit lower bound, `P != NP` proof, novelty certificate, formal proof certificate, or independent review is created by this audit.
