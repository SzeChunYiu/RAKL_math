# C041A — odd-slice copy rule is exactly non-amplifying

**Parent atom:** `O9d12a2a1b`  
**Cycle atom:** `O9d12a2a1b-C041A`  
**Authority:** `PROPOSAL_SHADOW_LOCAL_NEGATIVE_RESULT / NO_ROOT_AUTHORITY / SAME_CONTEXT_REVIEW_ONLY`  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`

## Source-bound setup

The local object is the Cavalar–Oliveira two-dimensional cover problem. For a graph `G subset [M]x[M]`, write `U=[M]x[M] \ G` for the complement ground set. A semi-filter over `U` is a nonempty upward-closed family of subsets of `U` that excludes the empty set; relevance above an edge is determined by containing the corresponding row and column traces. A legal pair covers a semi-filter when both operands are in the semi-filter but their intersection is not. Cover complexity `rho(G,G_{M,M})` is the minimum number of legal pairs covering every relevant semi-filter. The source identifies this cover complexity with cyclic intersection complexity in its exact stated scope.

Primary source: Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033 (2025), Definitions 18–21 and Theorem 30. Exact PDF bytes inspected in this cycle: SHA-256 `3f7d98691f3ac28208df6e8669d860c45b6068781dd77c737eb1e780641fbea7`.

## One uniform rule authorized by the frozen C041 discriminator

Let the parent size be `M`. Define the injection

`i:[M]x[M] -> [2M]x[2M]`, `i(u,v)=(2u-1,2v-1)`.

For a parent complement ground set `U`, define

`U' := i(U)`

and the associated child graph

`G' := [2M]x[2M] \ U'`.

Equivalently, child-complement membership is true exactly when both child coordinates are odd and the pulled-back parent pair lies in `U`. Therefore, if parent membership is uniformly decidable in `poly(M)`, child membership is uniformly decidable in `poly(2M)`. This is only the frozen local `E`-language explicitness coordinate; it supplies no `NP` verifier or root bridge.

## Proposition C041A.1 — exact cover-graph isomorphism

For the rule above, the full cover graph `Phi_{G',G_{2M,2M}}` is isomorphic to `Phi_{G,G_{M,M}}`. Consequently

`rho(G',G_{2M,2M}) = rho(G,G_{M,M})`.

The same bijection preserves the standard fractional set-cover relaxation used by C024, so

`rho_frac(G',G_{2M,2M}) = rho_frac(G,G_{M,M})`.

Thus this rule has exact augmentation `0`; it cannot amplify either integral or fractional cover complexity.

### Proof

The injection `i` is a Boolean-lattice isomorphism from `P(U)` to `P(U')` via `S -> i(S)`. Hence it bijects upward-closed nonempty families excluding the empty set, so it bijects parent and child semi-filters as abstract families.

Now consider a child graph edge `(r,c) in G'`. If `r` is even, its row trace into `U'` is empty, because every point of `U'` has odd first coordinate. If `c` is even, its column trace into `U'` is empty for the analogous reason. A semi-filter above such an edge would have to contain the empty set, contradicting the semi-filter definition. Therefore no relevant child semi-filter lies above an edge with an even coordinate.

The only child edges that can witness relevance are odd-odd edges `(2u-1,2v-1)`. Such an edge is in `G'` exactly when `(u,v)` is in `G`. Its row and column traces into `U'` are precisely the images under `i` of the parent row and column traces into `U`. Hence the map `F -> i(F):={i(S):S in F}` is a bijection between relevant parent semi-filters and relevant child semi-filters, preserving the witnessing edge.

Likewise every ordered pair `(E,H)` of subsets of `U` corresponds to `(i(E),i(H))`, and membership of `E`, `H`, and `E intersect H` in a semi-filter is preserved. Therefore the pair-to-semi-filter coverage relation is preserved exactly. The two bipartite cover graphs are isomorphic, proving equality of minimum integral cover size and of the LP relaxation. QED.

## Proposition C041A.2 — general slice transport of old dual mass

The exact copy rule is a hostile control for a broader transport fact. Suppose a child complement `V subset [2M]^2` has an embedded parent slice satisfying

`V cap (odd x odd) = i(U)`.

For every parent semi-filter `F` define its upward lift

`L(F) := {X subset V : exists S in F with i(S) subset X}`.

Then `L(F)` is a child semi-filter. If `F` is relevant above parent edge `(u,v)`, `L(F)` is relevant above child edge `(2u-1,2v-1)`. Moreover, if a child legal pair `(E',H')` covers `L(F)`, then the pullback pair

`(i^{-1}(E' cap i(U)), i^{-1}(H' cap i(U)))`

covers `F`. Therefore any parent dual-feasible weighting of relevant semi-filters can be lifted with the same weights and remains child dual-feasible. In particular,

`rho_frac(child) >= rho_frac(parent)`

under this exact slice-preservation hypothesis.

This establishes persistence/feasibility transport only. It does not establish any positive augmentation.

### Proof sketch with the exact required checks

Upward closure and exclusion of the empty set for `L(F)` follow directly from the definition and the same properties of `F`. Parent row/column traces embed inside the corresponding child traces, giving relevance. If `(E',H')` covers `L(F)`, then `E'` and `H'` each contain embedded members of `F`, so their pulled-back slice traces lie in `F` by upward closure. If the pullback intersection were in `F`, its image would be contained in `E' intersect H'`, forcing `E' intersect H'` into `L(F)`, contradiction. Thus the pullback pair covers `F`. The load of every child pair against lifted old mass is therefore bounded by the load of its parent pullback pair, hence by one.

## Proposition C041A.3 — residual-slack criterion for one fresh atom

Fix a lifted old dual `y` on a finite child cover graph and let

`ell(p) := sum_{F covered by p} y_F`, `s(p):=1-ell(p) >= 0`.

For one new relevant semi-filter `K`, there exists an `epsilon>0` such that adding mass `epsilon` only to `K` remains dual-feasible **iff** every child pair covering `K` has strictly positive slack.

Necessity is immediate: a saturated pair with `s(p)=0` covering `K` is violated by any positive `epsilon`. For sufficiency, the child pair universe is finite; choose `epsilon` no larger than the minimum positive slack among pairs covering `K` (and arbitrary positive `epsilon` if no pair covers `K`).

So the next augmentation atom is not merely “preserve relevance.” It is:

> Construct an off-slice child contribution that creates at least one new relevant semi-filter outside the neighborhoods of all saturated lifted pairs, while preserving the old dual transport and the source-domain/explicitness contracts.

This is an exact local reduction of positive one-coordinate augmentation to a saturated-neighborhood avoidance condition. It is not a recurrence, divergence theorem, circuit lower bound, NP membership proof, or P-vs-NP result.

## Counterexample-first comparison with C037

C037 showed that an arbitrary one-edge extension can destroy relevance of one of three positive-weight parent supports. The odd-slice copy rule avoids that failure by isolating an exact parent copy: all old relevant supports transport. But it still has zero augmentation because every relevant child object is merely the copied parent object.

The DifferenceWitness is therefore sharp:

- `C037`: persistence fails before augmentation can be asked;
- `C041A`: persistence and dual feasibility hold exactly, but augmentation is identically zero.

Hence “relevance persistence” and “positive residual capacity” are distinct obligations. C038-style persistence, even if later promoted, would not by itself close the C041 amplification atom.

## Local-to-global boundary

Local mathematical status: `SOLVED_PROPOSAL_SHADOW_NEGATIVE_FOR_COPY_ONLY_RULE`.

Local-to-global/gluing status: `OPEN`. No divergent sequence of positive increments is obtained, no superlogarithmic/superpolynomial rate is obtained, the graph-to-Boolean checkpoint is not advanced, and no NP verifier or lower-bound-preserving NP reduction is supplied. The P-vs-NP root remains open.

## Novelty classification

Shadow-only classification: `REPRESENTATION_NOVEL` is defensible for the explicit odd-slice obstruction packaging and `COMPOSITIONAL` for the residual-slack reduction from the existing LP dual. No protected novelty is retained or promoted in this cycle.