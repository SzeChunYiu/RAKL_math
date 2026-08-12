# YM-S1a2 R14 — SZZ clustering to the same OS transfer spectrum

**Authority:** proposal/shadow local composition only. No protected promotion, continuum theorem, lattice-spacing-uniform mass, asymptotic-freedom result, or root certificate.

**Root:** #5 (`OPEN_NO_SOLUTION_CERTIFICATE`)  
**Atom:** #88 (`YM-S1a2-SZZ-COVARIANCE-TO-SAME-OS-TRANSFER-SPECTRAL-GAP`)  
**Scope:** `d=4`, `G=SU(N)`, fixed unit lattice spacing, infinite volume, `0<beta<1/48`.

## Frozen chronology and exact dependencies

The pre-candidate fibre and trace were committed before this theorem-like local composition. The proof uses two prior proposal/shadow dependencies at exact heads:

- PR #240, head `90ff9f31d29be9317e9f7a77b8d82fcb7cd32f8b`: same SZZ infinite-volume Wilson measure inherits reflection positivity on the gauge-invariant bounded continuous positive-time cylinder algebra from matching finite periodic Wilson measures.
- PR #225, head `315a4cd2da3aa6b8f77a297e19a95162cbc666a9`: conditional density of centered smooth gauge-invariant positive-time cylinders in the OS excited sector once one same gauge/reflection-positive measure supplies both `L2` and the OS form.

Both dependencies remain draft/proposal-shadow. This R14 composition therefore inherits proposal/shadow authority even where its local mathematics is elementary.

## Primary-source packet

### Shen–Zhu–Zhu (SZZ)

H. Shen, R. Zhu, X. Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, arXiv:2204.12737v1.

For `SU(N)`, Assumption 1.1 is `|beta|<1/[16(d-1)]`; in four dimensions this is `|beta|<1/48`. Theorem 1.2 states that the whole periodic finite-volume Wilson sequence converges to the unique infinite-volume measure `mu^ym_{N,beta}`. The paper works on the common product configuration space `Q=G^{E+}` after periodic extension.

Corollary 1.6 applies to arbitrary smooth cylinder functions `f,g` with disjoint edge supports. It defines `d(A,B)` as the nearest distance between vertices in the two support edge sets and gives

`Cov_mu(f,g) <= c1 d(g) exp(-c_N d(Lambda_f,Lambda_g)) (|||f|||_infty |||g|||_infty + ||f||_2 ||g||_2)`,

where `c1` depends on support cardinalities while the exponent `c_N>0` depends on `K_S,N,d`, not on the chosen sources. Corollary 4.11 gives the same estimate for every tight limit, and uniqueness identifies that limit with `mu^ym_{N,beta}`.

The printed inequality is one-sided, not an absolute-covariance estimate. That sign detail is retained below rather than silently strengthened.

### Lüscher

M. Lüscher, *Construction of a Selfadjoint, Strictly Positive Transfer Matrix for Euclidean Lattice Gauge Theories*, DESY 76/54; Commun. Math. Phys. 54 (1977).

Equation (4) states physical/Osterwalder–Schrader positivity for gauge-invariant positive-time polynomials. Equation (5) constructs the physical Hilbert space by the reflected inner product, null quotient and completion. Immediately thereafter the Hamiltonian is obtained by identifying `e^{-aH}` with the operator `T` which shifts positive-time observables by one Euclidean lattice unit; the paper separately proves strict positivity of the Wilson transfer matrix. Proposition 2 reconstructs the Euclidean expectations as transfer-matrix Schwinger functions for the matching Wilson theory.

For this R14 argument the gauge-fixed canonical display is corroboration only. The actual infinite-volume object is the gauge-invariant OS quotient of the same SZZ measure; no gauge-fixed measure is substituted.

## Visual primary-source verification

Three load-bearing PDF surfaces were visually inspected in this cycle: SZZ Corollary 1.6, Lüscher's OS quotient/one-step-shift paragraph, and Lüscher's reconstruction/Proposition-2 page. All three screenshot attempts succeeded. The SZZ screenshot confirms the one-sided covariance sign and the source-independent exponent; the Lüscher screenshots confirm the quotient/completion, `e^{-aH}=T` one-step identification, and reconstruction statement.

## Elementary invariances on the exact SZZ limit

Every periodic finite-volume Wilson measure is invariant under lattice translations. For any bounded continuous cylinder `F` and fixed lattice translation `tau_k`, both `F` and `F o tau_k` are bounded continuous cylinders on the common product configuration space. Whole-sequence weak convergence therefore passes

`mu_L(F o tau_k)=mu_L(F)`

to

`mu(F o tau_k)=mu(F)`.

Thus the exact SZZ infinite-volume measure is translation invariant. Reflection invariance and gauge invariance are inherited by the analogous bounded-cylinder limit argument already typed in R13. Translation and reflection preserve cylinder smoothness, gauge invariance, support cardinality, `L2(mu)` norm and the SZZ derivative seminorm.

## Local proposition (proposal/shadow)

Let `mu=mu^ym_{N,beta}` in `d=4`, `G=SU(N)`, `0<beta<1/48`. Use the same Euclidean time reflection as in R13. Let `H_OS` be the gauge-invariant OS Hilbert space obtained from positive-time cylinders under `mu`, with vacuum `Omega=[1]`.

Then the one-step positive Euclidean time translation induces a positive self-adjoint contraction `T` on `H_OS`, `T Omega=Omega`. For every centered real smooth gauge-invariant positive-time cylinder `F`, there are finite constants `A_F,C_F` and the SZZ source-independent `c_N>0` such that, for all sufficiently large integers `n`,

`0 <= <[F],T^n[F]> <= A_F exp(-c_N n)`.

Because the real span of these centered source vectors is dense in the real excited sector, the complex span is dense in `Omega^perp`, and

`spec(T | Omega^perp) subset [0, exp(-c_N)]`.

Equivalently, for the fixed-cutoff OS Hamiltonian normalized by `T=e^{-H}` in unit lattice spacing, the excited spectrum starts at energy at least `c_N` in lattice units.

### Step 1 — the time shift descends as a contraction

Let `tau` denote one-unit positive Euclidean time translation. On positive-time cylinders define initially `T_0[F]=[tau F]`. Reflection and translation obey `theta tau = tau^{-1} theta`, while `mu` is translation invariant.

For a positive-time cylinder `F`, set

`a_m = ||[tau^m F]||_OS`.

Reflection positivity and OS Cauchy–Schwarz give

`a_1^2 = <[F],[tau^2 F]>_OS <= a_0 a_2`.

Iterating the same relation yields

`a_1 <= a_0^{1-2^{-r}} a_{2^r}^{2^{-r}}`.

The ordinary `L2(mu)` Cauchy–Schwarz bound gives `a_m <= ||F||_2`, uniformly in `m`, because translation preserves `mu`. Letting `r->infinity` gives `a_1<=a_0`. Therefore a null vector remains null under `tau`, and `T_0` descends to a contraction on the quotient and extends boundedly to `H_OS`.

The reflection/translation relation also gives symmetry:

`<[F],T[G]>_OS = <T[F],[G]>_OS`.

Hence the bounded extension is self-adjoint.

### Step 2 — positivity of the exact infinite-volume shift

The R13 same-measure construction used a cofinal reflection-compatible finite-volume Wilson sequence. On each sufficiently large member, Lüscher's Wilson transfer matrix is positive, so for every fixed gauge-invariant positive-time polynomial cylinder `P`,

`mu_L((theta P)(tau P)) >= 0`.

The integrand is a bounded continuous cylinder on the common compact product space. SZZ whole-sequence weak convergence passes the inequality to the exact infinite-volume measure:

`mu((theta P)(tau P)) >= 0`.

Uniform polynomial approximation plus compact gauge averaging, exactly as in R13, extends this to bounded continuous gauge-invariant cylinders. Thus `<[F],T[F]>_OS>=0` on a dense core. The bounded self-adjoint extension is therefore positive. Together with the contraction result, `0<=T<=I`. Translation invariance gives `T Omega=Omega`.

This step is where finite-volume transfer positivity is used; reflection positivity alone is not silently assumed to imply lattice one-step positivity.

### Step 3 — exact diagonal transfer moment is a translated SZZ covariance

For centered real smooth gauge-invariant positive-time `F`, the OS definition and the shift action give

`<[F],T^n[F]>_OS = mu((theta F)(tau_n F))`.

Reflection and translation invariance imply

`mu(theta F)=mu(F)=mu(tau_n F)=0`,

hence

`<[F],T^n[F]>_OS = Cov_mu(theta F, tau_n F)`.

Because `T` is positive, the left-hand side is nonnegative. Therefore SZZ's one-sided covariance estimate is sufficient; no unprinted absolute-value strengthening is needed.

### Step 4 — support distance is `n+O_F(1)`

Let `A` be the finite edge support of `theta F` and `B` the finite edge support of `F`. The support of `tau_n F` is `tau_n B`. For the translation-invariant lattice distance used by SZZ, the reverse triangle inequality on the finite vertex sets gives a finite source-dependent constant `C_F` such that

`d(A,tau_n B) >= n-C_F`.

Consequently the supports are disjoint for all sufficiently large `n`. Source support cardinality, smooth derivative seminorm and `L2(mu)` norm are invariant under `tau_n` and `theta`.

Applying Corollary 1.6 with `f=theta F`, `g=tau_n F` therefore gives an `n`-independent finite prefactor `B_F` and

`0 <= <[F],T^n[F]>_OS <= B_F exp[-c_N(n-C_F)] = A_F exp(-c_N n)`.

The crucial point is that `c_N` is common to the entire smooth-cylinder class. Source-dependent finite prefactors do not affect the `n`th-root rate.

### Step 5 — dense-source moment decay excludes slower transfer spectrum

Let `q=exp(-c_N)<1`. For any source vector `psi=[F]` above, the positive self-adjoint contraction has a spectral measure `nu_psi` on `[0,1]` with

`<psi,T^n psi> = integral lambda^n d nu_psi(lambda) <= A_psi q^n`

for all sufficiently large `n`.

If `nu_psi((q,1])>0`, then for some `epsilon>0` it has positive mass on `[q+epsilon,1]`, forcing the moment to be at least a positive constant times `(q+epsilon)^n`, contradicting the displayed bound. Hence `nu_psi((q,1])=0` for every controlled source vector.

PR #225 gives density of centered smooth gauge-invariant positive-time cylinder vectors in `Omega^perp` under the same-measure hypotheses now supplied by R13/R14. Therefore the bounded spectral projection `E_T((q,1])` vanishes on a dense subset of `Omega^perp` and hence on the whole excited sector. Thus

`spec(T|Omega^perp) subset [0,q]`.

With `T=e^{-H}` in unit lattice spacing, the fixed-cutoff OS Hamiltonian gap is at least `c_N` in lattice units. The argument simultaneously excludes an additional `T=1` vector in `Omega^perp`; no separate vacuum-uniqueness assumption is imported from Lüscher's finite-volume reconstruction discussion.

## Hostile controls and disanalogies

- **Langevin versus physical time:** SZZ's Markov semigroup is never identified with `T`; only static SZZ covariance under Euclidean lattice translation is used.
- **One-sided covariance:** the source prints `Cov <= ...`, not `|Cov| <= ...`; positivity of the diagonal physical transfer moment supplies the needed lower sign.
- **Reflection positivity versus one-step positivity:** one-step positivity is separately passed from the matching finite Wilson transfer matrices through weak convergence.
- **Finite prefactors:** support-dependent constants are harmless only because `c_N` is common and support distance grows linearly in `n` up to an additive source constant.
- **Density:** density is in the same OS quotient of the same `mu`, not imported from a fixed-graph spin-network basis or another measure.
- **Gauge:** no gauge-fixed probability measure is used in the infinite-volume proof.
- **Cutoff:** `c_N` is a dimensionless lattice exponent at spacing one. No statement is made that `c_N(a)/a` stays positive as `a->0`.

## Same-context expert cell

1. **Constructive QFT / OS reconstruction:** accepted the same-measure quotient identity and contraction argument; required separate one-step positivity rather than deriving it from reflection positivity by slogan.
2. **Lattice gauge transfer theory:** checked the Wilson action/reflection dependency and the finite-volume positive-transfer input used in the weak-limit step.
3. **Spectral analysis:** checked the common-`q` spectral-measure exclusion and that source-dependent finite prefactors do not weaken the spectral edge.
4. **SZZ probability:** checked the exact Corollary 1.6/4.11 scope, one-sided sign, source-independent `c_N`, support metric, and translation-invariance inheritance.
5. **Gauge theory:** checked that reflection/translation preserve the gauge-invariant source class and that no gauge-fixed substitute is used.
6. **Continuum/RG:** rejected any `a->0`, asymptotic-freedom, renormalized-mass, or continuum spectral promotion from the fixed-cutoff result.
7. **Adversarial proof/provenance/metrology:** checked the pre-candidate chronology, draft dependency heads, authority boundary, and zero independent-review credit.

All seven roles shared this evidence context. They count as `0/3` independent mathematical reviews.

## Episode -> diagnosis -> obstruction/lesson separation

**Episode:** `EP-YM-S1a2-R14-20260812`.

**Diagnosis:** `DG-YM-S1a2-R14-SAME-OS-TRANSFER-GAP-GLUE-PASS-SHADOW` — the post-RP fixed-cutoff transfer bridge is locally composable once one-step positivity is passed separately and the one-sided SZZ sign is handled through diagonal transfer positivity.

**Existing obstruction affected:** `F-YM-S1A2-OS-SZZ-SAME-THEORY-GLUING-UNBOUND` is locally discharged at fixed lattice spacing by the R11/R13/R14 chain. It remains relevant as provenance for the continuum/RG transport problem but no longer blocks the fixed-cutoff same-measure spectral identification.

**New failures:** none.

**New obstruction:** none minted. The residual moves to lattice-spacing-uniform RG/continuum transport rather than creating another local obstruction node.

**Lesson:** none minted. This is a standard compositional spectral argument and remains proposal/shadow.

## Residual

**Before:** `RES-YM-S1a2-POST-RP-COVARIANCE-TO-TRANSFER-MOMENTS-PLUS-SOURCE-COMPLETENESS-AND-PHYSICAL-GAP-UNBOUND`.

**After:** `RES-YM-S1a1-FIXED-CUTOFF-GAP-CLOSED-BUT-LATTICE-SPACING-UNIFORM-RG-CONTINUUM-SPECTRAL-TRANSPORT-UNBOUND`.

The next admissible discriminator is not another fixed-cutoff clustering theorem. It is a same-theory continuum/RG statement that transports a positive **physical** spectral scale through `a->0`, while preserving the Euclidean measure, gauge-invariant OS source algebra, quotient/Hilbert space, time normalization, continuum subsequence, nontriviality, and asymptotically-free short-distance behavior.

Root #5 remains `OPEN_NO_SOLUTION_CERTIFICATE`.
