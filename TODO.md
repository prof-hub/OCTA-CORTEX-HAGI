
# TODO — OCTA-CORTEX-HAGI (Repository Audit: 11 Jan 2026)

## Immediate / Short-term

✅ Populate `diagrams/` with high-quality SVGs

- octahedron_structure.svg, axis_labeling.svg, deformation_examples.svg

✅ Implement core computational tools in `tools/`

- symmetry_monitor.py (S(t), energy normalization)
- geometric_loss.py (loss wrapper)
- __init__.py

✅ Create initial toy experiment in `experiments/`

- paperclip_toy.py
- __init__.py

🟡 docs/containment-proofs.md, docs/glossary.md, docs/invariants.md

- Present but content needs clarification/completion

⬜ Add supporting formal documents to `docs/`

- group_theory.md (octahedral group Oₕ basics and representations)
- metric_derivation.md (detailed derivation of S(t), D(t), energy constraint)

## Mid-term

⬜ docs/formal_proofs.md (formal theorems, explicit assumptions)

⬜ experiments/adversarial_tests.ipynb (mesa-optimization, symmetry spoofing, failure modes)

## Needs Clarification

🟡 Additional experiments or notebooks beyond paperclip_toy.py — clarify scope
🟡 Full completion and review of all files in docs/ — clarify completeness
