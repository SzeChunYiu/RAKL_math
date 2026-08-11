# NS-B1a3b same-context expert cell — vorticity-geometry inheritance

**Authority:** `SAME_CONTEXT_REVIEW_ONLY / PRE_CANDIDATE / NO_INDEPENDENT_REVIEW / ROOT_AUTHORITY_NONE`

## Cell

1. **PDE scaling and endpoint specialist** — background: Serrin/CKN scaling, Type-I blow-up normalization, Sobolev compactness. Role: audit units, derivative count, criticality, endpoints, and circular bootstraps.
2. **Vorticity-geometry specialist** — background: Constantin–Fefferman geometric depletion, vorticity-direction criteria, vortex stretching. Role: identify the exact geometric object a criterion consumes and where normalization at `omega=0` matters.
3. **Blow-up/compactness specialist** — background: suitable weak solutions, Albritton–Barker finite-`I` ancient limits, persistence of singularities. Role: state exactly what convergence is inherited by the rescaled sequence and forbid upgrades not present in the producer theorem.
4. **Harmonic-analysis/nonlocality specialist** — background: Biot–Savart, strain singular integrals, BMO/commutators. Role: track what happens to pressure after curl and whether nonlocality has actually disappeared.
5. **Conditional-regularity transfer specialist** — background: whole-space and half-space geometric criteria, anisotropic criteria. Role: build DifferenceWitnesses for domain, Type-I notion, high-vorticity set, and regularity assumptions.
6. **Adversarial verification/metrology specialist** — background: topology counterexamples, proof-interface audits, RAKL v3 evidence boundaries. Role: attack inheritance before theorem transfer and prevent same-context agreement from being counted as independent review.

## Delegated findings

The scaling specialist records
`omega_lambda(x,t)=lambda^2 omega(lambda x,lambda^2 t)` and, where `omega != 0`,
`xi_lambda(x,t)=xi(lambda x,lambda^2 t)`. Thus `xi` itself is dimensionless, but a spatial Hölder seminorm obeys
`[xi_lambda]_{C^alpha}=lambda^alpha [xi]_{C^alpha}`. Any geometric criterion must therefore be read with its own scale, high-vorticity set, and time integrability; a bare uniform modulus cannot be inferred from scale invariance of velocity quantities. The normalization `xi=omega/|omega|` is not defined at zeros and is discontinuous as a map of weak vorticity fields near zero.

The compactness specialist accepts the existing B1a3 producer interface: strong local `L^3` velocity convergence, weak local pressure convergence, and natural weak derivative control supplied by the local energy quantity. Strong convergence of `u` does not give strong convergence of `curl u`; at the direct functional-analytic level, taking curl costs one derivative. Hence a vorticity-angle modulus is a strictly stronger output type than the registered compactness stage currently produces.

The vorticity-geometry specialist checks the literature-facing consumer types. Constantin–Fefferman is a conditional whole-space geometric criterion on vorticity direction. Miller's anisotropic criterion assumes scale-critical control of vorticity projected to a varying plane together with control of the plane field. Barker–Prange assumes, in a half-space/no-slip ODE-Type-I setting, uniform continuity of vorticity direction on specified high-vorticity subsets of shrinking regions. In each case geometry is an input to the theorem. None of these source signatures, as currently registered, states that Albritton–Barker finite `I` produces the input.

The harmonic-analysis specialist records an important route-specific distinction from the earlier pressure lane. Taking curl eliminates the pressure gradient exactly from
`partial_t omega + (u dot grad) omega - Delta omega = (omega dot grad)u`.
Therefore the old pressure-tail summability obstruction is not the immediate blocker. Nonlocality nevertheless remains: the symmetric velocity gradient/strain appearing in vortex stretching is recovered nonlocally from vorticity through singular-integral/Biot–Savart structure. A geometric cancellation theorem controls that nonlocal interaction only after its directional hypothesis has been established.

The transfer specialist rejects a direct Barker–Prange import. The target is whole space; the source theorem is half-space with no-slip boundary. The source Type-I assumption is the ODE blow-up rate, whereas the target producer is the Albritton–Barker finite-`I` class. Most importantly, vorticity alignment is separately assumed in the source. The theorem is therefore a near-solved analogue showing that Type-I plus geometry can be powerful, not an inheritance theorem for finite `I`.

The adversarial specialist supplies the counterexample-first discriminator on a local periodic box:
`w_n(x)=(0,n^{-1} sin(n x_1),0)`.
Then `div w_n=0`, `w_n -> 0` strongly in every finite `L^p`, and `||grad w_n||_2` is independent of `n`, while
`curl w_n=(0,0,cos(n x_1))`.
Away from its zero planes, the normalized vorticity alternates between `+e_3` and `-e_3` at spacing `O(1/n)`, so no uniform continuity/Hölder modulus survives. This is not a Navier–Stokes solution and does not refute an equation-specific inheritance theorem. It precisely falsifies the weaker topological inference from the compactness norms already available to vorticity-direction coherence.

## Deliberation

The cell considered three more ambitious actions: prove an alignment criterion from the vorticity equation directly, import the half-space Type-I alignment theorem, or use the July 2026 logarithmic-depletion preprint as a new rigidity trigger. All three were deferred. The first would skip the cheapest falsifier and risks a circular derivative bootstrap; the second fails its DifferenceWitness; the third contains extra concentration and logarithmic-direction assumptions and is a fresh preprint, so it may guide search but cannot bear theorem authority here.

The strongest source-safe question is therefore not whether vorticity geometry can regularize a solution, but whether the existing finite-`I` producer stage already supplies a consumer-ready geometric quantity. The oscillatory calibration predicts **no** at the topology level. A positive result would have to be equation-specific and produce a genuinely new estimate beyond the current compactness package.

## Pre-candidate consensus

**Unanimous same-context routing verdict:** freeze `NS-B1a3b-C001` as an inheritance/interface candidate:

> The registered finite-`I` compactness package does not by topology alone transfer a uniform critical vorticity-direction/geometric-depletion condition to the ancient limit. Any use of a geometric regularity theorem therefore requires a separately proved equation-specific geometry-inheritance estimate with exact domain, high-vorticity-set, endpoint, and scaling hypotheses.

This is a route-pruning/interface proposition. It is not a theorem that finite `I` can never imply geometric coherence by additional Navier–Stokes dynamics.

## Falsifier

Overturn the candidate by producing a source-valid or newly proved estimate from the exact finite-`I` hypotheses that controls, uniformly on the blow-up sequence and through the limit, an explicitly named scale-critical geometric functional `G` whose value exactly discharges a primary-source vorticity regularity/Liouville criterion. The proof must survive vorticity zeros, derivative loss, scaling, high-vorticity-set restriction, and the strain nonlocality without assuming the desired regularity in a bootstrap.
