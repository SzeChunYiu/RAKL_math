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

### Movasati — hostile and zero-envelope calibration, with source-status guard

H. Movasati, *Hodge cycles for cubic hypersurfaces*, arXiv:1902.00831, gives an explicit source domain in which a chosen pair of linear algebraic cycles is made rigid inside a selected deformation family while the corresponding Hodge locus can have positive-dimensional infinitesimal directions. This is useful as a **boundary calibration** for H4d1a: if the chosen witness is rigid in the selected family, the witness-reachable first-order envelope can be zero even when Hodge-preserving base directions are nonzero. Such a `ZERO` outcome demonstrates logical separation from full semiregularity but is deliberately treated as vacuous/boundary evidence rather than a coupled nonzero mechanism. The paper also contains higher-order/computational Hodge-locus evidence; those computations and conjectural interpretations are not promoted to theorem authority here.

Primary source: https://arxiv.org/abs/1902.00831

The earlier note *On a Hodge locus*, arXiv:2211.11405, was **withdrawn on 2025-02-25** and says that its material was incorporated into the newer collection *Leaf schemes and Hodge loci*, arXiv:2502.19988. The withdrawn item is retained only as provenance for the older search path and is not used as current primary authority. The successor collection is a current source for Hodge-locus/leaf-scheme context, but it does not by itself supply the required independently constructed nonsemiregular `0 < B_{T,m} < Ob_m` envelope.

Current successor source: https://arxiv.org/abs/2502.19988
Withdrawn provenance only: https://arxiv.org/abs/2211.11405

### Liu–Shen — explicit base-side Hodge equations remain base-side

K. Liu and Y. Shen, *Sections of Hodge bundles II: deformation of (p,p)-classes and applications to Kähler geometry*, arXiv:2602.13951v2 (revised 2026-07-19), develops an intrinsic Hodge map on Kuranishi families and an analytic/Beltrami description of Hodge loci. This may help specify the allowed directions of `T`, but it does not independently produce an algebraic-cycle witness or identify the witness obstruction image.

Primary source: https://arxiv.org/abs/2602.13951

## Source-bound conclusion

The inspected source set supports a sharper calibration interface but not a new theorem:

1. compute Hodge-branch directions independently on the base;
2. compute the chosen witness deformation/obstruction map independently;
3. define `B_{T,1}` as an image/reachable subobject of that pre-existing map, not from successful lifts;
4. classify `B_{T,1}` as full, zero, or proper nonzero;
5. use Movasati's rigid-cycle family only as a `ZERO` boundary calibration, not as evidence for the desired coupled nonzero case;
6. if a proper nonzero envelope is found, test its intersection with the detector kernel;
7. only then open a separate higher-Artin-order stability atom.

No inspected current primary source yet supplies a general coupled nonsemiregular example with `0 < B_{T,m} < Ob_m` and all-order stability. A failure to locate such a source is a source-acquisition/residual result, not permission to invent an ungrounded criterion.

Authority: `PRIMARY_SOURCE_ADDENDUM / PRE_CANDIDATE_SEARCH_CONTROL / NO_THEOREM_CANDIDATE / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`.
