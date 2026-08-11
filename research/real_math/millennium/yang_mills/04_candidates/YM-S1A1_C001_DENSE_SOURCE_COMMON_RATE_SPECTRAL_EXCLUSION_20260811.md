# YM-S1a1-C001 — Dense-source common-rate spectral exclusion

**Atom:** `YM-S1a1`  
**Candidate ID:** `YM-S1A1-C001-DENSE-SOURCE-COMMON-RATE-SPECTRAL-EXCLUSION`  
**Context hash:** `sha256:082ddb6131aa0316cbdd17248d762af6bc036caed877a2acce42087f1c940e3a`  
**Authority:** `LOCALLY_DERIVED_SPECTRAL_LEMMA / SAME_CONTEXT_CHECKED / NO_NOVELTY_CLAIM / NO_YANG_MILLS_TARGET_BINDING / ROOT_AUTHORITY_NONE`

## Question

The preceding exact three-state calibration showed that a rapidly decaying **restricted** source family can miss a lower-energy excitation. The repaired child asks whether the hidden-state defect disappears at the abstract transfer-operator level once two load-bearing hypotheses are made explicit:

1. the source-generated vectors are dense in the excited-state Hilbert space; and
2. every source obeys one **common** asymptotic transfer ratio `q<1`.

This candidate closes only that abstract implication. It deliberately excludes the Yang–Mills-specific obligations that the relevant Euclidean covariance is an exact physical transfer-matrix moment and that the source class controlled by the correlation theorem is dense after Osterwalder–Schrader reconstruction.

## Candidate lemma

Let `H` be a complex Hilbert space and let `T:H->H` be a positive self-adjoint contraction. Let `Omega` be a unit vector satisfying

`T Omega = Omega`.

Because `T` is self-adjoint, `H_exc := Omega^perp` is invariant under `T`. Let `S` be a set of nonzero vectors in `H_exc` whose linear span is dense in `H_exc`.

Assume there exists one number `q` with `0 <= q < 1` such that, for every `psi in S`,

`limsup_{n->infinity} <psi,T^n psi>^(1/n) <= q`.

Then

`Spec(T|H_exc) subset [0,q]`.

In particular, if an independently established normalization gives

`T = exp(-a H_phys)`

for some `a>0`, with `H_phys` nonnegative, self-adjoint and `H_phys Omega=0`, then

`Spec(H_phys|H_exc) subset [-(1/a) log q, infinity)`,

so the Hamiltonian gap is at least `-(1/a) log q`.

The conclusion remains valid under the stronger sourcewise estimates

`<psi,T^n psi> <= C_psi q^n`

with arbitrary finite source-dependent constants `C_psi`: the constants disappear under nth-root asymptotics. A common prefactor is not required.

## Proof

Fix `psi in S`. By the spectral theorem for the positive self-adjoint contraction `T`, there is a finite positive spectral measure

`mu_psi(B) = <psi,E_T(B)psi>`

supported on `[0,1]`, and

`<psi,T^n psi> = integral_[0,1] lambda^n d mu_psi(lambda)`.

Suppose `mu_psi((q,1])>0`. Since

`(q,1] = union_{k sufficiently large} [q+1/k,1]`,

countable additivity implies that for some `epsilon>0`,

`mu_psi([q+epsilon,1])>0`.

Hence

`<psi,T^n psi> >= (q+epsilon)^n mu_psi([q+epsilon,1])`.

Taking nth roots and `n->infinity` gives

`liminf <psi,T^n psi>^(1/n) >= q+epsilon`,

contradicting the assumed common bound. Therefore

`E_T((q,1]) psi = 0`

for every `psi in S`.

The spectral projection `E_T((q,1])` is a bounded linear operator. It therefore vanishes on `span(S)`, and by density it vanishes on all of `H_exc`. Thus the spectral measure of the restriction `T|H_exc` is supported in `[0,q]`, proving the first conclusion.

For the Hamiltonian statement, apply the spectral mapping theorem to the independently bound identity `T=exp(-a H_phys)`. The inequality `exp(-a E) <= q` on the excited spectrum is equivalent to `E >= -(1/a)log q`.

`QED`.

## Counterexample-first calibration

### World F1 — old hidden-state failure is rejected by the new hypothesis

Take the previous exact model

`T=diag(1,1/2,1/4)`

on `span{Omega,e1,e2}` and the single source `S={e2}`. Its visible ratio is `q=1/4`, but `span(S)` is not dense in `H_exc=span{e1,e2}`. The lemma is therefore inapplicable, exactly as required. The hidden state `e1` remains a valid falsifier of any version that drops density/cyclicity.

### World P1 — enlarged complete source family recovers the true gap

Use the same `T` but take `S={e1,e2}`. The source moments are `(1/2)^n` and `(1/4)^n`. One common choice is `q=1/2`; `span(S)=H_exc`. The conclusion gives

`Spec(T|H_exc) subset [0,1/2]`,

which is exact. Under unit time-step normalization `T=e^{-H}`, the inferred gap is `log 2`, again exact.

### World F2 — density without one common rate is insufficient

Let

`H = span{Omega} direct_sum l2(N)`

with orthonormal excited basis `{e_k}_{k>=1}` and define

`T Omega=Omega`,
`T e_k = (1-1/(k+1)) e_k`.

Then `S={e_k:k>=1}` has dense span in `H_exc`, and every individual source has a strictly decaying moment with its own rate

`q_k=1-1/(k+1)<1`.

But `sup_k q_k=1`, so `Spec(T|H_exc)` accumulates at `1` and there is no positive spectral gap. Thus **one common `q<1` is load-bearing**; sourcewise positivity or source-dependent gaps do not suffice.

## Target-domain consequences and non-consequences

The abstract source-visibility bridge is now logically clean:

`positive physical transfer matrix`
`+ dense/cyclic excited source family`
`+ one common asymptotic source rate q<1`
`=> full fixed-theory transfer spectral exclusion`.

This does **not** yet instantiate the hypotheses for four-dimensional Yang–Mills. In particular:

- Osterwalder–Seiler physical positivity supports a positive self-adjoint lattice transfer matrix, but the exact infinite-volume state/source identification used here must be bound in the same theory.
- Shen–Zhu–Zhu prove strong-coupling exponential covariance decay for a broad smooth-cylinder class with a common exponential exponent and source/support-dependent finite prefactors. Their theorem is Euclidean and strong-coupling; using it here requires an exact temporal covariance-to-transfer-moment identity and density of the controlled source class in the relevant physical excited space.
- Fixed-lattice spin-network/Peter–Weyl bases provide a kinematic completeness model, but fixed-graph Hamiltonian completeness is not automatically density in the exact infinite-volume Osterwalder–Schrader Hilbert space.
- No result here supplies `G5` weak/strong-coupling RG transport, `G6` the physical `a`-scaling needed for a nonzero finite continuum mass, or `G7` continuum spectral identification.
- Wilson confinement/area-law information is not silently substituted for neutral-sector spectral completeness.
- A Langevin/Poincare/log-Sobolev generator gap is not silently substituted for the physical Hamiltonian gap.

Primary anchors for those separate target obligations remain K. Osterwalder and E. Seiler, *Annals of Physics* 110 (1978), DOI `10.1016/0003-4916(78)90039-8`; M. Lüscher, *Communications in Mathematical Physics* 54 (1977), DOI `10.1007/BF01614090`; H. Shen, R. Zhu and X. Zhu, arXiv:`2204.12737` / *Communications in Mathematical Physics* 400 (2023); and G. Burgio et al., arXiv:`hep-lat/9906036`.

## Novelty classification

The proof uses only standard positive self-adjoint spectral calculus, the prior registered hidden-state failure, density, and a common-rate quantifier. No new mathematical operator or representation is introduced. Pending any separate novelty dossier, the defensible v3 ancestry label is therefore:

`PROVISIONAL_RAKL_TRIVIAL`

meaning “composed from pre-existing registered mathematical resources,” **not** “novel theorem.” The stronger publication/novelty authority remains unset.

## Residual opened

The local mathematical implication `density + common q -> full transfer spectral exclusion` is closed at derivation level.

The dominant remaining failure is now explicitly **local-to-global / gluing**, not a failure of the abstract spectral argument:

`YM-S1a2 — OS/SZZ SAME-THEORY BINDING`

Bind, inside one exact strong-coupling lattice Yang–Mills theory, a centered gauge-invariant smooth-cylinder source class to the physical positive transfer matrix so that:

1. translated Euclidean covariance is the required positive transfer moment;
2. source support distance grows as `n+O(1)` in Euclidean time;
3. the source vectors controlled by the common covariance exponent are dense/cyclic in the reconstructed excited space.

Only after that binding is source-proved should this lemma be instantiated as a fixed-cutoff/infinite-volume Yang–Mills transfer-gap statement.

## RAKL_METHOD_CASE_STUDY

**Method used.** Failure-guided hypothesis repair. The previous hidden-state counterexample was not blacklisted; it was converted into an explicit DifferenceWitness. The research action then isolated the minimal spectral-theorem implication and attacked its two load-bearing hypotheses with one failure world, one success world, and one hostile nonuniform-rate world.

**What worked.** The prior failure materially changed routing. It prevented another restricted-correlator argument and forced the source-density coordinate into the child atom. The v3 separation `episode -> diagnosis -> lesson` also kept the elementary counterexample from being overgeneralized into a claim against all correlation methods.

**What failed or remains open.** No target-specific Yang–Mills transfer theorem was obtained. The remaining obstruction is a gluing/interface problem: the SZZ common Euclidean exponent, physical transfer-matrix moment identity, and density of the same source class have not yet been bound in one source-proved theorem packet. `G5`, `G6`, and `G7` are untouched.

**Failure category.** Current residual: `GLUING / REPRESENTATION-BINDING`, not `ABSTRACT_SPECTRAL_MATHEMATICS`. Secondary open categories are `RG-TRANSPORT`, `PHYSICAL-UNIT-SCALING`, and `CONTINUUM-SPECTRAL-IDENTIFICATION`.

**v3 feature used.** Problem fibre + exact prior-failure retrieval + DifferenceWitness + counterexample-first action + separate gluing residual + seven-axis saturation bookkeeping.

**Framework-improvement hypothesis.** No new framework issue is warranted from this single cycle. However, repeated episodes of this form should be measured as `local section closes while gluing edge remains open`; if this pattern recurs across domains, RAKL should expose a first-class quantitative `gluing_debt` / interface-closure metric rather than counting local lemma closure as undifferentiated progress.
