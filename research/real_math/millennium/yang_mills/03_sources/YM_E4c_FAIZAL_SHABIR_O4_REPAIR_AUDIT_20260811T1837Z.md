# YM-E4c primary-source repair audit — O(4) restoration

**Authority:** `PROPOSAL_SHADOW_SOURCE_AUDIT / NO_THEOREM / NO_ROOT_AUTHORITY`  
**Atom:** `YM-E4c`  
**Prospective contract:** RAKL_math issue #141, frozen before this repair probe.  
**Primary source:** Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1 (9 June 2026), `https://arxiv.org/pdf/2606.19362`.

## Question

Can the written Proposition 4.6 proof be repaired, from the source itself, so that the finite-cutoff Schwinger functions admit an `O(a_k^alpha)` arbitrary-rotation defect and hence the same subsequential continuum Schwinger family satisfies full `O(4)` invariance?

The audit deliberately separates two obligations:

1. **local scaling:** the raw lattice sum must actually tend to zero with the displayed normalization; and
2. **representation/gluing:** the arbitrary continuum rotation used in the comparison must be a defined operation on the same finite-lattice gauge configuration/observable system, or be replaced by an explicit approximation/comparison map.

Either can block OS1 restoration independently.

## Exact source surfaces checked

The bounded audit used the current arXiv v1 PDF and checked:

- p. 82, Section 7.2: the short finite-hypercubic-symmetry argument;
- pp. 484-487, Lemma 4.5 and Proposition 4.6, especially equations (4.31), (4.33), (4.36), (4.42), (4.46)-(4.51);
- p. 5 and p. 511: the hypercubic lattice, oriented-bond and link-field configuration-space definitions;
- full-text searches for an interpolation/pullback defining arbitrary `O(4)` action on the link configuration space, including searches around `g^{-1}·A`, `rotated insertion`, `interpolated gauge field`, `lattice automorphism`, and `O(4) action`.

Mandatory PDF screenshot attempts were made on the relevant PDF pages. The screenshot backend returned `Cache miss` for pp. 485-487. This is recorded as `CANNOT_CHECK_SCREENSHOT_BACKEND`; the parsed primary PDF text was available and was used for the equation/domain audit. No visual-only claim is made.

## Finding A — the normalization repair is not present in the displayed chain

Equation (4.42) bounds the defect by a sum over `x in a_k Z^4` of terms with an `O(1)` exponential envelope. Equation (4.46) carries the corresponding unnormalized lattice sum into the Schwinger-function comparison. Equation (4.47) then estimates that sum by `C_6 a_k^{-4}` times a continuum integral. Equations (4.48)-(4.49) bound that continuum integral by `C_9 a_k` using the thickness of the slab symmetric difference.

Therefore the literal composition of (4.47) and (4.49) yields only an upper bound of order

`a_k^{-4} * a_k = a_k^{-3}`,

not the `O(a_k)` estimate asserted in (4.50). The source segment between these displays does not insert a compensating `a_k^4`, normalized counting measure, cancellation, or smaller per-site amplitude.

This verifies the arithmetic residual already frozen in issue #141. It is not counted as new semantic novelty in this cycle.

## Finding B — arbitrary `O(4)` rotation is not type-checked on the finite lattice

This repair probe exposed a distinct source-local representation defect.

The paper's standing lattice definitions place gauge variables on oriented coordinate bonds of the hypercubic lattice `a_k Z^4`; equivalently a finite-scale gauge field is an assignment of `SU(N)` elements to the bond set. Exact geometric symmetries of this configuration space are therefore lattice automorphisms (translations and the finite hypercubic rotation/reflection group), not arbitrary elements of continuous `O(4)`.

Nevertheless Proposition 4.6 takes every `g in O(4)`, writes a rotated insertion in equation (4.36) as `W_{sigma,k}(g^{-1}·A)`, states that the uninserted finite-lattice measure is `O(4)`-invariant, and then uses that premise in equation (4.37). For a generic rotation `g` that does not preserve `a_k Z^4` and its coordinate bonds, the paper segment does not define `g^{-1}·A` as an element of the same link-field configuration space.

The bounded full-text search located no separate interpolation-extension-restriction construction, no arbitrary-rotation pullback on link fields, and no comparison theorem that replaces exact finite-cutoff `O(4)` invariance by an asymptotically equivariant map. The source itself elsewhere refers to the exact finite-scale symmetry as the **discrete Euclidean group** and Section 7.2 separately invokes the finite hypercubic group.

Accordingly, equations (4.36)-(4.37) are not source-bound for arbitrary `g in O(4)` under the paper's own finite-lattice field definition. This is independent of the `a_k^{-4}` normalization mismatch.

**Scoped failure ID (proposal/shadow):** `F-YM-E4C-ARBITRARY-O4-LATTICE-ACTION-UNBOUND`.

**Scoped obstruction ID (proposal/shadow):** `O-YM-E4C-O4-ACTION-DOMAIN-GLUING`.

This does not prove that rotational invariance cannot be restored. A repair could define an explicit continuum interpolation or lattice approximation to each fixed rotation and prove an error tending to zero. What fails here is the written finite-cutoff identity used by this proof route.

## DifferenceWitness: exact lattice symmetry vs continuum `O(4)`

Shared structure: both act geometrically on Euclidean observables and should preserve gauge-invariant continuum correlation functions.

Load-bearing difference: a generic `g in O(4)` sends coordinate edges to non-coordinate directions and does not map the hypercubic bond set to itself. Thus exact invariance under the hypercubic subgroup cannot be substituted for a defined arbitrary-rotation action. The continuum target can still be recovered only through an explicit approximation/restoration theorem whose error is uniform in every other limit parameter used downstream.

This DifferenceWitness blocks the silent transfer but does not blacklist an interpolation-based repair.

## Same-context expert cell

These role-separated checks use the same evidence and **do not count as independent reviews**.

1. **Constructive QFT / OS reconstruction.** Full Euclidean covariance is a root-facing OS obligation. The local proof gap matters only through the same limiting Schwinger family; it does not alter the already-separate spectral-gap, nontriviality or UV obligations.
2. **Lattice gauge geometry / RG scaling.** Hypercubic link fields have only discrete exact spacetime rotations. The displayed Riemann-sum scaling loses `a_k^{-4}` unless a source-level density normalization or cancellation is supplied.
3. **Functional analysis / continuum symmetry.** A valid repair can use approximate actions `R_{k,g}` rather than exact finite-scale symmetry, but it must prove convergence/equicontinuity strong enough to pass the symmetry identity to the chosen subsequence.
4. **Gauge-covariant observable representation.** Any interpolation must preserve the intended gauge-invariant observable content and make domains/codomains explicit; an off-lattice continuum rotation cannot be applied to link variables by notation alone.
5. **Adversarial source verification.** Two independent hostile checks survive: literal exponent arithmetic `(a_k^{-4})(a_k)` and a generic irrational-angle rotation that does not preserve the bond set.
6. **RAKL v3 assurance / metrology.** Issue #141 is the durable prospective contract; this audit adds a new source-bound representation/gluing failure but gives no theorem, independent-review, or root-promotion authority.

Consensus: `PROPOSITION_4_6_REPAIR_NOT_SOURCE_BOUND / TWO_INDEPENDENT_RESIDUALS / OS1_GLUING_OPEN`.

## Local mathematical failure vs local-to-global failure

- **Local source-proof failure A:** missing normalization/cancellation in the sum estimate.
- **Local source-proof failure B:** arbitrary-rotation action on the finite link configuration space is unbound.
- **Local-to-global/gluing failure:** because either local step is unresolved, the proof does not currently establish full `O(4)` invariance of the same subsequential continuum Schwinger family, so OS1 remains unclosed along this route.

No conclusion is drawn about the truth or falsity of the full Yang-Mills construction beyond this proof interface.

## Repair contract after this audit

A viable next candidate must source-bind **both** coordinates, not just one:

1. replace the raw sum by a normalized density estimate, a proved per-site `O(a_k^4)` amplitude, or a genuine cancellation yielding `O(a_k^alpha)` with `alpha>0`; and
2. define a typed approximate rotation/comparison map on the lattice gauge/observable system for every fixed `g in O(4)`, prove gauge compatibility and the required locality/support bounds, and show its comparison error vanishes uniformly on the exact finite/infinite-volume and continuum subsequence used for OS reconstruction.

Only after both close can the result be glued to the continuum OS1 claim. Reflection positivity, OS Hilbert-space identification, source completeness, spectral-gap transport, nontriviality and asymptotic freedom remain separate obligations.

## Negative-history boundary

The repeated `YM-E1a1a0` Bałaban primary-source-acquisition cycles in PRs #85/#103/#116 were consulted as process history. Their repeated zero-semantic-novelty metadata-only acquisition route changed routing away from another copy of that search and toward the current same-theory constructive-continuum source repair. Their mathematical obstruction is not reused here.

The OS quotient/domination work in #126/#133 and draft PR #140 was also consulted but rejected as a direct mathematical transfer: it concerns varying OS null quotients/relative form bounds, while `YM-E4c` concerns Euclidean-rotation representation and scaling. The shared label `gluing` is insufficient for transfer.

## Root boundary

Root issue #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`. No continuum existence theorem, nontriviality proof, OS reconstruction certificate, physical mass-gap certificate, closed proof DAG, verifier/dependency/axiom audit, isolated recheck, bounded novelty certificate, or independent mathematical review is produced here.
