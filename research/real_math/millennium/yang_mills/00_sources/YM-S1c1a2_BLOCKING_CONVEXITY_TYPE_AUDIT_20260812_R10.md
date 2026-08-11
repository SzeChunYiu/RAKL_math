# YM-S1c1a2 R10 — admissible blocking interpolation / representation-type audit

Status: **proposal/shadow evidence only**. No Yang–Mills root claim, protected lesson, or independent-review credit.

## Frozen atom

- Root: `SzeChunYiu/RAKL_math#5` (`OPEN_NO_SOLUTION_CERTIFICATE`).
- Active atom: `SzeChunYiu/RAKL_math#177`.
- Signature: `YM-S1c1a2-AFIR-ENDPOINT-PRESERVING-VANISHING-UV-ALIGNMENT`.
- Fibre hash: `4e5f3c6fbc723a7784ed96d1439154ce3ec9f729b5c4a686d3ce00ac4c19fed8`.
- Residual entering this cycle: `RES-YM-S1c1a2-ENDPOINT-PRESERVING-VANISHING-AFIR-ANCHOR-OR-STRICT-CONTRACTION-SAME-OS-THEORY`.

The R9 residual asks for a genuinely vanishing AF/IR comparison on the same gauge-invariant OS theory. This cycle tested an upstream premise of the Appendix-F repair: whether its proposed interpolation is actually a path inside the stated admissible blocking space.

## Primary-source binding

Primary source: Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv:2606.19362v1.

The inspected primary PDF supplies the following load-bearing interfaces.

1. Eq. (2.51) defines a coarse block map schematically as
   `B[U]_{b'} = Proj_SU(N)(sum_{p in P(b')} kappa(p) U_p)`.
   Its output is therefore an `SU(N)`-valued coarse gauge configuration and the projection is part of the nonlinear map.

2. Lemma 2.3 states reflection-positivity compatibility through pullback of positive-time coarse observables under the block map. The stated admissible class is built from reflection-positive, gauge-covariant block maps/kernels and their finite compositions/limits.

3. Appendix-F Definition F.1 equips an admissible scheme with a regulator projector and block-spin map `B_Theta`; Definition F.2 and Lemma F.10 then interpolate two blockings by
   `B_{s,k} = (1-s) B_{0,k} + s B_{1,k}`.

4. In the proof of Lemma F.10, Eq. (F.72) writes the reflection-positive quadratic form of this convex combination as the convex combination of the two endpoint quadratic forms, with no squared coefficients or cross terms.

The primary parsed text is sufficient to audit the algebra and the representation interface. Mandatory page screenshots were attempted on three relevant PDF pages and each returned backend `Cache miss`; visual page verification is therefore `CANNOT_CHECK`, not silently counted as passed.

## Atomic falsifier 1: the displayed F.72 equality is not a quadratic-form identity

For any sesquilinear/real bilinear positive quadratic form `Q(x,y)=<Theta x,y>`, the exact expansion is

`Q((1-s)x+s y,(1-s)x+s y)`
`= (1-s)^2 Q(x,x) + s^2 Q(y,y) + s(1-s)[Q(x,y)+Q(y,x)]`.

This is not, in general,

`(1-s) Q(x,x) + s Q(y,y)`.

Thus the equality displayed in F.72 is not an algebraic identity without an additional special relation. This is a local proof defect.

**Important disanalogy / non-overclaim.** The failed equality does *not* by itself prove reflection positivity of every interpolated object is false. If an interpolated induced operator were independently known to map the positive-time algebra into itself, OS positivity of its pullback could give nonnegativity directly. What is missing is precisely the typed admissibility/preservation witness needed to use that route.

## Atomic falsifier 2: the configuration-map codomain is not convex

If the `B` interpolated in Appendix F is the nonlinear `SU(N)`-valued configuration block map defined earlier, raw pointwise linear interpolation is not closed in its codomain.

Exact hostile control in `SU(2)`:

- choose endpoint coarse links `U_0 = I` and `U_1 = -I`;
- at `s=1/2`, `(1-s)U_0+sU_1 = 0`;
- `0` is not in `SU(2)`.

So a linear midpoint of two group-valued blocking outputs is not itself a group-valued coarse link. Adding `Proj_SU(N)` after interpolation is not a free repair: at the hostile midpoint the polar projection is singular/nonunique, and any replacement needs its own gauge-covariance, continuity/locality, reflection-positivity, endpoint and uniformity proof.

## Representation/type disjunction

The source's notation can be read in two materially different ways.

### A. `B` is the nonlinear configuration block map

Then the convex formula in Lemma F.10 is not shown to remain in the space of `SU(N)`-valued block maps. The `SU(2)` midpoint control is an explicit codomain-closure failure for raw linear interpolation.

### B. `B` is an induced kernel/operator on observables

Then convex combinations may be algebraically meaningful in an ambient operator space, but Appendix F still needs a **realization/gluing witness** showing that every interpolated operator/kernel comes from, or is equivalent to, an admissible gauge-covariant blocking of the same regulated Yang–Mills theory and preserves the relevant positive-time algebra, endpoints, locality/finite-range structure and continuum-uniform controls.

The inspected primary text does not supply that typed witness. It is therefore `BLOCKED/UNKNOWN`; it is not reconstructed from generic RG or OS memory.

## Same-theory audit

A repair relevant to root #5 must bind all of the following, not merely an abstract path metric:

- the same gauge-invariant OS source algebra;
- the same reflection-positive quotient/Hilbert space;
- endpoint preservation for the actual AF and IR constructions;
- gauge covariance / gauge-invariant observables;
- locality and finite-range/blocking hypotheses used by the RG;
- regulator, volume, lattice-spacing and scale uniformity sufficient to exchange/pass limits;
- the same continuum subsequence and physical-time normalization;
- a comparison strong enough on a generating cylinder/source family to identify the reconstructed continuum state.

No numerical experiment can supply these theorem-level bindings; numerics remain calibration/falsification only.

## Expert cell (same context; zero independent-review credit)

1. **Constructive QFT / OS reconstruction.** The F.72 equality is false as written, but OS positivity could still be proved by a different positive-time-algebra preservation argument. The central missing item is the admissible typed path.
2. **Rigorous RG.** Universality interpolation must stay inside the actual finite-range/local RG scheme class with uniform constants; convexity in an ambient operator space is insufficient.
3. **Gauge theory / physical states.** `SU(N)` is nonconvex. Any retraction/geodesic replacement must be gauge covariant and avoid singularities while preserving the physical observable construction.
4. **Functional analysis / metric geometry.** The quadratic-form expansion has squared coefficients and cross terms. The path metric only applies after membership of the interpolated path in the admissible metric space has been established.
5. **Formal proof / quantifier audit.** `B` changes/overloads representation between configuration map and kernel/operator roles at a load-bearing step without an explicit equivalence/realization witness.
6. **Primary-source / RAKL metrology.** Preserve this as one coupled representation/gluing obstruction. The elementary controls are `RAKL_TRIVIAL`; they do not earn mathematical novelty or root authority.

## Episode → diagnosis → obstruction / lesson separation

- Episode: `EP-YM-S1c1a2-R10-20260812`.
- Diagnosis: `DG-YM-S1c1a2-R10-BLOCKING-CONVEXITY-TYPE-SHADOW`.
- Failure evidence:
  - `FS-YM-S1c1a2-F72-CONVEXITY-IDENTITY-R10-SHADOW`;
  - `FS-YM-S1c1a2-BLOCK-MAP-TYPE-CLOSURE-R10-SHADOW`.
- Scoped obstruction: `O-YM-S1c1a2-ADMISSIBLE-BLOCKING-INTERPOLATION-TYPE-CLOSURE-R10-SHADOW`.
- New lessons: none.
- New motifs: none.

The episode records what was attempted/observed. The diagnosis classifies the observation. The obstruction states the remaining interface. No same-context agreement is promoted into a reusable verified lesson.

## Outcome and new residual

Outcome: `PARTIAL_SUCCESS`.

The R9 endpoint-vanishing problem is not solved; it is now preceded by a newly isolated admissibility/type obligation. The residual is sharpened to:

`RES-YM-S1c1a2-TYPED-ADMISSIBLE-BLOCKING-PATH-PLUS-ENDPOINT-PRESERVING-VANISHING-AFIR-SAME-OS-THEORY`.

A high-information next discriminator is an explicit primary theorem giving one of:

1. an endpoint-preserving gauge-covariant interpolation/retraction of the nonlinear `SU(N)` block maps that remains reflection positive, local/finite-range and uniformly controlled; or
2. a theorem realizing the convexly interpolated kernels/operators as admissible same-theory blockings with those properties.

Only after that typing obligation is closed does the R9 requirement for a *vanishing* AF/IR comparison (anchor tending to zero, strict contraction with vanishing forcing, or typed zero-distance quotient) become the next active gate.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`; independent mathematical review count remains `0/3`.
