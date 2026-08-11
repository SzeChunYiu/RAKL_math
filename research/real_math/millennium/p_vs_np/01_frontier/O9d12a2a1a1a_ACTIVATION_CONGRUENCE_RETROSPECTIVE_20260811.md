# O9d12a2a1a1a — retrospective activation-congruence audit

**Date:** 2026-08-11  
**Parent:** `O9d12a2a1a1` (open PR #49)  
**Authority:** `RETROSPECTIVE_SOURCE_BOUND_ROUTE_DIAGNOSTIC / EXACT_LOCAL_SEMANTIC_LEMMA / NO_PRE_CANDIDATE_CREDIT / NO_LOWER_BOUND_CANDIDATE / ROOT_AUTHORITY_NONE`  
**Framework read first:** `SzeChunYiu/RAKL@decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8`  
**Application branch parent:** `SzeChunYiu/RAKL_math@3ccdcc51aa312af8b8288ff7cf6f4a681966d1fd`

## Chronology boundary

The projection/congruence insight below was obtained during this source audit before a fresh
`O9d12a2a1a1a` strict context packet was frozen. It is therefore permanently ineligible for
strict context-first candidate credit. It is recorded as retrospective route evidence and a
proposal-only v3 experience episode. The result may change search priority and atomization only.

## Source-bound question

Cavalar--Oliveira's Theorem 24 constructs, for a fixed cover witness

\[
\Lambda=\{(E_i,H_i)\}_{i=1}^t,\qquad E_i,H_i\subseteq U=A^c,
\]

the least upward-closed family `G_w` forced above a witness `w`, starting from generator
traces and repeatedly applying

\[
E_i,H_i\in G_w\Longrightarrow E_i\cap H_i\in G_w.
\]

PR #49 showed that in the normalized `G_NEQ` calibration this dynamics collapses to one-step
signature XOR, and opened the source-general question: is later closure activation genuinely
richer than a source-defined first-order projection?

Primary source: Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and
Two-Dimensional Cover Problems*, ECCC TR25-033 / arXiv:2503.14117 (2025), Definitions
18--21 and Theorem 24.

## Result 1: the coarse fired-pair vector is not a congruence

A projection that records only whether both antecedents of each rule are present initially is
too coarse.

Let

\[
\Gamma=\{a,1,2,3\},\quad A=\{a\},\quad U=\{1,2,3\},
\]

with generators

\[
\mathcal B=\{\{a,1\},\{a,3\},\{1,2\},\{2,3\}\},
\]

and rules

\[
(E_1,H_1)=(\{1,2\},\{2,3\}),\qquad
(E_2,H_2)=(\{2\},\{1,3\}).
\]

For `w=a`, the base family is the upward closure of `{1}` and `{3}`. For `w=2`, the
base family is the upward closure of `{1,2}` and `{2,3}`. In both states the initial
"both antecedents present" vector is `(1,0)`.

However:

- above `a`, rule 1 adds `{2}`; `H_2={1,3}` was already present, so rule 2 then adds
  `emptyset`;
- above `2`, rule 1 also adds `{2}`, but `H_2` is absent, so rule 2 never fires.

The family `Lambda` is a valid cover witness for the single target element `a`: every
semi-filter above `a` must contain `{1}` and `{3}`, hence `E_1,H_1`; preservation forces
`{2}`, while upward closure already gives `H_2`; preservation of rule 2 would force
`emptyset`, contradicting the semi-filter definition.

So first-stage rule firing alone loses load-bearing latent antecedent membership.

## Result 2: antecedent-membership projection is a congruence

Let `G_w^(0)` denote the Theorem-24 base family after generator seeding and upward closure.
Define the source-native projection

\[
\pi_\Lambda(w)=
\left(
 b_w,\,
 x^E_1,x^H_1,\ldots,x^E_t,x^H_t
\right),
\]

where

\[
b_w=\mathbf 1[\varnothing\in G_w^{(0)}],\qquad
x^E_i=\mathbf 1[E_i\in G_w^{(0)}],\qquad
x^H_i=\mathbf 1[H_i\in G_w^{(0)}].
\]

For fixed `Lambda`, also freeze its containment matrix: for every rule consequent
`C_i=E_i intersect H_i`, record which antecedents `E_j` and `H_j` contain `C_i`.

Then the complete rule-activation dynamics are determined by `pi_Lambda(w)` and this fixed
matrix.

Indeed, whenever rule `i` fires, Theorem 24 adds `C_i` and every superset of `C_i`. Therefore
an antecedent `E_j` becomes present exactly when it was already present or some fired
consequent `C_i` satisfies `C_i subseteq E_j`; likewise for `H_j`. This defines a monotone
Boolean update map on the `2t` antecedent bits. Induction over propagation rounds shows that
the projected full closure at every round equals the corresponding iterate of this Boolean
map.

Consequently, for two witnesses `w,w'` with equal `pi_Lambda`, all later rule firings are
identical. Moreover `emptyset` appears terminally iff either `b_w=1` already or some
eventually fired rule has `E_i intersect H_i=emptyset`.

Thus equal antecedent-membership projections are a congruence for the fixed-point recurrence.

### Scope

This does **not** say the raw terminal families `G_w` are equal: they can still differ on
sets that are irrelevant to every rule antecedent/consequent. It says those raw differences
do not alter the Theorem-24 propagation computation unless a new source-bound bridge shows
why such non-rule state carries cover-complexity information.

This also does not prove any circuit lower bound or any global capacity theorem. It only
removes a proposed source of "higher-order" witness-local activation information.

## Route effect

The child question from PR #49 asked whether later activation contains a genuine distinction
beyond a source-defined first-order projection. For the exact antecedent-membership
projection above, the answer is:

`NO_LATER_ACTIVATION_DIFFERENCE_BEYOND_FIXED_LAMBDA_PROJECTION`.

The useful remaining coordinate, if any, must live outside witness-local rule activation.
Candidate directions that remain logically open include:

1. global incidence geometry between many semi-filters and the selected pair family `Lambda`;
2. structure of the pair-containment/rule graph itself as `Lambda` varies;
3. multi-witness or multi-semi-filter correlations not reducible to one `pi_Lambda(w)`;
4. a source-bound quantity that charges pair selection globally while retaining a proved
   per-fusion budget.

A fresh child must freeze context before testing any of these.

## Expert-cell disposition

Six same-context roles were used.

1. **Circuit/fusion specialist:** accepted the specialization of Definitions 18--21 and
   Theorem 24; blocked any reversal of the upper construction into a lower bound.
2. **Closure/Horn specialist:** derived the antecedent-membership monotone recurrence and
   accepted congruence of the projected dynamics.
3. **Adversarial lower-bound specialist:** supplied the two-rule counterexample showing that
   the coarser fired-pair vector is insufficient; warned that raw `G_w` differences remain
   uncharged.
4. **Information/representation specialist:** classified the result as a representation
   compression of witness-local activation, not a hardness certificate.
5. **Formal assurance/provenance specialist:** marked the result retrospective because it
   preceded any fresh child context freeze; no strict candidate chronology is claimed.
6. **RAKL-method observer:** identified the positive research motif
   `source-defined projection -> cheapest congruence test -> prune representation before
   candidate invention`.

These are same-context analytical roles, not independent review.

## Saturation / novelty disposition

This episode retains novelty on `RELATION` and `OBSTRUCTION`: it identifies the exact
relation between source closure propagation and a finite antecedent state, and reopens the
root-critical obstruction outside witness-local activation. The current closure-activation
`PATH` is pruned rather than globally saturated; no absolute completeness claim is made.

The P-vs-NP root remains unresolved, so v3 problem-novelty classification is
`UNRESOLVED`. The local subproblem is a source-derived/compositional clarification rather
than evidence of a new mathematical operator.

## Next fresh atom

Open `O9d12a2a1a1b — GLOBAL_COVER_INCIDENCE_BEYOND_WITNESS_ACTIVATION`.

Exact question:

> After quotienting witness-local Theorem-24 propagation by the antecedent-membership
> congruence, is there a source-defined global incidence/correlation object over the full
> semi-filter cover graph whose value is not determined by independent witness signatures,
> has a proved bounded change under one legal fusion/pair selection, and survives the
> all-rectangle zero-cover, C010 multiplexing, C021 cheap-adjacency, C023 scalar-collapse,
> C024 integrality, C025 signature and XM004 raw-volume controls?

Candidate generation remains blocked until a fresh context, transfer matrix, expert review,
dual-memory review and hash-chained trace are frozen.
