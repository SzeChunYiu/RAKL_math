# H4d1a primary-source addendum — strict-weaker obstruction-envelope calibration

Date: 2026-08-11

Framework authority inspected for this continuation: `SzeChunYiu/RAKL@15f1c3affe5bf85ba41ff0ab65b25ba19e0d28a3`.
Application branch was synchronized with `RAKL_math/main@d8ac4102285c4ed1ba0fbd5d8818dc4c4731a8cc` before this addendum. The application gitlink/config pin also names the same RAKL framework commit.

This is a source update for the already-frozen H4d1a pre-candidate context. It does not rewrite the frozen context packet, generate a mathematical candidate, or change Hodge-root authority.

## Active discriminator

H4d1a asks whether full semiregularity can be weakened, for a fixed algebraic witness and fixed Hodge-locus branch `T`, to faithfulness only on an independently constructed branch-reachable obstruction envelope `B_{T,m}`. The envelope may not be defined using the fact that a desired lift succeeds. First-order control is insufficient unless a later child checks Artin-order stability.

## Primary-source controls

### Pridham — reduced obstruction theory is real, but not automatically branch-specific

J. P. Pridham, *Semiregularity via derived deformation theory*, arXiv:1112.6001, realizes the Buchweitz–Flenner semiregularity map as the tangent of a derived-moduli morphism, proves global obstruction annihilation, and constructs a global reduced obstruction theory. This is a legitimate source model for replacing an ambient obstruction theory by a smaller one. It does **not** by itself identify the image of the particular Hodge branch `T`, prove detector injectivity on that image, or supply an all-order H4d1a envelope.

Primary source: https://arxiv.org/abs/1112.6001

### Kloosterman — positive special-family control for comparing geometric and Hodge directions

R. Kloosterman, *Variational Hodge conjecture for complete intersections on hypersurfaces in projective space*, arXiv:2104.14845, proves the variational Hodge conjecture for the stated complete-intersection cycles. The proof compares the relevant geometric flag-Hilbert locus with the Hodge locus using explicit tangent-space, dimension, and smoothness information. This is a source-bound positive control for independently computing geometric directions before claiming equality with Hodge directions. It is not a general higher-codimension branch-envelope theorem.

Primary source: https://arxiv.org/abs/2104.14845

### Movasati — hostile boundary: Hodge deformation can be larger than algebraic-cycle deformation

H. Movasati, *On a Hodge locus*, arXiv:2211.11405, explicitly studies situations where the deformation space of the homology class of an algebraic cycle as a Hodge cycle is larger than its deformation space as an algebraic cycle, and describes a cubic-hypersurface case for further verification/computational study. This is useful here only as a hostile boundary/source-acquisition target: it reinforces that base-side Hodge directions cannot be identified with witness directions without a geometric comparison theorem. The article's computational evidence is not promoted to a Hodge theorem.

Primary source: https://arxiv.org/abs/2211.11405

### Liu–Shen — explicit base-side Hodge equations remain base-side

K. Liu and Y. Shen, *Sections of Hodge bundles II: deformation of (p,p)-classes and applications to Kähler geometry*, arXiv:2602.13951, develops an intrinsic Hodge map on Kuranishi families and an analytic/Beltrami description of Hodge loci. This may help specify the allowed directions of `T`, but it does not independently produce an algebraic-cycle witness or identify the witness obstruction image.

Primary source: https://arxiv.org/abs/2602.13951

## Source-bound conclusion

The inspected source set supports a sharper calibration interface but not a new theorem:

1. compute Hodge-branch directions independently on the base;
2. compute the chosen witness deformation/obstruction map independently;
3. define `B_{T,1}` as an image/reachable subobject of that pre-existing map, not from successful lifts;
4. classify `B_{T,1}` as full, zero, or proper nonzero;
5. if proper, test intersection with the detector kernel;
6. only then open a separate higher-Artin-order stability atom.

No inspected primary source yet supplies a general coupled nonsemiregular example with `0 < B_{T,m} < Ob_m` and all-order stability. A failure to locate such a source is a source-acquisition/residual result, not permission to invent an ungrounded criterion.

Authority: `PRIMARY_SOURCE_ADDENDUM / PRE_CANDIDATE_SEARCH_CONTROL / NO_THEOREM_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`.
