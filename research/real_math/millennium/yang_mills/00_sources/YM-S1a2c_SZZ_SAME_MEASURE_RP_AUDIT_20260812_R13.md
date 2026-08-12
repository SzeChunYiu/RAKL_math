# YM-S1a2c R13 — SZZ strong-coupling limit / same-measure reflection-positivity audit

**Authority:** proposal/shadow local composition only. No root promotion, protected lesson/obstruction, continuum theorem, physical-gap claim, or independent-review credit.

**Root:** #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Atom:** #238 (`YM-S1a2c-SZZ-STRONG-COUPLING-LIMIT-SAME-MEASURE-REFLECTION-POSITIVITY`)  
**Scope:** four-dimensional `SU(N)`, unit lattice spacing, fixed positive strong coupling `0 < beta < 1/48`, periodic finite volumes to the SZZ infinite-volume measure only.

## Frozen chronology

Issue #238 was already a durable prospective source-binding atom before the source acquisition and theorem composition recorded here. Its success contract requires the same Wilson action, compatible periodic/reflection geometry, a cofinal reflection-compatible volume subsequence, bounded-continuous reflected cylinder integrands, and separate typing of gauge/reflection invariance and source algebra. This R13 packet does not backfill root-level discovery credit.

## Primary source A — exact finite and infinite SZZ measures

H. Shen, R. Zhu, X. Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, arXiv:2204.12737.

The source defines the finite periodic lattice and Wilson measure in (1.1)–(1.2):
`d mu_{Lambda_L,N,beta} = Z^{-1} exp(N beta Re sum_{p in P^+} Tr(Q_p)) prod_e d sigma_N(Q_e)`.
For `SU(N)`, Assumption 1.1 is `|beta| < 1/[16(d-1)]`; in `d=4` this is `|beta|<1/48`. The paper defines the common infinite product configuration space `Q=G^{E+}`, extends every finite periodic measure to it by periodic extension, and Theorem 1.2 states that the whole finite-volume sequence converges weakly to the unique infinite-volume measure `mu^ym_{N,beta}`. These are exact same-measure data, not a reconstructed analogue.

## Primary source B — finite periodic Wilson reflection/physical positivity

M. Lüscher, *Construction of a Selfadjoint, Strictly Positive Transfer Matrix for Euclidean Lattice Gauge Theories*, DESY 76/54 (published version: Commun. Math. Phys. 54 (1977)).

The source uses a four-dimensional `SU(N)` Wilson lattice gauge theory. Its gauge plaquette term has coefficient `1/(2 g_0^2)` on the two plaquette orientations, i.e. `g_0^{-2} Re Tr(U_p)` per unoriented plaquette. Thus the pure-gauge weight matches SZZ after the positive-coupling identification
`g_0^{-2}=N beta`.

The source states OS positivity in its equation (4) for gauge-invariant positive-time polynomials. In the transfer-matrix construction, the gauge contribution is displayed in (20)–(21); Proposition 1 proves strict positivity of the transfer matrix, with the gauge-link kernel positivity reduced in (22)–(23) to positive character/Fourier coefficients. The reconstruction section chooses periodic boundary conditions for the gauge field in both spatial and time directions. Proposition 2 identifies the finite-volume Euclidean expectations with the transfer-matrix Schwinger functions and explicitly states that this proves Osterwalder–Schrader positivity (4).

The load-bearing pages were checked in parsed primary-PDF text. Visual checks succeeded for the Wilson action page and the gauge-kernel positivity page; the web PDF screenshot backend repeatedly failed on the Proposition-2 page, so that page was independently rendered from the same downloaded primary PDF and visually inspected. This visual fallback is verification only, not a separate source.

## Local composition

### Proposition (proposal/shadow local certificate)

Let `d=4`, `G=SU(N)`, and `0<beta<1/48`. Let `mu_L=mu_{Lambda_L,N,beta}` be the SZZ periodic Wilson measures, periodically extended to the common compact product configuration space `Q`, and let `mu=mu^ym_{N,beta}` be their SZZ weak limit.

Fix the Euclidean time reflection `theta` used by the finite Wilson positivity construction. For every gauge-invariant bounded continuous cylinder function `F` supported strictly in the positive-time half lattice,
`int_Q overline(F(theta Q)) F(Q) d mu(Q) >= 0`.

### Proof

1. **Same action/coupling.** For positive `beta`, set `g_0^{-2}=N beta`. The SZZ plaquette density and the Lüscher pure Wilson gauge plaquette density are then the same finite-volume probability weight, up to the notational choice of oriented versus unoriented plaquette summation.

2. **Compatible cofinal geometry.** Restrict SZZ's whole sequence to a cofinal odd side-length subsequence `L_j=2m_j+1`. This fits the periodic odd-site geometry used in the transfer construction. For a fixed finite positive-time cylinder support, choose `j` large enough that the support and its reflected support do not meet a periodic wrap seam. The finite-torus reflection then agrees with the infinite-lattice reflection on all variables in the integrand. Since SZZ proves convergence of the whole sequence, this cofinal subsequence has the same weak limit `mu`.

3. **Finite-volume polynomial positivity.** For every gauge-invariant positive-time polynomial cylinder `P`, Lüscher's finite periodic Wilson reconstruction gives
`int overline(P(theta Q)) P(Q) d mu_{L_j}(Q) >= 0`
for all sufficiently large `j` in the compatible subsequence.

4. **Pass to the SZZ limit.** The reflected quadratic integrand
`H_P(Q)=overline(P(theta Q)) P(Q)`
depends on finitely many link variables and is continuous. Because each link group is compact, it is also bounded. SZZ weak convergence on the common product space therefore gives
`int H_P d mu = lim_j int H_P d mu_{L_j} >= 0`.

5. **Extend from polynomial to bounded continuous gauge-invariant cylinders.** A fixed cylinder `F` is a continuous function on a finite product `SU(N)^m`. The unital self-adjoint algebra generated by matrix-coordinate functions and their conjugates separates points, so Stone–Weierstrass gives uniform polynomial approximation `P_n -> F`. Average each `P_n` over the compact finite vertex gauge group acting on those links. Because `F` is gauge invariant, the averaged polynomial `P_n^G` remains a polynomial, is gauge invariant, uses no new link variables, and satisfies
`||P_n^G-F||_infty <= ||P_n-F||_infty`.
The OS quadratic functional is continuous in uniform norm for a probability measure, hence positivity passes from `P_n^G` to `F`.

This closes the exact same-measure reflection-positivity coordinate posed in #238 at proposal/shadow authority.

## Gauge and reflection invariance are separate

No gauge fixing is imported into the SZZ measure. Finite Wilson measures are gauge invariant because each plaquette trace is invariant under local conjugation and product Haar measure is invariant. For any fixed local gauge transformation and finite cylinder test, sufficiently large tori realize the same transformation without wrap ambiguity, so weak convergence transfers gauge invariance to `mu`.

Likewise, the periodic Wilson action and Haar product measure are invariant under the lattice time reflection (plaquette orientations are reversed but `Re Tr(U_p)=Re Tr(U_p^{-1})`). The same finite-cylinder weak-limit argument transfers reflection invariance to `mu`.

These invariances do not replace OS positivity; they are typed separately as required by #238.

## Analogue / disanalogy audit

- **Valid composition:** finite Wilson RP -> weak limit is valid only because the reflected quadratic functional is a bounded continuous cylinder on the exact common configuration space.
- **Invalid analogue rejected:** SZZ's own use of the phrase “mass gap” for exponential correlation decay is not a physical OS Hamiltonian gap certificate.
- **Invalid source transfer rejected:** a positivity theorem for a different gauge action, nonperiodic finite measure, or gauge-fixed measure would not have discharged this atom.
- **Continuum disanalogy:** this result is fixed lattice spacing. It supplies no uniformity as `a -> 0`.

## Same-context expert cell

1. **Lattice gauge transfer-matrix specialist:** verified the Wilson plaquette normalization match, positive coupling, periodic gauge boundary conditions, polynomial OS core, and odd cofinal geometry.
2. **Constructive QFT / OS specialist:** verified that RP is passed only on a typed positive-time gauge-invariant cylinder algebra and that null-quotient/source-completeness questions remain downstream.
3. **Gibbs / weak-limit probability specialist:** verified common compact product space, whole-sequence -> subsequence convergence, and bounded-continuous test-function passage.
4. **Gauge-theory specialist:** verified gauge invariance and reflection invariance separately and rejected any need to switch to a gauge-fixed measure.
5. **Spectral specialist:** rejected promotion from this RP statement or SZZ support-distance clustering to a physical Hamiltonian mass gap without the missing covariance-to-transfer-moment/source-completeness bridge.
6. **RG / continuum specialist:** verified that no lattice-spacing, regulator, renormalization, or continuum uniformity is supplied by this fixed-cutoff result.
7. **Adversarial proof/provenance + RAKL v3 assurance:** checked the #238 prospective contract, source identities, authority boundary, and zero independent-review credit.

All seven roles share the same context. They are not independent reviews and count `0/3`.

## Episode -> diagnosis -> obstruction/lesson separation

**Episode:** `EP-YM-S1a2c-R13-20260812`.

**Diagnosis:** `DG-YM-S1a2c-R13-SAME-MEASURE-RP-GLUE-PASS-SHADOW` — the #238 same-measure RP coordinate is locally composable from exact primary-source premises plus elementary weak-limit/density steps.

**Existing obstruction affected:** `F-YM-S1A2-OS-SZZ-SAME-THEORY-GLUING-UNBOUND` is only partially discharged: its same-measure RP coordinate is closed, while covariance-to-transfer moments, quotient/source completeness, and physical-gap identification remain open.

**New failures:** none.

**New obstruction:** none.

**Lesson:** none minted. The local composition is standard and proposal/shadow only; no protected reusable lesson is promoted.

## Residual

**Before:** `RES-YM-S1a2c-SZZ-LIMIT-SAME-MEASURE-RP-UNBOUND`.

**After:** `RES-YM-S1a2-POST-RP-COVARIANCE-TO-TRANSFER-MOMENTS-PLUS-SOURCE-COMPLETENESS-AND-PHYSICAL-GAP-UNBOUND`.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.
