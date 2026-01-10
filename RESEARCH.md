# RESEARCH.md — Open Questions and Research Roadmap

## Overview

OCTA-CORTEX-HAGI is a **conceptual framework** at an early stage.  
The core idea — geometric containment of invariants via octahedral symmetry — is defined with rigor in ARCHITECTURE.md, but many aspects remain theoretical.

This document collects:
- Explicitly acknowledged open problems
- Testable hypotheses
- Prioritized research directions
- Validation roadmap

Contributions that preserve the geometric invariants are welcome (see CONTRIBUTING.md).

---

## Open Research Questions

1. **Embedding Geometric Metrics in High-Dimensional Spaces**  
   How to enforce Euclidean octahedral constraints in transformer embeddings or latent spaces without prohibitive computational overhead?  
   Possible approaches: constrained positional encodings, symmetry-equivariant layers, metric-learning wrappers.

2. **Scalability and Computational Cost**  
   Real-time symmetry monitoring (S(t), D(t)) adds overhead.  
   What is the empirical cost at scale (e.g., 7B–70B models)?  
   Can symmetry checks be approximated efficiently (e.g., sampling subset of Oₕ rotations)?

3. **Resistance to Adversarial Training and Mesa-Optimization**  
   Can gradient-based adversaries learn to spoof symmetry metrics (higher-order attacks)?  
   Are there deceptive alignments that preserve octahedral form while pursuing misaligned objectives?

4. **Formal Proofs of Containment**  
   The partial sketches in ARCHITECTURE.md need completion:  
   - Prove that certain classes of extincionist objectives are unreachable under the metric.  
   - Formalize “anti-paperclip” property using constrained optimization theory.

5. **Recursion and Multi-Scale Symmetry**  
   Sub-octahedra inheritance works in theory.  
   How does symmetry propagation behave across many recursive layers?  
   Risk of symmetry drift at depth?

6. **Interpretability and Debugging**  
   Geometric deformation is detectable, but can it be meaningfully projected to human-interpretable explanations?

---

## Testable Hypotheses

| Hypothesis | Description | Validation Method |
|------------|-------------|-------------------|
| H1 | Symmetry penalty reduces incidence of deceptive alignment in toy models | Train small models with/without geometric loss; measure capability vs alignment |
| H2 | Octahedral constraint prevents paperclip-type divergence faster than scalar reward shaping | Instrumented RL environments (e.g., Procgen variants) |
| H3 | Human-centered axis mapping outperforms generic cognitive axes in alignment stability | Ablation studies swapping axis labels |
| H4 | Monitoring overhead is sub-linear with careful rotation sampling | Benchmark on GPU clusters |

---

## Research Roadmap (Prioritized)

### Phase 1 — Prototyping (0–6 months)
- Implement minimal proof-of-concept in PyTorch (symmetry loss wrapper)
- Toy environments for H1 and H2
- Public release of prototype code

### Phase 2 — Formalization (6–18 months)
- Complete proofs using group theory and convex optimization
- Publish pre-print(s)
- Independent audit of containment claims

### Phase 3 — Scaling Experiments (18+ months)
- Integration attempts with medium-scale models
- Adversarial robustness testing
- Collaboration with alignment research groups

### Phase 4 — Community Extension
- Standardized benchmark suite for geometric alignment methods
- Extensions preserving core invariants (e.g., hybrid geometries)

---

## Related Work (Non-Exhaustive)

- Corrigibility and interruptibility (Soares et al., 2015)
- Quantilization (Taylor et al., 2016)
- Value space shaping and Pareto improvements (Armstrong & Mindermann, 2018)
- Equivariant networks and geometric deep learning (Cohen & Welling, 2016 onward)
- Topological approaches to alignment (ongoing independent research)

No claim of superiority — only of a distinct structural approach.

---

## Final Note

Progress depends on rigorous testing, not conceptual elegance alone.  
Any contribution that weakens the geometric invariants will be rejected.  
The goal is not to build AGI here, but to explore whether geometry can make unsafe optimization **structurally impossible**.

Issues and pull requests welcome.
```
