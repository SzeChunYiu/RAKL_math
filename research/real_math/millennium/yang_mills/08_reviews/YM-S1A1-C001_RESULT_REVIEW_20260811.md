# YM-S1A1-C001 result review

**Verdict:** `SUPPORTED_ABSTRACT_LEMMA / TARGET_BINDING_OPEN`  
**Root:** `OPEN_NO_SOLUTION_CERTIFICATE`

## Review question

Does density of a source family plus one common asymptotic positive-transfer moment rate rule out an unobserved slower mode?

## Cell and delegation

The same-context cell used six roles.

- Transfer-matrix/lattice gauge: physical representation assumptions and no-overclaim boundary.
- Operator/spectral theory: theorem statement and spectral-projector proof.
- Strong-coupling/cluster expansion: rate/prefactor quantifiers.
- RG/asymptotic freedom: volume/cutoff/coupling/continuum non-transfer.
- OS/constructive QFT: Euclidean-to-transfer binding and density after reconstruction.
- Formal/adversarial assurance: planted worlds, endpoints, quantifier audit and scope.

Each role cross-reviewed the statement, proof and residual list. The operator and assurance roles independently rederived the contradiction from `E_T((r,1])`; the transfer/OS and strong-coupling/RG pairs independently audited that no target-specific hypothesis had been smuggled into the abstract result.

## Findings

The proof is complete at the abstract operator level. For every `r>q`, a nonzero spectral projector above `r` has nontrivial action on some vector of the dense set. Positivity then forces that vector's nth-root moment rate to be at least `r`, contradicting the common bound `q`.

The old restricted-source hidden-mode example is not erased. It is a planted failure world because its source set is not dense. Enlarging to a dense set forces the slowest visible spectral rate to reappear.

No finite-volume, lattice-spacing, coupling-regime, RG, confinement-to-gap, or continuum-spectral uniformity is obtained from this lemma.

## Assurance status

- exact statement binding: PASS for the child candidate;
- proof DAG: closed for the abstract implication (`spectral projector -> dense hit -> positive moment lower bound -> contradiction -> spectral containment`);
- dependency audit: spectral theorem for bounded positive self-adjoint operators only;
- axiom audit: ordinary Hilbert-space functional analysis; no computational/numerical proof bridge;
- planted failure: PASS;
- planted success: PASS;
- target-binding audit: OPEN;
- bounded root novelty search: not invoked because no root promotion is attempted;
- isolated mathematical reviews required for root promotion: not invoked.

## Next route-discriminating atom

`YM-S1a2`: same-theory OS source binding.

Exact question: under the chosen reflection-positive lattice Yang–Mills representation, can the gauge-invariant smooth-cylinder observables for which one has a common Euclidean-time decay rate be mapped to a dense/cyclic subset of the **same** excited transfer Hilbert space with the covariance equal to the required positive transfer moments, while preserving a rate useful under the thermodynamic and eventual continuum limits?

A negative answer should be normalized as `UNPROVED_CORRELATION_TO_FULL_GAP_BINDING` or, if an explicit obstruction is found, a more precise scoped failure.
