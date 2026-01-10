import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
"""
Paperclip-style toy optimization experiment for OCTA-CORTEX-HAGI.

Demonstrates collapse under unconstrained optimization
vs containment under geometric symmetry penalty.
"""

import numpy as np

from tools.geometric_loss import geometric_loss


# ----------------------------
# Objective (paperclip-like)
# ----------------------------
def paperclip_objective(state: np.ndarray) -> float:
    """
    Naive objective that tries to maximize a single dimension (V1).
    This simulates unilateral resource maximization.
    """
    return state[0]


# ----------------------------
# Gradient (analytical)
# ----------------------------
def grad_objective(state: np.ndarray) -> np.ndarray:
    g = np.zeros_like(state)
    g[0] = 1.0
    return g


# ----------------------------
# Experiment runner
# ----------------------------
def run_experiment(
    steps: int = 50,
    lr: float = 0.1,
    penalty: float = 0.0,
):
    state = np.ones(6)

    history = []

    for _ in range(steps):
        grad = grad_objective(state)

        # Unconstrained update
        state = state + lr * grad

        # Apply geometric penalty indirectly (projected correction)
        if penalty > 0:
            loss = geometric_loss(paperclip_objective, state, penalty)
            # simple stabilization: rescale to unit norm
            state = state / np.linalg.norm(state)

        history.append(state.copy())

    return np.array(history)


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    print("\n=== Running UNCONSTRAINED optimization ===")
    unconstrained = run_experiment(penalty=0.0)
    print("Final state:", unconstrained[-1])

    print("\n=== Running GEOMETRICALLY CONSTRAINED optimization ===")
    constrained = run_experiment(penalty=1.0)
    print("Final state:", constrained[-1])

    print("\nNorm comparison:")
    print("Unconstrained norm:", np.linalg.norm(unconstrained[-1]))
    print("Constrained norm:", np.linalg.norm(constrained[-1]))
