# Same-context expert cell — RH-ANA-003 pre-candidate review

**Authority:** proposal/search governance only. This is not independent mathematical review and grants no theorem authority.

**Frozen fibre:** `sha256:31e2fc6491b0b61f8e7b7b96c668592b860b37166dc84e12cb488b3a19bb985d`.

## Cell composition and delegated roles

**Expert A — zero-density / zero-free analytic number theory.** Background: Dirichlet polynomials, zero-detection, zero-density estimates, zero-free regions. Role: audit exactly what current density theorems say about integer zero occupancy and identify the strongest non-circular conversion target.

**Expert B — zeta moments, mollifiers and resonance.** Background: mean values, mollifiers, resonance/large-values methods for zeta and L-functions. Role: test whether large-value/mollifier information can plausibly sharpen a cumulative density estimate into a blockwise exclusion theorem without importing a zero-location hypothesis.

**Expert C — explicit formulas, Li/Weil positivity and prime-zero duality.** Background: Weil explicit formula, Li coefficients, prime-power/archimedean decompositions, transform/convergence audits. Role: ask whether a density estimate controls the signed all-index remainder needed by RH-ANA-003, and identify any hidden transform or sign assumption.

**Expert D — proof, provenance and falsifier audit.** Background: proof DAGs, integer-count arguments, source/assumption tracking, adversarial near-misses. Role: enforce the exact RH root contract, candidate chronology, numerical-evidence boundary, and the `<1` threshold needed to infer emptiness from an upper bound.

## Round 1: findings

Expert A: Guth–Maynard 2026 materially improves the uniform exponent to `30/13`, but the resulting `T^(30(1-sigma)/13+o(1))` grows for every fixed `sigma<1`. Bellotti's explicit log-free estimates near one are similarly density bounds, not zero-occupancy statements. Mossinghoff–Trudgian–Yang gives exact exclusion only in a height-dependent region adjacent to `sigma=1`.

Expert B: the large-value machinery is optimized to upper-bound how often large Dirichlet-polynomial values/zero detectors occur. Nothing in the source theorem turns the count into `<1` on each tail block. A new mollifier or resonance inequality would be relevant only if it creates a genuinely local exclusion or a contradiction from even one off-line zero; merely improving the density exponent remains on the same saturated semantic axis.

Expert C: RH-ANA-003 needs an all-index prime/archimedean cancellation or tail mechanism. A zero-density theorem can constrain an aggregate zero contribution, but an all-index Li/Weil sign conclusion would require a rigorously justified transform and a bound strong enough after the relevant weights are applied. Importing a signed cancellation that already excludes off-line zeros would simply move the root assumption. The first useful test is therefore not another prime truncation but a source-bound count-to-exclusion threshold.

Expert D: because the relevant occupancy count is integer-valued, a direct upper-bound certificate of emptiness needs a strict `<1` bound for the exact local region being excluded. A finite verified prefix plus a cumulative `O(T^a)` tail bound does not meet that gate. Even `O(1)` with constant at least one permits finitely many off-line zeros. A proportion tending to zero permits sparse infinite exceptions.

## Round 2: cross-examination

A challenged D: could an asymptotic density theorem still imply eventual zero-freeness without an explicit `<1` numerical bound? D: yes only if its exact mathematical conclusion forces the relevant local count to tend to zero; since the count is integer-valued, eventual `<1` follows. Current cited bounds do not have that behavior for any fixed `sigma<1`.

B challenged A: could the zero-free region plus density estimate cover the whole right half of the critical strip after finite verification? A: no. The zero-free boundary approaches `1` as height grows; it excludes a shrinking neighborhood of `1`, while density bounds leave positive occupancy allowance in the remaining fixed half-strip.

C challenged B: could a mollifier detect a single off-line zero with an amplified contradiction even when density is large? B: that is a distinct mechanism and remains admissible. It would have to be derived as a new zero-detection/exclusion theorem; the current density exponent alone supplies no such contradiction.

D challenged C: can density be inserted into a Li/explicit-formula sum and sign-controlled by averaging? C: only after freezing the exact weights, sum/interchange order, archimedean terms and a uniform remainder theorem. Average cardinality control does not itself bound the signed weighted contribution needed for every `n`.

## Consensus search-policy decision

1. Do **not** invent a new positivity inequality yet.
2. First prove and source-audit a minimal **density-to-exclusion conversion lemma**: identify exactly what kind of global or local count bound would be sufficient, and test current primary-source bounds against that threshold.
3. Use the Platt–Trudgian height only as a finite-prefix calibration; no numerical extension is selected.
4. Retain mollifier/resonance and explicit-formula weighting as reopened alternatives only if they add a mechanism that changes the occupancy threshold, not merely the density exponent.
5. If current bounds fail the threshold, record a typed obstruction scoped to the **standalone density/zero-free + finite-prefix combination**, not a universal impossibility theorem about all future zero-density methods.

**Unresolved after same-context review:** whether a local zero-detection theorem derived from current large-values methods can force a contradiction from a single off-line zero; whether prime/archimedean weights in the exact Li formula can convert sparse-density information into a stronger signed tail statement. These remain future atoms/candidates, not assumptions.