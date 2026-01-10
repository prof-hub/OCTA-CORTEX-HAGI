"""Geometric loss wrapper for OCTA-CORTEX-HAGI."""

from __future__ import annotations

import os
import sys
from typing import Callable

import numpy as np

# Allow running as script by fixing import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.symmetry_monitor import symmetry_deviation


def geometric_loss(
    objective: Callable[[np.ndarray], float],
    state: np.ndarray,
    lambda_: float = 1.0,
) -> float:
    """
    Compute a scalar loss as:

        L(s) = objective(s) + lambda_ * S(s)^2

    where S(s) is the octahedral symmetry deviation.

    Args:
        objective: Function mapping state -> scalar objective value.
        state: 6D state vector ordered as [V1, V2, V3, V4, V5, V6].
        lambda_: Non-negative penalty coefficient.

    Returns:
        Scalar loss value.

    Notes:
        - Framework-agnostic (NumPy).
        - Penalizes geometric asymmetry.
    """
    if lambda_ < 0:
        raise ValueError(
            "lambda_ must be >= 0 (negative values would reward asymmetry)."
        )

    state = np.asarray(state, dtype=float)
    if state.shape != (6,):
        raise ValueError(
            "state must be a 6D vector ordered as [V1, V2, V3, V4, V5, V6]"
        )

    base = float(objective(state))
    s = float(symmetry_deviation(state))
    return base + lambda_ * (s**2)


# ---------------------------------------------------------------------
# Manual sanity check
# ---------------------------------------------------------------------
if __name__ == "__main__":

    def dummy_objective(s: np.ndarray) -> float:
        return float(np.sum(s))

    s1 = np.ones(6)
    s2 = np.array([2, 0, 1, 1, 1, 1])

    print("geometric_loss(np.ones(6)) =", geometric_loss(dummy_objective, s1))
    print(
        "geometric_loss([2,0,1,1,1,1]) =",
        geometric_loss(dummy_objective, s2),
    )
