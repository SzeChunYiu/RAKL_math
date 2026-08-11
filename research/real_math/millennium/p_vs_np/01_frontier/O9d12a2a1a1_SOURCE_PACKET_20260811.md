# O9d12a2a1a1 source packet — source-native closure propagation

**Atom:** `O9d12a2a1a1`  
**Authority:** `PRE_CANDIDATE_SOURCE_CONTEXT / NO_MATHEMATICAL_CANDIDATE / ROOT_AUTHORITY_NONE`

## Primary source: Cavalar–Oliveira

Bruno P. Cavalar and Igor C. Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033 (2025).

The source defines semi-filters, pair preservation, and cover complexity, then proves a fusion upper bound. In the proof of Theorem 24, for a fixed integral cover family

`Lambda = {(H_1,E_1),...,(H_t,E_t)}`

and witness `w`, it constructs the **minimal family `G_w subseteq P(U)`** forced into any semi-filter above `w` that preserves `Lambda`.

Source rules:

1. **Seed/upward rule.** If `w in B` for generator `B`, put `B intersect U` into `G_w`, together with all supersets inside `U`.
2. **Preservation propagation.** If both `E_i` and `H_i` are in `G_w`, put `E_i intersect H_i` into `G_w`, again together with all supersets.
3. Repeat propagation to a fixed point.

Claim 27 proves that `emptyset in G_w` iff `w in A`. The subsequent construction translates activation of the finite source vocabulary into sets `S_C^j`; the proof notes that at most `t+1` propagation rounds are required because every productive step introduces at least one of the at most `t` intersections `E_i intersect H_i`.

**Scope boundary:** this is an exact representation already present in the source proof. Theorem 24 uses it to prove an **upper** construction `D_intersection(A|B) <= rho(A,B)^2`. Nothing in the source states that closure depth, activation count, ancestry width, or any statistic of `G_w` lower-bounds `rho`.

## Primary analogue: Horn forward propagation

W. F. Dowling and J. H. Gallier, *Linear-time algorithms for testing the satisfiability of propositional horn formulae*, Journal of Logic Programming 1(3):267–284 (1984), DOI `10.1016/0743-1066(84)90014-1`.

The paper formulates Horn satisfiability as a graph/data-flow/pebbling process. This provides an exact **representation language** for monotone premise-to-consequence activation, useful for exposing sharing and ancestry.

**Transfer boundary:** algorithmic efficiency of Horn forward propagation is not a theorem about graph cover complexity or circuit lower bounds.

## Fractional / hierarchy warnings

- Mauricio Karchmer, Eyal Kushilevitz, Noam Nisan, *Fractional Covers and Communication Complexity*, SIAM J. Discrete Math. 8(1):76–92 (1995), DOI `10.1137/S0895480192238482`.
- Eden Chlamtac, Zac Friggstad, Konstantinos Georgiou, *Understanding Set Cover: Sub-exponential Time Approximations and Lift-and-Project Methods*, arXiv:1204.5489 (2012).

These sources justify treating fractional/local-consistency repairs as scoped tools with possible integrality gaps. They do not provide a P-versus-NP lower bound.

## Source-native re-representation chosen for this atom

Represent the finite Theorem-24 closure as an activation object:

- facts: `C in G_w` for source-relevant subsets `C`;
- seed facts: generator traces forced by `w`;
- monotone implications: `C -> C'` for source-relevant supersets `C subseteq C'`;
- binary implications: `E_i AND H_i -> E_i intersect H_i`;
- terminal fact: `emptyset in G_w`.

This representation is selected **before** any invariant is proposed. Its first purpose is to locate exactly what C025 generator signatures forgot and where C010-style reuse can occur.

## Required hostile calibration before candidate generation

1. **C025 projection test:** find whether two states with identical first-order generator-signature information can have different derived closure activation.
2. **C010 multiplexing test:** determine whether derived activation facts are shared across repeated blocks, invalidating additive counting.
3. **C021 upper-first test:** reject closure features that are equally large on a target with a proved cheap unrestricted construction.
4. **C023 compression test:** do not convert closure state to a scalar score until an extremal cheap-object calibration is passed.
5. **C024 correlation test:** keep one integral `Lambda`; do not fall back to independent fractional pair contributions.

Passing these tests would only justify a later fresh candidate atom. It would not establish a lower bound.
