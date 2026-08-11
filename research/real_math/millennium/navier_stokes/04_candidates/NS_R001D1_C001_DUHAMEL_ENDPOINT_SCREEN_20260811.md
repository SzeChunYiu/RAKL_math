# NS-R001d1-C001 — unsigned Duhamel endpoint closure screen

## Authority and chronology

This is the first post-gate candidate for frozen atom `NS-R001d1`. The pre-candidate packet on PR #48 passed its pinned exact-head application workflow before this candidate was authored. Current framework `SzeChunYiu/RAKL@a151d5612709ea0f95c3ea232630f246f722739a` was re-read before generation; its v3 recursive-experience layer adds immutable `TaskEpisode` evidence and preserves the mathematical context/memory/trace pre-candidate gates. Pending PR #33 has failed its exact-head application workflow and is not imported as accepted failure memory.

No Navier–Stokes theorem, regularity criterion, singular solution, novelty claim, or root authority is asserted.

## Exact proof architecture under test

On `R^3`, write the mild equation

\[
u(t)=e^{\nu t\Delta}u_0-\int_0^t e^{\nu(t-s)\Delta}\mathbb P\nabla\cdot(u\otimes u)(s)\,ds.
\]

The standard derivative heat estimate has the dimensionally exact form

\[
\|\nabla e^{\nu r\Delta}F\|_{L^3_x}
\le C_h(\nu r)^{-3/4}\|F\|_{L^2_x},
\]

where `1/2` derivative loss plus `1/4` of `L^2 -> L^3` smoothing produces the temporal power `3/4`. Since the Leray projector is order zero on the relevant Lebesgue spaces, the unsigned scalar estimate gives

\[
\|B(u,u)(t)\|_3
\le C_h\nu^{-3/4}\int_0^t(t-s)^{-3/4}\|u(s)\|_3\|u(s)\|_6\,ds.
\]

If

\[
M_t=\sup_{0<s<t}\|u(s)\|_3,\qquad g(s)=\|u(s)\|_6,
\]

then

\[
\|B(u,u)(t)\|_3\le C_h\nu^{-3/4}M_t\,J_t(g),\qquad
J_t(g)=\int_0^t(t-s)^{-3/4}g(s)\,ds.
\]

The Leray energy inequality plus Sobolev yields only

\[
\|g\|_{L^2(0,t)}
\le C_S\nu^{-1/2}\|u_0\|_2
\]

(up to the conventional factor from the energy normalization).

### Candidate hypothesis `H_endpoint`

The direct semigroup/energy closure would require a finite coefficient `K(t)` such that

\[
J_t(g)\le K(t)\|g\|_{L^2(0,t)}
\]

for every nonnegative scalar profile `g in L^2(0,t)` compatible with the information retained by this unsigned reduction.

The registered hostile control is a unit-`L^2` pulse concentrating at `s=t`.

## Scaling, dimensions, endpoint, and scope checklist

- True Navier–Stokes scaling: `u_lambda(x,t)=lambda u(lambda x,lambda^2 t)`.
- `||u||_3` is critical: scaling exponent `0`.
- `g=||u||_6` scales pointwise as `lambda^(1/2)`.
- `||g||_{L^2_t}` scales as `lambda^(-1/2)`, the same supercritical defect as the energy level.
- `J_t(g)` is invariant when time is rescaled parabolically, so an energy-only pointwise estimate has a criticality mismatch unless additional concentration-sensitive information enters.
- Units: `(nu r)^(-3/4)` has length unit `L^(-3/2)`; after multiplication by `||u tensor u||_2` and `ds`, the result has the `L^3_x` velocity norm unit `L^2/T`.
- Pressure/nonlocality: `P` is retained only through its norm boundedness; all pressure/Leray cancellation and coherence are deliberately discarded. A negative result therefore cannot rule out a pressure-coherent repair.
- Domain: whole space `R^3`; no boundary terms.
- Derivative loss: exactly one spatial derivative from `div`, represented by the extra heat factor `r^(-1/2)`.
- Endpoint warning: the kernel `r^(-3/4)` is not in `L^2(0,t)`, so the obvious `L^2_t` Cauchy–Schwarz closure is not licensed.
- Candidate authority: proof-architecture discriminator only.

## Source boundary

Primary anchors remain the frozen NS-R001d1 source packet: Fefferman's Clay problem description; Barker–Prange on localized critical smoothing (`arXiv:1812.09115`); Miller on strain/vorticity and advection depletion (`arXiv:2407.02691`); Cheskidov–Eguchi on finite-energy frequency-local critical smallness (`arXiv:2503.11642`); and Coiculescu–Palasek on large critical-data behavior (`arXiv:2503.14699`). None of these sources is cited as supplying `H_endpoint`.
