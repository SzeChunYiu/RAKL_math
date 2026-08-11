# YM-E1a1-C001 — local Haar concatenation leakage

**Status:** `EXACT_LOCAL_NEGATIVE_CALIBRATION / NO_NOVELTY_CLAIM / ROOT_AUTHORITY_NONE`

**Atom:** `YM-E1a1`  
**Context hash:** `sha256:95fe4879b25e9319e2de43ae287b467b86138752e66fd6dfa380e3a810d59802`  
**Pre-candidate trace terminus:** `sha256:55a16ceb14d6fed05212e9c577bdd7b49a0c94b12f9cc9b8a6e07e68425e3d33`

## Candidate question

Can a deliberately tiny finite marked vocabulary that records individual fundamental plaquette/single-contour scalar marks but omits their concatenated contour be exactly closed even under the simplest local gauge integration tangent?

The candidate is a counterexample-first calibration, not a proposed continuum theorem.

## Exact local setup

Let \(G=SU(N)\) with \(N\ge 3\), and let \(dU\) be normalized Haar measure. Arrange two adjacent oriented plaquettes so their shared link \(U\) appears with opposite orientation. Products of the exterior links give \(A,B\in SU(N)\). Write the oriented source loop and neighboring interaction factor as

\[
W_A(U)=\operatorname{Tr}(AU),
\qquad
X_B(U)=\operatorname{ReTr}(U^\dagger B).
\]

Define the normalized local source transport

\[
F_t(A,B)
=
\frac{\int_G \operatorname{Tr}(AU)
        e^{\,t\,\operatorname{ReTr}(U^\dagger B)}\,dU}
     {\int_G e^{\,t\,\operatorname{ReTr}(U^\dagger B)}\,dU}.
\]

At \(t=0\), \(\int \operatorname{Tr}(AU)dU=0\) and
\(\int \operatorname{ReTr}(U^\dagger B)dU=0\), so the normalization derivative contributes nothing. Hence

\[
F'_0(A,B)
=
\int_G\operatorname{Tr}(AU)\operatorname{ReTr}(U^\dagger B)\,dU.
\]

## Exact contraction

Expand the real part:

\[
F'_0
=
\frac12\int\operatorname{Tr}(AU)\operatorname{Tr}(U^\dagger B)dU
+
\frac12\int\operatorname{Tr}(AU)\operatorname{Tr}(B^\dagger U)dU.
\]

Schur/Haar orthogonality gives

\[
\int_G U_{ji}\,\overline{U_{lk}}\,dU
=
\frac1N\delta_{jl}\delta_{ik},
\]

and therefore

\[
\int_G\operatorname{Tr}(AU)\operatorname{Tr}(U^\dagger B)dU
=
\frac1N\operatorname{Tr}(AB).
\]

For the second integral choose the primitive central element
\(zI\in SU(N)\), \(z=e^{2\pi i/N}\). Under \(U\mapsto zU\) the integrand
\(\operatorname{Tr}(AU)\operatorname{Tr}(B^\dagger U)\) is multiplied by
\(z^2\). Normalized Haar measure is invariant, and \(z^2\ne1\) for
\(N\ge3\). Thus that integral is zero. Consequently

\[
\boxed{F'_0(A,B)=\frac{1}{2N}\operatorname{Tr}(AB)}
\qquad (N\ge3).
\]

If instead the interaction is parameterized in Wilson form
\(\exp[(\beta/N)\operatorname{ReTr}(U^\dagger B)]\), the corresponding
\(\beta\)-derivative is \(\operatorname{Tr}(AB)/(2N^2)\).

Geometrically, \(AB\) is the holonomy of the concatenated boundary obtained by canceling the shared oppositely oriented link: for adjacent plaquettes this is the \(1\times2\) rectangular contour.

## Planted SU(3) independence witness

Let

\[
P=\begin{pmatrix}
0&1&0\\
0&0&1\\
1&0&0
\end{pmatrix}\in SU(3).
\]

Both \(P\) and \(P^2\) have trace zero.

- With \(A=P,B=P\): \(\operatorname{Tr}(A)=\operatorname{Tr}(B)=0\) and \(\operatorname{Tr}(AB)=\operatorname{Tr}(P^2)=0\).
- With \(A=P,B=P^2\): the same separate scalar traces remain zero, but \(\operatorname{Tr}(AB)=\operatorname{Tr}(I)=3\).

Therefore the generated concatenated-loop coordinate cannot be reconstructed from the two separate scalar trace coordinates used by the deliberately tiny vocabulary.

## Result

`FINITE_CLOSURE_LEAK` is observed for the registered local calibration. Any marked source vocabulary that omits the concatenated rectangle (or an equivalent coordinate able to represent \(\operatorname{Tr}(AB)\)) is not exactly closed under this local Haar-elimination tangent.

This result is stronger than a numerical example but much narrower than a Yang–Mills RG theorem. It does **not** establish:

- failure of a graded/quasi-local loop/polymer/spin-network marked space;
- failure of Balaban's actual weak-coupling block transformation;
- uncontrolled support or norm growth;
- failure or preservation of reflection positivity;
- continuum existence, non-triviality, OS reconstruction, correlation decay, or a mass gap.

The \(SU(2)\) pseudoreal case is excluded from this candidate because the center argument does not kill the two-\(U\) contraction there.

## Failure diagnosis and next atom

The local failure is representation-level **operator/geometry proliferation**: the mark vocabulary is too small. The failure-lattice diagnosis remains `SUPPORTED` rather than being generalized to a method-wide impossibility.

Open child residual `YM-E1a1a`:

> Define the minimally widened graded/quasi-local gauge-invariant marked space carrying contour geometry, representation/multi-loop labels, support/reflection-buffer coordinates and a weighted complexity norm; then test an actual weak-coupling Balaban-style block for controlled mixing plus typed remainder and a scale-explicit one-step norm bound.

`YM-E1a1a` requires a fresh context fiber, dual-memory review, same-context expert cell and hash-chained pre-candidate trace before any candidate is generated.
