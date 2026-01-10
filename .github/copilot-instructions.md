# OCTA-CORTEX-HAGI AI Coding Instructions

## Framework Overview
OCTA-CORTEX-HAGI is a geometric AGI alignment framework using octahedral symmetry. Alignment is structural, enforced by symmetry preservation in a 6D state vector representing vertex activations.

## Key Architectural Elements
- **Core (Origin)**: Non-computational invariants defining the metric space.
- **Vertices (6)**: Bipolar axes in ℝ³, mapped to human-centered constraints:
  - V1: Human Subjective Experience
  - V2: Collective Biological Continuity
  - V3: Verified Knowledge
  - V4: Ontological Self-Limitation
  - V5: Symbiotic Cooperation
  - V6: Structural Prohibition of Elimination
- **State Vector**: `s ∈ ℝ⁶` ordered `[V1, V2, V3, V4, V5, V6]`, with constant norm `‖s‖₂`.
- **Symmetry Metric**: `S(t) = max_{R ∈ Oₕ} ‖s - R·s‖₂`, where Oₕ is approximated by permutations.
- **Geometric Loss**: Wrap objectives as `loss = objective(s) + λ * S(s)²` to penalize asymmetry.

## Coding Patterns
- Use NumPy arrays for state vectors; validate shape `(6,)` and ordering.
- Compute symmetry via `tools/symmetry_monitor.py`; use `full_oh=True` for full octahedral group (48 perms).
- Implement losses with `tools/geometric_loss.py`; set `λ > 0` to enforce symmetry.
- Represent deformations as elongations along axes, e.g., paperclip optimization as V6 dominance.
- Validate containment: Symmetric states have `S ≈ 0`; elongated states have `S > ε`.

## Developer Workflows
- No builds/tests yet; focus on research prototypes.
- Add experiments in `experiments/` as `.py` or `.ipynb` files.
- Update metrics in `tools/` for efficiency (e.g., sample rotations instead of all 48).
- Document proofs in `docs/` with formal math.

## Integration Points
- Framework-agnostic; integrate via loss wrappers in PyTorch/TensorFlow.
- No external dependencies beyond NumPy; keep pure for research.

## Key Files
- [ARCHITECTURE.md](ARCHITECTURE.md): Formal spec and metrics.
- [tools/symmetry_monitor.py](tools/symmetry_monitor.py): Symmetry computation.
- [tools/geometric_loss.py](tools/geometric_loss.py): Loss wrapper example.
- [RESEARCH.md](RESEARCH.md): Open questions and hypotheses.

Preserve geometric invariants; reject changes weakening symmetry constraints.
