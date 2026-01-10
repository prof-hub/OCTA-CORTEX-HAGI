"""Symmetry monitoring utilities for OCTA-CORTEX-HAGI."""

from __future__ import annotations

import itertools
from typing import Sequence

import numpy as np

_AXIS_PAIRS = [(0, 1), (2, 3), (4, 5)]  # (V1,V2), (V3,V4), (V5,V6)


def octahedral_permutations(full_oh: bool = True) -> list[np.ndarray]:
    """
    Generate permutations acting on the 6D vertex-activation vector [V1..V6].

    - If full_oh=True: returns 48 permutations (axis permutations * within-axis swaps).
      This matches O_h (rotations + reflections) as a conservative symmetry set.
    - If full_oh=False: returns 24 permutations approximating proper rotations only.
      (We restrict by parity of the induced 3D signed permutation; see note below.)
    """
    perms: list[np.ndarray] = []

    for axis_perm in itertools.permutations([0, 1, 2]):  # 3! = 6
        for flips in itertools.product([0, 1], repeat=3):  # 2^3 = 8
            # Build mapping by selecting which pair goes where, and whether it is flipped.
            mapping = []
            for out_axis in axis_perm:
                a, b = _AXIS_PAIRS[out_axis]
                if flips[out_axis]:
                    mapping.extend([b, a])
                else:
                    mapping.extend([a, b])

            perm = np.array(mapping, dtype=int)

            if not full_oh:
                # Optional restriction to 24 (proper rotations):
                # A practical proxy: require an even number of flips when axis_perm parity is odd,
                # so the induced signed permutation has determinant +1.
                # (This is a standard way to separate O from O_h in signed-permutation representations.)
                axis_parity = _permutation_parity(axis_perm)  # 0 even, 1 odd
                flip_parity = sum(flips) % 2
                if (axis_parity ^ flip_parity) != 0:
                    continue

            perms.append(perm)

    # Deduplicate just in case
    uniq = []
    seen = set()
    for p in perms:
        t = tuple(p.tolist())
        if t not in seen:
            seen.add(t)
            uniq.append(p)
    return uniq


def _permutation_parity(p: Sequence[int]) -> int:
    """Return 0 for even permutation, 1 for odd permutation."""
    inv = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            inv += int(p[i] > p[j])
    return inv % 2


def symmetry_deviation(state: np.ndarray, full_oh: bool = True) -> float:
    """
    Compute S(t) as the max deviation over the chosen octahedral permutation set.
    """
    state = np.asarray(state, dtype=float)
    if state.shape != (6,):
        raise ValueError(
            "state must be a 6D vector ordered as [V1, V2, V3, V4, V5, V6]"
        )

    deviations = []
    for perm in octahedral_permutations(full_oh=full_oh):
        rotated = state[perm]
        deviations.append(np.linalg.norm(state - rotated))

    return float(max(deviations)) if deviations else 0.0
