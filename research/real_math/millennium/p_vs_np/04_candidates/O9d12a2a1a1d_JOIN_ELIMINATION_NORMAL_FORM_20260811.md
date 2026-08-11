# O9d12a2a1a1d — join-elimination normal form for cyclic intersection complexity

**Status:** `VERIFIED_LOCAL_PROPOSAL_SHADOW / REPRESENTATION_ONLY`  
**Root authority:** `NONE`  
**Discovery chronology:** the representation candidate was proposed before the v3 pre-action receipt and therefore receives no prospective discovery credit. The subsequent verification action is bound to `PNP-O9d12a2a1a1d-PRE-ACTION-VERIFY-R1-20260811`.

## Statement

Let `Gamma` be finite and `B` a finite non-empty family of subsets of `Gamma`. Consider a finite cyclic syntactic sequence in the sense of Cavalar–Oliveira ECCC TR25-033 Section 2.5, and suppose exactly `k` gates use intersection. Evaluation starts all cyclic gates at the empty set and uses the source's monotone accumulating update rule.

Partition the gate nodes into counted intersection nodes `M={m_1,...,m_k}` and uncounted union nodes `U`.

For every union node `u`, build the directed graph containing only edges whose **head is a union node**. Treat each generator `B_j` and each counted intersection output `m_i` as an external source. Let `R(u)` be the set of such external sources that reach `u` by a path consisting only of union nodes after the first source edge.

Then the converged value of each union node is exactly the union of the converged values of the sources in `R(u)`. Consequently the original system has the same least-fixed-point output as a reduced system with exactly the `k` counted nodes, where every counted node has the form

`X_i >= P_i(X_1,...,X_k) ∩ Q_i(X_1,...,X_k)`

and each `P_i,Q_i` is a finite union of original generators and counted-node variables. The final output is likewise either one counted variable or a finite union of generators and counted variables.

Conversely, every finite system of this form expands to a cyclic syntactic sequence with exactly `k` intersection gates by implementing each finite union expression with uncounted binary union gates.

Thus cyclic intersection complexity admits an exact **join-elimination normal form**: all uncounted union-node topology can be compiled into reachability expressions around the `k` counted intersection nodes without changing the converged target or the counted cost.

## Proof

Write the converged gate values as a vector `(Y,Z)`, where `Y` are the values at counted intersection nodes and `Z` are the values at union nodes. Because the source update is accumulating and monotone, the converged vector is the least solution of the corresponding closure inequalities.

Fix temporarily an assignment `Y` to the counted nodes. The union subsystem contains only inequalities of the form

`Z_u >= V_a ∪ V_b`,

where each operand is either a generator, a counted variable from `Y`, or another union variable. Its least solution is obtained by ordinary directed reachability: `Z_u` is the union of exactly those external generator/counted values that can reach `u` through union nodes. Call this least union solution `J(Y)`. The claim follows directly by induction on finite path length in one direction and by closure of the reachability union under every union inequality in the other; cycles add no source beyond those already reachable.

Now eliminate `Z` from every counted-node inequality by substituting `J(Y)`. This gives a reduced monotone system

`Y_i >= P_i(Y) ∩ Q_i(Y)`

with `P_i,Q_i` finite unions of generators and counted variables.

To compare least solutions, first take any full closed solution `(Y,Z)` of the original system. Since `J(Y)` is the least union-subsystem solution for that fixed `Y`, we have `Z >= J(Y)`. Monotonicity of intersection then implies that `Y` satisfies every reduced inequality. Hence the projection of every full solution is a reduced solution.

Conversely, if `Y` satisfies the reduced inequalities, then `(Y,J(Y))` satisfies all original union inequalities by construction and all original counted-intersection inequalities by the substituted reduced inequalities. Hence every reduced solution lifts to a full solution.

The two maps preserve the componentwise order. Therefore the projection of the least full solution is exactly the least reduced solution, and `J` reconstructs the eliminated union values at that solution. Applying the same reachability expression to the designated final gate preserves the converged output.

For the converse representation direction, expand each finite union expression in the reduced system as a binary union tree (or an allowed cyclic union subnetwork), and use one intersection gate for each reduced counted equation. Cyclic dependencies between the `X_i` are permitted by the source model. The accumulating least-fixed-point semantics is therefore exactly the reduced closure system, and the number of intersection gates remains `k`.

## Counterexample-first hostile controls

The predeclared failure criterion was any finite cyclic system whose converged target changes after OR-reachability elimination. In addition to the proof argument, a bounded exhaustive calibration was run on a two-element ground set with generators `{0}` and `{1}`. Every syntactic system with one, two, or three gates, arbitrary gate-to-gate/generator operands, and arbitrary union/intersection labels was checked against the reduction; this covered `18 + 1,024 + 125,000` systems and found `0` target mismatches. The enumeration includes pure union SCCs, self-feedback, mutual feedback, counted-to-union-to-counted cycles, and multi-iteration activation. This computation is support only, not proof.

## What changed

The prior residual asked for a source-native property of a shared `t`-intersection cyclic system. This lemma removes a representation ambiguity: an admissible future property may be defined on the `k` counted meet nodes together with their generator/meet-source union expressions, rather than on arbitrary uncounted union-node presentation details.

This is stronger than merely closing the original generator family under free unions (the pending PR #113 proposal): it eliminates **all internal union nodes**, including union SCCs that carry counted outputs through feedback paths. PR #113 remains pending/non-main and supplies no authority to this result.

## What did not change

No lower-bound potential `Phi` was produced. No theorem of the form `Phi <= f(k)` was proved for a useful target statistic. No explicit graph was shown to have super-logarithmic cover complexity. No circuit lower bound and no `P != NP` bridge closed.

The remaining **local-to-global/gluing residual** is:

> On the exact join-eliminated `k`-meet normal form, find a presentation/quotient-respecting property `Phi` with a proved universal upper bound as a function of `k`, survive C010/C021/C023/C024/C025 hostile controls, and prove a super-logarithmic value on an explicit graph family.

Root status remains `OPEN_NO_SOLUTION_CERTIFICATE`.
