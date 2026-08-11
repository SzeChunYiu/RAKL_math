# RH-ANA-003 — current zero-density / zero-free + finite-prefix standalone closure is insufficient

**Atom:** `RH-ANA-003`  
**Frozen fibre:** `sha256:31e2fc6491b0b61f8e7b7b96c668592b860b37166dc84e12cb488b3a19bb985d`  
**Pre-action receipt:** `pre_action_receipt:ef4ceea2dd867fd33ba2e95d1f2e0981edfcf0b093cb07a0c36c201b962ebefb`  
**Outcome branch:** `REFUTED_CURRENT_DENSITY_STANDALONE_CLOSURE`  
**Authority:** scoped inference-form obstruction only; **not** an RH theorem and **not** an impossibility theorem for future zero-density, mollifier, resonance, explicit-formula, or zero-detection methods.

## 1. Exact target preserved

The root remains the classical Riemann Hypothesis: every nontrivial zero `rho` of `zeta(s)` satisfies `Re(rho)=1/2`. Fix `sigma>1/2`. Let

`N_sigma(T) = #{rho=beta+i gamma : beta>=sigma, 0<gamma<=T}`,

with multiplicity. RH is equivalent to `N_sigma(T)=0` for every fixed `sigma>1/2` and every `T`.

The current child question is narrower: can the presently selected zero-density/zero-free theorems, together with rigorous verification through a finite height, close the infinite tail **without adding another root-strength mechanism**?

## 2. Density-to-exclusion threshold lemma

Let `H>0` be a rigorously verified height at which `N_sigma(H)=0`. Cover the tail by dyadic blocks and define

`M_sigma,k = N_sigma(2^(k+1) H) - N_sigma(2^k H)`, `k>=0`.

Each `M_sigma,k` is a nonnegative integer. Therefore a rigorous bound

`M_sigma,k <= B_sigma,k < 1` for every `k>=0`

forces `M_sigma,k=0` for every block and hence excludes all zeros with `beta>=sigma` above `H`.

More generally, any exact local-tail bound that is eventually `<1`, plus rigorous checking of the finitely many preceding blocks, yields the same exclusion. This is merely integrality of the zero count; it does not assume RH.

## 3. Countermodel to the standalone cumulative-density inference

A cumulative upper bound does not imply emptiness merely because its exponent is small. Suppose the only tail theorem available has the shape

`N_sigma(T) <= B_sigma(T)`

and its right side permits values `>=1` for arbitrarily large `T`. Then that inequality alone cannot logically force `N_sigma(T)=0`: the synthetic monotone integer count

`N_tilde(T)=0` for `T<H`, and `N_tilde(T)=1` for `T>=H`

is a DifferenceWitness for the inference form whenever `B_sigma(T)>=1` on the relevant tail. This witness is **not** asserted to be a possible zeta zero distribution; it proves only that the stated numerical upper-bound premise, without additional zeta-specific structure, has not encoded zero occupancy.

The same point survives an `O(1)` cumulative bound if its allowed constant is at least one, and a vanishing *proportion* of off-line zeros can coexist logically with sparse exceptions. Thus the authority-changing threshold for a direct count argument is zero occupancy (or a local upper bound below one), not merely a better positive density exponent.

## 4. Test of the frozen primary-source bounds

### Guth–Maynard 2026

Guth and Maynard obtain the current uniform non-explicit estimate

`N(sigma,T) <= T^(30(1-sigma)/13 + o(1))`.

For every fixed `sigma<1`, the exponent `30(1-sigma)/13` is strictly positive. Hence the displayed upper-bound scale grows with `T`; it does not tend to zero and does not force any dyadic tail count below one. The one-defect DifferenceWitness remains compatible with the *shape* of this bound for sufficiently large `T`. Therefore this density estimate, by itself, does not close the RH tail.

This is not a criticism of the theorem: it is a strong density result with applications to large values and primes. It simply optimizes a coordinate different from exact zero occupancy.

### Bellotti 2024 explicit log-free density

Bellotti proves explicit estimates of the form

`N(sigma,T) <= C T^(B(1-sigma))`

in specified near-one ranges. In the displayed uniform range `sigma>=0.9927`, `3*10^12<T<=exp(6.7*10^12)`, the paper gives `B=1.448` and `C=1.62*10^11`. For any fixed `sigma<1` in that range the exponent is positive and the constant is positive, so the bound is not an emptiness certificate. At `sigma=0.9927` and `T=3*10^12`, the stated uniform right-hand side is about `2.19*10^11`, a calibration showing the large separation from the `<1` occupancy threshold; no numerical value is used as proof.

The source itself explicitly distinguishes the Density Hypothesis from RH and notes that log-free density can yield an absolute *constant* bound when `sigma=1-lambda/log T`; a positive constant bound still does not, without a `<1` constant or additional structure, force zero occupancy.

### Mossinghoff–Trudgian–Yang zero-free region

Their explicit Vinogradov–Korobov region excludes zeros for

`Re(s) >= 1 - 1/[55.241 (log|t|)^(2/3) (log log|t|)^(1/3)]`

in the stated height range. Its left boundary tends to `1` as `|t|` grows. Consequently it does not cover a fixed half-strip `Re(s)>=sigma` for any fixed `sigma<1` at all sufficiently large heights. It supplies exact zero occupancy only in a shrinking neighborhood of the `1`-line, leaving the rest of the RH half-strip unresolved.

### Platt–Trudgian finite verification

The rigorous interval-arithmetic verification through height `3*10^12` closes the bounded-height prefix. It contributes no theorem about the tail above that height unless paired with a separate tail-exclusion result.

## 5. Outcome and diagnosis boundary

**Episode outcome:** `REFUTED_CURRENT_DENSITY_STANDALONE_CLOSURE`.

What has been refuted is the following **standalone route**: finite-height verification + the selected current cumulative zero-density estimates + the selected near-one zero-free region, with no new local zero detector, no new sign/positivity theorem, and no additional exact explicit-formula mechanism, are sufficient to exclude all off-critical tail zeros.

This result does **not** refute:

- a future zero-density argument that yields a genuinely local tail count tending below one;
- a mollifier/resonance/large-value argument that makes even one off-line zero contradictory;
- zero repulsion or another zeta-specific localization theorem that upgrades density to exclusion;
- a rigorously justified explicit-formula or Li/Weil transform whose exact weights convert available density information into a decisive signed tail bound;
- a stronger theorem that directly excludes zeros in the full fixed half-strip.

## 6. Residual after the falsifier

The useful next residual is qualitative rather than another exponent optimization:

> Find a zeta-specific mechanism that changes the semantic target from “few possible off-line zeros” to “no possible off-line zero”: either a local count bound eventually `<1`, a contradiction caused by a single hypothetical off-line zero, or an exact weighted prime/archimedean tail inequality whose fully audited transform and sign control exclude such a zero.

For RH-ANA-003, merely decreasing a positive exponent in a cumulative `N(sigma,T)` bound is now a saturated variant unless accompanied by an explicit DifferenceWitness showing how the new result crosses the zero-occupancy threshold.

## 7. Failure classification

- **Primary:** `math` — the selected current theorems are mathematically too weak for the stated standalone root implication.
- **Secondary:** `representation` — cumulative density does not preserve the exact zero-occupancy coordinate needed by RH.
- **Not diagnosed as:** retrieval, source, provenance, verification, tooling, gluing, or meta-policy failure.

No root proof DAG node is closed by this negative result.