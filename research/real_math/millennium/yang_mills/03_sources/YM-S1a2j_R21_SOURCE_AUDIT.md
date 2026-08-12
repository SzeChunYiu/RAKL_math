# YM-S1a2j R21 — relevant-block inverse/conorm and graph-norm audit

Authority: **PROPOSAL/SHADOW ONLY**. Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`. This is a scoped source/proof-interface audit of Jonathan J. Wilson's 2026 author-uploaded Yang–Mills manuscript. It is not a Yang–Mills counterexample, not a source-wide refutation, not independent mathematical review, and not a continuum or physical-gap certificate.

## Chronology and strict-credit correction

The atom and fibre were frozen before the consequential source discriminator. However, after source retrieval the serialized pre-action receipt was independently re-hashed and its declared `receipt_canonical_sha256` was found not to equal the canonical hash of the receipt content. Current RAKL derives prospective chronology from the content-bound pair; therefore this run **does not claim strict prospective credit** for the source findings. The frozen file is left immutable. A separate append-only correction records `RETROSPECTIVE_BINDING_REFUTED` for strict metrology. The findings below remain useful proposal/shadow experience and source diagnosis only.

## Primary source boundary

Primary author-uploaded/indexed text inspected: Jonathan J. Wilson, *Rigorous Construction of Four-Dimensional Yang–Mills Quantum Field Theory Via Gribov–Zwanziger Quantization and Renormalization Group Analysis: Measure-Theoretic Foundations, Spectral Properties, and the Mass Gap* (2026), ResearchGate record 399279692 / DOI `10.13140/RG.2.2.22056.43527`, especially Sections 30.2, 30.6–30.7, 37.3, 38.2 and Appendix A.15.2.

The ResearchGate index exposed equation-level text, including (529)–(535) and (573)–(580), but a screenshot-capable `application/pdf` view was not acquired. Direct page opening failed. Consequently page-visual verification is `CANNOT_CHECK`; no formula absent from the indexed author text is reconstructed from memory.

## D1 — equation (534) is an operator-norm lower bound, not a conorm/inverse bound

The source defines a finite basis of local monomials spanning a relevant/marginal subspace and a linearized coupling map `L_k`. It then states a spectral splitting whose displayed relevant estimate is

`||L_k|_rel|| >= lambda_rel > 1`,

while the irrelevant estimate is an operator-norm upper bound `< 1`. The relevant inequality controls only the **largest** amplification in the chosen norm. In dimension greater than one it does not imply that every relevant vector expands, that the restriction is injective, or that the inverse is contractive.

Exact hostile control: for

`A_M = [[2,M],[0,2]]`,

both eigenvalues equal `2`, but

`A_M^{-1} e_2 = (-M/4, 1/2)`.

Hence `||A_M^{-1}|| >= sqrt(M^2/16+1/4)`, which exceeds `1` for, e.g., `M=4` and grows without bound with `M`. A forward spectral/eigenvalue statement therefore cannot substitute for the graph-transform quantity `m(A_k)>1` or `||A_k^{-1}||<1` in a fixed norm.

This control is standard linear algebra and carries no mathematical novelty claim.

## D2 — the source leaves a genuine one-dimensional rescue open, so D1 is not by itself a refutation of the target graph step

A one-dimensional invariant relevant block is different: if `L_k|_rel` is multiplication by a scalar and `|L_k| >= lambda_rel > 1`, then its inverse has norm at most `lambda_rel^{-1}<1`. The source contains statements that make this rescue plausible in one representation: Appendix A.15.2 says the only relevant **quadratic** operator in that lattice gauge classification is the mass term.

Therefore the nonnormal matrix control is a falsifier of the *general inference form*, not a proof that Wilson's actual relevant block lacks an inverse contraction. The decisive missing binding is the identity/cardinality of the exact relevant subspace used in Sections 30.6/30.7 and 38, together with invariance of that subspace under the same `L_k` and the graph metric.

## D3 — the manuscript's relevant-sector descriptions are not source-internally aligned enough to invoke the one-dimensional rescue

The exposed text uses several materially different descriptions:

1. Section 30.2 says there are no relevant operators in pure Yang–Mills, with the mass term forbidden by gauge invariance up to Gribov effects.
2. Section 30.6 nevertheless introduces `A_rel`, states the norm lower bound (534), and Theorem 30.6 gives a stable manifold of codimension `|A_rel|`.
3. Appendix A.15.2 says the only relevant quadratic operator is the mass term, while the kinetic term is marginal.
4. Section 37.3 describes the finite GZ relevant/marginal counterterm sector in a different symmetry/counterterm language.
5. Section 38 writes `u_k=(g_k,lambda_k)` with `lambda_k in R^{m-1}` collecting the remaining relevant/marginal coordinates, and its displayed update (580) assumes only that `||A_k||` is uniformly bounded. The graph-transform step then says the noncontracting finite-dimensional relevant sector is controlled by tuning, without displaying a relevant inverse/conorm constant.

These statements do not, on the acquired source surface, identify the exact `A_rel` used by the Section-30 graph with a one-dimensional mass coordinate and then identify that same coordinate with the relevant subblock inside Section-38 `lambda`. Nor do they supply a uniformly equivalent adapted norm or exponential-dichotomy estimate that would make the inverse margin explicit.

Accordingly the R21 discriminator is **partially resolved**: the broad request for an inverse factor is sharpened to a representation-binding question. Either the actual relevant block is source-bound as one-dimensional/scalar with a uniform multiplier bounded away from one, or a genuine conorm/inverse/adapted-norm estimate is needed. The exposed equation (534) alone is insufficient in the general finite-dimensional reading.

## Structural analogue / DifferenceWitness

Nonautonomous stable-manifold and exponential-dichotomy literature is structurally relevant because it separates stable and unstable evolution and uses quantitative dichotomy estimates; some formulations allow the full dynamics to be noninvertible while retaining invertibility along the unstable direction. This supports the *type* of missing target obligation. It does not transfer a theorem to Wilson's RG map: the target has a scale-dependent `O(g^2)` domain, GZ/gauge/regulator constraints, source-specific Banach norms, and downstream same-theory OS/continuum requirements.

The Brydges–Slade rigorous RG programme is a second near analogue: it proves model-specific contraction of a nonperturbative/irrelevant coordinate under explicit hypotheses. It does not provide the target relevant inverse block, graph metric, or GZ/OS glue.

## Same-context expert-cell synthesis

- **Rigorous lattice-gauge/RG:** equation (534) must be interpreted in the exact `Loc_k` coupling basis and same regulator norm; do not infer a stronger block estimate from the word “spectral”.
- **Nonautonomous invariant manifolds:** a graph transform across an unstable coordinate needs a backward/inverse or equivalent dichotomy estimate; if the unstable block is one-dimensional, the burden is much smaller but still must be source-bound.
- **Banach/operator theory:** operator norm lower bound is not conorm; nonnormality is the cheapest hostile near miss. A one-dimensional invariant block is the important exception.
- **Adversarial falsification:** the matrix control rejects the multi-dimensional inference but intentionally does not reject the one-dimensional rescue.
- **Formal assurance:** exact statement must bind subspace identity, dimension, norm, scale/regulator quantifiers, invertibility and contraction constant.
- **OS/continuum gluing:** even a successful local graph repair would not identify a gauge-invariant OS Hilbert space, physical Hamiltonian gap, lattice-spacing-uniform mass, or continuum state.
- **Novelty/metrology:** the linear-algebra fact is stored knowledge; the only candidate retained value is source-scoped diagnosis/representation localization.

These roles share context and earn `0/3` independent mathematical-review credit.

## Local vs local-to-global failure ledger

**Local mathematical/source-proof residual:** exact identity/cardinality of the Section-30 relevant block and its map into Section-38 `lambda`; if dimension >1, uniform conorm/inverse/adapted-norm estimate; if dimension =1, scalar multiplier and uniform inverse margin; cross-derivative terms in the actual graph metric; base-map `g -> g'` inversion and shrinking next-radius invariance remain separately open from R20.

**Local-to-global/gluing residuals (unchanged):** cross-regulator stable-graph/slaving estimate; same-theory gauge-invariant/reflection-positive OS source algebra; volume/lattice-spacing uniform physical normalization; transfer/Hamiltonian identification; continuum spectral identification. No local graph result is promoted across these interfaces.

## Outcome

`PARTIAL_SUCCESS_SOURCE_SCOPED_REPRESENTATION_BINDING_OBSTRUCTION / RETROSPECTIVE_SHADOW_ONLY`.

Residual-before: `RELEVANT_BACKWARD_GRAPH_CONTRACTION_UNBOUND`.

Residual-after: `RELEVANT_SECTOR_IDENTITY_CARDINALITY_AND_SAME_NORM_INVERSE_MARGIN_UNBOUND`, plus the previously separate base-map, shrinking-domain, regulator and OS/continuum gluing residuals.

Next discriminator: source-bind the exact `A_rel` basis/cardinality in Theorem 30.6, the map from that basis into the Section-38 `lambda` coordinates, and either (a) a one-dimensional invariant scalar multiplier uniformly bounded below by `>1`, or (b) a uniform conorm/inverse/adapted-norm/dichotomy estimate. Only after that should the full graph metric be re-tested.
