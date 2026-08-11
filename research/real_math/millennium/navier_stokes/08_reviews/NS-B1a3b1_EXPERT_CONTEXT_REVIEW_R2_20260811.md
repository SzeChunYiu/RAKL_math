# NS-B1a3b1 R2 same-context expert cell — log-BMO zoom / source interface

**Authority:** `SAME_CONTEXT_REVIEW_ONLY / PRE_CANDIDATE / NO_INDEPENDENT_REVIEW / ROOT_AUTHORITY_NONE`

## Roles and delegated questions

1. **Blow-up/ancient-solution specialist** — suitable weak solutions, Type-I rescaling, Albritton–Barker compactness. Determine exactly what the finite-`I` producer supplies and whether Grujic's theorem is an ancient-solution rigidity theorem.
2. **Harmonic-analysis specialist** — Campanato/BMO, Lorentz spaces, Calderón–Zygmund commutators. Compute the exact `bmo_{1/|log r|}` dilation law and inspect near/far-field dependencies.
3. **Vorticity-geometry specialist** — vortex stretching, direction fields, high-vorticity geometry. Track `xi=omega/|omega|`, the zero-vorticity endpoint, and which geometry is assumed versus produced.
4. **Scaling/compactness specialist** — parabolic scaling and weak/strong convergence. Audit spatial and temporal zoom, global-versus-local center quantifiers, and whether any convergence claim is silently strengthened.
5. **Adversarial falsification specialist** — attempt to break zoom non-expansion, direct finite-`I` transfer, and ancient-Liouville reinterpretation with the cheapest exact falsifiers.
6. **Formal assurance/provenance specialist** — bind current framework/application SHAs, stale-branch chronology, exact source version, and keep computation/source reading separate from proof or root authority.
7. **Novelty/research-value specialist** — distinguish a routine representation lemma from a new PDE theorem and decide whether solving it materially changes the active obstruction.

## Deliberation before candidate execution

The harmonic-analysis specialist proposes the lowest-cost discriminator. For `f_r(y)=f(x0+r y)` and a target ball `B_rho(y0)`, change of variables gives exact equality of mean oscillations with `f` on `B_{r rho}(x0+r y0)`. With `phi(s)=1/|log s|`, the target weighted factor is `|log rho|`; the source bound supplies `1/|log(r rho)|`. For `0<r<=1`, `|log(r rho)|=|log r|+|log rho|`, so the ratio is at most one. This is a candidate representation statement only until the frozen falsifier is executed.

The blow-up specialist warns that even a positive dilation result would not close the PDE edge. Albritton–Barker finite `I` yields a Type-I ancient-limit package; it does not, by the already merged `NS-B1a3b` audit, produce a vorticity-direction modulus. Grujic v2 Theorem 7.4 is framed at a first possible singular time and uses forward local analyticity and escape times, so it must not be relabeled as an ancient-solution Liouville theorem.

The vorticity specialist requires the zero-set endpoint to remain explicit. The source describes the direction as a unit vector field, but a search of the current v2 HTML did not locate an explicit convention at `omega=0`. The present cycle therefore records a source-signature applicability obligation rather than inventing a convention.

The scaling specialist separates three quantifier layers: spatial zoom of a **global** BMO norm, time-uniform bounds on a source interval, and global center/tail control. Spatial zoom may be stable while a merely local physical hypothesis still fails to become a global rescaled hypothesis.

The adversarial specialist freezes three failure tests: (i) find a zoom factor and bounded `bmo_phi` function that increases the norm; (ii) exhibit a Grujic hypothesis absent from the finite-`I` producer even if (i) fails; (iii) compare theorem time/state-space signatures to refute an ancient-Liouville reinterpretation.

The assurance specialist rejects prospective credit from the earlier partial branch `research/ns-b1a3b1-logbmo-zoom-interface-20260811@82d29134`: it was frozen against older framework/application subjects. Its experience can guide routing, but this R2 packet is freshly bound to `RAKL@fe47a12c...` and `RAKL_math@9932f136...`.

The novelty specialist expects, if verified, the dilation statement to be `REPRESENTATION`/compositional rather than a new Navier–Stokes theorem. Its research value is that it can remove “the log-BMO consumer may be destroyed by zoom” from the residual, leaving only producer generation and theorem-signature gluing.

## Pre-candidate consensus

Proceed with `NS-B1a3b1-C001`: verify the exact weighted-BMO zoom inequality first, then source-audit Definition 2.1, Theorem 4.1, its far-field estimates, and Theorem 7.4 of arXiv:2607.08866v2. A positive zoom result grants only a representation-transfer lemma. Direct PDE transfer remains blocked unless finite `I` supplies every global/time/high-vorticity input and the pre-singularity theorem is connected by a separately valid same-theory interface.
