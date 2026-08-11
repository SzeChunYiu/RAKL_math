# BSD A1a1 R5 — quadratic-base-change transport into the plectic ambient theory

**Cycle:** `BSD-A1a1-BASECHANGE-PLECTIC-20260811-R5`  
**Active canonical atom:** `BSD-A1a1-THETA-ORDER-COMPARISON`  
**RAKL_math base:** `47f56df0492339097a651d40b6c7289c4e2d4034`  
**Prospective fibre freeze:** `0c87fcdf33c4755d07cd26affe2e7fcebc7981a4`  
**Prospective expert review:** `ca22f08b98eaffc6d7bbee58a039f6ab30602c3b`  
**Frozen fibre:** `sha256:0738fbeff600a8025d89c0d0c215272768e23133d2291e0cbb29734d08f1ecf2`  
**Current framework at freeze:** `SzeChunYiu/RAKL@3863b4814e0020e72c8681727357eda1aab7bf2b`, method `3.0.0`, package `0.1.0`.  
**Authority:** `SCOPED_COMPOSITIONAL_LOCAL_LEMMA / SOURCE_BOUND_ROUTE_REFINEMENT / PROPOSAL_SHADOW / SAME_CONTEXT_REVIEW_ONLY / ROOT_AUTHORITY_NONE`.

## Why the representation changed

R3 showed that mock-plectic/plectic objects give a richer higher-rank arithmetic representation but leave the root-facing nonvanishing arrow open. R4 then normalized the desired theorem cell to a number-field, weight-two, **complex `s`-derivative order two** arithmetic bridge and rejected p-adic or higher-weight coordinate substitutions.

The plectic target used by Fornea–Gehrmann is naturally formulated over an imaginary quadratic field `K`, whereas the BSD root datum is the complex analytic rank of `E/Q`. R5 therefore tests an earlier typing question before repeating a direct second-derivative search:

```text
exact complex rank two for E/Q
  -> exact complex rank two for E/K in a plectic-admissible auxiliary field
  -> ? nonzero plectic arithmetic object
  -> ? Mordell-Weil/regulator/Sha/local BSD data over Q.
```

This rotation is memory-driven: R4 blocks a fresh overloaded “higher Gross–Zagier” search; R3 supplies the plectic target; the root-bridge diagnostic forces exact-coordinate preservation.

## Scoped local lemma: the complex `s`-coordinate does transport under a nonvanishing complementary twist

Let `K/Q` be quadratic with character `chi_K`, and let `E^K` denote the corresponding quadratic twist. Quadratic base change gives the factorization

```text
L(E/K,s) = L(E,s) L(E^K,s).
```

A current primary-source instance of the automorphic identity is Nelson, *Quadratic Hecke Sums and Mass Equidistribution*, equation (4.2), which writes `L(pi_D,s)=L(pi,s)L(pi tensor chi_D,s)`.

Assume

```text
ord_{s=1} L(E,s) = 2
and
L(E^K,1) != 0.
```

Then the product has exact order two at `s=1`. Moreover, differentiating twice and using `L(E,1)=L'(E,1)=0` gives

```text
L''(E/K,1) = L''(E,1) L(E^K,1) != 0.
```

So the `E/Q` versus `E/K` mismatch is **not intrinsically a complex-coordinate obstruction**. Conditional on selecting an admissible `K` with a nonzero complementary twist value, exact complex rank two transports into the plectic ambient theory without replacing the complex `s` variable by a Hida, anticyclotomic, or other p-adic coordinate.

This is a compositional local lemma using a stored base-change identity plus elementary Taylor algebra. It is not a new deep theorem, does not imply plectic nonvanishing, and does not imply BSD.

## Auxiliary-field selection: strong finite-local-prescription evidence, but exact plectic admissibility is not yet fully bound

Fornea–Gehrmann's exact target setup requires an imaginary quadratic `K` with `p` inert, conductor `N` unramified in `K`, and `N^-` the inert part of `N/p` square-free with an even number of prime factors; they also impose residual representation hypotheses. Their even-parity condition forces `epsilon(E/K)=+1`, so the plectic setup does not have an immediate sign contradiction with an exact even analytic order.

Nelson's Proposition 3.1 explicitly invokes Friedberg–Hoffstein Theorem B to obtain infinitely many quadratic characters with a nonzero central twisted value while prescribing finite local quadratic-character behavior, after reducing the problem to a compatible global root sign. The same primary paper explicitly remarks that negative discriminants could be used, so the nonvanishing mechanism is not restricted in principle to real quadratic fields.

What is **not** yet source-bound is one theorem instantiated exactly as follows for the active target:

```text
for every relevant analytic-rank-two E/Q,
choose an imaginary quadratic K satisfying the exact mock-plectic
inert/split/unramified pattern and all E,p,N^- residual hypotheses,
while also forcing L(E^K,1) != 0.
```

The Friedberg–Hoffstein application strongly supports the finite-local-prescription part, but the current audit does not silently identify Nelson's quaternionic local setup with every Fornea–Gehrmann hypothesis. Residual surjectivity/ramification conditions are properties of `(E,p,N^-)`, not consequences of choosing `K`. Thus the auxiliary-field selection interface is sharply smaller than the old generic representation mismatch but remains open at exact plectic scope.

## Downstream plectic bridge remains missing

After the local transport lemma, the next desired arrow is now cleanly typed:

```text
L''(E/K,1) != 0 with ord_{s=1} L(E/K,s)=2
   -> nonzero mock-plectic / plectic class, point, or regulator determinant.
```

The bounded current primary-source audit still does not locate such a theorem.

- Fornea–Gehrmann prove a strong **downstream** theorem beginning with `Q_K != 0`; nonvanishing is an input rather than an output of the complex analytic rank.
- Fornea 2026 constructs partially global plectic Heegner classes and comparison maps, but the missing complex-rank-to-nonvanishing significance is not supplied by the construction theorem.
- Hernández–Molina and Hernández Barrios–Molina give higher-derivative formulas for Hida–Rankin or anticyclotomic **p-adic** L-functions. Those are valuable plectic formulas but fail the R4 exact-coordinate discriminator.

No literature-wide nonexistence claim is made.

## Local mathematical failure versus gluing failure

These remain separate.

**Local success:** the exact complex rank-two datum can be transported from `E/Q` to `E/K` under a nonvanishing complementary twist by a source-bound factorization and exact Taylor calculation.

**Local/source-interface residual:** source-bind the existence of an auxiliary imaginary quadratic `K` satisfying the exact plectic finite-local and residual conditions together with `L(E^K,1)!=0`, or isolate the precise incompatibility.

**Local arithmetic residual:** prove complex-second-derivative nonvanishing over that same `K` implies nonzero root-faithful plectic arithmetic data without assuming algebraic rank two, Selmer rank two, finite Sha, p-adic BSD, or equivalent-strength arithmetic information.

**Local-to-global/gluing residual:** even a plectic/Selmer success must still be glued back to the exact BSD root over `Q`, including Mordell–Weil rank, regulator, Sha, real period, Tamagawa/local factors, torsion, and the full complex leading term. Nothing in the local base-change lemma performs that descent/gluing.

## Same-context expert-cell result

1. **Complex L/base-change lead:** accepts the product identity and exact second-derivative calculation; rejects any p-adic derivative substitute.
2. **Twist nonvanishing lead:** accepts finite-local-prescription evidence from the explicit Friedberg–Hoffstein application; keeps exact target instantiation open.
3. **Plectic local-conditions lead:** finds no parity contradiction because the source requires even `N^-`; flags residual representation hypotheses as independent of field selection.
4. **Euler-system/Selmer lead:** accepts `Q_K != 0 ->` Selmer information only in the proved direction and blocks reversal.
5. **Heights/regulator/full-BSD lead:** keeps regulator/Sha/Tamagawa/torsion and descent to `Q` separate.
6. **Adversarial gluing lead:** classifies the base-change result as a local relation success, not a root path.
7. **RAKL/provenance/metrology lead:** preserves prefreeze scouting as non-prospective evidence, shadow authority, current-v3 storage semantics, and conservative novelty accounting.

All are role-separated passes in one context; independent review credit remains `0`.

## Outcome and residual transformation

**Before R5**

```text
number field + weight-two + complex second derivative
  -> root-faithful arithmetic object,
with E/Q versus plectic E/K still implicit in the representation mismatch.
```

**After R5**

```text
A. CONDITIONAL LOCAL RELATION CLOSED:
   ord L(E/Q)=2 + L(E^K,1)!=0
     -> ord L(E/K)=2 and L''(E/K,1)!=0.

B. OPEN AUXILIARY-K INTERFACE:
   select/source-bind K satisfying exact plectic local/residual conditions
   and L(E^K,1)!=0.

C. OPEN COMPLEX-TO-PLECTIC ARITHMETIC BRIDGE:
   L''(E/K,1)!=0
     -> nonzero root-faithful plectic arithmetic data.

D. OPEN SAME-THEORY/GLOBAL BSD GLUING:
   plectic/Selmer information
     -> exact Mordell-Weil/regulator/Sha/Tamagawa/torsion/leading term over Q.
```

The scoped solved subproblem is classified `compositional` (with a secondary representation/transfer role). No proof novelty is claimed. No root candidate is generated. Root remains `OPEN_NO_SOLUTION_CERTIFICATE`.

## Next discriminator

Do **not** repeat the scalar theta-order or generic higher-Gross–Zagier scans. First bind the auxiliary-field selection theorem at the exact Fornea–Gehrmann local/residual signature, preferably by specializing Friedberg–Hoffstein with all local characters written explicitly. If that succeeds, immediately test the now clean `complex L''(E/K,1) -> plectic nonvanishing` arrow. If it fails on an exact local/sign/residual incompatibility, rotate the plectic setup rather than weakening the local conditions.
