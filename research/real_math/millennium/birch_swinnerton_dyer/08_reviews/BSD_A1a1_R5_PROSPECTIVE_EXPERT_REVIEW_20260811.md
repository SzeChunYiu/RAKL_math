# BSD A1a1 R5 — prospective expert-cell review

**Cycle:** `BSD-A1a1-BASECHANGE-PLECTIC-20260811-R5`  
**Active canonical atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**RAKL_math base:** `47f56df0492339097a651d40b6c7289c4e2d4034`  
**Durable fibre-freeze commit:** `0c87fcdf33c4755d07cd26affe2e7fcebc7981a4`  
**Fibre content hash:** `sha256:0738fbeff600a8025d89c0d0c215272768e23133d2291e0cbb29734d08f1ecf2`  
**Framework source of truth at freeze:** `SzeChunYiu/RAKL@3863b4814e0020e72c8681727357eda1aab7bf2b`, method `3.0.0`.  
**Authority:** proposal/shadow search planning only; same-context expert cell; independent mathematical review credit `0`.

## Why this action is different from R4

R4 normalized the missing theorem cell to a number-field, weight-two, complex-second-derivative arithmetic bridge. The plectic route audited in R3, however, is naturally formulated over an imaginary quadratic field `K` and assumes an even analytic rank for `E/K`. Before searching again for a direct `E/Q` second-derivative formula, R5 tests whether the exact complex `s`-order can be transported into the plectic ambient theory by a quadratic base change with a nonvanishing complementary twist. This preserves the complex `s` coordinate rather than replacing it by a Hida, anticyclotomic, or other p-adic deformation coordinate.

Exploratory source scouting that occurred before this durable review is motivating evidence only and receives no prospective-discovery credit. The following discriminator is frozen before the targeted verification/search.

## Seven-role same-context expert cell

1. **Complex L-functions / automorphic base-change lead.** Verify the exact factorization for quadratic base change and the Taylor-order calculation. Reject any formula that quietly changes the analytic coordinate or normalization.
2. **Quadratic-twist nonvanishing lead.** Verify the strongest applicable nonvanishing theorem for central quadratic twists, especially whether finite local behavior can be prescribed. Separate existence of a nonzero twist from compatibility with the plectic local pattern.
3. **Plectic / Shimura-curve local-conditions lead.** Type-check the imaginary quadratic `K`, inert/split conductor decomposition, root number, multiplicative prime `p`, and quaternionic embedding hypotheses in the exact source family. Flag sign-parity incompatibilities before using a nonvanishing theorem.
4. **Euler-system / Selmer lead.** Audit what mock-plectic or generalized-Kato nonvanishing proves downstream and forbid reversing one-way implications or importing Selmer rank two as an input.
5. **Heights / regulator / full-BSD lead.** Track what remains after any rank-order transfer: Mordell–Weil rank over `Q`, regulator identity, Sha finiteness/order, real period, Tamagawa/local factors, torsion, and descent from `K` to `Q`.
6. **Adversarial gluing lead.** Run counterexample-first checks on local-vs-global logic. A valid base-change order lemma is only a local relation success; it does not glue automatically to plectic nonvanishing or to the full BSD leading term.
7. **RAKL v3 / provenance / metrology lead.** Enforce TaskEpisode shadow authority, episode→diagnosis→failure/obstruction separation, memory selection/rejection accounting, seven saturation axes, canonical `method_specs.py` surface names, and explicit `CANNOT_MEASURE` fields.

All seven roles share the same model/context and therefore count as same-context review only.

## Prospectively frozen discriminator

For an elliptic curve `E/Q` with exact complex analytic rank two, test the following chain in order:

```text
ord_{s=1} L(E,s)=2
  + choose imaginary quadratic K with required finite local behavior
  + L(E^K,1) != 0
      |
      v
ord_{s=1} L(E/K,s)=2 and exact complex second derivative remains nonzero
      |
      v
? proved complex-second-derivative/nonvanishing bridge to mock-plectic or plectic arithmetic data
      |
      v
? same-theory Mordell-Weil/regulator/Sha/Tamagawa/torsion gluing back to BSD over Q
```

The first arrow is accepted only if the base-change factorization and the local-condition-compatible twist existence are source-bound or explicitly conditional. The second and third arrows are audited separately.

### Cheapest falsifiers

- The plectic source's local sign pattern may force a twist sign inconsistent with central nonvanishing.
- A quadratic-twist theorem may prove infinitely many nonzero central values but not with the finite local specifications needed to land in the plectic source family.
- The base-change identity may be valid only for a differently normalized L-function; exact order and Taylor coefficient must be checked at `s=1`.
- A purported downstream bridge may concern a p-adic/Hida derivative, not the complex `s` derivative.
- A source may assume `rank E(Q)=2`, Selmer rank two, finite Sha, p-adic BSD, or an equivalent arithmetic-strength premise.

## Decision policy

If finite-local-condition-compatible nonvanishing is verified, record a scoped compositional/transfer lemma for the exact complex-order transport and then test the next plectic arrow. If only unconditional/non-local-prescribed nonvanishing is verified, keep the local K-selection compatibility as an explicit residual rather than asserting existence. If sign parity blocks the target local pattern, record that as a local mathematical/source-interface obstruction and rotate the plectic setup. In all cases, preserve the later Mordell–Weil/regulator/Sha/Tamagawa/torsion step as a separate local-to-global/gluing obligation.

## Memory routing effect

Selected prior experience `EP-BSD-A1A1-COMPLEX-HIGHER-GZ-20260811-R4` prevents another overloaded “higher Gross–Zagier” search; `EP-BSD-A1A1-PLECTIC-BRIDGE-20260811-R3` supplies the richer target representation; `T-XM-ROOT-BRIDGE-STABILITY-AUDIT` supplies the coordinate/interface audit; `F-XM001-POINTWISE-GAP-COLLAPSE` blocks promotion from a coordinate-near statement to exact root information. The arbitrary-rank Kurihara/Taylor lane and another scalar theta-order scan are retrieved but rejected for this cycle because they do not test the smallest reopened relation/path coordinate.
