# BSD A1a2 R14 prospective same-context expert review

Authority: `PROPOSAL_SHADOW_ONLY`. Independent mathematical-review credit: `0/3`.

Frozen atom: `BSD-A1a2-EXACT-SELMER-DIMENSION-KURIHARA-ORDER-BRIDGE`. The current stored input is the R9+R12 lower bound `ord_{s=1}L(E,s)=2 -> dim_Qp H^1_f(Q,V_pE)>=2` under the exact Zhang hypotheses. The cycle tests whether the current Kim-Pollack discrete/Kurihara theorem cell supplies the missing exact upper bound/equality without importing it.

## Expert cell

### Analytic L-functions / modularity lead
Background: complex L-functions of modular elliptic curves, functional equations, Taylor order, modular symbols.

Finding: preserve the exact complex coordinate `ord_{s=1}L(E,s)=2`. A theorem about modular-symbol/Kurihara order is not automatically an analytic-order theorem. Low-rank `rk0`/`rk1` entry statements are useful controls but cannot be extrapolated to rank two.

Delegated check: search the primary Kim-Pollack manuscript for an explicit complex-rank-two -> Kurihara-order-two theorem, inequality, or corollary; reject analogy or parity as insufficient.

### Arithmetic geometry / Selmer-Euler-system lead
Background: Bloch-Kato Selmer groups, Kato Euler systems, Kolyvagin systems, Mordell-Weil/Sha interfaces.

Finding: Theorem 1.1 appears highly relevant downstream because it determines Selmer corank/module structure from Kurihara data. The exact input hypothesis and coefficient module must be retained. Do not infer Mordell-Weil rank or Sha finiteness merely from the p-Selmer coordinate.

Delegated check: bind the theorem's exact corank formula and all hypotheses; separate the exact-Selmer subproblem from later Mordell-Weil/Sha/regulator/Tamagawa/torsion/period gluing.

### p-adic Iwasawa / Kurihara-number lead
Background: cyclotomic Iwasawa theory, modular symbols, augmentation-local main conjectures, Kurihara numbers.

Finding: the source's stated strength is that discrete Kolyvagin derivatives can determine exact Selmer rank while being insensitive to analytic rank. This is precisely why the complex-to-discrete calibration is load-bearing rather than automatic.

Delegated check: inspect Theorem 1.2, parity applications, computational upper-bound statements, and Section 7 quantitative conjectures. Determine whether any exact relation with complex Taylor order is proved or only conjectural/analogical.

### Local-global / gluing lead
Background: local conditions, coefficient changes, p-localization, compatibility of theorem cells.

Finding: R12 already closes the p-infinity/V_p coefficient coordinate. Exact Selmer dimension and transverse p-local localization are distinct gluing obligations. Even a successful exact-rank theorem cell must not be advertised as a localization theorem.

Delegated check: verify same curve, same prime/local-condition compatibility with R12 and record any extra prime/local hypotheses. Keep local theorem validity separate from root-facing gluing.

### Adversarial falsification lead
Background: hostile examples, theorem-direction audits, premise-reimport detection.

Finding: cheapest falsifiers are (i) parity-only information with possible ranks 2,4,6; (ii) a theorem whose premise already includes exact Selmer/algebraic rank; (iii) numerical Kurihara order for individual curves; or (iv) a discrete/complex analogy with no proved transition. Any of these defeats strict root transport.

Delegated check: look first for those failure patterns before investing in composition.

### Formal methods / specification lead
Background: statement binding, dependency DAGs, quantifier and assumption audits.

Finding: the R14 candidate is not a new theorem. At most it can be a stored/compositional theorem path. The proof DAG must keep arrows separate:
`complex order 2 -> ? discrete order 2 -> exact Selmer dimension 2`, then separately localization and BSD leading-term glue.

Delegated check: record exact theorem/corollary numbers and no-go branches; root promotion remains forbidden.

### Novelty / research-value lead
Background: prior-art search, representation novelty, information-gain routing.

Finding: R11 already identified a generic complex-vs-Kurihara exact-order residual, so rediscovering that residual is zero novelty. A genuinely stronger contribution would be source-binding the 2025/2026 Kim-Pollack direct same-Q exact-rank theorem cell and showing exactly which edge of the R11 residual it closes and which edge remains.

Delegated check: search RAKL_math for arXiv:2505.09121/refined Tamagawa-number evidence before claiming a new application-state relation.

## Joint decision

Proceed with `SEARCH` in the same-domain Kim-Pollack theorem cell. Do not invoke `JUMP`, `GLUE`, or `LIFT` unless direct theorem-direction accounting is complete. The predeclared success discriminator is an explicit theorem transporting complex analytic order two to Kurihara/discrete order two or directly to exact Selmer dimension two under non-root-strength hypotheses. The predeclared failure discriminator is that the exact Selmer formula begins from an independently supplied discrete order/nonvanishing and only parity/analogy/computational information links back to complex analytic order.

Strongest objection: a discrete exact-rank theorem can look like the missing BSD upper bound while merely changing the coordinate in which the unknown rank is encoded. Treat this as a representation/gluing risk until an order-preserving transition is source-bound.

Unresolved uncertainty at freeze: whether Section 7 contains a proved complex/discrete order comparison stronger than parity. This is the next source discriminator.
