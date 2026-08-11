# O9d12a2a1a1d source packet — cyclic join-elimination audit

Status: `FROZEN_FOR_VERIFICATION / PROPOSAL_SHADOW_ONLY`  
Frozen at: `2026-08-11T15:31:40Z`  
Framework source of truth: `SzeChunYiu/RAKL@9027cc6beab7e935d714bbdf8e902b89b50caaa8`  
Application base: `SzeChunYiu/RAKL_math@111a3f95c72b0a418f968708bd3eda77ef98bccf`

## Primary source actually consulted

Bruno P. Cavalar and Igor C. Oliveira, **Boolean Circuit Complexity and Two-Dimensional Cover Problems**, ECCC TR25-033, 18 March 2025, report page and PDF re-opened on 11 August 2026.

Exact source controls used in this atom:

1. Section 2.5 defines a cyclic syntactic sequence `I_1,...,I_t`, each gate using union or intersection of another gate or an original generator; evaluation starts all cyclic gates at the empty set and iterates monotonically. `D^cyc_cap` counts only intersection operations.
2. Lemma 16 states that the monotone evaluation converges after at most the syntactic-sequence length.
3. Corollary 17 gives `D^cyc_cap(A|B) <= D_cap(A|B) <= (D^cyc_cap(A|B))^2` and explicitly notes that update-step unions do not increase intersection complexity.
4. Theorem 30 states, for non-trivial `A` and non-empty generator family `B`, `rho(A,B)=D^cyc_cap(A|B)`.
5. Theorem 24 is used only as route provenance: its construction gives the cover-to-intersection upper direction, not the join-elimination claim below.

Primary-source URLs are preserved in the public trace/evidence pointers; this local packet is a bounded projection, not a replacement for the paper.

## Pending application artifact consulted with downgraded authority

Draft PR #113, `research(pnp): quotient cost-zero union expansions before invariant search`, head `0df8dc978903278414479d4f448382ac2ec53b35`, was inspected but is **not current-main mathematical authority**. Its proposed free-union lemma is used only as search-priority evidence. The current atom does not assume that PR merged or that its local proof is promoted.

## Exact verification target

Candidate representation claim, frozen for verification only:

> Any finite cyclic syntactic sequence over a finite non-empty generator family `B` with exactly `k` intersection gates can be transformed, without changing its least-fixed-point output and without changing `k`, into a system whose counted core consists of exactly those `k` intersection gates. Each input to a counted intersection gate, and the final output expression, is a finite union of original generators and counted-intersection outputs. Pure-union gates are eliminated by reachability through the union-only dependency subgraph.

Converse direction to check: any such `k`-meet system with union expressions can be expanded into a cyclic syntactic sequence using exactly `k` intersection gates.

This is a representation-normal-form candidate only. It is not a lower bound, not a proof of `P != NP`, and not a novelty claim.

## Predeclared hostile worlds

The verification must fail the candidate if any of these changes semantics:

- a pure union SCC with no intersection gate;
- a union SCC fed by an intersection output and feeding back into an input of that same intersection gate;
- two intersection gates coupled through union-only paths in both directions;
- a final output gate that lies inside a union SCC;
- duplicate generator occurrences or the empty generator contribution;
- a target reached only after more than one synchronous fixed-point iteration.

The decisive falsifier is an explicit finite cyclic syntactic sequence in which OR-reachability elimination changes the converged set at any gate needed by an intersection input or the final output.

## Source boundary

No 2026 range-avoidance/circuit-lower-bound theorem is transferred into this atom. ECCC TR26-118 was retrieved as frontier context but rejected for this step because no applicability map or DifferenceWitness connects its range-avoidance/win-win coordinates to the cyclic set-system normalization being verified here.
