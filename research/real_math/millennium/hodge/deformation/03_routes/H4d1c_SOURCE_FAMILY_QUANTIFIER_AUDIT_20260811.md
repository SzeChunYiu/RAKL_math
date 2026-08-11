# H4d1c source-family quantifier and fixed-witness diagnostic audit

**Date:** 2026-08-11  
**Cycle:** `H4d1c-C001-SOURCE-FAMILY-QUANTIFIER-AUDIT`  
**Authority:** `SOURCE_BOUND_REPRESENTATION_ROUTE_NORMALIZATION / PROPOSAL_SHADOW / NO_HODGE_THEOREM / ROOT_AUTHORITY_NONE`

## Frozen question

H4d1b normalized direct first-order obstruction vanishing to actual fixed-witness
first-order liftability when the obstruction theory is complete. The surviving
H4d1c residual therefore asks for independent geometry forcing

`dπ_α|_(w0): T_(w0)W_α -> T_(s0)T`

to be surjective for one chosen central witness `w0`.

Before searching for such a theorem in a new family, this cycle audits a prior
question: **is failure of that fixed-witness test a source-complete negative
diagnostic for the algebraicity obligation that the deformation lane is trying
to propagate?**

The answer is no without extra source-family hypotheses.

## Four typed obligations

Keep the following statements distinct.

1. **Fixed-witness infinitesimal reachability `F(w0)`.** One preselected
   representative `w0` lifts every first-order branch direction:
   `dπ_(w0)(T_(w0)W)=T_(s0)T`.

2. **Source-family directional reachability `D`.** For every
   `v in T_(s0)T`, there exists *some* admissible central representative
   `w_v` and a tangent lift mapping to `v`.

3. **Source-component/branch coverage `C`.** Some admissible source component,
   or a controlled finite-type source family, dominates/covers the relevant
   branch in the sense actually needed by the variational argument.

4. **Compatible formal/algebraic propagation `G`.** Witnesses can be chosen
   compatibly through higher Artin orders and then algebraized, with rational
   coefficients, component switching, monodromy and singular degeneration
   controlled.

`F(w0)` is an `exists w0 / for every v` statement. `D` is a
`for every v / exists w_v` statement. The converse quantifier swap is not
formal. More importantly, neither `D` nor pointwise fiberwise existence gives
`G` without a gluing/compatibility theorem.

## Counterexample-first DifferenceWitness

Use the abstract source projection

`q: A^1_C -> A^1_C,  q(t)=t^2`.

It is surjective on complex points and dominant, but `dq_0=0`. Thus source
coverage or component dominance can coexist with failure of tangent
surjectivity at the selected special source point.

This is **not** a Hodge counterexample. It is a representation-level
DifferenceWitness. It blocks the inference

`fixed central tangent test fails => the branch has no algebraic witnesses`.

That inference needs additional hypotheses such as a distinguished smooth
source point, source smoothness/submersivity, or a theorem making the selected
component complete for the target witness category.

## Source-family completeness is a separate obligation

The rational Hodge root is an existence statement for algebraic cycle classes.
A deformation proof may choose a particular central geometric representative,
but the root contract does not canonically privilege that representative.

Accordingly, a negative fixed-witness result has only fixed-source authority
unless one proves that the chosen Hilbert/Chow/flag source is complete for all
admissible rational signed representatives relevant to the branch.

For signed rational cycles this source interface must preserve coefficients
after denominator clearing and must not silently replace a finite signed
combination by a single effective Hilbert point. No general boundedness or
finite-component theorem for the exact admissible source family is present in
the frozen H4d1c fibre. It must be supplied rather than assumed.

## Primary-source controls

### Bloch--Esnault--Kerz

Bloch, Esnault and Kerz formulate an infinitesimal variational-Hodge problem at
the level of rational `K_0` classes on formal thickenings. Under their stated
Chow--Künneth hypotheses, a Hodge-filtration condition is equivalent to the
existence of a compatible formal `K_0` pro-class. This is a useful
**representation control**: a deformation target can naturally live at class
level rather than as one fixed geometric support.

The same paper explicitly isolates algebraization as an additional problem and
shows that the map from global `K_0` to the inverse limit over thickenings is not
surjective in general. Therefore class-level formal lifting must not be credited
as algebraization.

Source: Spencer Bloch, Hélène Esnault, Moritz Kerz,
*Deformation of algebraic cycle classes in characteristic zero*,
arXiv:1310.1773, Theorem 1.2 and the discussion around equation (1.3).

### Kloosterman

Kloosterman's variational-Hodge theorem for complete-intersection cycles on
hypersurfaces remains a positive special-family control. It shows that explicit
flag-Hilbert/source geometry can make a fixed-source route powerful. It does
not supply a general source-completeness theorem for arbitrary smooth
projective rational cycles.

Source: Remke Kloosterman,
*Variational Hodge conjecture for complete intersections on hypersurfaces in
projective space*, arXiv:2104.14845.

### Complete obstruction semantics

Stacks Project Tag 07YG is retained only for the H4d1b normalization: in that
definition a complete obstruction vanishes iff a lift exists. It does not turn
a fixed-witness lifting problem into a source-complete algebraicity problem.

## Same-context expert-cell synthesis

The role-separated review is recorded separately. Consensus:

- keep H4d1c as a potentially useful **sufficient special-source mechanism**;
- do not treat failure at one chosen witness as a source-complete obstruction;
- open a source-family-complete child before using negative fixed-witness
  evidence to rotate the whole geometric/deformation lane;
- keep pointwise/source coverage, higher-order compatible lifting and
  algebraization as separate arrows.

These roles are same-context analytical passes, not independent review.

## Verdict

`PARTIAL_SUCCESS / REPRESENTATION_AND_PATH_NORMALIZATION`.

The fixed-witness H4d1c target is not rejected. Its authority is narrowed:
success can be valuable in a source-specific family, but failure cannot by
itself rule out algebraicity supplied by another representative/source
component or by a broader class-level source representation.

This is route governance, not a theorem about the rational Hodge conjecture.

## Residual opened

`H4d1c1-SOURCE-FAMILY-COMPLETE-LOCAL-ALGEBRAICITY-BRIDGE`.

The next source-complete atom must type the admissible source family and ask
which additional boundedness/properness/component-control hypotheses can turn
existential source coverage into a compatible geometric or formal family. It
must then audit higher Artin compatibility and algebraization separately.

The existing fixed-witness H4d1c special-family search may continue in parallel,
but a negative result there is no longer allowed to close the source-complete
path.

## Local versus gluing failures

**Local representation/decomposition failure:** a selected-witness
first-order tangent test has stronger/different quantifiers than the existential
source-family obligation.

**Local-to-global/gluing failure:** even if every direction or nearby fiber is
covered by some source, the witnesses may switch components and need not form a
compatible Artin tower or algebraize. Bloch--Esnault--Kerz provide a primary
control showing exactly why formal class lifting and algebraization must remain
separate.

## Novelty status

RAKL novelty class: `representation`. No theorem novelty and no new primitive
operator is claimed; structural novelty rank is `0`. The retained value is the
source-quantifier obstruction, the relation between fixed-source and
source-family conditions, and the corrected routing path.
