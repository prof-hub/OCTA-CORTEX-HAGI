# TODO — OCTA-CORTEX-HAGI

## Immediate (2–4 hours)

- [ ] Populate `diagrams/` with at least 3 high-quality SVGs
  (octahedron structure, axis labeling, deformation examples)

## Short-term (4–48 hours)

- [ ] Add supporting formal documents to `docs/`
  - `group_theory.md` (octahedral group Oₕ basics and representations)
  - `metric_derivation.md` (detailed derivation of S(t), D(t), energy constraint)

## Near-term (1–5 days)

- [ ] Implement core computational tools in `tools/`
  - `symmetry_monitor.py` (compute S(t), energy normalization)
  - `geometric_loss.py` (PyTorch-compatible loss wrapper with penalty S(t)²)
  - Include unit tests and example notebook

- [ ] Create initial toy experiments in `experiments/`
  - `toy_gridworld.ipynb` (simple environment testing paperclip-type divergence)
  - `multi_objective_test.py` (baseline vs geometric constraint comparison)

## Medium-term (5–14 days)

- [ ] Develop prototype optimizer and ablation suite
  - `prototype_optimizer.py` (full constrained optimizer)
  - `results_summary.md` (quantitative tables for hypotheses H1–H3)

- [ ] Formalize containment proofs
  - Create `docs/formal_proofs.md` with complete theorems and lemmas
  - Update ARCHITECTURE.md section 5 references

## Longer-term (2–6 weeks)

- [ ] Conduct adversarial testing
  - `adversarial_tests.ipynb` (mesa-optimization and spoofing attempts)
  - Update RESEARCH.md with findings and refined open questions

- [ ] Expand visual and explanatory materials as needed
  - Additional diagrams, interactive demos (if feasible)

## Ongoing

- [ ] Maintain symmetry with core invariants in all contributions
- [ ] Respond to issues and review pull requests preserving geometric containment
