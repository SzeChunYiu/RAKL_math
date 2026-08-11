# NS-B2a C001 R1 — F=1 ancient-Euler cutoff / gluing audit

**Authority:** proposal/shadow route diagnostic only. Root status remains `OPEN_NO_SOLUTION_CERTIFICATE`. This is not a Navier–Stokes theorem, not an Euler Liouville theorem, and not independent review.

## Exact source binding

Seregin, arXiv:2606.29468v1, Theorem 3.1 produces a nontrivial ancient Euler pair `(u,p)` on `R^3 x (-infinity,0)` with (3.5), Euler equation (3.6), local energy inequality (3.7), and nontriviality (3.8). In the logarithmic example immediately following the theorem, `F(a)=1`. The proof records compactness only on every fixed `Q(a)`: strong local `L_{3 nu}` for `1 <= nu < 10/9`, weak-star local `L_{2,infinity}`, and weak local gradient `L2`.

The equation change is load-bearing: the limit is Euler. Standard parabolic Navier–Stokes backward uniqueness is therefore not a valid closure operator.

## Discriminator: large-radius cutoff scaling

Freeze a standard cutoff on radius `R` with `|grad phi_R| = O(R^-1)` and a temporal transition of length `O(R^2)` with `|partial_t phi_R| = O(R^-2)`.

For `F=1`, (3.5) gives, schematically and uniformly in `R`,

- `sup_t int_{B_R}|u|^2 <= C R`;
- `int_{Q_R}|grad u|^2 <= C R`;
- `int_{Q_R}|p|^(3/2) <= C R^2`.

The standard local multiplicative inequality from the first two bounds gives `int_{Q_R}|u|^3 <= C R^2`. Hence the absolute cutoff terms satisfy

- temporal term: `R^-2 int_{Q_R}|u|^2 <= C R`;
- cubic boundary flux: `R^-1 int_{Q_R}|u|^3 <= C R`;
- pressure work, by Hölder: `R^-1 int_{Q_R}|p||u| <= C R`.

So the source-critical magnitude ledger does **not** make the standard large-radius cutoff errors tend to zero. This only prunes the direct absolute-estimate route; sign/cancellation or an additional source-valid tail observable could still close the interface.

## Quantifier / compactness audit

The source convergence is valid after fixing `R` (or `a`) and then passing to the blow-up subsequence. A global tail statement needed for rigidity has the opposite extra limit: `R -> infinity`. Fixed-radius convergence by itself does not provide a uniform-in-sequence tail estimate and does not authorize interchange of these limits. This is a local-to-global/gluing obstruction, not a failure of Seregin's local extraction.

Pressure localization has the same issue: local `D_F` control gives the correct critical magnitude but no vanishing annular pressure-work tail. Noncompact translations/dilations/profile leakage therefore remain live.

## Same-source positive analogue

Seregin's Section 4 is instructive rather than contradictory. In an axisymmetric higher-regularity branch, the paper introduces an additional condition (4.4) specifically so that spatial cutoff-derivative terms tend to zero as the cutoff radius goes to infinity before obtaining a conservation law. That is a source-internal witness that a large-radius decay coordinate can be a separate rigidity input.

## Adversarial-source check

Gavrilov's nontrivial smooth compactly supported steady Euler solution is **not** a counterexample to the F=1 source class. For nonzero steady compactly supported `U`, once `R` contains the support,

`R^-1 int_{-R^2}^0 int_{B_R}|grad U|^2 = R ||grad U||_2^2`,

which diverges. The candidate adversary is therefore rejected by the exact source signature.

## Outcome

`TRANSFER_BLOCKED_SCOPED / F1_STANDARD_CUTOFF_SCALE_NEUTRAL / GLOBAL_FLUX_TIGHTNESS_NOT_INHERITED_BY_FIXED_RADIUS_COMPACTNESS`.

Local mathematics: no source theorem is refuted and no local Euler contradiction is obtained.

Local-to-global/gluing: open. The missing certificate is a source-valid large-radius tail/no-incoming-flux, cancellation, or other scale-breaking coordinate that is inherited **before or through** the Euler limit.

Backward uniqueness: inapplicable at this node because the limit equation is Euler.

Type-I geometry/amplitude lanes: separate. Type-II outside Seregin's registered scenario: untouched.

## Next atom

`NS-B2a1`: freeze a quantitative annular energy/pressure-flux tightness target and test whether it is inherited from the original suitable weak Navier–Stokes sequence under Seregin's Euler scaling. Search same-source/same-equation mechanisms first; do not invent a generic Euler Liouville theorem until this gluing input is either produced or replaced by an exact rigidity theorem consuming only (3.5)-(3.8).
