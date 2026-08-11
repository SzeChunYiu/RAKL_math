# H4d1a — source-bound first-order witness-reachability calibration

**Atom:** `H4d1a`
**Frozen context:** `sha256:2a89d1bae5c4c675ec36ace29277fc885307226ceb13a0e6d09a09b72f52e35d`
**Pre-candidate terminal event:** `sha256:4035a5ee15fc2f1faa1d925f57648ba0cb76301219aa8bc913836f7063b7651f`
**Framework inspected for this run:** `SzeChunYiu/RAKL@decd1a4eae2b10cfdbb98e76b5023e2a756fa7a8`
**Application subject:** `SzeChunYiu/RAKL_math@7bc2697d95d0b3021cc242f24712bda22fae0b90`
**Machine gate:** GitHub Actions `Pinned RAKL application tests` run `31481157823` — success.
**Authority:** `SOURCE_BOUND_CALIBRATION / V3_SHADOW_EPISODE / NO_MATHEMATICAL_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`

## Question executed

The frozen H4d1a packet authorized one bounded discriminator after machine assurance:

> Can a branch-reachable first-order obstruction envelope `B_{T,1}` be constructed independently from source-defined Hodge-branch and witness-deformation geometry, and does a useful strict weakening appear before theorem invention?

The calibration must distinguish at least:
- `FULL`,
- `ZERO`,
- `PROPER_NONZERO`,
- `SOURCE_INSUFFICIENT` / `CANNOT_DEFINE_INDEPENDENTLY`.

It is not permitted to define “relevant obstructions” after observing that the obstruction vanishes.

## Expert cell and delegated checks

1. **VHS / Hodge-locus analyst.** Owned the base-side condition defining the Hodge branch and checked that type `(p,p)` persistence is not itself a witness-lifting statement.
2. **Algebraic-cycle / witness-moduli analyst.** Owned the deformation functor of the selected algebraic witness and the projection from witness data to the ambient family.
3. **Semiregularity / obstruction analyst.** Checked the positive control where source hypotheses make Hodge persistence equivalent to relative witness deformation.
4. **Special-family calibration analyst.** Compared complete-intersection positive geometry with the rigid-selected-witness cubic hostile family.
5. **Adversarial falsification analyst.** Tested the prohibited inference `Hodge branch direction -> chosen witness moves`.
6. **Formal assurance / research-method analyst.** Preserved chronology, v3 episode/diagnosis separation, root scope, and the distinction between a representation failure and a Hodge-theorem failure.

Consensus: `SOURCE_INSUFFICIENT_FOR_PROPER_ENVELOPE / REPRESENTATION_REFINEMENT_REQUIRED / ROOT_AUTHORITY_NONE`.

## Primary-source controls

### Positive control A — semiregular relative divisor deformation

Takeo Nishinou, *Deformation of pairs and semiregularity*, arXiv:2009.01651.

The source studies relative deformations of maps into a family of Kähler manifolds whose images are divisors and states that, under semiregularity, relative deformation is possible if and only if the cycle class remains Hodge in the family.

**Calibration use:** this is a witness-compatible control. Under the source's strong semiregularity hypotheses, Hodge persistence is genuinely coupled to deformation of the selected geometric witness. It does **not** prove the desired strict-weaker branch-envelope mechanism for arbitrary higher-codimension rational cycles.

### Positive control B — complete-intersection cycles on hypersurfaces

Remke Kloosterman, *Variational Hodge conjecture for complete intersections on hypersurfaces in projective space*, arXiv:2104.14845v2.

Theorem 1.1 states that for a smooth hypersurface containing a middle-dimensional complete intersection under the stated degree hypotheses, the Hodge locus of the primitive class is smooth at the hypersurface and is contained in the locus of hypersurfaces containing a complete intersection of the same multidegree.

**Calibration use:** special flag-Hilbert geometry can align Hodge-locus motion with a controlled algebraic witness category. This is a restricted positive control, not a general branch-envelope theorem.

### Hostile control — Hodge mobility with the selected witness frozen

Hossein Movasati, *Hodge cycles for cubic hypersurfaces*, arXiv:1902.00831v2.

The source chooses a smooth deformation space of the cubic Fermat variety in which the triple consisting of the variety and the two selected linear cycles is rigid. Nevertheless, for specified intersections and coefficients the finite-order Hodge locus attached to their linear combination can be smooth, reduced and positive-dimensional. In some regimes the algebraic cycles that should account for those Hodge classes are only conjecturally described or unknown.

**Decisive implication for this calibration:** a positive-dimensional Hodge branch can survive while the **chosen source witness family is rigid**. Therefore the map

`Hodge-class persistence -> mobility of the chosen witness`

is not source-valid in general. If class persistence is eventually realized algebraically, the realizing witness may have to change category/component/geometry.

This does not refute the Hodge conjecture and does not prove that the obstruction space is nonzero in every formalism. It falsifies the narrower representation move that tries to construct `B_{T,1}` from base Hodge directions alone while keeping the selected witness implicit.

### Fresh 2026 base-side control

Kefeng Liu and Yang Shen, *Sections of Hodge bundles II: Deformation of (p,p)-classes and applications to Kähler geometry*, arXiv:2602.13951v2, revised 19 July 2026.

The source gives an intrinsic analytic description of Hodge loci and a Beltrami-differential criterion for the variational Hodge conjecture.

**Calibration use:** this strengthens the *base-side* description of allowed Hodge directions. It does not, by itself, supply the selected cycle-witness deformation object or the projection needed to compute `B_{T,1}`. The inference here is deliberately limited to that scope distinction.

## Result

The planned source-domain calibration does **not** produce a certified `PROPER_NONZERO` envelope.

The strongest source-bound conclusion is:

`SOURCE_INSUFFICIENT_FOR_PROPER_ENVELOPE`.

More precisely:

1. strong source hypotheses can make Hodge persistence and witness deformation compatible (Nishinou; Kloosterman special geometry);
2. Hodge persistence can also coexist with rigidity of the originally selected witness family (Movasati);
3. therefore a Hodge branch `T` is not enough data to define the chosen-witness reachable obstruction image;
4. the next representation must expose the witness-moduli/deformation object and its projection to the Hodge branch **before** detector faithfulness is tested.

The newly observed scoped failure is:

`F-H4D1A-CLASS-WITNESS-PERSISTENCE-GAP`

with v3 fast-loop status `OBSERVED_ONLY` in this run. It is not promoted to a reusable obstruction.

## Local-to-global / gluing diagnosis

This is a **bridge/gluing failure**, not a local Hodge-locus failure.

The local section

`flat class remains of type (p,p) along T`

does not glue automatically with the local section

`the chosen algebraic witness deforms along T`.

The missing interface is a source-defined witness-moduli projection with explicit coverage/identity semantics. Even if that local bridge is solved, H4d1a still begins with an already algebraic central witness and leaves initial algebraicity, higher Artin order, algebraization, monodromy and global continuation open.

## Residual and next child

Open a fresh representation child:

`H4d1a1-WITNESS-MODULI-PROJECTION`

Exact question:

> For one source-controlled witness category, freeze a moduli/deformation object `W` and projection `pi: W -> S`. Relative to the Hodge branch `T`, compute the tangent/obstruction data of `W x_S T`, distinguish persistence of the same witness from replacement by another witness representing the same class, and only then define the first-order reachable obstruction image.

The child must choose the witness category before evaluation (flag Hilbert, Chow, stable maps, derived deformation object, or another source-justified category), freeze a fresh `MathContextFiber`, and run a new prospective source-bound discriminator.

No theorem candidate is authorized by this calibration.
