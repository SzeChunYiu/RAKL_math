# NS-B1a3b source packet — Type-I vorticity-direction rigidity

Authority: `SOURCE_BOUND_PRE_CANDIDATE_CONTEXT / ROOT_AUTHORITY_NONE`.

## Exact atom

`NS-B1a3b` is the geometry child of the dynamics-specific Type-I bridge. It asks for an exact scale-critical vorticity-direction/coherence property that matches a source-valid regularity or rigidity theorem, then audits whether that property is actually inherited from the registered Type-I class. This is orthogonal to `NS-B1a3a` global critical-topology tightness.

## Primary source 1 — Giga–Miura

Y. Giga, H. Miura, *On Vorticity Directions near Singularities for the Navier-Stokes Flows with Infinite Energy*, Comm. Math. Phys. 303 (2011), 289–300, DOI `10.1007/s00220-011-1197-x`; open preprint Hokkaido University Preprint Series 956 (2010), DOI `10.14943/84103`.

Exact interfaces used from the open preprint:

- Section 1, Theorem 1.1: for a whole-space Type-I mild solution on `R^3 x (-1,0)`, if for some `d>0` the vorticity direction `zeta=omega/|omega|` has one uniform spatial modulus of continuity on `Omega_d(t)={|omega|>d}` for all `t in (-1,0)`, then there is no blow-up at `t=0`.
- Remark 1.4: the modulus can be weakened to the shrinking-self-similar condition `(CA')`; this is the form used in the blow-up proof.
- Section 2.1: maximum normalization chooses `M_k=||u(t_k)||_infty`, `lambda_k=M_k^{-1}`, and `u_k(x,t)=lambda_k u(x_k+lambda_k x,t_k+lambda_k^2 t)`. The rescaled velocities are bounded by one and parabolic regularity gives uniform derivative bounds. A subsequence of `u_k, omega_k` converges locally uniformly to a bounded ancient mild solution. The source passes mildness through weak-star convergence of `u_k tensor u_k` in `L^infty`.
- Proposition 2.1: Type-I implies the limiting ancient vorticity is nonzero; otherwise bounded harmonicity plus mildness makes the limit a nonzero space-time constant velocity, contradicting the inherited Type-I decay as `t -> -infinity`.
- Proposition 2.2: on each compact subset of `{omega != 0}`, the rescaled high-vorticity threshold is eventually satisfied and `(CA')` collapses direction oscillation to zero, making the limiting vorticity direction spatially constant.
- The rigidity step: after rotation at a time slice, `omega=(0,0,omega_3)` implies `(curl omega)_3=0`, hence bounded `u_3` is harmonic and spatially constant; `omega_1=omega_2=0` then makes `u_1,u_2` independent of `x_3`; uniqueness propagates the two-dimensional structure. Lemma 2.3 kills bounded ancient 2D vorticity by a maximum-principle/Liouville argument.
- Corollary 2.6: for a whole-space Type-I mild solution, finiteness of `integral_{-1}^0 ||grad zeta||_{L^infty(Omega_d(t))}^2 dt` for a given `d>0` prevents blow-up. Remark 2.8 explicitly states that this condition is scaling invariant. It also notes a source-stated mixed-norm generalization with `2/a+3/b=1`, `2<=a<infinity`; that remark is not promoted here to a separately verified theorem.

Open primary-source locator: `https://eprints.lib.hokudai.ac.jp/repo/huscap/all/69763/re956.pdf`.

## Primary source 2 — Albritton–Barker

D. Albritton, T. Barker, *On local Type I singularities of the Navier–Stokes equations and Liouville theorems*, J. Math. Fluid Mech. 21 (2019), 43, DOI `10.1007/s00021-019-0448-z`.

Use: the existing `NS-B1` packet binds the Type-I singularity route to a nontrivial mild bounded ancient solution satisfying their registered finite-`I` condition. This source is used only to keep the object class consistent with the existing lane; it does not imply Giga–Miura directional coherence.

## Analogue / disanalogue controls

Constantin–Fefferman and Beirão da Veiga–Berselli establish stronger direction-coherence criteria for finite-energy weak solutions. Giga–Miura is selected because its Type-I-specific theorem permits infinite energy and makes the blow-up/rigidity interface explicit. The old `NS-R001b` calibration only falsified *local positive-eigenframe alignment* as a standalone bridge; it did not test nonlocal vorticity-direction continuity, so it is a disanalogy rather than a refutation.

The half-space versions are also disanalogies: boundary pressure/Stokes compactness and boundary vorticity conditions are extra interfaces absent in the whole-space theorem selected here.

## Exact audit questions before a candidate

1. Does the high-vorticity threshold transport correctly under `omega_k=lambda_k^2 omega`?
2. Is convergence strong enough to define/pass `zeta_k` away from vorticity zeros?
3. Does the whole-space mild formulation remove the local-pressure/far-field interface rather than silently assume decay?
4. Does normalization prevent translation/dilation escape of the singular core without requiring global critical tightness?
5. Is nontriviality of limiting vorticity source-proved rather than inferred from velocity normalization alone?
6. Is the 3D-to-2D step an exact consequence of constant vorticity direction rather than an illicit equation substitution?
7. Is backward uniqueness absent from the chosen rigidity route?
8. What is the exact negation of the scale-critical directional criterion under hypothetical Type-I blow-up?
9. Does any statement concern Type-II? It must not.

## Pre-candidate authority

No theorem candidate or root claim is made in this packet. The source-valid discriminator is whether the Giga–Miura scale-critical criterion provides an exact *conditional* Type-I rigidity interface while finite-`I` alone still fails to supply its directional-coherence hypothesis.
