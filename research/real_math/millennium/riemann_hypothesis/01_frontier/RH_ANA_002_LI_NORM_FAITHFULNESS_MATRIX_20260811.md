# RH-ANA-002 Li-norm faithfulness matrix — 2026-08-11

**Atom:** `RH-ANA-002`  
**Root:** `RAKL_math#3` — Riemann Hypothesis  
**Frozen context:** `sha256:300b787769442af040d944e0b52db106881844a9238c021e8804c7f382660742`  
**Parent strict-packet head:** `10b87a53fa961418954b8da4a480d4abdeadcbb5`  
**Current framework inspected before this audit:** `SzeChunYiu/RAKL@a151d5612709ea0f95c3ea232630f246f722739a`  
**Authority:** `SOURCE_BOUND_DEPENDENCY_AUDIT / NO_MATHEMATICAL_CANDIDATE / NO_RH_EVIDENCE / ROOT_AUTHORITY_NONE`

## Registered discriminator

The frozen pre-candidate trace registered exactly one candidate-free next action: reconstruct the proof dependencies behind Suzuki's Li-norm formulation, classify the transport from the positive norm surrogate to `lambda_n`, and ask whether the **unconditional** layer contains any exact sub-identity, sign statement, orthogonality relation, or source term for

`D_n := (2*pi)^(-1) ||G_n||_2^2 - lambda_n`

that is strictly weaker than the all-index RH-equivalent equality. If not, the route must be recorded as a scoped negative search result and the representation rotated rather than repaired by a new notation-level positivity conjecture.

## Framework freshness delta

The parent packet was frozen against the then-current framework at `15f1c3a...`; current `RAKL@main` is `a151d5612709ea0f95c3ea232630f246f722739a`. The current `AGENTS.md` and `rakl-core` manifest retain the same strict mathematical pre-candidate gates. The new v3 experience substrate adds an important **post-action** discipline: observed outcomes are frozen as immutable `TaskEpisode`s before failure interpretation, and a non-success episode does not by itself establish a causal obstruction. This audit therefore freezes `EP-RH-ANA-002-LI-NORM-AUDIT-20260811` first and projects only an `OBSERVED_ONLY` failure diagnosis afterward.

The GitHub connector exposed no workflow run bound to the framework merge commit at the time of this cycle, so no claim of framework-CI success is made. The application PR adds exact-subject assurance against the observed current framework SHA as a separate check.

## Primary-source dependency matrix

The source boundary is Masatoshi Suzuki, *Li coefficients as norms of functions in a model space*, arXiv:2301.05779v2 (2023), with a current-primary-literature rotation scan including Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096 (2026).

| Ingredient | Source status | What is actually available | Search consequence |
|---|---|---|---|
| `H_n(s)` and `G_n(z)` definitions | `UNCONDITIONAL` | Definitions (1.6)–(1.7) do not assume RH. | A positive analytic surrogate can be formed without RH. |
| Meromorphic zero-sum `M_n(s)` | `UNCONDITIONAL` | Lemma 2.1 gives absolute/uniform convergence on compacta away from zeros. | Zero information is encoded exactly, but not yet as a sign statement. |
| `H_n(s)= i xi(s)/(xi(s)+xi'(s)) M_n(s)` | `UNCONDITIONAL` | Proposition 2.1; its proof uses Weil's explicit formula with explicit convergence handling. | Exact zero/prime duality enters before the model-space step. |
| Boundedness, real-analyticity, `G_n|_R in L^2(R)` | `UNCONDITIONAL` | Proposition 2.2 holds for every positive integer `n`. | `P_n=(2*pi)^(-1)||G_n||_2^2 >= 0` is unconditional. |
| `Theta` is a meromorphic inner function / `E` is Hermite–Biehler | `RH_EQUIVALENT` | Proposition 3.1 makes these conditions equivalent to RH. | The model-space faithfulness coordinate cannot be imported as free analytic structure. |
| Orthonormal basis `{F_gamma}` of `K(Theta)` | `RH_CONDITIONAL` | Proposition 3.2 explicitly assumes RH. | Parseval/orthogonality used in the norm calculation is not an unconditional bridge. |
| Expansion of `G_n` in the zero-ordinate basis and norm evaluation | `RH_CONDITIONAL` | Section 3.4 invokes Proposition 3.2 after assuming RH. | The positive norm is transported to the Li zero-sum only inside the RH-coupled model-space regime. |
| `lambda_n = (2*pi)^(-1)||G_n||_2^2` for all `n>=1` | `RH_EQUIVALENT` | Theorem 1.1 states necessity and sufficiency. | Proving the whole family directly would relabel the root, not localize it. |
| `D_n` as a difference of two well-defined numbers | `UNCONDITIONAL_BOOKKEEPING` | Both terms are individually defined unconditionally. | Defining a defect creates no theorem about its sign, size, or structure. |
| Exact unconditional source formula/sign/orthogonality for `D_n` strictly weaker than RH | `NOT_FOUND_IN_REGISTERED_SOURCE_BOUNDARY` | No such bridge is stated or derived in the inspected 2023 proof boundary; Suzuki notes that other meanings/characterizations of `G_n` were unknown there. | **Do not invent another norm-positivity equivalent inside this saturated representation.** |

## Counterexample-first / circularity checks

1. **Positive-surrogate check.** `P_n >= 0` alone does not imply `lambda_n >= 0`; the missing equality is the whole faithfulness issue.
2. **Model-space check.** Proposition 3.1 identifies the key inner/Hermite–Biehler property with RH, and Proposition 3.2 assumes RH. Importing their consequences unconditionally would be circular.
3. **All-index check.** By Li's criterion, any proposed statement whose only proved effect is `lambda_n >= 0` for every `n` is already root-strength; calling it a “bridge lemma” does not make it smaller.
4. **Finite-data check.** RH-ANA-001 already falsified finite-prefix promotion as a global certificate in its registered symmetric-multiset scope, so no larger finite cutoff is an admissible repair.
5. **Absence-vs-impossibility check.** “Not found in this source route” is **not** “no such theorem exists.” The resulting failure record therefore remains `OBSERVED_ONLY`.

## Current-primary-literature rotation signal

Suzuki's 2026 arXiv:2606.09096 materially changes the representation while remaining unconditional in its proved results: the localized Weil quadratic form is realized through a continuous screw-function kernel and a canonical self-adjoint operator `A_a`; its lowest eigenvalue `lambda_a` is proved continuous in the localization scale `a`. The same paper explains the remaining RH bridge in terms of global nondegeneracy/sign behavior across scale and separately labels its limiting Hilbert–Pólya statement conjectural.

This is **not** a candidate for RH and is not imported into the frozen 2023 norm packet. It is only a high-information representation-rotation target for the next fresh context gate because it exposes a different structural coordinate: scale-localized quadratic-form spectrum rather than a static positive norm surrogate.

## Scoped result

`NO_STRICTLY_WEAKER_BRIDGE_FOUND_WITHIN_REGISTERED_SUZUKI_2023_SOURCE_BOUNDARY`.

What this result **does** establish for search control:

- the registered source audit is complete;
- unconditional `L^2` positivity is not, by itself, the missing transport theorem;
- the inspected proof's exact norm evaluation uses RH-coupled model-space structure;
- repeating the same norm-faithfulness family with new notation is now a saturated search move unless genuinely new unconditional source structure is supplied;
- current primary literature justifies rotating the next context toward localized Weil/prime-side structure.

What it **does not** establish:

- no unconditional `D_n` decomposition exists;
- the Suzuki norm route is mathematically impossible;
- any off-critical zeta zero exists;
- RH is true or false;
- the 2026 operator/screw-function route proves RH.

## Next action

No mathematical candidate is generated in this cycle. The next analytic cycle must reread current framework/application state and freeze a **fresh** context/memory/trace packet around the scale-localized Weil quadratic form / prime-side explicit-formula coordinate before proposing any inequality, coercivity estimate, zero-free mechanism, or scale-propagation theorem.
